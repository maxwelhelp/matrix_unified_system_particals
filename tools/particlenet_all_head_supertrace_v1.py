#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced, clean, unwrap
from data.jetclass_tiny_loader_v3_official import LABELS

FEATURE_NAMES={
 'kin':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_deta','part_dphi'],
 'kinpid':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_deta','part_dphi'],
 'full':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_d0','part_d0err','part_dz','part_dzerr','part_deta','part_dphi'],
}

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def table(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rs])+'\n'

def make_model(checkpoint,mode,device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd,strict=False)
    return model,res,input_dims

def split_ranges(C,groups):
    out=[]
    for g in range(groups):
        a=(C*g)//groups; b=(C*(g+1))//groups
        if a<b: out.append((g,a,b))
    return out

def particle_row(batch,mode,ei,pi):
    names=FEATURE_NAMES[mode]
    vals=batch['features'][ei,:,pi].detach().cpu().float().tolist()
    row={n:float(v) for n,v in zip(names,vals)}
    vec=batch['vectors'][ei,:,pi].detach().cpu().float()
    px,py,pz,en=[float(x) for x in vec[:4]]
    pt=(px*px+py*py)**0.5
    deta=float(batch['points'][ei,0,pi].detach().cpu())
    dphi=float(batch['points'][ei,1,pi].detach().cpu())
    dr=(deta*deta+dphi*dphi)**0.5
    row.update({'px':px,'py':py,'pz':pz,'energy':en,'pt':pt,'deta':deta,'dphi':dphi,'deltaR_from_axis':dr})
    return row

def baseline_logits(model,batch):
    with torch.no_grad():
        return model(batch['points'],batch['features'],batch['mask']).detach()

def gated_forward(model,batch,groups):
    gates=[]; meta=[]; captures=[]; hooks=[]
    # First dry shape info from known architecture via hook output at runtime.
    def make_hook(layer_id):
        def hook(m,inp,out):
            C=out.shape[1]
            if len(gates)<=layer_id:
                ranges=split_ranges(C,groups)
                g=torch.ones(len(ranges),device=out.device,requires_grad=True)
                gates.append(g)
                meta.append([(layer_id,gi,a,b) for gi,a,b in ranges])
            z=out
            energies=[]
            for idx,(ly,gi,a,b) in enumerate(meta[layer_id]):
                z_slice=z[:,a:b,:]*gates[layer_id][idx]
                z=z.clone() if idx==0 else z
                z[:,a:b,:]=z_slice
                energies.append(torch.sqrt((out[:,a:b,:].detach().float()**2).sum(dim=1)+1e-12))
            captures.append({'layer':layer_id,'energies':energies,'shape':tuple(out.shape)})
            return z
        return hook
    for i,conv in enumerate(model.edge_convs):
        hooks.append(conv.register_forward_hook(make_hook(i)))
    logits=model(batch['points'],batch['features'],batch['mask'])
    for h in hooks: h.remove()
    flat_meta=[]; flat_gates=[]
    for li,m in enumerate(meta):
        for idx,item in enumerate(m):
            flat_meta.append(item); flat_gates.append(gates[li][idx])
    return logits,flat_gates,flat_meta,captures

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=64)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--head-groups',type=int,default=8)
    ap.add_argument('--top-events',type=int,default=30)
    ap.add_argument('--top-particles',type=int,default=10)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_all_head_supertrace_v1')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    base=baseline_logits(model,batch); pred=base.argmax(-1); y=batch['y']; prob=F.softmax(base.float(),-1)
    model.zero_grad(set_to_none=True)
    logits,gates,meta,captures=gated_forward(model,batch,args.head_groups)
    obj=logits.gather(1,pred[:,None]).mean()
    obj.backward()
    grads=[]
    for i,g in enumerate(gates):
        grad=float(g.grad.detach().cpu()) if g.grad is not None else 0.0
        ly,gi,a,b=meta[i]
        grads.append({'layer':ly,'group_id':gi,'channels':f'ch{a}:{b}','grad':grad,'abs_grad':abs(grad),'positive_grad':max(0.0,grad),'head_id':f'L{ly}_ch{a}:{b}'})
    grads_sorted=sorted(grads,key=lambda r:r['abs_grad'],reverse=True)
    # build all-head particle score from positive gradients; if all nonpositive, use abs gradients
    weight_by=(lambda r:r['positive_grad'])
    if sum(weight_by(r) for r in grads)<1e-12:
        weight_by=lambda r:r['abs_grad']
    B,N=batch['mask'].shape[0],batch['mask'].shape[-1]
    super_score=torch.zeros(B,N,device=args.device)
    head_event_rows=[]
    # captures order can contain one per layer
    grad_lookup={(r['layer'],r['group_id']):weight_by(r) for r in grads}
    for cap in captures:
        ly=cap['layer']
        for gi,energy in enumerate(cap['energies']):
            w=grad_lookup.get((ly,gi),0.0)
            if w==0: continue
            en=energy.detach().float()
            en=en/(en.amax(dim=1,keepdim=True)+1e-9)
            super_score += w*en
    real_mask=batch['mask'][:,0,:].detach().bool()
    super_score=super_score.masked_fill(~real_mask,-1)
    event_score=super_score.max(dim=1).values
    top_e=torch.topk(event_score,min(args.top_events,event_score.numel())).indices.detach().cpu().tolist()
    event_rows=[]; particle_rows=[]
    for ei in top_e:
        real_n=int(real_mask[ei].sum().detach().cpu())
        pe=super_score[ei]
        idx=torch.topk(pe,min(args.top_particles,real_n)).indices.detach().cpu().tolist()
        event_rows.append({'event_idx':ei,'true':int(y[ei]),'true_label':LABELS[int(y[ei])],'pred':int(pred[ei]),'pred_label':LABELS[int(pred[ei])],'conf':float(prob[ei,pred[ei]].detach().cpu()),'pred_logit':float(base[ei,pred[ei]].detach().cpu()),'super_max_particle_score':float(pe.max().detach().cpu()),'real_particles':real_n,'top_particle_indices':json.dumps(idx)})
        for rank,pi in enumerate(idx,1):
            pr=particle_row(batch,args.mode,ei,pi)
            row={'event_idx':ei,'rank':rank,'particle_idx':pi,'super_score':float(super_score[ei,pi].detach().cpu()),'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'conf':float(prob[ei,pred[ei]].detach().cpu())}
            row.update(pr); particle_rows.append(row)
    class_rows=[]
    for c,lbl in enumerate(LABELS):
        m=(pred==c)
        if int(m.sum())==0: continue
        vals=event_score[m]
        class_rows.append({'pred_label':lbl,'n_pred':int(m.sum().cpu()),'super_score_mean':float(vals.mean().detach().cpu()),'super_score_p90':float(torch.quantile(vals.float(),0.9).detach().cpu()),'acc_within_pred':float((y[m]==pred[m]).float().mean().detach().cpu())})
    wcsv(out/'tables/all_head_gate_gradients.csv',grads_sorted)
    wcsv(out/'tables/all_head_supertrace_events.csv',event_rows)
    wcsv(out/'tables/all_head_supertrace_particles.csv',particle_rows)
    wcsv(out/'tables/all_head_supertrace_class_summary.csv',class_rows)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'n_events':int(y.numel()),'baseline_acc':float((pred==y).float().mean().detach().cpu()),'objective_pred_logit_mean':float(obj.detach().cpu()),'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'top_heads_by_abs_grad':grads_sorted[:20],'top_events':event_rows[:10],'class_summary':class_rows}
    wjson(out/'all_head_supertrace_summary.json',summary)
    md=['# ParticleNet All-Head Differentiable Supertrace v1\n\n',
        f"n_events={summary['n_events']} baseline_acc={fmt(summary['baseline_acc'])} objective_pred_logit_mean={fmt(summary['objective_pred_logit_mean'])}\n\n",
        'This treats all EdgeConv pseudo-head groups as differentiable gates and backpropagates the predicted-class logit through them. It is the all-head analogue of token/particle tracing.\n\n',
        '## Top differentiable head gates\n',
        table(['rank','head','grad','abs_grad','channels'],[[i+1,r['head_id'],fmt(r['grad']),fmt(r['abs_grad']),r['channels']] for i,r in enumerate(grads_sorted[:30])]),
        '\n## Class summary by predicted class\n',
        table(['pred_label','n_pred','super_mean','super_p90','acc_within_pred'],[[r['pred_label'],r['n_pred'],fmt(r['super_score_mean']),fmt(r['super_score_p90']),fmt(r['acc_within_pred'])] for r in class_rows]),
        '\n## Top events by all-head super-score\n',
        table(['event','true','pred','conf','super_max','real_particles','top_particle_indices'],[[r['event_idx'],r['true_label'],r['pred_label'],fmt(r['conf']),fmt(r['super_max_particle_score']),r['real_particles'],r['top_particle_indices']] for r in event_rows[:40]]),
        '\n## Top particles inside top events\n',
        table(['event','rank','particle','super_score','pt','energy','deta','dphi','deltaR','charge','pred'],[[r['event_idx'],r['rank'],r['particle_idx'],fmt(r['super_score']),fmt(r.get('pt')),fmt(r.get('energy')),fmt(r.get('deta')),fmt(r.get('dphi')),fmt(r.get('deltaR_from_axis')),fmt(r.get('part_charge','')),r['pred_label']] for r in particle_rows[:100]]),
        '\nFull CSV tables:\n- `reports/latest/tables/all_head_gate_gradients.csv`\n- `reports/latest/tables/all_head_supertrace_events.csv`\n- `reports/latest/tables/all_head_supertrace_particles.csv`\n- `reports/latest/tables/all_head_supertrace_class_summary.csv`\n']
    (out/'PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()

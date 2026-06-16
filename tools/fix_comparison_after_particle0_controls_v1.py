#!/usr/bin/env python3
import csv, json, argparse
from pathlib import Path
from datetime import datetime, timezone


def fnum(x, default=0.0):
    try:
        if x is None or x == '': return default
        return float(x)
    except Exception:
        return default

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def wcsv(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows:
            wr.writerow({k:r.get(k,'') for k in keys})

def loadjson(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def wjsonl(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r,ensure_ascii=False)+'\n')

def md_table(headers,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def row_by_control(rows, name):
    return next((r for r in rows if r.get('control') == name), {})

def random_mean(rows, prefix, key):
    rs=[r for r in rows if r.get('control','').startswith(prefix)]
    if not rs: return 0.0
    return sum(fnum(r.get(key)) for r in rs)/len(rs)

def update_c15(rows):
    missing=[r for r in rows if r.get('priority')=='P0' and str(r.get('status','')).startswith(('NEEDS','MISSING','CANDIDATE'))]
    for r in rows:
        if r.get('comparison_id')=='C15_DISCOVERY_READINESS_SCORE':
            r['support_signal']=f"p0_missing_count={len(missing)} readiness=method_debug"
            r['missing_control']=', '.join(x.get('comparison_id','') for x in missing[:8])
            r['status']='METHOD_DEBUG_NOT_DISCOVERY_READY' if missing else 'RESIDUAL_CANDIDATE_READY'
            r['evidence_json']=json.dumps({'missing_p0':[x.get('comparison_id') for x in missing]},ensure_ascii=False)
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rows',default='reports/latest/tables/automatic_comparison_rows_v2.csv')
    ap.add_argument('--json',default='manifests/latest/automatic_comparison_engine_v2.json')
    ap.add_argument('--dataset',default='reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl')
    ap.add_argument('--md',default='reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md')
    ap.add_argument('--controls',default='reports/latest/tables/particle0_topk_control_summary_v2.csv')
    args=ap.parse_args()
    rows=readcsv(args.rows)
    controls=readcsv(args.controls)
    if not rows or not controls:
        print(json.dumps({'ok':False,'reason':'missing rows or controls','rows':len(rows),'controls':len(controls)},indent=2))
        return
    rem0=row_by_control(controls,'remove_particle0')
    keep0=row_by_control(controls,'keep_only_particle0')
    rand_drop=random_mean(controls,'random_remove1_','acc_drop_from_baseline')
    rand_flip=random_mean(controls,'random_remove1_','pred_flip_rate')
    ratio=(fnum(rem0.get('acc_drop_from_baseline'))/max(1e-9,rand_drop)) if rem0 else 0.0
    for r in rows:
        if r.get('comparison_id')=='C1_STREAM_RELATION_VS_MISSING_CONTROL':
            r['support_signal']=(
                f"particle0 control available: remove_particle0_acc_drop={fmt(rem0.get('acc_drop_from_baseline'))}, "
                f"random_remove1_acc_drop_mean={fmt(rand_drop)}, ratio={fmt(ratio)}, "
                f"keep_only_particle0_acc={fmt(keep0.get('acc'))}"
            )
            r['contradiction_signal']='keep_only_particle0 is weak globally, so this is not a pure particle0-only shortcut'
            r['missing_control']='order/residual/class-specific controls'
            r['risk']='particle0 is causally important, but may still be sorting/leading-pT or known-observable proxy'
            r['recommended_next_experiment']='run particle order shuffle, known-observable residual, and class-specific all-head gradients'
            r['status']='SUPPORTED_BY_TARGETED_CONTROL_BUT_NEEDS_ORDER_RESIDUAL_TEST'
            r['training_label']='particle0_targeted_control_supported_order_residual_required'
            r['evidence_json']=json.dumps({'remove_particle0':rem0,'keep_only_particle0':keep0,'random_remove1_acc_drop_mean':rand_drop,'random_remove1_flip_mean':rand_flip,'target_vs_random_drop_ratio':ratio},ensure_ascii=False)
    rows=update_c15(rows)
    prio={'P0':0,'P1':1,'P2':2}
    rows=sorted(rows,key=lambda r:(prio.get(r.get('priority'),9), r.get('comparison_id','')))
    wcsv(args.rows,rows)
    dataset=[]
    for r in rows:
        dataset.append({'schema':'automatic_comparison_training_row.v2.fixed_after_particle0_controls','input':{k:r.get(k,'') for k in ['comparison_id','claim','support_signal','contradiction_signal','missing_control','risk','evidence_json']},'target':{k:r.get(k,'') for k in ['status','priority','training_label','recommended_next_experiment']}})
    wjsonl(args.dataset,dataset)
    out={'schema':'automatic_comparison_engine.v2','generated_at_utc':datetime.now(timezone.utc).isoformat(),'postprocess':'particle0_controls_fix_v1','comparisons':rows,'p0':[r for r in rows if r.get('priority')=='P0'],'next_big_stream_policy':'staged_sampled_large_stream_with_controls'}
    wjson(args.json,out)
    md=['# Automatic Comparison Engine v2\n\n',
        'v2 adds big-stream and discovery-readiness comparisons on top of v1. This report was postprocessed after particle0/top-k controls v2.\n\n',
        '## P0 comparisons\n',
        md_table(['status','comparison','claim','missing','next'],[[r.get('status'),r.get('comparison_id'),r.get('claim'),r.get('missing_control',''),r.get('recommended_next_experiment')] for r in rows if r.get('priority')=='P0']),
        '\n## All comparisons\n',
        md_table(['priority','status','comparison','support','risk'],[[r.get('priority'),r.get('status'),r.get('comparison_id'),r.get('support_signal'),r.get('risk')] for r in rows]),
        '\n## Particle0 control update\n\n',
        f"- remove_particle0 acc_drop: **{fmt(rem0.get('acc_drop_from_baseline'))}**\n",
        f"- random_remove1 acc_drop mean: **{fmt(rand_drop)}**\n",
        f"- targeted/random drop ratio: **{fmt(ratio)}**\n",
        f"- keep_only_particle0 acc: **{fmt(keep0.get('acc'))}**\n\n",
        'Interpretation: particle0/core is targeted-causal, but not sufficient alone globally. Remaining P0: order control, residual, class-specific gradients, heldout.\n\n',
        '## Big-stream policy\n\n',
        'Run staged large streams, but do not claim discovery until order/residual/heldout/cross-model tests pass.\n\n',
        '## Files\n\n',
        f'- JSON: `{args.json}`\n',
        f'- CSV: `{args.rows}`\n',
        f'- Training rows: `{args.dataset}`\n']
    Path(args.md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'patched_C1':True,'target_vs_random_drop_ratio':ratio,'out_json':args.json},indent=2,ensure_ascii=False))

if __name__=='__main__': main()

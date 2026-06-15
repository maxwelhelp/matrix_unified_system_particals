import glob
from pathlib import Path
import awkward as ak
import numpy as np
import torch

LABELS=['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
PART_BASE=['part_px','part_py','part_pz','part_energy','part_deta','part_dphi','part_d0val','part_d0err','part_dzval','part_dzerr','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon']
JET=['jet_pt','jet_energy']

def _as_list_array(a):
    return ak.to_list(a)

def _pad_wrap_array(a,length=128,pad_value=0.0):
    out=[]
    for row in _as_list_array(a):
        row=list(row)
        if len(row)==0:
            out.append([pad_value]*length)
        elif len(row)>=length:
            out.append(row[:length])
        else:
            reps=(length+len(row)-1)//len(row)
            out.append((row*reps)[:length])
    return np.asarray(out,dtype='float32')

def _pad_const_array(a,length=128,pad_value=0.0):
    return ak.to_numpy(ak.fill_none(ak.pad_none(a,length,clip=True),pad_value)).astype('float32')

def _clip_default(x): return np.clip(x,-5,5).astype('float32')
def _manual(x,sub=None,mul=1.0,clip_min=-5,clip_max=5):
    y=x.astype('float32')
    if sub is not None: y=y-sub
    y=y*mul
    if clip_min is not None or clip_max is not None: y=np.clip(y,clip_min if clip_min is not None else -np.inf,clip_max if clip_max is not None else np.inf)
    return y.astype('float32')

def make_features_official(arr,mode='full',length=128):
    # Official YAML: pf_features and pf_vectors use pad_mode=wrap; pf_mask uses pad_mode=constant.
    px=_pad_wrap_array(arr['part_px'],length); py=_pad_wrap_array(arr['part_py'],length); pz=_pad_wrap_array(arr['part_pz'],length); en=_pad_wrap_array(arr['part_energy'],length)
    deta=_pad_wrap_array(arr['part_deta'],length); dphi=_pad_wrap_array(arr['part_dphi'],length)
    pt=np.hypot(px,py); eps=1e-8
    jet_pt=np.asarray(arr['jet_pt'],dtype='float32')[:,None]; jet_e=np.asarray(arr['jet_energy'],dtype='float32')[:,None]
    part_pt_log=np.log(np.maximum(pt,eps)); part_e_log=np.log(np.maximum(en,eps)); part_logptrel=np.log(np.maximum(pt,eps)/np.maximum(jet_pt,eps)); part_logerel=np.log(np.maximum(en,eps)/np.maximum(jet_e,eps)); part_deltaR=np.hypot(deta,dphi)
    feats=[_manual(part_pt_log,1.7,0.7),_manual(part_e_log,2.0,0.7),_manual(part_logptrel,-4.7,0.7),_manual(part_logerel,-4.7,0.7),_manual(part_deltaR,0.2,4.0)]
    if mode in ('kinpid','full'):
        for b in ['part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon']:
            feats.append(_pad_wrap_array(arr[b],length))
    if mode=='full':
        d0=np.tanh(_pad_wrap_array(arr['part_d0val'],length)).astype('float32')
        d0err=_manual(_pad_wrap_array(arr['part_d0err'],length),0,1,0,1)
        dz=np.tanh(_pad_wrap_array(arr['part_dzval'],length)).astype('float32')
        dzerr=_manual(_pad_wrap_array(arr['part_dzerr'],length),0,1,0,1)
        feats += [d0,d0err,dz,dzerr]
    feats += [deta.astype('float32'),dphi.astype('float32')]
    x=np.stack(feats,axis=1).astype('float32')
    v=np.stack([px,py,pz,en],axis=1).astype('float32')
    # mask is part_mask=ones_like(part_energy), pad constant: real particles 1, padded 0.
    real_mask=_pad_const_array(ak.ones_like(arr['part_energy']),length,0.0).astype('bool')[:,None,:]
    labels=np.stack([np.asarray(arr[b],dtype='float32') for b in LABELS],axis=1)
    y=labels.argmax(axis=1).astype('int64')
    return x,v,real_mask,y,labels

def load_jetclass_balanced_official(data_dir,mode='full',samples_per_file=64,max_files=20,particles=128,device='cpu'):
    files=sorted(glob.glob(str(Path(data_dir)/'**/*.root'),recursive=True))[:max_files]
    if not files: raise FileNotFoundError(f'No ROOT files under {data_dir}')
    import uproot
    need=list(dict.fromkeys(PART_BASE+JET+LABELS))
    xs=[];vs=[];ms=[];ys=[];labs=[];used=[]
    for fp in files:
        tr=uproot.open(fp)['tree']; n=min(samples_per_file,int(tr.num_entries))
        arr=tr.arrays(need,entry_stop=n,library='ak')
        x,v,m,y,la=make_features_official(arr,mode,particles)
        xs.append(x); vs.append(v); ms.append(m); ys.append(y); labs.append(la); used.append(fp)
    x=np.concatenate(xs,0); v=np.concatenate(vs,0); m=np.concatenate(ms,0); y=np.concatenate(ys,0); la=np.concatenate(labs,0)
    return {'x':torch.tensor(x,device=device),'v':torch.tensor(v,device=device),'mask':torch.tensor(m,device=device),'y':torch.tensor(y,device=device),'labels':torch.tensor(la,device=device),'files':used,'label_names':LABELS}

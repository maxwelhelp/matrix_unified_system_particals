import glob, math
from pathlib import Path
import awkward as ak
import numpy as np
import torch

LABELS=['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
PART_BASE=['part_px','part_py','part_pz','part_energy','part_deta','part_dphi','part_d0val','part_d0err','part_dzval','part_dzerr','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon']
JET=['jet_pt','jet_energy']

def _pad(a,length=128):
    return ak.to_numpy(ak.fill_none(ak.pad_none(a,length,clip=True),0)).astype('float32')

def _clip(x): return np.clip(x,-5,5).astype('float32')
def _std(x,sub=None,mul=1,clip=True):
    y=x if sub is None else x-sub
    y=y*mul
    return _clip(y) if clip else y.astype('float32')

def _make_features(arr,mode,length=128):
    px=_pad(arr['part_px'],length); py=_pad(arr['part_py'],length); pz=_pad(arr['part_pz'],length); en=_pad(arr['part_energy'],length)
    deta=_pad(arr['part_deta'],length); dphi=_pad(arr['part_dphi'],length)
    pt=np.hypot(px,py); eps=1e-8
    jet_pt=np.asarray(arr['jet_pt'],dtype='float32')[:,None]; jet_e=np.asarray(arr['jet_energy'],dtype='float32')[:,None]
    f=[]
    f += [_std(np.log(pt+eps),1.7,0.7), _std(np.log(en+eps),2.0,0.7), _std(np.log((pt+eps)/(jet_pt+eps)),-4.7,0.7), _std(np.log((en+eps)/(jet_e+eps)),-4.7,0.7), _std(np.hypot(deta,dphi),0.2,4.0)]
    if mode in ('kinpid','full'):
        for b in ['part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon']:
            f.append(_pad(arr[b],length))
    if mode=='full':
        f += [np.tanh(_pad(arr['part_d0val'],length)).astype('float32'), _std(_pad(arr['part_d0err'],length),0,1), np.tanh(_pad(arr['part_dzval'],length)).astype('float32'), _std(_pad(arr['part_dzerr'],length),0,1)]
    f += [deta.astype('float32'), dphi.astype('float32')]
    x=np.stack(f,axis=1).astype('float32')
    v=np.stack([px,py,pz,en],axis=1).astype('float32')
    mask=(en>0).astype('bool')[:,None,:]
    labels=np.stack([np.asarray(arr[b],dtype='float32') for b in LABELS],axis=1)
    y=labels.argmax(axis=1).astype('int64')
    return x,v,mask,y,labels

def load_jetclass_batch(data_dir,mode='full',limit=256,max_files=20,particles=128,device='cpu'):
    files=sorted(glob.glob(str(Path(data_dir)/'**/*.root'),recursive=True))[:max_files]
    if not files: raise FileNotFoundError(f'No ROOT files under {data_dir}')
    import uproot
    need=list(dict.fromkeys(PART_BASE+JET+LABELS))
    xs=[]; vs=[]; ms=[]; ys=[]; labs=[]; used=[]; remain=limit
    for fp in files:
        if remain<=0: break
        tr=uproot.open(fp)['tree']
        n=min(int(tr.num_entries),remain)
        arr=tr.arrays(need,entry_stop=n,library='ak')
        x,v,m,y,la=_make_features(arr,mode,particles)
        xs.append(x); vs.append(v); ms.append(m); ys.append(y); labs.append(la); used.append(fp); remain-=len(y)
    x=np.concatenate(xs,0)[:limit]; v=np.concatenate(vs,0)[:limit]; m=np.concatenate(ms,0)[:limit]; y=np.concatenate(ys,0)[:limit]; la=np.concatenate(labs,0)[:limit]
    return {'x':torch.tensor(x,device=device),'v':torch.tensor(v,device=device),'mask':torch.tensor(m,device=device),'y':torch.tensor(y,device=device),'labels':torch.tensor(la,device=device),'files':used[:], 'label_names':LABELS}

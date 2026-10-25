"""Resume-safe adaptive rational closed-cover proof of original temporal A_N>0,A_M<0.

Each cell uses SHA-pinned 8 original physical modules, interval Step68l
center-branch U enclosure and Step55 exact ODE derivatives. The driver only
claims CERTIFIED when no unsolved cells remain; otherwise INCOMPLETE/FAILED.
State is atomically saved after each completed cell, so external timeout
cannot erase previous proof fragments. NO full Dirac rank claim.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from .hr_step68o_temporal_interval_annulus import evaluate_cell
from .hr_step68f_physical_pointwise import verified_sources
from .hr_step68n_interval_ode_jets import certify_sources,coefficient_interval


def gi(path):
    raw=Path(path).read_bytes()
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def atomic(path,state):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    t=path.with_suffix(path.suffix+'.part')
    t.write_text(json.dumps(state,indent=2,sort_keys=True)+'\n')
    t.replace(path)


def cover(state_path,start=F(1,8),end=F(17,20),max_cells=96,max_depth=16,reset=False):
    sources=verified_sources();certify_sources()
    state_path=Path(state_path)
    provenance={'original_shas':sources,'new_engine_sha':gi(Path(__file__).with_name('hr_step68o_temporal_interval_annulus.py')),
                'interval_jet_sha':gi(Path(__file__).with_name('hr_step68n_interval_ode_jets.py'))}
    if state_path.exists() and not reset:
        x=json.loads(state_path.read_text())
        if x['provenance']!=provenance or x['coverage']!=[str(start),str(end)]:
            raise ValueError('Checkpoint source/version/range drift; refusing unsafe resume')
        if x['status']=='CERTIFIED':return x
    else:
        x={'schema':'janus-adaptive-rational-temporal-v1','coverage':[str(start),str(end)],
           'provenance':provenance,'status':'INCOMPLETE','processed':0,
           'certified':[],'failures':[],'queue':[[str(start),str(end),0]],
           'claim':'Only certified closed cells form a rigorous proof; gaps not allowed',
           'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
        atomic(state_path,x)
    count=0
    while x['queue'] and count<max_cells:
        lo,hi,depth=x['queue'][-1]
        # A wide interval can straddle a pole even if the true physical
        # function is regular. Subdivide, never misreport such an evaluation.
        try:
            t=evaluate_cell(F(lo),F(hi))
            error=None
        except (ZeroDivisionError,ValueError) as exc:
            t=None
            error=type(exc).__name__+': '+str(exc)
        x['queue'].pop()
        count+=1;x['processed']+=1
        if t is not None and t['N'].lo>0 and t['M'].hi<0:
            x['certified'].append({'lo':lo,'hi':hi,
                'N':coefficient_interval(t['N']), 'M':coefficient_interval(t['M'])})
        elif depth>=max_depth:
            x['failures'].append({'lo':lo,'hi':hi,'depth':depth,
                'N':coefficient_interval(t['N']) if t else None,
                'M':coefficient_interval(t['M']) if t else None,
                'reason':error or 'Dependency overestimation or true possible sign obstruction; NO proof'})
        else:
            mid=(F(lo)+F(hi))/2
            x['queue'].append([str(mid),hi,depth+1])
            x['queue'].append([lo,str(mid),depth+1])
        # Atomic checkpoint after EVERY cell, including failed/unsolved cells.
        x['status']='FAILED' if x['failures'] else ('CERTIFIED' if not x['queue'] else 'INCOMPLETE')
        atomic(state_path,x)
    # Verify exact rational no-gaps partition before claiming certification.
    if x['status']=='CERTIFIED':
        cells=sorted((F(y['lo']),F(y['hi'])) for y in x['certified'])
        assert cells and cells[0][0]==start and cells[-1][1]==end
        assert all(p[1]==q[0] for p,q in zip(cells,cells[1:]))
        assert all(F(y['N'][0])>0 and F(y['M'][1])<0 for y in x['certified'])
    atomic(state_path,x)
    return x


def cli():
    a=argparse.ArgumentParser()
    a.add_argument('--state',required=True)
    a.add_argument('--start',type=F,default=F(1,8))
    a.add_argument('--end',type=F,default=F(17,20))
    a.add_argument('--max-cells',type=int,default=96)
    a.add_argument('--max-depth',type=int,default=16)
    a.add_argument('--reset',action='store_true')
    k=a.parse_args()
    if not 0<k.start<k.end<=F(17,20) or k.max_cells<1 or k.max_depth<0:
        raise ValueError('Invalid certified domain or positive budget')
    x=cover(k.state,k.start,k.end,k.max_cells,k.max_depth,k.reset)
    print(json.dumps({'status':x['status'],'processed':x['processed'],
          'certified_cells':len(x['certified']),'queue_left':len(x['queue']),
          'failed_cells':len(x['failures']),'range':x['coverage']}))
    if x['status']=='FAILED':raise SystemExit(1)

if __name__=='__main__':cli()

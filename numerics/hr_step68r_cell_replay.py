"""Resume-safe exact replay of archived JANUS temporal-sign rational interval cells.

This is a re-execution audit using the SAME original interval evaluation engine,
NOT an independent non-IBP Poisson oracle. Fail closed on archive/source drift;
only mark completed after every cell has been evaluated with identical endpoints.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha1,sha256
from pathlib import Path
import json
from .hr_step68o_temporal_interval_annulus import evaluate_cell
from .hr_step68p_adaptive_temporal_sign import gi,atomic
from .hr_step68f_physical_pointwise import verified_sources
from .hr_step68n_interval_ode_jets import certify_sources,coefficient_interval

PROOFS = {
    'outer': ('gate2b-step68p-adaptive-outer-cover.json', '179b967cc21160dcfef5eb98e1142c5ca17b83ee182d17162a2ec64708e48e4f', F(1,8), F(17,20),265),
    'inner': ('gate2b-step68q-inner-1over16-to-1over8-cover.json', '296e83528f9675fd42521b7cfffa2ec0f6057cce1d930a97a323aa007009e2c2', F(1,16),F(1,8),314),
}


def prep(label,proof_path=None):
    if label not in PROOFS:raise ValueError('Unknown proof label')
    name,h,start,end,count=PROOFS[label]
    path=Path(proof_path) if proof_path is not None else Path(__file__).resolve().parents[1]/'research/reports'/name
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=h:raise ValueError('Archived proof SHA256 drift')
    v=json.loads(raw)
    prov={'original_shas':verified_sources(),
          'new_engine_sha':gi(Path(__file__).with_name('hr_step68o_temporal_interval_annulus.py')),
          'interval_jet_sha':gi(Path(__file__).with_name('hr_step68n_interval_ode_jets.py'))}
    certify_sources()
    if v['provenance']!=prov:raise ValueError('Physical source provenance drift')
    if v['coverage']!=[str(start),str(end)] or v['status']!='CERTIFIED' or v['queue'] or v['failures']:
        raise ValueError('Proof incomplete or wrong radial range')
    rows=sorted(v['certified'],key=lambda x:F(x['lo']))
    if len(rows)!=count or F(rows[0]['lo'])!=start or F(rows[-1]['hi'])!=end or not all(F(x['hi'])==F(y['lo']) for x,y in zip(rows,rows[1:])):
        raise ValueError('Proof exact rational covering invalid')
    for row in rows:
        if F(row['lo'])>=F(row['hi']) or F(row['N'][0])<=0 or F(row['M'][1])>=0:raise ValueError('Archived cell unsigned')
    return rows,h,prov


def replay(label,state_path,max_cells=48,proof_path=None,reset=False):
    rows,h,prov=prep(label,proof_path)
    p=Path(state_path)
    expected={'proof_sha256':h,'source_provenance':prov,'label':label,'total':len(rows)}
    if p.exists() and not reset:
        state=json.loads(p.read_text())
        if any(state.get(k)!=v for k,v in expected.items()):raise ValueError('Replay state drift')
        if state.get('status')=='PASSED':return state
    else:
        state={**expected,'schema':'janus-temporal-replay-v1','completed':0,'status':'INCOMPLETE','failures':[],
               'warning':'Replay uses SAME authenticated Step58 interval evaluator; not a second independent theoretical oracle',
               'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
        atomic(p,state)
    for i in range(state['completed'],min(len(rows),state['completed']+max_cells)):
        t=rows[i]
        actual=evaluate_cell(F(t['lo']),F(t['hi']))
        if coefficient_interval(actual['N'])!=t['N'] or coefficient_interval(actual['M'])!=t['M']:
            state['failures'].append({'index':i,'bounds_saved':{'N':t['N'],'M':t['M']},
                                     'bounds_replayed':{'N':coefficient_interval(actual['N']),'M':coefficient_interval(actual['M'])}})
            state['status']='FAILED';atomic(p,state);raise AssertionError('Replayed rational bounds disagree with published original')
        state['completed']=i+1
        atomic(p,state)
    state['status']='PASSED' if state['completed']==len(rows) and not state['failures'] else 'INCOMPLETE'
    atomic(p,state)
    return state


def cli():
    a=argparse.ArgumentParser()
    a.add_argument('--label',required=True,choices=tuple(PROOFS))
    a.add_argument('--state',required=True)
    a.add_argument('--max-cells',type=int,default=48)
    a.add_argument('--reset',action='store_true')
    x=a.parse_args()
    if x.max_cells<1:raise ValueError('max_cells must be positive')
    r=replay(x.label,x.state,x.max_cells,reset=x.reset)
    print(json.dumps({k:r[k] for k in ('label','completed','total','status','failures')}))

if __name__=='__main__':cli()

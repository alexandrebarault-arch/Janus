"""b3c3d6: exact rational pointwise chart witness from original Step45/Step58.

NOT a Step55 radial solution, nor a global lapse/Dirac theorem. The test
requires the SHA-pinned original Step45 and Step58 modules and verifies
Fz and its first three radial jets on the positive-K stationary-shift chart.
"""
from __future__ import annotations
from pathlib import Path
from hashlib import sha1
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator

PINS={
    'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
}

def original_witness():
    base=Path(__file__).resolve().parent
    for filename,expected in PINS.items():
        raw=(base/filename).read_bytes()
        actual=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=expected:raise ValueError(f'original source drift {filename}: {actual}')
    p=exact_physical_ward();op=physical_operator()
    q=dict(zip(p['Q'],p['q']));dq=dict(zip(p['Q'],p['dq']))
    ddq=dict(zip(p['Q'],p['ddq']))
    dddq=dict(zip(p['Q'],op['qppp']))
    vals={v:sp.S.Zero for v in (*op['q'],*op['qp'],*op['qpp'],*op['qppp'],*op['q4'],op['z'],op['zr'],op['zrr'],op['zrrr'])}
    vals.update({q[k]:sp.Rational(v) for k,v in {
        'Lg':1,'Lf':1,'Sg':1,'Sf':1,'pg':sp.Rational(3,4),
        'pf':sp.Rational(311,100)}.items()})
    vals.update({dq[k]:sp.Rational(v) for k,v in {
        'Sg':1,'Sf':sp.Rational(4,5),'pLg':sp.Rational(-3,4)}.items()})
    vals[ddq['Lf']]=sp.Rational(42,25)
    vals[dddq['Lf']]=sp.Rational(4476,625)
    vals.update({op['z']:sp.Rational(3,5),op['zr']:sp.Rational(-96,125)})
    for sym,v in zip(p['parameters'][:8],(1,1,1,-4,1,0,0,-4)):
        vals[sym]=sp.Integer(v)
    def ev(expr):return sp.cancel(expr.subs(vals))
    residuals={}
    for name,expr in [('Fz',p['Fz']),('Hg',p['Hg']),('Hf',p['Hf']),('C',p['C_exact'])]:
        residuals[name]=ev(expr)
    jet=p['Fz']
    for k in (1,2,3):
        jet=op['Dt'](jet)
        residuals[f'Fz_d{k}']=ev(jet)
    for name,x in residuals.items():
        assert x==0,(name,x)
    assert ev(op['K'])==1
    assert vals[op['z']]>0 and 1-vals[op['z']]**2>0
    assert vals[q['pg']]>0 and vals[q['pf']]>0
    expected={'N':(sp.Rational(1293,250),sp.Rational(224,125),sp.S.Zero),
              'M':(sp.Rational(-79093,12500),sp.S.Zero,sp.S.Zero)}
    observed={}
    for label in ('N','M'):
        observed[label]=tuple(ev(op['operator'][label][j]) for j in (0,1,2))
        assert observed[label]==expected[label],(label,observed[label])
    assert observed['M'][1]==0 and observed['N'][1]!=0
    return {
        'step':'b3c3d6','scope':'ORIGINAL_STEP45_STEP58_EXACT_POINTWISE_SHIFT_JET_NOT_STEP55_NOT_DIRAC',
        'source_git_blob_shas':PINS,'constraints_zero':list(residuals),
        'K':'1','z':'3/5','pg':'3/4','pf':'311/100',
        'operator_N':[str(v) for v in observed['N']],
        'operator_M':[str(v) for v in observed['M']],
        'B_M_zero':True,'B_N_nonzero':True,
        'limitation':'Hg,Hf,C radial derivative hierarchy and global Step55 BVP not imposed',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(original_witness(),indent=2))

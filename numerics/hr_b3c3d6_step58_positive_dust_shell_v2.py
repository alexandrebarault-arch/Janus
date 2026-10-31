"""Exact positive-dust Step58 primary/secondary local jet family; NOT Step55."""
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import sympy as S
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator

BLOBS = {'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
         'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f'}

def authenticate():
    for name, sha in BLOBS.items():
        b = Path(__file__).with_name(name).read_bytes()
        assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest() == sha
    return True

@lru_cache(1)
def family():
    authenticate()
    p=exact_physical_ward(); op=physical_operator()
    q=dict(zip(p['Q'],p['q'])); qp=dict(zip(p['Q'],p['dq']))
    a=S.Symbol('a',real=True)
    fields=(*op['q'],*op['qp'],*op['qpp'],*op['qppp'],*op['q4'],
            op['z'],op['zr'],op['zrr'],op['zrrr'],*p['parameters'][:8])
    v={x:S.S.Zero for x in fields}
    for name in ('Lg','Lf','Sg','Sf'):v[q[name]]=S.S.One
    for x in p['parameters'][:3]:v[x]=S.S.One
    v[p['parameters'][3]]=-5;v[p['parameters'][4]]=1;v[p['parameters'][7]]=-2
    v[op['z']]=S.Rational(3,5);v[op['zr']]=a
    for x in (qp['Sg'],qp['Sf'],q['pSg'],q['pLf'],q['pSf'],q['pf']):v[x]=S.S.One
    v[q['pg']]=S.Rational(7,4);v[qp['pLg']]=S.Rational(1,4)
    v[op['qpp'][1]]=-S.Rational(3,2)-S.Rational(125,64)*a
    v[op['qppp'][2]]=S.Rational(29,16)-S.Rational(75,128)*a
    def ev(expr):return S.cancel(expr.subs(v))
    shell={k:ev(e) for k,e in {'Fz':op['Fz'],'Fzr':op['Dt'](op['Fz']),
           'Hg':p['Hg'],'Hgr':op['Dt'](p['Hg']),'Hf':p['Hf']}.items()}
    coeff={f'{k}{j}':ev(op['operator'][k][j]) for k in ('N','M') for j in (0,1,2)}
    c=ev(op['C'])
    return {'a':a,'v':v,'op':op,'p':p,'q':q,'shell':shell,'coeff':coeff,
            'C':c,'K':ev(op['K']),'z':ev(op['z']),
            'dust':(ev(q['pg']),ev(q['pf'])),
            'B_factor':ev(op['operator']['N'][1]-op['z']*op['C']/q['Lg'])}

def certificate():
    x=family();a=x['a'];b=x['coeff']
    assert all(t==0 for t in x['shell'].values())
    assert (x['K'],x['z'],*x['dust'])==(1,S.Rational(3,5),S.Rational(7,4),1)
    assert x['C']==-S.Rational(9,5)-S.Rational(5,4)*a
    assert b['N1']==-S.Rational(27,25)-S.Rational(3,4)*a
    assert b['M1']==x['B_factor']==b['N2']==b['M2']==0
    a0=-S.Rational(36,25)
    assert x['C'].subs(a,a0)==0 and b['N1'].subs(a,a0)==0
    return {'original_blobs':BLOBS,'exact_primary_shell':'Fz=Fzr=Hg=Hgr=Hf=0',
            'positive_chart':'K=1,z=3/5,pg=7/4,pf=1,Lg=Lf=Sg=Sf=1',
            'C':str(x['C']),'B_N':str(b['N1']),'B_M':'0',
            'C_zero_at_zr':'-36/25','scope':'local non-Step55 jet family; no universal B theorem',
            'six_physical_A_B_E':'NOT_CERTIFIED','two_boundary_BVP':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(certificate(),indent=2))

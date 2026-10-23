"""Certified symbolic normalization of original Step45/46 six-pair secondary.

Exactly cancel radial factors in the physical primary-reduced pLf' equation,
then use s=r**2 and U=pLf/r**2. Square-root branches require Lf>0,
Sfr>0, sqrt(1-z**2)>0 (certified on the Step54 tube).
This is ONLY a spatial initial-data ODE, not temporal Dirac preservation.
"""
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import sympy as sp
from .hr_step46_exact_secondary_ode import exact_f_momentum_ode

SOURCE_BLOBS={"numerics/hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e", "numerics/hr_step46_exact_secondary_ode.py":"bac025c28dbe1561c0c36c56dbfda46dc326f804"}
def check_original_source_blobs(root=None):
 root=Path(root) if root is not None else Path(__file__).resolve().parents[1]
 for rel,expected in SOURCE_BLOBS.items():
  raw=(root/rel).read_bytes()
  sha=sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  if sha!=expected:raise ValueError(f"Original six-pair source mismatch {rel}: {sha}")
 return SOURCE_BLOBS.copy()
@lru_cache(maxsize=1)
def normalized_symbolic():
 check_original_source_blobs()
 orig=exact_f_momentum_ode()
 d={'expr':orig['pLf_prime_rhs'],
    'symbols':tuple(orig['symbols']['q'].values()),
    'dqs':tuple(orig['symbols']['dq'].values()),
    'params':orig['symbols']['params'],
    'Dg':orig['original_primary_f_shift'],
    'Wf':orig['original_primary_f_potential'],
    'R3f':orig['original_R3f']}
 r=sp.symbols('r',positive=True);s=sp.symbols('s',nonnegative=True)
 Lg,Lf,Sgr,Sfr,Gmom,Psg,Rhog,Gprime,tg,tf,z1,Dbar,Wfbar,Rf,Lgr,Lfr,U=sp.symbols('Lg0 Lf0 Sgr0 Sfr0 Gmom Psg0 Rhog Gprime tg0 tf0 z1 Dbar Wfbar Rf Lgr0 Lfr0 U',real=True)
 q=dict(zip(('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf'),d['symbols']));dq=dict(zip(q,d['dqs']))
 mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=d['params']
 subs={q['Lg']:Lg,q['pLg']:r*r*Gmom,q['Sg']:r*Lg,q['pSg']:r*Psg,q['pg']:r*r*Rhog,q['Lf']:Lf,q['pLf']:r*r*U,q['Sf']:r*Lf,
       dq['Lg']:r*Lgr,dq['Lf']:r*Lfr,dq['Sg']:Sgr,dq['Sf']:Sfr,dq['pLg']:r*Gprime,dq['tg']:r*tg,dq['tf']:r*tf,
       z:r*z1,zr:z1,zrr:0,d['Dg']:r**3*Dbar,d['Wf']:r*r*Wfbar,d['R3f']:Rf}
 e=sp.cancel(sp.together(d['expr'].subs(subs)/r))
 # Positive branch: Lf=b*(1+c_f*s)^2>0 on the certified interval.
 e=e.subs(sp.Abs(Lf),Lf)
 e=sp.powdenest(e.subs(r,sp.sqrt(s)),force=False)
 if e.has(r):raise AssertionError("radial singular factor not eliminated")
 assert not e.has(r),set(str(x) for x in e.free_symbols if str(x)=='r')
 return (e,s,U,dict(Lg=Lg,Lf=Lf,Sgr=Sgr,Sfr=Sfr,Gmom=Gmom,Psg=Psg,Rhog=Rhog,Gprime=Gprime,tg=tg,tf=tf,z1=z1,Dbar=Dbar,Wfbar=Wfbar,Rf=Rf,Lgr=Lgr,Lfr=Lfr,mg=mg,mf=mf,m2=m2,beta=(b0,b1,b2,b3,b4)))
@lru_cache(maxsize=1)
def compiler(modules='mpmath'):
 expr,s,U,v=normalized_symbolic()
 syms=sorted(expr.free_symbols,key=str)
 return syms,sp.lambdify(syms,expr,modules=modules,cse=True)
if __name__=='__main__':
 e,s,u,v=normalized_symbolic();print('ops',sp.count_ops(e));print('vars',len(e.free_symbols));print('s=0',str(e.subs(s,0))[:350]);print('parts',len(sp.cse(e)[0]))

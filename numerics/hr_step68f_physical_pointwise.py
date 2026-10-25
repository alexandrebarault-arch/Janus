"""Step68f: byte-original physical Step45/46/55/57-60 joint run and exploratory pointwise Dirac residual.

All exact historical source modules imported from a byte-authenticated local
workspace. Profile values use mpmath at user-specified r>0 and a local
Taylor-3 solution of the genuine Step55 ODE 2sU_s=G(s,U)-2U whose U(s0)
is *chosen* inside the certified Ustar +/- 0.0001 barrier. The pointwise
local solution is not necessarily the unique globally regular center branch!

Numerical evaluation of the exact symbolic six-pair Cdot lower lapse
coefficients is exploratory (floating point), NOT interval certification,
not a demonstration of time gauge/lapse positivity or BD ghost freedom.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction
from hashlib import sha1
from pathlib import Path
import json
import mpmath as mp
import numpy as np
import sympy as sp
from . import hr_step55_global_barrier as old
from .hr_step58_temporal_operator import physical_operator
from .hr_step60_full_constraint_prolongation import full_constraint_prolongation
from .hr_step45_exact_physical_ward import exact_physical_ward

PINS={
'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
'hr_step57_secondary_principal_symbol.py':'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f',
'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
'hr_step59_third_jet_gate.py':'ae26a79cbfa7bb50fbb398d7d6c18478adf7627e',
'hr_step60_full_constraint_prolongation.py':'9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509'}


def verified_sources():
    root=Path(__file__).resolve().parent
    for name,sha in PINS.items():
        b=(root/name).read_bytes()
        actual=sha1(b'blob '+str(len(b)).encode()+b'\x00'+b).hexdigest()
        if actual!=sha:raise ValueError('byte-source mismatch: '+name+' != '+sha)
    return PINS.copy()


def mid(x):
    return mp.mpf(x.lo+x.hi)/(2*old.S)


def constants():
    return {k:mid(getattr(old,k)) for k in ('A','B','MG','MF','M2',
           'B0','B1','B2','B3','B4','CG','CF','KG','KF','Z1','PG','U0','U1','U2')}


def geometry(s,c):
    a,b,mg,mf,m2=(c[k] for k in ('A','B','MG','MF','M2'))
    b0,b1,b2,b3,b4=(c[k] for k in ('B0','B1','B2','B3','B4'))
    cg,cf,kg,kf,z1=(c[k] for k in ('CG','CF','KG','KF','Z1'))
    ug=1+cg*s;uf=1+cf*s
    Lg=a*ug**2;Lf=b*uf**2
    Sgr=a*ug*(1+5*cg*s);Sfr=b*uf*(1+5*cf*s)
    T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2
    T0=b0*Lg**2+2*b1*Lg*Lf+b2*Lf**2
    Tf=b2*Lg**2+2*b3*Lg*Lf+b4*Lf**2
    root=mp.sqrt(1-z1*z1*s)
    Dbar=m2*mg*Lg*Lf*T*z1/root
    Wgbar=m2*mg*(Lg*T0+Lf*T*root)
    Wfbar=m2*mg*(Lf*Tf+Lg*T*root)
    Rg=-48*cg/(a*a*ug**5)
    Rf=-48*cf/(b*b*uf**5)
    Gmom=c['PG']*(1+mp.mpf(5)/2*cg*s)
    Gprime=2*c['PG']*(1+5*cg*s)
    fac=Gmom/(2*mg*Lg*Sgr)
    betag=mp.sqrt(1+kg*kg*s)+s*fac*kg*Lg
    Rhog=-(Gmom**2/(4*mg*Lg)-fac*(s*Dbar+Lg*Gprime)-mg*Lg**3*Rg/2+s*z1*Dbar/Lg+Wgbar)/betag
    Psg=(s*Dbar+Lg*Gprime-Rhog*s*kg*Lg)/Sgr
    return dict(Lg0=Lg,Lf0=Lf,Sgr0=Sgr,Sfr0=Sfr,Gmom=Gmom,Psg0=Psg,
        Rhog=Rhog,Gprime=Gprime,tg0=kg*Lg,tf0=kf*Lf,z1=z1,
        Dbar=Dbar,Wfbar=Wfbar,Rf=Rf,Lgr0=4*a*cg*ug,Lfr0=4*b*cf*uf,
        Mg2=mg,Mf2=mf,m2=m2,beta0=b0,beta1=b1,beta2=b2,beta3=b3,beta4=b4)

@lru_cache(1)
def normalized_G():
    from .hr_step55_normalized_secondary import compiler
    return compiler(modules='mpmath')

def G(s,u,c):
    p=geometry(s,c);p['s']=s;p['U']=u
    xs,fn=normalized_G()
    return fn(*[p[str(k)] for k in xs])


def local_point(rstr='0.4', offset='0'):
    verified_sources();mp.mp.dps=55
    c=constants();r0=mp.mpf(rstr);s0=r0*r0
    # Not a global integration: initial value is selected from the certified
    # 0.0001 tube; derivatives imposed from TRUE physical original G.
    u0=c['U0']+c['U1']*s0+c['U2']*s0*s0+mp.mpf(offset)
    if abs(mp.mpf(offset))>=mp.mpf('0.0001'):raise ValueError('outside Step55 barrier')
    g0=G(s0,u0,c)
    u1=(g0-2*u0)/(2*s0)
    gs=mp.diff(lambda s:G(s,u0,c),s0)
    gu=mp.diff(lambda u:G(s0,u,c),u0)
    u2=(gs+(gu-4)*u1)/(2*s0)
    gss=mp.diff(lambda s:G(s,u0,c),s0,2)
    gsu=mp.diff(lambda s:mp.diff(lambda u:G(s,u,c),u0),s0)
    guu=mp.diff(lambda u:G(s0,u,c),u0,2)
    u3=(gss+2*gsu*u1+guu*u1*u1+(gu-6)*u2)/(2*s0)
    def U(s):
        d=s-s0
        return u0+u1*d+u2*d*d/2+u3*d**3/6
    def point(t):
        s=t*t;ge=geometry(s,c);gv=G(s,U(s),c)
        lg,lf=ge['Lg0'],ge['Lf0']
        pf0=u=U(s)
        Ffac=u/(2*c['MF']*lf*ge['Sfr0'])
        dust_beta=mp.sqrt(1+c['KF']**2*s)
        rhof=-(u*u/(4*c['MF']*lf)-Ffac*(-s*ge['Dbar']+lf*gv)
                -c['MF']*lf**3*ge['Rf']/2+s*c['Z1']*ge['Dbar']/lf+ge['Wfbar'])/(dust_beta+s*Ffac*c['KF']*lf)
        psf=(-s*ge['Dbar']+lf*gv-rhof*s*ge['tf0'])/ge['Sfr0']
        return dict(Lg=lg,pLg=s*ge['Gmom'],Sg=t*lg,pSg=t*ge['Psg0'],tg=mp.mpf(0),pg=s*ge['Rhog'],
                    Lf=lf,pLf=s*u,Sf=t*lf,pSf=t*psf,tf=mp.mpf(0),pf=s*rhof)
    p=exact_physical_ward();o=physical_operator();zsymbols=p['parameters'][-3:]
    jets={}
    for name in p['Q']:
        f=lambda t:point(t)[name]
        jets[name]=[f(r0),mp.diff(f,r0),mp.diff(f,r0,2),mp.diff(f,r0,3),mp.diff(f,r0,4)]
    for nm,k in [('tg',c['KG']),('tf',c['KF'])]:
        metric='Lg' if nm=='tg' else 'Lf'
        fun=lambda t:k*t*point(t)[metric]
        jets[nm][1:]=[fun(r0),mp.diff(fun,r0),mp.diff(fun,r0,2),mp.diff(fun,r0,3)]
    # Use a numpy eval-point for large original 6-pair Hamiltonian expressions.
    syms=(*o['q'],*o['qp'],*o['qpp'],*o['qppp'],*o['q4'],*zsymbols,o['zrrr'],*p['parameters'][:8])
    vals=[]
    for order in range(5):vals.extend(jets[name][order] for name in p['Q'])
    vals+= [r0*c['Z1'],c['Z1'],mp.mpf(0),mp.mpf(0)]
    vals+= [c[k] for k in ('MG','MF','M2','B0','B1','B2','B3','B4')]
    assert len(syms)==len(vals),(len(syms),len(vals))
    data={k:float(v) for k,v in zip(syms,vals)}
    return {'r':r0,'s':s0,'U':u0,'G':g0,'Ujet_s':(u1,u2,u3),
            'symbols':syms,'values':vals,'pointmap':data,'jets':jets,
            'reference_dust_f':point(r0)['pf']/s0}


def evaluate_report(radius='0.4',offset='0'):
    t=local_point(radius,offset); p=exact_physical_ward();v=physical_operator()
    result={'radius':radius,'offset_from_Ustar':offset,'original_source_shas':verified_sources(),
            'U_at_radius':str(t['U']),'Ujet_s':list(map(str,t['Ujet_s'])),
            'dust_f_rho':str(t['reference_dust_f'])}
    allvars=t['symbols'];args=[float(k) for k in t['values']]
    def ev(expr):
        expression=sp.lambdify(allvars,expr,modules='numpy',cse=True)
        return float(expression(*args))
    for name,expr in [('Fz',p['Fz']),('Hg',p['Hg']),('Hf',p['Hf']),('C',p['C_exact'])]:
        result[name]=ev(expr)
    result['raw_temporal_coefficients']={}
    for lapse in ('N','M'):
        result['raw_temporal_coefficients'][lapse]={str(n):ev(v['operator'][lapse][n])
                                             for n in (0,1,2)}
    result['note']='Exploratory double-precision evaluating factored original SymPy on local pointwise ODE Taylor jet; not full certified radial solution or a Dirac rank proof'
    return result

if __name__=='__main__':print(json.dumps(evaluate_report(),indent=2))

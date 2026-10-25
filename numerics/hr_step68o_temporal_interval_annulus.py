"""Original six-pair Cdot A_N/A_M OUTWARD-INTERVAL jets on whole radius cells.

Uses certified Step68l 1e-6 global U tube and exact Step55 ODE derivative
Taylor-3 jet, original interval I (fixed-point integer outward rounding) and
SHA-verified original Step58 full non-frozen-shift operator. BOUNDS only on
specified closed annular cells; no full-domain rank or lapse theorem implied.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sympy as sp
from . import hr_step55_global_barrier as old
from .hr_step68n_interval_ode_jets import Jet,I,jet_geometry,jet_G,certify_sources,coefficient_interval
from .hr_step68f_physical_pointwise import verified_sources
from .hr_step58_temporal_operator import physical_operator


def _ode_coeff(si):
    if si.lo<=0 or si.hi>I.c(F(289,400)).hi:
        raise ValueError('Only certified outer Step68l tube with s>0')
    star,_,_=old.stars(si)
    eps=I.c(F(1,1000000))
    ui=I(star.lo-eps.hi,star.hi+eps.hi)
    su=Jet([si,I.c(1)])
    uj=Jet(ui)
    for n in range(1,4):
        jet=(jet_G(su,uj)-2*uj)/(2*su)
        uj.a[n]=jet.a[n-1]/n
    return uj


def canonical_jets_cell(rlo=F(2,5),rhi=F(2,5)):
    certify_sources();verified_sources()
    rlo,rhi=F(rlo),F(rhi)
    if rlo<=0 or rhi<rlo or rhi>F(17,20):
        raise ValueError('Invalid positive radius or outside certified Step68l interval')
    R=I.hull(rlo,rhi)
    si=R**2
    uj=_ode_coeff(si)
    # Convert the true ODE s-derivatives to r-derivatives, interval-wise.
    # uj.a[n] = U^(n)(s)/n!, so U_r=2rU_s, U_rr/2=U_s+2r^2 U_ss,
    # U_rrr/6=2r U_ss+4/3 r^3 U_sss.
    us=uj.a[1];uss=2*uj.a[2];usss=6*uj.a[3]
    u=Jet([uj.a[0],2*R*us,us+2*R**2*uss,2*R*uss+F(4,3)*R**3*usss])
    rr=Jet([R,I.c(1)])
    s=rr**2
    ge=jet_geometry(s)
    gv=jet_G(s,u)
    c={name:Jet(getattr(old,name)) for name in ('MG','MF','KG','KF','Z1','M2')}
    mg,mf,kg,kf,z1=(c[x] for x in ('MG','MF','KG','KF','Z1'))
    lg,lf=ge['Lg0'],ge['Lf0']
    Ffac=u/(2*mf*lf*ge['Sfr0'])
    betaf=(1+kf**2*s).sqrt()
    rhof=-(u*u/(4*mf*lf)-Ffac*(-s*ge['Dbar']+lf*gv)-mf*lf**3*ge['Rf']/2+s*z1*ge['Dbar']/lf+ge['Wfbar'])/(betaf+s*Ffac*kf*lf)
    psf=(-s*ge['Dbar']+lf*gv-rhof*s*ge['tf0'])/ge['Sfr0']
    data={'Lg':lg,'pLg':s*ge['Gmom'],'Sg':rr*lg,'pSg':rr*ge['Psg0'],
          'tg':Jet(0),'pg':s*ge['Rhog'],'Lf':lf,'pLf':s*u,'Sf':rr*lf,
          'pSf':rr*psf,'tf':Jet(0),'pf':s*rhof}
    for name,k,metric in (('tg',kg,lg),('tf',kf,lf)):
        tp=rr*k*metric
        data[name]=Jet([I.c(0),tp.a[0],tp.a[1]/2,tp.a[2]/3])
    return data, R, si, uj


@lru_cache(1)
def _compiled():
    o=physical_operator()
    Pow2=sp.Function('interval_halfpow')
    pair={}
    for label in ('N','M'):
        expr=o['operator'][label][0]
        assert not any(expr.has(x) for x in o['q4'])
        safe=expr.replace(lambda x:x.is_Pow and x.exp.is_Rational and x.exp.q==2,
                          lambda x:Pow2(x.base,sp.Integer(x.exp.p)))
        syms=tuple(sorted(expr.free_symbols,key=str))
        fn=sp.lambdify(syms,safe,modules=[{'interval_halfpow':lambda x,p:x.sqrt()**int(p),
                                             'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
        pair[label]=(syms,fn)
    return o,pair


def evaluate_cell(rlo=F(2,5),rhi=F(2,5)):
    names='Lg pLg Sg pSg tg pg Lf pLf Sf pSf tf pf'.split()
    canonical,R,si,uj=canonical_jets_cell(rlo,rhi)
    o,pair=_compiled()
    assert tuple(names)==tuple('Lg pLg Sg pSg tg pg Lf pLf Sf pSf tf pf'.split())
    vals={}
    for keys,degree in ((o['q'],0),(o['qp'],1),(o['qpp'],2),(o['qppp'],3)):
        for key,name in zip(keys,names):
            vals[key]=canonical[name].a[degree]*{0:1,1:1,2:2,3:6}[degree]
    for key in o['q4']: vals[key]=I.c(0)
    for name,val in zip(('z','zr','zrr','zrrr'),(R*old.Z1,old.Z1,I.c(0),I.c(0))):
        vals[getattr(o,'get',dict.get)(name) if False else {'z':o['z'],'zr':o['zr'],'zrr':o['zrr'],'zrrr':o['zrrr']}[name]]=val
    p=__import__('numerics.hr_step45_exact_physical_ward',fromlist=['exact_physical_ward']).exact_physical_ward()
    for sym,key in zip(p['parameters'][:8],('MG','MF','M2','B0','B1','B2','B3','B4')):
        vals[sym]=getattr(old,key)
    result={}
    for label,(syms,fn) in pair.items():
        assert all(sym in vals for sym in syms)
        enclosure=I.c(fn(*[vals[x] for x in syms]))
        result[label]=enclosure
    return result


def audit_cells(ranges):
    sources=verified_sources();certify_sources()
    rows=[]
    for lo,hi in ranges:
        t=evaluate_cell(F(lo),F(hi))
        rows.append({'rlo':str(F(lo)),'rhi':str(F(hi)),
                     'N':coefficient_interval(t['N']),'M':coefficient_interval(t['M']),
                     'N_positive':t['N'].lo>0,'M_negative':t['M'].hi<0})
    return {'step':'68o','cell_count':len(rows),'cells':rows,
            'all_signs_certified':all(x['N_positive'] and x['M_negative'] for x in rows),
            'provenance':sources,'gate':'OPEN','janus':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(audit_cells([(F(2,5),F(2,5)),(F(39,100),F(41,100))]),indent=2))

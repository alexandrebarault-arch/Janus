"""Experimental interval *point* evaluation of original full temporal A_N/A_M.

No claims of sign until actual outward intervals exclude zero. Uses certified
Step68l U(s0) enclosure and exact Taylor AD through Step55 G, then physical
canonical 12-field construction and original Step58 0th-lapse coefficients.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
import json
from math import factorial
import sympy as sp
from . import hr_step55_global_barrier as old
from .hr_step68n_interval_ode_jets import Jet,I,jet_geometry,jet_G,fixed_s_ode_jet,coefficient_interval,certify_sources
from .hr_step58_temporal_operator import physical_operator
from .hr_step68f_physical_pointwise import verified_sources


def radial_canonical_jets(s0=F(4,25)):
    certify_sources(); verified_sources()
    # On positive s0 only, r0 rational in this test (2/5).
    if s0!=F(4,25):raise ValueError('current verified branch uses s0=4/25')
    r0=F(2,5)
    uj=fixed_s_ode_jet(s0)
    rr=Jet([I.c(r0),I.c(1)])
    s=rr**2
    d=s-Jet(I.c(s0))
    u=sum((Jet(uj['U_coefficients'][j])*d**j for j in range(4)),Jet(0))
    ge=jet_geometry(s)
    gv=jet_G(s,u)
    c={name:Jet(getattr(old,name)) for name in ('MG','MF','KG','KF','Z1','M2')}
    mg,mf,kg,kf,z1=(c[x] for x in ('MG','MF','KG','KF','Z1'))
    lg,lf=ge['Lg0'],ge['Lf0']
    Ffac=u/(2*mf*lf*ge['Sfr0'])
    betaf=(1+kf**2*s).sqrt()
    rhof=-(u*u/(4*mf*lf)-Ffac*(-s*ge['Dbar']+lf*gv)-mf*lf**3*ge['Rf']/2 +s*z1*ge['Dbar']/lf+ge['Wfbar'])/(betaf+s*Ffac*kf*lf)
    psf=(-s*ge['Dbar']+lf*gv-rhof*s*ge['tf0'])/ge['Sfr0']
    result={'Lg':lg, 'pLg':s*ge['Gmom'], 'Sg':rr*lg, 'pSg':rr*ge['Psg0'],
        'tg':Jet(0),'pg':s*ge['Rhog'], 'Lf':lf,'pLf':s*u,'Sf':rr*lf,
        'pSf':rr*psf,'tf':Jet(0),'pf':s*rhof}
    for nm,k,metric in (('tg',kg,lg),('tf',kf,lf)):
        # Intrinsic radial jet of the dust phase is an integral of t*k*L.
        tprime=rr*k*metric
        result[nm]=Jet([I.c(0),tprime.a[0],tprime.a[1]/2,tprime.a[2]/3])
    return result, {'r0':r0,'U':uj,'s':s,'u':u}


def physical_input_symbols_and_intervals():
    canonical,cert=radial_canonical_jets()
    o=physical_operator()
    names=tuple('Lg pLg Sg pSg tg pg Lf pLf Sf pSf tf pf'.split())
    assert len(names)==len(o['q'])==12
    values=[]
    for n in range(4):
        values.extend(canonical[name].a[n]*factorial(n) for name in names)
    # Original operator has no q4 in its A_N/A_M coefficient (verified).
    values.extend(I.c(0) for _ in o['q4'])
    values += [I.c(F(2,5))*old.Z1,old.Z1,I.c(0),I.c(0)]
    values += [getattr(old,k) for k in ('MG','MF','M2','B0','B1','B2','B3','B4')]
    p=__import__('numerics.hr_step45_exact_physical_ward',fromlist=['exact_physical_ward']).exact_physical_ward()
    symbols=(*o['q'],*o['qp'],*o['qpp'],*o['qppp'],*o['q4'],o['z'],o['zr'],o['zrr'],o['zrrr'],*p['parameters'][:8])
    assert len(values)==len(symbols)
    return dict(zip(symbols,values)),o


def interval_temporal_at_0_4():
    vals,o=physical_input_symbols_and_intervals()
    result={}
    for lab in ('N','M'):
        expr=o['operator'][lab][0]
        assert not any(expr.has(k) for k in o['q4'])
        syms=tuple(sorted(expr.free_symbols,key=str))
        # Error if any required symbol absent; interval geometry never guesses.
        assert set(syms)<=set(vals)
        # Preserve outward rounding for HALF-INTEGER powers in the exact
        # original Step58 operator (the original Step55 I supports only +/-1/2).
        # Do not modify the SHA-pinned original interval implementation.
        Pow2=sp.Function('interval_halfpow')
        safe=expr.replace(lambda v: v.is_Pow and v.exp.is_Rational and v.exp.q == 2,
                          lambda v: Pow2(v.base, sp.Integer(v.exp.p)))
        f=sp.lambdify(syms,safe,modules=[{'interval_halfpow':lambda x,p:x.sqrt()**int(p),
                                            'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
        interval=I.c(f(*[vals[s] for s in syms]))
        result[lab]={'enclosure':coefficient_interval(interval),
                     'positive_certified':interval.lo>0,'negative_certified':interval.hi<0,
                     'operations_symbolic':sp.count_ops(expr)}
    result['scope']='r0=2/5 only, global Step68l U enclosure, all 12 original canonical jets through third order'
    result['source_shas']=verified_sources()
    result['GATE_2B']='OPEN';result['JANUS_R']='NOT_VALIDATED'
    return result

if __name__=='__main__':print(json.dumps(interval_temporal_at_0_4(),indent=2))

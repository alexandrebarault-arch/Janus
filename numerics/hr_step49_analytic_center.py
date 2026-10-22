"""Step49 exact parity/regularized secondary near a nondegenerate spherical center.

The original six-canonical-pair C from Step45, after original f dust
primary elimination in Step46, admits analytic local implicit equation
W=G(s,U), where s=r², pLf=s U(s), W=pLf'/r.

We verify exactly C/r² is EVEN in r and finite on regular background
parity fields, and G(0,U)=3 U0-U. Therefore the scalar Briot--Bouquet
problem s U_s=-3/2*(U-U0)+s R(s,U)/2 has a unique analytic local
solution if the other prescribed source functions are analytic with
regular denominators, square roots and J(y)>0. This is NOT a global
existence theorem or a dynamic Dirac/lapse/ghost proof.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from math import isqrt
import sympy as sp
from .hr_step46_exact_secondary_ode import exact_f_momentum_ode


@lru_cache(maxsize=1)
def exact_center_parity():
    d=exact_f_momentum_ode()
    c=d['equation'];q=d['symbols']['q'];v=d['symbols']['dq']
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=d['symbols']['params']
    r=sp.symbols('r', real=True)
    A,B,LGr,LFr,SGr,SFr,Pg,PGprime,PsG,pgD,U,W,tg,tf,z1,Rf=sp.symbols(
        'A B LGr LFr SGr SFr Pg PGprime PsG pgD U W tg tf z1 Rf', real=True)
    Dbar,Wfbar=sp.symbols('Dbar Wfbar')
    # Each placeholder is a radial EVEN analytic function of s=r².
    # Not free constants; the parity identity is valid pointwise for such functions.
    substitution={
        q['Lg']:A,q['Sg']:r*A,q['pLg']:r*r*Pg,
        q['pSg']:r*PsG,q['pg']:r*r*pgD,
        q['Lf']:B,q['Sf']:r*B,q['pLf']:r*r*U,
        v['Lg']:r*LGr,v['Sg']:SGr,v['pLg']:r*PGprime,
        v['tg']:r*tg,v['Lf']:r*LFr,v['Sf']:SFr,v['tf']:r*tf,
        z:r*z1,zr:z1,zrr:0,
        d['V']:r*W,
        d['original_primary_f_shift']:r**3*Dbar,
        d['original_primary_f_potential']:r**2*Wfbar,
        d['original_R3f']:Rf}
    scaled=sp.cancel(c.subs(substitution)/r**2)
    odd_remainder=sp.cancel(scaled.subs(r,-r)-scaled)
    limit=sp.cancel(sp.limit(scaled,r,0))
    constraints={SGr:A,SFr:B,PsG:2*Pg,PGprime:2*Pg,LGr:0,LFr:0}
    lead=sp.factor(limit.subs(constraints))
    Aa=A*A*b1+2*A*B*b2+B*B*b3
    expected=-m2*Aa*(6*A*B*mf*mg*z1+A*mg*(U+W)-3*B*mf*Pg)/(2*A*B*mf)
    U0=mf*B*(Pg/(mg*A)-2*z1)
    slope=sp.factor(sp.diff(lead,W))
    solved=sp.solve(lead,W)[0]
    checks={
        'exact_even_parity':odd_remainder,
        'exact_finite_center_leading_formula':sp.cancel(lead-expected),
        'unique_regular_center_W_relation':sp.cancel(solved-(3*U0-U)),
        'nonzero_W_coefficient':sp.cancel(slope+m2*mg*Aa/(2*B*mf)),
    }
    if any(v!=0 for v in checks.values()):
        raise AssertionError('exact center analytic parity/implicit structure mismatch')
    return {'C_div_r2':scaled,'leading':lead,'W_implicit':solved,
            'U0':U0,'dCbar_dW_at_center':slope,
            'Astar':Aa,'r':r,'checks':checks,'symbols':(A,B,Pg,U,W,z1,mg,mf,m2)}


def benchmark_center_positive_dust(digits=50):
    """Exact rational lower bounds, enclosing ONLY sqrt(H²) by integer isqrt."""
    if not isinstance(digits,int) or digits<12 or digits>100:
        raise ValueError('outward decimal sqrt precision outside supported range')
    a=F('0.4');y=F('0.5787707228025044');b=a*y
    mg=F(1);mf=F('0.10879548725')**2;m2=F('23.3348939346')
    cg=F('0.0015');cf=F('-0.0012');z1=F('0.004')
    b0,b1,b2,b3,b4=map(F,('0','1','-4.2383993109','13.6801214252','-38.5117901844'))
    h2=F('.9')/(3*a**3)+(m2/3)*(b0+3*b1*y+3*b2*y*y+b3*y**3)
    if h2<=0:raise AssertionError('H² must be positive')
    t=10**digits
    low=F(isqrt((h2.numerator*t*t)//h2.denominator),t)
    high=low+F(1,t)
    A0=a*(b0*a*a+2*b1*a*b+b2*b*b)+b*(b1*a*a+2*b2*a*b+b3*b*b)
    Af=b*(b2*a*a+2*b3*a*b+b4*b*b)+a*(b1*a*a+2*b2*a*b+b3*b*b)
    pg=3*mg*a**3*h2-24*mg*a*cg-m2*mg*A0
    # U0=-2 mf b*(a H+z1) exactly, and sqrt(H²) enclosed outward.
    u0lo=-2*mf*b*(a*high+z1)
    u0hi=-2*mf*b*(a*low+z1)
    def pf_value(h):
        return 3*mf*b*(a*h+z1)**2-24*mf*b*cf-m2*mg*Af
    pflo=pf_value(low);pfhi=pf_value(high)
    if not(pg>F('.8855') and pflo>F('.1242') and pfhi>pflo):
        raise AssertionError('positive normalized center dust not certified')
    # J(y)>0 is a required nonzero implicit coefficient.
    J=b1+2*b2*y+b3*y*y
    if J<=F('0.65'):raise AssertionError('J center chart not nondegenerate')
    return {'pg_center_normalized_exact':str(pg),
            'pf_center_normalized_lower_exact':str(pflo),
            'pf_center_normalized_upper_exact':str(pfhi),
            'pg_center_display':float(pg),'pf_center_lower_display':float(pflo),
            'U0_lower_exact':str(u0lo),'U0_upper_exact':str(u0hi),
            'U0_display':float((u0lo+u0hi)/2),
            'J_center_exact':str(J),'J_display':float(J),
            'H_sqrt_grid_digits':digits}


def theorem_manifest():
    p=exact_center_parity();q=benchmark_center_positive_dust()
    return {'step':49,'center_equation':'2*s*U_s=G(s,U)-2U; G(0,U)=3 U0-U',
            'indicial_root':'-3/2','pLf_singular_homogeneous':'C/r',
            'analytic_local_existence':'CONDITIONAL_THEOREM',
            'theorem_hypotheses':[
                'Original six-pair spherical HR action and f lapse/radial primaries',
                'Prescribed g primary and all background radial source fields real analytic even in s',
                'S_i=r L_i, z=r z1(s), canonical and dust parity as explicitly substituted',
                'S_f_prime, J, dust denominator, sector masses and spatial metric denominators nonzero',
                'Compact-support lapse smearings or independently controlled boundary traces'],
            'proof':'Scaled physical C/r² is exactly even analytic under parity. Its W=pLf_prime/r coefficient is nonzero at center, so implicit analytic G exists with G(0,U)=3U0-U. Write s U_s=-3/2(U-U0)+s R(s,U)/2. Volterra fixed-point w(s)=s^-3/2/2 integral_0^s t^3/2 R(t,U0+w(t)) dt is locally contractive for small s, providing unique bounded analytic solution; the homogeneous C*s^-3/2 is excluded. Center dust positivity and J>0 follow exact rational enclosures.',
            'center_dust_certificate':q,
            'NOT_PROVED':['global analytic continuation to r=.85',
                          'rigorous ODE error bound on the numerical outward integration',
                          'uniform positive dust along the entire new nonpolynomial interval',
                          'Dirac secondary time preservation','lapse fixing or physical ghost freedom'],
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(theorem_manifest(),indent=2))

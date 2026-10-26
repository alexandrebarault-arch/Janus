"""Step68ad-B2: original six-pair physical G, continuous U_ss and U_sss.

Strictly conditional on the SHA-authenticated Step49/68v analytic-center
branch and original Step68ad-A comparison theorem. Uses 32+ closed rational
cells, outward 10^-28 interval arithmetic and four original Step68n jets.
Does NOT certify Step58 temporal Dirac coefficients or ghost freedom.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
import sympy as sp
from .hr_step55_normalized_secondary import normalized_symbolic
from . import hr_step55_global_barrier as old
from . import hr_step68n_interval_ode_jets as jets
from .hr_step68ad_b_directional_polarization import (
    physical_R2_global, physical_G_partials, source_R3)
from .hr_step68ad_center_derivative_transport import (
    load_physical_reports, damping_bounds, ratio_enclosure, blob_sha)

REQUIRED={
    'hr_step68ad_b_directional_polarization.py':'3d075699fb8266ddce2ee9b370afa85cb17f2c73',
    'hr_step68ad_center_derivative_transport.py':'3768d309f008391813c5fd70302ff487141afe1b',
}

def preflight():
    originals=jets.certify_sources()
    src=Path(__file__).resolve().parent
    for name,expected in REQUIRED.items():
        actual=blob_sha((src/name).read_bytes())
        if actual!=expected:raise ValueError(f'original derivative source drift {name}: {actual}')
    actual=blob_sha((src/'hr_step68n_interval_ode_jets.py').read_bytes())
    if actual!='96370e0599748c6dc07faf339ab3646ae3474e7d':
        raise ValueError('Original Step68n physical jets drift')
    return {**originals,**REQUIRED,'hr_step68n_interval_ode_jets.py':actual}


def as_pair(i):
    return [str(F(i.lo,old.S)),str(F(i.hi,old.S))]


def contains(i,value):
    f=F(value)
    return F(i.lo,old.S)<=f<=F(i.hi,old.S)


def exact_quadratic_G_certificate():
    """Original G is exactly quadratic in U, with G_UU=s*C(s)>0 for s>0.

    Analytic factorization is checked against the ORIGINAL symbolic six-pair
    expression. C is then bounded with the ORIGINAL outward interval engine
    over the entire continuum [0,1/1024], not point samples.
    """
    expr,s,u,v=normalized_symbolic()
    Lf,Lg,tf=v['Lf'],v['Lg'],v['tf']
    mf=v['mf'];b1,b2,b3=v['beta'][1:4];z1=v['z1']
    root=sp.sqrt(1-s*z1**2)
    at=Lf**2*b3+2*Lf*Lg*b2+Lg**2*b1
    bracket=(3*Lf**2*b3*root+2*Lf*Lg*b2*root
             +4*Lf*Lg*b2-Lg**2*b1*root+4*Lg**2*b1)
    C=-tf*bracket/(2*Lf*mf*sp.sqrt(Lf**2+s*tf**2)*root*at)
    if sp.diff(expr,u,3)!=0:
        raise AssertionError('Physical G no longer exactly quadratic in U')
    if sp.simplify(sp.diff(expr,u,2)-s*C)!=0:
        raise AssertionError('Exact six-pair G_UU=s*C factorization failed')
    interval_s=old.I.hull(0,F(1,1024))
    g=old.geometry(interval_s)
    lf,lg,tf0=g['Lf0'],g['Lg0'],g['tf0']
    rr=(1-interval_s*old.Z1**2).sqrt()
    at0=lf**2*old.B3+2*lf*lg*old.B2+lg**2*old.B1
    br=(3*lf**2*old.B3*rr+2*lf*lg*old.B2*rr
        +4*lf*lg*old.B2-lg**2*old.B1*rr+4*lg**2*old.B1)
    c=-tf0*br/(2*lf*old.MF*(lf**2+interval_s*tf0**2).sqrt()*rr*at0)
    if not (at0.lo>0 and br.lo>0 and tf0.hi<0 and c.lo>0):
        raise ArithmeticError('Positive original quadratic coefficient not certified')
    return {'original_G_polynomial_degree_U_exact':2,
            'G_UUU_identically_zero':True,
            'G_UU_equals_s_times_C_exact':True,
            'C_full_domain_outward_interval':as_pair(c),
            'At_positive':True,'bracket_positive':True,
            'tf0_negative':True,'G_UU_strict_positive_for_s_gt_zero':True,
            's_domain':['0','1/1024']}


def certify(folder:Path|str,cells:int=32):
    """Certificate on every s in [0,1/1024], including s=0.

    R2 first encloses U_ss via positive transport; that GLOBAL U_ss tube
    is then inserted into the genuine R3 chain rule on every closed cell.
    This is not differentiating interval enclosures of U or U_s.
    """
    if not isinstance(cells,int) or not 8<=cells<=2048:
        raise ValueError('cells outside certified verifier range')
    sources=preflight()
    quadratic=exact_quadratic_G_certificate()
    reports=load_physical_reports(folder)
    v,ac=reports['68v'],reports['68ac']
    r2=physical_R2_global(folder,cells=cells)
    uss=old.I.hull(*map(F,r2['U_ss_global_enclosure']))
    us=old.I.hull(F(v['U_s_center_lower_rational']),F(v['U_s_center_upper_rational']))
    if us.lo<=0:raise ArithmeticError('Original U_s strictly positive hypothesis lost')
    kap=old.I.c(F(1,10000000))
    smax=F(1,1024)
    lo=10**100;hi=-10**100
    rows=[]
    for i in range(cells):
        left=smax*i/cells;right=smax*(i+1)/cells
        s=old.I.hull(left,right)
        star,_,_=old.stars(s)
        delta=kap*s**3
        utube=old.I(star.lo-delta.hi,star.hi+delta.hi)
        partials=physical_G_partials(s,utube)
        r3=source_R3(partials,us,uss)
        lo=min(lo,r3.lo);hi=max(hi,r3.hi)
        rows.append({'s':[str(left),str(right)],'R3':as_pair(r3)})
    r3global=old.I(lo,hi)
    a3=damping_bounds(v['G_U_center_interval'],3)
    ussspair=ratio_enclosure(tuple(map(F,as_pair(r3global))),a3)
    usss=old.I.hull(*ussspair)
    # Exact analytic-center coefficients are independently pinned by Step68ac.
    u2lo,u2hi=map(F,ac['original_U2_interval'])
    u3lo,u3hi=map(F,ac['original_Step67b_U3_interval'])
    if not (contains(uss,2*u2lo) and contains(uss,2*u2hi)):
        raise ArithmeticError('Original U_ss(0)=2U2 not included')
    if not (contains(usss,6*u3lo) and contains(usss,6*u3hi)):
        raise ArithmeticError('Original U_sss(0)=6U3 not included')
    if not (r3global.hi<0 and usss.hi<0):
        raise ArithmeticError('Negative physical R3/U_sss not certified')
    if F(r2['R2_global_enclosure'][1])>=0 or F(r2['U_ss_global_enclosure'][1])>=0:
        raise ArithmeticError('Negative physical R2/U_ss not certified')
    if len(rows)!=cells or rows[0]['s'][0]!='0' or rows[-1]['s'][1]!='1/1024':
        raise AssertionError('Closed continuum partition incomplete')
    return {
        'step':'68ad-B2','status':'CONDITIONAL_RIGOROUS_PHYSICAL_CONTINUUM_HIGHER_JETS',
        'original_sources_verified':sources,
        'original_quadratic_G_structure':quadratic,
        'original_report_sha':{'68v':'d83a3b80862a2e990a4c4879ec8745a4e91c8b34',
                               '68ac':'16ae8dab3563c17134e4e20f886fb7306dc2e4ba'},
        's_domain':['0','1/1024'],'r_domain':['0','1/32'],
        'cells':cells,
        'R2_global':r2['R2_global_enclosure'],
        'a2_global':r2['a2_global_enclosure'],
        'U_ss_global':r2['U_ss_global_enclosure'],
        'R3_global':as_pair(r3global),
        'a3_global':list(map(str,a3)),
        'U_sss_global':list(map(str,ussspair)),
        'center_U_ss_2U2_included':True,
        'center_U_sss_6U3_included':True,
        'strict_negative_R2_U_ss_R3_U_sss':True,
        'R2_cells':r2['cells'],
        'R3_cells':rows,
        'method':'Original Step45/46/55 G through SHA-authentic Step68n Jet; four directional partials, Step68v certified U and U_s, Step68ad-A positive-kernel transport for U_ss then U_sss. Rational closed-cell cover; no division by s.',
        'scope':'Conditional on historical Step49 analytic regular center, Step68v cubic tube and slope proof, and exact original interval implementation. Only spatial higher derivatives, not temporal Dirac rank.',
        'temporal_Step58_A_N_A_M':'NOT_COMPUTED',
        'full_Dirac_rank':'NOT_COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
        'next_step':'68ad-C: reconstruct original Step58/60/68o, feed these rigorously enclosed U_ss and U_sss into original 12 canonical jets on seven pending cells r in [1/64,1/32], then r→0. Never differentiate coarse U/U_s tubes.'}


def main():
    import sys
    if len(sys.argv)<2 or len(sys.argv)>3:
        raise SystemExit('usage: python -m numerics.hr_step68ad_b2_physical_center_higher_jets research/reports [cells]')
    print(json.dumps(certify(sys.argv[1],int(sys.argv[2]) if len(sys.argv)==3 else 32),indent=2))

if __name__=='__main__':main()

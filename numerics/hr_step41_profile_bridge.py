"""Step41: link actual Step39 corrected momentum to Step40 continuous positivity.

Conservative inference, not a Dirac secondary proof.  The exact Step40
interval certificate covers EVERY coefficient in a closed, independent
five-dimensional even-polynomial ball. Its validity for the SPECIFIC Step39
profile follows by exact rational tests on its 9 finite Python floats.

The numerical local secondary remains a near-zero, not an exact equality.
"""
from __future__ import annotations
from fractions import Fraction as F
import hashlib
import json
import math
import numpy as np
from .hr_step39_highorder_secondary import solve_five_point,local_five_point
from .hr_step40_twodust_interval import interval_two_dust_certificate
from .hr_step40_curvature_box import exact_box_certificate

BALL=F('0.005')
RMAX=F('0.85')


def coefficient_membership(values, limit=BALL):
    """Use exact rational representations of binary64, not float tolerances."""
    try:
        values=tuple(float(x) for x in values)
        limit=F(limit)
    except (ValueError,TypeError,OverflowError) as exc:
        raise ValueError('finite coefficients and rational limit required') from exc
    if len(values)!=9 or not all(math.isfinite(x) for x in values):
        raise ValueError('exactly 9 finite coefficients required for degree-4 generator')
    if limit<=0:raise ValueError('positive coefficient bound required')
    if any(values[i] != 0.0 for i in (1,3,5,7)):
        raise ValueError('odd spherical-parity coefficients cannot be nonzero')
    rationals=[F.from_float(v) for v in values]
    largest=max(abs(rationals[i]) for i in (0,2,4,6,8))
    if largest>limit:raise ArithmeticError('profile exits certified polynomial ball')
    return {'coefficients_float':list(values),
            'max_abs_even_float':float(largest),
            'strict_margin_exact':str(limit-largest),
            'inside_closed_ball':True,
            'all_odd_exact_zero':True,
            'limit_exact':str(limit)}


def certified_step41_profile(*,h=.001,iterations=6,degree=4,
                             points=73,ncells=256):
    """Re-run corrected data and JOIN established mathematical certificates.

    Sampled secondary and primaries are diagnostics only. Interval guarantees
    apply to ALL r in [0,.85] and are not derived from these samples.
    """
    if not isinstance(points,int) or points<10 or points>301:
        raise ValueError('sample grid count outside controlled range')
    if degree!=4:raise ValueError('certified polynomial correction family is degree 4')
    w,fit=solve_five_point(scale=.1,degree=degree,iterations=iterations,h=h)
    last=fit['history'][-1]
    membership=coefficient_membership(last['f_delta'])
    dust=interval_two_dust_certificate(ncells=ncells,
                f_delta_per_coefficient_bound=BALL)
    chart=exact_box_certificate()
    if F(dust['strict_pg_over_r2_lower'])<=F('0.885'):
        raise ArithmeticError('g dust positivity theorem not verified')
    if F(dust['strict_pf_over_r2_lower'])<=F('0.039'):
        raise ArithmeticError('f dust positivity theorem not verified')
    if F(chart['J_uniform_lower_exact'])<=F(1,2):
        raise ArithmeticError('J chart theorem not verified')
    if F(chart['K_div_r2_uniform_lower_exact'])<=0:
        raise ArithmeticError('K chart theorem not verified')
    # Include endpoints in sampled data; limit h=0.001 and r_min>0.025+2h.
    rr=np.linspace(.03,float(RMAX),points)
    local=np.array([local_five_point(w,float(r),h)[0] for r in rr])
    fields=w.eval(rr,('Hg','Hf','Ddiag','Fz','pg','pf','z','K'))
    data={'radii':int(points),'r_min':float(rr[0]),'r_max':float(rr[-1]),
          'max_abs_local_C':float(np.max(abs(local))),
          'max_abs_local_C_over_r2':float(np.max(abs(local/rr**2))),
          'max_abs_primary':float(np.max(abs(fields[:4]))),
          'sampled_min_pg_over_r2':float(np.min(fields[4]/rr**2)),
          'sampled_min_pf_over_r2':float(np.min(fields[5]/rr**2))}
    if data['max_abs_primary']>1e-10 or data['max_abs_local_C']>2e-9:
        raise ArithmeticError('primary or local approximate-secondary test failed')
    if data['sampled_min_pg_over_r2']<=0 or data['sampled_min_pf_over_r2']<=0:
        raise ArithmeticError('sampled physical dust sign failure')
    canonical=json.dumps(membership['coefficients_float'],separators=(',',':'))
    return {'step':41,'source':'recomputed Step39 solve_five_point',
            'settings':{'scale':0.1,'degree':degree,'h':h,
                        'iterations':iterations},
            'membership':membership,
            'coefficient_sha256':hashlib.sha256(canonical.encode()).hexdigest(),
            'actual_profile_continuum_positive_two_dust':True,
            'continuous_dust_certificate':dust,
            'continuous_spatial_chart_certificate':chart,
            'dense_sample_diagnostics':data,
            'proof_transfer':'Step39 numerical coefficients lie in exact Step40 all-coefficient ball; exact interval positive dust theorem applies to the ACTUAL profile',
            'secondary_exact_zero':'NOT_PROVED',
            'Dirac_time_preservation':'NOT_DERIVED',
            'lapse_fixing':'NOT_DERIVED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(certified_step41_profile(),indent=2))

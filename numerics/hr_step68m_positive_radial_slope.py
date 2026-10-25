"""Step68m: prove strictly positive U_s on r in [1/8,17/20] by intervals.

A follow-on exact spatial property of unique regular-center Step55 radial
branch using Step68l's 100x tighter certified global enclosure.
This is NOT a certificate of temporal lapse signs or ghost freedom.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
from .hr_step55_global_barrier import I, S, stars, G
from .hr_step68l_refined_global_barrier import narrowed_global_barrier,authentic_originals

PIN68L='2a1ffc026a30abf41208b44a707dc869daf0929d'


def authenticate_chain():
    original=authentic_originals()
    src=Path(__file__).with_name('hr_step68l_refined_global_barrier.py').read_bytes()
    git=sha1(b'blob '+str(len(src)).encode()+b'\0'+src).hexdigest()
    if git!=PIN68L:raise ValueError('Step68l certified source changed: '+git)
    return original


def certify_positive_Us(cells=8192,lo_s='1/64',hi_s='289/400',delta_U='1/1000000',rerun_global=True):
    authenticate_chain()
    low,high,du=F(lo_s),F(hi_s),F(delta_U)
    if not isinstance(cells,int) or not 256<=cells<=32768:raise ValueError('bad cell count')
    if not F(0)<low<high<=F(289,400):raise ValueError('need strictly positive s')
    if du!=F(1,1000000):raise ValueError('requires certified exact Step68l tube 1e-6')
    if rerun_global:
        cert=narrowed_global_barrier(16384,'0.000001','0.00005')
        assert F(cert['strict_max_Fupper'])<0 and F(cert['strict_min_Flower'])>0
        assert F(cert['U_minus_Ustar_abs_lt'])==du
    D=I.c(du); lower=10**100;upper=-10**100
    for i in range(cells):
        s=I.hull(low+(high-low)*i/cells, low+(high-low)*(i+1)/cells)
        u,_,_=stars(s)
        eligible=I(u.lo-D.hi,u.hi+D.hi)
        us=(G(s,eligible)-2*eligible)/(2*s)
        if us.lo<=0:
            raise ArithmeticError(f'slope U_s sign not certified in slab {i}/{cells}: {us}')
        lower=min(lower,us.lo);upper=max(upper,us.hi)
    return {
        'step':'68m',
        'original_physical_shas':authentic_originals(),
        'Step68l_pinned_git_blob':PIN68L,
        'Step68l_certification_reexecuted':rerun_global,
        'grid_cells':cells,
        's_interval':[str(low),str(high)],
        'r_interval':['1/8','17/20'] if (low,high)==(F(1,64),F(289,400)) else ['sqrt(smin)','sqrt(smax)'],
        'U_enclosure':'Ustar(s)+[-1/1000000,+1/1000000] verified Step68l',
        'exact_ode':'2*s*U_s=G(s,U)-2*U',
        'strict_lower_U_s':str(F(lower,S)),
        'upper_U_s':str(F(upper,S)),
        'whole_closed_interval_positive':lower>0,
        'outward_arithmetic_scale':S,
        'small_center_r_below_1_8_covered':False,
        'temporal_lapse_A_coefficients_certified':False,
        'Dirac_rank':'NOT_COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }

if __name__=='__main__':print(json.dumps(certify_positive_Us(),indent=2))

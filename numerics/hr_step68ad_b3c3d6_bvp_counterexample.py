"""b3c3d6: exact counterexample to inferring a global positive-lapse BVP
from the pointwise Step58 first-jet projection. TOY operators, NOT Step58.
"""
from fractions import Fraction as F
import json
import sympy as sp


def certificate():
    r = sp.symbols('r', real=True)
    R = sp.Rational(17, 20)
    lo, hi = sp.Rational(1037, 2000), sp.Rational(2593, 5000)
    rho = (lo + hi) / 2
    S, D = 1 + rho, 1 - rho
    phi = (r / R)**2
    N = sp.factor((S + D*(1-phi))/2)
    M = sp.factor((S - D*(1-phi))/2)
    kappa = sp.factor(2*D/(S*R**2))
    # Both first-order scalar operators have IDENTICAL nonzero B=(1,-1).
    # L_bad=N'-M' and L_good=N'-M'+kappa*r*(N+M).
    bad = sp.factor(sp.diff(N-M, r))
    good = sp.factor(bad + kappa*r*(N+M))
    zeros = {
        'N_center': N.subs(r,0)-1,
        'M_center': M.subs(r,0)-rho,
        'N_even': sp.diff(N,r).subs(r,0),
        'M_even': sp.diff(M,r).subs(r,0),
        'outer_equal': (N-M).subs(r,R),
        'good_operator': good,
        'sum_constant': N+M-S,
        'difference_quadratic': N-M-D*(1-phi),
        'unique_good_difference': D-kappa*S*R**2/2,
        'bad_solution_difference_constant': (1-rho)-D,
    }
    for name, value in zeros.items():
        if sp.cancel(value) != 0:
            raise AssertionError((name,value))
    signs = {
        'rho_inside_b3c2_bounds': lo < rho < hi,
        'rho_positive': rho > 0,
        'rho_less_than_one': rho < 1,
        'D_positive': D > 0,
        'kappa_positive': kappa > 0,
        'bad_outer_difference_nonzero': D != 0,
    }
    if not all(signs.values()):
        raise AssertionError(signs)
    # N,M are strictly positive on [0,R]: N >= S/2, M >= rho.
    assert sp.factor(N-S/2) == sp.factor(D*(1-phi)/2)
    assert sp.factor(M-rho) == sp.factor(D*phi/2)
    # For L_bad, every C1 solution has (N-M)'=0; the prescribed center
    # difference D>0 cannot become zero at R. This is a global no-solution
    # result for the toy BVP, despite local jet projection rank 2 everywhere.
    return {
        'step':'b3c3d6', 'scope':'EXACT_TOY_BVP_COUNTEREXAMPLE_NOT_ORIGINAL_STEP58',
        'R':str(R), 'rho':str(rho), 'kappa':str(kappa),
        'B_both':['1','-1'], 'pointwise_endpoint_projection_rank_both':2,
        'good_operator':'Nprime-Mprime+kappa*r*(N+M)',
        'bad_operator':'Nprime-Mprime',
        'N_good':str(N), 'M_good':str(M),
        'good_global_positive_even_solution':True,
        'bad_global_solution_with_same_center_and_equal_outer':False,
        'symbolic_zero_residuals':len(zeros), 'exact_sign_checks':len(signs),
        'original_step58_probe_executed':False,
        'GATE_2B':'OPEN', 'JANUS_R':'NOT_VALIDATED'
    }


if __name__ == '__main__':
    print(json.dumps(certificate(),indent=2,ensure_ascii=False))

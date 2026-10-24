"""Exact Step66 normalized center shift Jacobian/Hessian: benchmark-only.

Synthetic algebra tests do not claim to reexecute original Step55 interval code.
"""
from fractions import Fraction as F
import sympy as sp
import pytest
from numerics.hr_step66_center_shift_implicit_condition import (
    normalized_shift_identity,exact_global_bounds,
    parity_preserving_shift_variation,fail_closed_parameters,manifest,
    S_MAX,R_MAX,K_LOWER,W_BENCH)

@pytest.fixture(scope='module')
def p():return normalized_shift_identity()


def test_exact_original_stationarity_after_radial_normalization(p):
    r=sp.symbols('r',positive=True)
    s,d,k,w=p['s'],p['d'],p['k'],p['w']
    Dg=r**3*d;K=r**2*k;z=r*w
    original=Dg-K*z/sp.sqrt(1-z*z)
    normalized=p['Fhat'].subs(s,r*r)
    assert sp.simplify(original/r**3-normalized)==0


def test_normalized_stationarity_derivative_strictly_nonzero_even_center(p):
    assert sp.simplify(p['Fhat_w']+p['k']/p['t']**sp.Rational(3,2))==0
    assert p['Fhat_w'].subs(p['s'],0)==-p['k']


def test_stationary_root_satisfies_normalized_Fz_at_positive_k():
    s,d,k=sp.symbols('s d k',positive=True)
    W=d/sp.sqrt(k*k+s*d*d)
    expr=d-k*W/sp.sqrt(1-s*W*W)
    assert sp.simplify(expr)==0


def test_first_derivatives_of_normalized_shift_from_exact_root(p):
    assert sp.simplify(p['Wd']-p['k']**2/p['root']**3)==0
    assert sp.simplify(p['Wk']+p['k']*p['d']/p['root']**3)==0


def test_hessian_symmetry_of_exact_root(p):
    assert sp.simplify(sp.diff(p['Wd'],p['k'])-sp.diff(p['Wk'],p['d']))==0
    assert p['Wdk']!=0


def test_on_shell_first_derivatives_with_sqrt_branch(p):
    s,k,w=p['s'],p['k'],p['w']
    dvalue=k*w/sp.sqrt(1-s*w*w)
    # Use physically positive (s,k,w) rationals to avoid spurious abs issues.
    sample={s:sp.Rational(1,4),k:sp.Rational(1,2),w:sp.Rational(1,250)}
    for true,proposed in ((p['Wd'],p['wd']),(p['Wk'],p['wk']),
                          (p['Wdd'],p['wdd']),(p['Wdk'],p['wdk']),(p['Wkk'],p['wkk'])):
        assert sp.simplify(true.subs(p['d'],dvalue).subs(sample)-proposed.subs(sample))==0


def test_direct_implicit_function_first_derivative_identity(p):
    assert sp.simplify(sp.diff(p['Fhat'],p['d'])+p['Fhat_w']*p['wd'])==0
    assert sp.simplify(sp.diff(p['Fhat'],p['k'])+p['Fhat_w']*p['wk'])==0


def test_second_derivative_dd_from_root(p):
    assert sp.simplify(p['Wdd']+3*p['s']*p['k']**2*p['d']/p['root']**5)==0


def test_mixed_second_derivative_from_root(p):
    assert sp.simplify(p['Wdk']-p['k']*(2*p['s']*p['d']**2-p['k']**2)/p['root']**5)==0


def test_second_derivative_kk_from_root(p):
    assert sp.simplify(p['Wkk']-p['d']*(2*p['k']**2-p['s']*p['d']**2)/p['root']**5)==0


def test_strict_rational_physical_benchmark_domain():
    out=exact_global_bounds()
    assert S_MAX==F(289,400) and R_MAX==F(17,20)
    assert F(out['t_min_exact'])>F(9999,10000)
    assert out['center_included']


def test_benchmark_normalized_first_derivative_bounds():
    b=exact_global_bounds()
    assert F(b['dw_dd_abs_le'])==F(1000,229)<F(22,5)
    assert F(b['dw_dk_abs_le'])==F(4,229)<F(1,50)


def test_rational_hessian_bounds_prove_global_C2_conditioning():
    b=exact_global_bounds()
    w=b['computational_witness_hessian_caps']
    assert F(w['wdd'])<F(1,5)
    assert F(w['wdk'])<F(20)
    assert F(w['wkk'])<F(1,5)


def test_center_wd_wk_and_hessian_are_finite(p):
    a=p['wd'].subs(p['s'],0)
    b=p['wk'].subs(p['s'],0)
    assert a==1/p['k']
    assert b==-p['w']/p['k']
    assert p['wdd'].subs(p['s'],0)==0
    assert p['wdk'].subs(p['s'],0)==-1/p['k']**2
    assert p['wkk'].subs(p['s'],0)==2*p['w']/p['k']**2


def test_parity_preserving_delta_z_has_explicit_radial_factor():
    obj=parity_preserving_shift_variation()
    r=sp.Symbol('r',nonnegative=True)
    assert sp.simplify(obj['delta_z']-r*obj['delta_w'])==0
    assert obj['delta_d'] in obj['delta_w'].free_symbols
    assert obj['delta_k'] in obj['delta_w'].free_symbols


def test_normalized_center_shift_nonzero_hessian_not_artificial_zero():
    p=normalized_shift_identity()
    assert p['wkk'].subs({p['s']:0,p['w']:W_BENCH})!=0
    assert p['wdk'].subs(p['w'],W_BENCH)!=0


def test_fail_closed_if_wrong_interval():
    with pytest.raises(ValueError,match='Unsupported radial chart'):
        fail_closed_parameters(0,F(3,4),K_LOWER,W_BENCH)
    with pytest.raises(ValueError,match='Unsupported radial chart'):
        fail_closed_parameters(F(1,100),S_MAX,K_LOWER,W_BENCH)


def test_fail_closed_if_wrong_positive_K_or_shift():
    with pytest.raises(ValueError,match='Benchmark'):
        fail_closed_parameters(0,S_MAX,F(1,10),W_BENCH)
    with pytest.raises(ValueError,match='Benchmark'):
        fail_closed_parameters(0,S_MAX,K_LOWER,F(1,50))
    assert fail_closed_parameters(0,S_MAX,K_LOWER,W_BENCH)['center_included']


def test_zero_K_branch_not_invertible():
    p=normalized_shift_identity()
    assert p['Fhat_w'].subs(p['k'],0)==0
    assert p['wd'].has(p['k'])
    # The source theorem explicitly excludes k=0 (J/other charts need work).
    assert K_LOWER>0


def test_report_never_claims_temporal_Dirac_completion():
    m=manifest()
    assert m['step']==66
    assert not m['physical_original_Step45_55_imported_in_this_module']
    assert m['original_full_temporal_Dirac_on_Step55']=='NOT_COMPUTED'
    assert m['lapse_rank_and_fixing']=='NOT_COMPUTED'
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'

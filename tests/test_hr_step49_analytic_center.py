"""Exact original-action parity, center-dust Fraction enclosures and local-IVP hypotheses."""
from fractions import Fraction as F
import sympy as sp
import pytest
from numerics.hr_step49_analytic_center import (
    exact_center_parity,benchmark_center_positive_dust,theorem_manifest)
from numerics.hr_step49_regular_center_shoot import estimate_u1


@pytest.fixture(scope='module')
def exact():return exact_center_parity()


@pytest.fixture(scope='module')
def dust():return benchmark_center_positive_dust()


def test_exact_scaled_physical_secondary_even_in_radius(exact):
    r=exact['r'];expr=exact['C_div_r2']
    assert sp.cancel(expr.subs(r,-r)-expr)==0


def test_exact_leading_C_after_original_f_primaries(exact):
    assert exact['checks']['exact_finite_center_leading_formula']==0
    assert exact['leading']!=0


def test_regular_center_implicit_formula_exact(exact):
    A,B,Pg,U,W,z1,mg,mf,m2=exact['symbols']
    assert sp.cancel(exact['W_implicit']-(3*exact['U0']-U))==0
    assert sp.simplify(exact['U0']-mf*B*(Pg/(mg*A)-2*z1))==0


def test_nonzero_implicit_C_coefficient_given_J_positive(exact):
    assert exact['dCbar_dW_at_center']!=0
    assert exact['checks']['nonzero_W_coefficient']==0


def test_rational_center_both_normalized_dusts_positive(dust):
    assert F(dust['pg_center_normalized_exact'])>F('.8855')
    assert F(dust['pf_center_normalized_lower_exact'])>F('.1242')


def test_very_narrow_outward_center_sqrt_enclosure(dust):
    lo=F(dust['U0_lower_exact']);hi=F(dust['U0_upper_exact'])
    assert lo<hi and hi-lo<F('1e-48')
    plo=F(dust['pf_center_normalized_lower_exact'])
    phi=F(dust['pf_center_normalized_upper_exact'])
    assert 0<phi-plo<F('1e-46')


def test_center_J_nonzero_certifies_implicit_chart(dust):
    assert F(dust['J_center_exact'])>F('.65')


def test_first_even_coefficient_compatible_with_local_analytic_series():
    # Volterra fixed point for constant analytic R=r0 has w=R*s/5.
    s,R0=sp.symbols('s R0',positive=True)
    t=sp.symbols('t',positive=True)
    w=sp.integrate(t**sp.Rational(3,2)*R0/2,(t,0,s))/s**sp.Rational(3,2)
    assert sp.simplify(w-R0*s/5)==0
    assert .0007897<estimate_u1()<.0007898


def test_rational_center_result_independent_of_sqrt_grid_refinement():
    coarse=benchmark_center_positive_dust(25)
    fine=benchmark_center_positive_dust(50)
    assert F(coarse['pf_center_normalized_lower_exact'])<=F(fine['pf_center_normalized_lower_exact'])
    assert F(coarse['pf_center_normalized_upper_exact'])>=F(fine['pf_center_normalized_upper_exact'])


def test_bad_sqrt_precision_fails_closed():
    for x in (5,200,12.2):
        with pytest.raises(ValueError):benchmark_center_positive_dust(x)


def test_analytic_local_theorem_not_global_ghost_claim():
    m=theorem_manifest()
    assert m['analytic_local_existence']=='CONDITIONAL_THEOREM'
    assert 'global analytic continuation to r=.85' in m['NOT_PROVED']
    assert 'Dirac secondary time preservation' in m['NOT_PROVED']
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'

"""Targeted exact-arithmetic proof and negative controls, not a full BD test."""
from fractions import Fraction as F
import pytest
from numerics.candidate_c_continuous_j_certificate import (
    A_LOW, A_HIGH, Y_LOW, Y_HIGH, MF2, CG, CF, M2, BETAS, Y0,
    q_coefficients, j_value, t_of_y, t_derivative_num,
    verified_bounds, unique_y_interval, witness, manifest)


def test_global_strict_inequality_certificate():
    m=verified_bounds()
    assert m['J_global_lower_strict']=='1/2'
    assert m['J_at_lower']>.5
    assert m['t_lower']<1<m['t_upper']
    assert m['t_upper']>64000


def test_quartic_is_exactly_eliminated_by_rational_parametrization():
    for y in (F('.5569'),F('.57'),F('1.1'),F('2.29')):
        t=t_of_y(y)
        q=q_coefficients()
        value=sum(c*y**i for i,c in enumerate(q))
        assert M2*value+(MF2*CG*y-CF)*t/3==0


@pytest.mark.parametrize('a',('1','.9','.4','.09','.0301646','.03','.025'))
def test_unique_root_exact_bisection_brackets(a):
    lo,hi=unique_y_interval(a)
    assert Y_LOW<lo<hi<Y_HIGH
    assert t_of_y(lo)<F(a)**-3<t_of_y(hi)
    assert hi-lo==(Y_HIGH-Y_LOW)/2**85
    assert j_value(lo)>F(1,2)
    assert witness(a)['relative_t_bracket']<1.e-20


def test_strict_monotonicity_analytic_proof_boundaries():
    q=q_coefficients()
    assert q[3]>0 and q[4]>0
    assert t_derivative_num(Y_LOW)>0
    assert t_derivative_num(Y_HIGH)>0
    assert j_value(Y_LOW)>F(1,2)
    assert BETAS[2]+BETAS[3]*Y_LOW>0
    assert CF-MF2*CG*Y_HIGH>0
    # No extrapolation beyond the denominator pole y=CF/(MF2*CG).
    assert Y_HIGH<CF/(MF2*CG)


def test_first_fold_has_positive_nonzero_J_but_not_kinetic_conclusion():
    c=witness('.0301646')
    assert c['J_mid']>1
    assert .556<c['y_mid']<2.3
    assert 'lapse fixing remain OPEN' in manifest()['limitations'][-1]


def test_source_y0_is_calibrated_decimal_not_exact_equation_root():
    # This ~1e-13 residual is not allowed to masquerade as an exact equality.
    assert abs(float(t_of_y(Y0)-1))<1e-10
    assert t_of_y(Y0)!=1


@pytest.mark.parametrize('invalid',('.0249999','1.00000001','-1'))
def test_out_of_range_rejected(invalid):
    with pytest.raises(ValueError):unique_y_interval(invalid)


@pytest.mark.parametrize('iterations',(0,-1,129,1.2))
def test_bad_bisection_rejected(iterations):
    with pytest.raises(ValueError):unique_y_interval('0.4',iterations)

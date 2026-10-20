"""Executable checks for restricted regular-center secondary rigidity."""
import numpy as np
import pytest
from numpy.polynomial import Polynomial as Poly
from numerics.hr_regular_secondary_flat import (
    BETAS,FlatData,MF2,MG2,M2,Y04,candidate_y,j_value,j_roots,
    polynomial_interval_minimum,regular_inverse_rhs,synchronized_candidate
)

def test_primary_and_secondary_pointwise_with_two_positive_dusts():
    w=synchronized_candidate()
    p_g,p_f=w.dust_density_over_r2()
    # The exact extrema of density/r^2 over the full [0,1] interval:
    lo_g,xg=polynomial_interval_minimum(p_g)
    lo_f,xf=polynomial_interval_minimum(p_f)
    assert min(lo_g,lo_f)>0
    assert not np.allclose(p_g.coef,p_f.coef)
    assert max(abs(w.secondary_polynomial().coef))<3e-15
    for r in (.1,.24,.43,.7,1.):
        assert max(abs(w.primary_residuals(r)))<4e-14

@pytest.mark.parametrize("eps",[-.15,-.08,0,.08,.15])
def test_open_regular_positive_family_not_only_one_hand_tuned_shape(eps):
    w=synchronized_candidate(eps)
    assert np.max(np.abs(w.secondary_polynomial().coef))<1e-14
    for p in w.dust_density_over_r2():
        assert polynomial_interval_minimum(p)[0]>0
    for r in (.14,.47,.82):
        assert np.max(np.abs(w.primary_residuals(r)))<4e-14

def test_nonzero_relative_momentum_has_nonzero_secondary():
    w=synchronized_candidate()
    # perturb f independently, rebuild both dust constraints from new Pf
    wp=FlatData(w.a,w.b,w.Pg,w.Pf+Poly([0.,.00025,.00015]))
    assert np.max(np.abs(wp.secondary_polynomial().coef))>1e-6
    for r in (.2,.4,.8):
        assert max(abs(wp.primary_residuals(r)))<4e-14
    assert all(polynomial_interval_minimum(p)[0]>0
               for p in wp.dust_density_over_r2())

def test_restricted_secondary_is_radial_total_derivative():
    w=synchronized_candidate()
    w=FlatData(w.a,w.b,w.Pg,w.Pf+Poly([.001,-.002,.0007]))
    rr=Poly([0.,1.]);x=w.x();pref=.5*M2*MG2*w.a**2*j_value(w.b/w.a)
    left=w.secondary_polynomial()
    right=pref*(rr**3*x).deriv()
    np.testing.assert_allclose(left.coef,right.coef,atol=1e-15)
    for r in (.2,.5,.8):
        assert left(r)==pytest.approx(pref*r*r*(3*x(r)+r*x.deriv()(r)),abs=2e-15)

def test_regular_center_kernel_is_trivial_but_singular_solution_exists():
    f=Poly([2.,-3.,4.,1.2])
    x=regular_inverse_rhs(f.coef)
    rr=Poly([0.,1.])
    np.testing.assert_allclose((3*x+rr*x.deriv()).coef,f.coef,atol=2e-15)
    # For f=0, general r>0 homogeneous solution is A*r^-3.
    for r in (.1,.3,.8):
        a=.03
        singular=a/r**3
        derivative=-3*a/r**4
        assert 3*singular+r*derivative==pytest.approx(0.,abs=1e-13)
    assert .03/.01**3>2e4 # violates finite P_i at the center

def test_J_degeneracy_is_outside_benchmark_and_not_misinterpreted():
    roots=np.sort(j_roots())
    np.testing.assert_allclose(roots,[.158524837,.46111868],atol=1e-7)
    assert all(j_value(candidate_y(a))>.5 for a in np.geomspace(.025,1.,30))
    w=synchronized_candidate()
    b=w.a*roots[-1]
    with pytest.raises(ValueError,match="degenerate"):
        FlatData(w.a,b,w.Pg,w.Pf).secondary_polynomial()

def test_invalid_inputs():
    with pytest.raises(ValueError):synchronized_candidate(.4)
    with pytest.raises(ValueError):synchronized_candidate(float("nan"))
    with pytest.raises(ValueError):polynomial_interval_minimum(Poly([1]),1,1)
    with pytest.raises(ValueError):candidate_y(.01)

import math
import numpy as np


def _elementary_from_diag(lams):
    l0,l1,l2,l3 = lams
    return np.array([
        1.0,
        l0+l1+l2+l3,
        l0*l1+l0*l2+l0*l3+l1*l2+l1*l3+l2*l3,
        l0*l1*l2+l0*l1*l3+l0*l2*l3+l1*l2*l3,
        l0*l1*l2*l3,
    ])


def test_identity_pullback_recovers_flrw_square_root_spectrum():
    from numerics.nonhomothetic_stueckelberg import spherical_square_root_invariants
    a = 0.73
    xi = 0.41
    alpha = a*xi
    n = 0.37
    r = 0.28
    out = spherical_square_root_invariants(
        a=a, r=r, n=n, alpha=alpha,
        T_t=1.0, T_r=0.0, R=r, R_t=0.0, R_r=1.0,
    )
    expected = _elementary_from_diag([n, xi, xi, xi])
    assert np.allclose(out.e, expected, rtol=2e-14, atol=2e-14)
    assert math.isclose(out.tr_spherical_block, n+xi, rel_tol=2e-14, abs_tol=2e-14)
    assert math.isclose(out.det_spherical_block, n*xi, rel_tol=2e-14, abs_tol=2e-14)
    assert math.isclose(out.angular_eigenvalue, xi, rel_tol=2e-14, abs_tol=2e-14)


def test_identity_interaction_density_matches_flrw_beta_polynomial():
    from numerics.nonhomothetic_stueckelberg import spherical_interaction_density
    a=0.81; xi=0.53; alpha=a*xi; n=0.47; r=0.19
    beta=(0.2,-0.7,1.1,-0.4,0.3)
    measured=spherical_interaction_density(
        a=a,r=r,n=n,alpha=alpha,betas=beta,
        T_t=1,T_r=0,R=r,R_t=0,R_r=1,
    )
    expected=(beta[0] + beta[1]*(n+3*xi)
              + beta[2]*(3*n*xi+3*xi*xi)
              + beta[3]*(3*n*xi*xi+xi**3)
              + beta[4]*n*xi**3)
    assert math.isclose(measured,expected,rel_tol=2e-14,abs_tol=2e-14)


def test_temporal_shift_reduces_to_aoki_eq64_on_homothetic_uniform_mode():
    from numerics.nonhomothetic_stueckelberg import temporal_shift_coefficient
    a=0.63; H=1.4; mu=-0.37; mudot=0.081
    measured=temporal_shift_coefficient(a=a,H_g=H,c=1.0,mu=mu,mu_dot=mudot)
    expected=-a*a*(mudot+H*mu*(2.0+mu))
    assert math.isclose(measured,expected,rel_tol=2e-14,abs_tol=2e-14)


def test_temporal_interaction_branch_factor_is_J_at_linear_map():
    from numerics.nonhomothetic_stueckelberg import temporal_interaction_branch_factor
    b1,b2,b3=1.2,-0.9,0.35; xi=0.47
    assert math.isclose(
        temporal_interaction_branch_factor(beta1=b1,beta2=b2,beta3=b3,xi=xi,mu=0.0),
        b1+2*b2*xi+b3*xi*xi, rel_tol=2e-14, abs_tol=2e-14,
    )


def test_nonhomothetic_temporal_shift_has_required_lapse_dependence():
    from numerics.nonhomothetic_stueckelberg import temporal_shift_coefficient
    a=0.72; H=0.83; c=0.61; mu=-0.44; mudot=0.052
    measured=temporal_shift_coefficient(a=a,H_g=H,c=c,mu=mu,mu_dot=mudot)
    expected=-(a*a/c)*(mudot+H*mu*(c+1.0+mu))
    assert math.isclose(measured,expected,rel_tol=2e-14,abs_tol=2e-14)

import math
import numpy as np


def _elementary_from_diag(lams):
    l0,l1,l2,l3 = lams
    return np.array([1.0,l0+l1+l2+l3,
        l0*l1+l0*l2+l0*l3+l1*l2+l1*l3+l2*l3,
        l0*l1*l2+l0*l1*l3+l0*l2*l3+l1*l2*l3,l0*l1*l2*l3])


def test_identity_pullback_recovers_flrw_square_root_spectrum():
    from numerics.nonhomothetic_stueckelberg import spherical_square_root_invariants
    a=0.73; xi=0.41; alpha=a*xi; n=0.37; r=0.28
    out=spherical_square_root_invariants(a=a,r=r,n=n,alpha=alpha,T_t=1,T_r=0,R=r,R_t=0,R_r=1)
    assert np.allclose(out.e,_elementary_from_diag([n,xi,xi,xi]),rtol=2e-14,atol=2e-14)
    assert math.isclose(out.tr_spherical_block,n+xi,rel_tol=2e-14,abs_tol=2e-14)
    assert math.isclose(out.det_spherical_block,n*xi,rel_tol=2e-14,abs_tol=2e-14)


def test_identity_interaction_density_matches_flrw_beta_polynomial():
    from numerics.nonhomothetic_stueckelberg import spherical_interaction_density
    a=0.81; xi=0.53; alpha=a*xi; n=0.47; r=0.19; beta=(0.2,-0.7,1.1,-0.4,0.3)
    measured=spherical_interaction_density(a=a,r=r,n=n,alpha=alpha,betas=beta,T_t=1,T_r=0,R=r,R_t=0,R_r=1)
    expected=(beta[0]+beta[1]*(n+3*xi)+beta[2]*(3*n*xi+3*xi*xi)+beta[3]*(3*n*xi*xi+xi**3)+beta[4]*n*xi**3)
    assert math.isclose(measured,expected,rel_tol=2e-14,abs_tol=2e-14)


def test_temporal_shift_reduces_to_aoki_eq64_on_homothetic_uniform_mode():
    from numerics.nonhomothetic_stueckelberg import temporal_shift_coefficient
    a=0.63; H=1.4; mu=-0.37; mudot=0.081
    assert math.isclose(temporal_shift_coefficient(a=a,H_g=H,c=1,mu=mu,mu_dot=mudot),-a*a*(mudot+H*mu*(2+mu)),rel_tol=2e-14,abs_tol=2e-14)


def test_temporal_interaction_branch_factor_is_J_at_linear_map():
    from numerics.nonhomothetic_stueckelberg import temporal_interaction_branch_factor
    b1,b2,b3=1.2,-0.9,0.35; xi=0.47
    assert math.isclose(temporal_interaction_branch_factor(beta1=b1,beta2=b2,beta3=b3,xi=xi,mu=0),b1+2*b2*xi+b3*xi*xi,rel_tol=2e-14,abs_tol=2e-14)


def test_nonhomothetic_temporal_shift_has_required_lapse_dependence():
    from numerics.nonhomothetic_stueckelberg import temporal_shift_coefficient
    a=0.72; H=0.83; c=0.61; mu=-0.44; mudot=0.052
    expected=-(a*a/c)*(mudot+H*mu*(c+1+mu))
    assert math.isclose(temporal_shift_coefficient(a=a,H_g=H,c=c,mu=mu,mu_dot=mudot),expected,rel_tol=2e-14,abs_tol=2e-14)


def test_homothetic_early_radial_polynomial_matches_aoki_eq68():
    from numerics.nonhomothetic_stueckelberg import homothetic_early_radial_polynomial_coefficients
    b1,b2,b3,K,w=1.0,-1.7,0.8,0.63,0.0
    measured=homothetic_early_radial_polynomial_coefficients(beta1=b1,beta2=b2,beta3=b3,K=K,w=w)
    D=b1+2*K*b2+K*K*b3; B2=(K*b2+K*K*b3)/D; B3=K*K*b3/D
    expected=np.array([-2*B2+(1+3*w)*B3,6*w*B2-2*B2-2,3*(w-1)])
    assert np.allclose(measured,expected,rtol=3e-14,atol=3e-14)


def test_nonhomothetic_radial_polynomial_reduces_to_homothetic_aoki_form():
    from numerics.nonhomothetic_stueckelberg import nonhomothetic_adiabatic_radial_polynomial_coefficients, homothetic_early_radial_polynomial_coefficients
    b1,b2,b3,K,w=1.0,-1.7,0.8,0.63,0.17
    raw=nonhomothetic_adiabatic_radial_polynomial_coefficients(beta1=b1,beta2=b2,beta3=b3,xi=K,c=1,Hdot_over_H2=-1.5*(1+w))
    normalized=homothetic_early_radial_polynomial_coefficients(beta1=b1,beta2=b2,beta3=b3,K=K,w=w)
    assert np.allclose(raw/raw[-1],normalized/normalized[-1],rtol=5e-14,atol=5e-14)


def test_y_tensor_sources_reproduce_aoki_eq98_to_101():
    from numerics.nonhomothetic_stueckelberg import homothetic_weak_metric_source_polynomials
    for b1,b2,b3,K,mu in ((1.0,-1.7,0.8,0.63,-0.31),(0.9,-0.6,0.22,0.47,0.18)):
        measured=homothetic_weak_metric_source_polynomials(beta1=b1,beta2=b2,beta3=b3,K=K,mu=mu)
        D=b1*K+2*b2*K*K+b3*K**3
        B2=(b2*K*K+b3*K**3)/D; B3=b3*K**3/D; q=1+mu
        expected=np.array([
            mu+B2*mu**2+B3*mu**3/3,
            -(mu-B3*mu**3/3),
            -(mu+(1+B2)*mu**2+(1+B2+B3)*mu**3/3)/q**3,
            +(mu+2*mu**2+(2+2*B2-B3)*mu**3/3)/q**3,
        ])
        assert np.allclose(measured,expected,rtol=3e-13,atol=3e-13)


def test_nonhomothetic_weak_metric_sources_reduce_to_homothetic_case():
    from numerics.nonhomothetic_stueckelberg import (
        nonhomothetic_weak_metric_source_polynomials,
        homothetic_weak_metric_source_polynomials,
    )
    args=dict(beta1=1.1,beta2=-0.73,beta3=0.29,xi=0.52,mu=-0.27)
    measured=nonhomothetic_weak_metric_source_polynomials(c=1.0,**args)
    expected=homothetic_weak_metric_source_polynomials(
        beta1=args['beta1'],beta2=args['beta2'],beta3=args['beta3'],K=args['xi'],mu=args['mu'])
    assert np.allclose(measured,expected,rtol=3e-14,atol=3e-14)

import numpy as np


def test_leading_map_reduces_to_aoki_homothetic():
    from numerics.nonhomothetic_pi_map import leading_nonhomothetic_pi_map_coefficients
    mu=-0.6692344189069116
    out=leading_nonhomothetic_pi_map_coefficients(
        a=1.3,conformal_H=0.07,c=1.0,mu=mu,mu_prime=0.0,r=0.8,
    )
    q=1.0+mu
    assert np.isclose(out.A,-1.0/1.3**2)
    assert np.isclose(out.C,1.0/(1.3**2*q))
    assert np.isclose(out.B,(0.8*0.07*mu/q)/1.3**2)
    assert np.isclose(out.D,out.B)


def test_leading_map_contains_lapse_and_mu_prime():
    from numerics.nonhomothetic_pi_map import leading_nonhomothetic_pi_map_coefficients
    a,H,c,mu,mup,r=0.9,0.12,0.27,-0.76,0.018,0.4
    out=leading_nonhomothetic_pi_map_coefficients(
        a=a,conformal_H=H,c=c,mu=mu,mu_prime=mup,r=r,
    )
    q=1.0+mu
    theta=(c*r/q)*(H*mu+mup/(c+q))/a**2
    assert np.isclose(out.A,-1.0/a**2)
    assert np.isclose(out.C,c/(q*a**2))
    assert np.isclose(out.B,theta)
    assert np.isclose(out.D,theta)

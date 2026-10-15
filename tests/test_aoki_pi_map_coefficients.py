import math


def test_homothetic_pi_map_coefficients_match_direct_formulas():
    from numerics.aoki_stueckelberg_adjoint import homothetic_pi_map_coefficients
    a=1.4; Hc=0.23; Hcp=-0.041; r=0.7; mu=-0.35
    c=homothetic_pi_map_coefficients(
        a=a,conformal_H=Hc,conformal_H_prime=Hcp,r=r,mu=mu,
    )
    assert math.isclose(c.A,-1/a**2,rel_tol=0,abs_tol=1e-15)
    assert math.isclose(c.C,1/(a*a*(1+mu)),rel_tol=0,abs_tol=1e-15)
    assert math.isclose(c.B,c.D,rel_tol=0,abs_tol=1e-15)
    assert math.isclose(c.B_r,Hc*mu/((1+mu)*a*a),rel_tol=0,abs_tol=1e-15)
    assert c.C_r==0.0
    assert math.isclose(c.A_t,2*Hc/a**2,rel_tol=0,abs_tol=1e-15)
    target_Dt=r*mu/(1+mu)/a**2*(Hcp-2*Hc**2)
    assert math.isclose(c.D_t,target_Dt,rel_tol=0,abs_tol=1e-15)

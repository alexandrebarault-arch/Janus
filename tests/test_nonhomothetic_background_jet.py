import math


def test_f_native_scale_jet_reduces_to_homothetic_limit():
    from numerics.nonhomothetic_background_jet import f_native_scale_jet
    K=1.7
    out=f_native_scale_jet(a=0.8,ap=0.12,app=-0.03,
                           xi=K,xi_p=0.0,xi_pp=0.0,
                           c=1.0,c_p=0.0)
    assert math.isclose(out.b, K*0.8, rel_tol=0, abs_tol=1e-14)
    assert math.isclose(out.b_f_p, K*0.12, rel_tol=0, abs_tol=1e-14)
    assert math.isclose(out.b_f_pp, K*(-0.03), rel_tol=0, abs_tol=1e-14)


def test_f_native_scale_jet_obeys_chain_rule_for_varying_c():
    from numerics.nonhomothetic_background_jet import f_native_scale_jet
    a,ap,app=1.1,0.2,-0.04
    xi,xi_p,xi_pp=0.7,0.03,-0.005
    c,c_p=0.8,0.02
    out=f_native_scale_jet(a=a,ap=ap,app=app,xi=xi,xi_p=xi_p,xi_pp=xi_pp,c=c,c_p=c_p)
    b_p=ap*xi+a*xi_p
    b_pp=app*xi+2*ap*xi_p+a*xi_pp
    assert math.isclose(out.b_f_p,b_p/c,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.b_f_pp,b_pp/c**2-b_p*c_p/c**3,rel_tol=0,abs_tol=1e-14)


def test_log_derivative_adapter_builds_common_and_f_native_jets():
    from numerics.nonhomothetic_background_jet import from_log_derivatives, f_native_scale_jet
    out=from_log_derivatives(a=0.4,Hc=0.9,Hc_N=-0.2,
        xi=1.3,xi_N=-0.07,xi_NN=0.015,c=0.8,c_N=0.03)
    ap=0.4*0.9
    Hp=0.9*(-0.2)
    app=0.4*(0.9**2+Hp)
    xip=0.9*(-0.07)
    xipp=Hp*(-0.07)+0.9**2*0.015
    cp=0.9*0.03
    assert math.isclose(out.a_p,ap,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.a_pp,app,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.xi_p,xip,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.xi_pp,xipp,rel_tol=0,abs_tol=1e-14)
    expected=f_native_scale_jet(a=0.4,ap=ap,app=app,xi=1.3,xi_p=xip,xi_pp=xipp,c=0.8,c_p=cp)
    assert out.f_native == expected

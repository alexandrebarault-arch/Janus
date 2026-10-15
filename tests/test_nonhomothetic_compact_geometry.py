import math
import numpy as np


def _jet():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    return from_log_derivatives(a=0.8,Hc=0.12,Hc_N=-0.02,
        xi=1.4,xi_N=0.03,xi_NN=-0.004,c=0.75,c_N=0.01)


def test_mu_zero_background_map_is_exact_nonhomothetic_flrw_at_center():
    from numerics.nonhomothetic_compact_geometry import background_map
    j=_jet()
    out=background_map(t=0.0,r=0.7,jet=j,mu=0.0,mu_p=0.0,mu_pp=0.0)
    assert np.allclose(out.g_common, np.diag([-j.a*j.a,j.a*j.a]), atol=1e-14, rtol=0)
    target_f=np.diag([-(j.a*j.xi*j.c)**2,(j.a*j.xi)**2])
    assert np.allclose(out.f_common,target_f,atol=1e-14,rtol=0)
    assert math.isclose(out.f_angular/out.g_angular,j.xi*j.xi,rel_tol=0,abs_tol=1e-14)


def test_homothetic_constant_mu_reproduces_aoki_background_map():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    from numerics.nonhomothetic_compact_geometry import background_map
    K=1.3; Hc=0.08; mu=-0.4; r=0.6
    j=from_log_derivatives(a=1.0,Hc=Hc,Hc_N=-0.5*Hc,
        xi=K,xi_N=0.0,xi_NN=0.0,c=1.0,c_N=0.0)
    out=background_map(t=0.0,r=r,jet=j,mu=mu,mu_p=0.0,mu_pp=0.0)
    M=mu*(2+mu)
    assert math.isclose(out.eta_f,-0.5*Hc*M*r*r,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.Jf[0,1],-Hc*M*r,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.Jf[1,1],1+mu,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.Jf[1,0],0.0,rel_tol=0,abs_tol=1e-14)


def test_dynamic_mu_uses_generalized_nonhomothetic_temporal_relation():
    from numerics.nonhomothetic_compact_geometry import background_map
    j=_jet(); mu=-0.55; mup=0.017; mupp=-0.002; r=0.4
    out=background_map(t=0.0,r=r,jet=j,mu=mu,mu_p=mup,mu_pp=mupp)
    q=mup+j.Hc*mu*(j.c+1+mu)
    assert math.isclose(out.eta_f,-0.5*q*r*r,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.Jf[0,1],-q*r,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(out.Jf[1,0],mup*r,rel_tol=0,abs_tol=1e-14)

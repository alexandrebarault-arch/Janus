import numpy as np


def test_relative_native_geometry_evolves_common_time_background_and_map():
    from numerics.nonhomothetic_hr_relative_native import relative_native_geometry
    out = relative_native_geometry(
        a=2.0,n=1.4,alpha=1.8,r=0.7,
        a_dot_over_a=0.3,a_ddot_over_a=0.11,
        n_dot_over_n=-0.2,n_ddot_over_n=0.06,
        alpha_dot_over_alpha=0.1,alpha_ddot_over_alpha=-0.03,
        common_time_offset=0.25,
        mu=-0.4,mu_dot=0.05,s=-0.2,s_dot=0.04,
        T=0.03,T_dot=-0.02,T_r=0.01,
        L_r=0.02,L_dot_r=-0.015,L_rr=0.025,
    )
    t=0.25
    ac=2.0*(1+0.3*t+0.5*0.11*t*t)
    muc=-0.4+0.05*t
    sc=-0.2+0.04*t
    tf=t+0.5*sc*0.7**2-0.03
    nf=1.4*(1-0.2*tf+0.5*0.06*tf*tf)
    af=1.8*(1+0.1*tf+0.5*(-0.03)*tf*tf)
    rf=(1+muc)*0.7-0.02
    assert np.isclose(out.g_radial_native[1,1],ac*ac,rtol=0,atol=1e-14)
    assert np.isclose(out.g_angular_native,ac*ac*0.7**2,rtol=0,atol=1e-14)
    assert np.isclose(out.n_f,nf,rtol=0,atol=1e-14)
    assert np.isclose(out.alpha_f,af,rtol=0,atol=1e-14)
    assert np.isclose(out.f_radius,rf,rtol=0,atol=1e-14)
    assert np.isclose(out.jacobian_f[0,0],1+0.5*0.04*0.7**2-(-0.02),rtol=0,atol=1e-14)
    assert np.isclose(out.jacobian_f[1,1],1+muc-0.025,rtol=0,atol=1e-14)


def test_zero_time_offset_keeps_legacy_geometry_when_new_a_rates_are_zero():
    from numerics.nonhomothetic_hr_relative_native import relative_native_geometry
    common=dict(a=1.2,n=0.8,alpha=0.9,r=0.6,
        n_dot_over_n=-0.1,n_ddot_over_n=0.02,
        alpha_dot_over_alpha=0.07,alpha_ddot_over_alpha=-0.01,
        mu=-0.25,mu_dot=0.03,s=-0.04,s_dot=0.005,
        T=0.02,T_dot=0.01,T_r=-0.02,L_r=0.01,L_dot_r=0.004,L_rr=-0.006,
        Phi_g=0.003,B_g_r=-0.002,Phi_f=0.004,B_f_r=0.001)
    old=relative_native_geometry(**common)
    new=relative_native_geometry(common_time_offset=0.0,a_dot_over_a=0.0,a_ddot_over_a=0.0,**common)
    assert np.allclose(old.g_radial_native,new.g_radial_native,rtol=0,atol=0)
    assert np.allclose(old.f_radial_native,new.f_radial_native,rtol=0,atol=0)
    assert np.allclose(old.jacobian_f,new.jacobian_f,rtol=0,atol=0)
    assert old.f_time==new.f_time and old.f_radius==new.f_radius

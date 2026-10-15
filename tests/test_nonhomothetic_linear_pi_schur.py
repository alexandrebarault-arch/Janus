import numpy as np


def test_f_eh_block_uses_native_conformal_time_support():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    from numerics.nonhomothetic_linear_pi_schur import reduce_nonhomothetic_linear_pi_metric_block
    from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives_taylor
    jet=from_log_derivatives(a=.03,Hc=3.2,Hc_N=-1.5,xi=1.9,xi_N=-1.4,xi_NN=1.2,c=.25,c_N=.08)
    T=.002; R=.006; kappa=.012; h=3e-5
    out=reduce_nonhomothetic_linear_pi_metric_block(
        betas=(0,1,-4,12,-30),jet=jet,time_radius=T,radial_radius=R,
        interaction_mass2=0.0,planck_ratio=kappa,amplitude_step=h,quadrature_order=12)
    f=jet.f_native
    expected=compact_eh_amplitude_derivatives_taylor(
        a0=f.b,ap0=f.b_f_p,app0=f.b_f_pp,time_radius=jet.c*T,radial_radius=R,
        amplitude_step=h,quadrature_order=12).hessian
    assert np.allclose(out.total_hessian[3:5,3:5],.5*kappa*expected,rtol=2e-12,atol=1e-30)
    assert abs(out.reduced_pi_hessian) < 1e-30

import numpy as np


def test_mu_zero_nonhomothetic_pi_map_cancels_static_spurious_derivative_direction():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    from numerics.nonhomothetic_linear_pi_action import compact_hr_linear_pi_five_field_hessian
    jet=from_log_derivatives(a=.03,Hc=0.0,Hc_N=0.0,
        xi=1.9795452448545166,xi_N=0.0,xi_NN=0.0,
        c=.23330184856024516,c_N=0.0)
    out=compact_hr_linear_pi_five_field_hessian(
        betas=(0,1,-4.2383993109,13.6801214252,-38.5117901844),jet=jet,
        time_radius=.002,radial_radius=.006,amplitude_step=3e-5,quadrature_order=14)
    from numerics.nonhomothetic_compact_sixfield_action import compact_hr_six_field_hessian_nonhomothetic
    raw=compact_hr_six_field_hessian_nonhomothetic(
        betas=(0,1,-4.2383993109,13.6801214252,-38.5117901844),jet=jet,mu=0.0,
        time_radius=.002,radial_radius=.006,amplitude_step=3e-5,quadrature_order=14)
    scale=max(np.linalg.norm(raw.hessian[:2,:2]),1e-30)
    assert abs(out.hessian[0,0])/scale < 1e-8

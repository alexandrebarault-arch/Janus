import numpy as np


def test_nonhomothetic_sixfield_hr_reduces_to_homothetic_oracle_on_small_support():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    from numerics.nonhomothetic_compact_sixfield_action import compact_hr_six_field_hessian_nonhomothetic
    from numerics.aoki_compact_sixfield_action import compact_hr_six_field_hessian
    H=0.05; w=0.0; p=2.0; K=1.25; mu=-0.43
    jet=from_log_derivatives(a=1.0,Hc=H,Hc_N=-H/p,
        xi=K,xi_N=0.0,xi_NN=0.0,c=1.0,c_N=0.0)
    kw=dict(betas=(0.0,1.0,-0.7,0.35,0.0),mu=mu,time_radius=0.025,
            radial_radius=0.35,amplitude_step=8e-4,quadrature_order=14)
    new=compact_hr_six_field_hessian_nonhomothetic(jet=jet,mu_p=0.0,mu_pp=0.0,**kw)
    old=compact_hr_six_field_hessian(K=K,w=w,conformal_H=H,**kw)
    scale=max(1.0,np.linalg.norm(old.hessian))
    assert np.linalg.norm(new.hessian-old.hessian)/scale < 2e-3
    gscale=max(1.0,np.linalg.norm(old.gradient))
    assert np.linalg.norm(new.gradient-old.gradient)/gscale < 2e-3

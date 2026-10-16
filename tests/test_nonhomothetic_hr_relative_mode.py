import numpy as np


def test_mode_correction_hessian_is_zero_at_mu_zero_and_for_zero_interaction():
    from numerics.nonhomothetic_hr_relative_mode import relative_hr_mode_correction_hessian
    common=dict(
        a=1.2,n=.85,alpha=.9,r=.7,k=2.1,
        n_dot_over_n=-.08,n_ddot_over_n=.03,
        alpha_dot_over_alpha=.17,alpha_ddot_over_alpha=.04,
        mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,
        betas=(0.0,1.0,-.7,.3,.1),m2=1.7,Mg2=.9,
        amplitude_step=4e-4,phase_samples=48,
    )
    H=relative_hr_mode_correction_hessian(**common)
    assert np.linalg.norm(H,ord=np.inf) < 1e-12
    finite=dict(common,mu=-.23,betas=(0,0,0,0,0))
    H0=relative_hr_mode_correction_hessian(**finite)
    assert np.linalg.norm(H0,ord=np.inf) < 1e-12


def test_static_mode_correction_is_symmetric_and_phase_average_converged():
    from numerics.nonhomothetic_hr_relative_mode import relative_hr_mode_correction_hessian
    common=dict(
        a=1.2,n=.85,alpha=.9,r=.8,k=2.1,
        mu=-.23,mu_dot=0.0,s=0.0,s_dot=0.0,
        betas=(0.0,1.0,-.7,.3,.1),m2=1.0,Mg2=1.0,
        amplitude_step=4e-4,
    )
    H1=relative_hr_mode_correction_hessian(phase_samples=48,**common)
    H2=relative_hr_mode_correction_hessian(phase_samples=96,**common)
    assert np.allclose(H2,H2.T,rtol=0,atol=1e-12)
    scale=max(1.0,np.linalg.norm(H2,ord=np.inf))
    assert np.linalg.norm(H1-H2,ord=np.inf)/scale < 2e-8


def test_correction_embedding_touches_only_hr_stueckelberg_and_metric_slots():
    from numerics.nonhomothetic_hr_relative_mode import embed_relative_hr_correction_hessian
    H8=np.arange(64,dtype=float).reshape(8,8)
    H8=.5*(H8+H8.T)
    H16=embed_relative_hr_correction_hessian(H8)
    idx=[2,3,8,9,12,13,14,15]
    assert np.allclose(H16[np.ix_(idx,idx)],H8)
    untouched=[0,1,4,5,6,7,10,11]
    assert np.linalg.norm(H16[untouched,:]) == 0.0
    assert np.linalg.norm(H16[:,untouched]) == 0.0

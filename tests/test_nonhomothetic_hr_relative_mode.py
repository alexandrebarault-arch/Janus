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
        amplitude_step=8e-4,
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


def test_high_k_hessian_uses_geometry_scaled_steps_and_is_step_converged():
    import math
    from numerics.candidate_c_native_hr_jets import candidate_c_native_hr_jets
    from numerics.candidate_c_adiabatic_stueckelberg_jets import candidate_c_adiabatic_stueckelberg_jets
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point,candidate_c_dust_params
    from numerics.nonhomothetic_hr_relative_mode import relative_hr_mode_correction_hessian
    a=.025; kh=.1
    point=candidate_c_dust_background_point(a,k_hmpc=kh)
    jets=candidate_c_native_hr_jets(a,k_hmpc=kh)
    st=candidate_c_adiabatic_stueckelberg_jets(a,k_hmpc=kh)
    p=candidate_c_dust_params(); k=math.sqrt(point.metric.k2); r=2.0/k
    common=dict(
        a=a,n=jets.n,alpha=jets.alpha,r=r,k=k,
        n_dot_over_n=jets.n_dot_over_n,n_ddot_over_n=jets.n_ddot_over_n,
        alpha_dot_over_alpha=jets.alpha_dot_over_alpha,alpha_ddot_over_alpha=jets.alpha_ddot_over_alpha,
        mu=st.mu,mu_dot=st.mu_dot,s=st.s,s_dot=st.s_dot,
        betas=(0,p.beta1,p.beta2,p.beta3,p.beta4),m2=p.m2_over_H02,Mg2=1.0,
        phase_samples=64,
    )
    H1=relative_hr_mode_correction_hessian(amplitude_step=8e-4,**common)
    H2=relative_hr_mode_correction_hessian(amplitude_step=4e-4,**common)
    assert np.all(np.isfinite(H1)) and np.all(np.isfinite(H2))
    scale=max(1.0,np.linalg.norm(H2,ord=np.inf))
    assert np.linalg.norm(H1-H2,ord=np.inf)/scale < 3e-3

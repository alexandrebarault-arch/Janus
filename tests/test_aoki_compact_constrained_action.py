import numpy as np


def _root(raw,K):
    b1,b2,b3=raw
    D=b1*K+2*b2*K*K+b3*K**3
    B2=(b2*K*K+b3*K**3)/D; B3=b3*K**3/D
    roots=np.roots([-2*B2+B3,-2*B2-2,-3])
    return sorted(float(z.real) for z in roots if abs(z.imag)<1e-10 and z.real>-1)[0]


def _target(raw,K,mu):
    b1,b2,b3=raw
    D=b1*K+2*b2*K*K+b3*K**3
    B2=(b2*K*K+b3*K**3)/D; B3=b3*K**3/D
    KS=-0.75*(2.0+mu)*(1.0+2.0*B2*mu+B3*mu*mu)
    cs2=2.0*(3.0+(1.0+B2)*mu)/(-3.0*(2.0+mu)*(1.0+2.0*B2*mu+B3*mu*mu))
    return -2.0*D*KS,cs2


def test_weak_interaction_schur_limit_recovers_hr_compact_oracle():
    from numerics.aoki_compact_action_oracle import recover_homothetic_pi_coefficients
    from numerics.aoki_compact_constrained_action import recover_constrained_pi_coefficients
    raw=(1.0,-4.2383993109,13.6801214252); K=1.0; mu=_root(raw,K)
    target=recover_homothetic_pi_coefficients(
        beta1=raw[0],beta2=raw[1],beta3=raw[2],K=K,w=0.0,mu=mu,
        time_scales=(0.5,1.0,2.0),radius=1.0,hubble_step=0.007,amplitude_step=0.002,quadrature_order=28,
    )
    out=recover_constrained_pi_coefficients(
        beta1=raw[0],beta2=raw[1],beta3=raw[2],K=K,w=0.0,mu=mu,
        interaction_strength=1e-3,planck_ratio=1.0,
        time_scales=(0.5,1.0,2.0),radius=1.0,hubble_step=0.007,
        amplitude_step=8e-4,quadrature_order=22,
    )
    assert np.isfinite(out.max_metric_condition)
    assert np.isclose(out.kinetic_hessian_coefficient,target.kinetic_hessian_coefficient,rtol=1.5e-2,atol=2e-4)
    assert np.isclose(out.sound_speed_squared,target.sound_speed_squared,rtol=2e-2,atol=2e-3)


def test_schur_correction_decreases_with_interaction_strength():
    from numerics.aoki_compact_action_oracle import recover_homothetic_pi_coefficients
    from numerics.aoki_compact_constrained_action import recover_constrained_pi_coefficients
    raw=(1.0,-2.0,6.0); K=1.0; mu=_root(raw,K)
    target=recover_homothetic_pi_coefficients(beta1=raw[0],beta2=raw[1],beta3=raw[2],K=K,w=0.0,mu=mu,quadrature_order=24)
    errs=[]
    for lam in (4e-3,2e-3,1e-3):
        out=recover_constrained_pi_coefficients(
            beta1=raw[0],beta2=raw[1],beta3=raw[2],K=K,w=0.0,mu=mu,
            interaction_strength=lam,planck_ratio=1.0,quadrature_order=20,amplitude_step=8e-4,
        )
        errs.append(abs(out.kinetic_hessian_coefficient-target.kinetic_hessian_coefficient))
    assert errs[2] < errs[1] < errs[0]


def test_weak_schur_limit_tracks_aoki_on_both_kinetic_signs():
    from numerics.aoki_compact_constrained_action import recover_constrained_pi_coefficients
    controls=(
        ((1.0,-4.2383993109,13.6801214252),1.0),
        ((1.0,-4.2383993109,13.6801214252),0.7),
        ((1.0,-2.0,6.0),1.0),
    )
    signs=set()
    for raw,K in controls:
        mu=_root(raw,K)
        kinetic_target,cs2_target=_target(raw,K,mu)
        out=recover_constrained_pi_coefficients(
            beta1=raw[0],beta2=raw[1],beta3=raw[2],K=K,w=0.0,mu=mu,
            interaction_strength=1e-4,planck_ratio=1.0,
            time_scales=(0.5,1.0,2.0),radius=1.0,hubble_step=0.007,
            amplitude_step=1e-3,quadrature_order=18,
        )
        assert np.isclose(out.kinetic_hessian_coefficient,kinetic_target,rtol=2e-3,atol=2e-4)
        assert np.isclose(out.sound_speed_squared,cs2_target,rtol=3e-3,atol=2e-3)
        signs.add(np.sign(kinetic_target))
    assert signs == {-1.0,1.0}

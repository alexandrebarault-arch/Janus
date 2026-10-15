import numpy as np


def test_generic_compact_pullback_matches_existing_homothetic_action_pointwise():
    from numerics.aoki_compact_action_oracle import _action
    from numerics.nonhomothetic_compact_oscillation_action import homothetic_pi_compact_action
    kwargs=dict(
        amp=0.0013,hubble=0.017,
        beta1=1.0,beta2=-4.2383993109,beta3=13.6801214252,
        K=0.83,w=0.0,mu=-0.62,T=0.7,R=0.9,order=24,
    )
    assert np.isclose(homothetic_pi_compact_action(**kwargs),_action(**kwargs),rtol=2e-12,atol=2e-12)


def test_generic_compact_pullback_matches_for_zero_and_negative_amplitude():
    from numerics.aoki_compact_action_oracle import _action
    from numerics.nonhomothetic_compact_oscillation_action import homothetic_pi_compact_action
    base=dict(hubble=-0.011,beta1=1.0,beta2=-2.0,beta3=6.0,K=1.0,w=0.0,mu=-0.55,T=1.2,R=0.8,order=22)
    for amp in (0.0,-0.0017):
        assert np.isclose(homothetic_pi_compact_action(amp=amp,**base),_action(amp=amp,**base),rtol=2e-12,atol=2e-12)


def test_frozen_homothetic_null_direction_recovers_aoki_leading_map():
    from numerics.nonhomothetic_compact_oscillation_action import frozen_displacement_null_ratio
    mu=-0.6692344189069116
    ratio,nullness=frozen_displacement_null_ratio(
        beta1=1.0,beta2=-4.2383993109,beta3=13.6801214252,
        xi=1.0,c=1.0,mu=mu,T=1.0,R=1.0,order=36,amplitude_step=2e-4,
    )
    assert np.isclose(ratio,-1.0/(1.0+mu),rtol=2e-5,atol=2e-6)
    assert nullness < 5e-5


def test_frozen_nonhomothetic_null_direction_contains_relative_lapse():
    from numerics.nonhomothetic_compact_oscillation_action import frozen_displacement_null_ratio
    for xi,c,mu in ((1.5,0.7,-0.77),(2.0,0.25,-0.77),(0.7,1.3,-0.61)):
        ratio,nullness=frozen_displacement_null_ratio(
            beta1=1.0,beta2=-4.2383993109,beta3=13.6801214252,
            xi=xi,c=c,mu=mu,T=1.0,R=1.0,order=36,amplitude_step=2e-4,
        )
        assert np.isclose(ratio,-c/(1.0+mu),rtol=1.5e-4,atol=2e-5)
        assert nullness < 5e-4

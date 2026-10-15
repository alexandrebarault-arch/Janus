import numpy as np


def _aoki_target(raw, K, mu, w=0.0):
    b1, b2, b3 = raw
    D = b1*K + 2.0*b2*K*K + b3*K**3
    B2 = (b2*K*K + b3*K**3)/D
    B3 = b3*K**3/D
    KS = 0.75*(3.0*w - 1.0)*(2.0 + mu)*(1.0 + 2.0*B2*mu + B3*mu*mu)
    cs2 = (
        2.0*(3.0*(1.0-w) + (1.0-(3.0*w-1.0)*B2)*mu)
        /(3.0*(3.0*w-1.0)*(2.0+mu)*(1.0+2.0*B2*mu+B3*mu*mu))
    )
    return -2.0*D*KS, cs2


def _regular_roots(raw, K, w=0.0):
    b1, b2, b3 = raw
    D = b1*K + 2.0*b2*K*K + b3*K**3
    B2 = (b2*K*K + b3*K**3)/D
    B3 = b3*K**3/D
    roots = np.roots([
        -2.0*B2 + (1.0+3.0*w)*B3,
        6.0*w*B2 - 2.0*B2 - 2.0,
        3.0*(w-1.0),
    ])
    return sorted(float(z.real) for z in roots if abs(z.imag) < 1e-10 and z.real > -1.0)


def test_compact_support_hr_action_recovers_aoki_kinetic_and_gradient_coefficients():
    from numerics.aoki_compact_action_oracle import recover_homothetic_pi_coefficients

    controls = [
        ((1.0, -4.2383993109, 13.6801214252), 1.0),
        ((1.0, -4.2383993109, 13.6801214252), 0.7),
        ((1.0, -2.0, 6.0), 1.0),
    ]
    signs = set()
    for raw, K in controls:
        mu = _regular_roots(raw, K)[0]
        kinetic_target, cs2_target = _aoki_target(raw, K, mu)
        result = recover_homothetic_pi_coefficients(
            beta1=raw[0], beta2=raw[1], beta3=raw[2],
            K=K, w=0.0, mu=mu,
            time_scales=(0.5, 1.0, 2.0), radius=1.0,
            hubble_step=0.007, amplitude_step=0.002,
            quadrature_order=36,
        )
        assert np.isclose(result.kinetic_hessian_coefficient, kinetic_target, rtol=1.5e-3, atol=2e-5)
        assert np.isclose(result.sound_speed_squared, cs2_target, rtol=1.5e-3, atol=2e-5)
        assert abs(result.zero_hubble_hessian) < 2e-8
        signs.add(np.sign(kinetic_target))
    assert signs == {-1.0, 1.0}

import math
import numpy as np


def _root(raw, K):
    b1, b2, b3 = raw
    D = b1*K + 2.0*b2*K*K + b3*K**3
    B2 = (b2*K*K + b3*K**3)/D
    B3 = b3*K**3/D
    roots = np.roots([-2.0*B2 + B3, -2.0*B2 - 2.0, -3.0])
    vals = sorted(float(z.real) for z in roots if abs(z.imag) < 1.0e-10 and z.real > -1.0)
    return vals[0]


def test_homothetic_uniform_kinetic_signature_matches_aoki_dust_controls():
    from numerics.nonhomothetic_oscillation_kinetic import (
        aoki_homothetic_kinetic_coefficient,
        homothetic_uniform_velocity_hessian,
    )
    controls = [
        ((1.0, -4.2383993109, 13.6801214252), 1.0),
        ((1.0, -4.2383993109, 13.6801214252), 0.7),
        ((1.0, -3.0, 10.0), 0.5),
        ((1.0, -2.0, 6.0), 1.0),
    ]
    signs = []
    for raw, K in controls:
        mu = _root(raw, K)
        ks, D = aoki_homothetic_kinetic_coefficient(
            beta1=raw[0], beta2=raw[1], beta3=raw[2],
            K=K, w=0.0, mu=mu,
        )
        assert D > 0.0
        H = homothetic_uniform_velocity_hessian(
            beta1=raw[0], beta2=raw[1], beta3=raw[2],
            K=K, w=0.0, mu=mu, radius=0.02,
        )
        eig = np.linalg.eigvalsh(H)
        physical = eig[np.argmax(np.abs(eig))]
        null = eig[np.argmin(np.abs(eig))]
        assert abs(null) < 5.0e-4*abs(physical)
        assert math.copysign(1.0, physical) == math.copysign(1.0, ks)
        signs.append(math.copysign(1.0, ks))
    assert set(signs) == {-1.0, 1.0}


def test_uniform_kinetic_sign_is_stable_under_radius_and_step_changes():
    from numerics.nonhomothetic_oscillation_kinetic import homothetic_uniform_velocity_hessian
    raw = (1.0, -4.2383993109, 13.6801214252)
    K = 1.0
    mu = _root(raw, K)
    vals = []
    for radius in (0.012, 0.02, 0.03):
        for step in (5.0e-4, 1.0e-3, 2.0e-3):
            H = homothetic_uniform_velocity_hessian(
                beta1=raw[0], beta2=raw[1], beta3=raw[2],
                K=K, w=0.0, mu=mu, radius=radius, step=step,
            )
            eig = np.linalg.eigvalsh(H)
            physical = eig[np.argmax(np.abs(eig))]
            assert physical > 0.0
            vals.append(physical/radius**5)
    assert max(vals)/min(vals) < 1.01


def test_general_velocity_hessian_reduces_to_homothetic_wrapper():
    from numerics.nonhomothetic_oscillation_kinetic import (
        uniform_velocity_hessian,
        homothetic_uniform_velocity_hessian,
    )
    raw = (1.0, -4.2383993109, 13.6801214252)
    K = 1.0
    w = 0.0
    mu = _root(raw, K)
    e = -1.5*(1.0 + w)
    M = mu*(2.0 + mu)
    generic = uniform_velocity_hessian(
        betas=(0.0, *raw, 0.0),
        a=1.0, b=K, c=1.0, mu=mu, mu_dot=0.0,
        sigma_prime_coefficient=-M,
        sigma_dot_coefficient=-(1.0 + e)*M,
        radius=0.02, step=1.0e-3,
    )
    wrapped = homothetic_uniform_velocity_hessian(
        beta1=raw[0], beta2=raw[1], beta3=raw[2],
        K=K, w=w, mu=mu, radius=0.02, step=1.0e-3,
    )
    assert np.allclose(generic, wrapped, rtol=0.0, atol=1.0e-18)

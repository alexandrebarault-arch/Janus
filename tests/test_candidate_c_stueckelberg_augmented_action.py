import math
import numpy as np


def _candidate_augmented_hessian(a, k_hmpc):
    from numerics.candidate_c_dust_background import (
        candidate_c_dust_background_point,
        candidate_c_dust_params,
    )
    from numerics.de_felice_two_dust_action import flat_gauge_two_dust_hessian
    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    betas = (0.0, p.beta1, p.beta2, p.beta3, p.beta4)
    H14 = flat_gauge_two_dust_hessian(
        point.metric, point.derivatives, betas=betas,
        rho_g=point.rho_g_m, rho_f=point.rho_f_m,
    )
    return H14, point


def _metric_schur(H16):
    metric = list(range(12, 16))
    keep = list(range(12))
    Hmm = H16[np.ix_(metric, metric)]
    Hmk = H16[np.ix_(metric, keep)]
    Hkk = H16[np.ix_(keep, keep)]
    assert np.linalg.matrix_rank(Hmm) == 4
    reduced = Hkk - Hmk.T @ np.linalg.solve(Hmm, Hmk)
    return 0.5*(reduced + reduced.T), float(np.linalg.cond(Hmm))


def _augmented_stueckelberg_reduced_hessian(a, k_hmpc):
    from numerics.prebd_stueckelberg_transform import direct_flat_augmented_transform
    H14, point = _candidate_augmented_hessian(a, k_hmpc)
    nHf = point.metric.H_omega / point.metric.a
    nHf_dot = (
        point.derivatives.H_omega_prime - point.metric.H_omega*point.metric.H
    ) / point.metric.a**2
    P = direct_flat_augmented_transform(
        k=math.sqrt(point.metric.k2), nHf=nHf, nHf_dot=nHf_dot,
    )
    H16 = P.T @ H14 @ P
    return _metric_schur(0.5*(H16 + H16.T))


def _native_augmented_stueckelberg_reduced_hessian(a, k_hmpc):
    from numerics.prebd_stueckelberg_transform import direct_native_augmented_transform
    H14, point = _candidate_augmented_hessian(a, k_hmpc)
    bg = point.metric
    bgp = point.derivatives
    n = bg.xi*bg.c
    alpha = bg.a*bg.xi
    nHf = bg.H_omega/bg.a
    nHf_dot = (bgp.H_omega_prime - bg.H_omega*bg.H)/bg.a**2
    n_dot_over_n = (bgp.xi_prime/bg.xi + bgp.c_prime/bg.c)/bg.a
    P = direct_native_augmented_transform(
        k=math.sqrt(bg.k2), nHf=nHf, nHf_dot=nHf_dot,
        n_dot_over_n=n_dot_over_n,
        n_over_alpha=n/alpha, alpha_over_n=alpha/n,
    )
    H16 = P.T @ H14 @ P
    return _metric_schur(0.5*(H16 + H16.T))


def _reference_prebd_stueckelberg(a, kh):
    from numerics.de_felice_dust_physical_action import _candidate_transformed
    from numerics.candidate_c_linear_stueckelberg_action import _bridge_rates
    from numerics.prebd_stueckelberg_transform import (
        prebd_bridge_matrices,
        transform_state_rate_hessian,
    )
    reference, point = _candidate_transformed(a, kh)
    nHf, nHf_dot = _bridge_rates(point)
    R, Rdot = prebd_bridge_matrices(
        k=math.sqrt(point.metric.k2), nHf=nHf, nHf_dot=nHf_dot,
    )
    return transform_state_rate_hessian(reference, R, Rdot)


def test_transform_before_metric_schur_matches_validated_prebd_route():
    for a, kh in ((0.3, 0.1), (0.5, 0.2), (0.7, 0.1)):
        direct, cond = _augmented_stueckelberg_reduced_hessian(a, kh)
        reference = _reference_prebd_stueckelberg(a, kh)
        scale = max(1.0, float(np.linalg.norm(reference, ord=np.inf)))
        error = float(np.linalg.norm(direct-reference, ord=np.inf)/scale)
        assert error < 1e-8
        assert math.isfinite(cond) and cond < 3e5


def test_native_auxiliary_stueckelberg_route_has_same_physical_schur_action():
    for a, kh in ((0.3, 0.1), (0.5, 0.2), (0.7, 0.1)):
        native, cond = _native_augmented_stueckelberg_reduced_hessian(a, kh)
        reference = _reference_prebd_stueckelberg(a, kh)
        scale = max(1.0, float(np.linalg.norm(reference, ord=np.inf)))
        error = float(np.linalg.norm(native-reference, ord=np.inf)/scale)
        assert error < 1e-8
        assert math.isfinite(cond) and cond < 3e5

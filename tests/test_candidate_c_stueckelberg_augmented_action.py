import math
import numpy as np


def _augmented_stueckelberg_reduced_hessian(a, k_hmpc):
    from numerics.candidate_c_dust_background import (
        candidate_c_dust_background_point,
        candidate_c_dust_params,
    )
    from numerics.de_felice_two_dust_action import flat_gauge_two_dust_hessian
    from numerics.prebd_stueckelberg_transform import direct_flat_augmented_transform

    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    betas = (0.0, p.beta1, p.beta2, p.beta3, p.beta4)
    H14 = flat_gauge_two_dust_hessian(
        point.metric, point.derivatives, betas=betas,
        rho_g=point.rho_g_m, rho_f=point.rho_f_m,
    )
    nHf = point.metric.H_omega / point.metric.a
    nHf_dot = (
        point.derivatives.H_omega_prime - point.metric.H_omega*point.metric.H
    ) / point.metric.a**2
    P = direct_flat_augmented_transform(
        k=math.sqrt(point.metric.k2), nHf=nHf, nHf_dot=nHf_dot,
    )
    H16 = P.T @ H14 @ P
    H16 = 0.5*(H16 + H16.T)
    metric = list(range(12, 16))
    keep = list(range(12))
    Hmm = H16[np.ix_(metric, metric)]
    Hmk = H16[np.ix_(metric, keep)]
    Hkk = H16[np.ix_(keep, keep)]
    assert np.linalg.matrix_rank(Hmm) == 4
    reduced = Hkk - Hmk.T @ np.linalg.solve(Hmm, Hmk)
    return 0.5*(reduced + reduced.T), float(np.linalg.cond(Hmm))


def test_transform_before_metric_schur_matches_validated_prebd_route():
    from numerics.de_felice_dust_physical_action import _candidate_transformed
    from numerics.candidate_c_linear_stueckelberg_action import _bridge_rates
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.prebd_stueckelberg_transform import (
        prebd_bridge_matrices,
        transform_state_rate_hessian,
    )

    for a, kh in ((0.3, 0.1), (0.5, 0.2), (0.7, 0.1)):
        direct, cond = _augmented_stueckelberg_reduced_hessian(a, kh)
        reference, point = _candidate_transformed(a, kh)
        nHf, nHf_dot = _bridge_rates(point)
        R, Rdot = prebd_bridge_matrices(
            k=math.sqrt(point.metric.k2), nHf=nHf, nHf_dot=nHf_dot,
        )
        reference = transform_state_rate_hessian(reference, R, Rdot)
        scale = max(1.0, float(np.linalg.norm(reference, ord=np.inf)))
        error = float(np.linalg.norm(direct-reference, ord=np.inf)/scale)
        assert error < 1e-8
        assert math.isfinite(cond) and cond < 3e5

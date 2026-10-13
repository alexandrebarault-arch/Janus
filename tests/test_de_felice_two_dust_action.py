import inspect
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_dust_background import (
    candidate_c_dust_background_point,
    candidate_c_dust_params,
)


def _control(a=0.5, k_hmpc=0.1):
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    p = candidate_c_dust_params()
    betas = (0.0, p.beta1, p.beta2, p.beta3, p.beta4)
    return point, betas


def test_two_dust_augmented_action_is_exact_quadratic_and_symmetric():
    import numerics.de_felice_two_dust_action as dust
    point, betas = _control()
    H = dust.flat_gauge_two_dust_hessian(
        point.metric, point.derivatives, betas=betas,
        rho_g=point.rho_g_m, rho_f=point.rho_f_m,
    )
    assert dust.DUST_DYNAMIC_ORDER == ("psi_f", "E_f", "q_g", "q_f")
    assert dust.DUST_RATE_ORDER == ("psi_f_dot", "E_f_dot", "q_g_dot", "q_f_dot")
    assert dust.DUST_AUXILIARY_ORDER == ("Phi_g", "Phi_f", "B_g", "B_f", "p_g", "p_f")
    assert H.shape == (14, 14)
    assert np.all(np.isfinite(H))
    assert np.allclose(H, H.T, rtol=0.0, atol=1e-11)
    assert 'cs2' not in inspect.signature(dust.flat_gauge_two_dust_hessian).parameters
    assert np.allclose(H[np.ix_([6, 7], [12, 13])], np.eye(2), rtol=0.0, atol=1e-13)


def test_two_dust_metric_schur_preserves_canonical_momenta_and_reconstructs_action():
    import numerics.de_felice_two_dust_action as dust
    for a, k_hmpc in ((0.5, 0.1), (0.1, 0.05)):
        point, betas = _control(a, k_hmpc)
        out = dust.eliminate_flat_gauge_two_dust(
            point.metric, point.derivatives, betas=betas,
            rho_g=point.rho_g_m, rho_f=point.rho_f_m,
        )
        assert out.metric_auxiliary_rank == 4
        assert out.reduced_hessian.shape == (10, 10)
        assert out.metric_reconstruction_matrix.shape == (4, 10)
        assert np.all(np.isfinite(out.reduced_hessian))
        assert np.allclose(out.reduced_hessian, out.reduced_hessian.T, rtol=0.0, atol=2e-10)
        assert math.isfinite(out.metric_auxiliary_condition_number)

        # Reduced order is 4 states, 4 rates, p_g, p_f.  Exact pressureless
        # matter remains first-order, so p_g,p_f are canonical variables.
        assert np.allclose(
            out.reduced_hessian[np.ix_([6, 7], [8, 9])],
            np.eye(2), rtol=0.0, atol=1e-12,
        )

        u = np.array([0.13, -0.021, 0.037, -0.044,
                      0.017, -0.008, 0.026, -0.019,
                      0.31, -0.27], dtype=float)
        metric_aux = out.metric_reconstruction_matrix @ u
        full = np.concatenate([u[:8], metric_aux, u[8:]])
        lhs = 0.5 * float(full @ out.augmented_hessian @ full)
        rhs = 0.5 * float(u @ out.reduced_hessian @ u)
        scale = max(1.0, abs(lhs), abs(rhs))
        assert abs(lhs-rhs) <= 1e-10*scale

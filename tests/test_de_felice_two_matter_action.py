import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_case_c import case_c_background_from_a
from numerics.de_felice_two_matter_action import (
    DFKessenceFluid,
    matter_log_phidot_rates,
    flat_gauge_quadratic_hessian,
    eliminate_flat_gauge_auxiliaries,
)


def _case_c(a, k):
    point = case_c_background_from_a(a, k=k)
    g = DFKessenceFluid(rho=point.rho1, pressure=point.rho1/3.0, cs2=1.0/3.0)
    f = DFKessenceFluid(rho=point.rho2, pressure=0.0, cs2=0.1)
    return point, g, f


def test_matter_rate_variables_include_background_phidot_drift():
    point, g, f = _case_c(0.2,20.0)
    rg, rf = matter_log_phidot_rates(point.metric, point.derivatives, g_fluid=g, f_fluid=f)
    bg = point.metric; bgp = point.derivatives
    Hg = bg.H/bg.a
    expected_g = -3.0*Hg*g.cs2
    n_dot_over_n = (bgp.xi_prime/bg.xi + bgp.c_prime/bg.c)/bg.a
    n = bg.xi*bg.c
    Hf = bg.H_omega/(bg.a*bg.xi*bg.c)
    expected_f = n_dot_over_n - 3.0*n*Hf*f.cs2
    assert math.isclose(rg, expected_g, rel_tol=2e-13, abs_tol=2e-13)
    assert math.isclose(rf, expected_f, rel_tol=2e-13, abs_tol=2e-13)


def test_two_matter_flat_gauge_hessian_is_symmetric():
    point, g, f = _case_c(0.1, 12.0)
    Q = flat_gauge_quadratic_hessian(
        point.metric, point.derivatives,
        betas=(0.0,1.0,0.0,0.0,0.0),
        g_fluid=g, f_fluid=f, finite_difference_step=5e-5,
    )
    assert Q.shape == (12,12)
    assert np.all(np.isfinite(Q))
    assert np.allclose(Q,Q.T,rtol=2e-10,atol=2e-10)


def test_two_matter_case_c_has_exactly_three_kinetic_directions_after_auxiliary_elimination():
    for a,k in ((0.1,12.0),(0.2,20.0),(0.4,30.0)):
        point, g, f = _case_c(a,k)
        reduced = eliminate_flat_gauge_auxiliaries(
            point.metric, point.derivatives,
            betas=(0.0,1.0,0.0,0.0,0.0),
            g_fluid=g, f_fluid=f, finite_difference_step=5e-5,
        )
        eig = np.linalg.eigvalsh(reduced.kinetic_hessian)
        scale = max(1.0,float(np.max(np.abs(eig))))
        tol = 2e-7*scale
        assert np.count_nonzero(np.abs(eig)>tol) == 3
        assert np.min(np.abs(eig)) < tol
        assert reduced.auxiliary_rank == 4

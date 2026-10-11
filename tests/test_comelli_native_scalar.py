import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.flrw_two_matter import candidate_c, diagnostics, solve_branch
from numerics.comelli_native_scalar import (
    LocalBarotropicFluid,
    native_metric_matrix_N,
)


def _expected_candidate_c_cs2(a):
    p = candidate_c()
    grid = np.geomspace(1.0, a, 1600)
    y = solve_branch(grid, p)[-1]
    return float(diagnostics(np.array([a]), np.array([y]), p)['scalar_cs2'][0])


def test_native_metric_system_recovers_de_felice_high_k_gravity_speed():
    a = 0.5  # z=1; radiation is only a 6e-4 correction to rho_m here.
    k_hmpc = 0.5
    point = candidate_c_background_point(a, k_hmpc=k_hmpc)

    rho_g = point.rho_g_m + point.rho_g_r
    p_g = point.rho_g_r / 3.0
    w_g = p_g / rho_g
    g_fluid = LocalBarotropicFluid(rho=rho_g, w=w_g)
    f_fluid = LocalBarotropicFluid(rho=point.rho_f_m, w=0.0)

    M = native_metric_matrix_N(point, g_fluid=g_fluid, f_fluid=f_fluid)
    eig = np.linalg.eigvals(M)
    speeds = sorted(
        abs(v.imag) * point.metric.H / math.sqrt(point.metric.k2)
        for v in eig if abs(v.imag) > 1e-5
    )

    expected = math.sqrt(_expected_candidate_c_cs2(a))
    assert speeds, 'native scalar system must contain a propagating gravity pair'
    # The native six-dimensional metric system has one gravity pair and the
    # matter-fluid pair(s) eliminated through the constraints. Match the pair
    # nearest the independent De Felice high-frequency prediction.
    measured = min(speeds, key=lambda s: abs(s-expected))
    assert math.isclose(measured, expected, rel_tol=0.02, abs_tol=0.01)

import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_candidate_dust_density_maps_reconstruct_sector_contrasts_from_raw_phase_momenta():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    from numerics.dust_observables import dust_density_maps, evaluate_dust_observables
    a = 0.5
    k = 0.05
    point = candidate_c_dust_background_point(a, k_hmpc=k)
    action = candidate_c_dust_canonical_action(a, k_hmpc=k, derivative_step_N=2e-4)
    maps = dust_density_maps(action, point.metric, rho_g=point.rho_g_m, rho_f=point.rho_f_m)
    z = np.array([0.027, -0.014, 0.009, 0.31, -0.22, 0.18])
    obs = evaluate_dust_observables(maps, z)
    p = action.matter_momentum_map @ z
    Z = float(action.bd_state_map @ z)
    n = point.metric.xi * point.metric.c
    expected_g = p[0] / point.rho_g_m
    expected_f = (
        p[1] / (n * point.metric.xi**3) - 3.0 * point.rho_f_m * Z
    ) / point.rho_f_m
    assert math.isclose(obs.delta_g, expected_g, rel_tol=2e-12, abs_tol=2e-12)
    assert math.isclose(obs.delta_f, expected_f, rel_tol=2e-12, abs_tol=2e-12)
    assert math.isclose(obs.delta_relative, expected_g-expected_f,
                        rel_tol=2e-12, abs_tol=2e-12)


def test_density_pullback_uses_recovered_matter_momentum_not_naive_final_Pi():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    from numerics.dust_observables import dust_density_maps
    point = candidate_c_dust_background_point(0.5, k_hmpc=0.1)
    action = candidate_c_dust_canonical_action(0.5, k_hmpc=0.1, derivative_step_N=2e-4)
    maps = dust_density_maps(action, point.metric, rho_g=point.rho_g_m, rho_f=point.rho_f_m)
    assert abs(maps.delta_g_map[5]) > 1e-8 or abs(maps.delta_f_map[5]) > 1e-8
    naive_g = np.array([0.0, 0.0, 0.0, 1.0/point.rho_g_m, 0.0, 0.0])
    assert not np.allclose(maps.delta_g_map, naive_g, rtol=0, atol=1e-10)

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_quasistatic_bound import (
    spin2_static_kernels,
    candidate_c_frozen_kernel,
    find_h_equals_meff_redshift,
    late_linear_rotation_bound,
)


def test_spin2_static_kernel_limits():
    r = 0.2
    far = spin2_static_kernels(r=r, yukawa_fraction=0.0)
    assert far == (1.0, 1.0, 1.0)

    short = spin2_static_kernels(r=r, yukawa_fraction=1.0)
    qgg, qgf, qff = short
    assert math.isclose(qgg, 1.0 + (4.0 / 3.0) * r * r, abs_tol=1e-14)
    assert math.isclose(qgf, -1.0 / 3.0, abs_tol=1e-14)
    assert math.isclose(qff, 1.0 + 4.0 / (3.0 * r * r), abs_tol=1e-12)


def test_candidate_c_present_frozen_kernel_reference_point():
    d = candidate_c_frozen_kernel(a=1.0, k_hmpc=0.1)
    assert math.isclose(d.r, 0.0605863064, rel_tol=0.0, abs_tol=3e-9)
    assert math.isclose(d.yukawa_fraction, 0.9805, rel_tol=2e-4)
    assert math.isclose(d.q_gg, 1.0048, rel_tol=3e-4)
    assert math.isclose(d.q_gf, -0.3073, rel_tol=4e-4)
    assert math.isclose(d.q_ff, 357.14, rel_tol=8e-4)


def test_candidate_c_h_equals_meff_and_late_rotation_bound():
    z_cross = find_h_equals_meff_redshift()
    assert math.isclose(z_cross, 16.24, rel_tol=0.0, abs_tol=0.08)

    b = late_linear_rotation_bound()
    assert 4.0 < b.delta_theta_deg < 4.3
    assert 1.65 < b.max_differential_growth < 1.75
    assert b.final_relative_to_common_upper_reference < 0.13

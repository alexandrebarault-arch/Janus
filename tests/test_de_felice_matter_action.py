import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.de_felice_matter_action import (
    kessence_lapse_quadratic_coefficient,
    kessence_pure_lapse_quadratic_density,
)


def _expected(rho, pressure, cs2):
    return -0.5 * pressure + 0.5 * (1.0 + cs2) / cs2 * (rho + pressure)


def test_de_felice_eq54_pure_lapse_coefficient_for_generic_kessence():
    for rho, pressure, cs2 in (
        (2.7, 0.4, 0.63),
        (1.9, 0.0, 0.2),
        (3.2, 1.1, 1.0),
    ):
        measured = kessence_lapse_quadratic_coefficient(
            rho=rho, pressure=pressure, cs2=cs2
        )
        assert math.isclose(
            measured, _expected(rho, pressure, cs2),
            rel_tol=2e-14, abs_tol=2e-14,
        )


def test_same_matter_formula_applies_to_g_and_f_sectors_before_volume_factors():
    rho_g, p_g, cs2_g = 2.7, 0.4, 0.63
    rho_f, p_f, cs2_f = 5.1, 0.2, 0.31
    Phi_g, Phi_f = 0.07, -0.11

    Lg = kessence_pure_lapse_quadratic_density(
        rho=rho_g, pressure=p_g, cs2=cs2_g, Phi=Phi_g
    )
    Lf = kessence_pure_lapse_quadratic_density(
        rho=rho_f, pressure=p_f, cs2=cs2_f, Phi=Phi_f
    )

    assert math.isclose(Lg, _expected(rho_g, p_g, cs2_g) * Phi_g**2)
    assert math.isclose(Lf, _expected(rho_f, p_f, cs2_f) * Phi_f**2)


def test_canonical_scalar_limit_cs2_one():
    rho, pressure = 4.3, 0.7
    measured = kessence_lapse_quadratic_coefficient(
        rho=rho, pressure=pressure, cs2=1.0
    )
    assert math.isclose(measured, rho + 0.5 * pressure)

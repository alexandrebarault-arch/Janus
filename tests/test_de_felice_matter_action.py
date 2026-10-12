import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.de_felice_matter_action import (
    kessence_lapse_quadratic_coefficient,
    kessence_pure_lapse_quadratic_density,
    kessence_scalar_quadratic_density,
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


def test_full_scalar_density_matches_de_felice_eq54_flat_fourier_mode():
    rho, pressure, cs2 = 4.7, 0.8, 0.37
    lapse, a, k = 1.23, 0.74, 2.1
    Phi, B, psi, E = 0.09, -0.12, 0.07, -0.035
    q, qdot = 0.041, -0.063

    measured = kessence_scalar_quadratic_density(
        rho=rho,
        pressure=pressure,
        cs2=cs2,
        lapse=lapse,
        scale_factor=a,
        k=k,
        Phi=Phi,
        B=B,
        psi=psi,
        E=E,
        delta_phi_over_phidot=q,
        delta_phidot_over_phidot=qdot,
    )

    enthalpy = rho + pressure
    tr_h = 6.0 * psi
    hij_hij = 12.0 * psi**2 + (2.0 / 3.0) * k**4 * E**2
    v2 = k**2 * B**2
    expected = (
        pressure
        * (
            -0.5 * Phi**2
            + 0.5 * v2
            + 0.125 * (tr_h**2 - 2.0 * hij_hij)
            + 0.5 * tr_h * Phi
        )
        + 0.5 * enthalpy * qdot**2
        + 0.5 * (1.0 - cs2) / cs2 * enthalpy * (qdot - Phi) ** 2
        + 0.5 * enthalpy * (Phi - qdot) * (2.0 * Phi - tr_h)
        - 0.5
        * lapse**2
        * enthalpy
        / a**2
        * k**2
        * (q + a * B / lapse) ** 2
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_metric_off_principal_matter_action_has_intrinsic_sound_speed():
    rho, pressure, cs2 = 3.9, 0.6, 1.0 / 3.0
    lapse, a, k = 1.17, 0.81, 3.2

    # With metric perturbations off, Eq. (54) reduces to
    #   h/(2 cs2) qdot^2 - N^2 h k^2/(2 a^2) q^2.
    # Thus omega^2/k^2 = (N^2/a^2) cs2.
    h = rho + pressure
    q = 0.053
    qdot = -0.071
    measured = kessence_scalar_quadratic_density(
        rho=rho,
        pressure=pressure,
        cs2=cs2,
        lapse=lapse,
        scale_factor=a,
        k=k,
        Phi=0.0,
        B=0.0,
        psi=0.0,
        E=0.0,
        delta_phi_over_phidot=q,
        delta_phidot_over_phidot=qdot,
    )
    expected = h / (2.0 * cs2) * qdot**2 - lapse**2 * h * k**2 / (2.0 * a**2) * q**2
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)

    kinetic = h / cs2
    gradient = lapse**2 * h / a**2
    coordinate_speed2 = gradient / kinetic
    assert math.isclose(coordinate_speed2, lapse**2 * cs2 / a**2, rel_tol=2e-14)

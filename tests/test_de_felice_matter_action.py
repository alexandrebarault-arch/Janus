import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numerics.de_felice_matter_action as matter_action


def _expected(rho, pressure, cs2):
    return -0.5 * pressure + 0.5 * (1.0 + cs2) / cs2 * (rho + pressure)


def test_de_felice_eq54_pure_lapse_coefficient_for_generic_kessence():
    for rho, pressure, cs2 in (
        (2.7, 0.4, 0.63),
        (1.9, 0.0, 0.2),
        (3.2, 1.1, 1.0),
    ):
        measured = matter_action.kessence_lapse_quadratic_coefficient(
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

    Lg = matter_action.kessence_pure_lapse_quadratic_density(
        rho=rho_g, pressure=p_g, cs2=cs2_g, Phi=Phi_g
    )
    Lf = matter_action.kessence_pure_lapse_quadratic_density(
        rho=rho_f, pressure=p_f, cs2=cs2_f, Phi=Phi_f
    )

    assert math.isclose(Lg, _expected(rho_g, p_g, cs2_g) * Phi_g**2)
    assert math.isclose(Lf, _expected(rho_f, p_f, cs2_f) * Phi_f**2)


def test_canonical_scalar_limit_cs2_one():
    rho, pressure = 4.3, 0.7
    measured = matter_action.kessence_lapse_quadratic_coefficient(
        rho=rho, pressure=pressure, cs2=1.0
    )
    assert math.isclose(measured, rho + 0.5 * pressure)


def test_free_kessence_scalar_principal_part_has_intrinsic_sound_speed():
    rho = 4.2
    pressure = 1.4
    cs2 = 1.0 / 3.0
    lapse = 0.8
    scale_factor = 1.7
    k = 3.2
    u = 0.23
    u_dot = -0.41

    measured = matter_action.kessence_scalar_quadratic_density(
        rho=rho,
        pressure=pressure,
        cs2=cs2,
        lapse=lapse,
        scale_factor=scale_factor,
        k=k,
        Phi=0.0,
        B=0.0,
        psi=0.0,
        E=0.0,
        field_ratio=u,
        field_velocity_ratio=u_dot,
    )

    expected = (
        0.5 * (rho + pressure) / cs2 * u_dot**2
        - 0.5 * lapse**2 * (rho + pressure) / scale_factor**2 * k**2 * u**2
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)

    kinetic_coeff = (rho + pressure) / cs2
    gradient_coeff = lapse**2 * (rho + pressure) / scale_factor**2 * k**2
    omega2 = gradient_coeff / kinetic_coeff
    assert math.isclose(omega2, cs2 * lapse**2 * k**2 / scale_factor**2)


def test_full_scalar_action_reduces_to_existing_pure_lapse_identity():
    rho, pressure, cs2 = 2.7, 0.4, 0.63
    Phi = 0.07
    measured = matter_action.kessence_scalar_quadratic_density(
        rho=rho,
        pressure=pressure,
        cs2=cs2,
        lapse=1.2,
        scale_factor=0.9,
        k=4.0,
        Phi=Phi,
        B=0.0,
        psi=0.0,
        E=0.0,
        field_ratio=0.0,
        field_velocity_ratio=0.0,
    )
    expected = matter_action.kessence_pure_lapse_quadratic_density(
        rho=rho, pressure=pressure, cs2=cs2, Phi=Phi
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_shift_enters_as_de_felice_gauge_invariant_spatial_combination():
    rho, pressure, cs2 = 3.0, 0.6, 0.4
    lapse, scale_factor, k = 0.9, 1.3, 2.1
    B, u = -0.12, 0.31
    measured = matter_action.kessence_scalar_quadratic_density(
        rho=rho,
        pressure=pressure,
        cs2=cs2,
        lapse=lapse,
        scale_factor=scale_factor,
        k=k,
        Phi=0.0,
        B=B,
        psi=0.0,
        E=0.0,
        field_ratio=u,
        field_velocity_ratio=0.0,
    )
    shifted = u + scale_factor * B / lapse
    expected = (
        0.5 * pressure * k**2 * B**2
        - 0.5 * lapse**2 * (rho + pressure) / scale_factor**2 * k**2 * shifted**2
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_spatial_metric_trace_and_shear_contractions_match_scalar_decomposition():
    rho, pressure, cs2 = 4.0, 0.8, 0.5
    k, psi, E = 2.4, -0.13, 0.07
    measured = matter_action.kessence_scalar_quadratic_density(
        rho=rho,
        pressure=pressure,
        cs2=cs2,
        lapse=1.0,
        scale_factor=1.0,
        k=k,
        Phi=0.0,
        B=0.0,
        psi=psi,
        E=E,
        field_ratio=0.0,
        field_velocity_ratio=0.0,
    )
    expected = pressure * (1.5 * psi**2 - (1.0 / 6.0) * k**4 * E**2)
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_background_volume_factor_gives_correct_g_and_f_coordinate_speeds():
    cs2_g, cs2_f = 1.0 / 3.0, 0.27
    a, r, c = 0.7, 1.8, 0.65
    b = a * r
    N_g = 1.0
    N_f = r * c
    k = 5.0

    assert hasattr(matter_action, "kessence_scalar_quadratic_lagrangian")

    def coefficients(lapse, scale, rho, pressure, cs2):
        kinetic = matter_action.kessence_scalar_quadratic_lagrangian(
            rho=rho, pressure=pressure, cs2=cs2,
            lapse=lapse, scale_factor=scale, k=k,
            Phi=0.0, B=0.0, psi=0.0, E=0.0,
            field_ratio=0.0, field_velocity_ratio=1.0,
        ) * 2.0
        gradient = -matter_action.kessence_scalar_quadratic_lagrangian(
            rho=rho, pressure=pressure, cs2=cs2,
            lapse=lapse, scale_factor=scale, k=k,
            Phi=0.0, B=0.0, psi=0.0, E=0.0,
            field_ratio=1.0, field_velocity_ratio=0.0,
        ) * 2.0
        return kinetic, gradient

    Kg, Gg = coefficients(N_g, a, 4.0, 4.0 / 3.0, cs2_g)
    Kf, Gf = coefficients(N_f, b, 2.5, 0.4, cs2_f)

    assert math.isclose(Gg / Kg, cs2_g * k**2 / a**2, rel_tol=2e-14)
    assert math.isclose(Gf / Kf, cs2_f * c**2 * k**2 / a**2, rel_tol=2e-14)

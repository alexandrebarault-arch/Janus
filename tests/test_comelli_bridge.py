import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_bridge import (
    beta_to_comelli_a,
    comelli_f1_f2,
    janus_J_Gamma,
    comelli_branch_lhs,
    janus_branch_potential_lhs,
)


def test_beta_to_comelli_factorial_mapping():
    beta = (0.0, 1.2, -3.4, 5.6, -7.8)
    a = beta_to_comelli_a(beta)
    assert a == (0.0, 1.2, -1.7, 5.6 / 6.0, -7.8 / 24.0)


def test_f1_f2_match_janus_J_Gamma():
    beta = (0.0, 1.0, -4.2383993109, 13.6801214252, -38.5117901844)
    y = 0.5922763712069927
    c = 0.8512702016825817
    a = beta_to_comelli_a(beta)
    f1, f2 = comelli_f1_f2(y, c, a)
    J, Gamma = janus_J_Gamma(y, c, beta)
    assert math.isclose(f2, y * J, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(f1, Gamma, rel_tol=0.0, abs_tol=1e-12)


def test_background_constraint_potential_parts_are_same_equation():
    beta = (0.0, 1.0, -4.2383993109, 13.6801214252, -38.5117901844)
    y = 0.9335321962075307
    kappa = 0.10879548725**2
    a = beta_to_comelli_a(beta)
    lhs_comelli = comelli_branch_lhs(y, kappa, a)
    lhs_janus = janus_branch_potential_lhs(y, kappa, beta)
    assert math.isclose(lhs_comelli, -lhs_janus, rel_tol=0.0, abs_tol=1e-12)


def test_additional_gauge_invariants_follow_raw_definitions_not_a3_typo():
    """A.3 must be derived from the raw definitions in Eqs. 4.6-4.7.

    Those definitions imply calB1-calE' = Xi2-c^2 Xi1.  Substitution into
    Phi_i and calF_i therefore fixes A.3 with calE', even though Appendix A
    prints an unprimed calE.  This test is independent of the printed A.3.
    """
    from numerics.comelli_bridge import additional_gauge_invariants

    H = 1.7
    H_omega = 1.1
    c = 0.83
    c_prime = -0.07

    # Raw scalar perturbations and their first derivatives.
    raw_B1, raw_B2 = 0.08, 0.14
    raw_E1, raw_E2 = 0.07, 0.04
    raw_E1_prime, raw_E2_prime = 0.02, -0.01
    raw_F1, raw_F2 = 0.011, -0.006

    Xi1 = raw_B1 + raw_E1_prime
    Xi2 = raw_B2 + raw_E2_prime
    calE = raw_E1 - raw_E2
    calE_prime = raw_E1_prime - raw_E2_prime
    calB1 = raw_B2 - c**2 * raw_B1 + (1.0 - c**2) * raw_E1_prime

    Phi1 = raw_F1 - H * Xi1
    Phi2 = raw_F2 - H_omega * Xi2 / c**2
    calF1 = raw_F2 - raw_F1 + (H - H_omega) * Xi1
    calF2 = raw_F2 - raw_F1 + (H - H_omega) * Xi2 / c**2

    # Identity forced directly by the raw definitions.
    assert math.isclose(calB1 - calE_prime, Xi2 - c**2 * Xi1, abs_tol=1e-12)

    B1_prime = -0.04
    E_double_prime = -0.02
    Psi1, Psi2 = -0.010, 0.006
    gi = additional_gauge_invariants(
        H=H,
        H_omega=H_omega,
        c=c,
        c_prime=c_prime,
        B1=calB1,
        B1_prime=B1_prime,
        E=calE,
        E_prime=calE_prime,
        E_double_prime=E_double_prime,
        Phi1=Phi1,
        Phi2=Phi2,
        Psi1=Psi1,
        Psi2=Psi2,
    )

    assert math.isclose(gi["F1"], calF1, abs_tol=1e-12)
    assert math.isclose(gi["F2"], calF2, abs_tol=1e-12)
    assert math.isclose(
        c**2 * (gi["F2"] + gi["F1"]),
        (calB1 - calE_prime) * (H + H_omega)
        - 2.0 * c**2 * (Phi1 - Phi2),
        abs_tol=1e-12,
    )

    # A.1 and A.4 also contain calE'.
    assert math.isclose(
        gi["B2"], calB1 - (1.0 - c**2) * calE_prime, abs_tol=1e-12
    )
    assert math.isclose(
        c**2 * (gi["A2"] - gi["A1"]),
        (calB1 - calE_prime) * (c * (H - H_omega) - c_prime),
        abs_tol=1e-12,
    )

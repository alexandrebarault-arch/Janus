"""Residual form of the scalar two-matter perturbation equations.

Equations are transcribed from Comelli, Crisostomi & Pilo,
Phys. Rev. D 90, 084003 (2014), arXiv:1403.5679, Appendix A.
Fourier convention: Delta -> -k^2.

The module deliberately exposes equation residuals rather than an ODE solver.
This keeps the published equations independently testable before any DAE
reduction or numerical integration is introduced.
"""

from __future__ import annotations


def metric_slip_residuals(*, a, m2, f1, kappa, c, xi, E,
                          Phi1, Psi1, Phi2, Psi2):
    r1 = Psi1 + Phi1 - m2 * a**2 * f1 * E
    r2 = Psi2 + Phi2 + m2 * a**2 * f1 * E / (kappa * c * xi**2)
    return r1, r2


def fluid_g_residuals(*, w, rho, H, k2, delta_rho, delta_rho_prime,
                      u, u_prime, Phi_prime, Psi):
    if rho == 0.0 or 1.0 + w == 0.0:
        raise ValueError("rho and 1+w must be non-zero")
    continuity = delta_rho_prime - (1.0 + w) * (
        rho * (k2 * u - 3.0 * Phi_prime) - 3.0 * H * delta_rho
    )
    euler = u_prime - (
        (3.0 * w - 1.0) * H * u
        - w / (1.0 + w) * delta_rho / rho
        - Psi
    )
    return continuity, euler


def fluid_f_residuals(*, w, rho, H_omega, c, c_prime_over_c, k2,
                      delta_rho, delta_rho_prime, u, u_prime,
                      Phi_prime, Psi):
    if rho == 0.0 or 1.0 + w == 0.0:
        raise ValueError("rho and 1+w must be non-zero")
    continuity = delta_rho_prime - (1.0 + w) * (
        rho * (k2 * u - 3.0 * Phi_prime) - 3.0 * H_omega * delta_rho
    )
    euler = u_prime - (
        u * ((3.0 * w - 1.0) * H_omega + c_prime_over_c)
        - c**2 * (w / (1.0 + w) * delta_rho / rho + Psi)
    )
    return continuity, euler


def g_einstein_residuals(*, a, m2, f1, f2, H, H_prime, k2, G8pi,
                         rho, pressure, delta_rho, delta_p, u,
                         Phi, Phi_prime, Phi_double_prime,
                         Psi, Psi_prime, E, F, A, B, c):
    r00 = (
        -2.0 * k2 * Phi
        + 6.0 * H * (Psi * H - Phi_prime)
        + a**2 * m2 * f2 * (3.0 * F + k2 * E)
        + G8pi * a**2 * delta_rho
    )
    r0i = (
        2.0 * Psi * H
        - 2.0 * Phi_prime
        + a**2 * m2 * B * f2 / (c + 1.0)
        + G8pi * a**2 * (pressure + rho) * u
    )
    rtrace = (
        m2 * a**2 * (2.0 * f1 * F + f2 * A)
        + 2.0 * Psi * (H**2 + 2.0 * H_prime)
        - 2.0 * Phi_double_prime
        - 2.0 * H * (2.0 * Phi_prime - Psi_prime)
        - G8pi * a**2 * delta_p
    )
    return r00, r0i, rtrace


def f_einstein_residuals(*, a, m2, f1, f2, H_omega, H_omega_prime,
                         c, c_prime_over_c, xi, kappa, k2, G8pi,
                         rho, pressure, delta_rho, delta_p, u,
                         Phi, Phi_prime, Phi_double_prime,
                         Psi, Psi_prime, E, F, A, B):
    c2 = c**2
    xi2 = xi**2
    r00 = (
        -2.0 * c2 * k2 * Phi
        + 6.0 * H_omega * (Psi * H_omega - Phi_prime)
        + m2 * a**2 * f2 * c2 / (kappa * xi2) * (-k2 * E - 3.0 * F)
        + G8pi / kappa * a**2 * c2 * xi2 * delta_rho
    )
    r0i = (
        2.0 * c * (Psi * H_omega - Phi_prime)
        - m2 * a**2 * f2 * B / (kappa * xi2 * (1.0 + c))
        + G8pi / kappa * c * a**2 * xi2 * (pressure + rho) * u
    )
    rtrace = (
        m2 * a**2 / (kappa * xi2) * (2.0 * c * f1 * F + f2 * A)
        + 2.0 * (
            H_omega**2
            + 2.0 * H_omega_prime
            - 2.0 * c_prime_over_c * H_omega
        ) * Psi
        - 2.0 * Phi_double_prime
        + 2.0 * (c_prime_over_c - 2.0 * H_omega) * Phi_prime
        + 2.0 * H_omega * Psi_prime
        - G8pi / kappa * a**2 * c2 * xi2 * delta_p
    )
    return r00, r0i, rtrace

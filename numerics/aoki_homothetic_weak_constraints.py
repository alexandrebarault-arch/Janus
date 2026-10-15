"""Local homothetic weak-metric constraints for the Aoki oscillation sector.

The interaction source is evaluated from the exact Hassan-Rosen square root in
a common radial chart and transformed back to the native g/f charts. The four
unknown weak metric amplitudes ``(phi_g, psi_g, phi_f, psi_f)`` are then fixed by
the native ``tt`` and ``tr`` Einstein constraints for a local Fourier mode.

The interaction prefactors ``mass_g2`` and ``mass_f2`` are explicit. This
keeps the audit independent of any paper-specific normalization of m_g^2 and
m_f^2 and makes the m^2 -> 0 decoupling limit directly testable.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.aoki_hr_native_sources import native_interaction_sources


@dataclass(frozen=True)
class WeakConstraintSolution:
    potentials: np.ndarray
    matrix: np.ndarray
    rhs: np.ndarray
    residual: np.ndarray
    relative_residual: float
    condition_number: float
    source_jacobian: np.ndarray
    f_native_covector: np.ndarray


def _validate_real(name: str, value: float, *, positive: bool = False) -> float:
    x = float(value)
    if not math.isfinite(x) or (positive and x <= 0.0):
        raise ValueError(f"{name} must be {'positive and ' if positive else ''}finite")
    return x


def _native_source_vector(
    x: np.ndarray,
    *,
    betas,
    a_g: float,
    a_g_prime: float,
    a_f: float,
    radius: float,
    mu: float,
    conformal_H: float,
    conformal_H_prime: float,
) -> np.ndarray:
    """Return (Vg00,Vg01,Vf00,Vf01) for one real perturbation sample."""
    (
        phi_g, psi_g, phi_f, psi_f,
        delta_eta, delta_r, delta_eta_t, delta_eta_r, delta_r_t, delta_r_r,
    ) = [float(v) for v in x]

    # Aoki gauge: the oscillatory Stückelberg displacement is carried by the
    # g native chart, while the f chart retains the nonlinear adiabatic map.
    ag = a_g + a_g_prime*delta_eta
    rg = radius + delta_r
    if ag <= 0.0 or rg <= 0.0:
        raise ValueError("linearization sample left the positive g chart")
    Jg = np.array([
        [1.0 + delta_eta_t, delta_eta_r],
        [delta_r_t, 1.0 + delta_r_r],
    ], dtype=float)
    gn = ag*ag*np.diag([-math.exp(2.0*phi_g), math.exp(2.0*psi_g)])
    gang = ag*ag*rg*rg

    M = mu*(2.0 + mu)
    eta_f_t = 1.0 - 0.5*conformal_H_prime*radius*radius*M
    eta_f_r = -conformal_H*radius*M
    rf = (1.0 + mu)*radius
    Jf = np.array([
        [eta_f_t, eta_f_r],
        [0.0, 1.0 + mu],
    ], dtype=float)
    fn = a_f*a_f*np.diag([-math.exp(2.0*phi_f), math.exp(2.0*psi_f)])
    fang = a_f*a_f*rf*rf

    out = native_interaction_sources(
        g_radial_native=gn,
        f_radial_native=fn,
        g_angular_native=gang,
        f_angular_native=fang,
        jacobian_g=Jg,
        jacobian_f=Jf,
        betas=betas,
    )
    return np.asarray([
        out.g_native[0, 0], out.g_native[0, 1],
        out.f_native[0, 0], out.f_native[0, 1],
    ], dtype=float)


def _source_jacobian(*, step: float, **kwargs) -> np.ndarray:
    h = float(step)
    if not math.isfinite(h) or h <= 0.0:
        raise ValueError("source_step must be positive and finite")
    J = np.empty((4, 10), dtype=float)
    for j in range(10):
        e = np.zeros(10, dtype=float)
        e[j] = h
        J[:, j] = (
            _native_source_vector(e, **kwargs)
            - _native_source_vector(-e, **kwargs)
        )/(2.0*h)
    return J


def _tt_tr_matrix(*, a: float, a_prime: float, r: float, omega: float, k: float) -> np.ndarray:
    """2x2 native Einstein matrix for columns (phi,psi), rows (tt,tr)."""
    a2 = a*a
    a3 = a2*a
    a4 = a2*a2
    iw_t = -1j*omega
    ik_r = 1j*k
    return np.array([
        [
            6.0*a_prime*a_prime/a4,
            -2.0*(a*a_prime*iw_t/a4 + ik_r/(r*a2) + 1.0/(r*r*a2)),
        ],
        [
            -2.0*a_prime*ik_r/a3,
            -2.0*iw_t/(r*a2),
        ],
    ], dtype=complex)


def solve_weak_metric_constraints(
    *,
    betas,
    a_g: float,
    a_g_prime: float,
    a_f: float,
    a_f_prime: float,
    conformal_H: float,
    conformal_H_prime: float,
    radius: float,
    mu: float,
    omega: float,
    k: float,
    delta_eta: complex,
    delta_r: complex,
    mass_g2: float,
    mass_f2: float,
    source_step: float = 2.0e-6,
) -> WeakConstraintSolution:
    """Solve the four local native ``tt,tr`` weak Einstein constraints.

    The Fourier convention is ``exp[i(k r - omega eta)]`` in the common
    chart. Covectors are transformed to the f-native chart by
    ``q_f = J_f^{-T} q_common`` on the nonlinear homothetic background.
    """
    beta = tuple(float(v) for v in betas)
    if len(beta) != 5 or not all(math.isfinite(v) for v in beta):
        raise ValueError("betas must contain five finite coefficients")
    a_g = _validate_real("a_g", a_g, positive=True)
    a_f = _validate_real("a_f", a_f, positive=True)
    a_g_prime = _validate_real("a_g_prime", a_g_prime)
    a_f_prime = _validate_real("a_f_prime", a_f_prime)
    conformal_H = _validate_real("conformal_H", conformal_H)
    conformal_H_prime = _validate_real("conformal_H_prime", conformal_H_prime)
    radius = _validate_real("radius", radius, positive=True)
    mu = _validate_real("mu", mu)
    omega = _validate_real("omega", omega)
    k = _validate_real("k", k)
    mass_g2 = _validate_real("mass_g2", mass_g2)
    mass_f2 = _validate_real("mass_f2", mass_f2)
    if mu <= -1.0:
        raise ValueError("mu must exceed -1")
    if mass_g2 < 0.0 or mass_f2 < 0.0:
        raise ValueError("interaction mass prefactors must be non-negative")
    delta_eta = complex(delta_eta)
    delta_r = complex(delta_r)
    if not all(math.isfinite(v) for z in (delta_eta, delta_r) for v in (z.real, z.imag)):
        raise ValueError("Stueckelberg amplitudes must be finite")

    src_kwargs = dict(
        betas=beta,
        a_g=a_g,
        a_g_prime=a_g_prime,
        a_f=a_f,
        radius=radius,
        mu=mu,
        conformal_H=conformal_H,
        conformal_H_prime=conformal_H_prime,
    )
    Jsrc = _source_jacobian(step=source_step, **src_kwargs)

    q_common = np.array([-omega, k], dtype=float)
    M = mu*(2.0 + mu)
    Jf_background = np.array([
        [1.0 - 0.5*conformal_H_prime*radius*radius*M, -conformal_H*radius*M],
        [0.0, 1.0 + mu],
    ], dtype=float)
    q_f = np.linalg.solve(Jf_background.T, q_common)
    omega_f = -float(q_f[0])
    k_f = float(q_f[1])
    r_f = (1.0 + mu)*radius

    E = np.zeros((4, 4), dtype=complex)
    E[:2, :2] = _tt_tr_matrix(
        a=a_g, a_prime=a_g_prime, r=radius, omega=omega, k=k,
    )
    E[2:, 2:] = _tt_tr_matrix(
        a=a_f, a_prime=a_f_prime, r=r_f, omega=omega_f, k=k_f,
    )

    rates = np.array([
        delta_eta,
        delta_r,
        -1j*omega*delta_eta,
        +1j*k*delta_eta,
        -1j*omega*delta_r,
        +1j*k*delta_r,
    ], dtype=complex)
    source_stueck = Jsrc[:, 4:] @ rates
    source_potentials = Jsrc[:, :4].astype(complex)
    row_mass = np.array([mass_g2, mass_g2, mass_f2, mass_f2], dtype=float)

    matrix = E + row_mass[:, None]*source_potentials
    rhs = -row_mass*source_stueck
    try:
        potentials = np.linalg.solve(matrix, rhs)
    except np.linalg.LinAlgError as exc:
        raise np.linalg.LinAlgError("weak tt/tr constraint matrix is singular") from exc
    residual = matrix@potentials - rhs
    denom = max(
        1.0e-30,
        float(np.linalg.norm(rhs)),
        float(np.linalg.norm(matrix@potentials)),
    )
    relative = float(np.linalg.norm(residual)/denom)
    return WeakConstraintSolution(
        potentials=np.asarray(potentials, dtype=complex),
        matrix=np.asarray(matrix, dtype=complex),
        rhs=np.asarray(rhs, dtype=complex),
        residual=np.asarray(residual, dtype=complex),
        relative_residual=relative,
        condition_number=float(np.linalg.cond(matrix)),
        source_jacobian=np.asarray(Jsrc, dtype=float),
        f_native_covector=np.asarray(q_f, dtype=float),
    )

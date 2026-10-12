import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.bigravity_scalar_action import hr_diagonal_scalar_potential_density
from numerics.hr_scalar_potential import (
    hr_scalar_potential_density_de_felice,
    hr_scalar_quadratic_potential_density_de_felice,
)


def test_full_hr_scalar_potential_matches_existing_diagonal_limit():
    a = 0.73
    r = 1.21
    nbar = 1.08
    m2 = 0.67
    Mg2 = 1.4
    k = 2.6
    betas = (0.19, 0.41, -0.23, 0.17, 0.31)

    Phi1L, Psi1L, E1L = 0.032, -0.021, 0.008
    Phi2L, Psi2L, E2L = -0.026, 0.018, -0.006
    old = hr_diagonal_scalar_potential_density(
        a=a, r=r, Nbar=nbar, m2=m2, M1sq=Mg2,
        betas=betas, k=k,
        Phi1=Phi1L, Phi2=Phi2L,
        Psi1=Psi1L, E1=E1L,
        Psi2=Psi2L, E2=E2L,
    )

    psi_g = -Psi1L - k*k*E1L/3.0
    E_g = 2.0*E1L
    psi_f = -Psi2L - k*k*E2L/3.0
    E_f = 2.0*E2L
    new = hr_scalar_potential_density_de_felice(
        N=1.0, a=a, n=nbar, alpha=a*r,
        m2=m2, Mg2=Mg2, betas=betas, k=k,
        Phi_g=Phi1L/2.0, B_g=0.0, psi_g=psi_g, E_g=E_g,
        Phi_f=Phi2L/2.0, B_f=0.0, psi_f=psi_f, E_f=E_f,
    )
    assert math.isclose(new, old, rel_tol=3e-12, abs_tol=3e-12)


def test_quadratic_hr_shift_block_matches_de_felice_delta_rank_one_form():
    # beta1-only => J=1 exactly.  Eq. (45)-(46) gives
    # L_shift = (1/2) m^2 Mg^2 N a^3 xi J/(ctilde+1)
    #           * k^2 (B_g-ctilde B_f)^2.
    N = 1.0
    a = 0.8
    xi = 1.17
    ctilde = 0.86
    alpha = a*xi
    n = N*xi*ctilde
    m2 = 0.7
    Mg2 = 1.3
    k = 2.2
    betas = (0.0,1.0,0.0,0.0,0.0)

    common = dict(
        N=N, a=a, n=n, alpha=alpha, m2=m2, Mg2=Mg2,
        betas=betas, k=k,
        Phi_g=0.0, psi_g=0.0, E_g=0.0,
        Phi_f=0.0, psi_f=0.0, E_f=0.0,
    )
    h = 2e-5
    def V(bg_shift, bf_shift):
        return hr_scalar_quadratic_potential_density_de_felice(
            **common, B_g=bg_shift, B_f=bf_shift
        )

    base = V(0.0,0.0)
    q11 = (V(h,0.0)-2.0*base+V(-h,0.0))/h**2
    q22 = (V(0.0,h)-2.0*base+V(0.0,-h))/h**2
    q12 = (V(h,h)-V(h,-h)-V(-h,h)+V(-h,-h))/(4.0*h*h)

    coeff = 0.5*m2*Mg2*N*a**3*xi/(ctilde+1.0)*k*k
    assert math.isclose(q11, 2.0*coeff, rel_tol=3e-7, abs_tol=3e-7)
    assert math.isclose(q12, -2.0*coeff*ctilde, rel_tol=3e-7, abs_tol=3e-7)
    assert math.isclose(q22, 2.0*coeff*ctilde**2, rel_tol=3e-7, abs_tol=3e-7)
    assert math.isclose(q11*q22-q12*q12, 0.0, abs_tol=3e-5)


def test_quadratic_helper_reduces_to_exact_diagonal_potential_when_shifts_vanish():
    kwargs = dict(
        N=1.0, a=0.8, n=1.06, alpha=0.92,
        m2=0.7, Mg2=1.3, betas=(0.2,0.4,-0.1,0.15,0.3), k=2.2,
        Phi_g=0.03, B_g=0.0, psi_g=-0.02, E_g=0.004,
        Phi_f=-0.01, B_f=0.0, psi_f=0.015, E_f=-0.003,
    )
    exact = hr_scalar_potential_density_de_felice(**kwargs)
    quadratic = hr_scalar_quadratic_potential_density_de_felice(**kwargs)
    assert math.isclose(quadratic, exact, rel_tol=3e-13, abs_tol=3e-13)

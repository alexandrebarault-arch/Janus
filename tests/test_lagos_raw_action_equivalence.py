import math
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.de_felice_consistent_px_control import consistent_px_background
from numerics.de_felice_raw_scalar_action import (
    RawBimetricBackground,
    raw_two_matter_scalar_density_g_flat,
)
from numerics.lagos_two_matter_action import (
    KessenceBackground,
    two_matter_lagrangian_healthy,
)


M2 = 23.3348939346


def _metric_background(b, k):
    return ScalarBackground(
        a=b.a,
        m2=M2,
        f1=b.gamma_m / M2,
        f2=b.zeta / M2,
        H=b.a * b.H,
        H_omega=b.ctilde * b.a * b.H,
        c=b.ctilde,
        xi=b.xi,
        kappa=b.kappa,
        k2=k * k,
        G8pi=1.0,
    )


def _raw_background(b):
    return RawBimetricBackground(
        N=1.0,
        a=b.a,
        xi=b.xi,
        ctilde=b.ctilde,
        kappa=b.kappa,
        H=b.H,
        Hf=b.Hf,
        Hdot_over_N=b.Hdot,
        Hfdot_over_n=b.Hfdot_over_n,
        mu_g=b.mu_g,
        mu_f=b.mu_f,
        zeta=b.zeta,
        gamma_m=b.gamma_m,
        Mgsq=1.0,
    )


def _compare_one_point(a, raw):
    b=consistent_px_background(a, cs2_g=0.4, cs2_f=0.3)
    k=7.0
    (
        Phi,Bdf,varphi,bdf,Sigma,S,Sigma_dot,S_dot,
        u_g,q_g,u_f,q_f,
    )=raw

    # Exact De Felice <-> Lagos scalar map in g-flat gauge.
    Psi1=0.0
    E1=0.0
    Psi2=-Sigma-k*k*S/6.0
    E2=S/2.0
    Psi1_dot=0.0
    E1_dot=0.0
    Psi2_dot=-Sigma_dot-k*k*S_dot/6.0
    E2_dot=S_dot/2.0
    B1=b.a*Bdf
    B2=b.a*b.xi*bdf

    state=np.array([
        Psi1,Psi2,E1,E2,Phi,varphi,B1,B2,u_g,u_f,
    ])
    rates=np.array([
        Psi1_dot,Psi2_dot,E1_dot,E2_dot,q_g,q_f,
    ])
    matter_g=KessenceBackground(b.rho_g,b.pressure_g,0.4)
    matter_f=KessenceBackground(b.rho_f,b.pressure_f,0.3)
    lagos=two_matter_lagrangian_healthy(
        _metric_background(b,k), matter_g, matter_f, state, rates
    )

    de_felice=raw_two_matter_scalar_density_g_flat(
        _raw_background(b),
        k=k,
        Phi=Phi,
        B=Bdf,
        varphi=varphi,
        b=bdf,
        Sigma=Sigma,
        S=S,
        Sigma_dot=Sigma_dot,
        S_dot=S_dot,
        rho_g=b.rho_g,
        pressure_g=b.pressure_g,
        cs2_g=0.4,
        u_g=u_g,
        u_g_dot=q_g,
        rho_f=b.rho_f,
        pressure_f=b.pressure_f,
        cs2_f=0.3,
        u_f=u_f,
        u_f_dot=q_f,
    )
    return lagos,de_felice,b


def test_lagos_two_matter_action_matches_raw_de_felice_in_common_gauge():
    raw=np.array([
        0.041,-0.027,-0.019,0.033,0.014,-0.0032,
        -0.021,0.0041,0.026,-0.017,-0.023,0.031,
    ])
    for a in (0.5,0.4,0.3):
        lagos,de_felice,b=_compare_one_point(a,raw)
        assert b.ctilde>0.0
        assert math.isclose(lagos,de_felice,rel_tol=2e-11,abs_tol=2e-11)

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import (
    ScalarBackground,
    ScalarBackgroundDerivatives,
    MetricState,
    MatterSources,
    MatterEvolutionSources,
    constraint_residual_vector,
    solve_metric_constraints,
    acceleration_residual_vector,
    solve_metric_accelerations,
)


def test_acceleration_solver_recovers_manufactured_solution():
    bg = ScalarBackground(
        a=0.73, m2=2.4, f1=0.36, f2=0.58,
        H=1.35, H_omega=1.01, c=0.7481481481481481,
        xi=1.18, kappa=0.21, k2=4.7, G8pi=1.0,
    )
    bgp = ScalarBackgroundDerivatives(
        H_prime=-0.42,
        H_omega_prime=-0.31,
        c_prime=-0.08,
        xi_prime=0.05,
        f1_prime=0.02,
        f2_prime=-0.03,
    )
    state = MetricState(E=0.031, Phi1=0.018, Phi2=-0.012)
    E_p, P1_p, P2_p = 0.009, -0.006, 0.004
    B1 = 0.022
    B2 = B1 - (1.0 - bg.c**2) * E_p
    dphi = state.Phi1 - state.Phi2
    fsum = ((B1-E_p)*(bg.H+bg.H_omega) - 2*bg.c**2*dphi) / bg.c**2
    fdiff = (bg.H-bg.H_omega)*dphi
    F1 = (bg.H_omega*fsum - fdiff)/(bg.H+bg.H_omega)
    F2 = fsum - F1
    q_true = np.array([E_p, P1_p, P2_p, B1, B2, F1, F2])

    psi1 = bg.a**2*bg.m2*bg.f1*state.E - state.Phi1
    psi2 = -bg.a**2*bg.m2*bg.f1*state.E/(bg.kappa*bg.c*bg.xi**2) - state.Phi2
    base_g00 = (-2*bg.k2*state.Phi1
                +6*bg.H*(psi1*bg.H-P1_p)
                +bg.a**2*bg.m2*bg.f2*(3*F1+bg.k2*state.E))
    drho_g = -base_g00/(bg.G8pi*bg.a**2)
    base_g0i = (2*psi1*bg.H - 2*P1_p
                + bg.a**2*bg.m2*B1*bg.f2/(bg.c+1))
    mom_g = -base_g0i/(bg.G8pi*bg.a**2)

    c2=bg.c**2; xi2=bg.xi**2
    base_f00 = (-2*c2*bg.k2*state.Phi2
                +6*bg.H_omega*(psi2*bg.H_omega-P2_p)
                +bg.m2*bg.a**2*bg.f2*c2/(bg.kappa*xi2)
                  *(-bg.k2*state.E-3*F2))
    drho_f = -base_f00*bg.kappa/(bg.G8pi*bg.a**2*c2*xi2)
    base_f0i = (2*bg.c*(psi2*bg.H_omega-P2_p)
                -bg.m2*bg.a**2*bg.f2*B2/(bg.kappa*xi2*(1+bg.c)))
    mom_f = -base_f0i*bg.kappa/(bg.G8pi*bg.c*bg.a**2*xi2)
    src = MatterSources(drho_g, mom_g, drho_f, mom_f)

    solved_constraints = solve_metric_constraints(
        bg, state, src, E_prime=E_p
    )
    assert np.max(np.abs(solved_constraints.vector-q_true)) < 2e-12

    E_pp, P1_pp, P2_pp, B1_p = 0.003, -0.002, 0.0015, -0.004
    acc_true = np.array([E_pp, P1_pp, P2_pp, B1_p])

    K1 = bg.a**2*bg.m2*bg.f1
    K1_p = K1*(2*bg.H + bgp.f1_prime/bg.f1)
    psi1_p = K1_p*state.E + K1*E_p - P1_p
    K2 = bg.a**2*bg.m2*bg.f1/(bg.kappa*bg.c*xi2)
    K2_p = K2*(2*bg.H + bgp.f1_prime/bg.f1
               - bgp.c_prime/bg.c - 2*bgp.xi_prime/bg.xi)
    psi2_p = -K2_p*state.E - K2*E_p - P2_p

    Cg = bg.a**2*bg.m2*bg.f2/(1+bg.c)
    Cg_p = Cg*(2*bg.H + bgp.f2_prime/bg.f2
               - bgp.c_prime/(1+bg.c))
    dg0_base = (2*bgp.H_prime*psi1 + 2*bg.H*psi1_p - 2*P1_pp
                + Cg_p*B1 + Cg*B1_p
                + bg.G8pi*bg.a**2*2*bg.H*mom_g)
    mom_g_p = -dg0_base/(bg.G8pi*bg.a**2)

    Cf = bg.m2*bg.a**2*bg.f2/(bg.kappa*xi2*(1+bg.c))
    Cf_p = Cf*(2*bg.H + bgp.f2_prime/bg.f2
               -2*bgp.xi_prime/bg.xi - bgp.c_prime/(1+bg.c))
    Df = bg.G8pi/bg.kappa*bg.c*bg.a**2*xi2
    Df_p = Df*(bgp.c_prime/bg.c + 2*bg.H + 2*bgp.xi_prime/bg.xi)
    B2_p = B1_p + 2*bg.c*bgp.c_prime*E_p - (1-c2)*E_pp
    df0_base = (2*bgp.c_prime*(psi2*bg.H_omega-P2_p)
                +2*bg.c*(psi2_p*bg.H_omega + psi2*bgp.H_omega_prime-P2_pp)
                -Cf_p*B2 - Cf*B2_p + Df_p*mom_f)
    mom_f_p = -df0_base/Df

    a_diff = (B1-E_p)*(bg.c*(bg.H-bg.H_omega)-bgp.c_prime)/c2
    a_sum = (2*bg.c**3*(psi2-psi1)
             +B1*(bg.c*(bg.H_omega+bg.H)-3*bgp.c_prime)
             +3*bgp.c_prime*E_p
             +bg.c*(2*B1_p-2*E_pp-E_p*(bg.H_omega+bg.H)))/c2
    A1 = 0.5*(a_sum-a_diff)
    A2 = 0.5*(a_sum+a_diff)

    base_gtrace = (bg.m2*bg.a**2*(2*bg.f1*F1+bg.f2*A1)
                   +2*psi1*(bg.H**2+2*bgp.H_prime)
                   -2*P1_pp -2*bg.H*(2*P1_p-psi1_p))
    delta_p_g = base_gtrace/(bg.G8pi*bg.a**2)

    base_ftrace = (bg.m2*bg.a**2/(bg.kappa*xi2)
                   *(2*bg.c*bg.f1*F2+bg.f2*A2)
                   +2*(bg.H_omega**2+2*bgp.H_omega_prime
                       -2*(bgp.c_prime/bg.c)*bg.H_omega)*psi2
                   -2*P2_pp
                   +2*(bgp.c_prime/bg.c-2*bg.H_omega)*P2_p
                   +2*bg.H_omega*psi2_p)
    delta_p_f = base_ftrace*bg.kappa/(bg.G8pi*bg.a**2*c2*xi2)

    evo = MatterEvolutionSources(
        momentum_g_prime=mom_g_p,
        momentum_f_prime=mom_f_p,
        delta_p_g=delta_p_g,
        delta_p_f=delta_p_f,
    )
    solved = solve_metric_accelerations(
        bg, bgp, state, solved_constraints, src, evo
    )
    assert np.allclose(solved.vector, acc_true, rtol=0.0, atol=3e-11)
    assert solved.rank == 4
    assert solved.condition_number < 1e7
    assert np.linalg.norm(
        acceleration_residual_vector(
            solved.vector, bg, bgp, state, solved_constraints, src, evo
        ), ord=np.inf
    ) < 1e-10

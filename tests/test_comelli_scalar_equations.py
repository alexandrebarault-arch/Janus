import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_scalar_equations import (
    fluid_g_residuals,
    fluid_f_residuals,
    metric_slip_residuals,
    g_einstein_residuals,
    f_einstein_residuals,
)


def test_metric_slip_residuals_vanish_on_published_algebraic_solution():
    a, m2, f1 = 0.7, 2.3, 0.41
    kappa, c, xi, E = 0.17, 0.82, 1.3, 0.06
    phi1, phi2 = 0.02, -0.03
    psi1 = a*a*m2*f1*E - phi1
    psi2 = -a*a*m2*f1*E/(kappa*c*xi*xi) - phi2
    r1, r2 = metric_slip_residuals(a=a, m2=m2, f1=f1, kappa=kappa,
                                    c=c, xi=xi, E=E,
                                    Phi1=phi1, Psi1=psi1,
                                    Phi2=phi2, Psi2=psi2)
    assert abs(r1) < 1e-14
    assert abs(r2) < 1e-14


def test_fluid_conservation_residuals_vanish_for_constructed_derivatives():
    w, rho, H, k2 = 0.0, 3.2, 1.4, 5.0
    drho, u, phip, psi = 0.04, -0.02, 0.003, 0.01
    drhop = (1+w) * (rho*(k2*u - 3*phip) - 3*H*drho)
    up = (3*w-1)*H*u - w/(1+w)*drho/rho - psi
    r = fluid_g_residuals(w=w, rho=rho, H=H, k2=k2,
                          delta_rho=drho, delta_rho_prime=drhop,
                          u=u, u_prime=up, Phi_prime=phip, Psi=psi)
    assert max(abs(x) for x in r) < 1e-14

    w2, rho2, Hw, cp_over_c, c = 1/3, 2.7, 0.9, -0.08, 0.76
    drho2, u2, phi2p, psi2 = -0.06, 0.015, -0.004, -0.012
    drho2p = (1+w2) * (rho2*(k2*u2 - 3*phi2p) - 3*Hw*drho2)
    u2p = u2*((3*w2-1)*Hw + cp_over_c) - c*c*(w2/(1+w2)*drho2/rho2 + psi2)
    r = fluid_f_residuals(w=w2, rho=rho2, H_omega=Hw,
                          c=c, c_prime_over_c=cp_over_c, k2=k2,
                          delta_rho=drho2, delta_rho_prime=drho2p,
                          u=u2, u_prime=u2p, Phi_prime=phi2p, Psi=psi2)
    assert max(abs(x) for x in r) < 1e-14


def test_g_einstein_residuals_match_a10_a11_a12_trace():
    p = dict(a=0.8, m2=1.9, f1=0.37, f2=0.52, H=1.2, H_prime=-0.4,
             k2=3.1, G8pi=1.0, rho=2.2, pressure=0.0,
             delta_rho=0.07, delta_p=0.0, u=-0.013,
             Phi=0.021, Phi_prime=-0.004, Phi_double_prime=0.006,
             Psi=-0.017, Psi_prime=0.005, E=0.03, F=0.011,
             A=-0.009, B=0.014, c=0.86)
    base00 = (-2*p['k2']*p['Phi'] + 6*p['H']*(p['Psi']*p['H']-p['Phi_prime'])
              + p['a']**2*p['m2']*p['f2']*(3*p['F'] + p['k2']*p['E']))
    p['delta_rho'] = -base00/(p['G8pi']*p['a']**2)
    basemom = (2*p['Psi']*p['H'] - 2*p['Phi_prime']
               + p['a']**2*p['m2']*p['B']*p['f2']/(p['c']+1))
    p['u'] = -basemom/(p['G8pi']*p['a']**2*(p['rho']+p['pressure']))
    basetr = (p['m2']*p['a']**2*(2*p['f1']*p['F']+p['f2']*p['A'])
              + 2*p['Psi']*(p['H']**2+2*p['H_prime'])
              - 2*p['Phi_double_prime']
              - 2*p['H']*(2*p['Phi_prime']-p['Psi_prime']))
    p['delta_p'] = basetr/(p['G8pi']*p['a']**2)
    r = g_einstein_residuals(**p)
    assert max(abs(x) for x in r) < 1e-13


def test_f_einstein_residuals_match_a14_a15_a16_trace():
    p = dict(a=0.8, m2=1.9, f1=0.37, f2=0.52, H_omega=0.95,
             H_omega_prime=-0.31, c=0.86, c_prime_over_c=-0.07,
             xi=1.25, kappa=0.19, k2=3.1, G8pi=1.0,
             rho=1.7, pressure=0.0, delta_rho=0.03, delta_p=0.0,
             u=0.01, Phi=-0.016, Phi_prime=0.002,
             Phi_double_prime=-0.005, Psi=0.012, Psi_prime=-0.003,
             E=0.03, F=-0.008, A=0.007, B=-0.012)
    c2=p['c']**2; xi2=p['xi']**2
    base00 = (-2*c2*p['k2']*p['Phi']
              + 6*p['H_omega']*(p['Psi']*p['H_omega']-p['Phi_prime'])
              + p['m2']*p['a']**2*p['f2']*c2/(p['kappa']*xi2)
                *(-p['k2']*p['E']-3*p['F']))
    p['delta_rho'] = -base00 * p['kappa']/(p['G8pi']*p['a']**2*c2*xi2)
    basemom = (2*p['c']*(p['Psi']*p['H_omega']-p['Phi_prime'])
               - p['m2']*p['a']**2*p['f2']*p['B']
                 /(p['kappa']*xi2*(1+p['c'])))
    p['u'] = -basemom*p['kappa']/(p['G8pi']*p['c']*p['a']**2*xi2*(p['rho']+p['pressure']))
    basetr = (p['m2']*p['a']**2/(p['kappa']*xi2)
              *(2*p['c']*p['f1']*p['F']+p['f2']*p['A'])
              + 2*(p['H_omega']**2+2*p['H_omega_prime']
                   -2*p['c_prime_over_c']*p['H_omega'])*p['Psi']
              -2*p['Phi_double_prime']
              +2*(p['c_prime_over_c']-2*p['H_omega'])*p['Phi_prime']
              +2*p['H_omega']*p['Psi_prime'])
    p['delta_p'] = basetr*p['kappa']/(p['G8pi']*p['a']**2*c2*xi2)
    r = f_einstein_residuals(**p)
    assert max(abs(x) for x in r) < 1e-13

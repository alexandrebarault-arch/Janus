"""Compact homothetic six-field HR oracle using the shared native-chart density.

This mirrors ``aoki_compact_sixfield_action`` but delegates the Hassan-Rosen
square-root/density evaluation to ``native_hr_potential_density``.  It exists
as a bridge oracle before the same native primitive is promoted to a genuinely
non-homothetic finite-mu Candidate-C action.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.nonhomothetic_hr_native_action import native_hr_potential_density


@dataclass(frozen=True)
class CompactNativeHRSixFieldHessian:
    gradient: np.ndarray
    hessian: np.ndarray


def _profile_value(t, r, T, R):
    if abs(t) >= T or r <= 0.0 or r >= R:
        return 0.0
    x = t/T
    return (1.0-x*x)**3*(r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6)


def _profiles(t, r, T, R):
    x = t/T
    A = (1.0-x*x)**3
    At = (-6.0*x*(1.0-x*x)**2)/T
    Att = (-6.0+36.0*x*x-30.0*x**4)/(T*T)
    F = r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    Fr = 2.0*r-12.0*r**3/R**2+18.0*r**5/R**4-8.0*r**7/R**6
    Frr = 2.0-36.0*r**2/R**2+90.0*r**4/R**4-56.0*r**6/R**6
    return A, At, Att, F, Fr, Frr


def _action(x, *, betas, K, w, mu, conformal_H,
            time_radius, radial_radius, quadrature_order):
    eta_amp, r_amp, pg, sg, pf, sf = [float(v) for v in x]
    if abs(1.0+3.0*w) < 1.0e-12:
        raise ValueError("w=-1/3 requires a separate conformal chart")
    p = 2.0/(1.0+3.0*w)
    xt, wt = np.polynomial.legendre.leggauss(quadrature_order)
    xr, wr = np.polynomial.legendre.leggauss(quadrature_order)
    ts = time_radius*xt
    rs = 0.5*radial_radius*(xr+1.0)
    tw = time_radius*wt
    rw = 0.5*radial_radius*wr
    C = mu/(1.0+mu)
    M = mu*(2.0+mu)
    total = 0.0

    for i, t in enumerate(ts):
        u = 1.0+conformal_H*t/p
        if u <= 0.0:
            raise ValueError("compact support leaves FLRW chart")
        Hc = conformal_H/u
        Hcp = -(conformal_H*conformal_H/p)/(u*u)
        abase = u**p
        inva2 = abase**-2
        inva2_t = -2.0*Hc*inva2

        for j, r in enumerate(rs):
            A, At, Att, F, Fr, Frr = _profiles(
                t, r, time_radius, radial_radius,
            )
            P = At*F
            Q = A*Fr
            Pt = Att*F
            Pr = At*Fr
            Qt = Pr
            Qr = A*Frr

            E = inva2*(-P+r*Hc*C*Q)
            Et = (
                inva2_t*(-P+r*Hc*C*Q)
                + inva2*(-Pt+r*C*(Hcp*Q+Hc*Qt))
            )
            Er = inva2*(-Pr+C*Hc*(Q+r*Qr))
            R = inva2*(Q/(1.0+mu)+r*Hc*C*P)
            Rt = (
                inva2_t*(Q/(1.0+mu)+r*Hc*C*P)
                + inva2*(Qt/(1.0+mu)+r*C*(Hcp*P+Hc*Pt))
            )
            Rr = inva2*(Qr/(1.0+mu)+C*Hc*(P+r*Pr))

            deta = eta_amp*E
            deta_t = eta_amp*Et
            deta_r = eta_amp*Er
            drad = r_amp*R
            drad_t = r_amp*Rt
            drad_r = r_amp*Rr

            eta_g = t+deta
            rg = r+drad
            ug = 1.0+conformal_H*eta_g/p
            if ug <= 0.0 or rg <= 0.0:
                raise ValueError("g chart left positive branch")
            ag = ug**p
            phig = pg*_profile_value(eta_g, rg, time_radius, radial_radius)
            psig = sg*_profile_value(eta_g, rg, time_radius, radial_radius)
            Jg = np.array([
                [1.0+deta_t, deta_r],
                [drad_t, 1.0+drad_r],
            ], dtype=float)
            gn = ag*ag*np.diag([-math.exp(2.0*phig), math.exp(2.0*psig)])
            gang = ag*ag*rg*rg

            eta_f = t-0.5*Hc*r*r*M
            eta_ft = 1.0-0.5*Hcp*r*r*M
            eta_fr = -Hc*r*M
            rf = (1.0+mu)*r
            uf = 1.0+conformal_H*eta_f/p
            if uf <= 0.0 or rf <= 0.0:
                raise ValueError("f chart left positive branch")
            af = uf**p
            phif = pf*_profile_value(eta_f, rf, time_radius, radial_radius)
            psif = sf*_profile_value(eta_f, rf, time_radius, radial_radius)
            Jf = np.array([
                [eta_ft, eta_fr],
                [0.0, 1.0+mu],
            ], dtype=float)
            fn = (K*af)**2*np.diag([-math.exp(2.0*phif), math.exp(2.0*psif)])
            fang = (K*af)**2*rf*rf

            total += tw[i]*rw[j]*native_hr_potential_density(
                g_radial_native=gn,
                f_radial_native=fn,
                g_angular_native=gang,
                f_angular_native=fang,
                jacobian_g=Jg,
                jacobian_f=Jf,
                betas=betas,
                m2=1.0,
                Mg2=1.0,
            )
    return float(total)


def compact_native_hr_six_field_hessian(
    *, betas, K, w, mu, conformal_H, time_radius, radial_radius,
    amplitude_step=7.0e-4, quadrature_order=16,
):
    beta = tuple(float(v) for v in betas)
    if len(beta) != 5 or K <= 0.0 or mu <= -1.0 or amplitude_step <= 0.0:
        raise ValueError("invalid compact native HR inputs")
    if quadrature_order < 8:
        raise ValueError("quadrature_order must be at least 8")
    h = float(amplitude_step)
    n = 6
    kwargs = dict(
        betas=beta, K=float(K), w=float(w), mu=float(mu),
        conformal_H=float(conformal_H), time_radius=float(time_radius),
        radial_radius=float(radial_radius), quadrature_order=int(quadrature_order),
    )
    zero = np.zeros(n, dtype=float)
    f0 = _action(zero, **kwargs)
    gradient = np.zeros(n, dtype=float)
    H = np.zeros((n, n), dtype=float)
    for i in range(n):
        ei = np.zeros(n, dtype=float)
        ei[i] = h
        fp = _action(ei, **kwargs)
        fm = _action(-ei, **kwargs)
        gradient[i] = (fp-fm)/(2.0*h)
        H[i, i] = (fp-2.0*f0+fm)/(h*h)
        for j in range(i+1, n):
            ej = np.zeros(n, dtype=float)
            ej[j] = h
            value = (
                _action(ei+ej, **kwargs) - _action(ei-ej, **kwargs)
                - _action(-ei+ej, **kwargs) + _action(-ei-ej, **kwargs)
            )/(4.0*h*h)
            H[i, j] = H[j, i] = value
    return CompactNativeHRSixFieldHessian(
        gradient=np.asarray(gradient, dtype=float),
        hessian=np.asarray(H, dtype=float),
    )

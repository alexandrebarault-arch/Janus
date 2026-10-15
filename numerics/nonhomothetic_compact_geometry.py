"""Local compact background geometry for non-homothetic spherical pullbacks."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class NonhomotheticBackgroundMap:
    t: float
    r: float
    a: float
    xi: float
    c: float
    mu: float
    q: float
    eta_f: float
    r_f: float
    Jg: np.ndarray
    Jf: np.ndarray
    g_common: np.ndarray
    f_common: np.ndarray
    g_angular: float
    f_angular: float
    b_native: float


def background_map(*, t: float, r: float, jet, mu: float,
                   mu_p: float = 0.0, mu_pp: float = 0.0) -> NonhomotheticBackgroundMap:
    """Evaluate the local adiabatic two-metric map on a quadratic time jet.

    ``t`` is the common g-sector conformal time measured from the jet center.
    The f-native background conformal coordinate obeys ``d eta_f = c d t``.
    The nonlinear radial map is ``r_f=(1+mu) r`` and the temporal spherical
    shift is fixed by the exact non-homothetic relation

    ``q = mu' + Hc*mu*(c+1+mu)``, ``eta_f = integral(c dt)-q r^2/2``.
    """
    vals=(t,r,mu,mu_p,mu_pp,jet.a,jet.a_p,jet.a_pp,jet.xi,jet.xi_p,
          jet.xi_pp,jet.c,jet.c_p)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("background map inputs must be finite")
    if r <= 0.0 or mu <= -1.0:
        raise ValueError("require r>0 and mu>-1")

    t=float(t); r=float(r)
    a=jet.a + jet.a_p*t + 0.5*jet.a_pp*t*t
    ap=jet.a_p + jet.a_pp*t
    xi=jet.xi + jet.xi_p*t + 0.5*jet.xi_pp*t*t
    c=jet.c + jet.c_p*t
    mut=float(mu) + float(mu_p)*t + 0.5*float(mu_pp)*t*t
    mut_p=float(mu_p) + float(mu_pp)*t
    if a <= 0.0 or xi <= 0.0 or c <= 0.0 or mut <= -1.0:
        raise ValueError("local Taylor background left the regular positive branch")

    Hc=ap/a
    Hc_p=jet.a_pp/a - Hc*Hc
    S=c + 1.0 + mut
    q=mut_p + Hc*mut*S
    q_p=(float(mu_pp)
         + Hc_p*mut*S
         + Hc*mut_p*S
         + Hc*mut*(jet.c_p + mut_p))

    tau_f=jet.c*t + 0.5*jet.c_p*t*t
    eta_f=tau_f - 0.5*q*r*r
    eta_ft=c - 0.5*q_p*r*r
    eta_fr=-q*r
    r_f=(1.0+mut)*r
    r_ft=mut_p*r
    r_fr=1.0+mut

    fjet=jet.f_native
    b=fjet.b + fjet.b_f_p*eta_f + 0.5*fjet.b_f_pp*eta_f*eta_f
    if b <= 0.0:
        raise ValueError("f-native scale factor left the positive Taylor chart")

    Jg=np.eye(2,dtype=float)
    Jf=np.array([[eta_ft,eta_fr],[r_ft,r_fr]],dtype=float)
    gn=a*a*np.diag([-1.0,1.0])
    fn=b*b*np.diag([-1.0,1.0])
    gc=gn.copy()
    fc=Jf.T@fn@Jf
    gang=a*a*r*r
    fang=b*b*r_f*r_f
    return NonhomotheticBackgroundMap(
        t=t,r=r,a=float(a),xi=float(xi),c=float(c),mu=float(mut),q=float(q),
        eta_f=float(eta_f),r_f=float(r_f),Jg=Jg,Jf=Jf,
        g_common=gc,f_common=fc,g_angular=float(gang),f_angular=float(fang),
        b_native=float(b),
    )

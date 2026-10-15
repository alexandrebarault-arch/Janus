"""Local non-homothetic FLRW background jets for compact-action audits."""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class FNativeScaleJet:
    b: float
    b_eta_p: float
    b_eta_pp: float
    b_f_p: float
    b_f_pp: float


def f_native_scale_jet(*, a, ap, app, xi, xi_p, xi_pp, c, c_p):
    vals=(a,ap,app,xi,xi_p,xi_pp,c,c_p)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("background-jet inputs must be finite")
    if a<=0.0 or xi<=0.0 or c<=0.0:
        raise ValueError("a, xi and c must be positive")
    b=a*xi
    bp=ap*xi+a*xi_p
    bpp=app*xi+2.0*ap*xi_p+a*xi_pp
    return FNativeScaleJet(
        b=float(b), b_eta_p=float(bp), b_eta_pp=float(bpp),
        b_f_p=float(bp/c),
        b_f_pp=float(bpp/(c*c)-bp*c_p/(c*c*c)),
    )


@dataclass(frozen=True)
class NonhomotheticBackgroundJet:
    a: float
    a_p: float
    a_pp: float
    Hc: float
    Hc_p: float
    xi: float
    xi_p: float
    xi_pp: float
    c: float
    c_p: float
    f_native: FNativeScaleJet


def from_log_derivatives(*, a, Hc, Hc_N, xi, xi_N, xi_NN, c, c_N):
    vals=(a,Hc,Hc_N,xi,xi_N,xi_NN,c,c_N)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("log-derivative background inputs must be finite")
    if a<=0.0 or xi<=0.0 or c<=0.0:
        raise ValueError("a, xi and c must be positive")
    Hcp=Hc*Hc_N
    ap=a*Hc
    app=a*(Hc*Hc+Hcp)
    xip=Hc*xi_N
    xipp=Hcp*xi_N+Hc*Hc*xi_NN
    cp=Hc*c_N
    fjet=f_native_scale_jet(
        a=a,ap=ap,app=app,xi=xi,xi_p=xip,xi_pp=xipp,c=c,c_p=cp,
    )
    return NonhomotheticBackgroundJet(
        a=float(a),a_p=float(ap),a_pp=float(app),Hc=float(Hc),Hc_p=float(Hcp),
        xi=float(xi),xi_p=float(xip),xi_pp=float(xipp),c=float(c),c_p=float(cp),
        f_native=fjet,
    )

"""Local Taylor jets for the two native conformal FLRW charts."""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class ConformalTaylorJet:
    a0: float
    ap0: float
    app0: float


@dataclass(frozen=True)
class TwoMetricConformalTaylorJets:
    g: ConformalTaylorJet
    f: ConformalTaylorJet
    eta_f_prime: float


def native_conformal_taylor_jets(*, a: float, xi: float, c: float,
                                 H: float, H_prime: float) -> TwoMetricConformalTaylorJets:
    vals=(a,xi,c,H,H_prime)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all background inputs must be finite")
    if a <= 0.0 or xi <= 0.0 or c <= 0.0:
        raise ValueError("a, xi and c must be positive")

    a=float(a); xi=float(xi); c=float(c); H=float(H); Hp=float(H_prime)
    b=a*xi
    g=ConformalTaylorJet(
        a0=a,
        ap0=a*H,
        app0=a*(H*H+Hp),
    )
    # eta_f is the natural f conformal time, d eta_f / d eta = c.
    # On the dynamical FLRW branch b'/b = c H in g conformal time,
    # hence db/d eta_f = b H and d2b/deta_f2 = b(H^2 + H'/c).
    f=ConformalTaylorJet(
        a0=b,
        ap0=b*H,
        app0=b*(H*H+Hp/c),
    )
    return TwoMetricConformalTaylorJets(g=g,f=f,eta_f_prime=c)

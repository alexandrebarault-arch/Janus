"""Matter-only W2 blocks for the spherical bimetric lapse ratio.

The g-matter expressions are isolated from nubirel/bim-solver at
8852e8e9921edeeedf1a447d3bf27b82ec24433c. The f-matter expressions are
the exact sector dual, represented in the upstream variables R=Bf/Bg.

This is a derivation/regression aid, not an executable replacement for the
upstream C++ lapse machinery.
"""
from __future__ import annotations
import math


def _polys(R, b1, b2, b3):
    P = b1 + 2.0*b2*R + b3*R*R
    Qg = b2 + b3*R
    Qf = b1 + b2*R
    C = b1 - b3*R*R
    return P, Qg, Qf, C


def g_matter_blocks(*, Ag, Af, R, p, b1, b2, b3, kg, kf,
                    Dg, Sg, Tg, vg, Df, Sf, Tf, vf):
    """Return (Delta Wg2, Delta Wf2) due only to g-sector dust."""
    lam = math.sqrt(1.0 + p*p)
    P, Qg, _, C = _polys(R,b1,b2,b3)
    E = Dg - Sg*vg + Tg
    H = Dg + Sg*vg + Tg
    common = kg*Ag*Ag*Af*Af*(1.0+p*p)*R*R*P
    dWg = -0.5*common * (-lam*C*E + 2.0*Af*Qg*(Sg*vg + p*p*H))
    dWf = common*Qg*(Dg+Tg)
    return dWg, dWf


def f_matter_blocks(*, Ag, Af, R, p, b1, b2, b3, kg, kf,
                    Dg, Sg, Tg, vg, Df, Sf, Tf, vf):
    """Return (Delta Wg2, Delta Wf2) due only to f-sector dust.

    Derived by applying the published exact sector duality before eliminating
    Bf in favor of R=Bf/Bg. No Appendix-D hand transcription is used.
    """
    if R == 0:
        raise ZeroDivisionError("R=Bf/Bg must be nonzero")
    lam = math.sqrt(1.0 + p*p)
    P, _, Qf, C = _polys(R,b1,b2,b3)
    E = Df - Sf*vf + Tf
    H = Df + Sf*vf + Tf
    base = kf*Ag*Ag*Af*Af*(1.0+p*p)*P
    dWg = -base*Qf*(Df+Tf)/(R**5)
    dWf = base/(2.0*R**6) * (lam*C*E + 2.0*Ag*R*Qf*(Sf*vf + p*p*H))
    return dWg, dWf


def dual_state(s):
    """Exchange sectors in the reduced upstream variable representation."""
    return dict(
        Ag=s['Af'], Af=s['Ag'], R=1.0/s['R'], p=-s['p'],
        b1=s['b3'], b2=s['b2'], b3=s['b1'],
        kg=s['kf'], kf=s['kg'],
        Dg=s['Df'], Sg=s['Sf'], Tg=s['Tf'], vg=s['vf'],
        Df=s['Dg'], Sf=s['Sg'], Tf=s['Tg'], vf=s['vg'],
    )

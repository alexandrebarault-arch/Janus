"""Covariant divergence of a spherically symmetric mixed tensor."""
from __future__ import annotations
import math
import numpy as np


def mixed_tensor_divergence(*, g_radial, dg_radial, g_angular, dg_angular,
                            V_radial, dV_radial, V_angular):
    """Return radial-chart components of ``nabla_mu V^mu{}_nu``.

    Coordinates 0,1 are the time/radial chart. ``dg_radial[c,a,b]`` and
    ``dV_radial[c,a,b]`` denote partial derivatives with respect to coordinate
    ``c``. The two angular mixed components are both ``V_angular``.
    """
    g=np.asarray(g_radial,dtype=float)
    dg=np.asarray(dg_radial,dtype=float)
    V=np.asarray(V_radial,dtype=float)
    dV=np.asarray(dV_radial,dtype=float)
    dq=np.asarray(dg_angular,dtype=float)
    if g.shape!=(2,2) or dg.shape!=(2,2,2) or V.shape!=(2,2) or dV.shape!=(2,2,2) or dq.shape!=(2,):
        raise ValueError("invalid spherical tensor shapes")
    vals=[g_angular,V_angular]
    if not (np.all(np.isfinite(g)) and np.all(np.isfinite(dg)) and np.all(np.isfinite(V)) and np.all(np.isfinite(dV)) and np.all(np.isfinite(dq)) and all(math.isfinite(float(x)) for x in vals)):
        raise ValueError("all spherical tensor inputs must be finite")
    if float(g_angular)<=0.0:
        raise ValueError("g_angular must be positive")
    gi=np.linalg.inv(g)
    Gamma=np.zeros((2,2,2),dtype=float)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                Gamma[a,b,c]=0.5*sum(
                    gi[a,d]*(dg[b,d,c]+dg[c,d,b]-dg[d,b,c])
                    for d in range(2)
                )
    gamma_ang=0.5*dq/float(g_angular)
    out=np.zeros(2,dtype=float)
    for nu in range(2):
        val=sum(dV[mu,mu,nu] for mu in range(2))
        for lam in range(2):
            trace=sum(Gamma[mu,mu,lam] for mu in range(2)) + 2.0*gamma_ang[lam]
            val += trace*V[lam,nu]
        val -= sum(
            Gamma[lam,mu,nu]*V[mu,lam]
            for mu in range(2) for lam in range(2)
        )
        val -= 2.0*gamma_ang[nu]*float(V_angular)
        out[nu]=val
    return out

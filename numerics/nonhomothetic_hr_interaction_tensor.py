"""Full mixed Hassan-Rosen interaction tensors from a square-root matrix."""
from __future__ import annotations
import math
import numpy as np


def _elementary_symmetric(S: np.ndarray) -> np.ndarray:
    tr1=float(np.trace(S))
    S2=S@S; tr2=float(np.trace(S2))
    S3=S2@S; tr3=float(np.trace(S3))
    e1=tr1
    e2=0.5*(tr1*tr1-tr2)
    e3=(tr1**3-3.0*tr1*tr2+2.0*tr3)/6.0
    e4=float(np.linalg.det(S))
    return np.array([1.0,e1,e2,e3,e4],dtype=float)


def _Y_matrices(S: np.ndarray) -> tuple[np.ndarray,...]:
    e=_elementary_symmetric(S)
    I=np.eye(4)
    powers=[I]
    for _ in range(4):
        powers.append(powers[-1]@S)
    out=[]
    for n in range(4):
        Y=np.zeros((4,4),dtype=float)
        for r in range(n+1):
            Y += ((-1.0)**r)*e[r]*powers[n-r]
        out.append(Y)
    return tuple(out)


def _one_side(S: np.ndarray, beta4: tuple[float,...]) -> np.ndarray:
    Y=_Y_matrices(S)
    V=np.zeros((4,4),dtype=float)
    for n in range(4):
        V += ((-1.0)**n)*beta4[n]*Y[n]
    return V


def interaction_mixed_tensors(S, betas):
    """Return ``(V_g^mu_nu, V_f^mu_nu)`` for standard beta conventions.

    ``S`` is the principal square root ``sqrt(g^{-1}f)`` represented as a
    mixed-index 4x4 matrix in any common coordinate basis. The result is
    similarity-covariant. Overall Einstein-equation signs and the common
    ``m^2``/Planck prefactors are intentionally not included.
    """
    S=np.asarray(S,dtype=float)
    beta=tuple(float(x) for x in betas)
    if S.shape!=(4,4) or not np.all(np.isfinite(S)):
        raise ValueError("S must be a finite 4x4 matrix")
    if len(beta)!=5 or not all(math.isfinite(x) for x in beta):
        raise ValueError("betas must contain five finite values")
    det=float(np.linalg.det(S))
    if abs(det)<=1e-14*max(1.0,float(np.linalg.norm(S,ord=np.inf))**4):
        raise np.linalg.LinAlgError("S is singular")
    vg=_one_side(S,beta[:4])
    Sinv=np.linalg.inv(S)
    rev=(beta[4],beta[3],beta[2],beta[1])
    vf=_one_side(Sinv,rev)
    return vg,vf

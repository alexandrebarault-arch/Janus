"""Time-dependent quadratic reductions used by the raw De Felice route.

For L = 1/2 qdot^T K qdot + qdot^T C q + 1/2 q^T Q q, a coordinate
whose K row/column vanishes can still appear through qdot*C*q. If the
background is time-dependent it must be integrated by parts before that
coordinate is eliminated.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class ReducedQuadraticMatrices:
    K: np.ndarray
    C: np.ndarray
    Q: np.ndarray


@dataclass(frozen=True)
class EulerLagrangeMatrices:
    K: np.ndarray
    D: np.ndarray
    E: np.ndarray


@dataclass(frozen=True)
class DeFeliceY2Map:
    u_f: float
    u_f_dot: float


def _square_matrix(x, name):
    a=np.asarray(x,dtype=float)
    if a.ndim!=2 or a.shape[0]!=a.shape[1]:
        raise ValueError(f"{name} must be square")
    if not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be finite")
    return a


def eliminate_time_dependent_null_coordinate(K,C,Q,Cdot,*,null_index=-1,tol=1e-10):
    K=_square_matrix(K,"K"); C=_square_matrix(C,"C"); Q=_square_matrix(Q,"Q"); Cdot=_square_matrix(Cdot,"Cdot")
    if not (K.shape==C.shape==Q.shape==Cdot.shape):
        raise ValueError("K, C, Q and Cdot must have the same shape")
    n=K.shape[0]; z=int(null_index)%n
    keep=[i for i in range(n) if i!=z]
    scale=max(1.0,float(np.max(np.abs(K))))
    if np.max(np.abs(K[z,:]))>tol*scale or np.max(np.abs(K[:,z]))>tol*scale:
        raise ValueError("selected coordinate is not kinetic-null")
    Kyy=K[np.ix_(keep,keep)]
    Cyy=C[np.ix_(keep,keep)]
    Qyy=Q[np.ix_(keep,keep)]
    d=C[keep,z]-C[z,keep]
    r=Q[keep,z]-Cdot[z,keep]
    qzz=float(Q[z,z]-Cdot[z,z])
    qscale=max(1.0,abs(float(Q[z,z])),abs(float(Cdot[z,z])))
    if abs(qzz)<=tol*qscale:
        raise np.linalg.LinAlgError("time-dependent null coordinate remains non-algebraic")
    return ReducedQuadraticMatrices(
        K=Kyy-np.outer(d,d)/qzz,
        C=Cyy-np.outer(d,r)/qzz,
        Q=Qyy-np.outer(r,r)/qzz,
    )


def euler_lagrange_matrices(K,C,Q,Kdot,Cdot):
    K=_square_matrix(K,"K"); C=_square_matrix(C,"C"); Q=_square_matrix(Q,"Q"); Kdot=_square_matrix(Kdot,"Kdot"); Cdot=_square_matrix(Cdot,"Cdot")
    if not (K.shape==C.shape==Q.shape==Kdot.shape==Cdot.shape):
        raise ValueError("all matrices must have the same shape")
    return EulerLagrangeMatrices(K=K,D=Kdot+C-C.T,E=Cdot-Q)


def de_felice_y2hat_map(*,k,R,Rdot,Y2hat,S,Sigma,Y2hat_dot,S_dot,Sigma_dot):
    vals=(k,R,Rdot,Y2hat,S,Sigma,Y2hat_dot,S_dot,Sigma_dot)
    if not np.all(np.isfinite(vals)) or k<0:
        raise ValueError("map inputs must be finite and k non-negative")
    combo=Sigma+k*k*S/6.0
    combo_dot=Sigma_dot+k*k*S_dot/6.0
    return DeFeliceY2Map(
        u_f=float(Y2hat+R*combo),
        u_f_dot=float(Y2hat_dot+R*combo_dot+Rdot*combo),
    )

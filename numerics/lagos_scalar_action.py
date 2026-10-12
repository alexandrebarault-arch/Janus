"""Scalar quadratic action for Hassan-Rosen massive bigravity.

Transcribes the scalar metric terms of Lagos & Ferreira, arXiv:1610.00553,
Eqs. (3.6)-(3.8), specialized to massive bigravity: constant Planck masses
and alpha_L=0. Matter perturbation actions are intentionally not included yet.

All returned Lagrangians use the common normalization M1^2 a^3.
``ScalarBackground.k2`` is the comoving Fourier k^2. Lagos Appendix A defines
spatial index contractions with the background metric of the sector on which
the derivative acts, so

    partial_1^2 -> -k^2/a^2,
    partial_2^2 -> -k^2/b^2.

For the cross-shift term in Eq. (3.8), ``partial_i B2 partial^i B1``, the raised
index belongs to the derivative acting on B1 and therefore uses metric 1.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_action_bridge import lagos_bigravity_parameters

INTERACTION_STATE_ORDER=("Psi1","Psi2","E1","E2","Phi1","Phi2","B1","B2")
RATE_ORDER=("Psi1_dot","Psi2_dot","E1_dot","E2_dot")
AUXILIARY_ORDER=("Phi1","Phi2","B1","B2")
DYNAMIC_ORDER=("Psi1","Psi2","E1","E2")

@dataclass(frozen=True)
class AuxiliarySolution:
    auxiliaries: np.ndarray
    auxiliary_hessian_rank: int
    stationarity_residual: float
    reduced_lagrangian: float


def _state(x):
    arr=np.asarray(x,dtype=float)
    if arr.shape!=(8,): raise ValueError("scalar state must have length 8")
    return arr

def _rates(v):
    arr=np.asarray(v,dtype=float)
    if arr.shape!=(4,): raise ValueError("scalar rate vector must have length 4")
    return arr

def _sector_laplacians(bg,p):
    a=bg.a; b=a*p.r
    if a==0.0 or b==0.0: raise ValueError("sector scale factors must be non-zero")
    return bg.k2/(a*a), bg.k2/(b*b)


def interaction_lagrangian_raw(bg: ScalarBackground,state)->float:
    Psi1,Psi2,E1,E2,Phi1,Phi2,B1,B2=_state(state)
    p=lagos_bigravity_parameters(bg)
    r,Nbar,Z,Zt=p.r,p.Nbar,p.Z,p.Z_tilde
    a,b=bg.a,bg.a*p.r
    lap1,lap2=_sector_laplacians(bg,p)
    k2=bg.k2
    nu2=1.0/bg.kappa
    H=bg.H/bg.a; Hb=bg.c*H
    if r==0.0 or Nbar==0.0 or Nbar+r==0.0: raise ValueError("singular Lagos background")
    if abs(H-Hb)<=1e-13*max(1.0,abs(H),abs(Hb)):
        ratio=0.0 if H==0.0 else -r/H
    else:
        ratio=(Nbar-r)/(H-Hb)
    l1=(
        r*Z/(2.0*(Nbar+r))*lap1*B1*B1
        +2.0*r*Zt*Psi1*(1.5*Psi1+k2*E1)
        +ratio*H*Z*Phi1*(3.0*Psi1+k2*E1)
    )
    factor2=Nbar*r**3/nu2
    shift2=nu2*Nbar*Z/(2.0*r**3*(Nbar+r))*lap2*B2*B2
    zt2=2.0*nu2*Nbar*r*r*Zt*Psi2*(1.5*Psi2+k2*E2)
    if abs(H-Hb)>1e-13*max(1.0,abs(H),abs(Hb)):
        lapse2=Hb*nu2*Z*(Nbar-r)/(Nbar*r**3*(H-Hb))*Phi2*(3.0*Psi2+k2*E2)
    elif H==0.0:
        lapse2=0.0
    else:
        lapse2=-(Hb*nu2*Z)/(Nbar*r**2*H)*Phi2*(3.0*Psi2+k2*E2)
    l2=factor2*(shift2+zt2+lapse2)
    l12=(
        -2.0*r*Zt*(3.0*Psi2*Psi1+k2*Psi2*E1+k2*Psi1*E2)
        -Z*Nbar/(Nbar+r)*lap1*B2*B1
        -Z*ratio*(H*Phi1*(3.0*Psi2+k2*E2)+Hb*Phi2*(3.0*Psi1+k2*E1))
    )
    return float(l1+l2+l12)


def interaction_lagrangian_healthy(bg: ScalarBackground,state)->float:
    Psi1,Psi2,E1,E2,Phi1,Phi2,B1,B2=_state(state)
    p=lagos_bigravity_parameters(bg)
    r,Nbar,Z,Zt=p.r,p.Nbar,p.Z,p.Z_tilde
    c=bg.c; k2=bg.k2
    lap1,lap2=_sector_laplacians(bg,p)
    return float(
        r*Z/(2.0*(Nbar+r))*lap1*B1*B1
        +Nbar*Nbar*Z/(2.0*(Nbar+r))*lap2*B2*B2
        -Z*Nbar/(Nbar+r)*lap1*B1*B2
        +2.0*r*Zt*Psi1*(1.5*Psi1+k2*E1)
        +2.0*Nbar*Nbar*r**5*Zt*Psi2*(1.5*Psi2+k2*E2)
        -2.0*r*Zt*(3.0*Psi2*Psi1+k2*Psi2*E1+k2*Psi1*E2)
        +r*Z*Phi1*(3.0*(Psi2-Psi1)+k2*(E2-E1))
        +c*r*Z*Phi2*(3.0*(Psi1-Psi2)+k2*(E1-E2))
    )


def einstein_hilbert_lagrangian(bg: ScalarBackground,state,rates)->float:
    """Pure EH scalar self-actions, common-normalized by M1^2 a^3."""
    Psi1,Psi2,E1,E2,Phi1,Phi2,B1,B2=_state(state)
    P1d,P2d,E1d,E2d=_rates(rates)
    p=lagos_bigravity_parameters(bg); r,Nbar=p.r,p.Nbar
    a,b=bg.a,bg.a*r; H=bg.H/bg.a; Hb=bg.H_omega/bg.a
    if Nbar==0.0: raise ValueError("Nbar must be non-zero")
    lap1,lap2=_sector_laplacians(bg,p)
    l1=(
        -3.0*P1d*P1d-6.0*H*P1d*Phi1
        -2.0*a*a*lap1*E1d*(P1d+H*Phi1)
        +2.0*lap1*P1d*B1+lap1*Psi1*Psi1-2.0*lap1*Phi1*Psi1
        +2.0*H*lap1*Phi1*B1-3.0*H*H*Phi1*Phi1
    )
    l2_inner=(
        -3.0*P2d*P2d/(Nbar*Nbar)-6.0*Hb*P2d*Phi2/(Nbar*Nbar)
        -2.0*b*b*lap2*E2d*(P2d+Hb*Phi2)/(Nbar*Nbar)
        +2.0*lap2*P2d*B2/Nbar+lap2*Psi2*Psi2-2.0*lap2*Phi2*Psi2
        +2.0*Hb*lap2*Phi2*B2/Nbar-3.0*Hb*Hb*Phi2*Phi2/(Nbar*Nbar)
    )
    return float(l1+Nbar*r**3*bg.kappa*l2_inner)


def pure_metric_lagrangian_healthy(bg,state,rates)->float:
    return float(einstein_hilbert_lagrangian(bg,state,rates)+interaction_lagrangian_healthy(bg,state))


def velocity_hessian(bg):
    zero_s=np.zeros(8); n=len(RATE_ORDER); Hmat=np.empty((n,n)); basis=np.eye(n)
    Lbasis=[pure_metric_lagrangian_healthy(bg,zero_s,e) for e in basis]
    for i in range(n):
        Hmat[i,i]=2.0*Lbasis[i]
        for j in range(i+1,n):
            mixed=pure_metric_lagrangian_healthy(bg,zero_s,basis[i]+basis[j]); hij=mixed-Lbasis[i]-Lbasis[j]
            Hmat[i,j]=Hmat[j,i]=hij
    return Hmat


def _state_from_dynamic_aux(dynamic,auxiliaries):
    q=np.asarray(dynamic,float); aux=np.asarray(auxiliaries,float)
    if q.shape!=(4,) or aux.shape!=(4,): raise ValueError("dynamic and auxiliary vectors must have length 4")
    return np.array([q[0],q[1],q[2],q[3],aux[0],aux[1],aux[2],aux[3]],float)


def _auxiliary_quadratic_form(bg,dynamic,rates):
    q=np.asarray(dynamic,float); v=_rates(rates); n=len(AUXILIARY_ORDER); z=np.zeros(n)
    base=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,z),v); eye=np.eye(n); grad=np.empty(n); A=np.empty((n,n))
    for i in range(n):
        lp=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,eye[i]),v); lm=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,-eye[i]),v)
        grad[i]=0.5*(lp-lm); A[i,i]=lp+lm-2.0*base
        for j in range(i+1,n):
            lpp=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,eye[i]+eye[j]),v); lpm=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,eye[i]-eye[j]),v); lmp=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,-eye[i]+eye[j]),v); lmm=pure_metric_lagrangian_healthy(bg,_state_from_dynamic_aux(q,-eye[i]-eye[j]),v)
            A[i,j]=A[j,i]=0.25*(lpp-lpm-lmp+lmm)
    return A,grad,float(base)


def eliminate_auxiliaries(bg,dynamic,rates):
    A,grad,base=_auxiliary_quadratic_form(bg,dynamic,rates); rank=int(np.linalg.matrix_rank(A))
    if rank!=len(AUXILIARY_ORDER): raise np.linalg.LinAlgError(f"auxiliary Hessian rank {rank}, expected {len(AUXILIARY_ORDER)}")
    aux=np.linalg.solve(A,-grad); residual=float(np.linalg.norm(A@aux+grad,ord=np.inf)); reduced=float(base+grad@aux+0.5*aux@A@aux)
    return AuxiliarySolution(np.asarray(aux,float),rank,residual,reduced)


def reduced_pure_metric_lagrangian(bg,dynamic,rates): return eliminate_auxiliaries(bg,dynamic,rates).reduced_lagrangian

def reduced_velocity_hessian(bg):
    q=np.zeros(4); n=len(RATE_ORDER); z=np.zeros(n); base=reduced_pure_metric_lagrangian(bg,q,z); eye=np.eye(n); Hmat=np.empty((n,n))
    for i in range(n):
        lp=reduced_pure_metric_lagrangian(bg,q,eye[i]); lm=reduced_pure_metric_lagrangian(bg,q,-eye[i]); Hmat[i,i]=lp+lm-2.0*base
        for j in range(i+1,n):
            lpp=reduced_pure_metric_lagrangian(bg,q,eye[i]+eye[j]); lpm=reduced_pure_metric_lagrangian(bg,q,eye[i]-eye[j]); lmp=reduced_pure_metric_lagrangian(bg,q,-eye[i]+eye[j]); lmm=reduced_pure_metric_lagrangian(bg,q,-eye[i]-eye[j]); Hmat[i,j]=Hmat[j,i]=0.25*(lpp-lpm-lmp+lmm)
    return Hmat

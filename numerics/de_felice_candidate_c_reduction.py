"""Candidate-C benchmark for the raw time-dependent De Felice scalar reduction.

This is an oracle/diagnostic module, not phenomenology. It keeps the raw
source action separate from the physical-variable reduction and uses finite
differences only for background-time derivatives of already quadratic
coefficient matrices.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.de_felice_raw_scalar_action import RawBimetricBackground, raw_two_matter_scalar_density_g_flat
from numerics.time_dependent_quadratic_reduction import (
    de_felice_y2hat_map, eliminate_time_dependent_null_coordinate,
    euler_lagrange_matrices,
)


@dataclass(frozen=True)
class RawCandidateBackground:
    a: float; xi: float; ctilde: float; kappa: float; H: float; Hf: float
    Hdot: float; Hfdot_over_n: float; rho_g: float; pressure_g: float
    rho_f: float; pressure_f: float; mu_g: float; mu_f: float
    zeta: float; gamma_m: float; R: float; Rdot: float


@dataclass(frozen=True)
class ThreeModeSpeeds:
    k_values: np.ndarray
    speeds: np.ndarray
    extrapolated: np.ndarray


def candidate_c_raw_background(a: float) -> RawCandidateBackground:
    pt=candidate_c_background_point(float(a),k_hmpc=0.0)
    m=pt.metric
    H=m.H/m.a
    xi=m.xi; c=m.c; kappa=m.kappa; m2=m.m2
    J=m.f2/xi
    Gamma=m.f1
    Hf=H/xi
    rho_g=pt.rho_g_m+pt.rho_g_r
    pressure_g=pt.rho_g_r/3.0
    rho_f=pt.rho_f_m; pressure_f=0.0
    zeta=m2*xi*J
    gamma_m=m2*Gamma
    Hdot=0.5*(zeta*(c-1.0)-(rho_g+pressure_g))
    Hfdot_over_n=-0.5*(m2*J*(c-1.0)/(kappa*xi**3*c)+(rho_f+pressure_f)/kappa)
    mu_g=3.0*H**2-rho_g
    mu_f=3.0*kappa*Hf**2-rho_f
    c_N=pt.y_NN/xi-(pt.y_N/xi)**2
    R=1.0/(c*H)
    Rdot=-R*(H*c_N/c+Hdot/H)
    return RawCandidateBackground(float(a),xi,c,kappa,H,Hf,Hdot,Hfdot_over_n,rho_g,pressure_g,rho_f,pressure_f,mu_g,mu_f,zeta,gamma_m,R,Rdot)


def _raw_bg(b):
    return RawBimetricBackground(N=1.0,a=b.a,xi=b.xi,ctilde=b.ctilde,kappa=b.kappa,H=b.H,Hf=b.Hf,Hdot_over_N=b.Hdot,Hfdot_over_n=b.Hfdot_over_n,mu_g=b.mu_g,mu_f=b.mu_f,zeta=b.zeta,gamma_m=b.gamma_m,Mgsq=1.0)


def _quadratic_hessian(fun, scales):
    """Exact-quadratic coefficient extraction in one joint variable space."""
    scales=np.asarray(scales,float); n=len(scales); out=np.zeros((n,n)); z=np.zeros(n)
    f0=fun(z); fi=[]
    for i in range(n):
        ei=np.zeros(n); ei[i]=scales[i]
        vi=fun(ei); fi.append(vi)
        out[i,i]=2.0*(vi-f0)/scales[i]**2
        for j in range(i):
            ej=np.zeros(n); ej[j]=scales[j]
            out[i,j]=out[j,i]=(fun(ei+ej)-vi-fi[j]+f0)/(scales[i]*scales[j])
    return out


def _primary_matrices(a,k,cs2_g,cs2_f):
    """Return primary K,C,Q after one Schur elimination of lapse/shift.

    Building the full joint Hessian first avoids the former nested finite
    differences of an already numerically reduced Lagrangian.
    """
    b=candidate_c_raw_background(a)
    scales=np.array([
        1.0,b.a/max(k,1.0),1.0,b.a*b.xi/max(k,1.0),
        1.0,1.0,1.0/max(k*k,1.0),1.0,
        1.0,1.0,1.0/max(k*k,1.0),1.0,
    ])
    def lag(x):
        Phi,B,varphi,bshift=x[:4]
        ug,Y2,S,Sigma=x[4:8]
        ugd,Y2d,Sd,Sigmad=x[8:12]
        mapped=de_felice_y2hat_map(
            k=k,R=b.R,Rdot=b.Rdot,Y2hat=Y2,S=S,Sigma=Sigma,
            Y2hat_dot=Y2d,S_dot=Sd,Sigma_dot=Sigmad,
        )
        density=raw_two_matter_scalar_density_g_flat(
            _raw_bg(b),k=k,Phi=Phi,B=B,varphi=varphi,b=bshift,
            Sigma=Sigma,S=S,Sigma_dot=Sigmad,S_dot=Sd,
            rho_g=b.rho_g,pressure_g=b.pressure_g,cs2_g=cs2_g,
            u_g=ug,u_g_dot=ugd,rho_f=b.rho_f,pressure_f=b.pressure_f,
            cs2_f=cs2_f,u_f=mapped.u_f,u_f_dot=mapped.u_f_dot,
        )
        return b.a**3*density
    H=_quadratic_hessian(lag,scales)
    A=H[:4,:4]
    X=H[:4,4:]
    D=H[4:,4:]
    reduced=D-X.T@np.linalg.solve(A,X)
    return b,reduced[4:,4:],reduced[4:,:4],reduced[:4,:4]


def _primary_derivatives(a,k,cs2_g,cs2_f,diff_step):
    """Five-point derivatives in x=ln(a) of primary coefficient matrices."""
    h=float(diff_step)
    vals=[_primary_matrices(a*math.exp(j*h),k,cs2_g,cs2_f) for j in (-2,-1,0,1,2)]
    b,K,C,Q=vals[2]
    def d1(idx):
        fm2,fm1,_,fp1,fp2=[v[idx] for v in vals]
        return (fm2-8.0*fm1+8.0*fp1-fp2)/(12.0*h)
    def d2(idx):
        fm2,fm1,f0,fp1,fp2=[v[idx] for v in vals]
        return (-fp2+16.0*fp1-30.0*f0+16.0*fm1-fm2)/(12.0*h*h)
    Kx=d1(1); Cx=d1(2); Qx=d1(3); Cxx=d2(2)
    Kdot=b.H*Kx
    Cdot=b.H*Cx
    Qdot=b.H*Qx
    Cddot=b.Hdot*Cx+b.H*b.H*Cxx
    return b,K,C,Q,Kdot,Cdot,Qdot,Cddot


def _physical_with_derivatives(a,k,cs2_g,cs2_f,diff_step):
    b,K,C,Q,Kdot,Cdot,Qdot,Cddot=_primary_derivatives(a,k,cs2_g,cs2_f,diff_step)
    keep=[0,1,2]; z=3
    d=C[keep,z]-C[z,keep]
    r=Q[keep,z]-Cdot[z,keep]
    q=float(Q[z,z]-Cdot[z,z])
    if abs(q)<=1e-14*max(1.0,abs(float(Q[z,z])),abs(float(Cdot[z,z]))):
        raise np.linalg.LinAlgError("time-dependent null coordinate remains non-algebraic")
    Kred=K[np.ix_(keep,keep)]-np.outer(d,d)/q
    Cred=C[np.ix_(keep,keep)]-np.outer(d,r)/q
    Qred=Q[np.ix_(keep,keep)]-np.outer(r,r)/q

    dd=Cdot[keep,z]-Cdot[z,keep]
    rd=Qdot[keep,z]-Cddot[z,keep]
    qdot=float(Qdot[z,z]-Cddot[z,z])
    Kred_dot=(
        Kdot[np.ix_(keep,keep)]
        -(np.outer(dd,d)+np.outer(d,dd))/q
        +np.outer(d,d)*qdot/q**2
    )
    Cred_dot=(
        Cdot[np.ix_(keep,keep)]
        -(np.outer(dd,r)+np.outer(d,rd))/q
        +np.outer(d,r)*qdot/q**2
    )
    red=eliminate_time_dependent_null_coordinate(K,C,Q,Cdot,null_index=3,tol=1e-8)
    return b,red,Kred_dot,Cred_dot


def physical_matrices(a,k,*,cs2_g=0.4,cs2_f=0.3,diff_step=5e-4):
    b,red,_,_=_physical_with_derivatives(a,k,cs2_g,cs2_f,diff_step)
    return b,red


def mode_speeds(a,k,*,cs2_g=0.4,cs2_f=0.3,diff_step=5e-4):
    b,red,Kdot,Cdot=_physical_with_derivatives(a,k,cs2_g,cs2_f,diff_step)
    eom=euler_lagrange_matrices(red.K,red.C,red.Q,Kdot,Cdot)
    # Rescale the geometric S direction before the eigensolve. This is a
    # similarity-equivalent coordinate conditioning, not a physics change.
    T=np.diag([1.0,1.0,1.0/(k*k)])
    K=T.T@eom.K@T
    D=T.T@eom.D@T
    E=T.T@eom.E@T
    A=np.block([[np.zeros((3,3)),np.eye(3)],[-np.linalg.solve(K,E),-np.linalg.solve(K,D)]])
    roots=np.linalg.eigvals(A)
    speeds=sorted(float(r.imag*a/k) for r in roots if r.imag>1e-6)
    if len(speeds)!=3:
        raise RuntimeError(f"expected 3 oscillatory scalar pairs, got {len(speeds)}")
    return np.asarray(speeds)


def candidate_c_three_mode_extrapolation(a=0.5,*,k_values=(100.0,150.0,250.0),cs2_g=0.4,cs2_f=0.3,diff_step=5e-4):
    ks=np.asarray(k_values,float)
    rows=np.vstack([mode_speeds(a,float(k),cs2_g=cs2_g,cs2_f=cs2_f,diff_step=diff_step) for k in ks])
    x=1.0/ks**2
    intercept=np.array([np.polyfit(x,rows[:,j],1)[1] for j in range(3)])
    return ThreeModeSpeeds(ks,rows,intercept)

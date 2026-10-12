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


def _hessian(fun, scales):
    scales=np.asarray(scales,float); n=len(scales); out=np.zeros((n,n)); z=np.zeros(n); f0=fun(z)
    for i in range(n):
        ei=np.zeros(n); ei[i]=scales[i]
        fp=fun(ei); fm=fun(-ei)
        out[i,i]=(fp+fm-2*f0)/scales[i]**2
        for j in range(i):
            ej=np.zeros(n); ej[j]=scales[j]
            out[i,j]=out[j,i]=(fun(ei+ej)-fun(ei-ej)-fun(-ei+ej)+fun(-ei-ej))/(4*scales[i]*scales[j])
    return out


def _eliminate_primary(b,k,p,v,cs2_g,cs2_f):
    # p=(u_g,Y2hat,S,Sigma), v in the same order.
    ug,Y2,S,Sigma=p; ugd,Y2d,Sd,Sigmad=v
    mapped=de_felice_y2hat_map(k=k,R=b.R,Rdot=b.Rdot,Y2hat=Y2,S=S,Sigma=Sigma,Y2hat_dot=Y2d,S_dot=Sd,Sigma_dot=Sigmad)
    def Laux(aux):
        Phi,B,varphi,bshift=aux
        d=raw_two_matter_scalar_density_g_flat(_raw_bg(b),k=k,Phi=Phi,B=B,varphi=varphi,b=bshift,Sigma=Sigma,S=S,Sigma_dot=Sigmad,S_dot=Sd,rho_g=b.rho_g,pressure_g=b.pressure_g,cs2_g=cs2_g,u_g=ug,u_g_dot=ugd,rho_f=b.rho_f,pressure_f=b.pressure_f,cs2_f=cs2_f,u_f=mapped.u_f,u_f_dot=mapped.u_f_dot)
        return b.a**3*d
    s=np.array([1.0,b.a/max(k,1.0),1.0,b.a*b.xi/max(k,1.0)])
    A=_hessian(Laux,s)
    z=np.zeros(4); f0=Laux(z); g=np.zeros(4)
    for i in range(4):
        e=np.zeros(4); e[i]=s[i]
        g[i]=(Laux(e)-Laux(-e))/(2*s[i])
    return float(f0-0.5*g@np.linalg.solve(A,g))


def _primary_matrices(a,k,cs2_g,cs2_f):
    b=candidate_c_raw_background(a)
    qscale=np.array([1.0,1.0,1.0/max(k*k,1.0),1.0])
    scale=np.r_[qscale,qscale]
    def F(x): return _eliminate_primary(b,k,x[:4],x[4:],cs2_g,cs2_f)
    H=_hessian(F,scale)
    return b,H[4:,4:],H[4:,:4],H[:4,:4]


def physical_matrices(a,k,*,cs2_g=0.4,cs2_f=0.3,diff_step=5e-4):
    b,K,C,Q=_primary_matrices(a,k,cs2_g,cs2_f)
    ap=a*math.exp(diff_step); am=a*math.exp(-diff_step)
    _,_,Cp,_=_primary_matrices(ap,k,cs2_g,cs2_f)
    _,_,Cm,_=_primary_matrices(am,k,cs2_g,cs2_f)
    Cdot=b.H*(Cp-Cm)/(2*diff_step)
    red=eliminate_time_dependent_null_coordinate(K,C,Q,Cdot,null_index=3,tol=1e-8)
    return b,red


def mode_speeds(a,k,*,cs2_g=0.4,cs2_f=0.3,diff_step=5e-4):
    b,red=physical_matrices(a,k,cs2_g=cs2_g,cs2_f=cs2_f,diff_step=diff_step)
    outer=5.0*diff_step
    _,rp=physical_matrices(a*math.exp(outer),k,cs2_g=cs2_g,cs2_f=cs2_f,diff_step=diff_step)
    _,rm=physical_matrices(a*math.exp(-outer),k,cs2_g=cs2_g,cs2_f=cs2_f,diff_step=diff_step)
    Kdot=b.H*(rp.K-rm.K)/(2*outer)
    Cdot=b.H*(rp.C-rm.C)/(2*outer)
    eom=euler_lagrange_matrices(red.K,red.C,red.Q,Kdot,Cdot)
    Ki=np.linalg.inv(eom.K)
    A=np.block([[np.zeros((3,3)),np.eye(3)],[-Ki@eom.E,-Ki@eom.D]])
    roots=np.linalg.eigvals(A)
    speeds=sorted([float(r.imag*a/k) for r in roots if r.imag>1e-6])
    if len(speeds)!=3:
        raise RuntimeError(f"expected 3 oscillatory scalar pairs, got {len(speeds)}")
    return np.asarray(speeds)


def candidate_c_three_mode_extrapolation(a=0.5,*,k_values=(100.0,150.0,250.0),cs2_g=0.4,cs2_f=0.3,diff_step=5e-4):
    ks=np.asarray(k_values,float)
    rows=np.vstack([mode_speeds(a,float(k),cs2_g=cs2_g,cs2_f=cs2_f,diff_step=diff_step) for k in ks])
    x=1.0/ks**2
    intercept=np.array([np.polyfit(x,rows[:,j],1)[1] for j in range(3)])
    return ThreeModeSpeeds(ks,rows,intercept)

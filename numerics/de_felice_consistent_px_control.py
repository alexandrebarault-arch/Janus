"""Self-consistent P(X) control for the raw De Felice scalar reduction.

This module is a diagnostic oracle. Unlike the Candidate-C probe benchmark,
its two fluids have constant barotropic equations of state w_a=c_a^2, so the
background and the Eq. (54) matter perturbation variables are mutually
consistent.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.de_felice_raw_scalar_action import (
    RawBimetricBackground,
    raw_two_matter_scalar_density_g_flat,
)

_BETA1=1.0
_BETA2=-4.2383993109
_BETA3=13.6801214252
_BETA4=-38.5117901844
_ALPHA=0.10879548725
_KAPPA=_ALPHA**2
_M2=23.3348939346
_Y0=0.55688253212
_RHO_G0=3.0*(0.30+9.0e-5)
_RHO_F0=3.0*0.23958426762


@dataclass(frozen=True)
class ConsistentPXBackground:
    a: float
    xi: float
    ctilde: float
    kappa: float
    H: float
    Hf: float
    Hdot: float
    Hfdot_over_n: float
    rho_g: float
    pressure_g: float
    rho_f: float
    pressure_f: float
    mu_g: float
    mu_f: float
    zeta: float
    gamma_m: float
    R: float
    Rdot: float
    nlogdot: float


def _ug(xi):
    return 3.0*_BETA1*xi+3.0*_BETA2*xi**2+_BETA3*xi**3


def _uf(xi):
    return _BETA4+3.0*_BETA3/xi+3.0*_BETA2/xi**2+_BETA1/xi**3


def _densities(a,xi,cs2_g,cs2_f):
    rho_g=_RHO_G0*a**(-3.0*(1.0+cs2_g))
    rho_f=_RHO_F0*(_Y0/(a*xi))**(3.0*(1.0+cs2_f))
    return rho_g,rho_f


def _friedmann_match(xi,a,cs2_g,cs2_f):
    rho_g,rho_f=_densities(a,xi,cs2_g,cs2_f)
    return _KAPPA*(_M2*_ug(xi)+rho_g)-xi**2*(_M2*_uf(xi)+rho_f)


def _solve_xi(a,cs2_g,cs2_f):
    grid=np.geomspace(0.03,5.0,1000)
    vals=[_friedmann_match(x,a,cs2_g,cs2_f) for x in grid]
    roots=[]
    for x1,x2,f1,f2 in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
        if f1==0.0:
            roots.append(float(x1))
        elif f1*f2<0.0:
            lo=float(x1); hi=float(x2); flo=float(f1)
            for _ in range(80):
                mid=0.5*(lo+hi); fm=_friedmann_match(mid,a,cs2_g,cs2_f)
                if flo*fm<=0.0:
                    hi=mid
                else:
                    lo=mid; flo=fm
            roots.append(0.5*(lo+hi))
    if not roots:
        raise RuntimeError("no positive healthy-like xi root")
    return roots[-1]


def consistent_px_background(a,*,cs2_g=0.4,cs2_f=0.3,diff_step=2.0e-5):
    if a<=0.0 or cs2_g<=0.0 or cs2_f<=0.0:
        raise ValueError("a and sound speeds must be positive")
    x=math.log(a); h=float(diff_step)
    xis=[_solve_xi(math.exp(x+j*h),cs2_g,cs2_f) for j in (-2,-1,0,1,2)]
    xm2,xm1,xi,xp1,xp2=xis
    xi_N=(xm2-8.0*xm1+8.0*xp1-xp2)/(12.0*h)
    xi_NN=(-xp2+16.0*xp1-30.0*xi+16.0*xm1-xm2)/(12.0*h*h)
    c=1.0+xi_N/xi
    J=_BETA1+2.0*_BETA2*xi+_BETA3*xi**2
    Jp=2.0*_BETA2+2.0*_BETA3*xi
    Gamma=xi*J+0.5*(c-1.0)*xi**2*Jp
    rho_g,rho_f=_densities(a,xi,cs2_g,cs2_f)
    pressure_g=cs2_g*rho_g
    pressure_f=cs2_f*rho_f
    H=math.sqrt((_M2*_ug(xi)+rho_g)/3.0)
    Hf=H/xi
    Hdot=0.5*(_M2*xi*J*(c-1.0)-(rho_g+pressure_g))
    Hfdot=-0.5*(_M2*J*(c-1.0)/(_KAPPA*xi**3*c)+(rho_f+pressure_f)/_KAPPA)
    mu_g=3.0*H**2-rho_g
    mu_f=3.0*_KAPPA*Hf**2-rho_f
    c_N=xi_NN/xi-(xi_N/xi)**2
    nlogdot=H*(c_N/c+xi_N/xi)
    R=1.0/(c*H)
    Rdot=-R*(H*c_N/c+Hdot/H)
    return ConsistentPXBackground(
        a=float(a),xi=float(xi),ctilde=float(c),kappa=_KAPPA,H=float(H),Hf=float(Hf),
        Hdot=float(Hdot),Hfdot_over_n=float(Hfdot),rho_g=float(rho_g),
        pressure_g=float(pressure_g),rho_f=float(rho_f),pressure_f=float(pressure_f),
        mu_g=float(mu_g),mu_f=float(mu_f),zeta=float(_M2*xi*J),
        gamma_m=float(_M2*Gamma),R=float(R),Rdot=float(Rdot),nlogdot=float(nlogdot),
    )


def _raw_bg(b):
    return RawBimetricBackground(
        N=1.0,a=b.a,xi=b.xi,ctilde=b.ctilde,kappa=b.kappa,H=b.H,Hf=b.Hf,
        Hdot_over_N=b.Hdot,Hfdot_over_n=b.Hfdot_over_n,mu_g=b.mu_g,mu_f=b.mu_f,
        zeta=b.zeta,gamma_m=b.gamma_m,Mgsq=1.0,
    )


def _quadratic_hessian(fun,scales):
    scales=np.asarray(scales,float); n=len(scales); H=np.zeros((n,n)); z=np.zeros(n)
    f0=fun(z); fi=[]
    for i in range(n):
        ei=np.zeros(n); ei[i]=scales[i]; vi=fun(ei); fi.append(vi)
        H[i,i]=2.0*(vi-f0)/scales[i]**2
        for j in range(i):
            ej=np.zeros(n); ej[j]=scales[j]
            H[i,j]=H[j,i]=(fun(ei+ej)-vi-fi[j]+f0)/(scales[i]*scales[j])
    return H


def _primary_matrices(a,k,cs2_g,cs2_f):
    b=consistent_px_background(a,cs2_g=cs2_g,cs2_f=cs2_f)
    scales=np.array([
        1.0,b.a/max(k,1.0),1.0,b.a*b.xi/max(k,1.0),
        1.0,1.0,1.0/max(k*k,1.0),1.0,
        1.0,1.0,1.0/max(k*k,1.0),1.0,
    ])
    def lag(x):
        Phi,B,varphi,bshift=x[:4]
        ug,Y2,S,Sigma=x[4:8]
        ugd,Y2d,Sd,Sigmad=x[8:12]
        geom=Sigma+k*k*S/6.0
        geomd=Sigmad+k*k*Sd/6.0
        uf=Y2+b.R*geom
        qg=ugd-3.0*b.H*cs2_g*ug
        qf0=Y2d+b.R*geomd+b.Rdot*geom
        qf=qf0+(b.nlogdot-3.0*b.ctilde*b.H*cs2_f)*uf
        density=raw_two_matter_scalar_density_g_flat(
            _raw_bg(b),k=k,Phi=Phi,B=B,varphi=varphi,b=bshift,Sigma=Sigma,S=S,
            Sigma_dot=Sigmad,S_dot=Sd,rho_g=b.rho_g,pressure_g=b.pressure_g,
            cs2_g=cs2_g,u_g=ug,u_g_dot=qg,rho_f=b.rho_f,pressure_f=b.pressure_f,
            cs2_f=cs2_f,u_f=uf,u_f_dot=qf,
        )
        return b.a**3*density
    H=_quadratic_hessian(lag,scales)
    A=H[:4,:4]; X=H[:4,4:]; D=H[4:,4:]
    red=D-X.T@np.linalg.solve(A,X)
    return b,red[4:,4:],red[4:,:4],red[:4,:4]


def _primary_derivatives(a,k,cs2_g,cs2_f,h=0.003):
    vals=[_primary_matrices(a*math.exp(j*h),k,cs2_g,cs2_f) for j in (-2,-1,0,1,2)]
    b,K,C,Q=vals[2]
    def d1(idx):
        fm2,fm1,_,fp1,fp2=[v[idx] for v in vals]
        return (fm2-8.0*fm1+8.0*fp1-fp2)/(12.0*h)
    def d2(idx):
        fm2,fm1,f0,fp1,fp2=[v[idx] for v in vals]
        return (-fp2+16.0*fp1-30.0*f0+16.0*fm1-fm2)/(12.0*h*h)
    Kx,Cx,Qx=d1(1),d1(2),d1(3)
    Cxx=d2(2)
    return b,K,C,Q,b.H*Kx,b.H*Cx,b.H*Qx,b.Hdot*Cx+b.H**2*Cxx


def consistent_px_mode_speeds(a,k,*,cs2_g=0.4,cs2_f=0.3,diff_step=0.003):
    b,K,C,Q,Kdot,Cdot,Qdot,Cddot=_primary_derivatives(a,k,cs2_g,cs2_f,diff_step)
    keep=[0,1,2]; z=3
    d=C[keep,z]-C[z,keep]
    r=Q[keep,z]-Cdot[z,keep]
    q=float(Q[z,z]-Cdot[z,z])
    Kred=K[np.ix_(keep,keep)]-np.outer(d,d)/q
    Cred=C[np.ix_(keep,keep)]-np.outer(d,r)/q
    Qred=Q[np.ix_(keep,keep)]-np.outer(r,r)/q
    dd=Cdot[keep,z]-Cdot[z,keep]
    rd=Qdot[keep,z]-Cddot[z,keep]
    qd=float(Qdot[z,z]-Cddot[z,z])
    Kred_dot=Kdot[np.ix_(keep,keep)]-(np.outer(dd,d)+np.outer(d,dd))/q+np.outer(d,d)*qd/q**2
    Cred_dot=Cdot[np.ix_(keep,keep)]-(np.outer(dd,r)+np.outer(d,rd))/q+np.outer(d,r)*qd/q**2
    D=Kred_dot+Cred-Cred.T
    E=Cred_dot-Qred
    T=np.diag([1.0,1.0,1.0/(k*k)])
    Kred=T.T@Kred@T; D=T.T@D@T; E=T.T@E@T
    A=np.block([[np.zeros((3,3)),np.eye(3)],[-np.linalg.solve(Kred,E),-np.linalg.solve(Kred,D)]])
    roots=np.linalg.eigvals(A)
    return np.array(sorted(float(r.imag*a/k) for r in roots if r.imag>1.0e-7))


def consistent_px_gravity_target(bg):
    J=bg.zeta/(_M2*bg.xi)
    Gamma=bg.gamma_m/_M2
    W=_M2*(1.0+_KAPPA*bg.xi**2)*J/(2.0*_KAPPA*bg.xi)-bg.H**2
    B=2.0*W+bg.xi**2*(bg.rho_f+bg.pressure_f)/_KAPPA
    cs2=(
        _M2/(3.0*B)*(1.0+1.0/(_KAPPA*bg.xi**2))*(4.0*Gamma-bg.xi*J*(bg.ctilde+1.0))
        +(bg.ctilde-4.0*bg.H**2*Gamma/(bg.xi*J*B))/3.0
    )
    if cs2<=0.0:
        raise ValueError("control background has a gradient-unstable gravity scalar")
    return math.sqrt(cs2)

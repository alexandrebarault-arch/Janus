"""Fit compact principal kinetic/gradient matrices for (pi, q_g, q_f)."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.nonhomothetic_threefield_schur import reduce_nonhomothetic_threefield_metric_block


@dataclass(frozen=True)
class ThreeFieldPrincipalFit:
    kinetic: np.ndarray
    gradient: np.ndarray
    masslike: np.ndarray
    nonnull_squared_speeds: np.ndarray
    fit_relative_residual: float


def _profile_integrals(T: float, R: float, order: int = 56):
    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    t=T*xt[:,None]
    r=.5*R*(xr[None,:]+1.0)
    W=(T*wt)[:,None]*(.5*R*wr)[None,:]
    x=t/T
    A=(1-x*x)**3
    At=(-6*x*(1-x*x)**2)/T
    F=r*r-3*r**4/R**2+3*r**6/R**4-r**8/R**6
    Fr=2*r-12*r**3/R**2+18*r**5/R**4-8*r**7/R**6
    rr2=r*r
    It=float(np.sum(W*rr2*(At*F)**2))
    Ig=float(np.sum(W*rr2*(A*Fr)**2))
    I0=float(np.sum(W*rr2*(A*F)**2))
    return It,Ig,I0


def _nonnull_speeds(K,G,rtol=1e-10):
    K=np.asarray(K,float)
    G=np.asarray(G,float)
    w,U=np.linalg.eigh(0.5*(K+K.T))
    scale=max(1.0,float(np.max(np.abs(w))))
    keep=np.abs(w)>rtol*scale
    if not np.any(keep):
        return np.empty(0,float)
    Ur=U[:,keep]
    Kr=Ur.T@K@Ur
    Gr=Ur.T@G@Ur
    A=-np.linalg.solve(Kr,Gr)
    vals=np.linalg.eigvals(A)
    if np.max(np.abs(vals.imag))>1e-7*max(1.0,float(np.max(np.abs(vals.real)))):
        raise np.linalg.LinAlgError('principal speeds became complex')
    return np.sort(vals.real)


def fit_threefield_principal_matrices(*,betas,jet,time_scales,radial_scales,
        interaction_mass2,planck_ratio,rho_g,rho_f,cs2_g,cs2_f,
        pressure_g=0.0,pressure_f=0.0,amplitude_step=2e-5,quadrature_order=14):
    """Fit H(T,R)=I_t K + I_r G + I_0 M after the metric Schur complement."""
    Ts=tuple(float(x) for x in time_scales)
    Rs=tuple(float(x) for x in radial_scales)
    if len(Ts)<2 or len(Rs)<2 or not all(math.isfinite(x) and x>0 for x in Ts+Rs):
        raise ValueError('need positive finite time/radial scales')
    rows=[]
    mats=[]
    for T in Ts:
        for R in Rs:
            out=reduce_nonhomothetic_threefield_metric_block(
                betas=betas,jet=jet,time_radius=T,radial_radius=R,
                interaction_mass2=interaction_mass2,planck_ratio=planck_ratio,
                rho_g=rho_g,rho_f=rho_f,cs2_g=cs2_g,cs2_f=cs2_f,
                pressure_g=pressure_g,pressure_f=pressure_f,
                amplitude_step=amplitude_step,quadrature_order=quadrature_order)
            rows.append(_profile_integrals(T,R))
            mats.append(out.reduced_physical_hessian)
    X=np.asarray(rows,float)
    Y=np.asarray(mats,float).reshape(len(rows),9)
    coeff,_,rank,_=np.linalg.lstsq(X,Y,rcond=None)
    if rank<3:
        raise np.linalg.LinAlgError('principal compact fit is rank deficient')
    pred=X@coeff
    residual=float(np.linalg.norm(pred-Y)/max(1e-30,np.linalg.norm(Y)))
    K=coeff[0].reshape(3,3)
    G=coeff[1].reshape(3,3)
    M=coeff[2].reshape(3,3)
    K=.5*(K+K.T)
    G=.5*(G+G.T)
    M=.5*(M+M.T)
    return ThreeFieldPrincipalFit(
        kinetic=K,
        gradient=G,
        masslike=M,
        nonnull_squared_speeds=_nonnull_speeds(K,G),
        fit_relative_residual=residual,
    )

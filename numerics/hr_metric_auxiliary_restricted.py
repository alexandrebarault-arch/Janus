"""Restricted compact-lapse/shift Schur gate on the Step32b COMMON action.

Four configuration-level auxiliaries Phi_g,U_g,Phi_f,U_f are eliminated
ALGEBRAICALLY from a finite-dimensional 18-amplitude Hessian obtained by
integrating one positive-EH_g/f + all-beta HR + 2 canonical dust action.

IMPORTANT: the trial basis does NOT close under full spacetime diffeomorphisms
or metric rate integrability and Phi is NOT the canonical ADM lapse variable.
The 4x4 inverse and its 14x14 Schur complement are a reproducible Galerkin
matrix identity, NOT full GR/BD constraints, propagation speeds, ghost status
or any physical on-shell nonhomothetic result.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_common_time_metric_rates import action, ORDER
from numerics.hr_full_onshell_tadpole import Trajectory

AUXILIARY_INDICES=(0,1,7,8)
RETAINED_INDICES=tuple(i for i in range(18) if i not in AUXILIARY_INDICES)
PHASE_MOMENTUM_INDICES=((5,6),(12,13))


@dataclass(frozen=True)
class RestrictedAuxiliary:
    hessian:np.ndarray
    gradient:np.ndarray
    auxiliary:np.ndarray
    mixed:np.ndarray
    retained:np.ndarray
    schur:np.ndarray
    response:np.ndarray
    condition:float
    auxiliary_rank:int
    symplectic:np.ndarray
    order:tuple[str,...]=ORDER


def hessian_and_gradient(*,step=.012,gradient_step=2e-5,trajectory=None,quadrature_order=20,
                         time_radius=.027,radial_radius=.32,betas=None,m2=None):
    """Explicit centered finite Hessian of the ONE actual spacetime action."""
    if not math.isfinite(step) or not 0<step<.07:
        raise ValueError('finite positive Hessian step required (<0.07)')
    if not math.isfinite(gradient_step) or not 0<gradient_step<.002:
        raise ValueError('independent finite positive gradient step required')
    if type(quadrature_order) is not int or quadrature_order<10:
        raise ValueError('quadrature must be integer >= 10')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    kwargs=dict(trajectory=bg,quadrature_order=quadrature_order,
                time_radius=time_radius,radial_radius=radial_radius)
    if betas is not None: kwargs['betas']=betas
    if m2 is not None: kwargs['m2']=m2
    def value(v):return action(v,**kwargs).total
    n=18;z=np.zeros(n);v0=value(z)
    H=np.zeros((n,n));g=np.zeros(n)
    for i in range(n):
        p=np.zeros(n);p[i]=step
        sp=value(p);sm=value(-p)
        gp=p*(gradient_step/step)
        g[i]=(value(gp)-value(-gp))/(2*gradient_step)
        H[i,i]=(sp-2*v0+sm)/(step*step)
        for j in range(i):
            q=np.zeros(n);q[j]=step
            H[i,j]=H[j,i]=(value(p+q)-value(p-q)-value(-p+q)+value(-p-q))/(4*step*step)
    if not (np.all(np.isfinite(H)) and np.all(np.isfinite(g))):
        raise ArithmeticError('nonfinite preconstraint Hessian/gradient')
    return .5*(H+H.T),g


def restricted_auxiliary_schur(*,step=.012,quadrature_order=20,
                               max_condition=1e8,**kwargs):
    """Stationarize only the four restricted lapse/shift *trial amplitudes*.

    For Q(x_aux,y)=.5*x.T A x +x.T B y +.5*y.T C y:
       x_aux*=-A^-1 B y; Q_eff=.5*y.T(C-B.T A^-1 B)y.
    The function deliberately refuses singular/ill-conditioned test bases.
    """
    if not math.isfinite(max_condition) or max_condition<=1:
        raise ValueError('positive max_condition greater than one required')
    H,g=hessian_and_gradient(step=step,quadrature_order=quadrature_order,**kwargs)
    ix=np.array(AUXILIARY_INDICES);iy=np.array(RETAINED_INDICES)
    A=H[np.ix_(ix,ix)];B=H[np.ix_(ix,iy)];C=H[np.ix_(iy,iy)]
    cond=float(np.linalg.cond(A))
    rank=int(np.linalg.matrix_rank(A,tol=1e-11))
    if rank!=4 or not math.isfinite(cond) or cond>max_condition:
        raise np.linalg.LinAlgError('restricted auxiliary block ill-conditioned or singular')
    X=-np.linalg.solve(A,B)
    S=.5*((C+B.T@X)+(C+B.T@X).T)
    index={v:i for i,v in enumerate(RETAINED_INDICES)}
    P=np.array([[S[index[pi],index[rate]] for rate in (6,13)]
                for pi in (5,12)])
    return RestrictedAuxiliary(H,g,A,B,C,S,X,cond,rank,P)


def restricted_quadratic_residuals(result,retained):
    """Compare exact 18D quadratic Q at aux saddle versus 14D Schur Q.

    This controls algebraic correctness only. It does NOT claim that the
    saddle is a physical Hamiltonian lapse/shift constraint solution.
    """
    y=np.asarray(retained,float)
    if y.shape!=(14,) or not np.all(np.isfinite(y)):
        raise ValueError('14 finite retained trial amplitudes required')
    x=result.response@y
    full=np.zeros(18)
    full[list(AUXILIARY_INDICES)]=x
    full[list(RETAINED_INDICES)]=y
    e18=float(full@result.hessian@full/2)
    e14=float(y@result.schur@y/2)
    aux_grad=result.auxiliary@x+result.mixed@y
    return full,e18,e14,aux_grad

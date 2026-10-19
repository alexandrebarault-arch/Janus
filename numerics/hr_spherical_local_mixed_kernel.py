"""Local bilinear radial smearing jet kernel for two-metric HR+two-dust bracket.

This decomposes the TRUE mixed functional Poisson bracket in an arbitrary
regular off-shell radial geometry before imposing either primary constraint.
At a radius r, {Hg[N],Hf[M]}_r = sum_{i,j=0}^2 K_ij(r) N^(i)(r) M^(j)(r).

K_ij comes from independent exact functional Euler derivatives of the
IBP-converted Hamiltonian densities. No primary constraint surface, Dirac
secondary condition, gauge reduction, or physical ghost verdict is implied.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_mixed_hamiltonian_bracket import (
  Q,CANONICAL_PAIRS,BOUNDS,DEFAULT_BETAS,DEFAULT_M2,DEFAULT_MG2,DEFAULT_MF2,
  _check_fields,_compiled,_sample,_nodes,default_fields,compact_smearings,
)

@dataclass(frozen=True)
class LocalKernel:
    coefficients:np.ndarray
    g_gradient_by_njet:np.ndarray
    f_gradient_by_mjet:np.ndarray
    radius:float


def local_mixed_kernel(fields=None,r=.43,*,z_mode='root',z_fixed=None,
    betas=DEFAULT_BETAS,m2=DEFAULT_M2,mg2=DEFAULT_MG2,mf2=DEFAULT_MF2,
    complex_step=1.e-18):
    """Exact differential operator to second order in each compact smearing.

    For each smearing jet 0,1,2 use centered monomials whose derivatives
    at r isolate Kronecker delta jets. Assembles local 3x3 coefficient
    matrix without expanding a 1000-term symbolic mixed bracket.
    """
    fields=default_fields() if fields is None else fields
    _check_fields(fields)
    if not (math.isfinite(r) and BOUNDS[0]<r<BOUNDS[1]):
        raise ValueError('interior finite radius required')
    if not math.isfinite(complex_step) or complex_step<=0:
        raise ValueError('positive complex step required')
    ev=_compiled()
    unit=Poly([-r,1.])
    basis=(Poly([1.]),unit,unit*unit/2.)
    zero=Poly([0.])
    g=np.zeros((3,12));f=np.zeros((3,12))
    for j in range(3):
        for sector in (0,1):
            N,M=(basis[j],zero) if sector==0 else (zero,basis[j])
            v=_sample(fields,N,M,r,z_mode=z_mode,z_fixed=z_fixed,
                      betas=betas,m2=m2,mg2=mg2,mf2=mf2)
            vc=_sample(fields,N,M,complex(r,complex_step),z_mode=z_mode,
                       z_fixed=z_fixed,betas=betas,m2=m2,mg2=mg2,mf2=mf2)
            val=np.asarray(ev(*v),float); rad=np.asarray(ev(*vc),complex)
            if val.shape!=(50,) or not np.all(np.isfinite(val)):
                raise ArithmeticError('nonfinite canonical radial partial derivatives')
            if sector==0:g[j]=val[2:14]-np.imag(rad[14:26])/complex_step
            else:f[j]=val[26:38]-np.imag(rad[38:50])/complex_step
    C=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            for k,(q,p) in enumerate(CANONICAL_PAIRS):
                idx=2*k
                C[i,j]+=g[i,idx]*f[j,idx+1]-g[i,idx+1]*f[j,idx]
    return LocalKernel(C,g,f,r)


def evaluate_kernel(kernel,N,M):
    """Local mixed Poisson density for any polynomial/radial jet pair."""
    r=kernel.radius
    if not isinstance(N,Poly) or not isinstance(M,Poly):
        raise ValueError('radial polynomial smearings required')
    vn=np.array([N.deriv(j)(r) for j in range(3)])
    vm=np.array([M.deriv(j)(r) for j in range(3)])
    return float(vn@kernel.coefficients@vm)


def integrate_kernel(fields=None,N=None,M=None,*,order=24,interval=BOUNDS,
                    z_mode='root',z_fixed=None,**kwargs):
    """Radial integration of the local 3x3 differential smearing kernel."""
    fields=default_fields() if fields is None else fields
    _check_fields(fields)
    n,mm=compact_smearings()
    N=n if N is None else N
    M=mm if M is None else M
    a,b=interval
    if not all(abs(s(x))<2e-10 for s in (N,M) for x in (a,b)):
        raise ValueError('compact lapse smearings must vanish on both boundaries')
    x,w=_nodes(order,a,b)
    contributions=np.zeros((3,3))
    for r,wr in zip(x,w):
        res=local_mixed_kernel(fields,float(r),z_mode=z_mode,z_fixed=z_fixed,**kwargs)
        vn=np.array([N.deriv(j)(r) for j in range(3)])
        vm=np.array([M.deriv(j)(r) for j in range(3)])
        contributions+=wr*res.coefficients*np.outer(vn,vm)
    return contributions

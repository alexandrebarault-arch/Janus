"""Exact local HR interaction spectral polynomial and derivatives.

Eigenvalues: (temporal, radial, angular, angular). Local algebraic block
only: not the complete finite-mu dynamical action.
"""
import numpy as np


def spectral_potential(t, r, ell, betas):
    """Return U, gradient, Hessian in (t,r,ell) for sum beta_n e_n."""
    b = np.asarray(betas, dtype=float)
    x = np.array([t, r, ell], dtype=float)
    if b.shape != (5,) or not np.all(np.isfinite(b)) or not np.all(np.isfinite(x)):
        raise ValueError("expected finite eigenvalues and five beta coefficients")
    t, r, l = x
    e = np.array([1, t+r+2*l, t*r+2*l*(t+r)+l*l,
                  2*t*r*l+(t+r)*l*l, t*r*l*l])
    de = np.array([[0,0,0], [1,1,2],
                   [r+2*l,t+2*l,2*(t+r+l)],
                   [2*r*l+l*l,2*t*l+l*l,2*t*r+2*l*(t+r)],
                   [r*l*l,t*l*l,2*t*r*l]])
    d2 = np.zeros((5,3,3))
    d2[2,0,1]=d2[2,1,0]=1
    d2[2,0,2]=d2[2,2,0]=2
    d2[2,1,2]=d2[2,2,1]=2
    d2[2,2,2]=2
    d2[3,0,1]=d2[3,1,0]=2*l
    d2[3,0,2]=d2[3,2,0]=2*r+2*l
    d2[3,1,2]=d2[3,2,1]=2*t+2*l
    d2[3,2,2]=2*(t+r)
    d2[4,0,1]=d2[4,1,0]=l*l
    d2[4,0,2]=d2[4,2,0]=2*r*l
    d2[4,1,2]=d2[4,2,1]=2*t*l
    d2[4,2,2]=2*t*r
    return float(b@e), b@de, np.tensordot(b,d2,axes=(0,0))

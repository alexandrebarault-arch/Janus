"""Finite-mu Hassan-Rosen correction for one relative scalar Fourier mode."""
from __future__ import annotations

import math
import numpy as np

from numerics.nonhomothetic_hr_relative_native import relative_native_hr_density


def _relative_hr_mode_action(
    x,
    *,
    a: float,
    n: float,
    alpha: float,
    r: float,
    k: float,
    betas,
    m2: float,
    Mg2: float,
    phase_samples: int,
    **background,
) -> float:
    """Return the common-volume-normalized real-mode finite-mu HR correction.

    ``x`` order is ``(L,T,Ldot,Tdot,Phi_g,Phi_f,B_g,B_f)``.  The real
    Fourier mode is phase averaged and multiplied by two so its quadratic
    normalization matches the single complex Fourier amplitude convention of
    the De Felice action.
    """
    q = np.asarray(x, dtype=float)
    if q.shape != (8,) or not np.all(np.isfinite(q)):
        raise ValueError("mode coordinates must contain eight finite values")
    if not (math.isfinite(k) and k >= 0.0):
        raise ValueError("k must be finite and non-negative")
    if phase_samples < 16:
        raise ValueError("phase_samples must be at least 16")

    L,T,Ldot,Tdot,Pg,Pf,Bg,Bf = [float(v) for v in q]
    mu = float(background.get("mu", 0.0))
    finite_vals = []
    linear_vals = []
    for theta in np.linspace(0.0, 2.0*math.pi, int(phase_samples), endpoint=False):
        co = math.cos(theta)
        si = math.sin(theta)
        common = dict(
            a=a,n=n,alpha=alpha,r=r,
            T=T*co,T_dot=Tdot*co,T_r=-k*T*si,
            L_r=-k*L*si,L_dot_r=-k*Ldot*si,L_rr=-k*k*L*co,
            Phi_g=Pg*co,B_g_r=-k*Bg*si,
            Phi_f=Pf*co,
        )
        finite = dict(common)
        finite.update(background)
        finite["B_f_r"] = -k*Bf*si/(1.0+mu)
        finite_vals.append(relative_native_hr_density(
            betas=betas,m2=m2,Mg2=Mg2,**finite,
        ))

        ref = dict(common)
        ref.update(background)
        ref.update(mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,B_f_r=-k*Bf*si)
        linear_vals.append(relative_native_hr_density(
            betas=betas,m2=m2,Mg2=Mg2,**ref,
        ))

    return float(-2.0*(np.mean(finite_vals)-np.mean(linear_vals))/(a**3*r*r))


def relative_hr_mode_correction_hessian(
    *,
    a: float,
    n: float,
    alpha: float,
    r: float,
    k: float,
    betas,
    m2: float = 1.0,
    Mg2: float = 1.0,
    amplitude_step: float = 5.0e-4,
    phase_samples: int = 64,
    **background,
) -> np.ndarray:
    """Return the 8x8 finite-mu HR correction Hessian for one scalar mode."""
    h = float(amplitude_step)
    if not (math.isfinite(h) and h > 0.0):
        raise ValueError("amplitude_step must be positive and finite")
    nvar = 8
    eye = np.eye(nvar, dtype=float)
    mu = float(background.get("mu", 0.0))
    if mu <= -1.0:
        raise ValueError("mu must exceed -1")
    k_eff = max(abs(float(k)), 1.0)
    # ``amplitude_step`` is a dimensionless perturbation fraction, not a raw
    # step in every scalar coordinate.  L enters through k L and k^2 L, T
    # through k T, and the shifts through their metric-normalized gradients.
    # Scaling the polarization vectors prevents a high-k Hessian probe from
    # leaving the real/positive pullback branch while preserving the Hessian
    # in the original coordinates through the explicit scale divisions below.
    scales = np.array([
        h*float(r)/k_eff,
        h/k_eff,
        h/k_eff,
        h,
        h,
        h,
        h/max(abs(float(a)*float(k)), 1.0),
        h/max(abs((float(alpha)/float(n))*float(k)/(1.0+mu)), 1.0),
    ], dtype=float)
    kwargs = dict(
        a=float(a),n=float(n),alpha=float(alpha),r=float(r),k=float(k),
        betas=tuple(float(v) for v in betas),m2=float(m2),Mg2=float(Mg2),
        phase_samples=int(phase_samples),**background,
    )
    zero = np.zeros(nvar, dtype=float)
    f0 = _relative_hr_mode_action(zero, **kwargs)
    H = np.zeros((nvar,nvar), dtype=float)
    for i in range(nvar):
        si = float(scales[i])
        ei = si*eye[i]
        H[i,i] = (
            _relative_hr_mode_action(ei,**kwargs)
            - 2.0*f0
            + _relative_hr_mode_action(-ei,**kwargs)
        )/(si*si)
        for j in range(i+1,nvar):
            sj = float(scales[j])
            ej = sj*eye[j]
            value = (
                _relative_hr_mode_action(ei+ej,**kwargs)
                - _relative_hr_mode_action(ei-ej,**kwargs)
                - _relative_hr_mode_action(-ei+ej,**kwargs)
                + _relative_hr_mode_action(-ei-ej,**kwargs)
            )/(4.0*si*sj)
            H[i,j] = H[j,i] = value
    return 0.5*(H+H.T)


def embed_relative_hr_correction_hessian(H8) -> np.ndarray:
    """Embed the HR-only correction in the validated 16-variable augmented order."""
    H = np.asarray(H8,dtype=float)
    if H.shape != (8,8) or not np.all(np.isfinite(H)):
        raise ValueError("H8 must be a finite 8x8 matrix")
    out = np.zeros((16,16),dtype=float)
    idx = [2,3,8,9,12,13,14,15]
    out[np.ix_(idx,idx)] = H
    return 0.5*(out+out.T)

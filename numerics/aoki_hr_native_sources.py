"""Hassan-Rosen interaction tensors in the native radial charts of both metrics."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.nonhomothetic_hr_interaction_tensor import interaction_mixed_tensors


@dataclass(frozen=True)
class NativeInteractionSources:
    square_root_common: np.ndarray
    g_common: np.ndarray
    f_common: np.ndarray
    g_native: np.ndarray
    f_native: np.ndarray


def _finite_matrix(name: str, value, shape=(2,2)) -> np.ndarray:
    arr=np.asarray(value,dtype=float)
    if arr.shape!=shape or not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must be a finite {shape[0]}x{shape[1]} matrix")
    return arr


def _radial_principal_sqrt(A: np.ndarray) -> np.ndarray:
    det=float(np.linalg.det(A))
    tr=float(np.trace(A))
    if det<=0.0:
        raise ValueError("radial g^-1 f determinant must be positive")
    sd=math.sqrt(det)
    den=tr+2.0*sd
    if den<=0.0:
        raise ValueError("radial principal square root is not real")
    return (A+sd*np.eye(2))/math.sqrt(den)


def _to_native(V_common: np.ndarray, J: np.ndarray) -> np.ndarray:
    Ji=np.linalg.inv(J)
    out=np.zeros((4,4),dtype=float)
    out[:2,:2]=J@V_common[:2,:2]@Ji
    out[2,2]=V_common[2,2]
    out[3,3]=V_common[3,3]
    return out


def native_interaction_sources(
    *,
    g_radial_native,
    f_radial_native,
    g_angular_native: float,
    f_angular_native: float,
    jacobian_g,
    jacobian_f,
    betas,
) -> NativeInteractionSources:
    """Evaluate mixed HR tensors and express each in its own native chart.

    ``jacobian_g`` and ``jacobian_f`` are ``d x_native / d x_common`` for the
    two radial coordinate pairs. Angular coordinates are shared.
    """
    gn=_finite_matrix("g_radial_native",g_radial_native)
    fn=_finite_matrix("f_radial_native",f_radial_native)
    Jg=_finite_matrix("jacobian_g",jacobian_g)
    Jf=_finite_matrix("jacobian_f",jacobian_f)
    vals=(g_angular_native,f_angular_native)
    if not all(math.isfinite(float(v)) for v in vals) or min(vals)<=0.0:
        raise ValueError("angular metric coefficients must be positive and finite")
    if abs(np.linalg.det(Jg))<=1e-14 or abs(np.linalg.det(Jf))<=1e-14:
        raise np.linalg.LinAlgError("native coordinate Jacobian is singular")

    gc=Jg.T@gn@Jg
    fc=Jf.T@fn@Jf
    A=np.linalg.solve(gc,fc)
    Sr=_radial_principal_sqrt(A)
    ell=math.sqrt(float(f_angular_native/g_angular_native))
    S=np.zeros((4,4),dtype=float)
    S[:2,:2]=Sr
    S[2,2]=ell
    S[3,3]=ell
    vg_common,vf_common=interaction_mixed_tensors(S,betas)
    return NativeInteractionSources(
        square_root_common=S,
        g_common=vg_common,
        f_common=vf_common,
        g_native=_to_native(vg_common,Jg),
        f_native=_to_native(vf_common,Jf),
    )

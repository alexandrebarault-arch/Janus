"""Physical density observables for the exact two-dust canonical system."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.de_felice_dust_physical_action import DustCanonicalAction


@dataclass(frozen=True)
class DustObservables:
    delta_rho_g: float
    delta_rho_f: float
    delta_g: float
    delta_f: float
    delta_common: float
    delta_relative: float


def _boundary_gradient(coordinates, zdot_column, *, z_index: int) -> np.ndarray:
    x=np.asarray(coordinates,dtype=float)
    c=np.asarray(zdot_column,dtype=float)
    if x.ndim!=1 or c.shape!=x.shape or not np.all(np.isfinite(x)) or not np.all(np.isfinite(c)):
        raise ValueError("coordinates and zdot_column must be finite equal-length vectors")
    z=int(z_index)
    if z<0 or z>=len(x):
        raise ValueError("z_index is outside coordinates")
    grad=c*x[z]
    grad=grad.copy()
    grad[z]=float(c@x)
    return grad


def undo_bd_boundary_momentum_shift(momentum_after, *, coordinates, zdot_column, z_index: int=3) -> np.ndarray:
    """Recover momenta before the Y_i Zdot integration-by-parts boundary term.

    With ``F=sum_{i!=z} c_i x_i Z + 1/2 c_z Z^2`` and
    ``L_after=L_before-dF/dt``, the momenta obey
    ``Pi_before = Pi_after + dF/dx``.
    """
    p=np.asarray(momentum_after,dtype=float)
    if p.ndim!=1 or not np.all(np.isfinite(p)):
        raise ValueError("momentum_after must be a finite vector")
    grad=_boundary_gradient(coordinates,zdot_column,z_index=z_index)
    if p.shape!=grad.shape:
        raise ValueError("momentum_after must match coordinate dimension")
    return p+grad


def density_from_phase_momentum(*, momentum_local: float, enthalpy: float, psi: float) -> float:
    """Return delta-rho from p = delta-rho + 3(rho+P) psi."""
    vals=(momentum_local,enthalpy,psi)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("phase-density inputs must be finite")
    if enthalpy<=0.0:
        raise ValueError("enthalpy must be positive")
    return float(momentum_local-3.0*enthalpy*psi)


def reconstruct_dust_observables(
    action: DustCanonicalAction,
    *,
    Y,
    Pi,
    rho_g: float,
    rho_f: float,
    bg: ScalarBackground,
) -> DustObservables:
    """Map canonical phase variables to physical dust density observables.

    ``action.matter_momentum_map`` is already expressed in the final canonical
    variables after the time-dependent BD boundary transformation; therefore
    applying that map performs the required momentum pullback implicitly.
    The explicit ``undo_bd_boundary_momentum_shift`` helper above is retained
    as an independently tested identity/oracle.
    """
    Y=np.asarray(Y,dtype=float); Pi=np.asarray(Pi,dtype=float)
    if Y.shape!=(3,) or Pi.shape!=(3,) or not np.all(np.isfinite(Y)) or not np.all(np.isfinite(Pi)):
        raise ValueError("Y and Pi must be finite length-3 vectors")
    if not (math.isfinite(rho_g) and rho_g>0.0 and math.isfinite(rho_f) and rho_f>0.0):
        raise ValueError("dust background densities must be finite and positive")
    phase=np.concatenate([Y,Pi])
    pmap=np.asarray(action.matter_momentum_map,dtype=float)
    zmap=np.asarray(action.bd_state_map,dtype=float)
    if pmap.shape!=(2,6) or zmap.shape!=(6,):
        raise ValueError("canonical action is missing matter/BD reconstruction maps")

    n=bg.xi*bg.c
    pref_f=n*bg.xi**3
    if not (math.isfinite(pref_f) and pref_f>0.0):
        raise ValueError("f-sector common normalization must be positive")

    p_common=pmap@phase
    Z=float(zmap@phase)
    drg=float(p_common[0])
    p_f_local=float(p_common[1]/pref_f)
    drf=density_from_phase_momentum(
        momentum_local=p_f_local, enthalpy=rho_f, psi=Z,
    )
    dg=drg/rho_g
    df=drf/rho_f

    wg=rho_g
    wf=pref_f*rho_f
    common=(wg*dg+wf*df)/(wg+wf)
    return DustObservables(
        delta_rho_g=drg,
        delta_rho_f=drf,
        delta_g=float(dg),
        delta_f=float(df),
        delta_common=float(common),
        delta_relative=float(dg-df),
    )

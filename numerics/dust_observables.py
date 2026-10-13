"""Pull canonical two-dust phase variables back to physical density contrasts."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.de_felice_dust_physical_action import DustCanonicalAction


@dataclass(frozen=True)
class DustDensityMaps:
    delta_rho_g_map: np.ndarray
    delta_rho_f_map: np.ndarray
    delta_g_map: np.ndarray
    delta_f_map: np.ndarray
    delta_relative_map: np.ndarray


@dataclass(frozen=True)
class DustDensityObservables:
    delta_rho_g: float
    delta_rho_f: float
    delta_g: float
    delta_f: float
    delta_relative: float


def dust_density_maps(
    action: DustCanonicalAction,
    bg: ScalarBackground,
    *,
    rho_g: float,
    rho_f: float,
) -> DustDensityMaps:
    """Return linear maps from canonical ``(Y,Pi)`` to sector densities."""
    if not (math.isfinite(rho_g) and rho_g > 0.0 and math.isfinite(rho_f) and rho_f > 0.0):
        raise ValueError("dust densities must be finite and positive")
    pmap = np.asarray(action.matter_momentum_map, dtype=float)
    zmap = np.asarray(action.bd_state_map, dtype=float)
    if pmap.shape != (2, 6) or zmap.shape != (6,):
        raise ValueError("canonical action is missing valid matter/BD reconstruction maps")
    n = bg.xi * bg.c
    prefactor_f = n * bg.xi**3
    if not (math.isfinite(prefactor_f) and prefactor_f > 0.0):
        raise ValueError("f-sector momentum prefactor must be positive")

    # g-flat gauge has psi_g=0, so p_g=delta rho_g directly. The f-sector
    # common-normalized phase momentum is n*xi^3 times the local momentum
    # p_local=delta rho_f+3 rho_f psi_f, with psi_f=Z in Eq. (72).
    drg = pmap[0].copy()
    drf = pmap[1] / prefactor_f - 3.0 * rho_f * zmap
    dg = drg / rho_g
    df = drf / rho_f
    rel = dg - df
    return DustDensityMaps(
        delta_rho_g_map=np.asarray(drg, dtype=float),
        delta_rho_f_map=np.asarray(drf, dtype=float),
        delta_g_map=np.asarray(dg, dtype=float),
        delta_f_map=np.asarray(df, dtype=float),
        delta_relative_map=np.asarray(rel, dtype=float),
    )


def evaluate_dust_observables(maps: DustDensityMaps, state) -> DustDensityObservables:
    z = np.asarray(state, dtype=float)
    if z.shape != (6,) or not np.all(np.isfinite(z)):
        raise ValueError("canonical state must be a finite length-6 vector")
    drg = float(maps.delta_rho_g_map @ z)
    drf = float(maps.delta_rho_f_map @ z)
    dg = float(maps.delta_g_map @ z)
    df = float(maps.delta_f_map @ z)
    return DustDensityObservables(
        delta_rho_g=drg,
        delta_rho_f=drf,
        delta_g=dg,
        delta_f=df,
        delta_relative=float(dg - df),
    )

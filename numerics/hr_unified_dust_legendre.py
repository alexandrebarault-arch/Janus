"""Exact native Hamiltonian/Legendre controls for two irrotational dust sectors.

Covariant dust action: -rho sqrt(-g)/2 * (g^ab theta_a theta_b+1).
The dust density rho is a Lagrange multiplier, not a second propagating
fluid scalar. The canonical phase pair (theta,p_theta) survives separately
in each metric. This does not by itself eliminate bimetric constraints.
All densities below are per native dT dR dOmega, with spherical angular
metric coefficient g_omegaomega included exactly once.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class DustLegendre:
    lagrangian: np.ndarray
    momentum: np.ndarray
    hamiltonian: np.ndarray
    reduced_hamiltonian: np.ndarray
    stationary_rho: np.ndarray
    native_lapse: np.ndarray
    native_shift: np.ndarray
    spatial_measure: np.ndarray


def native_dust_legendre(metric,rho,theta_T,theta_R):
    """Full unreduced Hamiltonian and rho-eliminated expression for p>0.

    The equality Hamiltonian==reduced_hamiltonian only holds when the
    algebraic density constraint rho==stationary_rho is imposed, e.g.
    for theta_T=N*sqrt(1+gamma^rr theta_R^2)+N^r theta_R.
    """
    if len(metric)!=4:raise ValueError('native spherical metric must have four components')
    gtt,gtr,grr,gang=[np.asarray(x,dtype=float) for x in metric]
    density=np.asarray(rho,dtype=float)
    qt=np.asarray(theta_T,dtype=float)
    qr=np.asarray(theta_R,dtype=float)
    if np.any(grr<=0) or np.any(gang<=0) or np.any(density<=0):
        raise ValueError('spatial metric and dust density must be positive')
    shift=gtr/grr
    lapse_sq=-gtt+gtr*gtr/grr
    if np.any(lapse_sq<=0):raise ValueError('lapse must be positive')
    lapse=np.sqrt(lapse_sq)
    spatial=np.sqrt(grr)*gang
    norm=1+qr*qr/grr
    speed=qt-shift*qr
    p=spatial*density*speed/lapse
    if np.any(p<=0):raise ValueError('future oriented positive dust momentum required')
    L=spatial*density*speed*speed/(2*lapse)-lapse*spatial*density*norm/2
    H=lapse*(p*p/(2*spatial*density)+spatial*density*norm/2)+shift*p*qr
    stationary=p/(spatial*np.sqrt(norm))
    reduced=lapse*p*np.sqrt(norm)+shift*p*qr
    return DustLegendre(L,p,H,reduced,stationary,lapse,shift,spatial)

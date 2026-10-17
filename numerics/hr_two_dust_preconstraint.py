"""Compact preconstraint two-dust phase Hessian + native HR interaction.

This is a *partial*, time-local Galerkin action: it adds both exact-dust
canonical phase PAIRS to the already audited finite-mu HR interaction.
It deliberately does not include Einstein-Hilbert, the metric constraints,
a background-on-shell proof, or a physical propagation verdict.

Order:
 [0:16] HR native sampling compact amplitudes and rate slots;
 [16:22] (Y_g,p_g,Y_f,p_f,Y_gdot,Y_fdot).

The f material scalar is q_f_native = (Y_f - T) F. This is the
first-order time-Stueckelberg phase relation (Y2-T), not an independent
extra fluid scalar. Its derivatives are taken through the FULL inverse
background chart J^-T. The p_g/p_f slots stay canonical.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

from numerics.hr_compact_radial_interaction import compact_scalar_profile
from numerics.hr_native_sampling_compact import (
    SAMPLED_COMPACT_ORDER, integrate_sampled_compact_hr_interaction,
)

PRECONSTRAINT_ORDER = SAMPLED_COMPACT_ORDER + (
    "Y_g","p_g","Y_f","p_f","Y_g_dot","Y_f_dot"
)


@dataclass(frozen=True)
class TwoDustPreconstraint:
    hessian: np.ndarray
    gradient: np.ndarray
    interaction_hessian: np.ndarray
    dust_hessian: np.ndarray
    radius: float
    quadrature_order: int
    order: tuple[str,...] = PRECONSTRAINT_ORDER


def _e(index):
    v=np.zeros(22)
    v[index]=1.
    return v


def _sym(a,b):
    return np.outer(a,b)+np.outer(b,a)


def _dust_kernel(*,rho,lapse,scale,measure,momentum,phase,phase_rate,
                 phase_radial,Phi,shift,log_phidot_rate):
    """Native quadratic dust phase Hessian with measure already included."""
    z=phase_rate+log_phidot_rate*phase-Phi
    spatial=phase_radial+(scale/lapse)*shift
    return measure*(
        _sym(momentum,z)+rho*np.outer(Phi,Phi)
        -(lapse*lapse*rho/(scale*scale))*np.outer(spatial,spatial)
    )


def two_dust_phase_compact_hessian(*,radius,quadrature_order=24,
        a_g,n_g,rho_g,a_f,n_f,rho_f,
        mu,mu_dot,sigma,sigma_dot,
        log_phidot_rate_g=0.,log_phidot_rate_f=0.):
    """Time-instantaneous spatial 4pi integral of TWO canonical dust actions.

    n_g,a_g and n_f,a_f are native lapse/scale at this frozen instant.
    The HR code calls the f variables (n,alpha) rather than (n_f,a_f).
    No background drift of the metric is implicitly invented here.
    """
    vals=(radius,a_g,n_g,rho_g,a_f,n_f,rho_f,mu,mu_dot,sigma,
          sigma_dot,log_phidot_rate_g,log_phidot_rate_f)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("dust inputs must be finite")
    if min(radius,a_g,n_g,a_f,n_f,rho_g,rho_f)<=0 or mu<=-1:
        raise ValueError("require positive scales/densities and mu>-1")
    if type(quadrature_order) is not int or quadrature_order<8:
        raise ValueError("quadrature_order must be integer >= 8")

    points,weights=np.polynomial.legendre.leggauss(quadrature_order)
    H=np.zeros((22,22))
    for z,w in zip(points,weights):
        r=.5*radius*(z+1.)
        F,Fr,_,_=compact_scalar_profile(r,radius)
        Tt=1.+.5*sigma_dot*r*r
        Tr=sigma*r
        Rt=mu_dot*r
        Rr=1.+mu
        D=Tt*Rr-Tr*Rt
        if D<=0:
            raise ValueError("f native chart lost positive orientation")
        native_r=Rr*r
        quad=2.*math.pi*radius*w
        phase_g=F*_e(16)
        p_g=F*_e(17)
        rate_g=F*_e(20)
        rad_g=Fr*_e(16)
        phi_g=F*_e(0)
        shift_g=Fr*_e(1)
        Hg=_dust_kernel(
            rho=rho_g,lapse=n_g,scale=a_g,
            measure=n_g*a_g**3*r*r,
            momentum=p_g,phase=phase_g,phase_rate=rate_g,
            phase_radial=rad_g,Phi=phi_g,shift=shift_g,
            log_phidot_rate=log_phidot_rate_g)

        # q_f^native = Y_f - T, with f-native gradients J^-T.
        phase_f=F*(_e(18)-_e(8))
        p_f=F*_e(19)
        rate_common=F*(_e(21)-_e(10))
        rad_common=Fr*(_e(18)-_e(8))
        rate_native=(Rr*rate_common-Rt*rad_common)/D
        radial_native=(-Tr*rate_common+Tt*rad_common)/D
        phi_f=F*_e(4)
        shift_f=Fr*_e(5)
        Hf=_dust_kernel(
            rho=rho_f,lapse=n_f,scale=a_f,
            measure=D*n_f*a_f**3*native_r*native_r,
            momentum=p_f,phase=phase_f,phase_rate=rate_native,
            phase_radial=radial_native,Phi=phi_f,shift=shift_f,
            log_phidot_rate=log_phidot_rate_f)
        H+=quad*(Hg+Hf)
    return .5*(H+H.T)


def assemble_hr_two_dust_preconstraint(*,radius,quadrature_order=24,
        rho_g,rho_f,log_phidot_rate_g=0.,log_phidot_rate_f=0.,
        **hr_parameters)->TwoDustPreconstraint:
    """Combine exact finite-mu *interaction* and the two dust phase blocks.

    Positive EH kinetic terms are NOT included; metric amplitudes have not
    been eliminated. Do not diagonalize this unreduced Hessian as a
    physical stability operator.
    """
    required=("N","a","n","alpha","mu","mu_dot","sigma_r","sigma_dot")
    if not all(x in hr_parameters for x in required):
        raise ValueError("HR background must contain both native metrics/chart")
    dust=two_dust_phase_compact_hessian(
        radius=radius,quadrature_order=quadrature_order,
        a_g=hr_parameters["a"],n_g=hr_parameters["N"],rho_g=rho_g,
        a_f=hr_parameters["alpha"],n_f=hr_parameters["n"],rho_f=rho_f,
        mu=hr_parameters["mu"],mu_dot=hr_parameters["mu_dot"],
        sigma=hr_parameters["sigma_r"],sigma_dot=hr_parameters["sigma_dot"],
        log_phidot_rate_g=log_phidot_rate_g,
        log_phidot_rate_f=log_phidot_rate_f)
    native=integrate_sampled_compact_hr_interaction(
        radius=radius,quadrature_order=quadrature_order,**hr_parameters)
    Hint=np.zeros((22,22))
    Hint[:16,:16]=native.hessian
    H=.5*(Hint+dust+Hint.T+dust.T)
    g=np.zeros(22)
    g[:16]=native.gradient
    return TwoDustPreconstraint(
        hessian=H,gradient=g,interaction_hessian=Hint,dust_hessian=dust,
        radius=float(radius),quadrature_order=quadrature_order)

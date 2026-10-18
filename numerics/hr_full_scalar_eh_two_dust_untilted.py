"""Strict untilted native scalar EH + finite-mu HR + TWO dust interface.

Geometric restrictions: sigma=sigma_dot=mu_dot=0, constant mu>-1,
T=t, R_f=(1+mu)r. All *native* EH scalar trace/shear variables are
included in the 24-vector, but physical nonhomothetic chart perturbations
in EH, full time dynamics, metric/BD reduction remain OPEN.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_full_scalar_eh_homothetic import integrate_untilted_native_scalar_eh

@dataclass(frozen=True)
class UntilitedEHHRDust:
    hessian: np.ndarray
    gradient: np.ndarray
    eh_hessian: np.ndarray
    hr_hessian: np.ndarray
    dust_hessian: np.ndarray
    amplitude_order: tuple[str,...]


def assemble_untilted_scalar_eh_hr_two_dust(*,radius,quadrature_order=24,
        rho_g,rho_f,g_scale_rate,planck_ratio=1.,
        log_phidot_rate_g=0.,log_phidot_rate_f=0.,**hr_parameters):
    """Do not infer dynamics from eigenvalues of this finite-radial 24x24 jet.

    The EH scalar sector is complete for each of the two given native
    spherical metrics, but relative f chart-perturbation EH variations
    and the time-dependent background are NOT part of this frozen gate.
    """
    for key in ('N','a','n','alpha','k','mu','mu_dot','sigma_r','sigma_dot'):
        if key not in hr_parameters:
            raise ValueError(f'missing background scalar {key}')
    for key in ('mu_dot','sigma_r','sigma_dot'):
        if not math.isclose(float(hr_parameters[key]),0.,rel_tol=0.,abs_tol=1e-14):
            raise ValueError('full scalar EH gate only supports untilted constant radial chart')
    from numerics.hr_two_dust_preconstraint import (assemble_hr_two_dust_preconstraint,PRECONSTRAINT_ORDER)
    partial=assemble_hr_two_dust_preconstraint(
        radius=radius,quadrature_order=quadrature_order,rho_g=rho_g,rho_f=rho_f,
        log_phidot_rate_g=log_phidot_rate_g,
        log_phidot_rate_f=log_phidot_rate_f,**hr_parameters)
    eh=integrate_untilted_native_scalar_eh(radius=radius,
        quadrature_order=quadrature_order,k=hr_parameters['k'],
        N=hr_parameters['N'],a=hr_parameters['a'],a_rate=g_scale_rate,
        n=hr_parameters['n'],alpha=hr_parameters['alpha'],
        alpha_rate=hr_parameters.get('alpha_dot',0.),
        mu=hr_parameters['mu'],planck_ratio=planck_ratio)
    H=np.zeros((24,24));G=np.zeros(24)
    H[:22,:22]=partial.hessian
    G[:22]=partial.gradient
    H+=eh.hessian
    G+=eh.gradient
    hi=np.zeros_like(H);hi[:22,:22]=partial.interaction_hessian
    hd=np.zeros_like(H);hd[:22,:22]=partial.dust_hessian
    if not np.allclose(H,H.T,rtol=0,atol=1e-11):
        raise ArithmeticError('combined native scalar action is not symmetric')
    return UntilitedEHHRDust(.5*(H+H.T),G,eh.hessian,hi,hd,
                 tuple(PRECONSTRAINT_ORDER)+('psi_g_dot','E_g_dot'))

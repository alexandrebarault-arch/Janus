"""Full six-amplitude (2 chart+4 native metric) EH spacetime quadratic test.

The function differentiates the *exact nonlinear native ADM+GHY action*
under compact interior coordinate deformations and native scalar fields.
It is an action-level Hessian before metric/BD constraints. Pure relative
chart directions must disappear from native f-EH after exact time/radial
integration: they are compact diffeomorphism reparametrizations, not new
EH propagating fields. The HR interaction is not included.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_eh_full_scalar_chart_ward import full_scalar_spacetime_action

QUADRATIC_ORDER=('deltaT','deltaR','Phi_f','U_f','psi_f','E_f')

@dataclass(frozen=True)
class EHChartQuadratic:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    steps: np.ndarray
    order: tuple[str,...] = QUADRATIC_ORDER


def full_scalar_eh_chart_quadratic(*,time_radius=.4,radial_radius=.6,
        quadrature_order=42,chart_step=.003,field_step=.004,
        freeze_native_sampling=False):
    """Return 6x6 second variation of the full spacetime f-EH action.

    Frozen sampling is an explicitly WRONG, noncovariant negative control.
    Keep field amplitudes independent and native, not a common-chart gauge.
    """
    ss=np.array([chart_step,chart_step]+[field_step]*4,float)
    if not np.all(np.isfinite(ss)) or np.any(ss<=0):
        raise ValueError('positive finite finite-difference steps required')
    def eval_x(x):
        return full_scalar_spacetime_action(
            eps_time=float(x[0]),eps_radial=float(x[1]),
            amplitudes=tuple(float(v) for v in x[2:]),
            freeze_native_sampling=freeze_native_sampling,
            time_radius=time_radius,radial_radius=radial_radius,
            quadrature_order=quadrature_order)
    z=np.zeros(6); f0=eval_x(z);h=np.zeros((6,6));g=np.zeros(6)
    for i in range(6):
        p=np.zeros(6);p[i]=ss[i]
        plus=eval_x(p);minus=eval_x(-p)
        g[i]=(plus-minus)/(2*ss[i])
        h[i,i]=(plus-2*f0+minus)/ss[i]**2
        for j in range(i+1,6):
            q=np.zeros(6);q[j]=ss[j]
            h[i,j]=h[j,i]=(eval_x(p+q)-eval_x(p-q)
                              -eval_x(-p+q)+eval_x(-p-q))/(4*ss[i]*ss[j])
    return EHChartQuadratic(float(f0),g,.5*(h+h.T),ss)


def native_eh_metric_quadratic_in_deformed_chart(*,eps_time,eps_radial,
        time_radius=.4,radial_radius=.6,quadrature_order=42,step=.003):
    """Four native scalar field Hessian at any finite compact chart shift.

    A true change of variables preserves the metric-field Hessian as well
    as the action, not just its first-order chart Ward identity.
    """
    if not math.isfinite(step) or step<=0:
        raise ValueError('positive field difference step required')
    def ff(x):
        return full_scalar_spacetime_action(
            amplitudes=x,eps_time=eps_time,eps_radial=eps_radial,
            time_radius=time_radius,radial_radius=radial_radius,
            quadrature_order=quadrature_order)
    z=np.zeros(4);f0=ff(z);out=np.zeros((4,4))
    for i in range(4):
        e=np.zeros(4);e[i]=step
        out[i,i]=(ff(e)+ff(-e)-2*f0)/step**2
        for j in range(i+1,4):
            d=np.zeros(4);d[j]=step
            out[i,j]=out[j,i]=(ff(e+d)-ff(e-d)-ff(-e+d)+ff(-e-d))/(4*step**2)
    return out

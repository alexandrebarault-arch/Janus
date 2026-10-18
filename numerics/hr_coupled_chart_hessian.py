"""Common/relative four chart-amplitude HR Hessian and off-shell Ward caution.

No on-shell background equations are imposed. Thus the diagonal coordinate
paths are EXACTLY invariant, but their tangent vectors need not be Hessian
null eigenvectors at an off-shell point with a nonlinear gauge-orbit chart.
Treating the off-shell mixed Hessian as a dynamical kinetic matrix is invalid.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_coupled_diagonal_ward import (
    BETAS,_quad,_bump,_native_chart,_native_metric,_pull,_interaction_density,
)

ORDER=('g_time_chart','g_radial_chart','f_time_chart','f_radial_chart')

@dataclass(frozen=True)
class CoupledChartHessian:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    amplitude_order: tuple[str,...]=ORDER


def coupled_hr_independent_chart_action(*,chart=(0.,0.,0.,0.),
        betas=BETAS,g_fields=(.012,-.014,.016,.009),
        f_fields=(-.017,.013,-.011,.008),
        time_radius=.4,radial_radius=.6,quadrature_order=38):
    vec=np.asarray(chart,float)
    if vec.shape!=(4,) or not np.all(np.isfinite(vec)):
        raise ValueError('four finite independent chart amplitudes required')
    bs=tuple(betas)
    if len(bs)!=5 or not all(math.isfinite(float(b)) for b in bs):
        raise ValueError('five finite interaction coefficients required')
    t,r,w=_quad(time_radius,radial_radius,quadrature_order)
    b,bt,br,c,ct,cr=_bump(t,r,time_radius,radial_radius)
    # g is pulled back from common g-native coordinates (u_g,v_g)
    egT,egR,efT,efR=vec
    u=t+egT*b;v=r+egR*c
    g00=1+egT*bt;g01=egT*br
    g10=egR*ct;g11=1+egR*cr
    if np.min(g00*g11-g01*g10)<=0 or np.min(v)<=0:
        raise ValueError('nonregular common g chart')
    gm=_pull(_native_metric(u,v,'g',g_fields),g00,g01,g10,g11)
    # f-native time/radius background map is composed with its own
    # independently varied common chart (u_f,v_f).
    uf=t+efT*b;vf=r+efR*c
    fu00=1+efT*bt;fu01=efT*br
    fu10=efR*ct;fu11=1+efR*cr
    T,R,Tt,Tr,Rt,Rr=_native_chart(uf,vf)
    f00=Tt*fu00+Tr*fu10
    f01=Tt*fu01+Tr*fu11
    f10=Rt*fu00+Rr*fu10
    f11=Rt*fu01+Rr*fu11
    if np.min(f00*f11-f01*f10)<=0 or np.min(R)<=0:
        raise ValueError('nonregular f chart')
    fm=_pull(_native_metric(T,R,'f',f_fields),f00,f01,f10,f11)
    return float(np.sum(w*_interaction_density(gm,fm,bs)))


def coupled_hr_independent_chart_hessian(*,step=.003,quadrature_order=40,
                                           **kwargs):
    if not math.isfinite(step) or step<=0:
        raise ValueError('positive finite difference step required')
    def S(x):return coupled_hr_independent_chart_action(chart=x,
                          quadrature_order=quadrature_order,**kwargs)
    z=np.zeros(4);s0=S(z);H=np.zeros((4,4));grad=np.zeros(4)
    for i in range(4):
        e=np.zeros(4);e[i]=step
        grad[i]=(S(e)-S(-e))/(2*step)
        H[i,i]=(S(e)-2*s0+S(-e))/step**2
        for j in range(i+1,4):
            f=np.zeros(4);f[j]=step
            H[i,j]=H[j,i]=(S(e+f)-S(e-f)-S(-e+f)+S(-e-f))/(4*step**2)
    return CoupledChartHessian(s0,grad,H)

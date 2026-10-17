"""Independent beta4 spacetime Ward audit using the native HR 22-jet.

Crosschecks the *existing* Hessian (14x14 native metric+chart, promoted to
22x22 with f-field sampling) against the beta4 volume's separate exact
change-of-variables/total-divergence calculation. This is interaction only.

The q variation is an f-native lapse scalar perturbation q(T,R), not a
common-chart scalar held frozen under independent coordinate variations.
The perturbations of the background coordinate map vanish on every outer
boundary of the spacetime cylinder, including the radial boundary.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_beta4_spacetime_ward import _mesh, _background, _shift_fields
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet
from numerics.hr_native_field_sampling import add_native_field_sampling


@dataclass(frozen=True)
class NativeBeta4Ward:
    mixed_complete: np.ndarray
    mixed_frozen_sampling: np.ndarray
    mixed_sampling_contribution: np.ndarray
    jacobian_min: float
    quadrature_order: int
    native_field: str


def native_beta4_mixed_ward(*,time_radius=.4,radial_radius=.6,order=32,
                            native_field="lapse"):
    """Calculate mixed (chart deformation, f-native lapse) derivatives.

    The action normalization is m^2 Mg^2 = 1, beta4=1, with the native
    HR interaction sign L_int = -sqrt(-g)*sum beta_n e_n. Thus compare
    with MINUS the positive beta4 volume Ward coefficients.
    """
    native_fields={"lapse":4,"shift":5,"trace":6,"shear":7}
    if native_field not in native_fields:
        raise ValueError("unknown native f metric mode")
    idx=native_fields[native_field]
    deriv_idx=idx-4
    t,r,weights=_mesh(time_radius,radial_radius,order)
    complete=np.zeros(2)
    frozen=np.zeros(2)
    sampling=np.zeros(2)
    jac_min=float('inf')
    for i in range(order):
        ti=float(t[i,0]);sigma=.08+.025*ti;mu=-.22+.05*ti
        n=1+.05*ti+.03*ti*ti
        alpha=1+.02*ti+.015*ti*ti
        n_dot=.05+.06*ti
        alpha_dot=.02+.03*ti
        for j in range(order):
            ri=float(r[0,j])
            T=ti+.5*sigma*ri*ri
            R=(1+mu)*ri
            native=native_hr_stueckelberg_jet(
                N=1.,a=1.,n=n,alpha=alpha,k=1.,m2=1.,Mg2=1.,
                betas=(0.,0.,0.,0.,1.),mu=mu,r=ri,
                sigma_r=sigma,sigma_dot=.025,mu_dot=.05,
                n_dot=n_dot,alpha_dot=alpha_dot,
                n_ddot=.06,alpha_ddot=.03,
            )
            sampled=add_native_field_sampling(native,r=ri)
            jac_min=min(jac_min,float(np.linalg.det(native.radial_jacobian)))
            # f-native lapse perturbation q(T,R), with TRUE native derivatives.
            q=1+.45*T+.30*R*R+.20*T*R*R
            q_T=.45+.20*R*R
            q_R=(.60+.40*T)*R
            v=np.zeros(22)
            v[idx]=q;v[14+deriv_idx]=q_T;v[18+deriv_idx]=q_R
            vf=v.copy();vf[14+deriv_idx]=vf[18+deriv_idx]=0
            for mode_index,kind in enumerate(('time','radial')):
                dT,dR,dTt,dTr,dRt,dRr=_shift_fields(
                    t[i:i+1,:1],r[:1,j:j+1],time_radius,radial_radius,kind
                )
                disp=np.zeros(22)
                disp[8]=dT[0,0];disp[9]=dTt[0,0]
                disp[10]=dTr[0,0];disp[11]=dRt[0,0]
                disp[12]=dRr[0,0];disp[13]=dR[0,0]/ri
                # Local jet density is per unit dOmega after r^2 factoring.
                # weights from _mesh already contain 4*pi*dt*dr.
                weight=float(weights[i,j])*ri*ri
                complete[mode_index]+=weight*(v@sampled.hessian@disp)
                frozen[mode_index]+=weight*(vf@sampled.hessian@disp)
                sampling[mode_index]+=weight*((v-vf)@sampled.hessian@disp)
    return NativeBeta4Ward(
        mixed_complete=complete,mixed_frozen_sampling=frozen,
        mixed_sampling_contribution=sampling,
        jacobian_min=jac_min,quadrature_order=order,
        native_field=native_field,
    )

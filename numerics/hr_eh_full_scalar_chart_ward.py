"""Full native spherical scalar ADM action pulled through a finite 2D chart.

Kinematic diffeomorphism/change-of-variables benchmark only. The ADM+GHY
representative is evaluated in the *native* foliation T=const; its scalar
volume density is subsequently pulled into common (t,r) coordinates with the
exact 2D Jacobian. This DOES NOT supply the second-order chart-perturbation
Hessian for the coupled HR+EH+two-dust action or validate on-shell dynamics.

Native fields: independent lapse Phi, radial shift U, spatial isotropic
trace psi, and trace-free scalar shear E, all with explicit native radial
and temporal derivative samples. A deliberate frozen-field option is a
negative control: it loses the native field advection and violates the
compact diffeomorphism Ward identity.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_eh_spacetime_ward import _quadrature, _chart, _shapes

FIELD_NAMES = ('lapse', 'shift', 'trace', 'shear')

@dataclass(frozen=True)
class FullScalarChartWard:
    full_mixed: np.ndarray
    frozen_mixed: np.ndarray
    chart_min_determinant: float
    baseline_actions: np.ndarray
    quadrature_order: int


def native_fields(T, R, amplitudes):
    """Smooth regular native fields and all spatial/time derivatives.

    Arrays of T and R must broadcast. Individual amplitudes correspond to
    Phi, U, psi, E. U=O(R) at the origin, E=O(R²) so Qr=Qt there.
    """
    amps = np.asarray(amplitudes, dtype=float)
    if amps.shape != (4,) or not np.all(np.isfinite(amps)):
        raise ValueError('four finite native metric amplitudes required')
    T, R = np.broadcast_arrays(np.asarray(T, float), np.asarray(R, float))
    if not np.all(np.isfinite(T)) or not np.all(np.isfinite(R)) or np.any(R<=0):
        raise ValueError('finite time and positive native radius required')
    phi = amps[0] * (1 + .27*T + (.08+.02*T)*R**2)
    shift = amps[1] * R * (1 + .16*T + .07*R**2)
    ur = amps[1] * (1 + .16*T + .21*R**2)
    psi = amps[2] * (1 + .21*T + (.11+.02*T)*R**2)
    psir = amps[2] * ( .22+.04*T)*R
    psirr = amps[2] * (.22+.04*T) * np.ones_like(R)
    psit = amps[2] * (.21+.02*R**2)
    shear = amps[3] * R**2 * (1+.13*T+.05*R**2)
    er = amps[3] * (2*(1+.13*T)*R + .20*R**3)
    err = amps[3] * (2*(1+.13*T) + .60*R**2)
    et = amps[3] * (.13*R**2)
    return (phi,shift,ur,psi,psir,psirr,psit,shear,er,err,et)


def native_adm_from_field_samples(T, R, samples, *, k=1.7):
    """Exact nonlinear native ADM density from independent scalar field jets.

    Public oracle interface: samples=(Phi,U,U_R,psi,psi_R,psi_RR,
    psi_T,E,E_R,E_RR,E_T), supplied in the NATIVE chart. With one compact
    radial harmonic basis this can be tested independently against the
    earlier analytic six-variable spherical ADM Hessian.
    """
    T,R=np.broadcast_arrays(np.asarray(T,float),np.asarray(R,float))
    if not math.isfinite(float(k)) or k<=0 or np.any(R<=0):
        raise ValueError('invalid native chart or k')
    if len(samples)!=11: raise ValueError('eleven native scalar samples required')
    phi,U,Ur,psi,psir,psirr,psit,E,Er,Err,Et=samples
    a=1+.15*T+.035*T*T
    adot=.15+.07*T
    n=1+.08*T+.02*T*T
    Qr=1+2*psi-2*k*k*E/3
    Qt=1+2*psi+k*k*E/3
    qr=2*psir-2*k*k*Er/3
    qt=2*psir+k*k*Er/3
    qtt=2*psirr+k*k*Err/3
    qrdot=2*psit-2*k*k*Et/3
    qtdot=2*psit+k*k*Et/3
    lapse_sq=1+2*phi+U*U/Qr
    if np.any(a<=0) or np.any(n<=0) or np.any(Qr<=0) or np.any(Qt<=0) or np.any(lapse_sq<=0):
        raise ValueError('non-Lorentzian native metric trial amplitude')
    N=n*np.sqrt(lapse_sq)
    L=a*np.sqrt(Qr)
    S=a*R*np.sqrt(Qt)
    Z=1+R*qt/(2*Qt)
    W=np.sqrt(Qt/Qr)*Z
    Wprime=np.sqrt(Qt/Qr)*(
        (qt/Qt-qr/Qr)*Z/2 + qt/(2*Qt) + R*(qtt/Qt-(qt/Qt)**2)/2
    )
    R3=2/S**2*(1-W*W-2*(S/L)*Wprime)
    radial_shift = (n/a)*U/Qr
    radial_shift_prime=(n/a)*(Ur/Qr-U*qr/(Qr*Qr))
    kr=(adot/a+qrdot/(2*Qr)-radial_shift_prime-radial_shift*qr/(2*Qr))/N
    kt=(adot/a+qtdot/(2*Qt)-radial_shift*(1/R+qt/(2*Qt)))/N
    density=.5*N*L*S*S*(R3-4*kr*kt-2*kt*kt)
    if not np.all(np.isfinite(density)):
        raise ArithmeticError('nonfinite full-scalar ADM density')
    return density


def native_full_scalar_adm_density(T,R,amplitudes,*,sample_at=None,k=1.7):
    """Native spherical ADM+GHY density sampled at moved f coordinates.

    When sample_at is supplied, the field AND all its native derivatives
    are intentionally frozen at the baseline coordinates, which is an
    intentionally NONcovariant negative control.
    """
    T,R = np.broadcast_arrays(np.asarray(T,float),np.asarray(R,float))
    Ts,Rs=(T,R) if sample_at is None else np.broadcast_arrays(*sample_at)
    samples=native_fields(Ts,Rs,amplitudes)
    return native_adm_from_field_samples(T,R,samples,k=k)


def full_scalar_spacetime_action(*,amplitudes=(0.,0.,0.,0.),
        eps_time=0.,eps_radial=0.,freeze_native_sampling=False,
        time_radius=.4,radial_radius=.6,quadrature_order=38):
    """Integrate exact native ADM density times d(T,R)/d(t,r), with 4pi.

    The f native outer boundary is held fixed by compact eps profiles;
    the nonlinear T,R image domain is consequently unchanged.
    """
    if not all(math.isfinite(float(v)) for v in (eps_time,eps_radial)):
        raise ValueError('finite chart displacements required')
    t,r,w=_quadrature(time_radius,radial_radius,quadrature_order)
    T0,R0,Tt,Tr,Rt,Rr,_=_chart(t,r)
    temporal,radial=_shapes(t,r,time_radius,radial_radius)
    et=float(eps_time);er=float(eps_radial)
    T=T0+et*temporal[0]
    R=R0+er*radial[1]
    Dt=Tt+et*temporal[2]
    Dr=Tr+et*temporal[3]
    Et=Rt+er*radial[4]
    Er=Rr+er*radial[5]
    D=Dt*Er-Dr*Et
    if np.min(D)<=0 or np.min(R)<=0:
        raise ValueError('orientation or native radial chart is not regular')
    sample=(T0,R0) if freeze_native_sampling else None
    dens=native_full_scalar_adm_density(T,R,amplitudes,sample_at=sample)
    return float(np.sum(w*D*dens))


def full_scalar_chart_ward(*,time_radius=.4,radial_radius=.6,
                            quadrature_order=42,eps=0.002,field_step=0.002):
    """Finite-difference Ward variations in both charts x all four modes.

    At eps=field_step=0 the exact mixed derivative vanishes by compact
    coordinate invariance. Each frozen-sampling result is a negative control.
    """
    if not (math.isfinite(eps) and math.isfinite(field_step) and eps>0 and field_step>0):
        raise ValueError('positive finite variation steps required')
    t,r,_=_quadrature(time_radius,radial_radius,quadrature_order)
    J=_chart(t,r)[-1]
    full=np.empty((4,2));frozen=np.empty((4,2));baseline=np.empty(4)
    for mode in range(4):
        base=np.zeros(4)
        base[mode]=field_step
        baseline[mode]=full_scalar_spacetime_action(
            amplitudes=base,time_radius=time_radius,radial_radius=radial_radius,
            quadrature_order=quadrature_order)
        for which in range(2):
            for freeze,dest in ((False,full),(True,frozen)):
                vals=[]
                for e,v in ((eps,field_step),(eps,-field_step),
                            (-eps,field_step),(-eps,-field_step)):
                    amps=np.zeros(4);amps[mode]=v
                    vals.append(full_scalar_spacetime_action(
                        amplitudes=amps,eps_time=e if which==0 else 0.,
                        eps_radial=e if which==1 else 0.,
                        freeze_native_sampling=freeze,time_radius=time_radius,
                        radial_radius=radial_radius,quadrature_order=quadrature_order))
                dest[mode,which]=(vals[0]-vals[1]-vals[2]+vals[3])/(4*eps*field_step)
    return FullScalarChartWard(full,frozen,float(np.min(J)),baseline,quadrature_order)

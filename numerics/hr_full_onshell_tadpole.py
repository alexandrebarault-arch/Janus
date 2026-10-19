"""Full common-chart spherical ADM+HR+two-dust 12-direction tadpole gate.

This is a *real physical perturbation* of both common-chart metrics on an
on-shell HOMOGENEOUS dust-only Candidate-C background, NOT an independent
nonhomothetic solution. The pure-chart f-native version is reconstructed by
pullback if needed. EH uses a positive ADM+GHY representative for both metrics.

All fields are varied independently BEFORE applying dust proper-time/norm
constraints. No physical BD reduction, scalar eigenvalues, or fold claim.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from scipy.integrate import solve_ivp

BETAS=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
M2=23.3348939346
MG2=1.
MF2=.10879548725**2
CG=.9
Y0=.5568825591873054
CF=3*.23958426762*Y0**3
ORDER=('Phi_g','U_g','psi_g','E_g','theta_g','rho_g',
       'Phi_f','U_f','psi_f','E_f','theta_f','rho_f')


def background(a):
    """Dust-only Candidate-C homogeneous 2-metric on-shell point."""
    if not math.isfinite(a) or not .22<a<.66:raise ValueError('a outside control support')
    b0,b1,b2,b3,b4=BETAS
    c=np.array([MF2*M2*b3/3,MF2*M2*b2-M2*b4/3,
                MF2*M2*b1-M2*b3,MF2*CG/(3*a**3)-M2*b2,
                -CF/(3*a**3)-M2*b1/3])
    roots=np.roots(c)
    y=min((x.real for x in roots if abs(x.imag)<1e-9 and x.real>0),
          key=lambda x:abs(x.real-Y0))
    py=np.polyval(np.polyder(c),y)
    pn=-MF2*CG*y/a**3+CF/a**3
    yn=-pn/py
    V=b0+3*b1*y+3*b2*y*y+b3*y**3
    E2=CG/(3*a**3)+M2*V/3
    nf=y+yn
    if E2<=0 or nf<=0:raise ValueError('non-Lorentzian background branch')
    H=math.sqrt(E2)
    return (a,a*y,a*H,nf*a*H,nf,CG/a**3,CF/(a*y)**3)


@dataclass(frozen=True)
class Trajectory:
    forward:object
    backward:object
    width:float

    @classmethod
    def solve(cls,a0=.4,width=.04):
        if not .26<a0<.55 or not 0<width<=.05:raise ValueError('invalid trajectory interval')
        def rhs(t,z):
            a,b,ad,bd,nf,rhog,rhof=background(float(z[0]))
            return [ad]
        f=solve_ivp(rhs,(0.,width),[a0],rtol=3e-12,atol=1e-14,dense_output=True)
        b=solve_ivp(rhs,(0.,-width),[a0],rtol=3e-12,atol=1e-14,dense_output=True)
        if not (f.success and b.success):raise RuntimeError('background IVP failed')
        return cls(f.sol,b.sol,width)

    def at(self,t):
        if not math.isfinite(t) or abs(t)>self.width:raise ValueError('time out of background IVP')
        a=float((self.forward if t>=0 else self.backward)(t)[0])
        return background(a)


def profile(t,r,time_radius,radial_radius):
    if not(0<time_radius and 0<radial_radius):raise ValueError('positive support')
    tq=1-(t/time_radius)**2;rq=1-(r/radial_radius)**2
    T=tq**4;Tr=-8*t/time_radius**2*tq**3
    F=rq**4;Fr=-8*r/radial_radius**2*rq**3
    Frr=-8/radial_radius**2*rq**3+48*r*r/radial_radius**4*rq**2
    return T,Tr,F,Fr,Frr


def sector_density(*,scale,scale_rate,lapse,rho0,amp,t,r,time_radius,radial_radius,planck,k=1.7):
    """EH+covariant dust at quadratic/nonlinear metric values per solid angle.

    Output: gravitational density, matter density, native 2x2 metric,
    angular component, intrinsic R3 (for separate physical-deformation test).
    """
    amp=np.asarray(amp,float)
    if amp.shape!=(6,) or not np.all(np.isfinite(amp)) or planck<=0 or k<=0:
        raise ValueError('six finite field amplitudes and positive coefficients')
    T,Tr,F,Fr,Frr=profile(t,r,time_radius,radial_radius)
    p,u,s,e,theta,dens=amp
    phi=p*T*F
    U=u*T*r*F
    Ur=u*T*(F+r*Fr)
    psi=s*T*F;psir=s*T*Fr;psirr=s*T*Frr;psit=s*Tr*F
    E=e*T*r*r*F;Er=e*T*(2*r*F+r*r*Fr)
    Err=e*T*(2*F+4*r*Fr+r*r*Frr)
    Et=e*Tr*r*r*F
    qr=1+2*psi-2*k*k*E/3
    qt=1+2*psi+k*k*E/3
    qr_r=2*psir-2*k*k*Er/3
    qt_r=2*psir+k*k*Er/3
    qt_rr=2*psirr+k*k*Err/3
    qr_t=2*psit-2*k*k*Et/3
    qt_t=2*psit+k*k*Et/3
    lapse_sq=1+2*phi+U*U/qr
    if np.any(qr<=0) or np.any(qt<=0) or np.any(lapse_sq<=0):
        raise ValueError('metric scalar sector left real Lorentzian branch')
    N=lapse*np.sqrt(lapse_sq)
    L=scale*np.sqrt(qr)
    S=scale*r*np.sqrt(qt)
    z=1+r*qt_r/(2*qt)
    w=np.sqrt(qt/qr)*z
    wr=np.sqrt(qt/qr)*((qt_r/qt-qr_r/qr)*z/2
                     +qt_r/(2*qt)+r*(qt_rr/qt-(qt_r/qt)**2)/2)
    R3=2/S**2*(1-w*w-2*(S/L)*wr)
    shift=(lapse/scale)*U/qr
    shiftr=(lapse/scale)*(Ur/qr-U*qr_r/(qr*qr))
    Kr=(scale_rate/scale+qr_t/(2*qr)-shiftr-shift*qr_r/(2*qr))/N
    Kt=(scale_rate/scale+qt_t/(2*qt)-shift*(1/r+qt_r/(2*qt)))/N
    eh=.5*planck*N*L*S*S*(R3-4*Kr*Kt-2*Kt*Kt)
    theta_t=lapse+theta*Tr*F
    theta_r=theta*T*Fr
    rho=rho0*(1+dens*T*F)
    if np.any(rho<=0):raise ValueError('negative dust multiplier density')
    dust=.5*rho*N*L*S*S*((theta_t-shift*theta_r)**2/N**2
                          -theta_r**2/L**2-1)
    g00=-lapse**2*(1+2*phi)
    g01=lapse*scale*U
    g11=scale**2*qr
    area=scale**2*r*r*qt
    return eh,dust,(g00,g01,g11),area,R3


def hr_density(g,f,garea,farea,m2=M2,mg2=MG2,betas=BETAS):
    g00,g01,g11=g;f00,f01,f11=f
    dg=g00*g11-g01*g01;df=f00*f11-f01*f01
    if np.any(dg>=0) or np.any(df>=0) or np.any(garea<=0) or np.any(farea<=0):
        raise ValueError('bad HR Lorentzian metric')
    s=np.sqrt(df/dg)
    tsq=(g11*f00+g00*f11-2*g01*f01)/dg+2*s
    if np.any(tsq<=0):raise ValueError('complex HR radial square root')
    tau=np.sqrt(tsq)
    ell=np.sqrt(farea/garea)
    ens=(np.ones_like(tau),tau+2*ell,s+2*ell*tau+ell**2,
         2*ell*s+ell**2*tau,ell*ell*s)
    return -m2*mg2*np.sqrt(-dg)*garea*sum(b*en for b,en in zip(betas,ens))


@dataclass(frozen=True)
class ActionResult:
    contributions:np.ndarray
    total:float
    names:tuple[str,...]=('EH_g','EH_f','HR','dust_g','dust_f')


def action(amplitudes=None,*,trajectory=None,time_radius=.027,radial_radius=.32,
           quadrature_order=24,betas=BETAS,m2=M2):
    if amplitudes is None:amplitudes=np.zeros(12)
    x=np.asarray(amplitudes,float)
    if x.shape!=(12,) or not np.all(np.isfinite(x)):
        raise ValueError('12 finite canonical/scalar trial directions needed')
    if type(quadrature_order)!=int or quadrature_order<10 or radial_radius<=0 or time_radius<=0:
        raise ValueError('positive support and quadrature >=10')
    bg=trajectory or Trajectory.solve(width=.04)
    if time_radius>bg.width:raise ValueError('trial extends beyond on-shell IVP')
    points,weights=np.polynomial.legendre.leggauss(quadrature_order)
    tt=time_radius*points
    rr=radial_radius*(points+1)/2
    t=tt[:,None];r=rr[None,:]
    # Original 2D integral 4pi dt dr = 2pi*Tmax*Rmax sum w_i w_j.
    measure=2*math.pi*time_radius*radial_radius*weights[:,None]*weights[None,:]
    q=np.array([bg.at(float(ti)) for ti in tt])
    a,b,ad,bd,nf,rhog,rhof=[q[:,i,None] for i in range(7)]
    eg,dg,gm,ga,_=sector_density(scale=a,scale_rate=ad,lapse=1.,rho0=rhog,
        amp=x[:6],t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,planck=MG2)
    ef,df,fm,fa,_=sector_density(scale=b,scale_rate=bd,lapse=nf,rho0=rhof,
        amp=x[6:],t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,planck=MF2)
    hr=hr_density(gm,fm,ga,fa,m2=m2,betas=betas)
    cs=np.array([np.sum(measure*z) for z in (eg,ef,hr,dg,df)])
    return ActionResult(cs,float(np.sum(cs)))


def gradient(*,step=2e-5,**kwargs):
    if not math.isfinite(step) or step<=0:raise ValueError('positive difference step required')
    res=np.zeros(12)
    for i in range(12):
        e=np.zeros(12);e[i]=step
        res[i]=(action(e,**kwargs).total-action(-e,**kwargs).total)/(2*step)
    return res


def metric_physical_witness(*,field='psi_f',amplitude=.003,t=0.,r=.19,
                            time_radius=.027,radial_radius=.32):
    """Non-coordinate f curvature + relative angular ratio witness."""
    bg=Trajectory.solve(width=.04).at(t)
    x=np.zeros(12)
    if field not in ORDER:raise ValueError('unknown field')
    x[ORDER.index(field)]=amplitude
    q=bg
    eg,dg,gm,ga,gR=sector_density(scale=q[0],scale_rate=q[2],lapse=1.,rho0=q[5],
        amp=x[:6],t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,planck=MG2)
    ef,df,fm,fa,fR=sector_density(scale=q[1],scale_rate=q[3],lapse=q[4],rho0=q[6],
        amp=x[6:],t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,planck=MF2)
    return float(fR),float(gR),float(math.sqrt(fa/ga))

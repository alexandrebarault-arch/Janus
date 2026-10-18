"""Step31: exact g-Einstein spatial anisotropy obstruction from physical f shear.

A compact, regular *physical* deformation of f in the common g chart is
NOT the Step30 pure inverse-coordinate compensation. Both comoving dusts
remain normalized and separately conserved if the f density compensates
its changed spatial volume. Keeping g and g dust at the on-shell
homogeneous Candidate-C background then leaves a nonzero necessary
g radial-minus-angular Euler equation, sourced by exact Hassan--Rosen HR.

This is a NO for the *f-only, frozen-g* ansatz, NOT a no-go for
backreacted nonhomothetic backgrounds. No f Einstein equation is solved,
no scalar constraint or stability eigenvalue is inferred.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
M2=23.3348939346
MF2=.10879548725**2
CG=.9
Y0=.5568825591873054
CF=3*.23958426762*Y0**3

@dataclass(frozen=True)
class Snapshot:
    a:float
    b:float
    ng:float
    nf:float
    y:float
    H:float


def candidate_c_snapshot(a=.4):
    """Independent dust-only quartic, restricted regular Step30 sample domain."""
    if not math.isfinite(a) or not .22<a<.66:raise ValueError('sample a out of range')
    b0,b1,b2,b3,b4=BETA
    c=np.array([MF2*M2*b3/3,MF2*M2*b2-M2*b4/3,
      MF2*M2*b1-M2*b3,MF2*CG/(3*a**3)-M2*b2,
      -CF/(3*a**3)-M2*b1/3],float)
    roots=np.roots(c)
    pos=[float(z.real) for z in roots if abs(z.imag)<1e-9 and z.real>0]
    if not pos:raise RuntimeError('no positive dust branch')
    y=min(pos,key=lambda z:abs(math.log(z/Y0)))
    py=np.polyval(np.polyder(c),y)
    if abs(py)<1e-11:raise RuntimeError('degenerate branch')
    pn=-MF2*CG*y/a**3+CF/a**3
    nf=y-pn/py
    V=b0+3*b1*y+3*b2*y*y+b3*y**3
    H2=CG/(3*a**3)+M2*V/3
    if nf<=0 or H2<=0:raise RuntimeError('nonphysical background sample')
    return Snapshot(float(a),float(a*y),1.,float(nf),float(y),math.sqrt(H2))


def profile(t,r,*,T=.06,R=.4):
    """C^3 compact radial/time bump; u-v=O(r^2) at regular centre."""
    if min(T,R)<=0 or not all(math.isfinite(v) for v in (t,r,T,R)) or r<0:
        raise ValueError('invalid compact support')
    if abs(t)>=T or r>=R:return 0.
    return r*r*(1-(t/T)**2)**4*(1-(r/R)**2)**4


def deformation(t,r,eps,*,T=.06,R=.4):
    if not math.isfinite(eps):raise ValueError('nonfinite shear')
    u=eps*profile(t,r,T=T,R=R)
    v=-u/2
    if min(1+2*u,1+2*v)<=0:raise ValueError('f metric not spatial positive')
    return u,v


def physical_f(s:Snapshot,r,u,v):
    """f_2, f_angular, f dust density, normalized clock gradient.

    sqrt(gamma_f)=b^3 r^2 sqrt(1+2u)(1+2v), so
    rho_f=CF/[b^3 sqrt(1+2u)(1+2v)] exactly conserves comoving dust.
    """
    if r<=0 or min(1+2*u,1+2*v)<=0:raise ValueError('positive r/metric required')
    f=np.diag([-s.nf*s.nf,s.b*s.b*(1+2*u)])
    af=s.b*s.b*r*r*(1+2*v)
    rho=CF/(s.b**3*math.sqrt(1+2*u)*(1+2*v))
    grad=np.array([s.nf,0.])
    return f,af,rho,grad


def g_metric(s:Snapshot,r,*,lapse=None,radial_log=0.,angular_log=0.):
    N=s.ng if lapse is None else float(lapse)
    if N<=0 or r<=0:raise ValueError('positive lapse/radius required')
    g=np.diag([-N*N,s.a*s.a*math.exp(2*radial_log)])
    ag=s.a*s.a*r*r*math.exp(2*angular_log)
    return g,ag


def hr_density(g,ag,f,af,*,beta=BETA,m2=M2):
    """Independent exact spherical principal 2x2 root, all five betas."""
    if len(beta)!=5 or not all(math.isfinite(float(x)) for x in beta):
        raise ValueError('five finite betas required')
    dg=float(np.linalg.det(g));df=float(np.linalg.det(f))
    if dg>=0 or df>=0 or min(ag,af)<=0:raise ValueError('Lorentzian HR domain')
    d=math.sqrt(df/dg)
    tau2=float(np.trace(np.linalg.solve(g,f)))+2*d
    if tau2<=0:raise ValueError('nonprincipal real root')
    tau=math.sqrt(tau2);ell=math.sqrt(af/ag)
    e=(1.,tau+2*ell,d+2*ell*tau+ell*ell,
       2*ell*d+ell*ell*tau,ell*ell*d)
    return -m2*math.sqrt(-dg)*ag*sum(b*z for b,z in zip(beta,e))


def polynomials(x,z,n,*,beta=BETA):
    b0,b1,b2,b3,b4=beta
    A=b0+b1*(x+2*z)+b2*(2*x*z+z*z)+b3*x*z*z
    B=b1+b2*(x+2*z)+b3*(2*x*z+z*z)+b4*x*z*z
    return A,B


def analytic_g_lapse_shift(s,u,v,*,beta=BETA,m2=M2):
    """Difference in g lapse Euler dL/dNg per comoving volume."""
    x=s.y*math.sqrt(1+2*u);z=s.y*math.sqrt(1+2*v)
    A,_=polynomials(x,z,s.nf/s.ng,beta=beta)
    A0,_=polynomials(s.y,s.y,s.nf/s.ng,beta=beta)
    return -m2*s.a**3*(A-A0)


def analytic_g_pressure_anisotropy(s,u,v,*,beta=BETA,m2=M2):
    """(dL/dlog a_r - 0.5 dL/dlog a_theta)/(Ng*a_r*a_theta^2*r^2).

    Exact identity for diagonal metrics:
      m² (x-z)[beta1+beta2*(z+n)+beta3*n*z], n=Nf/Ng.
    No beta0/beta4. g EH and g comoving dust are isotropic if g
    stays homogeneous, hence a nonzero result obstructs that ansatz.
    """
    x=s.y*math.sqrt(1+2*u);z=s.y*math.sqrt(1+2*v)
    n=s.nf/s.ng
    return m2*(x-z)*(beta[1]+beta[2]*(z+n)+beta[3]*n*z)


def independent_g_lapse_shift(s,r,u,v,*,beta=BETA,m2=M2,h=1e-5):
    """Direct numerical partial g lapse variation of exact 2x2 HR action."""
    if h<=0 or h>=s.ng/4:raise ValueError('bad step')
    f,af,_,_=physical_f(s,r,u,v)
    f0,af0,_,_=physical_f(s,r,0.,0.)
    def derivative(ff,aa):
        gp,ap=g_metric(s,r,lapse=s.ng+h)
        gm,am=g_metric(s,r,lapse=s.ng-h)
        return (hr_density(gp,ap,ff,aa,beta=beta,m2=m2)
              -hr_density(gm,am,ff,aa,beta=beta,m2=m2))/(2*h*r*r)
    return derivative(f,af)-derivative(f0,af0)


def independent_g_pressure_anisotropy(s,r,u,v,*,beta=BETA,m2=M2,h=1e-5):
    """Direct independent partial g radial and angular log variations."""
    if h<=0 or h>.05:raise ValueError('bad step')
    f,af,_,_=physical_f(s,r,u,v)
    def L(rad,ang):
        g,ag=g_metric(s,r,radial_log=rad,angular_log=ang)
        return hr_density(g,ag,f,af,beta=beta,m2=m2)
    dr=(L(h,0)-L(-h,0))/(2*h)
    dt=(L(0,h)-L(0,-h))/(2*h)
    return (dr-dt/2)/(s.ng*s.a**3*r*r)


def dust_norm_and_current(s,r,u,v):
    """Independent exact f dust normalization and current per dOmega.

    The current is sqrt(-f2)*fOmega*rho*(-f2^-1 grad(theta)).
    """
    f,af,rho,grad=physical_f(s,r,u,v)
    norm=float(grad@np.linalg.solve(f,grad))
    current=math.sqrt(-np.linalg.det(f))*af*rho*(-np.linalg.solve(f,grad))
    return norm,current,rho


def native_transport(s,r,u,v,*,lam=.78,lamdot=.04,sigma=.08,sigmadot=.025):
    """At a common-chart point: exact passive native tensor and dust transport.

    This maps a *physically sheared* f to native coordinates; it does NOT
    undo its changed relative eigenvalues x,z or turn it into homogeneous f.
    """
    J=np.array([[1+.5*sigmadot*r*r,sigma*r],[lamdot*r,lam]],float)
    D=float(np.linalg.det(J))
    if D<=0:raise ValueError('bad chart orientation')
    f,af,rho,grad=physical_f(s,r,u,v)
    inv=np.linalg.inv(J)
    fn=inv.T@f@inv
    gradn=grad@inv
    un=-np.linalg.solve(fn,gradn)
    cn=math.sqrt(-np.linalg.det(fn))*af*rho*un
    return dict(J=J,D=D,common=f,native=fn,ang=af,grad=grad,
                grad_native=gradn,rho=rho,current_native=cn)


def integrated_anisotropy_witness(s,eps,*,R=.4,order=40):
    """Positive radial moment of necessary g pressure anisotropy at t=0.

    This is NOT a full 5-sector time/radial action or full tadpole test.
    """
    if order<4:raise ValueError('quadrature order >=4')
    z,w=np.polynomial.legendre.leggauss(order)
    rs=.5*R*(z+1)
    total=0.
    for r,weight in zip(rs,w):
        u,v=deformation(0.,float(r),eps,R=R)
        total+=float(weight)*r*r*profile(0.,float(r),R=R)*analytic_g_pressure_anisotropy(s,u,v)
    return .5*R*total

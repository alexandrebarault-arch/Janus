"""Exact native-field compensation for a nonhomothetic f chart.

Given an *on-shell homogeneous* physical f metric in the common g chart,
this module rewrites the SAME f tensor, dust scalar and conserved current
in native (T,R) coordinates.  It is a pure coordinate control, NOT a
new physical nonhomothetic solution, Stückelberg mode or BD constraint.

The new native metric generically has a shift, anisotropic radial/angular
components, and radial dust gradients: imposing an FLRW f-native ansatz
again after the transformation would change the physical spacetime.

Radiation-free Candidate-C two-dust homogeneous background is explicitly
sampled with an implicit quartic root and the dynamical-branch f lapse.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from scipy.integrate import solve_ivp

BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
M2=23.3348939346
MF2=.10879548725**2
CG=.9
Y0=.5568825591873054
CF=3*.23958426762*Y0**3


def potential(y):
    b0,b1,b2,b3,_=BETA
    return b0+3*b1*y+3*b2*y*y+b3*y**3


def branch_point(a):
    """y, y_N, E=H_g, Nf on the dust-only on-shell dynamical branch."""
    if not math.isfinite(a) or not .22<a<.66:
        raise ValueError('this local on-shell benchmark is for 0.22<a<0.66')
    b0,b1,b2,b3,b4=BETA
    c=np.array([MF2*M2*b3/3, MF2*M2*b2-M2*b4/3,
       MF2*M2*b1-M2*b3, MF2*CG/(3*a**3)-M2*b2,
       -CF/(3*a**3)-M2*b1/3],float)
    roots=np.roots(c)
    positive=[z.real for z in roots if abs(z.imag)<1e-9 and z.real>0]
    if not positive:raise RuntimeError('Candidate C branch unavailable')
    y=min(positive,key=lambda z:abs(math.log(z/Y0)))
    py=np.polyval(np.polyder(c),y)
    if abs(py)<1e-12:raise RuntimeError('singular homogeneous quartic root')
    pn=-MF2*CG*y/a**3+CF/a**3
    yN=-pn/py
    E2=CG/(3*a**3)+M2*potential(y)/3
    nf=y+yN
    if E2<=0 or nf<=0:raise RuntimeError('homogeneous background invalid')
    return float(y),float(yN),math.sqrt(E2),float(nf)


@dataclass(frozen=True)
class HomogeneousDustTrajectory:
    """Two-sided IVP solution of a_dot=aH, theta_f_dot=Nf, with Ng=1."""
    forward:object
    backward:object
    halfwidth:float

    @classmethod
    def solve(cls,a0=.4,halfwidth=.075,rtol=2e-11):
        if not (.22<a0<.66) or not 0<halfwidth<.10:raise ValueError('invalid sample domain')
        def rhs(t,z):
            y,yn,E,nf=branch_point(float(z[0]))
            return [z[0]*E,nf]
        f=solve_ivp(rhs,(0.,halfwidth),(a0,0.),rtol=rtol,atol=2e-13,dense_output=True)
        b=solve_ivp(rhs,(0.,-halfwidth),(a0,0.),rtol=rtol,atol=2e-13,dense_output=True)
        if not (f.success and b.success):raise RuntimeError('Candidate C background integration failed')
        return cls(f.sol,b.sol,halfwidth)

    def at(self,t):
        if not math.isfinite(t) or abs(t)>self.halfwidth:
            raise ValueError('t outside exact-ODE sample support')
        a,theta=(self.forward if t>=0 else self.backward)(t)
        a=float(a);theta=float(theta)
        y,yn,H,nf=branch_point(a)
        return dict(t=t,a=a,b=a*y,Ng=1.,Nf=nf,H=H,
                    adot=a*H,bdot=nf*a*H,theta=theta,
                    rho_g=CG/a**3,rho_f=CF/(a*y)**3)


@dataclass(frozen=True)
class Chart:
    """T=t+(sigma(t)/2)r²; R=lambda(t)r, with regular time tilt."""
    lam0:float=.78
    lamdot:float=.04
    sig0:float=.08
    sigdot:float=.025

    def forward(self,t,r):
        if not all(math.isfinite(v) for v in (t,r)) or r<0:raise ValueError('invalid (t,r)')
        lam=self.lam0+self.lamdot*t
        sig=self.sig0+self.sigdot*t
        T=t+.5*sig*r*r
        R=lam*r
        tt=1+.5*self.sigdot*r*r
        tr=sig*r
        rt=self.lamdot*r
        rr=lam
        D=tt*rr-tr*rt
        if R<0 or D<=0 or lam<=0:raise ValueError('non-orientation-preserving f map')
        return T,R,np.array([[tt,tr],[rt,rr]],float),D

    def inverse(self,T,R):
        if not all(math.isfinite(v) for v in (T,R)) or R<0:raise ValueError('invalid (T,R)')
        t=T
        for _ in range(25):
            lam=self.lam0+self.lamdot*t
            if lam<=0:raise ValueError('nonpositive lambda')
            r=R/lam
            Tp,Rp,J,D=self.forward(t,r)
            dt=(Tp-T)/(D/lam)
            t-=dt
            if abs(dt)<2e-15:break
        r=R/(self.lam0+self.lamdot*t)
        Tp,Rp,J,D=self.forward(t,r)
        if abs(Tp-T)>5e-13 or abs(Rp-R)>5e-13:raise ArithmeticError('chart inverse failed')
        return t,r,J,D


def physical_f_metric(q,r):
    """Physical homogeneous f metric on common g coordinates, incl area."""
    return np.diag([-q['Nf']**2,q['b']**2]),q['b']**2*r*r


def physical_g_metric(q,r):
    return np.diag([-q['Ng']**2,q['a']**2]),q['a']**2*r*r


def native_compensated_f(T,R,bg,chart):
    """f_native=(J^{-1})^T f_common J^{-1}; exact dust transport.

    Here J=d(T,R)/d(t,r), native angular radius is b(t)^2 r^2,
    native phase theta=theta_f(t(T,R)), rho_f=Cf/b(t)^3.
    """
    t,r,J,D=chart.inverse(T,R)
    q=bg.at(t)
    common,ang=physical_f_metric(q,r)
    inv=np.linalg.inv(J)
    native=inv.T@common@inv
    # Native theta gradient is (theta_t,theta_r) J^{-1}.
    theta_native_grad=np.array([q['Nf'],0.])@inv
    sqrt_native=math.sqrt(-np.linalg.det(native))*ang
    u_native=-np.linalg.solve(native,theta_native_grad)
    current=sqrt_native*q['rho_f']*u_native
    return dict(native=native,angular=ang,grad=theta_native_grad,
        rho=q['rho_f'],phase=q['theta'],current=current,
        q=q,t=t,r=r,J=J,D=D)


def uncompensated_native_flrw(T,R,bg,chart,*,central_scale_compensated=True):
    """Scale-only, no-shift f-native ansatz; NOT the transported metric.

    With sigma != 0, sampling b(t(T,R)) also depends on R at fixed T,
    so this is not literally a homogeneous FLRW field in native coords.
    It is a deliberately restricted comparison model, not a solution.
    """
    t,r,J,D=chart.inverse(T,R)
    q=bg.at(t)
    lam=chart.lam0+chart.lamdot*t
    native_b=q['b']/lam if central_scale_compensated else q['b']
    native=np.diag([-q['Nf']**2,native_b**2])
    return native,native_b*native_b*R*R


def pull_native_to_common(native,angular,J):
    return J.T@native@J,float(angular)


def spherical_hr_density(g,ag,f,af,betas=BETA,m2=M2,Mg2=1.):
    """Direct 2x2 principal-root all-beta HR potential, per solid angle."""
    g=np.asarray(g,float);f=np.asarray(f,float)
    dg=np.linalg.det(g);df=np.linalg.det(f)
    if dg>=0 or df>=0 or min(ag,af)<=0:raise ValueError('bad Lorentzian two-metric branch')
    s=math.sqrt(df/dg)
    tau2=np.trace(np.linalg.solve(g,f))+2*s
    if tau2<=0:raise ValueError('nonreal HR radial square root')
    tau=math.sqrt(tau2);ell=math.sqrt(af/ag)
    es=(1,tau+2*ell,s+2*ell*tau+ell*ell,
        2*ell*s+ell*ell*tau,ell*ell*s)
    return float(-m2*Mg2*math.sqrt(-dg)*ag*sum(float(b)*e for b,e in zip(betas,es)))


def analytic_homogeneous_hr_density(q,r):
    y=q['b']/q['a'];v=q['Nf']/q['Ng']
    b0,b1,b2,b3,b4=BETA
    e=(1,v+3*y,3*v*y+3*y*y,3*v*y*y+y**3,v*y**3)
    return -M2*q['Ng']*q['a']**3*r*r*sum(x*z for x,z in zip(BETA,e))


def direct_g_lapse_residual(q,r,f_common,ang,step=1e-5):
    """Necessary g Friedmann lapse residual from native physical HR action.

    Uses g ADM gravity + canonical g dust source from homogeneous background,
    plus INDEPENDENT finite-difference of the exact spherical HR potential.
    """
    if r<=0 or step<=0:raise ValueError('r and finite-difference step must be > 0')
    def integrand(N):
        g=np.diag([-N*N,q['a']**2])
        grav=-3*q['a']*q['adot']**2/N
        dust=-N*CG
        potential=spherical_hr_density(g,q['a']**2*r*r,f_common,ang)/(r*r)
        return grav+dust+potential
    N=q['Ng']
    return (integrand(N+step)-integrand(N-step))/(2*step)


def native_current_divergence(T,R,bg,chart,h=2e-5):
    """Numerical native continuity ∂_T(sqrt(-f)rho u^T)+∂_R(...)."""
    if R<3*h:raise ValueError('radius must exceed stencil')
    a=native_compensated_f(T+h,R,bg,chart)['current'][0]
    b=native_compensated_f(T-h,R,bg,chart)['current'][0]
    c=native_compensated_f(T,R+h,bg,chart)['current'][1]
    d=native_compensated_f(T,R-h,bg,chart)['current'][1]
    return (a-b+c-d)/(2*h)


def independent_native_dust_lagrangian(q,r,chart,*,t,phase_amp=.027,density_amp=.08):
    """Off-shell covariant dust density in both common and native charts.

    Finite phase profile: theta=theta0(t)+eps*t*r²;
    finite dust density: rho=Cf/b³*(1+delta*r²).
    Neither perturbation is imposed on shell; comparison tests the SAME
    native phase gradients and scalar-density Jacobian, not zero=zero.
    """
    if r<=0:raise ValueError('radial point must be positive')
    T,R,J,D=chart.forward(t,r)
    data=native_compensated_f(T,R,q,chart)
    bg=data['q']
    common,angular=physical_f_metric(bg,r)
    grad_common=np.array([bg['Nf']+phase_amp*r*r,2*phase_amp*t*r])
    grad_native=grad_common@np.linalg.inv(J)
    density=bg['rho_f']*(1+density_amp*r*r)
    if density<=0:raise ValueError('nonpositive perturbed dust density')
    def lag(metric,ang,grad):
        det=np.linalg.det(metric)
        return -.5*math.sqrt(-det)*ang*density*(1+grad@np.linalg.solve(metric,grad))
    common_l=lag(common,angular,grad_common)
    native_l=lag(data['native'],data['angular'],grad_native)
    return float(common_l),float(D*native_l),float(native_l)


def compact_g_lapse_tadpole(bg,chart,*,time_radius=.03,radial_radius=.28,
                              order=18,step=2e-5,scale_only=False):
    """First variation of *one actual shared spacetime sub-action*.

    Includes g ADM+GHY flat background at arbitrary lapse N(t,r), canonical
    g dust charge density -N Cg and exact nonlinear HR square root with the
    compensated f metric.  f-EH/f-dust do NOT contribute to direct partial
    g-lapse variations, at fixed f native chart and independent f fields.

    Not a full five-sector on-shell Euler test: g scalar trace/shear,
    f lapse/shift/scale, relative chart and BD variations not included.
    """
    if not 0<time_radius<.05 or not 0<radial_radius<.5:
        raise ValueError('compact support outside tested trajectory')
    if not isinstance(order,int) or order<8 or not 0<step<1e-3:
        raise ValueError('invalid quadrature/finite variation')
    tnodes,tw=np.polynomial.legendre.leggauss(order)
    rnodes,rw=np.polynomial.legendre.leggauss(order)
    ts=time_radius*tnodes
    rs=.5*radial_radius*(rnodes+1)
    cache=[]
    for t,wt in zip(ts,tw):
        q=bg.at(float(t))
        for r,wr in zip(rs,rw):
            r=float(r)
            T,R,J,_=chart.forward(float(t),r)
            if scale_only:
                n,ang=uncompensated_native_flrw(T,R,bg,chart)
            else:
                f=native_compensated_f(T,R,bg,chart)
                n,ang=f['native'],f['angular']
            fc,af=pull_native_to_common(n,ang,J)
            weight=4*math.pi*time_radius*.5*radial_radius*wt*wr
            bump=(1-(t/time_radius)**2)**4*(1-(r/radial_radius)**2)**4
            cache.append((q,r,fc,af,float(weight),float(bump)))
    def action(eps):
        val=0.
        for q,r,f,af,w,bump in cache:
            N=q['Ng']+eps*bump
            g=np.diag([-N*N,q['a']**2])
            EH=-3*q['a']*q['adot']**2/N
            dust=-N*CG
            HR=spherical_hr_density(g,q['a']**2*r*r,f,af)/(r*r)
            val+=w*r*r*(EH+dust+HR)
        return float(val)
    return (action(step)-action(-step))/(2*step)

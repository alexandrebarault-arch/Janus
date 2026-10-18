"""Homogeneous two-metric EH+HR+TWO DUST Routhian, background on-shell audit.

The positive Einstein-Hilbert minisuperspace Lagrangian with GHY terms,
negative HR potential and two COMOVING canonical dust momenta is
L=-3 Mg² a adot²/Ng -3 Mf² b bdot²/Nf
  - m² Mg² a³[Ng V(b/a)+Nf W(b/a)] - Ng Cg - Nf Cf.

Cg,Cf are conserved dust momenta obtained by Routh reducing the clock
variables; they are NOT the covariant dust Lagrangians evaluated on shell.
The lapse constraints and scale Euler residuals are exact partial variations
of the SAME fixed-field Lagrangian. Candidate-C checks are background ONLY.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class MiniParams:
    beta: tuple[float, float, float, float, float]
    m2: float
    Mg2: float
    Mf2: float
    Cg: float
    Cf: float

@dataclass(frozen=True)
class MiniPoint:
    a: float; b: float; adot: float; bdot: float
    addot: float; bddot: float; Ng: float; Nf: float
    Ngdot: float=0.0; Nfdot: float=0.0


def _check(p, q):
    vals=(p.m2,p.Mg2,p.Mf2,p.Cg,p.Cf,*p.beta,q.a,q.b,q.adot,q.bdot,
          q.addot,q.bddot,q.Ng,q.Nf,q.Ngdot,q.Nfdot)
    if len(p.beta)!=5 or not all(math.isfinite(float(x)) for x in vals):
        raise ValueError('all minisuperspace inputs must be finite')
    if min(p.Mg2,p.Mf2,q.a,q.b,q.Ng,q.Nf)<=0 or min(p.m2,p.Cg,p.Cf)<0:
        raise ValueError('positive Planck masses, scales and lapses, nonnegative sources')


def potentials(y, beta):
    b0,b1,b2,b3,b4=beta
    V=b0+3*b1*y+3*b2*y*y+b3*y**3
    W=b1+3*b2*y+3*b3*y*y+b4*y**3
    # dg/da at fixed b is 3a² A; df/da is 3a² J.
    A=b0+2*b1*y+b2*y*y
    J=b1+2*b2*y+b3*y*y
    K=b2+2*b3*y+b4*y*y
    return V,W,A,J,K


def routhian(p: MiniParams,q: MiniPoint):
    _check(p,q)
    V,W,_,_,_=potentials(q.b/q.a,p.beta)
    return (-3*p.Mg2*q.a*q.adot**2/q.Ng
            -3*p.Mf2*q.b*q.bdot**2/q.Nf
            -p.m2*p.Mg2*q.a**3*(q.Ng*V+q.Nf*W)
            -q.Ng*p.Cg-q.Nf*p.Cf)


def residuals(p: MiniParams,q: MiniPoint):
    """(dL/dNg,dL/dNf, ELa,ELb, Bianchi dynamical-branch factor).

    ELa = d/dt(dL/dadot)-dL/da; similarly ELb.
    Sign convention lapse residuals are dL/dN, not equation multiplied -1.
    Last quantity is adot/Ng - bdot/Nf; branch relation requires zero
    ONLY for dynamical J != 0, not on the algebraic J=0 branch.
    """
    _check(p,q)
    y=q.b/q.a
    V,W,A,J,K=potentials(y,p.beta)
    rg=(3*p.Mg2*q.a*q.adot**2/q.Ng**2
        -p.m2*p.Mg2*q.a**3*V-p.Cg)
    rf=(3*p.Mf2*q.b*q.bdot**2/q.Nf**2
        -p.m2*p.Mg2*q.a**3*W-p.Cf)
    ea=(-3*p.Mg2*(q.adot**2+2*q.a*q.addot
                   -2*q.a*q.adot*q.Ngdot/q.Ng)/q.Ng
        +3*p.m2*p.Mg2*q.a**2*(q.Ng*A+q.Nf*J))
    eb=(-3*p.Mf2*(q.bdot**2+2*q.b*q.bddot
                   -2*q.b*q.bdot*q.Nfdot/q.Nf)/q.Nf
        +3*p.m2*p.Mg2*q.a**2*(q.Ng*J+q.Nf*K))
    return np.array([rg,rf,ea,eb,q.adot/q.Ng-q.bdot/q.Nf],float)


def lapse_variation_from_covariant_dust(*,N,scale,C):
    """Dust clock first-order Routh, warning about on-shell substitution.

    Native homogeneous dust action is Lcov=(rho/2) a³ [theta_dot²/N-N].
    p=a³ rho theta_dot/N=C>0. On norm shell theta_dot=N:
    Lcov == 0 but its partial derivative dLcov/dN at fixed theta_dot
    and fixed rho is -a³ rho=-C. Routhian -N*C has that derivative.
    """
    if not all(math.isfinite(float(x)) for x in (N,scale,C)) or min(N,scale)<=0 or C<0:
        raise ValueError('invalid dust clock')
    rho=C/scale**3
    theta_dot=N
    cov=.5*rho*scale**3*(theta_dot**2/N-N)
    partial_N=-.5*rho*scale**3*(theta_dot**2/N**2+1)
    routh=-N*C
    return np.array([cov,partial_N,routh,-C],float)


# Candidate-C dust-only variant corresponding to numerics/candidate_c_dust_background.py.
_C_BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
_C_M2=23.3348939346
_C_ALPHA=.10879548725
_C_GM=.30
_C_FM=.23958426762
_C_YREF=.55688253212


def _present_eq(y):
    beta=_C_BETA
    V,W,*_=potentials(y,beta)
    # mg²=1; Mf²=alpha²; rho_f(a=1,b=y)=3 Omega_fm0.
    return (_C_GM+_C_M2*V/3
        -y*y*(_C_FM+_C_M2*W/(3*y**3))/_C_ALPHA**2)


def resolve_candidate_c_dust_y0():
    xs=np.linspace(.5*_C_YREF,1.5*_C_YREF,1001)
    roots=[]
    left=xs[0];v=_present_eq(left)
    for right in xs[1:]:
        w=_present_eq(right)
        if v*w<=0:
            lo=float(left);hi=float(right);flo=float(v)
            for _ in range(75):
                mid=(lo+hi)/2
                fm=_present_eq(mid)
                if flo*fm<=0:hi=mid
                else:lo=mid;flo=fm
            roots.append((lo+hi)/2)
        left,v=right,w
    if not roots:raise RuntimeError('no present dust normalization root')
    return float(min(roots,key=lambda x:abs(x-_C_YREF)))


def branch_polynomial(a,p,y):
    """Quartic is algebraically equivalent to both lapse Friedmann constraints."""
    b0,b1,b2,b3,b4=p.beta
    Mg2=p.Mg2;Mf2=p.Mf2;m2=p.m2
    # Multiply E²_g = y² E²_f by Mf²*y after dividing by Mg².
    # g dust Cg/(3 Mg² a³), f dust Cf/(3 Mf² (a y)³).
    Om_g=p.Cg/(3*Mg2*a**3)
    return (Mf2/Mg2)*(Om_g*y + m2/3*(3*b1*y*y+3*b2*y**3+b3*y**4+b0*y)) - (
        p.Cf/(3*Mg2*a**3) + m2/3*(b1+3*b2*y+3*b3*y*y+b4*y**3)
    )


def candidate_c_dust_point(a=1.):
    """Return independently implicit-differentiated dust-only dynamical branch.

    a is the g scale factor; Ng=1 and time is g cosmic time. The
    candidate y is the positive quartic root continuously closest to the
    present y0 at a=1, using a dense continuation along ln a.
    """
    if not math.isfinite(a) or not (0.01<=a<=2.):
        raise ValueError('sampled a must be in [0.01,2]')
    y0=resolve_candidate_c_dust_y0()
    p=MiniParams(beta=_C_BETA,m2=_C_M2,Mg2=1.,Mf2=_C_ALPHA**2,
                 Cg=3*_C_GM,Cf=3*_C_FM*y0**3)
    yprev=y0
    # More robust than selecting largest root: continue from present point.
    for A in np.geomspace(1.,a,max(2,int(120*abs(np.log(a)))+2)):
        # p(y) is quartic; derive roots through a simple polynomial evaluation.
        coeff=np.array([p.Mf2*p.m2*p.beta[3]/3,
             p.Mf2*p.m2*p.beta[2]-p.m2*p.beta[4]/3,
             p.Mf2*p.m2*p.beta[1]-p.m2*p.beta[3],
             p.Mf2*p.Cg/(3*A**3)-p.m2*p.beta[2],
             -p.Cf/(3*A**3)-p.m2*p.beta[1]/3])
        roots=np.roots(coeff)
        positive=[z.real for z in roots if abs(z.imag)<1e-7 and z.real>0]
        if not positive:raise RuntimeError('no positive branch root')
        yprev=float(min(positive,key=lambda z:abs(math.log(z/yprev))))
    y=yprev
    # Algebraic branch P(y,N)=0; derivatives of original polynomial at fixed a.
    def P(y,N):return branch_polynomial(math.exp(N),p,y)
    N=math.log(a)
    # Exact polynomial partials derived analytically.
    b0,b1,b2,b3,b4=p.beta;m2=p.m2;mf=p.Mf2
    c4=mf*m2*b3/3
    c3=mf*m2*b2-m2*b4/3
    c2=mf*m2*b1-m2*b3
    c1=mf*p.Cg/(3*a**3)-m2*b2
    # c0 = -Cf/(3a³) -m² b1/3
    py=4*c4*y**3+3*c3*y*y+2*c2*y+c1
    pyy=12*c4*y*y+6*c3*y+2*c2
    c1n=-mf*p.Cg/a**3
    c1nn=3*mf*p.Cg/a**3
    c0n=p.Cf/a**3
    c0nn=-3*p.Cf/a**3
    pn=c1n*y+c0n
    pny=c1n
    pnn=c1nn*y+c0nn
    if abs(py)<1e-10:raise RuntimeError('singular background branch derivative')
    yn=-pn/py
    ynn=-(pnn+2*pny*yn+pyy*yn**2)/py
    V,W,A,J,K=potentials(y,p.beta)
    E2=p.Cg/(3*a**3)+p.m2*V/3
    if E2<=0:raise RuntimeError('negative H²')
    E=math.sqrt(E2)
    E2n=-p.Cg/a**3+p.m2*J*yn
    En=E2n/(2*E)
    ng=1.; nf=y+yn  # dynamical branch Nf/N_g=bdot/adot
    nfn=yn+ynn
    if nf<=0:raise RuntimeError('nonpositive f lapse')
    adot=a*E
    addot=a*(E*E+E*En)
    bdot=nf*adot
    bddot=nf*addot + nfn*E*adot
    q=MiniPoint(a=a,b=a*y,adot=adot,bdot=bdot,addot=addot,
        bddot=bddot,Ng=ng,Nf=nf,Ngdot=0.,Nfdot=nfn*E)
    return p,q,dict(y=y,yN=yn,yNN=ynn,E=E,EN=En,branch_residual=P(y,N))


def compact_temporal_tadpoles(p: MiniParams, *,times,weights,background,
                              time_radius:float,amplitude_step:float=1.e-5):
    """Direct first variation of a 1D spacetime minisuperspace Routhian.

    Time-compact variations independently perturb a,b,Ng,Nf. For scale
    factors, also vary the time derivatives with the bump derivative.
    Their integrated coefficients must vanish on shell after integration
    by parts. No ADM/HR scalar perturbation physics is implied here.

    'background' contains one MiniPoint per Gauss-Legendre time node.
    """
    t=np.asarray(times,float);w=np.asarray(weights,float)
    if (t.ndim!=1 or w.shape!=t.shape or len(background)!=len(t)
        or not np.all(np.isfinite(t)) or not np.all(np.isfinite(w))
        or not math.isfinite(time_radius) or time_radius<=0
        or not math.isfinite(amplitude_step) or amplitude_step<=0
        or np.any(abs(t)>=time_radius)):
        raise ValueError('invalid compact temporal variational domain')
    bump=(1-(t/time_radius)**2)**4
    dbump=-8*t/(time_radius*time_radius)*(1-(t/time_radius)**2)**3
    grad=[]
    for field in ('a','b','Ng','Nf'):
        def S(sign):
            val=0.
            for i,q in enumerate(background):
                delta=sign*amplitude_step*bump[i]
                attrs={field:getattr(q,field)+delta}
                if field=='a':attrs['adot']=q.adot+sign*amplitude_step*dbump[i]
                if field=='b':attrs['bdot']=q.bdot+sign*amplitude_step*dbump[i]
                val+=w[i]*routhian(p,MiniPoint(**{**vars(q),**attrs}))
            return val
        grad.append((S(1)-S(-1))/(2*amplitude_step))
    return np.array(grad,float)
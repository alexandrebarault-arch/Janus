"""Exact curved, non-comoving two-dust *primary* constraint witness.

Positive-Einstein-Hilbert spherical ADM g/f plus all-beta Hassan--Rosen.
Constructs radially curved spatial three-metrics, nonzero and independent
radial dust phase gradients, relative shift z(r), and independently positive
dust momenta while satisfying H_g=H_f=D_g+D_f=F_z=0 *pointwise*.

This is constrained INITIAL DATA, NOT a time-evolved solution, local BD
secondary, nor a full nonhomothetic cosmological background. All expressions
are analytic SymPy functions, with numerical evaluation at strictly r>0.
"""
from __future__ import annotations
from dataclasses import dataclass,field
import math
import numpy as np
import sympy as sp

R=sp.Symbol('r', real=True, positive=True)
BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
M2=23.3348939346
MG2=1.
MF2=.10879548725**2
CG=.9
Y04=.5787707228025044   # independently verified Candidate-C no-radiation a=.4 point


@dataclass(frozen=True)
class CurvedPrimary:
    expr:dict[str,sp.Expr]
    params:dict[str,float]
    _cache:dict=field(default_factory=dict,compare=False,repr=False)

    def _compiled(self,fields):
        if fields not in self._cache:
            self._cache[fields]=sp.lambdify(R,[self.expr[k] for k in fields],modules='numpy',cse=True)
        return self._cache[fields]

    def eval(self,r,fields=('Hg','Hf','Ddiag','Fz','pg','pf','z')):
        r=np.asarray(r)
        if np.any(r<=0) or not np.all(np.isfinite(r)):
            raise ValueError('r must be finite and positive')
        vals=self._compiled(tuple(fields))(r)
        return np.array([np.broadcast_to(x,r.shape) for x in vals],dtype=float)


def build_primary(*,a=.4,y=Y04,curv_g=.015,curv_f=-.012,
                  z_slope=.04,theta_g=.012,theta_f=-.016,
                  grav_g=.04,grav_f=-.035,f_delta=()):
    """Construct *exactly* satisfying six canonical spherical constraints.

    - L_i=A_i u_i(r)^2, S_i=A_i r u_i(r)^2;
    - theta_i'=k_i r L_i (smooth even theta_i at spherical center);
    - z(r)=z_slope*r (smooth radial shift at center);
    - D_g=K z/sqrt(1-z²), D_f=-D_g;
    - linear solve of independent H_g=H_f=0 for p_g,p_f;
    - pS_i obtained from exact D_i radial momentum equations.

    Separate dust positive-density checks are performed in assert_regular.
    Does not constrain the full secondary or determine a lapse ratio.
    """
    v=(a,y,curv_g,curv_f,z_slope,theta_g,theta_f,grav_g,grav_f,*f_delta)
    if not all(math.isfinite(float(x)) for x in v) or a<=0 or y<=0:
        raise ValueError('finite positive background data required')
    if max(abs(curv_g),abs(curv_f),abs(z_slope),abs(theta_g),abs(theta_f),abs(grav_g),abs(grav_f),*(abs(float(v)) for v in f_delta))>.19:
        raise ValueError('witness restricted to regular chart and dust neighborhood')
    b=a*y
    b0,b1,b2,b3,b4=BETA
    vg=b0+3*b1*y+3*b2*y*y+b3*y**3
    H2=CG/(3*a**3)+M2*vg/3
    if H2<=0:raise ValueError('nonreal benchmark expansion')
    H=math.sqrt(H2)
    pa=-6*MG2*a*a*H
    pb=-6*MF2*b*a*H
    # Floating constants inside SymPy remain numerical, permitting rapid lambdify.
    ug=1+sp.Float(curv_g)*R**2;uf=1+sp.Float(curv_f)*R**2
    Lg=sp.Float(a)*ug**2; Sg=Lg*R
    Lf=sp.Float(b)*uf**2; Sf=Lf*R
    thgr=sp.Float(theta_g)*R*Lg
    thfr=sp.Float(theta_f)*R*Lf
    tg=sp.integrate(thgr,R);tf=sp.integrate(thfr,R)
    z=sp.Float(z_slope)*R
    root=sp.sqrt(1-z*z)
    # Gravitational momenta are independently selected, not tied by a gauge ansatz.
    # pL_i' = 2r [u_i+2r u_i'] P_i makes the flat limit pL_i=r² P_i.
    Pg=sp.Float(pa/3)*(1+sp.Float(grav_g)*R)
    Pf=sp.Float(pb/3)*(1+sp.Float(grav_f)*R)+sum(sp.Float(v)*R**i for i,v in enumerate(f_delta))
    pLg=sp.integrate(2*R*(ug+2*R*sp.diff(ug,R))*Pg,R)
    pLf=sp.integrate(2*R*(uf+2*R*sp.diff(uf,R))*Pf,R)
    # Curvatures evaluated directly from the original spherical spatial ADM metric.
    def R3(L,S):
        W=sp.diff(S,R)/L
        return 2/S**2*(1-W**2-2*S/L*sp.diff(W,R))
    Rg=R3(Lg,Sg); Rf=R3(Lf,Sf)
    qg=sp.Float(M2*MG2)
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    K=qg*Lg*Lf*At
    D=K*z/root
    Wg=qg*(Lg*A0+Lf*At*root)
    Wf=qg*(Lf*As+Lg*At*root)
    # Gravitational base terms before substituting pS, and dust lapse gradients.
    def dust_solution(L,S,pL,mass2,theta_r,Dsector,W,Rcurv):
        beta_dust=sp.sqrt(1+theta_r**2/L**2)
        factor=pL/(2*sp.Float(mass2)*S*sp.diff(S,R))
        kinetic=L*pL**2/(4*sp.Float(mass2)*S**2)
        pot=-sp.Float(mass2)*L*S**2*Rcurv/2
        # pS=[Dsector+L pL'-p theta_r]/S'.
        constant=kinetic-factor*(Dsector+L*sp.diff(pL,R))+pot+z*D/L+W
        coefficient=beta_dust+factor*theta_r
        p=-constant/coefficient
        pS=(Dsector+L*sp.diff(pL,R)-p*theta_r)/sp.diff(S,R)
        return p,pS
    pg,pSg=dust_solution(Lg,Sg,pLg,MG2,thgr,D,Wg,Rg)
    pf,pSf=dust_solution(Lf,Sf,pLf,MF2,thfr,-D,Wf,Rf)
    cg=Lg*pLg**2/(4*MG2*Sg**2)-pLg*pSg/(2*MG2*Sg)-MG2*Lg*Sg**2*Rg/2+pg*sp.sqrt(1+thgr**2/Lg**2)
    cf=Lf*pLf**2/(4*MF2*Sf**2)-pLf*pSf/(2*MF2*Sf)-MF2*Lf*Sf**2*Rf/2+pf*sp.sqrt(1+thfr**2/Lf**2)
    dg=pSg*sp.diff(Sg,R)-Lg*sp.diff(pLg,R)+pg*thgr
    df=pSf*sp.diff(Sf,R)-Lf*sp.diff(pLf,R)+pf*thfr
    Hg=cg+z*dg/Lg+Wg
    Hf=cf+z*dg/Lf+Wf
    residuals={
        'Hg':Hg,'Hf':Hf,'Ddiag':dg+df,'Fz':dg-K*z/root,
        'Dg':dg,'Df':df,'pg':pg,'pf':pf,'z':z,'K':K,
        'Lg':Lg,'Sg':Sg,'Lf':Lf,'Sf':Sf,
        'pLg':pLg,'pSg':pSg,'pLf':pLf,'pSf':pSf,
        'tg':tg,'tf':tf,'thgr':thgr,'thfr':thfr,
        'R3g':Rg,'R3f':Rf,'root':root,
        'Wg':Wg,'Wf':Wf, 'Cgg':cg,'Cff':cf,
    }
    return CurvedPrimary(residuals,dict(a=a,b=b,y=y,curv_g=curv_g,curv_f=curv_f,
                                       z_slope=z_slope,theta_g=theta_g,theta_f=theta_f,
                                       grav_g=grav_g,grav_f=grav_f,f_delta=tuple(float(v) for v in f_delta)))


def assert_regular(witness, radii=np.linspace(.12,.88,11),tol=3.e-10):
    r=np.asarray(radii,float)
    fields=('Hg','Hf','Ddiag','Fz','pg','pf','z','K','R3g','R3f','thgr','thfr','Dg','Df')
    vals=witness.eval(r,fields)
    residual=np.max(abs(vals[:4]))
    if residual>tol:raise ArithmeticError(f'primary residual {residual} exceeds {tol}')
    if min(np.min(vals[4]),np.min(vals[5]))<=0:
        raise ArithmeticError('at least one dust canonical momentum is nonpositive')
    if min(np.abs(vals[7]))<1.e-8 or max(abs(vals[6]))>=1:
        raise ArithmeticError('degenerate relative-shift root')
    return {'primary_max':float(residual),'dust_g_min':float(np.min(vals[4])),
            'dust_f_min':float(np.min(vals[5])), 'max_abs_z':float(np.max(np.abs(vals[6]))),
            'curvature_g_max':float(np.max(abs(vals[8]))),
            'curvature_f_max':float(np.max(abs(vals[9]))),
            'phase_g_max':float(np.max(abs(vals[10]))),
            'phase_f_max':float(np.max(abs(vals[11]))),
            'Dg_max':float(np.max(abs(vals[12])))}

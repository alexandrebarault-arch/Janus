"""Spherically reduced Hassan--Rosen mixed Hamiltonian functional bracket.

Two positive Einstein--Hilbert ADM sectors and TWO distinct irrotational dust
canonical pairs. Computes actual Euler--Lagrange functional derivatives of
radially smeared lapse-linear primary Hamiltonians, including all spatial
curvature and gravitational momentum derivative terms. The algebraic relative
shift z is either a fixed external scalar or set to its exact lapse-independent
root. A nonzero off-shell bracket is NOT by itself the BD secondary: one must
still perform the complete Dirac time preservation and constraint rank test.

Unit solid angle, r in (r_min,r_max) with compact lapse smearings; this is
not a complete gauge reduction or a proof of 4D bimetric ghost freedom.
"""
from __future__ import annotations
from functools import lru_cache
from dataclasses import dataclass
import math
import numpy as np
import sympy as sp
from numpy.polynomial import Polynomial as Poly

CANONICAL_PAIRS = (("Lg","pLg"),("Sg","pSg"),("tg","pg"),
                   ("Lf","pLf"),("Sf","pSf"),("tf","pf"))
Q = tuple(v for pair in CANONICAL_PAIRS for v in pair)
DEFAULT_BETAS=(.2,1.3,-.35,.4,-.17)
DEFAULT_M2=.91
DEFAULT_MG2=1.7
DEFAULT_MF2=.63
BOUNDS=(.1,.9)


def default_fields():
    # Same nonhomogeneous smooth canonical benchmark as the verified Step33d
    # spatial Ward. No canonical pair is omitted or related to the other.
    return {
        'Lg':Poly([1.12,.13,.04]), 'Sg':Poly([0.,.88,.07]),
        'pLg':Poly([0.,0.,-.12,.031]), 'pSg':Poly([0.,-.088,.022]),
        'tg':Poly([.1,.08,-.014]), 'pg':Poly([0.,0.,.17,.026]),
        'Lf':Poly([.96,.08,.035]), 'Sf':Poly([0.,.73,.06]),
        'pLf':Poly([0.,0.,-.072,.02]), 'pSf':Poly([0.,-.062,.012]),
        'tf':Poly([-.07,.052,.017]), 'pf':Poly([0.,0.,.12,.016]),
    }


def compact_smearings():
    a,b=BOUNDS
    profile=Poly([-a,1.])**3 * Poly([b,-1.])**3
    return profile*(Poly([1.,.4])),profile*Poly([.7,-.3,.5])


def _check_fields(fields):
    if set(fields)!=set(Q) or not all(isinstance(fields[q],Poly) for q in Q):
        raise ValueError('all twelve canonical radial polynomial fields required')


def _k_polynomial(fields, *,betas,m2,mg2):
    b0,b1,b2,b3,b4=betas
    Lg,Lf,Sg,Sf=(fields[k] for k in ('Lg','Lf','Sg','Sf'))
    return m2*mg2*Lg*Lf*(b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf)


def relative_shift_jet(fields, *,betas=DEFAULT_BETAS,m2=DEFAULT_M2,mg2=DEFAULT_MG2,r):
    """Exact z*,z*',z*'' after eliminating *lapse-independent* relative shift.

    Use u=Dg/K, z=u/sqrt(1+u²), preserving signs also for K<0.
    Dg=pSg*Sg'-Lg*pLg'+pg*tg', with TWO species still distinct.
    No root is selected on the degenerate K=0 branch.
    """
    _check_fields(fields)
    if len(betas)!=5 or not all(math.isfinite(float(x)) for x in (*betas,m2,mg2)) or m2<=0 or mg2<=0:
        raise ValueError('finite five betas and positive m², Mg² required')
    D=fields['pSg']*fields['Sg'].deriv()-fields['Lg']*fields['pLg'].deriv()+fields['pg']*fields['tg'].deriv()
    K=_k_polynomial(fields,betas=betas,m2=m2,mg2=mg2)
    d,d1,d2=(D.deriv(k)(r) for k in (0,1,2))
    k,k1,k2=(K.deriv(j)(r) for j in (0,1,2))
    if abs(k)<1e-13 or not all(np.isfinite(v) for v in (d,d1,d2,k,k1,k2)):
        raise ValueError('degenerate or nonfinite relative-shift K')
    u=d/k
    u1=d1/k-d*k1/(k*k)
    u2=d2/k-2*d1*k1/(k*k)-d*k2/(k*k)+2*d*k1*k1/(k**3)
    den=np.sqrt(1+u*u)
    z=u/den
    z1=u1/den**3
    z2=u2/den**3-3*u*u1*u1/den**5
    return z,z1,z2


def _smeared_lagrangians():
    # N,N1 and M,M1 are independent compact test smearing jets.
    q={k:sp.Symbol(k,real=True) for k in Q}
    q1={k:sp.Symbol(k+'_r',real=True) for k in Q}
    q2={k:sp.Symbol(k+'_rr',real=True) for k in Q}
    z,zr,zrr,N,Nr,Nrr,M,Mr,Mrr=sp.symbols('z zr zrr N Nr Nrr M Mr Mrr',real=True)
    beta=sp.symbols('b0:5',real=True)
    m2,mg2,mf2=sp.symbols('m2 mg2 mf2',positive=True,real=True)
    Lg,Sg,plg,psg,tg,pg,Lf,Sf,plf,psf,tf,pf=[q[k] for k in ('Lg','Sg','pLg','pSg','tg','pg','Lf','Sf','pLf','pSf','tf','pf')]
    Sgr,Sfr,tgr,tfr=[q1[k] for k in ('Sg','Sf','tg','tf')]
    Lgr,Lfr=[q1[k] for k in ('Lg','Lf')]
    b0,b1,b2,b3,b4=beta
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    As=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    root=sp.sqrt(1-z*z)
    Wg=m2*mg2*(Lg*A0+Lf*At*root)
    Wf=m2*mg2*(Lf*As+Lg*At*root)
    # The gravitational intrinsic curvature R3 in each C_EH has been
    # EXACTLY radially integrated by parts, with zero lapse at boundaries:
    # int N[-M² L+M² Sr²/L+2M² S(Sr/L)'] dr
    #   = int [-M² N L -M² N Sr²/L -2M² N' S Sr/L] dr.
    kin_g=Lg*plg**2/(4*mg2*Sg**2)-plg*psg/(2*mg2*Sg)
    kin_f=Lf*plf**2/(4*mf2*Sf**2)-plf*psf/(2*mf2*Sf)
    dg_no_plr=psg*Sgr+pg*tgr
    dustg=pg*sp.sqrt(1+tgr*tgr/(Lg*Lg))
    dustf=pf*sp.sqrt(1+tfr*tfr/(Lf*Lf))
    # -N z pLg' and -M z Lg pLg'/Lf also integrated by parts.
    Fg=(N*(kin_g+dustg-mg2*Lg-mg2*Sgr*Sgr/Lg+Wg+z*dg_no_plr/Lg)
        -2*mg2*Nr*Sg*Sgr/Lg+(Nr*z+N*zr)*plg)
    A=M*z*Lg/Lf
    Ar=(Mr*z*Lg/Lf+M*zr*Lg/Lf+M*z*Lgr/Lf-M*z*Lg*Lfr/Lf**2)
    Ff=(M*(kin_f+dustf-mf2*Lf-mf2*Sfr*Sfr/Lf+Wf+z*dg_no_plr/Lf)
        -2*mf2*Mr*Sf*Sfr/Lf+Ar*plg)
    symbols=[q[k] for k in Q]+[q1[k] for k in Q]+[q2[k] for k in Q]
    symbols += [z,zr,zrr,N,Nr,Nrr,M,Mr,Mrr,m2,mg2,mf2,*beta]
    # d/dr = chain rule on all independent field and smearing jets.
    # Partial derivatives are symbolic/EXACT. The radial total derivative of
    # dF/dq_r is evaluated with complex-step differentiation of the whole
    # smooth radial profile. This prevents exponential expression swell from
    # expanding an Euler gradient containing up to z*(r) second derivatives.
    partials=[]
    for F in (Fg,Ff):
        partials.append(([sp.diff(F,q[name]) for name in Q],
                         [sp.diff(F,q1[name]) for name in Q]))
    return symbols,Fg,Ff,partials


@lru_cache(maxsize=1)
def _compiled():
    syms,Fg,Ff,partials=_smeared_lagrangians()
    evaluator=sp.lambdify(syms, [Fg,Ff,*partials[0][0],*partials[0][1],
                                    *partials[1][0],*partials[1][1]],
                         modules='numpy',cse=True)
    return evaluator


def _nodes(order,a,b):
    if type(order) is not int or order<12 or not all(math.isfinite(v) for v in (a,b)) or not 0<a<b:
        raise ValueError('finite regular radial interval and quadrature order >=12')
    x,w=np.polynomial.legendre.leggauss(order)
    return (a+b)/2+(b-a)*x/2, (b-a)*w/2


def _sample(fields,N,M,r,*,z_mode,betas,m2,mg2,mf2,z_fixed):
    for s in (mg2,mf2,m2,*betas):
        if not math.isfinite(float(s)):raise ValueError('nonfinite parameter')
    if mg2<=0 or mf2<=0 or m2<0 or len(betas)!=5:
        raise ValueError('positive Planck couplings, nonnegative mass², five betas')
    vals=[]
    for k in (0,1,2):
        for field in Q:
            vals.append(fields[field].deriv(k)(r))
    if z_mode=='root':
        zvals=relative_shift_jet(fields,betas=betas,m2=m2,mg2=mg2,r=r)
    elif z_mode=='fixed':
        if not isinstance(z_fixed,Poly):raise ValueError('fixed z requires polynomial')
        zvals=tuple(z_fixed.deriv(k)(r) for k in range(3))
    else:raise ValueError('z_mode must be root or fixed')
    if abs(zvals[0])>=1:raise ValueError('nonreal HR shift')
    vals+=list(zvals)
    for func in (N,M):
        vals += [func.deriv(k)(r) for k in range(3)]
    vals += [m2,mg2,mf2,*betas]
    return vals


@dataclass(frozen=True)
class MixedBracket:
    bracket:float
    sector_contributions:tuple[float,float,float,float,float,float]
    hg_integral:float
    hf_integral:float
    shift_equation_max:float
    independent_dust_pairs:int=2


def mixed_smeared_poisson(fields=None,N=None,M=None,*,z_mode='root',
                          z_fixed=None,order=48,interval=BOUNDS,
                          betas=DEFAULT_BETAS,m2=DEFAULT_M2,
                          mg2=DEFAULT_MG2,mf2=DEFAULT_MF2):
    """Mixed {H_g[N],H_f[M]} from ALL twelve exact functional derivatives.

    In root mode, the z EOM F_z=0 makes each H_i separately stationary
    under δz, so the envelope theorem permits the same fixed-z partial
    functional derivative *evaluated* at z*(fields),z*',z*''.
    This is a necessary local Dirac-analysis input, NOT an on-shell
    secondary BD constraint: full primary-preservation/lapse fixing absent.
    """
    fields=default_fields() if fields is None else fields
    _check_fields(fields)
    if N is None or M is None:
        n,mm=compact_smearings()
        N=n if N is None else N
        M=mm if M is None else M
    if not isinstance(N,Poly) or not isinstance(M,Poly):
        raise ValueError('polynomial compact lapse smearings required')
    a,b=interval
    if any(abs(q(v))>2e-10 for q in (N,M) for v in (a,b)):
        raise ValueError('both smearing functions must vanish at radial endpoints')
    r,w=_nodes(order,a,b)
    evaluate=_compiled()
    contributions=np.zeros(6)
    hg=hf=0.
    maxshift=0.
    for ri,wi in zip(r,w):
        v=_sample(fields,N,M,float(ri),z_mode=z_mode,betas=betas,
                  m2=m2,mg2=mg2,mf2=mf2,z_fixed=z_fixed)
        values=np.asarray(evaluate(*v),float)
        eps=1.e-18
        vc=_sample(fields,N,M,complex(ri,eps),z_mode=z_mode,betas=betas,
                   m2=m2,mg2=mg2,mf2=mf2,z_fixed=z_fixed)
        radial=np.asarray(evaluate(*vc),complex)
        if values.shape!=(50,) or not np.all(np.isfinite(values)):
            raise ArithmeticError('invalid partial functional gradients')
        hg+=wi*values[0];hf+=wi*values[1]
        dg=values[2:14]-np.imag(radial[14:26])/eps
        df=values[26:38]-np.imag(radial[38:50])/eps
        for i,(qq,pp) in enumerate(CANONICAL_PAIRS):
            qi=2*i;pi=2*i+1
            contributions[i]+=wi*(dg[qi]*df[pi]-dg[pi]*df[qi])
        # Exact algebraic relative-shift F=Dg-K z/sqrt(1-z²).
        if z_mode=='root':
            D=(fields['pSg']*fields['Sg'].deriv()-fields['Lg']*fields['pLg'].deriv()
               +fields['pg']*fields['tg'].deriv())(ri)
            K=_k_polynomial(fields,betas=betas,m2=m2,mg2=mg2)(ri)
            z=v[36]
            maxshift=max(maxshift,abs(float(D-K*z/math.sqrt(1-z*z))))
    return MixedBracket(float(sum(contributions)),tuple(map(float,contributions)),
                        float(hg),float(hf),float(maxshift))


def smeared_primary(fields,N,M,*,z_mode='root',z_fixed=None,order=48,
                   interval=BOUNDS,betas=DEFAULT_BETAS,m2=DEFAULT_M2,
                   mg2=DEFAULT_MG2,mf2=DEFAULT_MF2):
    """Integrated-by-parts primary actions for independent variation tests."""
    _check_fields(fields)
    a,b=interval
    if any(abs(q(v))>2e-10 for q in (N,M) for v in (a,b)):
        raise ValueError('smearings must vanish at both boundaries')
    r,w=_nodes(order,a,b)
    ev=_compiled()
    out=np.zeros(2)
    for ri,wi in zip(r,w):
        v=_sample(fields,N,M,float(ri),z_mode=z_mode,betas=betas,
                  m2=m2,mg2=mg2,mf2=mf2,z_fixed=z_fixed)
        out+=wi*np.asarray(ev(*v)[:2],float)
    return out


def functional_gradients_at(fields,N,M,r,*,z_mode='root',z_fixed=None,
                            betas=DEFAULT_BETAS,m2=DEFAULT_M2,
                            mg2=DEFAULT_MG2,mf2=DEFAULT_MF2,
                            complex_step=1.e-18):
    """Return the 2x12 exact Euler functional gradient at one radial point.

    The density's partial derivatives wrt the independent canonical field
    jets are symbolic. The radial derivative d/dr(dF/dq') is evaluated by
    complex-step differentiation of those analytic functions, including
    z*',z*'' if the relative shift is eliminated. A caller can check these
    gradients by varying the independently integrated full primary action.
    """
    _check_fields(fields)
    if not math.isfinite(complex_step) or complex_step<=0 or not BOUNDS[0]<r<BOUNDS[1]:
        raise ValueError('positive complex step and interior radial point required')
    base=_sample(fields,N,M,float(r),z_mode=z_mode,z_fixed=z_fixed,
                 betas=betas,m2=m2,mg2=mg2,mf2=mf2)
    move=_sample(fields,N,M,complex(r,complex_step),z_mode=z_mode,
                 z_fixed=z_fixed,betas=betas,m2=m2,mg2=mg2,mf2=mf2)
    evaluator=_compiled()
    val=np.asarray(evaluator(*base),float)
    moved=np.asarray(evaluator(*move),complex)
    if not np.all(np.isfinite(val)) or not np.all(np.isfinite(moved)):
        raise ArithmeticError('nonfinite radial canonical gradient')
    g=val[2:14]-np.imag(moved[14:26])/complex_step
    f=val[26:38]-np.imag(moved[38:50])/complex_step
    return np.vstack((g,f))

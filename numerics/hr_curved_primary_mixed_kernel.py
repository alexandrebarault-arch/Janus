"""Local mixed H_g-H_f Poisson bracket on curved/moving two-dust data.

Independent symbolic functional gradients of the ORIGINAL two spherical
canonical Hamiltonians after exact radial IBP; complex-step evaluates
spatial Euler total derivatives. Same six canonical pairs as Step33e.

Only tested on regular primary-satisfying initial data; not a Dirac
secondary-preservation or physical BD proof.
"""
from __future__ import annotations
from functools import lru_cache
import numpy as np
import sympy as sp
from .hr_curved_moving_dust_primary import R,CurvedPrimary,BETA,M2,MG2,MF2

Q=('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')

@lru_cache(maxsize=1)
def _compiled():
    q={k:sp.Symbol(k) for k in Q}
    qr={k:sp.Symbol(k+'_r') for k in Q}
    z,zr,N,Nr,M,Mr=sp.symbols('z zr N Nr M Mr')
    mg2,mf2,m2=sp.symbols('Mg2 Mf2 m2')
    b0,b1,b2,b3,b4=sp.symbols('beta0:5')
    Lg,plg,Sg,psg,tg,pg,Lf,plf,Sf,psf,tf,pf=[q[k] for k in Q]
    Lgr,Sgr,tgr,Lfr,Sfr,tfr=[qr[k] for k in ('Lg','Sg','tg','Lf','Sf','tf')]
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    Wg=m2*mg2*(Lg*A0+Lf*At*sp.sqrt(1-z*z))
    Wf=m2*mg2*(Lf*As+Lg*At*sp.sqrt(1-z*z))
    kin_g=Lg*plg**2/(4*mg2*Sg**2)-plg*psg/(2*mg2*Sg)
    kin_f=Lf*plf**2/(4*mf2*Sf**2)-plf*psf/(2*mf2*Sf)
    dg_noplr=psg*Sgr+pg*tgr
    dustg=pg*sp.sqrt(1+tgr*tgr/Lg**2)
    dustf=pf*sp.sqrt(1+tfr*tfr/Lf**2)
    # Intrinsic spherical curvature integrated by parts (compact lapses).
    Fg=N*(kin_g+dustg-mg2*Lg-mg2*Sgr**2/Lg+Wg+z*dg_noplr/Lg)
    Fg+=-2*mg2*Nr*Sg*Sgr/Lg+(Nr*z+N*zr)*plg
    a=M*z*Lg/Lf
    ar=Mr*z*Lg/Lf+M*zr*Lg/Lf+M*z*Lgr/Lf-M*z*Lg*Lfr/Lf**2
    Ff=M*(kin_f+dustf-mf2*Lf-mf2*Sfr**2/Lf+Wf+z*dg_noplr/Lf)
    Ff+=-2*mf2*Mr*Sf*Sfr/Lf+ar*plg
    variables=[q[k] for k in Q]+[qr[k] for k in Q]
    variables +=[z,zr,N,Nr,M,Mr,mg2,mf2,m2,b0,b1,b2,b3,b4]
    # 2 density + 24 q partial + 24 q' partial = 50 symbols.
    eqs=[Fg,Ff]
    for F in (Fg,Ff):
        eqs += [sp.diff(F,q[k]) for k in Q]
        eqs += [sp.diff(F,qr[k]) for k in Q]
    return sp.lambdify(variables,eqs,modules='numpy',cse=True)


class CurvedLocalKernel:
    def __init__(self,coeffs,g,f,r):
        self.coefficients=coeffs
        self.g_euler=g
        self.f_euler=f
        self.r=r


def _sample(w:CurvedPrimary,r,N,Nr,M,Mr):
    vals=[]
    for i in (0,1):
        for key in Q:
            vals.append(w.expr[key].diff(R,i).subs(R,r))
    zz=w.expr['z']
    vals +=[zz.subs(R,r),zz.diff(R).subs(R,r),N,Nr,M,Mr,MG2,MF2,M2,*BETA]
    return [complex(x) if isinstance(r,complex) else float(x) for x in vals]


def local_curved_bracket(w:CurvedPrimary,r=.43,step=1e-18):
    """Nine smearing-jet coefficients K_ij at a constrained curved point.

    Samples every one of SIX canonical pairs. All 12 q and q' partials
    are symbolic; the radial total derivative d/dr(partial F/partial q')
    is complex-step differentiated along the full curved canonical data.
    """
    if not 0.05<r<.95 or not step>0:raise ValueError('interior regular radius and step required')
    ev=_compiled()
    g=np.zeros((3,12));f=np.zeros((3,12))
    for j in range(3):
        N=[float(j==0),0.,0.]; M=[float(j==0),0.,0.]
        if j==1:N=[0.,1.,0.];M=[0.,1.,0.]
        if j==2:N=[0.,0.,1.];M=[0.,0.,1.]
        # For smearing of the quadratic derivative jet: N''=1 at r0.
        # N and N' at r+i eps must obey N(r+i eps)=N0+i eps*N1
        # and N'(r+i eps)=N1+i eps*N2.
        for sector in (0,1):
            def arguments(move):
                e=complex(0.,step) if move else 0.
                ns=N[0]+e*N[1]; nrs=N[1]+e*N[2]
                ms=M[0]+e*M[1]; mrs=M[1]+e*M[2]
                if sector==0:ms=0.;mrs=0.
                else:ns=0.;nrs=0.
                return _sample(w,r+e,ns,nrs,ms,mrs)
            x=np.asarray(ev(*arguments(False)),float)
            y=np.asarray(ev(*arguments(True)),complex)
            euler=x[2+24*sector:14+24*sector]-np.imag(y[14+24*sector:26+24*sector])/step
            if sector==0:g[j]=euler
            else:f[j]=euler
    out=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            out[i,j]=sum(g[i,2*k]*f[j,2*k+1]-g[i,2*k+1]*f[j,2*k] for k in range(6))
    return CurvedLocalKernel(out,g,f,r)

"""Step37 finite-radius curved/noncomoving SECONDARY collocation continuation.

Uses the EXISTING Step33g physical primary builder and symbolic Euler partials.
No independent field-theoretic BD rank/lapse preservation is established.
Input primary generator must accept the new optional f_delta polynomial.
"""
import numpy as np
import sympy as sp
from numpy.polynomial import Polynomial
from .hr_curved_moving_dust_primary import R, build_primary, BETA, M2, MG2, MF2
from .hr_curved_primary_mixed_kernel import Q, _compiled


def kernel_fast(w,r=.43,step=1e-20):
    """Full six-pair mixed Hamiltonian jet with cached native field sampling."""
    if not (.025<r<.9 and step>0):
        raise ValueError('interior radius and positive complex step required')
    key='step37_lambdified_q_and_qr'
    if key not in w._cache:
        w._cache[key]=sp.lambdify(R,
            [w.expr[k] for k in Q]+[sp.diff(w.expr[k],R) for k in Q]
            +[w.expr['z'],sp.diff(w.expr['z'],R)],'numpy',cse=True)
    sample=w._cache[key]
    real=np.asarray(sample(r),float)
    pert=np.asarray(sample(r+1j*step),complex)
    constants=[MG2,MF2,M2,*BETA]
    g=np.zeros((3,12));f=np.zeros((3,12))
    compiled=_compiled()
    for i in range(3):
        for sector in (0,1):
            N=float(sector==0 and i==0)
            Nr=float(sector==0 and i==1)
            M=float(sector==1 and i==0)
            Mr=float(sector==1 and i==1)
            N2=float(sector==0 and i==2)
            M2jet=float(sector==1 and i==2)
            v=np.asarray(compiled(*real,N,Nr,M,Mr,*constants),float)
            vc=np.asarray(compiled(*pert,N+1j*step*Nr,Nr+1j*step*N2,
                     M+1j*step*Mr,Mr+1j*step*M2jet,*constants),complex)
            start=2+24*sector
            grad=v[start:start+12]-np.imag(vc[start+12:start+24])/step
            if sector==0:g[i]=grad
            else:f[i]=grad
    out=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            out[i,j]=sum(g[i,2*k]*f[j,2*k+1]-g[i,2*k+1]*f[j,2*k]
                         for k in range(6))
    return out


def local_candidate(w,r=.43,h=.001):
    """C=K00-K01' on primary witness, with separate derivative-Ward check."""
    if not h>0 or r-h<=.025 or r+h>=.9:
        raise ValueError('radial derivative stencil outside domain')
    a=kernel_fast(w,r-h);b=kernel_fast(w,r);c=kernel_fast(w,r+h)
    d01=(c[0,1]-a[0,1])/(2*h)
    d20=(c[2,0]-a[2,0])/(2*h)
    return float(b[0,0]-d01),float(b[0,1]-b[1,0]+d20)


def solve_even_center(*,scale=.1,degree=4,iterations=3,h=.001):
    """Numerical preconditioned collocation, not continuous exact C=0 proof.

    Free Pf generator is Qf=(pLf)'/[2r] at flat background, NOT pLf/r².
    Therefore the inverse factor (n+2)/2 is mandatory for r^n.
    """
    if not (0<=scale<=.2 and 1<=degree<=6 and 1<=iterations<=6):
        raise ValueError('restricted smooth low-amplitude continuation')
    fit_r=np.linspace(.05,.85,max(18,4*degree+2))
    val_r=np.array([.04,.11,.21,.31,.41,.51,.61,.71,.83])
    y=.5787707228025044;a=.4;b=a*y
    J=BETA[1]+2*BETA[2]*y+BETA[3]*y*y
    A=.5*M2*MG2*a*a*J
    if J<=0 or A<=0:raise ValueError('nondegenerate J>0 required')
    delta=np.zeros(2*degree+1)
    history=[]
    for i in range(iterations+1):
        w=build_primary(curv_g=.015*scale,curv_f=-.012*scale,
            z_slope=.04*scale,theta_g=.012*scale,theta_f=-.016*scale,
            grav_g=0.,grav_f=0.,f_delta=tuple(delta))
        C=np.array([local_candidate(w,float(r),h)[0] for r in fit_r])
        V=np.array([local_candidate(w,float(r),h)[0] for r in val_r])
        E=w.eval(val_r,('Hg','Hf','Ddiag','Fz','pg','pf','z','K'))
        history.append({'iteration':i,'max_C':float(np.max(np.abs(V))),
             'max_C_div_r2':float(np.max(np.abs(V/val_r**2))),
             'max_primary':float(np.max(np.abs(E[:4]))),
             'min_pg':float(np.min(E[4])),'min_pf':float(np.min(E[5])),
             'min_abs_K':float(np.min(abs(E[7]))),
             'max_abs_z':float(np.max(abs(E[6]))),
             'f_delta':list(map(float,delta))})
        if i==iterations:break
        p=Polynomial.fit(fit_r**2,C/fit_r**2,degree,domain=[0.,.85**2]).convert()
        for k,v in enumerate(p.coef):
            n=2*k
            delta[n]+=MF2*b*v*(n+2)/(2*A*(n+3))
    return {'scale':scale,'degree':degree,'iterations':iterations,
            'fit_radius':[float(fit_r.min()),float(fit_r.max())],
            'validation_radii':val_r.tolist(),'history':history,
            'verdict':'FINITE_RADIAL_COLLOCATION_NOT_EXACT_DIRAC_SECONDARY'}

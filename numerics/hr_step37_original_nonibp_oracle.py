"""Independent original non-IBP second-order finite-difference radial Poisson oracle.

Unlike hr_step37_curved_solver's analytic Euler-IBP derivatives,
this perturbs every canonical grid node, differentiating UNINTEGRATED EH 3D
curvature and pL' numerically, and re-solving shift z at each perturbation.
Near-secondary data are prone to O(dr²) discretization error; verify both
resolution convergence and the continuum IBP kernel separately.
"""
import numpy as np
import sympy as sp
from .hr_curved_moving_dust_primary import R,BETA,M2,MG2,MF2
from .hr_curved_primary_mixed_kernel import Q


def sample_canonical(w,r):
    fn=sp.lambdify(R,[w.expr[k] for k in Q],modules='numpy',cse=True)
    return np.asarray(np.broadcast_arrays(*[np.asarray(x)+np.zeros_like(r) for x in fn(r)]),float)


def _deriv(x,r):
    dr=r[1]-r[0]
    z=np.empty_like(x)
    z[1:-1]=(x[2:]-x[:-2])/(2*dr)
    z[0]=(-3*x[0]+4*x[1]-x[2])/(2*dr)
    z[-1]=(3*x[-1]-4*x[-2]+x[-3])/(2*dr)
    return z


def hamiltonians(q,r):
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    Sgr,Sfr=_deriv(Sg,r),_deriv(Sf,r)
    tgr,tfr=_deriv(tg,r),_deriv(tf,r)
    pLgr=_deriv(pLg,r)
    Wg0=Sgr/Lg;Wf0=Sfr/Lf
    Rg=2/Sg**2*(1-Wg0**2-2*Sg/Lg*_deriv(Wg0,r))
    Rf=2/Sf**2*(1-Wf0**2-2*Sf/Lf*_deriv(Wf0,r))
    b0,b1,b2,b3,b4=BETA
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=M2*MG2*Lg*Lf*At
    Dg=pSg*Sgr-Lg*pLgr+pg*tgr
    z=Dg/np.sqrt(K*K+Dg*Dg) # tested K>0 only
    root=np.sqrt(1-z*z)
    WG=M2*MG2*(Lg*A0+Lf*At*root)
    WF=M2*MG2*(Lf*As+Lg*At*root)
    Cg=Lg*pLg**2/(4*MG2*Sg**2)-pLg*pSg/(2*MG2*Sg)-MG2*Lg*Sg**2*Rg/2+pg*np.sqrt(1+(tgr/Lg)**2)
    Cf=Lf*pLf**2/(4*MF2*Sf**2)-pLf*pSf/(2*MF2*Sf)-MF2*Lf*Sf**2*Rf/2+pf*np.sqrt(1+(tfr/Lf)**2)
    return Cg+z*Dg/Lg+WG,Cf+z*Dg/Lf+WF


def _compact_smears(r):
    x=(r-.2)/(.7-.2)
    N=np.where((r>.2)&(r<.7),np.sin(np.pi*x)**4,0.)
    M=N*(1+.2*np.sin(2*np.pi*x))
    return N,M


def original_pb(w,n=201,step=1e-21):
    if n<30 or n>1001:raise ValueError('reasonable collocation range required')
    r=np.linspace(.1,.9,n)
    q=sample_canonical(w,r)
    N,M=_compact_smears(r)
    dr=r[1]-r[0]
    g=np.zeros_like(q)
    f=np.zeros_like(q)
    for i in range(12):
        for j in range(1,n-1):
            p=q.astype(complex)
            p[i,j]+=1j*step
            h1,h2=hamiltonians(p,r)
            g[i,j]=np.imag(np.dot(N,h1))*dr/step
            f[i,j]=np.imag(np.dot(M,h2))*dr/step
    pairs=np.array([np.dot(g[2*i,1:-1],f[2*i+1,1:-1])-
                    np.dot(g[2*i+1,1:-1],f[2*i,1:-1]) for i in range(6)]) /dr
    h1,h2=hamiltonians(q,r)
    return {'n':int(n),'dr':float(dr),'bracket':float(pairs.sum()),
            'pair_contributions':pairs.tolist(),'max_abs_discrete_primary':
            float(max(np.max(abs(h1[12:-12])),np.max(abs(h2[12:-12])))),
            'min_pg':float(np.min(q[5])),'min_pf':float(np.min(q[11]))}

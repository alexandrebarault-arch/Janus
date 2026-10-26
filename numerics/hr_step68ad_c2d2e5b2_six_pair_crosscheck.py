"""Step68ad-C2d2e5b2: six-canonical-pair NON-IBP vs IBP grid cross-check.

OFF SHELL ONLY. Finite-difference collocation, not a functional Dirac rank proof.
Reconstructs the exact density formulas read from authenticated GitHub blobs:
nonIBP 005449ade6e3582e3b9a5c3374a881a77e73e3f6,
IBP 6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81,
ADM c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41.
The source modules themselves are not executed by this script.
"""
import numpy as np
from time import perf_counter
BETA=(.2,1.3,-.35,.4,-.17)
M2=.91;MG2=1.7;MF2=.63

def q_fields(r):
    return np.array([
        1.12+.13*r+.04*r*r,
        -.12*r*r+.031*r**3,
        .88*r+.07*r*r,
        -.088*r+.022*r*r,
        .1+.08*r-.014*r*r,
        .17*r*r+.026*r**3,
        .96+.08*r+.035*r*r,
        -.072*r*r+.02*r**3,
        .73*r+.06*r*r,
        -.062*r+.012*r*r,
        -.07+.052*r+.017*r*r,
        .12*r*r+.016*r**3,
    ])

def deriv(x,dr):
    y=np.empty_like(x)
    y[1:-1]=(x[2:]-x[:-2])/(2*dr)
    y[0]=(-3*x[0]+4*x[1]-x[2])/(2*dr)
    y[-1]=(3*x[-1]-4*x[-2]+x[-3])/(2*dr)
    return y

def densities(q,dr,kind='original',frozen_z=None):
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    Sgr,Sfr=deriv(Sg,dr),deriv(Sf,dr)
    tgr,tfr=deriv(tg,dr),deriv(tf,dr)
    pLgr=deriv(pLg,dr)
    Wg0=Sgr/Lg; Wf0=Sfr/Lf
    Rg=2/Sg**2*(1-Wg0**2-2*Sg/Lg*deriv(Wg0,dr))
    Rf=2/Sf**2*(1-Wf0**2-2*Sf/Lf*deriv(Wf0,dr))
    b0,b1,b2,b3,b4=BETA
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=M2*MG2*Lg*Lf*At
    Dg=pSg*Sgr-Lg*pLgr+pg*tgr
    if np.any(np.real(K)<=0): raise ValueError('requires regular K>0 chart')
    z=Dg/np.sqrt(K*K+Dg*Dg) if frozen_z is None else frozen_z
    root=np.sqrt(1-z*z)
    WG=M2*MG2*(Lg*A0+Lf*At*root)
    WF=M2*MG2*(Lf*As+Lg*At*root)
    Cg=Lg*pLg**2/(4*MG2*Sg**2)-pLg*pSg/(2*MG2*Sg)-MG2*Lg*Sg**2*Rg/2+pg*np.sqrt(1+(tgr/Lg)**2)
    Cf=Lf*pLf**2/(4*MF2*Sf**2)-pLf*pSf/(2*MF2*Sf)-MF2*Lf*Sf**2*Rf/2+pf*np.sqrt(1+(tfr/Lf)**2)
    return Cg+z*Dg/Lg+WG,Cf+z*Dg/Lf+WF,z,K,Dg

def smear(r):
    x=(r-.2)/(.7-.2)
    N=np.where((r>.2)&(r<.7),np.sin(np.pi*x)**4,0.)
    M=N*(1+.2*np.sin(2*np.pi*x))
    return N,M

def gradients(q,r,step=1e-21,freeze_shift=False):
    dr=r[1]-r[0];n=len(r)
    N,M=smear(r)
    base_z=densities(q,dr)[2] if freeze_shift else None
    g=np.zeros_like(q);f=np.zeros_like(q)
    for i in range(12):
        for j in range(1,n-1):
            p=q.astype(complex)
            p[i,j]+=1j*step
            h1,h2,*_=densities(p,dr,frozen_z=base_z)
            g[i,j]=np.imag(np.dot(N,h1))*dr/step
            f[i,j]=np.imag(np.dot(M,h2))*dr/step
    return g,f

def bracket(q,r,freeze_shift=False):
    dr=r[1]-r[0]
    g,f=gradients(q,r,freeze_shift=freeze_shift)
    pairs=np.array([np.dot(g[2*i,1:-1],f[2*i+1,1:-1])-np.dot(g[2*i+1,1:-1],f[2*i,1:-1]) for i in range(6)])/dr
    return pairs

def ibp_densities(q,dr,N,M):
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    Sgr,Sfr=deriv(Sg,dr),deriv(Sf,dr)
    tgr,tfr=deriv(tg,dr),deriv(tf,dr)
    Lgr,Lfr=deriv(Lg,dr),deriv(Lf,dr)
    Nr,Mr=deriv(N,dr),deriv(M,dr)
    b0,b1,b2,b3,b4=BETA
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=M2*MG2*Lg*Lf*At
    D=pSg*Sgr-Lg*deriv(pLg,dr)+pg*tgr
    if np.any(np.real(K)<=0): raise ValueError('requires regular K>0 chart')
    z=D/np.sqrt(K*K+D*D)
    zr=deriv(z,dr)
    root=np.sqrt(1-z*z)
    WG=M2*MG2*(Lg*A0+Lf*At*root)
    WF=M2*MG2*(Lf*As+Lg*At*root)
    kg=Lg*pLg**2/(4*MG2*Sg**2)-pLg*pSg/(2*MG2*Sg)
    kf=Lf*pLf**2/(4*MF2*Sf**2)-pLf*pSf/(2*MF2*Sf)
    dustg=pg*np.sqrt(1+(tgr/Lg)**2)
    dustf=pf*np.sqrt(1+(tfr/Lf)**2)
    dg=pSg*Sgr+pg*tgr
    fg=N*(kg+dustg-MG2*Lg-MG2*Sgr*Sgr/Lg+WG+z*dg/Lg)-2*MG2*Nr*Sg*Sgr/Lg+(Nr*z+N*zr)*pLg
    ar=Mr*z*Lg/Lf+M*zr*Lg/Lf+M*z*Lgr/Lf-M*z*Lg*Lfr/Lf**2
    ff=M*(kf+dustf-MF2*Lf-MF2*Sfr*Sfr/Lf+WF+z*dg/Lf)-2*MF2*Mr*Sf*Sfr/Lf+ar*pLg
    return fg,ff

def gradients_ibp(q,r,step=1e-21):
    dr=r[1]-r[0];n=len(r)
    N,M=smear(r)
    g=np.zeros_like(q);f=np.zeros_like(q)
    for i in range(12):
        for j in range(1,n-1):
            p=q.astype(complex);p[i,j]+=1j*step
            a,b=ibp_densities(p,dr,N,M)
            g[i,j]=np.imag(sum(a))*dr/step
            f[i,j]=np.imag(sum(b))*dr/step
    return g,f

def bracket_ibp(q,r):
    dr=r[1]-r[0];g,f=gradients_ibp(q,r)
    return np.array([np.dot(g[2*i,1:-1],f[2*i+1,1:-1])-np.dot(g[2*i+1,1:-1],f[2*i,1:-1]) for i in range(6)])/dr

def boundary_B(q,r,N,M):
    dr=r[1]-r[0]
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    Sgr,Sfr=deriv(Sg,dr),deriv(Sf,dr)
    _,_,z,_,_=densities(q,dr)
    return 2*MG2*N*Sg*Sgr/Lg+2*MF2*M*Sf*Sfr/Lf-z*pLg*(N+M*Lg/Lf)



def action_difference(q,r,N,M):
    """Trapezoid integral of (original minus IBP) per lapse sector."""
    dr=r[1]-r[0]
    h1,h2,*_=densities(q,dr)
    fg,ff=ibp_densities(q,dr,N,M)
    return np.array([np.trapezoid(N*h1-fg,r),np.trapezoid(M*h2-ff,r)])


def sector_boundary(q,r,N,M):
    """The two separate primitive boundary jumps [B_g],[B_f]."""
    dr=r[1]-r[0]
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    Sgr,Sfr=deriv(Sg,dr),deriv(Sf,dr)
    _,_,z,_,_=densities(q,dr)
    Bg=2*MG2*N*Sg*Sgr/Lg-z*pLg*N
    Bf=2*MF2*M*Sf*Sfr/Lf-z*pLg*M*Lg/Lf
    return np.array([Bg[-1]-Bg[0],Bf[-1]-Bf[0]])


def audit(ns=(41,81,161,321)):
    rows=[]
    for n in ns:
        r=np.linspace(.1,.9,n);q=q_fields(r)
        p=bracket(q,r);v=bracket_ibp(q,r)
        pf=bracket(q,r,freeze_shift=True)
        h1,h2,z,K,D=densities(q,r[1]-r[0])
        N,M=smear(r)
        a=action_difference(q,r,N,M)
        bc=sector_boundary(q,r,N,M)
        noncompact=action_difference(q,r,np.ones(n),np.ones(n))
        bnc=sector_boundary(q,r,np.ones(n),np.ones(n))
        rows.append({'n':n,'h':float(r[1]-r[0]),'bracket_original':float(sum(p)),
                     'bracket_ibp':float(sum(v)),
                     'pair_original':p.tolist(),'pair_ibp':v.tolist(),
                     'pair_frozen_shift':pf.tolist(),
                     'frozen_shift_bracket_difference':float(sum(p-pf)),
                     'bracket_difference':float(sum(p-v)),
                     'compact_action_difference':a.tolist(),
                     'compact_boundary':bc.tolist(),
                     'noncompact_action_difference':noncompact.tolist(),
                     'noncompact_boundary':bnc.tolist(),
                     'noncompact_boundary_residual':(noncompact-bnc).tolist(),
                     'K_min':float(min(K)),
                     'shift_equation_max':float(max(abs(D-K*z/np.sqrt(1-z*z))))})
    return rows


if __name__=='__main__':
    import json
    print(json.dumps({'status':'NUMERICAL_OFF_SHELL_ONLY','rows':audit()},indent=2))

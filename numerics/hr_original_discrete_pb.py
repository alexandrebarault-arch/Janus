"""Independent grid finite-variation check of original NON-IBP spherical ADM action.

This is a convergence test on constrained *initial data*, NOT Dirac closure or
cosmological stability. Complex-step varies 12 independent canonical fields.
"""
import numpy as np

BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
M2=23.3348939346
MG2=1.
MF2=.10879548725**2
Y=.5787707228025044
CG=.9
Q=('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')


def primary_fields(r,*,curv_g=.015,curv_f=-.012,z_slope=.04,
                   theta_g=.012,theta_f=-.016,grav_g=.04,grav_f=-.035):
    """Analytic original-constraint witness, independently expanded polynomials."""
    a=.4;b=a*Y
    b0,b1,b2,b3,b4=BETA
    vg=b0+3*b1*Y+3*b2*Y**2+b3*Y**3
    H=np.sqrt(CG/(3*a**3)+M2*vg/3)
    pa=-6*MG2*a*a*H;pb=-6*MF2*b*a*H
    result={}
    blocks=[]
    for prefix,A,ms,c,k,grav,pbar in (
        ('g',a,MG2,curv_g,theta_g,grav_g,pa/3),
        ('f',b,MF2,curv_f,theta_f,grav_f,pb/3)):
        u=1+c*r*r
        L=A*u*u; S=L*r
        pL=pbar*(r*r+(2*grav/3)*r**3+2.5*c*r**4+2*c*grav*r**5)
        pLr=pbar*(2*r+2*grav*r*r+10*c*r**3+10*c*grav*r**4)
        theta=A*k*(r*r/2+c*r**4/2+c*c*r**6/6)
        theta_r=k*r*L
        Sr=A*u*(1+5*c*r*r)
        R3=-48*c/(A*A*u**5)
        blocks.append((L,S,pL,pLr,theta,theta_r,Sr,R3,ms))
    Lg,Sg,pLg,pLgr,tg,tgr,Sgr,Rg,_=blocks[0]
    Lf,Sf,pLf,pLfr,tf,tfr,Sfr,Rf,_=blocks[1]
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=M2*MG2*Lg*Lf*At
    z=z_slope*r
    root=np.sqrt(1-z*z)
    D=K*z/root
    Wg=M2*MG2*(Lg*A0+Lf*At*root)
    Wf=M2*MG2*(Lf*As+Lg*At*root)
    def dust(L,S,pL,pLr,th_r,Sr,R3,ms,Dsector,W):
        fac=pL/(2*ms*S*Sr)
        constant=L*pL**2/(4*ms*S**2)-fac*(Dsector+L*pLr)-ms*L*S**2*R3/2+z*D/L+W
        coeff=np.sqrt(1+th_r**2/L**2)+fac*th_r
        p=-constant/coeff
        pS=(Dsector+L*pLr-p*th_r)/Sr
        return p,pS
    pg,pSg=dust(Lg,Sg,pLg,pLgr,tgr,Sgr,Rg,MG2,D,Wg)
    pf,pSf=dust(Lf,Sf,pLf,pLfr,tfr,Sfr,Rf,MF2,-D,Wf,Rf) if False else dust(Lf,Sf,pLf,pLfr,tfr,Sfr,Rf,MF2,-D,Wf)
    return np.stack([Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf]).astype(float)


def hamiltonian(q,r):
    """Original unintegrated EH 3-curvature, shift momentum and dust sqrt.

    NO analytic IBP and NO analytic canonical functional derivatives are used.
    z is eliminated at each (possibly complex) perturbed canonical grid point.
    """
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    dr=r[1]-r[0]
    def deriv(x):
        # Centered 2nd-order interior, 2nd-order one-sided endpoints.
        y=np.empty_like(x)
        y[1:-1]=(x[2:]-x[:-2])/(2*dr)
        y[0]=(-3*x[0]+4*x[1]-x[2])/(2*dr)
        y[-1]=(3*x[-1]-4*x[-2]+x[-3])/(2*dr)
        return y
    Sgr,Sfr=deriv(Sg),deriv(Sf)
    Lgr,Lfr=deriv(Lg),deriv(Lf)
    tgr,tfr=deriv(tg),deriv(tf)
    pLgr,pLfr=deriv(pLg),deriv(pLf)
    Wgr,Wfr=Sgr/Lg,Sfr/Lf
    Rg=2/Sg**2*(1-Wgr**2-2*Sg/Lg*deriv(Wgr))
    Rf=2/Sf**2*(1-Wfr**2-2*Sf/Lf*deriv(Wfr))
    b0,b1,b2,b3,b4=BETA
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=M2*MG2*Lg*Lf*At
    Dg=pSg*Sgr-Lg*pLgr+pg*tgr
    z=Dg/np.sqrt(K*K+Dg*Dg) # branch K>0 throughout the tested neighborhood
    root=np.sqrt(1-z*z)
    Wg=M2*MG2*(Lg*A0+Lf*At*root)
    Wf=M2*MG2*(Lf*As+Lg*At*root)
    Cg=Lg*pLg**2/(4*MG2*Sg**2)-pLg*pSg/(2*MG2*Sg)-MG2*Lg*Sg**2*Rg/2+pg*np.sqrt(1+tgr**2/Lg**2)
    Cf=Lf*pLf**2/(4*MF2*Sf**2)-pLf*pSf/(2*MF2*Sf)-MF2*Lf*Sf**2*Rf/2+pf*np.sqrt(1+tfr**2/Lf**2)
    return Cg+z*Dg/Lg+Wg,Cf+z*Dg/Lf+Wf


def pb_complex_step(q,r,N,M,step=1e-22):
    """Grid canonical bracket: sum_j dHg/dq_j dHf/dp_j / dr, etc."""
    dr=r[1]-r[0]
    n=q.shape[1]
    grad_g=np.zeros_like(q)
    grad_f=np.zeros_like(q)
    for i in range(12):
        for j in range(1,n-1):
            perturb=q.astype(complex)
            perturb[i,j]+=1j*step
            hg,hf=hamiltonian(perturb,r)
            grad_g[i,j]=np.imag(np.dot(N,hg))*dr/step
            grad_f[i,j]=np.imag(np.dot(M,hf))*dr/step
    bracket=sum(np.dot(grad_g[2*k,1:-1],grad_f[2*k+1,1:-1])-
                np.dot(grad_g[2*k+1,1:-1],grad_f[2*k,1:-1]) for k in range(6))/dr
    return float(bracket)


def smearing(r,lo=.2,hi=.7):
    x=(r-lo)/(hi-lo)
    mask=(r>lo)&(r<hi)
    base=np.where(mask,np.sin(np.pi*x)**4,0.)
    twist=.65*np.sin(2*np.pi*x)+.25*np.cos(4*np.pi*x)
    return base,base,base*np.exp(twist),base*np.exp(-twist)


def run(n=251,**kwargs):
    r=np.linspace(.1,.9,n)
    q=primary_fields(r,**kwargs)
    N,M,N2,M2=smearing(r)
    hg,hf=hamiltonian(q,r)
    return {'n':n,'dr':r[1]-r[0], 'min_pg':float(np.min(q[5])), 'min_pf':float(np.min(q[11])),
            'max_abs_Hg_discrete':float(np.max(abs(hg[10:-10]))),
            'max_abs_Hf_discrete':float(np.max(abs(hf[10:-10]))),
            'pb1':pb_complex_step(q,r,N,M),
            'pb2_same_NM':pb_complex_step(q,r,N2,M2)}

if __name__=='__main__':
    import sys,json
    print(json.dumps(run(int(sys.argv[1]) if len(sys.argv)>1 else 251),indent=2))


def exact_primary_checks(r,q,*,curv_g=.015,curv_f=-.012,z_slope=.04,
                         theta_g=.012,theta_f=-.016,grav_g=.04,grav_f=-.035):
    """Evaluate ORIGINAL continuum Hamiltonian and momentum constraints, no grid derivatives."""
    a=.4;b=a*Y
    b0,b1,b2,b3,b4=BETA
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf=q
    ug=1+curv_g*r*r;uf=1+curv_f*r*r
    Sgr=a*ug*(1+5*curv_g*r*r)
    Sfr=b*uf*(1+5*curv_f*r*r)
    vg=b0+3*b1*Y+3*b2*Y*Y+b3*Y**3
    H=np.sqrt(CG/(3*a**3)+M2*vg/3)
    pa=-6*MG2*a*a*H;pb=-6*MF2*b*a*H
    pLgr=pa/3*(2*r+2*grav_g*r*r+10*curv_g*r**3+10*curv_g*grav_g*r**4)
    pLfr=pb/3*(2*r+2*grav_f*r*r+10*curv_f*r**3+10*curv_f*grav_f*r**4)
    tgr=theta_g*r*Lg;tfr=theta_f*r*Lf
    Rg=-48*curv_g/(a*a*ug**5)
    Rf=-48*curv_f/(b*b*uf**5)
    Dg=pSg*Sgr-Lg*pLgr+pg*tgr
    Df=pSf*Sfr-Lf*pLfr+pf*tfr
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    As=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=M2*MG2*Lg*Lf*At
    z=z_slope*r
    root=np.sqrt(1-z*z)
    Wg=M2*MG2*(Lg*A0+Lf*At*root)
    Wf=M2*MG2*(Lf*As+Lg*At*root)
    Hg=Lg*pLg**2/(4*MG2*Sg**2)-pLg*pSg/(2*MG2*Sg)-MG2*Lg*Sg**2*Rg/2+pg*np.sqrt(1+tgr**2/Lg**2)+z*Dg/Lg+Wg
    Hf=Lf*pLf**2/(4*MF2*Sf**2)-pLf*pSf/(2*MF2*Sf)-MF2*Lf*Sf**2*Rf/2+pf*np.sqrt(1+tfr**2/Lf**2)+z*Dg/Lf+Wf
    return np.stack((Hg,Hf,Dg+Df,Dg-K*z/root))


def flat_closed_bracket(r,N,M,q):
    """Independent Step33f flat/comoving closed expression, actual pL/r^2."""
    a=.4;b=a*Y
    J=BETA[1]+2*BETA[2]*Y+BETA[3]*Y**2
    Pg=q[1]/r**2;Pf=q[7]/r**2
    X=Pg/(MG2*a)-Pf/(MF2*b)
    vg=BETA[0]+3*BETA[1]*Y+3*BETA[2]*Y**2+BETA[3]*Y**3
    H=np.sqrt(CG/(3*a**3)+M2*vg/3)
    pa=-6*MG2*a*a*H;pb=-6*MF2*b*a*H
    Xr=(pa/3*(2/3)*.04/(MG2*a)-pb/3*(2/3)*(-.035)/(MF2*b))*np.ones_like(r)
    K00=M2*MG2*a*a/2*J*r*r*(3*X+r*Xr)
    return float(np.trapezoid(N*M*K00,r))

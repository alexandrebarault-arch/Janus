"""Independent *numerically collocated* full original spherical ADM+HR+two-dust
Hamiltonian Poisson bracket on curved radial primary-satisfying data.

Independent of Step33g's SymPy Euler/IBP implementation. Uses the ORIGINAL
unintegrated spatial curvature and Dg containing pL' with z root recomputed on
EACH canonical field variation. Canonical Dirac delta is discretized as
{q_i,p_j}=delta_ij/w_i, in a Gauss pseudospectral quadrature. Convergence is
required: no discrete bracket alone establishes a physical BD secondary.
"""
from __future__ import annotations
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

BETAS=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
M2=23.3348939346; MG2=1.; MF2=.10879548725**2
A=.4; Y=.5787707228025044; CG=.9
BOUNDS=(.1,.9)
PAIRS=(('Lg','pLg'),('Sg','pSg'),('tg','pg'),('Lf','pLf'),('Sf','pSf'),('tf','pf'))
ORDER=tuple(x for pair in PAIRS for x in pair)


def grid(n=24, interval=BOUNDS):
    if not isinstance(n,int) or n<12:raise ValueError('at least 12 collocation points')
    lo,hi=interval
    if not (0<lo<hi):raise ValueError('strictly positive interior radial domain')
    t,w=leggauss(n);x=(hi+lo)/2+(hi-lo)*t/2;w=w*(hi-lo)/2
    # Gauss-Legendre nodal barycentric weights, alternating signs.
    bary=(-1.)**np.arange(n)*np.sqrt((1-t*t)*leggauss(n)[1])
    dx=x[:,None]-x[None,:]
    D=np.zeros((n,n));mask=~np.eye(n,dtype=bool)
    rat=bary[None,:]/bary[:,None]
    D[mask]=(rat/np.where(mask,dx,1.))[mask]
    np.fill_diagonal(D,-D.sum(axis=1))
    return x,w,D


def _curvature(L,S,D):
    Lr=D@L;Sr=D@S; Srr=D@Sr
    W=Sr/L
    Wr=Srr/L-Sr*Lr/(L*L)
    return 2/S**2*(1-W*W-2*S*Wr/L)


def _calc(q,D):
    Lg,plg,Sg,psg,tg,pg,Lf,plf,Sf,psf,tf,pf=(q[k] for k in ORDER)
    Sgr=D@Sg;Sfr=D@Sf;tgr=D@tg;tfr=D@tf
    dG=psg*Sgr-Lg*(D@plg)+pg*tgr
    dF=psf*Sfr-Lf*(D@plf)+pf*tfr
    b0,b1,b2,b3,b4=BETAS
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    As=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    K=M2*MG2*Lg*Lf*At
    # Valid regular-root (the numerically chosen branch is sign sensitive).
    if np.any(abs(K)<1.e-9):raise ValueError('degenerate K in collocation')
    u=dG/K
    z=u/np.sqrt(1+u*u)
    wG=M2*MG2*(Lg*A0+Lf*At*np.sqrt(1-z*z))
    wF=M2*MG2*(Lf*As+Lg*At*np.sqrt(1-z*z))
    cg=Lg*plg**2/(4*MG2*Sg*Sg)-plg*psg/(2*MG2*Sg)-MG2*Lg*Sg*Sg*_curvature(Lg,Sg,D)/2+pg*np.sqrt(1+(tgr/Lg)**2)
    cf=Lf*plf**2/(4*MF2*Sf*Sf)-plf*psf/(2*MF2*Sf)-MF2*Lf*Sf*Sf*_curvature(Lf,Sf,D)/2+pf*np.sqrt(1+(tfr/Lf)**2)
    return cg+z*dG/Lg+wG,cf+z*dG/Lf+wF,dG+dF,dG-K*z/np.sqrt(1-z*z),z


def curved_primary_arrays(x,D,*,curv_g=.015,curv_f=-.012,z_slope=.04,
                          theta_g=.012,theta_f=-.016,grav_g=.04,grav_f=-.035):
    a=A;b=A*Y
    bet=BETAS;vg=bet[0]+3*bet[1]*Y+3*bet[2]*Y*Y+bet[3]*Y**3
    h=math.sqrt(CG/(3*a**3)+M2*vg/3)
    Pg0=-2*MG2*a*a*h;Pf0=-2*MF2*b*a*h
    fields={}; geo=[]
    for key,scale,curv,theta,gfrac,P0 in [('g',a,curv_g,theta_g,grav_g,Pg0),('f',b,curv_f,theta_f,grav_f,Pf0)]:
        u=1+curv*x*x
        L=scale*u*u;S=L*x
        # Analytical primitive of pL'=2r (1+5c r²) P0 (1+gfrac*r).
        pl=P0*(x*x+(2/3)*gfrac*x**3+(5/2)*curv*x**4+2*curv*gfrac*x**5)
        t=theta*scale*(.5*x*x+.5*curv*x**4+curv**2*x**6/6)
        fields['L'+key]=L;fields['S'+key]=S;fields['pL'+key]=pl;fields['t'+key]=t
        geo.append((L,S,pl,t))
    (Lg,Sg,pLg,tg),(Lf,Sf,pLf,tf)=geo
    Sgr=D@Sg;Sfr=D@Sf
    thgr=D@tg;thfr=D@tf
    b0,b1,b2,b3,b4=BETAS
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    As=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    K=M2*MG2*Lg*Lf*At
    z=z_slope*x;root=np.sqrt(1-z*z)
    d=K*z/root
    wg=M2*MG2*(Lg*A0+Lf*At*root)
    wf=M2*MG2*(Lf*As+Lg*At*root)
    for key,L,S,pl,tr,ds,mass,W in [('g',Lg,Sg,pLg,thgr,d,MG2,wg),('f',Lf,Sf,pLf,thfr,-d,MF2,wf)]:
        Sr=D@S;pr=D@pl
        factor=pl/(2*mass*S*Sr)
        kinetic=L*pl*pl/(4*mass*S*S)
        pot=-mass*L*S*S*_curvature(L,S,D)/2
        constant=kinetic-factor*(ds+L*pr)+pot+z*d/L+W
        coeff=np.sqrt(1+(tr/L)**2)+factor*tr
        p=-constant/coeff
        ps=(ds+L*pr-p*tr)/Sr
        fields['p'+key]=p;fields['pS'+key]=ps
    return fields


def smear(x, *,kind='N'):
    lo,hi=BOUNDS
    k=(x-lo)**3*(hi-x)**3
    if kind=='N':return k*(1+.4*x)
    if kind=='M':return k*(.7-.3*x+.5*x*x)
    if kind=='P':return k*(1-.45*x+.7*x*x)
    if kind=='Q':return k*(.4+.8*x-.15*x*x)
    raise ValueError('unknown compact lapse probe')


def bracket(q,D,weights,N,M,*,h=1.e-6):
    """Independent nodal canonical PB from variations of ORIGINAL H_g and H_f."""
    def action(q):
        cg,cf,_,_,_= _calc(q,D)
        return float(weights@(cg*N)),float(weights@(cf*M))
    derivG={};derivF={}
    for field in ORDER:
        dg=np.empty(len(weights));df=np.empty(len(weights))
        for i in range(len(weights)):
            # Recompute physical z* after EVERY field perturbation; keep both dusts.
            old=q[field][i]
            q[field][i]=old+h; plus=action(q)
            q[field][i]=old-h; minus=action(q)
            q[field][i]=old
            dg[i]=(plus[0]-minus[0])/(2*h)
            df[i]=(plus[1]-minus[1])/(2*h)
        derivG[field]=dg;derivF[field]=df
    terms=[]
    for u,v in PAIRS:
        terms.append(np.sum((derivG[u]*derivF[v]-derivG[v]*derivF[u])/weights))
    return float(sum(terms)),np.array(terms)


def witness(n=24,*,N='N',M='M'):
    x,w,D=grid(n)
    q=curved_primary_arrays(x,D)
    cg,cf,dd,fz,z=_calc(q,D)
    val,pairs=bracket(q,D,w,smear(x,kind=N),smear(x,kind=M))
    return dict(n=n,bracket=val,pairs=pairs,primary_residual=float(max(np.max(abs(cg)),np.max(abs(cf)),np.max(abs(dd)),np.max(abs(fz)))),
                minimum_pg=float(min(q['pg'])),minimum_pf=float(min(q['pf'])),max_z=float(max(abs(z))))

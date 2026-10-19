"""Exact radially smeared canonical Poisson bracket of ONE/TWO HR dust sectors.

This is the pressureless irrotational dust contribution to the full radial
ADM constraint algebra. It does NOT compute the EH/HR field-theory constraint
brackets, BD secondary, or a propagation speed. Use positive radial scale L.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class DustRadialData:
    r: np.ndarray
    L: np.ndarray
    theta: np.ndarray
    p: np.ndarray
    N: np.ndarray
    M: np.ndarray


def sample_dust_radial(n=97, *, seed_shift=0.):
    """Regular nonhomogeneous profiles, compact lapse tests, nonzero theta_r."""
    if type(n) is not int or n < 17 or not math.isfinite(float(seed_shift)):
        raise ValueError('grid n >= 17 and finite profile offset required')
    r=np.linspace(0.,1.,n)
    L=1.1+.09*r+.04*np.cos(2*np.pi*r)+.03*seed_shift
    theta=.14*np.sin(2*np.pi*r)+.027*r*r+.012*seed_shift*np.sin(3*np.pi*r)
    p=.75+.1*np.cos(2*np.pi*r)+.02*seed_shift*r
    c=r*r*(1.-r)**2
    N=c*(1.+.22*r)
    M=c*(r-.4+.15*np.sin(np.pi*r))
    return DustRadialData(r,L,theta,p,N,M)


def _checked(z:DustRadialData):
    vals=[np.asarray(getattr(z,k),float) for k in ('r','L','theta','p','N','M')]
    r,L,theta,p,N,M=vals
    if r.ndim!=1 or len(r)<5 or any(x.shape!=r.shape for x in vals):
        raise ValueError('all radial arrays must have one matching 1D shape')
    if not all(np.all(np.isfinite(x)) for x in vals) or np.any(L<=0) or np.any(p<=0):
        raise ValueError('finite arrays with positive L and matter p required')
    dr=np.diff(r)
    if np.any(dr<=0) or np.max(abs(dr-dr[0]))>1e-12 or dr[0]<=0:
        raise ValueError('strictly increasing uniform radial grid required')
    if max(abs(N[0]),abs(N[-1]),abs(M[0]),abs(M[-1]))>1e-12:
        raise ValueError('test lapse smearings must vanish at both radial endpoints')
    return r,L,theta,p,N,M


def _deriv(x, dr):
    return np.gradient(x,dr,edge_order=2)


def discrete_action(z:DustRadialData, lapse, theta=None, P=None):
    """Discrete H[N]=sum_i N_i P_i sqrt(1+(Dtheta)_i²/L_i²).

    P=w*p is the CANONICAL nodal momenta; trapezoid weights are absorbed.
    This discretization retains the genuinely two-sided radial gradients.
    """
    r,L,t,p,_,_=_checked(z)
    lapse=np.asarray(lapse,float)
    if lapse.shape!=r.shape:raise ValueError('bad lapse shape')
    h=r[1]-r[0]
    w=np.full(len(r),h);w[[0,-1]]*=.5
    t=t if theta is None else np.asarray(theta,float)
    P=w*p if P is None else np.asarray(P,float)
    if t.shape!=r.shape or P.shape!=r.shape or not np.all(np.isfinite(t)) or not np.all(np.isfinite(P)):
        raise ValueError('bad canonical variables')
    u=_deriv(t,h)
    return float(np.sum(lapse*P*np.sqrt(1.+(u/L)**2)))


def bracket_from_functional_variations(z:DustRadialData,*,step=2e-6):
    """Independent canonical FD bracket on all nodal phase/p-density pairs.

    This uses neither analytic continuum Poisson identity nor radial moment
    constraints. It differentiates the discretized two Hamiltonians wrt
    theta_i and canonical momenta P_i=w_i*p_i.
    """
    r,L,t,p,N,M=_checked(z)
    if not math.isfinite(step) or step<=0:raise ValueError('positive finite-difference step required')
    h=r[1]-r[0]
    w=np.full(len(r),h);w[[0,-1]]*=.5
    P=w*p
    grads=[]
    for lapse in (N,M):
        dt=np.zeros(len(r));dp=np.zeros(len(r))
        for i in range(len(r)):
            v=np.zeros(len(r));v[i]=step
            dt[i]=(discrete_action(z,lapse,theta=t+v,P=P)-discrete_action(z,lapse,theta=t-v,P=P))/(2*step)
            dp[i]=(discrete_action(z,lapse,theta=t,P=P+v)-discrete_action(z,lapse,theta=t,P=P-v))/(2*step)
        grads.append((dt,dp))
    (qt,qp),(rt,rp)=grads
    return float(np.dot(qt,rp)-np.dot(qp,rt))


def continuum_momentum_bracket(z:DustRadialData):
    """Right side D_d[(N M'-M N')/L²], evaluated on same radial grid.

    Exact continuum identity: {H_d[N],H_d[M]}=int dr (p theta'/L²)
    (N M'-M N'), for compact N,M. L is spatial metric background data.
    """
    r,L,theta,p,N,M=_checked(z)
    h=r[1]-r[0]
    u=_deriv(theta,h);Np=_deriv(N,h);Mp=_deriv(M,h)
    integrand=p*u*(N*Mp-M*Np)/(L*L)
    return float(np.trapezoid(integrand,r))


def continuum_hamiltonian_bracket(z:DustRadialData):
    """Independent continuum variation + IBP, before simplifying h*h_u=u/L²."""
    r,L,theta,p,N,M=_checked(z)
    h=r[1]-r[0]
    u=_deriv(theta,h)
    v=np.sqrt(1.+u*u/(L*L))
    s=u/(L*L*v)
    # First variation delta H_N / delta theta= -(N p s)' ;
    # delta H_N / delta p=N v, with a compact boundary term.
    dNps=_deriv(N*p*s,h)
    dMps=_deriv(M*p*s,h)
    return float(np.trapezoid(-dNps*M*v+N*v*dMps,r))


def nonrelativistic_wrong_bracket(z:DustRadialData):
    """Negative control: a truncated h=1+u²/(2L²) violates exact closure."""
    r,L,theta,p,N,M=_checked(z)
    h=r[1]-r[0]
    u=_deriv(theta,h)
    kin=1.+.5*(u/L)**2
    kin_u=u/(L*L)
    Np=_deriv(N,h);Mp=_deriv(M,h)
    return float(np.trapezoid(p*kin*kin_u*(N*Mp-M*Np),r))


def crossed_dust_sector_bracket(*,independent=True):
    """Independent canonical phase pairs imply identically zero cross bracket."""
    if independent is not True:raise ValueError('cross bracket assumes two independent canonical pairs')
    return 0.

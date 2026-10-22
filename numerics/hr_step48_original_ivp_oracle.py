"""Independent ORIGINAL unintegrated six-pair Poisson oracle for Step47 IVP.

Canonical q(r) is constructed from Step47's dense radial ODE plus algebraic
primary dust reconstruction. True clock scalars theta_i(r) are integrated
analytically so the ORIGINAL nodal Hamiltonian can differentiate them.

The Poisson functional gradients are then obtained using the unmodified
historical hr_step37_original_nonibp_oracle.hamiltonians, not the analytic
C expression used to DEFINE the ODE. Four-grid Richardson is exploratory,
never a rigorous continuum bound, and is not a Dirac time-preservation test.
"""
from __future__ import annotations
from decimal import Decimal,localcontext
from functools import lru_cache
from pathlib import Path
import hashlib
import numpy as np
from scipy.integrate import solve_ivp
from .hr_step47_interior_ivp import source_data,compiled_rhs
from .hr_step45_secondary_point_certificate import frozen_primary_at
from .hr_step37_original_nonibp_oracle import hamiltonians

GIT_PINS={
    'numerics/hr_step37_original_nonibp_oracle.py':'005449ade6e3582e3b9a5c3374a881a77e73e3f6',
    'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step45_secondary_point_certificate.py':'6ab94dacb0c6429bdce8d71311161a6b76ecc0e6',
    'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step47_interior_ivp.py':'c558a827939f2e1fffbfc0290f2b3cc88cb69ef9',
}
# Actual input constants are unchanged from the Step47 benchmark.
A=.4
B=A*.5787707228025044
CG=.0015
CF=-.0012
KG=.0012
KF=-.0016


def git_blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def verify_actual_providers(root=None):
    root=Path(root) if root is not None else Path(__file__).resolve().parents[1]
    observed={}
    for rel,expected in GIT_PINS.items():
        h=git_blob((root/rel).read_bytes())
        if h!=expected:raise ValueError(f'historical GitHub provider changed: {rel}, {h} != {expected}')
        observed[rel]=h
    return observed


def clock(r,k,scale,c):
    # theta'(r)=k*r*L(r), with L=scale*(1+c*r²)^2.
    s=r*r
    return k*scale*(s/2+c*s*s/2+c*c*s**3/6)


def solve_ivp_initial_data(start=.05,stop=.85,rtol=1e-10,atol=1e-14,max_step=.02):
    if not (.04<=start<stop<=.85 and 0<rtol<=1e-6 and 0<atol<=1e-10):
        raise ValueError('interior IVP domain/accuracy invalid')
    p=frozen_primary_at(start)['pLf']
    initial=float((p.lo+p.hi)/2)
    _,rhs,_=compiled_rhs()
    def ode(r,y):
        vals,_=source_data(float(r),float(y[0]))
        return [float(rhs(*vals))]
    result=solve_ivp(ode,(start,stop),[initial],rtol=rtol,atol=atol,
                     max_step=max_step,dense_output=True)
    if not result.success:raise ArithmeticError(result.message)
    return result


def sample_actual_canonical(sol, rr):
    """12 ORIGINAL canonical fields; no use of compiled Euler/IBP Kij."""
    _,rhs,matter=compiled_rhs()
    q=np.empty((12,len(rr)))
    max_C=0.
    for i,r0 in enumerate(rr):
        r=float(r0)
        pLf=float(sol.sol(r)[0])
        vals,bg=source_data(r,pLf)
        pLf_prime=float(rhs(*vals))
        pf,pSf,C=map(float,matter(*vals,pLf_prime))
        q[:,i]=[bg['Lg'],bg['pLg'],bg['Sg'],bg['pSg'],
                clock(r,KG,A,CG),bg['pg'],
                bg['Lf'],pLf,bg['Sf'],pSf,
                clock(r,KF,B,CF),pf]
        max_C=max(max_C,abs(C))
    if not np.isfinite(q).all():raise ArithmeticError('nonfinite canonical sample')
    return q,float(max_C)


def compact_pair(rr,pair):
    if pair=='A':lo,hi=.2,.7
    elif pair=='B':lo,hi=.25,.73
    else:raise ValueError('lapse pair must be A or B')
    x=(rr-lo)/(hi-lo)
    mask=(rr>lo)&(rr<hi)
    N=np.where(mask,np.sin(np.pi*x)**4,0.)
    if pair=='A':M=N*(1+.2*np.sin(2*np.pi*x))
    else:M=N*(1-.3*np.cos(2*np.pi*x)+.12*np.sin(4*np.pi*x))
    return N,M


def original_unintegrated_poisson(sol,n=321,pair='A',step=1e-21):
    if not isinstance(n,int) or n<81 or n>2561 or step<=0:
        raise ValueError('unsupported radial grid/complex step')
    r=np.linspace(.05,.85,n)
    q,maxC=sample_actual_canonical(sol,r)
    N,M=compact_pair(r,pair)
    dr=r[1]-r[0]
    g=np.zeros((12,n));f=np.zeros((12,n))
    for i in range(12):
        for j in range(1,n-1):
            perturbed=q.astype(complex)
            perturbed[i,j]+=1j*step
            hg,hf=hamiltonians(perturbed,r)
            g[i,j]=np.dot(N,np.imag(hg))*dr/step
            f[i,j]=np.dot(M,np.imag(hf))*dr/step
    components=[float((np.dot(g[2*i,1:-1],f[2*i+1,1:-1])
                      -np.dot(g[2*i+1,1:-1],f[2*i,1:-1]))/dr)
                for i in range(6)]
    h1,h2=hamiltonians(q,r)
    return {'n':n,'pair':pair,'bracket':float(sum(components)),
            'six_contributions':components,
            'max_discrete_primaries':float(max(np.max(abs(h1[12:-12])),
                                               np.max(abs(h2[12:-12])))),
            'min_pf_div_r2_sample':float(np.min(q[11]/r**2)),
            'max_analytic_C_substitution_sample':maxC}


def richardson(original_values):
    with localcontext() as ctx:
        ctx.prec=48
        x=[Decimal(str(v)) for v in original_values]
        r2=[(4*x[i+1]-x[i])/3 for i in range(len(x)-1)]
        r4=[(16*r2[i+1]-r2[i])/15 for i in range(len(r2)-1)]
        return {'R2':[float(v) for v in r2],
                'R4':[float(v) for v in r4],
                'assumption':'Even powers of radial mesh spacing; NOT a proven bound'}


def run_original_check(grids=(161,321,641,1281),*,check_git=True):
    if check_git:sha=verify_actual_providers()
    else:sha={'WARNING':'Historical dependency pin bypassed; local reconstruction only'}
    if len(grids)<3 or any(grids[i+1]!=2*grids[i]-1 for i in range(len(grids)-1)):
        raise ValueError('must supply at least 3 successive halving grids')
    sol=solve_ivp_initial_data()
    pairs={}
    for p in ('A','B'):
        raw=[original_unintegrated_poisson(sol,n,p) for n in grids]
        pairs[p]={'grid_results':raw,
                  'richardson_exploratory':richardson([x['bracket'] for x in raw])}
    return {'step':48,'mode':'NUMERICAL_ORIGINAL_NONIBP_IVP_CROSSCHECK',
            'original_provider_pins':sha,'IVP_nfev':sol.nfev,
            'IVP_pLf_endpoint':float(sol.y[0,-1]),
            'two_lapse_pairs':pairs,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'NOT_PROVED':['exact global C=0','uniform dust positivity along IVP',
                          'regular spherical center','secondary time preservation',
                          'full Dirac constraint rank and lapse fixing']}


if __name__=='__main__':
    import json
    print(json.dumps(run_original_check(),indent=2))

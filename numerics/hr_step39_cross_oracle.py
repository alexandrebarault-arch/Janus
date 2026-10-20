"""Step39 two-lapse-pair cross-oracle and derivative-stencil convergence.

Uses genuine Step33g symbolic mixed Kij and Step37 primary/solver source.
Analytic lapse jets + Gauss integral do not rely on the original nodal PB
finite-difference discretization. Never infer an exact Dirac secondary.
"""
from __future__ import annotations
import numpy as np
from numpy.polynomial.legendre import leggauss
from .hr_curved_moving_dust_primary import build_primary
from .hr_step37_curved_solver import kernel_fast, solve_even_center
from .hr_step37_original_nonibp_oracle import sample_canonical, hamiltonians

PARAMS=dict(curv_g=.0015,curv_f=-.0012,z_slope=.004,
            theta_g=.0012,theta_f=-.0016,grav_g=0.,grav_f=0.)


def lapse_jets(r, pair='A'):
    if pair not in ('A','B'):raise ValueError('only independent compact pairs A and B')
    lo,hi=(.2,.7) if pair=='A' else (.25,.73)
    x=(np.asarray(r)-lo)/(hi-lo)
    inside=(x>0)&(x<1)
    th=np.pi*x;sn=np.sin(th);cs=np.cos(th)
    n=sn**4;nx=4*np.pi*sn**3*cs
    nxx=4*np.pi**2*(3*sn**2*cs**2-sn**4)
    if pair=='A':
        m=1+.2*np.sin(2*th)
        mx=.4*np.pi*np.cos(2*th)
        mxx=-.8*np.pi**2*np.sin(2*th)
    else:
        m=1-.3*np.cos(2*th)+.12*np.sin(4*th)
        mx=.6*np.pi*np.sin(2*th)+.48*np.pi*np.cos(4*th)
        mxx=1.2*np.pi**2*np.cos(2*th)-1.92*np.pi**2*np.sin(4*th)
    a=np.asarray([n,nx/(hi-lo),nxx/(hi-lo)**2])
    b=np.asarray([n*m,(nx*m+n*mx)/(hi-lo),
                  (nxx*m+2*nx*mx+n*mxx)/(hi-lo)**2])
    return np.where(inside,a,0.),np.where(inside,b,0.)


def gauss_jet_bracket(w, pair='A', points=96):
    if not isinstance(points,int) or not 16<=points<=512:raise ValueError('Gauss points')
    if pair not in ('A','B'):raise ValueError('unknown lapse pair')
    lo,hi=(.2,.7) if pair=='A' else (.25,.73)
    xi,wi=leggauss(points)
    radii=lo+(xi+1)*(hi-lo)/2
    weights=wi*(hi-lo)/2
    result=0.
    for r,weight in zip(radii,weights):
        n,m=lapse_jets(float(r),pair)
        result+=float(weight*(n@kernel_fast(w,float(r))@m))
    return float(result)


def original_nonibp_extended(w, pair='A', n=1281, step=1e-21):
    """Only extended grid cap/smearing; original Step37 H density unchanged.

    This direct-nodal variation has O(n²) time and finite difference roundoff.
    A second, mathematically different oracle is gauss_jet_bracket().
    """
    if not isinstance(n,int) or not 30<=n<=4097 or step<=0:
        raise ValueError('validated grid or step out of range')
    if pair not in ('A','B'):raise ValueError('lapse pair')
    rr=np.linspace(.1,.9,n)
    q=sample_canonical(w,rr)
    nsm,msm=lapse_jets(rr,pair)
    N=nsm[0];M=msm[0]
    dr=rr[1]-rr[0]
    grads=np.zeros((2,12,n))
    for i in range(12):
        for j in range(1,n-1):
            perturb=q.astype(complex)
            perturb[i,j]+=1j*step
            hg,hf=hamiltonians(perturb,rr)
            grads[0,i,j]=np.dot(N,np.imag(hg))*dr/step
            grads[1,i,j]=np.dot(M,np.imag(hf))*dr/step
    contributions=[float(np.dot(grads[0,2*i,1:-1],grads[1,2*i+1,1:-1])-
                   np.dot(grads[0,2*i+1,1:-1],grads[1,2*i,1:-1]))/dr
                   for i in range(6)]
    hg,hf=hamiltonians(q,rr)
    return {'pair':pair,'n':n,'bracket':float(sum(contributions)),
            'contributions':contributions,
            'max_original_discrete_primary':float(max(np.max(abs(hg[12:-12])),np.max(abs(hf[12:-12])))),
            'min_pg':float(np.min(q[5])),'min_pf':float(np.min(q[11]))}


def witness(*,h=.001,degree=4,iterations=5):
    out=solve_even_center(scale=.1,degree=degree,iterations=iterations,h=h)
    w=build_primary(**PARAMS,f_delta=tuple(out['history'][-1]['f_delta']))
    return w,out


def h_scan(h_values=(.001,.0005,.00025,.000125,.0000625)):
    results=[]
    for h in h_values:
        w,out=witness(h=h,degree=4,iterations=6)
        results.append({'h':h,'max_C_local_sample':out['history'][-1]['max_C'],
            'max_C_over_r2_sample':out['history'][-1]['max_C_div_r2'],
            'max_primary_sample':out['history'][-1]['max_primary'],
            'min_pg_sample':out['history'][-1]['min_pg'],
            'min_pf_sample':out['history'][-1]['min_pf'],
            'IBP_A':gauss_jet_bracket(w,'A',48),
            'IBP_B':gauss_jet_bracket(w,'B',48)})
    return results


if __name__=='__main__':
    import json
    w,sol=witness()
    print(json.dumps({'step':39,
        'original_profile_IBP_96':{p:gauss_jet_bracket(w,p,96) for p in ('A','B')},
        'original_nodal_641':{p:original_nonibp_extended(w,p,641) for p in ('A','B')},
        'stencil_scan':h_scan()},indent=2))

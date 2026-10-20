"""Experimental fourth-order radial derivative for Step37's local secondary.

Unmodified Step37 solver stays byte-identical for audit provenance. This
module reproduces its regular-center preconditioned update while replacing
K01' and K20' with symmetric five-point O(h^4) differentiation.
No continuum C=0, full Dirac preservation, or physical validity inferred.
"""
import numpy as np
from numpy.polynomial import Polynomial
from .hr_curved_moving_dust_primary import build_primary,BETA,M2,MG2,MF2
from .hr_step37_curved_solver import kernel_fast


def local_five_point(w,r=.43,h=.002):
    if not (.025<r<.9 and h>0 and r-2*h>.025 and r+2*h<.9):
        raise ValueError('five-point stencil outside interior chart')
    kmm,km,k0,kp,kpp=(kernel_fast(w,float(r+d*h)) for d in (-2,-1,0,1,2))
    deriv01=(-kpp[0,1]+8*kp[0,1]-8*km[0,1]+kmm[0,1])/(12*h)
    deriv20=(-kpp[2,0]+8*kp[2,0]-8*km[2,0]+kmm[2,0])/(12*h)
    return float(k0[0,0]-deriv01),float(k0[0,1]-k0[1,0]+deriv20)


def solve_five_point(*,scale=.1,degree=4,iterations=6,h=.002):
    if not (0<=scale<=.2 and 1<=degree<=6 and 1<=iterations<=8 and
            0<h<=.004):
        raise ValueError('restricted experimental settings required')
    fit_r=np.linspace(.05,.85,max(18,4*degree+2))
    val_r=np.array([.04,.11,.21,.31,.41,.51,.61,.71,.83])
    y=.5787707228025044;a=.4;b=a*y
    j=BETA[1]+2*BETA[2]*y+BETA[3]*y*y
    A=.5*M2*MG2*a*a*j
    assert j>0 and A>0
    delta=np.zeros(2*degree+1)
    history=[]
    for i in range(iterations+1):
        w=build_primary(curv_g=.015*scale,curv_f=-.012*scale,
            z_slope=.04*scale,theta_g=.012*scale,theta_f=-.016*scale,
            grav_g=0.,grav_f=0.,f_delta=tuple(delta))
        C=np.array([local_five_point(w,float(r),h)[0] for r in fit_r])
        V=np.array([local_five_point(w,float(r),h)[0] for r in val_r])
        E=w.eval(val_r,('Hg','Hf','Ddiag','Fz','pg','pf','z','K'))
        history.append({'iteration':i,'max_abs_C_sample':float(np.max(abs(V))),
            'max_abs_C_div_r2_sample':float(np.max(abs(V/val_r**2))),
            'max_primary_sample':float(np.max(abs(E[:4]))),
            'min_pg_sample':float(np.min(E[4])),'min_pf_sample':float(np.min(E[5])),
            'f_delta':list(map(float,delta))})
        if i==iterations:break
        p=Polynomial.fit(fit_r**2,C/fit_r**2,degree,domain=[0.,.85**2]).convert()
        for k,v in enumerate(p.coef):
            n=2*k
            delta[n]+=MF2*b*v*(n+2)/(2*A*(n+3))
    return w,{'h':h,'scale':scale,'degree':degree,'iterations':iterations,
              'validation_radii':list(map(float,val_r)),'history':history,
              'status':'APPROXIMATE_FINITE_COLLOCATION_NOT_EXACT_DIRAC_SECONDARY'}

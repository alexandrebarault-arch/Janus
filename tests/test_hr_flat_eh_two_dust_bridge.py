"""Differential controls of restricted EH and independent two-dust interface."""
import math
import numpy as np
import pytest
from numerics.hr_flat_eh_two_dust_bridge import (
    native_flat_eh_local_hessian,flat_eh_compact_restricted_hessian,
    assemble_flat_eh_hr_two_dust_restricted,
)
from numerics.hr_compact_radial_interaction import compact_scalar_profile
from numerics.hr_two_dust_preconstraint import assemble_hr_two_dust_preconstraint

P=dict(N=1.03,a=.85,n=1.16,alpha=.74,k=2.2,m2=.7,Mg2=1.2,
       betas=(.31,1.,-.4,.2,.13),mu=-.24,sigma_r=.08,
       sigma_dot=.025,mu_dot=.11,n_dot=.09,alpha_dot=-.07,
       n_ddot=.025,alpha_ddot=-.02)

# Independent scalar ADM density, not differentiated symbolically above.
def exact_native_eh(scale,rate,lapse,r,Phi,U,Ur):
    N=lapse*np.sqrt(1+2*Phi+U*U)
    kr=(rate/scale-lapse*Ur/scale)/N
    kt=(rate/scale-lapse*U/(scale*r))/N
    return N*scale**3*r*r*(-4*kr*kt-2*kt*kt)

def _num_H(f,dim=3,h=1.1e-4):
    z=np.zeros(dim);H=np.zeros((dim,dim));f0=f(z)
    for i in range(dim):
        e=np.zeros(dim);e[i]=h
        H[i,i]=(f(e)-2*f0+f(-e))/h**2
        for j in range(i+1,dim):
            d=np.zeros(dim);d[j]=h
            H[i,j]=H[j,i]=(f(e+d)-f(e-d)-f(-e+d)+f(-e-d))/(4*h*h)
    return H

def test_local_exact_adm_quadratic_taylor_hessian():
    phi=np.eye(3)[0]*.61;u=np.eye(3)[1]*-.41;ur=np.eye(3)[2]*.82
    kw=dict(scale=.9,rate=.14,lapse=1.13,r=.27)
    h=native_flat_eh_local_hessian(**kw,phi=phi,shift=u,shift_r=ur)
    def scalar(x):
        return exact_native_eh(**kw,Phi=phi@x,U=u@x,Ur=ur@x)
    numerical=_num_H(scalar)
    np.testing.assert_allclose(h,numerical,atol=5e-8,rtol=6e-7)

def test_local_restricted_eh_hessian_zero_shift_for_static_background():
    e=np.eye(4)
    H=native_flat_eh_local_hessian(scale=1.,rate=0.,lapse=1.,r=.3,
                                    phi=e[0],shift=e[1],shift_r=e[2])
    assert H[0,0]==H[0,1]==H[0,2]==0
    assert H[1,1]<0 and H[1,2]<0

def test_g_compact_eh_matches_independent_adm_density_integral():
    radius=.37;order=40;a=.83;n=1.07;ad=.19
    H=flat_eh_compact_restricted_hessian(radius=radius,quadrature_order=order,
        N=n,a=a,g_scale_rate=ad,n=1.12,alpha=.92,planck_ratio=0.9,
        mu=0.,mu_dot=0.,sigma_r=0.,sigma_dot=0.)
    x,w=np.polynomial.legendre.leggauss(order)
    r=.5*radius*(x+1);weights=2*math.pi*radius*w
    def scalar(v):
        out=0.
        for rr,ww in zip(r,weights):
            F,Fr,Frr,_=compact_scalar_profile(rr,radius)
            out+=ww*.5*exact_native_eh(a,ad,n,rr,v[0]*F,v[1]*Fr,v[1]*Frr)
        return out
    numerical=_num_H(scalar,dim=2,h=2e-5)
    np.testing.assert_allclose(H[np.ix_([0,1],[0,1])],numerical,atol=3e-7,rtol=3e-6)
    assert H[0,0]<0

def test_f_shift_uses_inverse_chart_and_native_rate_transport():
    kw=dict(radius=.3,quadrature_order=36,N=1.,a=1.,g_scale_rate=0.,
         n=1.12,alpha=.94,n_dot=.0,alpha_dot=.0,
         mu=-.23,mu_dot=.12,sigma_r=.17,sigma_dot=.025)
    H=flat_eh_compact_restricted_hessian(**kw)
    # B_fdot enters native U_R through tilted f-native temporal chart.
    assert np.abs(H[13,5])>1e-9
    assert np.abs(H[13,13])<1e-12 # only bilinear B_f * B_fdot at zero H_f
    flat=flat_eh_compact_restricted_hessian(**dict(kw,sigma_r=0.))
    assert abs(flat[13,5])<1e-12
    np.testing.assert_allclose(H[13,[0,1,2,3,4,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21]],0.,atol=2e-13)

def test_eh_has_no_fictitious_tensor_or_dust_components():
    H=flat_eh_compact_restricted_hessian(radius=.23,quadrature_order=20,
      N=P['N'],a=P['a'],g_scale_rate=.04,n=P['n'],alpha=P['alpha'],
      n_dot=P['n_dot'],alpha_dot=P['alpha_dot'],
      n_ddot=P['n_ddot'],alpha_ddot=P['alpha_ddot'],
      mu=P['mu'],mu_dot=P['mu_dot'],sigma_r=P['sigma_r'],sigma_dot=P['sigma_dot'])
    allowed={0,1,4,5,13}
    assert H.shape==(22,22)
    assert np.max(np.abs(H-H.T))<1e-14
    for j in range(22):
        if j not in allowed:
            np.testing.assert_allclose(H[j],0,atol=3e-14)

def test_eh_compact_quadrature_stability_and_positive_planck_scaling():
    kw=dict(radius=.25,N=P['N'],a=P['a'],g_scale_rate=.07,
      n=P['n'],alpha=P['alpha'],n_dot=P['n_dot'],alpha_dot=P['alpha_dot'],
      n_ddot=P['n_ddot'],alpha_ddot=P['alpha_ddot'],mu=P['mu'],mu_dot=P['mu_dot'],
      sigma_r=P['sigma_r'],sigma_dot=P['sigma_dot'])
    a=flat_eh_compact_restricted_hessian(quadrature_order=18,planck_ratio=1.2,**kw)
    b=flat_eh_compact_restricted_hessian(quadrature_order=32,planck_ratio=1.2,**kw)
    np.testing.assert_allclose(a,b,atol=3e-12,rtol=4e-9)
    c=flat_eh_compact_restricted_hessian(quadrature_order=24,planck_ratio=2.4,**kw)
    np.testing.assert_allclose(c[:2,:2],a[:2,:2],atol=2e-12)
    np.testing.assert_allclose(c[4:6,4:6],2*a[4:6,4:6],atol=2e-12)

def test_restricted_eh_hr_two_dust_assemble_preserves_pairs():
    kw=dict(radius=.23,quadrature_order=20,rho_g=.9,rho_f=.6,
        g_scale_rate=.04,planck_ratio=1.2,
        log_phidot_rate_g=.12,log_phidot_rate_f=-.17)
    out=assemble_flat_eh_hr_two_dust_restricted(**kw,**P)
    old=assemble_hr_two_dust_preconstraint(**{k:v for k,v in kw.items() if k not in ('g_scale_rate','planck_ratio')},**P)
    np.testing.assert_allclose(out.hessian,out.eh_hessian+out.hr_hessian+out.dust_hessian,atol=2e-13)
    np.testing.assert_allclose(out.hessian-old.hessian,out.eh_hessian,atol=2e-13)
    assert out.hessian[17,20]==pytest.approx(old.hessian[17,20],rel=3e-13)
    assert out.hessian[19,21]==pytest.approx(old.hessian[19,21],rel=3e-13)
    assert out.hessian[19,10]==pytest.approx(old.hessian[19,10],rel=3e-13)
    assert out.metric_subblock_rank==4

def test_restricted_eh_rejects_bad_chart():
    kw=dict(radius=.25,N=1.,a=1.,g_scale_rate=0.,n=1.,alpha=1.,
        mu=-.25,mu_dot=.18,sigma_r=0.05,sigma_dot=.03)
    with pytest.raises(ValueError):
        flat_eh_compact_restricted_hessian(**dict(kw,mu=-1.))
    with pytest.raises(ValueError):
        flat_eh_compact_restricted_hessian(**dict(kw,sigma_dot=-3000.))
    with pytest.raises(ValueError):
        flat_eh_compact_restricted_hessian(**dict(kw,planck_ratio=-.2))
    with pytest.raises(ValueError):
        flat_eh_compact_restricted_hessian(**dict(kw,quadrature_order=7))

def test_f_compact_eh_native_direct_adm_density_derivative():
    radius=.31;order=34;kw=dict(N=1.,a=.89,g_scale_rate=0.,
        n=1.12,alpha=.94,n_dot=.06,alpha_dot=.11,n_ddot=.025,
        alpha_ddot=-.03,mu=-.19,mu_dot=.12,sigma_r=.18,sigma_dot=.025,
        planck_ratio=1.35)
    H=flat_eh_compact_restricted_hessian(radius=radius,quadrature_order=order,**kw)
    x,w=np.polynomial.legendre.leggauss(order)
    r=.5*radius*(x+1);weights=2*math.pi*radius*w
    def scalar(v):
        out=0.
        for rr,ww in zip(r,weights):
            F,Fr,Frr,_=compact_scalar_profile(rr,radius)
            t_t=1+.5*kw['sigma_dot']*rr*rr
            t_r=kw['sigma_r']*rr
            r_t=kw['mu_dot']*rr
            r_r=1+kw['mu']
            D=t_t*r_r-t_r*r_t
            shift=v[1]*Fr
            native_ur=(t_t*v[1]*Frr-t_r*v[2]*Fr)/D
            offset=.5*kw['sigma_r']*rr*rr
            native_n=kw['n']+kw['n_dot']*offset+.5*kw['n_ddot']*offset*offset
            native_a=kw['alpha']+kw['alpha_dot']*offset+.5*kw['alpha_ddot']*offset*offset
            native_rate=kw['alpha_dot']+kw['alpha_ddot']*offset
            out+=ww*.5*kw['planck_ratio']*D*exact_native_eh(
                native_a,native_rate,native_n,r_r*rr,v[0]*F,shift,native_ur)
        return out
    numerical=_num_H(scalar,dim=3,h=2e-5)
    np.testing.assert_allclose(H[np.ix_([4,5,13],[4,5,13])],numerical,atol=3e-7,rtol=6e-6)

def test_g_static_shift_quadratic_is_radial_boundary():
    # For flat static FLRW, ADM shift quadratic integrates to a boundary:
    # r^2[-4(U'/r)U-2(U/r)^2] = -2 (r U^2)'.
    H=flat_eh_compact_restricted_hessian(radius=.3,quadrature_order=36,
        N=1.04,a=.91,g_scale_rate=0.,n=1.11,alpha=.82,
        mu=0.,mu_dot=0.,sigma_r=0.,sigma_dot=0.)
    assert abs(H[1,1])<2e-12
    assert abs(H[0,1])<2e-12

"""Independent scalar ADM and full native trace/shear controls."""
import math
import numpy as np
import pytest
from numerics.hr_full_scalar_eh_homothetic import (_profiles,scalar_native_adm_jet,
                                                     integrate_untilted_native_scalar_eh)

P=dict(scale=.91,scale_rate=.14,lapse=1.13,r=.17,profile_radius=.30,k=2.1)

def independent_native_adm(x, *,scale,scale_rate,lapse,r,profile_radius,k):
    """Exact nonlinear ADM from native L,S geometry, not the Taylor-jet code."""
    F,Fr,Frr,Pe,Per,Perr,_,_=_profiles(r,profile_radius,k)
    ph,B,s,E,sd,Ed=x
    A=1+2*s*F-2*k*k*E*Pe/3
    Bq=1+2*s*F+k*k*E*Pe/3
    Ar=2*s*Fr-2*k*k*E*Per/3
    Br=2*s*Fr+k*k*E*Per/3
    Brr=2*s*Frr+k*k*E*Perr/3
    At=2*sd*F-2*k*k*Ed*Pe/3
    Bt=2*sd*F+k*k*Ed*Pe/3
    U=B*Fr;Ur=B*Frr
    nADM=lapse*math.sqrt(1+2*ph*F+U*U/A)
    spatial_l=scale*math.sqrt(A)
    spatial_s=scale*r*math.sqrt(Bq)
    spatial_sprime=scale*math.sqrt(Bq)*(1+r*Br/(2*Bq))
    W=spatial_sprime/spatial_l
    Z=1+r*Br/(2*Bq)
    Zprime=Br/(2*Bq)+r/2*(Brr/Bq-Br**2/Bq**2)
    Wprime=math.sqrt(Bq/A)*((Br/Bq-Ar/A)*Z/2+Zprime)
    Ric3=2/spatial_s**2*(1-W*W-2*(spatial_s/spatial_l)*Wprime)
    Nr=lapse/scale*U/A
    Nrprime=lapse/scale*(Ur/A-U*Ar/A**2)
    Kr=(scale_rate/scale+At/(2*A)-Nrprime-Nr*Ar/(2*A))/nADM
    Kt=(scale_rate/scale+Bt/(2*Bq)-Nr*(1/r+Br/(2*Bq)))/nADM
    return nADM*spatial_l*spatial_s**2*(Ric3-4*Kr*Kt-2*Kt*Kt)

def fd_hessian(fun,n=6,h=5e-5):
    z=np.zeros(n);base=fun(z);out=np.zeros((n,n))
    for i in range(n):
        u=np.zeros(n);u[i]=h
        out[i,i]=(fun(u)+fun(-u)-2*base)/h**2
        for j in range(i+1,n):
            v=np.zeros(n);v[j]=h
            out[i,j]=out[j,i]=(fun(u+v)-fun(u-v)-fun(-u+v)+fun(-u-v))/(4*h*h)
    return out

def test_full_scalar_eh_hessian_against_independent_exact_adm():
    out=scalar_native_adm_jet(**P)
    fd=fd_hessian(lambda x:independent_native_adm(x,**P),h=3e-5)
    np.testing.assert_allclose(fd,out.hessian,rtol=2e-4,atol=2e-6)
    assert out.hessian.shape==(6,6)
    np.testing.assert_allclose(out.hessian,out.hessian.T,atol=1e-13)

def test_trace_and_shear_have_genuine_time_kinetic_entries():
    out=scalar_native_adm_jet(**P)
    assert abs(out.hessian[4,4])>1e-8
    assert abs(out.hessian[5,5])>1e-8
    # The kinetic psi_dot-E_dot cross vanishes by trace/traceless projection.
    assert abs(out.hessian[4,5])<1e-12
    assert abs(out.hessian[2,5])<1e-12
    assert abs(out.hessian[3,4])<1e-12
    assert abs(out.hessian[3,5])>1e-8

def test_flat_limit_eh_matches_exact_lapse_shift_jet():
    out=scalar_native_adm_jet(**P)
    a=P['scale'];ad=P['scale_rate'];n=P['lapse'];r=P['r'];R=P['profile_radius'];k=P['k']
    F,Fr,Frr,*_= _profiles(r,R,k)
    h=ad/a;b=n/a;v=np.array([F,Fr,Frr]);fa=a**3*r*r/n
    exp=np.zeros((2,2))
    exp[0,0]=-18*h*h*F*F*fa
    exp[0,1]=exp[1,0]=fa*(-4*h*b*F*Frr-8*h*b*F*Fr/r)
    exp[1,1]=fa*((6*h*h-4*b*b/r**2)*Fr*Fr-8*b*b/r*Fr*Frr)
    np.testing.assert_allclose(out.hessian[:2,:2],exp,atol=1e-12,rtol=2e-11)

def test_scalar_3curvature_restored_in_static_kinetic_free_spatial_variations():
    out=scalar_native_adm_jet(**dict(P,scale_rate=0.))
    # Nonzero 3-curvature quadratic spatial scalar trace/shear couplings.
    assert abs(out.hessian[2,2])>1e-8
    assert abs(out.hessian[2,3])>1e-8
    assert abs(out.hessian[3,3])>1e-8

def test_homothetic_eh_integral_quadrature_convergence():
    kw=dict(radius=.3,k=2.1,N=1.,a=.93,a_rate=.12,n=1.09,
            alpha=.85,alpha_rate=.14,mu=-.28,planck_ratio=1.4)
    lo=integrate_untilted_native_scalar_eh(**dict(kw,quadrature_order=18))
    hi=integrate_untilted_native_scalar_eh(**dict(kw,quadrature_order=32))
    np.testing.assert_allclose(lo.hessian,hi.hessian,atol=4e-10,rtol=4e-9)
    assert lo.hessian.shape==(24,24)
    assert abs(lo.hessian[22,22])>1e-10
    assert abs(lo.hessian[23,23])>1e-10
    assert abs(lo.hessian[14,14])>1e-10
    assert abs(lo.hessian[15,15])>1e-10

def test_f_coordinate_radial_rescaling_invariance():
    kw=dict(radius=.27,k=1.9,N=1.,a=.95,a_rate=.07,n=1.12,alpha=.83,alpha_rate=.11,planck_ratio=1.3)
    for m in (.62,.83,1.4):
        out=integrate_untilted_native_scalar_eh(**dict(kw,mu=m-1,quadrature_order=24))
        # Native f profiles are geometric functions of R_f/(m*R_common).
        # Time and spatial scalar amplitudes unchanged, but U_f=B_f F'_common
        # is m times native derivative, so f Hessian scales linearly in m^3
        # on flat background for metric lapse/trace/time-rate channels.
        assert out.f_radial_scale==pytest.approx(m)
        assert np.linalg.norm(out.hessian[4:8,4:8])>1e-8

def test_static_compact_radial_shift_is_eh_boundary():
    kw=dict(radius=.29,k=2.2,N=1.03,a=.94,a_rate=0.,n=1.11,
            alpha=.8,alpha_rate=0.,mu=-.22)
    H=integrate_untilted_native_scalar_eh(**kw,quadrature_order=34).hessian
    assert abs(H[1,1])<1e-11
    assert abs(H[5,5])<1e-11

def test_native_scalar_eh_domain_guards():
    with pytest.raises(ValueError):scalar_native_adm_jet(**dict(P,r=0.))
    with pytest.raises(ValueError):scalar_native_adm_jet(**dict(P,k=0.))
    with pytest.raises(ValueError):integrate_untilted_native_scalar_eh(radius=.3,k=2.,N=1.,a=1.,a_rate=0.,n=1.,alpha=1.,alpha_rate=0.,mu=-1.)
    with pytest.raises(ValueError):integrate_untilted_native_scalar_eh(radius=.3,k=2.,N=1.,a=1.,a_rate=0.,n=1.,alpha=1.,alpha_rate=0.,quadrature_order=2)

def test_shear_and_trace_kinetic_hessians_match_closed_forms():
    out=scalar_native_adm_jet(**P)
    r=P['r'];a=P['scale'];n=P['lapse'];k=P['k']
    F,_,_,E,_,_,_,_=_profiles(r,P['profile_radius'],k)
    expected_trace=-12*a**3*r*r*F*F/n
    expected_shear=(a**3*r*r/n)*k**4*E*E/3
    assert out.hessian[4,4]==pytest.approx(expected_trace,rel=2e-12)
    assert out.hessian[5,5]==pytest.approx(expected_shear,rel=2e-12)
    assert abs(out.hessian[4,5])<1e-13

def test_native_f_eh_exact_coordinate_rescaling_with_shift_amplitude_transform():
    # Fix native f radius and native k. Changing the COMMON radial coordinate
    # by m must not change the physical native f EH Hessian after consistently
    # redefining the common B_f amplitude (B_native=m*B_common).
    native_R=.31;native_k=1.7
    fields=[4,5,6,7,14,15]
    reference=None
    for m in (1.,.72,1.31):
        out=integrate_untilted_native_scalar_eh(
            radius=native_R/m,k=native_k*m,
            N=1.,a=.92,a_rate=.09,n=1.13,alpha=.84,
            alpha_rate=.12,mu=m-1,planck_ratio=1.5,quadrature_order=28)
        H=out.hessian[np.ix_(fields,fields)]
        transform=np.diag([1,1/m,1,1/(m*m),1,1/(m*m)])
        physically_normalized=transform@H@transform
        if reference is None:reference=physically_normalized
        else:np.testing.assert_allclose(physically_normalized,reference,atol=3e-11,rtol=4e-11)


def test_f_native_shear_projection_exactly_matches_existing_hr_basis():
    # E is a Hessian potential (two radial derivatives): under R_f=m*r,
    # E_f_native=m^2 E_f_common. Both metrics must use the same shear
    # coefficient in physical g/f radial and angular components.
    r=.18;R=.3;k=2.2;m=.76
    _,_,_,Pc,_,_,_,_=_profiles(r,R,k)
    _,_,_,Pn,_,_,_,_=_profiles(m*r,m*R,k/m)
    eh_radial=(-2/3)*(k/m)**2*(m*m*Pn)
    hr_radial=(-2/3)*k*k*Pc
    eh_angular=(1/3)*(k/m)**2*(m*m*Pn)
    hr_angular=(1/3)*k*k*Pc
    assert eh_radial==pytest.approx(hr_radial,abs=1e-13)
    assert eh_angular==pytest.approx(hr_angular,abs=1e-13)

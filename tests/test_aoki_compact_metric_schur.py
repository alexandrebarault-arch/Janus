import numpy as np


def _kwargs(mass2):
    return dict(
        betas=(0,1,-4.2383993109,13.6801214252,0), K=1.0, w=0.0,
        mu=-0.669234418875108, conformal_H=0.08,
        time_radius=0.55, radial_radius=0.7,
        interaction_mass2=mass2, planck_ratio=1.0,
        amplitude_step=7e-4, quadrature_order=16,
    )


def test_zero_interaction_mass_removes_pi_from_total_action():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    out=reduce_compact_metric_block(**_kwargs(0.0))
    assert abs(out.total_hessian[0,0]) < 1e-12
    assert np.linalg.norm(out.total_hessian[0,1:]) < 1e-12
    assert abs(out.reduced_pi_hessian) < 1e-12
    assert np.linalg.norm(out.total_gradient) < 1e-12
    assert abs(out.reduced_pi_gradient) < 1e-12


def test_small_mass_schur_tends_to_hr_only_pi_entry():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    out=reduce_compact_metric_block(**_kwargs(2e-5))
    leading=-2e-5*out.hr_hessian[0,0]
    assert abs(leading) > 1e-10
    assert abs(out.reduced_pi_hessian-leading)/abs(leading) < 2e-3
    assert np.isfinite(out.metric_condition_number)


def test_total_metric_block_is_symmetric():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    out=reduce_compact_metric_block(**_kwargs(3e-3))
    assert np.allclose(out.total_hessian,out.total_hessian.T,rtol=0,atol=2e-8)
    assert out.metric_rank == 4


def test_reduced_compact_action_recovers_aoki_coefficients_at_small_mass_ratio():
    from numerics.aoki_compact_metric_schur import recover_reduced_pi_coefficients
    raw=(1.0,-4.2383993109,13.6801214252); K=1.0; w=0.0
    D=raw[0]*K+2*raw[1]*K*K+raw[2]*K**3
    B2=(raw[1]*K*K+raw[2]*K**3)/D
    B3=raw[2]*K**3/D
    roots=np.roots([-2*B2+B3,-2*B2-2,-3.0])
    mu=min(float(z.real) for z in roots if abs(z.imag)<1e-10 and z.real>-1)
    common=(3*w-1)*(2+mu)*(1+2*B2*mu+B3*mu*mu)
    KS=0.75*common
    cs2=2*(3*(1-w)+(1-(3*w-1)*B2)*mu)/(3*common)
    target_hr=-2*D*KS
    mass2=2e-7
    out=recover_reduced_pi_coefficients(
        betas=(0,*raw,0),K=K,w=w,mu=mu,
        interaction_mass2=mass2,planck_ratio=1.0,
        time_scales=(0.5,1.0,2.0),radius=1.0,
        hubble_step=0.007,amplitude_step=2e-3,quadrature_order=18,
    )
    assert np.isclose(out.kinetic_hessian_coefficient/(-mass2),target_hr,rtol=8e-3,atol=2e-3)
    assert np.isclose(out.sound_speed_squared,cs2,rtol=8e-3,atol=2e-3)


def test_compact_static_regular_root_matches_full_aoki_finite_mass_control():
    from numpy.polynomial import Polynomial as Poly
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    raw=(1.0,-4.2383993109,13.6801214252); K=1.0; w=0.0
    D=raw[0]+2*raw[1]+raw[2]
    B2=(raw[1]+raw[2])/D; B3=raw[2]/D
    H=0.25; mass2=1e-3; mg2=mass2*D; mf2=mg2
    u=Poly([0.0,1.0]); one=Poly([1.0])
    g=mg2*(one+u)**2*(9+18*B2*u+(6*B2**2+4*B3)*u**2-B3**2*u**4)
    f=mf2*(9+18*(1+B2)*u+(10+34*B2+4*B3+6*B2**2)*u**2
        +(2+14*B2+8*B3+12*B2**2)*u**3
        +(2*B2+2*B3+2*B2**2-B3**2+4*B2*B3)*u**4)
    full=u*(g+f)-3*H**2*u*(one+u)**2*(3+2*(1+B2)*u+(2*B2-B3)*u**2)
    roots=np.roots(np.trim_zeros(full.coef[::-1],trim='f'))
    target=min((r.real for r in roots if abs(r.imag)<1e-9 and -0.9<r.real<-0.5),key=lambda z:abs(z+0.67))

    kw=dict(betas=(0,*raw,0),K=K,w=w,conformal_H=H,time_radius=.4,radial_radius=.6,
            interaction_mass2=mass2,planck_ratio=1.0,amplitude_step=.0015,quadrature_order=12)
    def residual(mu):
        return reduce_compact_metric_block(mu=mu,**kw).reduced_pi_gradient
    lo,hi=-0.75,-0.60
    flo,fhi=residual(lo),residual(hi)
    assert flo*fhi < 0
    for _ in range(26):
        mid=0.5*(lo+hi); fm=residual(mid)
        if flo*fm <= 0:
            hi=mid; fhi=fm
        else:
            lo=mid; flo=fm
    got=0.5*(lo+hi)
    assert np.isclose(got,target,rtol=4e-3,atol=2e-3)

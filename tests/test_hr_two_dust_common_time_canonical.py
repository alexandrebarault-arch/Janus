"""Independent Legendre / common-time two-dust symplectic acceptance tests.

Green asserts BOTH independent matter phase-space pairs, NOT BD reduction
or scalar propagation speeds.
"""
import numpy as np
import pytest
from numerics.hr_full_onshell_tadpole import (Trajectory,sector_density,
       background,action as covariant_action,profile,CG,CF,MF2,MG2,M2)
from numerics.hr_two_dust_common_time_canonical import (
    ORDER,PAIR_INDICES,action,derivative,adm_dust_geometry,phase_samples,
    dust_legendre_density,dust_reduced_density,kinetic_pair_block,
    analytic_canonical_pair_integrals
)

@pytest.fixture(scope='module')
def bg():return Trajectory.solve(width=.04)


def _one_sector(bg,sector,t=.007,r=.14):
    a,b,ad,bd,nf,rhog,rhof=bg.at(t)
    if sector=='g':s,v,n,rho,M,C=a,ad,1.,rhog,MG2,CG
    else:s,v,n,rho,M,C=b,bd,nf,rhof,MF2,CF
    arr=np.array([.021,-.015,.016,-.009,.0012,.037])
    eh,dust,metric,area,_=sector_density(
        scale=s,scale_rate=v,lapse=n,rho0=rho,amp=arr,
        t=t,r=r,time_radius=.027,radial_radius=.32,planck=M)
    N,shift,vol,rr=adm_dust_geometry(metric,area)
    T,Tr,F,Fr,_=profile(t,r,.027,.32)
    theta_t=n+arr[4]*Tr*F
    theta_r=arr[4]*T*Fr
    density=rho*(1+arr[5]*T*F)
    return float(dust),float(N),float(shift),float(vol),float(rr),float(theta_t),float(theta_r),float(density),C


def test_two_native_sector_covariant_dust_matches_exact_arbitrary_offshell_legendre(bg):
    for sector in ('g','f'):
        d,N,shift,vol,rr,td,tr,rho,C=_one_sector(bg,sector)
        p=vol*rho*(td-shift*tr)/N
        cov,can,p_calc,rho_stat=dust_legendre_density(
            N=N,shift=shift,rootgamma=vol,g_rr=rr,rho=rho,
            theta_t=td,theta_r=tr,p=p)
        assert cov==pytest.approx(d,abs=5e-17)
        assert can==pytest.approx(d,abs=5e-17)
        assert p_calc==pytest.approx(p,rel=1e-13)
        assert p>0 and rho_stat>0
        assert abs(d)>1e-10  # NOT the trivial on-shell zero dust Lagrangian


def test_stationary_dust_multiplier_exact_reduced_hamiltonian_at_finite_gradients(bg):
    for sector in ('g','f'):
        _,N,shift,vol,rr,td,tr,rho,C=_one_sector(bg,sector)
        p=C*.14**2*1.03
        q=1+tr*tr/rr
        rho_opt=p/(vol*np.sqrt(q))
        _,off,p_legendre,rho_found=dust_legendre_density(
            N=N,shift=shift,rootgamma=vol,g_rr=rr,rho=rho_opt,
            theta_t=td,theta_r=tr,p=p)
        exact=dust_reduced_density(N=N,shift=shift,r_rr=rr,
                                    theta_t=td,theta_r=tr,p=p)
        assert off==pytest.approx(exact,abs=2e-17)
        assert rho_found==pytest.approx(rho_opt,abs=2e-16)
        # Hamiltonian is minimized at the multiplier stationary point.
        for factor in (.65,1.5):
            _,lower,*_=dust_legendre_density(N=N,shift=shift,
                rootgamma=vol,g_rr=rr,rho=rho_opt*factor,
                theta_t=td,theta_r=tr,p=p)
            assert lower<exact


def test_dust_hamiltonian_is_affine_in_adm_lapse_and_shift(bg):
    _,N,shift,vol,rr,td,tr,rho,C=_one_sector(bg,'f')
    p=C*.14**2*.98
    # Exact 2D ADM metric auxiliaries N and N^r have zero SECOND derivatives
    # for fixed p,theta_r,spatial metric (unlike Phi,U variables).
    def L(n,s):return dust_reduced_density(N=n,shift=s,r_rr=rr,
                                    theta_t=td,theta_r=tr,p=p)
    h=.013
    assert L(N+h,shift)+L(N-h,shift)==pytest.approx(2*L(N,shift),abs=3e-17)
    assert L(N,shift+h)+L(N,shift-h)==pytest.approx(2*L(N,shift),abs=3e-17)
    assert (L(N+h,shift+h)-L(N+h,shift-h)-L(N-h,shift+h)+L(N-h,shift-h))==pytest.approx(0.,abs=3e-17)


def test_canonical_action_same_eh_and_hr_and_background_as_step31(bg):
    old=covariant_action(trajectory=bg)
    new=action(trajectory=bg)
    np.testing.assert_allclose(old.contributions,new.contributions,atol=2e-15)
    assert new.total==pytest.approx(old.total,abs=2e-15)
    assert len(ORDER)==14


def test_all_twelve_legitimate_compact_field_tadpoles_zero(bg):
    # Independent 'theta_rate' jet is NOT a legal stand-alone compact
    # variation of theta and has a nonzero linear symplectic boundary term.
    compact_indices=(0,1,2,3,4,5,7,8,9,10,11,12)
    values=np.array([derivative(i,trajectory=bg) for i in compact_indices])
    assert np.max(np.abs(values))<1.3e-10,values
    assert derivative(6,trajectory=bg)>1e-4
    assert derivative(13,trajectory=bg)>1e-5


def test_exact_independent_two_pair_phase_velocity_hessian_rank_two(bg):
    num=kinetic_pair_block(step=.003,trajectory=bg)
    ana=analytic_canonical_pair_integrals()
    np.testing.assert_allclose(num,ana,rtol=2e-7,atol=1.3e-11)
    assert np.linalg.matrix_rank(num,tol=1e-8)==2
    assert num[0,0]>0 and num[1,1]>0
    assert abs(num[0,1])<4e-12 and abs(num[1,0])<4e-12


def test_phase_pair_integral_quadrature_and_compact_support(bg):
    a=analytic_canonical_pair_integrals(quadrature_order=20)
    b=analytic_canonical_pair_integrals(quadrature_order=36)
    np.testing.assert_allclose(a,b,rtol=1e-10,atol=1e-14)
    narrower=analytic_canonical_pair_integrals(time_radius=.018,radial_radius=.27)
    assert np.all(np.diag(narrower)<np.diag(b))


def test_rate_momentum_mixed_derivative_finite_differences_refine(bg):
    a=kinetic_pair_block(step=.005,quadrature_order=20,trajectory=bg)
    b=kinetic_pair_block(step=.003,quadrature_order=28,trajectory=bg)
    np.testing.assert_allclose(a,b,rtol=9e-7,atol=2e-11)


def test_reduced_dust_exactly_linear_in_each_phase_rate_at_fixed_p(bg):
    x=np.zeros(14)
    for ix in (6,13):
        e=x.copy();e[ix]=.04
        f=x.copy();f[ix]=-.04
        center=action(x,trajectory=bg).total
        assert action(e,trajectory=bg).total+action(f,trajectory=bg).total==pytest.approx(2*center,abs=2e-15)


def test_reduced_dust_exactly_linear_in_each_momentum_at_fixed_fields(bg):
    x=np.zeros(14)
    for ix in (5,12):
        e=x.copy();e[ix]=.1
        f=x.copy();f[ix]=-.1
        center=action(x,trajectory=bg).total
        assert action(e,trajectory=bg).total+action(f,trajectory=bg).total==pytest.approx(2*center,abs=2e-15)


def test_canonical_phase_pair_charges_do_not_mix_in_cross_sector(bg):
    base=action(trajectory=bg).total
    for i,j in ((5,13),(12,6),(5,12),(6,13)):
        h=.03; x=np.zeros(14);y=np.zeros(14);x[i]=h;y[j]=h
        hmix=(action(x+y,trajectory=bg).total-action(x-y,trajectory=bg).total
              -action(-x+y,trajectory=bg).total+action(-x-y,trajectory=bg).total)/(4*h*h)
        assert abs(hmix)<8e-15


def test_single_metric_lapse_no_hr_yields_nonzero_onshell_tadpole(bg):
    val=derivative(0,m2=0,trajectory=bg)
    assert abs(val)>1e-6
    valf=derivative(7,m2=0,trajectory=bg)
    assert abs(valf)>1e-7


def test_analytic_pair_coefficients_scale_with_two_independent_dust_charges():
    a=analytic_canonical_pair_integrals()
    assert a[0,0]/a[1,1]==pytest.approx(CG/CF,rel=1e-13)
    assert a[0,1]==a[1,0]==0


def test_metric_profiles_still_couple_with_hr(bg):
    # Cross-metric Phi_g--psi_f action coefficient vanishes with HR=0.
    def cross(m2):
        h=.001;u=np.zeros(14);v=np.zeros(14);u[0]=h;v[9]=h
        return (action(u+v,m2=m2,trajectory=bg).total-action(u-v,m2=m2,trajectory=bg).total
                -action(-u+v,m2=m2,trajectory=bg).total+action(-u-v,m2=m2,trajectory=bg).total)/(4*h*h)
    assert abs(cross(M2))>1e-5
    assert abs(cross(0))<4e-12


def test_legendre_domain_and_action_shape_guards(bg):
    args=dict(N=1.,shift=.02,rootgamma=.5,g_rr=1.1,rho=.2,
              theta_t=1.1,theta_r=.1,p=.1)
    with pytest.raises(ValueError):dust_legendre_density(**dict(args,rho=-.2))
    with pytest.raises(ValueError):dust_reduced_density(N=1,shift=0,r_rr=1,theta_t=1,theta_r=0,p=0)
    with pytest.raises(ValueError):action(np.zeros(12),trajectory=bg)
    with pytest.raises(ValueError):action(np.zeros(14),trajectory=bg,quadrature_order=5)
    with pytest.raises(ValueError):action(np.zeros(14),trajectory=bg,time_radius=.05)
    with pytest.raises(ValueError):derivative(14,trajectory=bg)
    with pytest.raises(ValueError):kinetic_pair_block(step=0,trajectory=bg)


def test_full_14_amplitude_hessian_has_both_exact_sparse_symplectic_rate_rows(bg):
    from numerics.hr_two_dust_common_time_canonical import full_preconstraint_hessian
    H=full_preconstraint_hessian(trajectory=bg,quadrature_order=20)
    assert H.shape==(14,14)
    np.testing.assert_array_equal(H,H.T)
    a=analytic_canonical_pair_integrals(quadrature_order=20)
    np.testing.assert_allclose(H[np.ix_([5,12],[6,13])],a,
                               atol=4e-12,rtol=3e-7)
    # Each rate jet touches ONLY its own dust momentum.
    expected=np.zeros((2,14));expected[0,5]=a[0,0];expected[1,12]=a[1,1]
    np.testing.assert_allclose(H[[6,13],:],expected,atol=4e-12,rtol=3e-7)
    np.testing.assert_allclose(H[np.ix_([5,12],[5,12])],0.,atol=4e-12)
    assert abs(H[0,9])>1e-5


def test_complete_preconstraint_hessian_refinement_and_hr_cross(bg):
    from numerics.hr_two_dust_common_time_canonical import full_preconstraint_hessian
    H18=full_preconstraint_hessian(trajectory=bg,quadrature_order=18,step=.004)
    H26=full_preconstraint_hessian(trajectory=bg,quadrature_order=26,step=.003)
    np.testing.assert_allclose(H18,H26,rtol=4e-3,atol=1e-6)
    assert abs(H26[0,9]-H18[0,9])<2e-8


def test_dust_velocity_source_is_momentum_density_not_an_extra_on_shell_tadpole(bg):
    # For an independent local jet delta theta_t, the p*theta_t term
    # gives a NONZERO first derivative. Only compact theta(t,r) variations
    # with their linked theta_t=partial_t theta make action tadpoles vanish.
    x=np.zeros(14);x[6]=.01
    y=np.zeros(14);y[13]=.01
    d=analytic_canonical_pair_integrals()
    # background momentum density is C*r²; single phase-rate derivative
    # equals int p0*TF, whereas mixed derivative uses int p0*(TF)².
    assert derivative(6,trajectory=bg)>d[0,0]
    assert derivative(13,trajectory=bg)>d[1,1]
    assert action(x,trajectory=bg).total>action(trajectory=bg).total
    assert action(y,trajectory=bg).total>action(trajectory=bg).total


def test_canonical_dust_shift_constraint_sign_from_exact_adm_formula(bg):
    _,N,shift,vol,rr,td,tr,rho,C=_one_sector(bg,'g')
    p=.96*C*.14**2
    h=1e-5
    def f(shift_value):
        return dust_reduced_density(N=N,shift=shift_value,r_rr=rr,
                                    theta_t=td,theta_r=tr,p=p)
    assert (f(shift+h)-f(shift-h))/(2*h)==pytest.approx(-p*tr,rel=1e-10)
    def g(n):
        return dust_reduced_density(N=n,shift=shift,r_rr=rr,
                                    theta_t=td,theta_r=tr,p=p)
    assert (g(N+h)-g(N-h))/(2*h)==pytest.approx(
             -p*np.sqrt(1+tr*tr/rr),rel=1e-10)


def test_14_amplitude_full_hessian_rejects_bad_step(bg):
    from numerics.hr_two_dust_common_time_canonical import full_preconstraint_hessian
    with pytest.raises(ValueError):full_preconstraint_hessian(step=0,trajectory=bg)

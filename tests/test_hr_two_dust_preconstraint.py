"""Independent phase-space normalization and two-sector transport regressions."""
import math
import numpy as np
import pytest
from numerics.hr_two_dust_preconstraint import (
    two_dust_phase_compact_hessian, assemble_hr_two_dust_preconstraint,
    PRECONSTRAINT_ORDER,
)
from numerics.hr_compact_radial_interaction import compact_scalar_profile

P = dict(radius=.23,quadrature_order=18,a_g=.85,n_g=1.03,rho_g=.9,
         a_f=.74,n_f=1.16,rho_f=.6,mu=-.24,mu_dot=.11,
         sigma=.08,sigma_dot=.025,log_phidot_rate_g=.12,
         log_phidot_rate_f=-.17)
HP = dict(N=1.03,a=.85,n=1.16,alpha=.74,k=2.2,m2=.7,Mg2=1.2,
          betas=(.31,1.,-.4,.2,.13),mu=-.24,sigma_r=.08,
          sigma_dot=.025,mu_dot=.11,n_dot=.09,alpha_dot=-.07,
          n_ddot=.025,alpha_ddot=-.02)

def norm(R,order=60):
    x,w=np.polynomial.legendre.leggauss(order)
    rr=R*(x+1)/2
    F=np.array([compact_scalar_profile(t,R)[0] for t in rr])
    return float(np.sum(R*w/2*rr**2*F**2))

def test_visible_canonical_normalization_is_spherical_volume():
    H=two_dust_phase_compact_hessian(**P)
    expected=4*math.pi*P['n_g']*P['a_g']**3*norm(P['radius'])
    assert H[17,20]==pytest.approx(expected,rel=2e-11)

def test_twin_canonical_pair_and_stueckelberg_cancellation():
    H=two_dust_phase_compact_hessian(**P)
    expected=4*math.pi*P['n_f']*P['a_f']**3*(1+P['mu'])**3*norm(P['radius'])
    assert H[19,21]==pytest.approx(expected,rel=2e-11)
    assert H[19,10]==pytest.approx(-expected,rel=2e-11)
    assert H[19,18]==pytest.approx(-H[19,8],rel=1e-12)

def test_two_dust_hessian_preserves_canonical_momentum_structure():
    H=two_dust_phase_compact_hessian(**P)
    np.testing.assert_allclose(H,H.T,atol=2e-14,rtol=0)
    assert len(PRECONSTRAINT_ORDER)==22
    assert PRECONSTRAINT_ORDER[-6:]==('Y_g','p_g','Y_f','p_f','Y_g_dot','Y_f_dot')
    np.testing.assert_allclose(H[np.ix_([17,19],[17,19])],0,atol=1e-14)
    # For sigma != 0, native q_R contains a rate component because the
    # native foliation tilts relative to common time. Not an extra mode.
    assert H[20,20]==0 and H[20,21]==0 and H[21,21]<0
    Hstraight=two_dust_phase_compact_hessian(**dict(P,sigma=0.))
    assert Hstraight[21,21]==pytest.approx(0.,abs=1e-14)
    assert H[17,20]>0 and H[19,21]>0
    assert H[17,21]==0 and H[19,20]==0

def test_material_relative_phase_zero_for_Yf_equal_T():
    H=two_dust_phase_compact_hessian(**P)
    x=np.zeros(22)
    x[8]=x[18]=.23
    x[10]=x[21]=-.14
    x[19]=.09
    assert abs(x@H@x)<1e-13

def test_phase_hessian_matches_independent_direct_density_quadrature():
    H=two_dust_phase_compact_hessian(**P)
    x=np.zeros(22)
    x[[0,1,4,5,8,10,16,17,18,19,20,21]] = [
        .13,.04,-.02,-.06,.17,.08,.21,-.11,.37,.14,-.05,.19]
    t,w=np.polynomial.legendre.leggauss(P['quadrature_order'])
    R=P['radius'];S=0.
    for z,ww in zip(t,w):
        r=.5*R*(1+z)
        F,Fr,_,_=compact_scalar_profile(r,R)
        J=np.array([[1+.5*P['sigma_dot']*r*r,P['sigma']*r],
                    [P['mu_dot']*r,1+P['mu']]])
        D=float(np.linalg.det(J))
        yg=x[16]*F;ygdot=x[20]*F;pg=x[17]*F
        pgphi=x[0]*F;Ug=x[1]*Fr
        mg=P['n_g']*P['a_g']**3*r*r
        lg=pg*(ygdot+P['log_phidot_rate_g']*yg-pgphi)
        lg+=.5*P['rho_g']*pgphi**2
        lg-=.5*P['n_g']**2*P['rho_g']/P['a_g']**2*(x[16]*Fr+P['a_g']/P['n_g']*Ug)**2
        y=(x[18]-x[8])*F;ydot=(x[21]-x[10])*F
        grad=np.linalg.solve(J.T,[ydot,(x[18]-x[8])*Fr])
        pf=x[19]*F;phif=x[4]*F;Uf=x[5]*Fr
        mf=D*P['n_f']*P['a_f']**3*((1+P['mu'])*r)**2
        lf=pf*(grad[0]+P['log_phidot_rate_f']*y-phif)
        lf+=.5*P['rho_f']*phif**2
        lf-=.5*P['n_f']**2*P['rho_f']/P['a_f']**2*(grad[1]+P['a_f']/P['n_f']*Uf)**2
        S+=2*math.pi*R*ww*(mg*lg+mf*lf)
    assert .5*x@H@x==pytest.approx(S,rel=2e-12,abs=2e-13)

def test_quadrature_convergence():
    a=two_dust_phase_compact_hessian(**dict(P,quadrature_order=16))
    b=two_dust_phase_compact_hessian(**dict(P,quadrature_order=28))
    np.testing.assert_allclose(a,b,atol=1e-12,rtol=1e-11)

def test_combined_hr_and_two_dust_hessians_add_without_rate_invention():
    out=assemble_hr_two_dust_preconstraint(radius=.23,quadrature_order=16,
        rho_g=.9,rho_f=.6,log_phidot_rate_g=.12,
        log_phidot_rate_f=-.17,**HP)
    assert out.hessian.shape==(22,22)
    np.testing.assert_allclose(out.hessian,out.interaction_hessian+out.dust_hessian,
                               rtol=0,atol=2e-13)
    assert np.max(abs(out.interaction_hessian[16:,:]))==0
    assert abs(out.hessian[19,21])>0
    assert abs(out.hessian[19,10])>0
    np.testing.assert_allclose(out.hessian,out.hessian.T,rtol=0,atol=2e-13)

def test_singular_chart_and_invalid_dust_rejected():
    with pytest.raises(ValueError): two_dust_phase_compact_hessian(**dict(P,mu=-1.))
    with pytest.raises(ValueError): two_dust_phase_compact_hessian(**dict(P,rho_f=-.1))
    with pytest.raises(ValueError): two_dust_phase_compact_hessian(**dict(P,sigma_dot=-2000.))

def test_native_tilt_rate_square_matches_independent_integral():
    H=two_dust_phase_compact_hessian(**P)
    x,w=np.polynomial.legendre.leggauss(60)
    R=P['radius'];rr=R*(x+1)/2
    F=np.array([compact_scalar_profile(t,R)[0] for t in rr])
    Rr=1+P['mu'];Tr=P['sigma']*rr
    D=(1+.5*P['sigma_dot']*rr*rr)*Rr-Tr*(P['mu_dot']*rr)
    expected=-4*math.pi*P['n_f']**3*P['a_f']*P['rho_f']*Rr**2
    expected*=np.sum(R*w/2*rr**2*Tr**2*F**2/D)
    assert H[21,21]==pytest.approx(expected,rel=2e-11)
    assert expected<0

def test_two_independent_canonical_momenta_survive_transport():
    H=two_dust_phase_compact_hessian(**P)
    # The independent matter momenta p_g and p_f remain coupled to
    # independent common-time velocities Y_gdot and (Y_fdot-Tdot).
    D=H[np.ix_([17,19],[20,21])]
    assert np.linalg.matrix_rank(D,tol=1e-12)==2
    np.testing.assert_allclose(D,np.diag(np.diag(D)),atol=1e-14)
    assert H[19,10]==pytest.approx(-D[1,1],rel=1e-12)

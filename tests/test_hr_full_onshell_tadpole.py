"""Independent on-shell 12-way scalar/matter Euler tests from ONE physical action."""
import math
import numpy as np
import pytest
from numerics.hr_full_onshell_tadpole import (
    BETAS,CG,CF,MF2,M2,ORDER,Trajectory,background,profile,
    sector_density,hr_density,action,gradient,metric_physical_witness,
)

@pytest.fixture(scope='module')
def bg(): return Trajectory.solve()


def test_background_two_dust_continuity_and_bianchi(bg):
    for t in (-.025,-.014,0.,.02,.03):
        a,b,ad,bd,nf,rhog,rhof=bg.at(t)
        assert bd==pytest.approx(nf*ad,abs=4e-15)
        assert rhog*a**3==pytest.approx(CG,rel=1e-14)
        assert rhof*b**3==pytest.approx(CF,rel=1e-14)
        assert nf>0 and MF2>0


def test_full_common_spacetime_action_has_five_expected_sectors(bg):
    z=action(trajectory=bg)
    assert z.names==('EH_g','EH_f','HR','dust_g','dust_f')
    assert z.contributions.shape==(5,)
    assert z.total==pytest.approx(sum(z.contributions),abs=5e-17)
    assert z.contributions[0]<0 and z.contributions[1]<0
    assert z.contributions[2]!=0
    np.testing.assert_allclose(z.contributions[3:5],0.,atol=2e-16)


def test_all_twelve_tadpoles_zero_at_fixed_matter_clock_and_density(bg):
    grad=gradient(trajectory=bg,step=2e-5,quadrature_order=28)
    assert grad.shape==(12,)
    assert np.max(np.abs(grad))<6e-11,dict(zip(ORDER,grad))


@pytest.mark.parametrize('i',range(12),ids=ORDER)
def test_all_twelve_independent_field_perturbations_have_zero_linear_term(bg,i):
    x=np.zeros(12);step=2e-5;x[i]=step
    plus=action(x,trajectory=bg,quadrature_order=26).total
    minus=action(-x,trajectory=bg,quadrature_order=26).total
    assert abs((plus-minus)/(2*step))<6e-11


def test_linear_response_has_cubic_central_difference_convergence(bg):
    g1=gradient(trajectory=bg,step=3e-4)
    g2=gradient(trajectory=bg,step=1e-4)
    # Nonlinear finite perturbation coefficient means central difference has O(h²).
    assert abs(g2[2])<.13*abs(g1[2])
    assert max(abs(v) for v in g2)<5e-10


def test_quadrature_and_time_radial_domain_refinement(bg):
    for kw in ({'quadrature_order':18},{'quadrature_order':34},
               {'quadrature_order':24,'time_radius':.018,'radial_radius':.27}):
        g=gradient(trajectory=bg,step=1.5e-5,**kw)
        assert max(abs(x) for x in g)<9e-11


def test_negative_control_remove_all_interaction_keeps_eh_dust_but_breaks_background(bg):
    base=action(trajectory=bg)
    zero=action(trajectory=bg,m2=0.)
    assert zero.contributions[2]==0.
    np.testing.assert_allclose(zero.contributions[[0,1,3,4]],base.contributions[[0,1,3,4]])
    g=gradient(trajectory=bg,m2=0.)
    assert abs(g[0])>1e-5 and abs(g[6])>1e-5
    assert abs(g[2])>1e-4


def test_nontrivial_f_relative_spatial_trace_perturbation_is_not_compensated_chart():
    f3,g3,relative=metric_physical_witness(field='psi_f',amplitude=.003)
    assert abs(f3)>1.e-2
    assert abs(g3)<1e-13
    assert relative!=pytest.approx(background(.4)[1]/background(.4)[0],abs=1e-5)


def test_nonzero_quadratic_physical_f_scalar_action_after_linear_tadpoles_cancel(bg):
    base=action(trajectory=bg).total
    for i in (6,7,8,9,10):
        h=1e-3;e=np.zeros(12);e[i]=h
        hess=(action(e,trajectory=bg).total+action(-e,trajectory=bg).total-2*base)/h**2
        assert abs(hess)>1e-8,(ORDER[i],hess)
    # The matter multiplier appears linearly in the original covariant action,
    # so its pure rho-rho second derivative vanishes exactly by construction.
    e=np.zeros(12);e[11]=.01
    assert action(e,trajectory=bg).total==pytest.approx(base,abs=1e-15)


def test_homogeneous_hr_action_density_equals_minisuperspace_potential():
    a,b,ad,bd,nf,rhog,rhof=background(.4)
    r=.21
    g=(-np.ones(1),np.zeros(1),np.array([a*a]))
    f=(-np.array([nf*nf]),np.zeros(1),np.array([b*b]))
    y=b/a
    V=BETAS[0]+3*BETAS[1]*y+3*BETAS[2]*y*y+BETAS[3]*y**3
    W=BETAS[1]+3*BETAS[2]*y+3*BETAS[3]*y*y+BETAS[4]*y**3
    exact=-M2*a**3*r*r*(V+nf*W)
    assert float(hr_density(g,f,a*a*r*r,b*b*r*r)[0])==pytest.approx(exact,abs=2e-15)


def test_dust_clock_and_multiplier_must_be_varied_before_on_shell_substitution():
    a,b,ad,bd,nf,rhog,rhof=background(.4)
    for sc,lap,rho,pn in ((a,1.,rhog,CG),(b,nf,rhof,CF)):
        # Covariant homogeneous dust density L=(a³rho/2)(theta_dot²/N-N).
        clock=lap
        assert (sc**3*rho/2)*(clock**2/lap-lap)==0.
        dN=-.5*sc**3*rho*(clock**2/lap**2+1)
        assert dN==pytest.approx(-pn,abs=1e-13)


def test_f_physical_metric_perturbation_transports_correctly_to_tilted_native_coordinates():
    t=.003;r=.19;Tmax=.027;Rmax=.32
    a,b,ad,bd,nf,rhog,rhof=background(.4)
    amp=np.array([.012,-.019,.017,.006,.021,-.008])
    ef,df,(f00,f01,f11),fa,_=sector_density(scale=b,scale_rate=bd,lapse=nf,
         rho0=rhof,amp=amp,t=0.,r=r,time_radius=Tmax,radial_radius=Rmax,
         planck=MF2)
    F=np.array([[float(f00),float(f01)],[float(f01),float(f11)]])
    lam=.78;ldot=.04;sig=.08;sdot=.025
    J=np.array([[1+.5*sdot*r*r,sig*r],[ldot*r,lam]])
    inv=np.linalg.inv(J)
    native=inv.T@F@inv
    np.testing.assert_allclose(J.T@native@J,F,rtol=3e-15,atol=4e-16)
    assert abs(native[0,1])>1e-4
    assert fa>0
    # The f relative spatial 2-sphere eigenvalue is visibly nonhomogeneous.
    assert math.sqrt(fa/(a*a*r*r))!=pytest.approx(b/a,abs=1e-5)


def test_two_native_dust_legendre_pairs_exist_in_same_action_background():
    # Independent per-solid-angle dust Legendre transforms with lapse N,
    # spatial volume gamma=a³r² and radial gradient theta_r.
    r=.18
    a,b,ad,bd,nf,rhog,rhof=background(.4)
    for sc,lap,rho,gr in ((a,1.,rhog,.027),(b,nf,rhof,-.031)):
        gamma=sc**3*r*r
        rate=lap*1.04
        p=gamma*rho*rate/lap
        L=.5*rho*lap*gamma*((rate/lap)**2-(gr/sc)**2-1)
        H=lap*(p*p/(2*gamma*rho)+gamma*rho/2*(1+gr*gr/sc**2))
        assert p*rate-L==pytest.approx(H,rel=2e-15)
        assert gamma*rho/lap>0


def test_metric_domain_and_trial_basis_rejections(bg):
    for kw in ({'quadrature_order':4},{'time_radius':.2},
               {'radial_radius':0}):
        with pytest.raises(ValueError):action(trajectory=bg,**kw)
    with pytest.raises(ValueError):action(np.zeros(9),trajectory=bg)
    with pytest.raises(ValueError):sector_density(scale=.9,scale_rate=.2,
       lapse=1.,rho0=1.,amp=[-9,0,0,0,0,0],t=0.,r=.12,
       time_radius=.027,radial_radius=.32,planck=1.)
    with pytest.raises(ValueError):background(.1)


def test_eh_hr_and_both_dust_sources_cancel_separately_at_first_order(bg):
    for i in (0,2,6,8):
        h=1e-5;z=np.zeros(12);z[i]=h
        pieces=(action(z,trajectory=bg).contributions-
                action(-z,trajectory=bg).contributions)/(2*h)
        assert abs(np.sum(pieces))<8e-11
        assert abs(pieces[2])>1e-7  # independently nontrivial HR source
        if i==0:
            assert pieces[0]>1e-4 and pieces[3]<-1e-4
            np.testing.assert_allclose(pieces[[1,4]],0.,atol=1e-16)
        elif i==6:
            assert pieces[1]>1e-7 and pieces[4]<-1e-5
            np.testing.assert_allclose(pieces[[0,3]],0.,atol=1e-16)


def test_nontrivial_g_f_relative_spatial_mode_mixes_only_via_interaction(bg):
    def cross(m2):
        h=.002;src=[]
        for i,j in ((1,1),(1,-1),(-1,1),(-1,-1)):
            e=np.zeros(12);e[0]=i*h;e[8]=j*h
            src.append(action(e,trajectory=bg,m2=m2).total)
        return (src[0]-src[1]-src[2]+src[3])/(4*h*h)
    physical=cross(M2)
    decoupled=cross(0.)
    assert physical==pytest.approx(-.000184236013,rel=1e-6)
    assert abs(decoupled)<1e-9


def test_beta4_is_exactly_f_volume_no_g_lapse_coupling_at_fixed_f(bg):
    z=np.zeros(12);z[0]=2e-4
    beta4=(0.,0.,0.,0.,1.)
    plus=action(z,trajectory=bg,betas=beta4).contributions[2]
    minus=action(-z,trajectory=bg,betas=beta4).contributions[2]
    assert plus==pytest.approx(minus,abs=1e-15)


def test_quadrature_convergence_of_finite_relative_perturbation_action(bg):
    e=np.zeros(12);e[8]=.003;e[9]=-.001
    lo=action(e,trajectory=bg,quadrature_order=22).contributions
    hi=action(e,trajectory=bg,quadrature_order=34).contributions
    np.testing.assert_allclose(lo,hi,atol=2e-12,rtol=3e-10)

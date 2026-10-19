"""Falsifiable curved/noncomoving primary-surface controls, not BD secondary."""
import math
import numpy as np
import pytest
import sympy as sp
from numerics.hr_curved_moving_dust_primary import (
    R,BETA,M2,MG2,MF2,build_primary,assert_regular)

@pytest.fixture(scope='module')
def witness():
    return build_primary()


def test_exact_primary_constraints_on_genuinely_curved_noncomoving_witness(witness):
    w=assert_regular(witness)
    assert w['primary_max']<1e-12
    assert w['curvature_g_max']>.1 and w['curvature_f_max']>.1
    assert w['phase_g_max']>1e-4 and w['phase_f_max']>1e-4
    assert w['Dg_max']>1e-4
    assert w['max_abs_z']>.01
    assert w['dust_g_min']>0 and w['dust_f_min']>0


@pytest.mark.parametrize('r',[.11,.17,.28,.43,.66,.83,.89])
def test_original_unsimplified_adm_constraint_densities_match_zeros(witness,r):
    # Independently reconstruct canonical constraints from raw spherical R3,
    # without using the witness's internally generated Hg/Hf/Ddiag/Fz.
    names=('Lg','Sg','Lf','Sf','pLg','pSg','pLf','pSf','pg','pf',
           'thgr','thfr','z','K','Wg','Wf','R3g','R3f')
    v=dict(zip(names,witness.eval(r,names).flatten()))
    Sr_g=float(sp.lambdify(R,sp.diff(witness.expr['Sg'],R),'numpy')(r))
    Sr_f=float(sp.lambdify(R,sp.diff(witness.expr['Sf'],R),'numpy')(r))
    plr_g=float(sp.lambdify(R,sp.diff(witness.expr['pLg'],R),'numpy')(r))
    plr_f=float(sp.lambdify(R,sp.diff(witness.expr['pLf'],R),'numpy')(r))
    # The actual original ADM three-curvature geometric density, not source algebra.
    def original(L,S,pL,pS,p,th,curv,Mp2):
        C=L*pL*pL/(4*Mp2*S*S)-pL*pS/(2*Mp2*S)
        C-=Mp2*L*S*S*curv/2
        C+=p*math.sqrt(1+(th/L)**2)
        return C
    Cg=original(v['Lg'],v['Sg'],v['pLg'],v['pSg'],v['pg'],v['thgr'],v['R3g'],MG2)
    Cf=original(v['Lf'],v['Sf'],v['pLf'],v['pSf'],v['pf'],v['thfr'],v['R3f'],MF2)
    Dg=v['pSg']*Sr_g-v['Lg']*plr_g+v['pg']*v['thgr']
    Df=v['pSf']*Sr_f-v['Lf']*plr_f+v['pf']*v['thfr']
    Hg=Cg+v['z']*Dg/v['Lg']+v['Wg']
    Hf=Cf+v['z']*Dg/v['Lf']+v['Wf']
    Fz=Dg-v['K']*v['z']/math.sqrt(1-v['z']**2)
    np.testing.assert_allclose((Hg,Hf,Dg+Df,Fz),0.,atol=4e-13,rtol=0)
    assert abs(Dg)>1e-6 and abs(Df)>1e-6
    assert abs(v['thgr'])>1e-5 and abs(v['thfr'])>1e-5


def test_original_hassan_rosen_radial_principal_root_vs_affine_lapses(witness):
    # Independent original 2x2 block principal root for arbitrary nonzero
    # lapses and common shift, versus the *whole* lapse-affine canonical H.
    b0,b1,b2,b3,b4=BETA
    for r in (.16,.43,.8):
        keys=('Lg','Sg','Lf','Sf','z','Wg','Wf','Dg','Df','Cgg','Cff')
        q=dict(zip(keys,witness.eval(r,keys).flatten()))
        for Ng,Nf,V in ((1.2,.9,.02),(.7,1.8,-.03)):
            Vg=V+(Ng/q['Lg']+Nf/q['Lf'])*q['z']; Vf=V
            # 2x2 Lorentzian metric covariants (tt,tr,rr) in common chart
            def metric(N,L,V):return np.array([[-N*N+L*L*V*V,L*L*V],[L*L*V,L*L]],float)
            g=metric(Ng,q['Lg'],Vg);f=metric(Nf,q['Lf'],Vf)
            A=np.linalg.solve(g,f)
            det=np.linalg.det(A)
            assert det>0
            trace=np.trace(A)
            t=math.sqrt(trace+2*math.sqrt(det))
            ell=q['Sf']/q['Sg']; rootdet=math.sqrt(det)
            e=[1,t+2*ell,rootdet+2*ell*t+ell**2,
               2*ell*rootdet+ell**2*t,ell**2*rootdet]
            HR=M2*MG2*q['Lg']*q['Sg']**2*Ng*sum(b*e0 for b,e0 in zip(BETA,e))
            by_affine=Ng*q['Wg']+Nf*q['Wf']
            assert HR==pytest.approx(by_affine,rel=2e-12,abs=2e-12)
            old=Ng*q['Cgg']+Nf*q['Cff']+Vg*q['Dg']+Vf*q['Df']+HR
            new=Ng*(q['Cgg']+q['z']*q['Dg']/q['Lg']+q['Wg'])+Nf*(q['Cff']+q['z']*q['Dg']/q['Lf']+q['Wf'])+V*(q['Dg']+q['Df'])
            assert old==pytest.approx(new,rel=2e-12,abs=2e-12)
            assert abs(new)<2e-12


def test_true_curvature_against_direct_finite_difference_of_spatial_geometry(witness):
    for r in (.18,.39,.75):
        for s in ('g','f'):
            L=witness.expr['L'+s];S=witness.expr['S'+s]
            lv=sp.lambdify(R,L,'numpy');sv=sp.lambdify(R,S,'numpy')
            delta=1e-4
            lp= (lv(r+delta)-lv(r-delta))/(2*delta)
            sp1=(sv(r+delta)-sv(r-delta))/(2*delta)
            sp2=(sv(r+delta)-2*sv(r)+sv(r-delta))/delta**2
            W=sp1/lv(r)
            Wr=sp2/lv(r)-sp1*lp/lv(r)**2
            R3=2/sv(r)**2*(1-W**2-2*sv(r)/lv(r)*Wr)
            old=float(witness.eval(r,('R3'+s,))[0])
            assert R3==pytest.approx(old,rel=2e-4,abs=3e-5)


@pytest.mark.parametrize('c_g,c_f,t_g,t_f,zrate',[
    (.0,.0,.0,.0,.0),(.006,-.009,.006,-.007,.02),
    (-.013,.014,-.015,.012,-.035),(.018,-.014,.012,.008,.05)])
def test_continuity_from_flat_comoving_to_curved_tilted(c_g,c_f,t_g,t_f,zrate):
    w=build_primary(curv_g=c_g,curv_f=c_f,theta_g=t_g,theta_f=t_f,z_slope=zrate)
    x=assert_regular(w,np.array([.15,.27,.43,.59,.83]))
    assert x['primary_max']<1e-12


def test_nonzero_momentum_and_matter_gradients_are_required_for_cancellation(witness):
    # Deliberately erase an essential term from the SAME primary equations.
    r=.43
    names=('pg','pf','thgr','thfr','Dg','Df','K','z','Lg','Lf','Sg','Sf')
    v=dict(zip(names,witness.eval(r,names).flatten()))
    # Removing the g dust momentum part from radial D without re-solving pS
    # breaks both momentum primary and algebraic relative-shift equation.
    badD=v['Dg']-v['pg']*v['thgr']
    assert abs(badD+v['Df'])>1e-5
    assert abs(badD-v['K']*v['z']/math.sqrt(1-v['z']**2))>1e-5
    # Flattening the geometry changes the spatial curvature term by a lot.
    assert abs(float(witness.eval(r,('R3g',))[0]))>.1


def test_two_phase_clocks_independent_and_regular_at_center(witness):
    for r in (1e-6,.2,.8):
        thgr,thfr,Lg,Lf = witness.eval(r,('thgr','thfr','Lg','Lf')).flatten()
        assert thgr/Lg==pytest.approx(witness.params['theta_g']*r)
        assert thfr/Lf==pytest.approx(witness.params['theta_f']*r)
        assert thgr*thfr<0
    assert sp.simplify(sp.diff(witness.expr['tg'],R)-witness.expr['thgr'])==0
    assert sp.simplify(sp.diff(witness.expr['tf'],R)-witness.expr['thfr'])==0


def test_three_dimensions_spatial_curvature_nonzero_and_different(witness):
    for r in (.2,.43,.75):
        R3g,R3f=witness.eval(r,('R3g','R3f')).flatten()
        assert abs(R3g)>1 and abs(R3f)>1 and R3g*R3f<0


def test_relative_shift_root_and_two_radial_momentum_densities(witness):
    vals=witness.eval(np.linspace(.11,.89,19),('z','K','Dg','Df','Ddiag','Fz'))
    z,k,dg,df,d,fr=vals
    np.testing.assert_allclose(d,0,atol=1e-12)
    np.testing.assert_allclose(fr,0,atol=1e-12)
    np.testing.assert_allclose(dg, k*z/np.sqrt(1-z*z),atol=1e-12)
    np.testing.assert_allclose(df,-dg,atol=1e-12)
    assert np.min(np.abs(dg))>0


def test_positive_dust_density_is_not_baked_into_algebraic_solver():
    # The witness is only accepted where both independently computed dust
    # positive momenta are actually checked; no abs() or clipping allowed.
    w=build_primary(curv_g=.015,curv_f=-.012)
    p=w.eval(np.linspace(.11,.89,15),('pg','pf'))
    assert np.min(p)>0
    assert not np.allclose(p[0],p[1])


def test_failure_guards():
    with pytest.raises(ValueError):build_primary(curv_g=1)
    with pytest.raises(ValueError):build_primary(a=-.4)
    with pytest.raises(ValueError):build_primary(theta_f=float('nan'))
    w=build_primary()
    with pytest.raises(ValueError):w.eval(0.)
    with pytest.raises(ValueError):w.eval(float('nan'))


def test_flat_zero_gradient_limit_original_step33f_dust_formula():
    w=build_primary(curv_g=0,curv_f=0,theta_g=0,theta_f=0,z_slope=0,
                    grav_g=0,grav_f=0)
    r=.43;a=w.params['a'];b=w.params['b'];y=b/a
    P_g=w.expr['pLg']/R**2;P_f=w.expr['pLf']/R**2
    P_g=float(sp.lambdify(R,P_g,'numpy')(r));P_f=float(sp.lambdify(R,P_f,'numpy')(r))
    b0,b1,b2,b3,b4=BETA
    Vg=b0+3*b1*y+3*b2*y*y+b3*y**3
    Vf=b1+3*b2*y+3*b3*y*y+b4*y**3
    pg0=r*r*(3*P_g*P_g/(4*MG2*a)-M2*MG2*a**3*Vg)
    pf0=r*r*(3*P_f*P_f/(4*MF2*b)-M2*MG2*a**3*Vf)
    pg,pf=w.eval(r,('pg','pf')).flatten()
    assert pg==pytest.approx(pg0,rel=2e-13)
    assert pf==pytest.approx(pf0,rel=2e-13)

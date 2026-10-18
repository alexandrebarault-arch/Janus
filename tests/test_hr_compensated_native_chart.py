"""Step30 exact inverse-chart compensation, on-shell dust and HR controls."""
import math
import numpy as np
import pytest
from numerics.hr_compensated_native_chart import (
    HomogeneousDustTrajectory,Chart,branch_point,CG,CF,BETA,M2,
    physical_f_metric,physical_g_metric,native_compensated_f,
    uncompensated_native_flrw,pull_native_to_common,
    spherical_hr_density,analytic_homogeneous_hr_density,
    native_current_divergence,direct_g_lapse_residual,
)

@pytest.fixture(scope='module')
def model():return HomogeneousDustTrajectory.solve(),Chart()


def test_dust_only_candidate_c_quartic_root_and_time_branch():
    y,yN,E,nf=branch_point(.4)
    assert y==pytest.approx(.578770722803,abs=5e-10)
    assert nf==pytest.approx(.518526433828,abs=5e-10)
    assert E==pytest.approx(2.385971903909,abs=5e-10)


def test_homogeneous_ivp_preserves_dynamical_bianchi_and_charges(model):
    bg,_=model
    for t in (-.05,-.03,0.,.025,.06):
        q=bg.at(t)
        assert q['bdot']==pytest.approx(q['Nf']*q['adot'],rel=2e-15)
        assert q['rho_g']*q['a']**3==pytest.approx(CG,rel=2e-15)
        assert q['rho_f']*q['b']**3==pytest.approx(CF,rel=2e-15)
    h=1e-5
    for t in (-.03,0.,.035):
        theta_rate=(bg.at(t+h)['theta']-bg.at(t-h)['theta'])/(2*h)
        assert theta_rate==pytest.approx(bg.at(t)['Nf'],rel=5e-9)


def test_nonhomothetic_chart_inverse_and_orientation(model):
    _,chart=model
    for t,r in ((-.04,.05),(0.,.12),(.03,.25),(.05,.32)):
        T,R,J,D=chart.forward(t,r)
        ti,ri,ji,di=chart.inverse(T,R)
        assert ti==pytest.approx(t,abs=3e-14)
        assert ri==pytest.approx(r,abs=3e-14)
        np.testing.assert_allclose(ji,J,atol=1e-14)
        assert D>0 and di==pytest.approx(D)


def test_native_inverse_pullback_reproduces_both_f_metric_components(model):
    bg,chart=model
    for t,r in ((-.04,.07),(-.015,.24),(0.,.20),(.05,.29)):
        T,R,J,_=chart.forward(t,r)
        c=native_compensated_f(T,R,bg,chart)
        physical,area=physical_f_metric(bg.at(t),r)
        recovered,areaback=pull_native_to_common(c['native'],c['angular'],J)
        np.testing.assert_allclose(recovered,physical,atol=3e-14,rtol=5e-14)
        assert areaback==pytest.approx(area,rel=2e-15)
        assert abs(c['native'][0,1])>1e-6


def test_explicit_inverse_jacobian_native_metric_formula(model):
    bg,chart=model;t=.02;r=.21
    T,R,J,D=chart.forward(t,r);q=bg.at(t)
    z=native_compensated_f(T,R,bg,chart)
    lam=J[1,1];Tt=J[0,0];Tr=J[0,1];Rt=J[1,0]
    nt=q['Nf'];b=q['b']
    direct=np.array([[-nt*nt*lam*lam+b*b*Rt*Rt,
                       nt*nt*lam*Tr-b*b*Rt*Tt],
                      [nt*nt*lam*Tr-b*b*Rt*Tt,
                       -nt*nt*Tr*Tr+b*b*Tt*Tt]])/D**2
    np.testing.assert_allclose(z['native'],direct,atol=2e-15)
    assert direct[0,1]!=0


def test_compensated_native_dust_clock_norm_exact(model):
    bg,chart=model
    for t,r in ((-.03,.09),(0.,.2),(.045,.31)):
        T,R,_,_=chart.forward(t,r)
        z=native_compensated_f(T,R,bg,chart)
        norm=z['grad']@np.linalg.solve(z['native'],z['grad'])
        assert norm==pytest.approx(-1.,abs=2e-14)
        assert z['rho']>0
        # A tilted native f phase must have a radial derivative.
        assert abs(z['grad'][1])>1e-4


def test_native_dust_current_exact_piola_transformation(model):
    bg,chart=model
    for t,r in ((-.02,.08),(0.,.2),(.025,.33)):
        T,R,J,D=chart.forward(t,r)
        z=native_compensated_f(T,R,bg,chart)
        expected=CF*r*r*J[:,0]/D
        np.testing.assert_allclose(z['current'],expected,atol=2e-15,rtol=3e-13)
        # Nonzero native radial flux when lambda_dot != 0.
        assert z['current'][1]>0


def test_native_dust_current_conservation_across_compact_chart(model):
    bg,chart=model
    for t,r in ((-.025,.15),(0.,.2),(.028,.28)):
        T,R,_,_=chart.forward(t,r)
        assert abs(native_current_divergence(T,R,bg,chart,h=3e-5))<1e-9
        assert abs(native_current_divergence(T,R,bg,chart,h=1.5e-5))<3e-10


def test_exact_hr_interaction_matches_homogeneous_on_shell_across_radius(model):
    bg,chart=model
    for t,r in ((-.03,.07),(.0,.12),(.025,.2),(.04,.3)):
        T,R,J,_=chart.forward(t,r)
        native=native_compensated_f(T,R,bg,chart)
        f,af=pull_native_to_common(native['native'],native['angular'],J)
        g,ag=physical_g_metric(bg.at(t),r)
        direct=spherical_hr_density(g,ag,f,af)
        analytic=analytic_homogeneous_hr_density(bg.at(t),r)
        assert direct==pytest.approx(analytic,abs=4e-14,rel=2e-13)


def test_direct_g_lapse_variation_zero_on_fully_compensated_onshell_background(model):
    bg,chart=model
    for t,r in ((-.03,.08),(0.,.12),(.01,.2),(.04,.3)):
        T,R,J,_=chart.forward(t,r)
        z=native_compensated_f(T,R,bg,chart)
        f,af=pull_native_to_common(z['native'],z['angular'],J)
        residual=direct_g_lapse_residual(bg.at(t),r,f,af,step=8e-6)
        assert abs(residual)<7e-9


def test_naive_uncompensated_native_flrw_reproduces_step29_center_red(model):
    bg,chart=model;t=0.;r=1e-4
    T,R,J,_=chart.forward(t,r);q=bg.at(t)
    native,af=uncompensated_native_flrw(T,R,bg,chart,
                                        central_scale_compensated=False)
    f,af=pull_native_to_common(native,af,J)
    residual=direct_g_lapse_residual(q,r,f,af)
    assert residual==pytest.approx(.160780603695,rel=5e-7)


def test_scale_only_compensation_passes_center_but_fails_finite_radius(model):
    bg,chart=model
    results=[]
    for r in (1e-4,.05,.1,.2):
        T,R,J,_=chart.forward(0.,r)
        f,af=uncompensated_native_flrw(T,R,bg,chart,
                                       central_scale_compensated=True)
        f,af=pull_native_to_common(f,af,J)
        results.append(direct_g_lapse_residual(bg.at(0.),r,f,af))
    assert abs(results[0])<3e-8
    assert results[-1]>2e-4
    assert 3.6 < abs(results[-1]/results[-2]) < 4.4  # O(r²) source


def test_compensated_native_requires_nonflrw_shift_and_spatial_terms(model):
    bg,chart=model;t=0.;r=.2
    T,R,J,_=chart.forward(t,r)
    exact=native_compensated_f(T,R,bg,chart)
    forced,forced_area=uncompensated_native_flrw(T,R,bg,chart)
    assert abs(exact['native'][0,1]-forced[0,1])>1e-3
    assert abs(exact['native'][1,1]-forced[1,1])>3e-5
    f_forced,area_forced=pull_native_to_common(forced,forced_area,J)
    f_correct,area_correct=pull_native_to_common(exact['native'],exact['angular'],J)
    assert np.linalg.norm(f_forced-f_correct)>3e-3
    assert area_forced==pytest.approx(area_correct)


def test_coordinate_only_relabelling_cannot_rescue_physical_fold(model):
    bg,chart=model
    q=bg.at(0.)
    # Exact compensation returns the SAME y on every common slice; it has
    # no independent relative-mu field. Lambda is chart convention only.
    for r in (.02,.1,.2):
        T,R,J,_=chart.forward(0.,r)
        c=native_compensated_f(T,R,bg,chart)
        f,af=pull_native_to_common(c['native'],c['angular'],J)
        g,ag=physical_g_metric(q,r)
        assert math.sqrt(af/ag)==pytest.approx(q['b']/q['a'],abs=2e-15)
    assert abs(chart.lam0-1.)>.1


def test_basic_parameter_guards_and_singular_jacobian():
    with pytest.raises(ValueError):branch_point(0.01)
    with pytest.raises(ValueError):HomogeneousDustTrajectory.solve(halfwidth=-1.)
    with pytest.raises(ValueError):Chart(lam0=-.3).forward(0.,.2)
    with pytest.raises(ValueError):Chart().inverse(0.,-.1)
    with pytest.raises(ValueError):native_current_divergence(0.,0.,None,Chart())


def test_offshell_dust_native_lagrangian_nonzero_exact_density_transform(model):
    from numerics.hr_compensated_native_chart import independent_native_dust_lagrangian
    bg,chart=model
    for t,r in ((-.02,.1),(.0,.2),(.03,.28)):
        common,native_weighted,native=independent_native_dust_lagrangian(
            bg,r,chart,t=t,phase_amp=.037,density_amp=.16)
        assert abs(common)>1e-7
        assert native_weighted==pytest.approx(common,abs=1e-15,rel=5e-13)
        T,R,J,D=chart.forward(t,r)
        assert abs(native-common)>1e-7  # missing Jacobian is erroneous


def test_g_lapse_compact_time_radial_action_tadpole_restored_by_full_compensation(model):
    from numerics.hr_compensated_native_chart import compact_g_lapse_tadpole
    bg,chart=model
    res=compact_g_lapse_tadpole(bg,chart,order=20,step=2e-5)
    assert abs(res)<5e-10
    truncated=compact_g_lapse_tadpole(bg,chart,order=20,
                                     step=2e-5,scale_only=True)
    assert abs(truncated)>1e-8


def test_compact_tadpole_quadrature_and_variation_step_refine(model):
    from numerics.hr_compensated_native_chart import compact_g_lapse_tadpole
    bg,chart=model
    for order,step in ((12,4e-5),(18,2e-5),(26,1e-5)):
        corr=compact_g_lapse_tadpole(bg,chart,order=order,step=step)
        wrong=compact_g_lapse_tadpole(bg,chart,order=order,step=step,
                                     scale_only=True)
        assert abs(corr)<6e-10
        assert abs(wrong)>1e-8

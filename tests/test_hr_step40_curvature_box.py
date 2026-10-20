"""Exact rational uniform curvature gate and explicit degeneracy counter-control."""
from fractions import Fraction as F
import pytest
from numerics.hr_step40_curvature_box import (A0,Y0,R,CURV_SAFE,B2,B3,eta,j_eta,
    k_over_r2,exact_box_certificate,failure_at_antialigned,
    critical_curvature_bracket,manifest)


def test_exact_uniform_margin_exceeds_half():
    c=exact_box_certificate()
    assert F(c['J_uniform_lower_exact'])>F(1,2)
    assert F(c['K_div_r2_uniform_lower_exact'])>0
    assert c['curvature_abs_max']=='3/200'


def test_wider_uncertain_a_and_y_parameter_box():
    c=exact_box_certificate(amin=F('.395'),amax=F('.405'),
                            ymin=F('.5787'),ymax=F('.5789'))
    assert F(c['J_uniform_lower_exact'])>F(1,2)
    assert F(c['K_div_r2_uniform_lower_exact'])>0


@pytest.mark.parametrize('cg,cf',[(F('.015'),F('.015')),(F('.015'),F('-.015')),
                                   (F('-.015'),F('.015')),(F('-.015'),F('-.015')),
                                   (F(0),F(0)),(F('.007'),F('-.012'))])
def test_spatial_box_contains_true_exact_algebraic_factors(cg,cf):
    c=exact_box_certificate()
    jlower=F(c['J_uniform_lower_exact'])
    klower=F(c['K_div_r2_uniform_lower_exact'])
    for rr in (F(0),F('0.1'),F('.3'),F('.65'),R):
        assert j_eta(eta(cg,cf,rr*rr))>=jlower
        assert k_over_r2(A0,Y0,cg,cf,rr*rr)>=klower


def test_center_K_zero_is_spherical_factor_only():
    c=exact_box_certificate()
    assert k_over_r2(A0,Y0,F('0.015'),F('-0.015'),0)>0
    assert 0**2*k_over_r2(A0,Y0,F('0.015'),F('-0.015'),0)==0
    assert F(c['K_div_r2_uniform_lower_exact'])>0


def test_negative_counterexample_for_excessive_curvature():
    assert failure_at_antialigned(F('.078'))>0
    assert failure_at_antialigned(F('.08'))<0
    assert j_eta(Y0)>0
    with pytest.raises(ValueError): exact_box_certificate(cmax=F('.08'))


def test_sharp_algebraic_curvature_threshold_exists_and_unique():
    low,high=critical_curvature_bracket()
    assert F('.07854')<low<high<F('.07856')
    assert failure_at_antialigned(low)>0>failure_at_antialigned(high)
    assert high-low==F('.002')/2**72


def test_background_neighborhood_parameters_are_genuinely_independent():
    c=exact_box_certificate(amin=F('.395'),amax=F('.405'),
                            ymin=F('.5787'),ymax=F('.5789'))
    assert c['a_interval'][0] != c['a_interval'][1]
    assert c['y_interval'][0] != c['y_interval'][1]


@pytest.mark.parametrize('kw',[
    {'cmax':F(-1)}, {'rmax':F(0)}, {'amin':F(0)},
    {'amin':F(2),'amax':F(1)}, {'ymin':F(0)},
    {'ymin':F(2),'ymax':F(1)}, {'cmax':F(3)}])
def test_bad_parameter_boxes_rejected(kw):
    with pytest.raises(ValueError):exact_box_certificate(**kw)


def test_negative_conformal_denominator_guard():
    with pytest.raises(ValueError):eta(F(-2),F(0),F(1))
    with pytest.raises(ValueError):eta(F(0),F(0),F(-1))


def test_bisection_depth_guard():
    for bad in (0,-1,129,1.5):
        with pytest.raises(ValueError):critical_curvature_bracket(bad)


def test_full_manifest_keeps_dirac_and_dust_gates_explicitly_open():
    m=manifest()
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'
    assert any('dust' in s for s in m['limits'])
    assert any('Dirac' in s for s in m['limits'])

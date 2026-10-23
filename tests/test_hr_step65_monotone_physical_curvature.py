"""Original 3-module Step55 G physical benchmark G_UU monotonicity certificates."""
from fractions import Fraction as F
import pytest
import sympy as sp
from numerics import hr_step65_monotone_physical_curvature as m
from numerics import hr_step62_physical_G_curvature as prev


def test_original_physical_45_46_55_byte_gates():
    assert m.check_sources()==prev.PINNED
    assert prev.curvature_identity()['polynomial_U_degree']==2


def test_symbolic_physical_curvature_formula_uses_original_G():
    src=prev.curvature_identity()
    assert sp.cancel(sp.together(src['guu']-src['physical_formula']))==0


def test_rational_root_enclosures_are_outward_exact():
    for q in (F('0.000001'),F('1.5'),F('1.000001'),F('0.99998')):
        z=m.rational_sqrt_enclosure(q,14)
        assert z.lo*z.lo<=q<=z.hi*z.hi
        assert z.hi-z.lo<=F(1,10**14)


def test_sqrt_negative_rejected():
    with pytest.raises(ValueError):m.rational_sqrt_enclosure(F(-1,3))


def test_exact_positive_denominator_on_entire_benchmark():
    g=m.geometry_intervals(prev.Interval(0,m.S_MAX))
    assert g['interaction'].lo>0 and g['T'].lo>0
    assert g['lf'].lo>0 and g['lg'].lo>0


def test_logarithmic_curvature_factor_is_strictly_positive():
    x=m.strict_slope_certificate()
    lo,hi=map(F,x['log_derivative_interval'])
    assert 0<lo<hi<F(1,100)
    assert F(x['factor_interval'][0])>=1


def test_uniform_derivative_is_strictly_bounded_between_point8_and_one():
    x=m.strict_slope_certificate()
    lo,hi=map(F,x['G_sUU_interval'])
    assert F(4,5)<lo<hi<F(1)
    assert x['source_degree_U']==2


def test_exact_endpoint_enclosure_is_strictly_below_point634():
    y=m.sharp_endpoint_certificate()
    lo,hi=map(F,y['endpoint_curvature'])
    assert 0<lo<hi<F(317,500)
    assert lo>F(633,1000)


def test_endpoint_enclosure_is_strictly_more_informative_than_step62():
    old=prev.benchmark_rational_certificate()
    old_max=F(old['curvature'][1])
    new_max=F(m.sharp_endpoint_certificate()['endpoint_curvature'][1])
    assert new_max<old_max
    assert new_max<F(317,500)<F(337,500)


def test_strict_monotone_implies_uniform_endpoint_maximum():
    assert F(m.strict_slope_certificate()['G_sUU_interval'][0])>0
    assert prev.curvature_identity()['guu'].subs(prev.curvature_identity()['s'],0)==0
    assert m.sharp_endpoint_certificate()['uniform_G_UU_bound']==('0','317/500')


def test_taylor_sensitivity_improved_uniformly_on_real_step55_tube():
    y=m.sharp_endpoint_certificate()
    assert F(y['G_U_sensitive_bound'])==F(317,5_000_000)
    assert F(y['quadratic_Taylor_remainder'])==F(317,100_000_000_000)
    old=prev.certified_tube_linearization()
    assert F(y['G_U_sensitive_bound'])<old['Gu_difference_strict']
    assert F(y['quadratic_Taylor_remainder'])<old['Taylor_quadratic_remainder_strict']


def test_monotonicity_not_model_independent_negative_control():
    # Change sign of f dust phase slope alone, keeping other positive factors.
    # The original G_UU expression reverses sign; Step65 must NOT be
    # misrepresented as a universal theorem for all HR parameter choices.
    a=prev.curvature_identity()
    tf=a['variables']['tf0']
    assert sp.simplify(a['guu'].subs(tf,-tf)+a['guu'])==0
    assert a['guu']!=0


def test_symbolic_curvature_decreasing_in_U_still_zero():
    c=prev.curvature_identity()
    assert sp.diff(c['guu'],c['U'])==0
    assert sp.diff(c['guu'],c['U'],2)==0


def test_rejected_zero_divisor_in_interval_proof():
    with pytest.raises(ValueError,match="outside certified benchmark"): m.geometry_intervals(prev.Interval(-1000,1000))


def test_manifest_explicit_dirac_and_lapse_gates_open():
    x=m.manifest()
    assert x['temporal_Dirac_rank']=='NOT_COMPUTED'
    assert x['lapse_fixing']=='NOT_COMPUTED'
    assert x['GATE_2B']=='OPEN' and x['JANUS_R']=='NOT_VALIDATED'

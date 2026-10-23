"""Targeted real physical G_UU algebra and exact-Fraction interval sign gates."""
from fractions import Fraction as F
import sympy as sp
import pytest
from numerics import hr_step62_physical_G_curvature as m


def test_three_original_physical_modules_genuinely_byte_authentic():
    assert m.check_sources()==m.PINNED
    assert len(m.PINNED)==3


def test_exact_source_fail_closed_on_one_mutated_file(tmp_path,monkeypatch):
    for f in m.PINNED:
        (tmp_path/f).write_bytes((__import__('pathlib').Path(m.__file__).parent/f).read_bytes())
    (tmp_path/'hr_step46_exact_secondary_ode.py').write_text('malicious mutation\n')
    monkeypatch.setattr(m,'__file__',str(tmp_path/'new_step62.py'))
    with pytest.raises(ValueError,match='historical source mismatch'):
        m.check_sources()


def test_original_six_pair_G_exact_polynomial_degree_two():
    a=m.curvature_identity();assert a['polynomial_U_degree']==2
    assert sp.Poly(a['G'],a['U']).degree()==2


def test_exact_G_second_derivative_equals_closed_physical_expression():
    a=m.curvature_identity()
    assert sp.cancel(sp.together(sp.diff(a['G'],a['U'],2)-a['physical_formula']))==0


def test_physical_G_third_U_derivative_vanishes_identically():
    a=m.curvature_identity()
    assert sp.diff(a['G'],a['U'],3)==0


def test_G_UU_vanishes_at_center_and_is_U_independent():
    a=m.curvature_identity()
    assert a['guu'].subs(a['s'],0)==0
    assert sp.diff(a['guu'],a['U'])==0


def test_physical_G_U_at_center_is_exact_negative_Sfr_over_Lf():
    a=m.curvature_identity()
    assert sp.cancel(sp.diff(a['G'],a['U']).subs(a['s'],0)+
                     a['variables']['Sfr0']/a['variables']['Lf0'])==0


def test_original_benchmark_rational_interaction_and_T_strictly_positive():
    b=m.benchmark_rational_certificate()
    assert F(b['At'][0])>0 and F(b['numerator'][0])>0
    assert F(b['At'][1])>F(b['At'][0])
    assert F(b['numerator'][1])>F(b['numerator'][0])


def test_uniform_exact_fraction_curvature_between_zero_and_one():
    b=m.benchmark_rational_certificate()
    assert F(b['curvature'][0])==0
    assert 0<F(b['curvature'][1])<1
    assert F(b['curvature'][1])>F(3,5)
    assert b['s_interval']==('0','289/400')


def test_rational_sqrt_envelopes_genuinely_enclose_all_s():
    s=F('0.7225'); z1=F('.004'); kf=F('-.0016')
    lo=F(m.benchmark_rational_certificate()['sqrt1'][0])
    hi=F(m.benchmark_rational_certificate()['sqrt2'][1])
    assert lo**2<1-s*z1**2 and hi**2>1+s*kf**2


def test_symbolic_curvature_odd_in_f_dust_slope_at_fixed_geometry():
    a=m.curvature_identity();tf=a['variables']['tf0']
    # Due to sqrt(tf**2), reversing the f-dust phase slope reverses G_UU.
    assert sp.simplify(a['guu'].subs(tf,-tf)+a['guu'])==0


def test_vanishing_phase_slope_annihilates_quadratic_U_curvature():
    a=m.curvature_identity();tf=a['variables']['tf0']
    assert sp.simplify(a['guu'].subs(tf,0))==0


def test_fraction_interval_multiplication_handles_negative_and_zero():
    I=m.Interval
    a=I(-2,3);b=I(-5,-1)
    assert (a*b).bounds()==('-15','10')
    assert (a**2).bounds()==('0','9')
    assert (b**2).bounds()==('1','25')
    assert (I(1)/I(2,4)).bounds()==('1/4','1/2')


def test_fraction_interval_denominator_zero_rejected():
    with pytest.raises(ZeroDivisionError):_=m.Interval(1)/m.Interval(-1,1)


def test_physical_curvature_manifest_no_false_dirac_rank_claim():
    a=m.manifest()
    assert a['imported_actual_physical_G'] is True
    assert a['G_UUU_exact_zero'] is True
    assert a['physical_temporal_rank']=='NOT_COMPUTED'
    assert a['GATE_2B']=='OPEN' and a['JANUS_R']=='NOT_VALIDATED'


def test_exact_physical_G_U_tube_linearization_sensitivity():
    t=m.certified_tube_linearization()
    assert t['Gu_difference_strict']==F(337,5_000_000)
    assert t['curvature_upper_strict']==F(337,500)


def test_exact_quadratic_Taylor_remainder_on_Step55_U_tube():
    t=m.certified_tube_linearization()
    assert t['Taylor_quadratic_remainder_strict']==F(337,100_000_000_000)
    a=m.curvature_identity()
    # Symbolic equality, not a heuristic Taylor truncation:
    delta=sp.Symbol('delta')
    g=a['G'];u=a['U']
    remainder=sp.expand(g.subs(u,u+delta)-g-sp.diff(g,u)*delta)
    assert sp.cancel(sp.together(remainder-sp.diff(g,u,2)*delta**2/2))==0

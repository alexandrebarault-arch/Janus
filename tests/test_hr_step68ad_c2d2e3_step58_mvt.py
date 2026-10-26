"""Independent tests of conditional Step58 continuum sign enclosure.

No test equates lapse-coefficient signs with admissible positive lapse solutions.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch
import pytest
import sympy as sp
from numerics import hr_step68n_interval_ode_jets as jets
from numerics import hr_step68o_temporal_interval_annulus as annulus
from numerics.hr_step68ad_c2d2b_executed_temporal_probe import denominator_identity
from numerics.hr_step68ad_c2d2a_temporal_replay import verify_original_files
from numerics.hr_step68ad_c2b_center_boxes import load_pinned,certify_cells
from numerics.hr_step68ad_c2d2e3_step58_mvt import (
    I,old,fourth_jet_order,canonical_jets4,validated_s_jet,
    original_step58_duals,step58_value_derivative,mean_value_step58,
    certified_step58_continuum,factored_compiled)
from numerics.hr_step58_temporal_operator import physical_operator

ROOT=Path(__file__).resolve().parents[1]

@pytest.fixture(scope='module')
def reports():return load_pinned(ROOT/'research/reports')

@pytest.fixture(scope='module')
def compiled():return factored_compiled()[1]


def test_original_source_authentication(reports):
    assert len(verify_original_files(ROOT/'numerics'))==6
    assert len(annulus.verified_sources())==8
    assert len(annulus.certify_sources())==4
    assert certify_cells(reports)['cell_count']==7


def test_original_operator_really_uses_third_radial_jets():
    op=physical_operator()
    for name in ('N','M'):
        expr=op['operator'][name][0]
        assert any(expr.has(v) for v in op['qppp'])
        assert not any(expr.has(v) for v in op['q4'])


def test_fourth_derivative_chain_rule_exact():
    r=sp.symbols('r',real=True);x=sp.symbols('x');u=sp.Function('u');s=r*r
    expr=sp.diff(u(s),r,4)/24
    expect=(sp.S.Half*sp.diff(u(x),x,2)
            +2*r*r*sp.diff(u(x),x,3)
            +sp.Rational(2,3)*r**4*sp.diff(u(x),x,4)).subs(x,s)
    assert sp.simplify(expr-expect)==0


def test_fourth_ode_coefficient_recurrence_exact():
    t=sp.symbols('t');a,b,c,d,e=sp.symbols('a b c d e')
    U=a+b*t+c*t**2+d*t**3+e*t**4
    G=2*U+2*t*sp.diff(U,t)
    rhs=(G-2*U)/(2*t)
    assert sp.expand(rhs).coeff(t,3)/4==e


def test_jet_order_scope_restored():
    assert jets.K==3
    with fourth_jet_order():assert jets.K==4
    assert jets.K==3
    with pytest.raises(RuntimeError):
        with fourth_jet_order():raise RuntimeError('test')
    assert jets.K==3


@pytest.mark.parametrize('r',[F(1,64),F(1,48),F(1,32)])
def test_exact_48_original_lower_jet_coefficients(r,reports):
    with fourth_jet_order():
        canonical,uj,box=canonical_jets4(r,r,reports)
        with patch.object(annulus,'_ode_coeff',lambda si:validated_s_jet(box,jets.Jet,I)):
            original,_,_,_=annulus.canonical_jets_cell(r,r)
        assert set(canonical)==set(original)
        for name in canonical:
            for j in range(4):
                a,b=canonical[name].a[j],original[name].a[j]
                assert (a.lo,a.hi)==(b.lo,b.hi)
        assert uj.a[4].lo<=uj.a[4].hi


def test_original_cse_shell_identity(compiled):
    op=physical_operator()
    for name in ('N','M'):
        *_,idx,alt=denominator_identity(op,name)
        assert idx in (75,79)
        assert alt is not None


@pytest.mark.parametrize('r',[F(1,64),F(1,32)])
def test_original_step58_pointwise_agrees_with_dual_values(r,reports,compiled):
    with fourth_jet_order():
        _,_,box=canonical_jets4(r,r,reports)
        with patch.object(annulus,'_ode_coeff',lambda si:validated_s_jet(box,jets.Jet,I)):
            original=annulus.evaluate_cell(r,r)
    dual=step58_value_derivative(r,r,reports,compiled)
    for label in ('N','M'):
        x=original[label];y=dual[label].v
        assert max(x.lo,y.lo)<=min(x.hi,y.hi)
        assert abs((x.lo+x.hi)-(y.lo+y.hi))<10**13


def test_original_step58_dual_includes_qrrr_derivatives(reports):
    vals,_,_,_=original_step58_duals(F(1,64),F(1,64),reports)
    op=physical_operator()
    assert any(vals[v].d.lo!=0 or vals[v].d.hi!=0 for v in op['qppp'])


def test_coarse_first_subcell_is_incomplete_not_false_positive(reports,compiled):
    a=F(1,64);b=F(1,56);hi=a+(b-a)/32
    x=mean_value_step58(a,hi,reports,compiled)
    assert x['N']['mean_value'].lo<=0
    assert x['M']['mean_value'].hi<0


def test_adaptive_first_subcell_both_signs(reports,compiled):
    a=F(1,64);b=F(1,56);hi=a+(b-a)/32;mid=(a+hi)/2
    for lo,end in ((a,mid),(mid,hi)):
        x=mean_value_step58(lo,end,reports,compiled)
        assert x['N']['mean_value'].lo>0
        assert x['M']['mean_value'].hi<0


def test_reject_radius_outside_certified_chart(reports):
    with pytest.raises(ValueError):canonical_jets4(F(0),F(1,64),reports)
    with pytest.raises(ValueError):canonical_jets4(F(1,64),F(1,16),reports)


def test_tampered_report_is_rejected(tmp_path):
    src=ROOT/'research/reports'
    for name in ('gate2b-step68v-global-monotone-radial-U.json',
                 'gate2b-step68ac-authentic-U4-report.json',
                 'gate2b-step68ad-B2-original-G-Uss-Usss.json'):
        (tmp_path/name).write_bytes((src/name).read_bytes())
    name='gate2b-step68ac-authentic-U4-report.json'
    (tmp_path/name).write_bytes((tmp_path/name).read_bytes()+b' ')
    with pytest.raises(ValueError):load_pinned(tmp_path)


def test_tampered_original_step58_is_rejected(tmp_path):
    for name in verify_original_files(ROOT/'numerics'):
        (tmp_path/name).write_bytes((ROOT/'numerics'/name).read_bytes())
    name='hr_step58_temporal_operator.py'
    (tmp_path/name).write_bytes((tmp_path/name).read_bytes()+b'# tampered\n')
    with pytest.raises(ValueError):verify_original_files(tmp_path)


def test_full_225_rational_continuum_certification(reports):
    result=certified_step58_continuum(reports)
    published=json.loads((ROOT/'research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json').read_text())
    assert result==published
    assert result['total_leaves']==225
    assert result['adaptive_bisections']==1
    assert [len(c['leaves']) for c in result['cells']]==[33,32,32,32,32,32,32]
    assert F(result['min_N_lower'])>0
    assert F(result['max_M_upper'])<0
    for c in result['cells']:
        for leaf in c['leaves']:
            assert F(leaf['N'][0])>0 and F(leaf['M'][1])<0
    assert result['GATE_2B']=='OPEN'
    assert result['JANUS_R']=='NOT_VALIDATED'

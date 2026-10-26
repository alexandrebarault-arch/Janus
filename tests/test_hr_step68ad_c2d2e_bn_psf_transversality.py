"""Independent tests of Step60 BN/pSf conditional transversality."""
from fractions import Fraction as F
import sympy as sp
import pytest
from numerics.hr_step68ad_c2d2e_bn_psf_transversality import (
    original_bn_affine,compiled_slope,slope_dual,mean_value_slope,certify)
from numerics.hr_step68ad_c2b_center_boxes import load_pinned
from numerics.hr_step68ad_c2d2c_step60_lower_quotient_replay import evaluate_lower_quotient

@pytest.fixture(scope='module')
def reports():return load_pinned('research/reports')

def test_original_exact_affinity():
    x,p,j=original_bn_affine()
    assert sp.diff(x,p,2)==0
    assert not j.has(p)
    assert sp.simplify(sp.diff(x,p)-j)==0

def test_original_source_provenance(reports):
    from numerics.hr_step60_full_constraint_prolongation import verified_original_sources
    from numerics.hr_step68ad_c2b_center_boxes import certify_cells
    assert verified_original_sources()['hr_step58_temporal_operator.py']=='802c23aebd41780d8c462f1aa1711707fe4ee88f'
    assert certify_cells(reports)['pinned_original_report_git_blobs']['B2']=='ac961b5b83667a83497497d22a701c24584cb561'

def test_compiled_original_slope():
    syms,fn=compiled_slope()
    assert len(syms)>0 and callable(fn)
    assert 'pSf' not in [str(s) for s in syms]

@pytest.mark.parametrize('r',[F(1,64),F(1,48),F(1,32)])
def test_pointwise_slope_negative(r,reports):
    v=slope_dual(r,r,reports)
    assert v.v.hi<0

@pytest.mark.parametrize('a,b',[(F(1,64),F(1,64)+F(1,100000)),
    (F(1,48),F(1,48)+F(1,100000)),(F(1,32)-F(1,100000),F(1,32))])
def test_mean_value_slope_strict_negative(a,b,reports):
    v=mean_value_slope(a,b,reports)
    assert v['mean_value'].hi<0

def test_full_seven_cell_certificate(reports):
    r=certify(reports,32)
    assert r['subcells']==224 and r['original_cells']==7
    assert r['J_strictly_negative_continuum']
    assert F(r['max_J_upper'])<0
    assert r['BN_zero_on_shell']=='NOT_PROVED'
    for row in r['cells']:
        for leaf in row['leaves']:
            assert F(leaf['J'][1])<0

def test_reject_invalid_domain(reports):
    with pytest.raises(ValueError):slope_dual(F(0),F(1,64),reports)
    with pytest.raises(ValueError):mean_value_slope(F(1,48),F(1,48),reports)
    with pytest.raises(ValueError):certify(reports,0)

def test_bn_enclosure_is_not_a_sign_certificate(reports):
    v=evaluate_lower_quotient(F(1,48),F(1,48),reports)['BN']
    assert F(v['enclosure'][0])<0<F(v['enclosure'][1])

def test_independent_original_bn_psf_perturbation(reports):
    from numerics.hr_step68ad_c2d2c_step60_lower_quotient_replay import (
        canonical_symbol_values,compiled_lower_quotient)
    from numerics.hr_step68ad_c2d2a_temporal_replay import (
        box_for_rounded_s,inject_s_jet)
    from numerics.hr_step68ad_c2b_center_boxes import Q,validate_reports
    from numerics.hr_step68n_interval_ode_jets import I,Jet
    from numerics import hr_step68o_temporal_interval_annulus as annulus
    r=F(1,48);si=I.hull(r,r)**2
    box=box_for_rounded_s(reports,si,{'r':[str(r),str(r)]},Q,validate_reports)
    with inject_s_jet(annulus,box,Jet,I,si):
        vals=canonical_symbol_values(r,r)
    syms,fn=compiled_lower_quotient()['BN']
    psf=next(s for s in syms if str(s)=='pSf')
    original=I.c(fn(*[vals[s] for s in syms])[0])
    vals[psf]=vals[psf]+I.c(F(1,10000))
    shifted=I.c(fn(*[vals[s] for s in syms])[0])
    slope=slope_dual(r,r,reports).v
    # Original BN is exactly affine in pSf. Both independently computed
    # interval values must contain the expected finite-difference effect.
    delta=I.c(F(1,10000))*slope
    observed=shifted-original
    assert max(delta.lo,observed.lo)<=min(delta.hi,observed.hi)
    assert shifted.hi<0

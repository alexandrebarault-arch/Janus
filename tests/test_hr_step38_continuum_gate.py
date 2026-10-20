"""Standalone Step38 exact-rational and stored-data error-control tests."""
import json
from decimal import Decimal as D
from fractions import Fraction as F
import pytest
from numerics.hr_step38_continuum_gate import (
    A,B,CF,CG,Y,RMAX,J,eta_at_s,K_over_r2_at_s,
    continuous_sign_certificate,read_step37_report,richardson,gate_manifest)


def test_spatial_geometry_exact_analytic_monotonicity():
    s=RMAX**2
    assert CF-CG<0
    assert 1+CF*s>0
    assert eta_at_s(s)<eta_at_s(F(0))==Y
    assert J(eta_at_s(s))>F('0.6')


def test_continuous_spatial_J_and_K_lower_bounds_by_exact_inequalities():
    proof=continuous_sign_certificate()
    assert F(proof['J_exact_lower'])>F('0.6')
    assert F(proof['K_over_r2_exact_lower'])>0
    for r in (F(0),F('.05'),F('.11'),F('.4'),F('.85')):
        assert J(eta_at_s(r*r))>=F(proof['J_exact_lower'])
        assert K_over_r2_at_s(r*r)>=F(proof['K_over_r2_exact_lower'])


def test_spherical_center_is_coordinate_zero_not_positive_K_at_origin():
    lower=F(continuous_sign_certificate()['K_over_r2_exact_lower'])
    assert lower>0
    assert 0**2*K_over_r2_at_s(F(0))==0
    assert F('.01')**2*K_over_r2_at_s(F('.01')**2)>0


def test_rational_certificate_domain_guard():
    for s in (F(-1),RMAX**2+F('0.0001')):
        with pytest.raises(ValueError):eta_at_s(s)


def test_four_step37_report_nodes_are_dyadically_nested():
    data=read_step37_report()
    assert [row['n'] for row in data]==[81,161,321,641]
    assert data[-1]['after']<0


def test_richardson_corrected_has_positive_plateau_not_zero():
    d=richardson(read_step37_report())
    values=[D(s) for s in d['second_Oh4']]
    assert len(values)==2
    assert D('5.3e-9')<values[-1]<D('5.5e-9')
    assert abs(values[1]-values[0])<D('2e-13')
    assert d['rigorous_bound'] is False


def test_richardson_uncorrected_retains_large_positive_bracket():
    d=richardson(read_step37_report(),channel='before')
    assert D('.00938')<D(d['last_estimate'])<D('.0094')
    assert d['rigorous_bound'] is False


def test_observed_second_order_difference_scaling():
    data=read_step37_report()
    rates=richardson(data)['successive_difference_ratios']
    assert len(rates)==2
    assert all(3.9<rate<4.1 for rate in rates)


def test_wrong_nesting_is_rejected():
    src=read_step37_report()
    wrong=[dict(v) for v in src]
    wrong[2]['n']=320
    with pytest.raises(ValueError,match='dyadically'):
        richardson(wrong)


def test_wrong_channel_is_rejected():
    with pytest.raises(ValueError):richardson(read_step37_report(),channel='speed')


def test_manifest_explicitly_keeps_physics_open():
    d=gate_manifest()
    assert d['GATE_2B']=='OPEN'
    assert d['Dirac_secondary_preservation']=='NOT_DERIVED'
    assert d['continuous_C_local_zero']=='NOT_PROVED'
    assert d['JANUS_R']=='NOT_VALIDATED'

"""Step68ad-B2: real SHA-original six-pair physical continuum certificate tests."""
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
import pytest
from numerics import hr_step55_global_barrier as old
from numerics.hr_step45_exact_physical_ward import exact_physical_ward
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
from numerics.hr_step68ad_b_directional_polarization import (
    physical_G_partials,physical_R2_global,source_R2,source_R3)
from numerics.hr_step68ad_b2_physical_center_higher_jets import (
    certify,preflight,exact_quadratic_G_certificate)
from numerics.hr_step68ad_center_derivative_transport import load_physical_reports

ROOT=Path(__file__).resolve().parents[1]
REPORTS=ROOT/'research'/'reports'

@pytest.fixture(scope='module')
def c32():return certify(REPORTS,32)

@pytest.fixture(scope='module')
def c64():return certify(REPORTS,64)


def test_six_original_physical_sources_and_two_operators_authenticated():
    p=preflight()
    assert len(p)==7
    assert p['hr_step55_global_barrier.py']=='a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
    assert p['hr_step68n_interval_ode_jets.py']=='96370e0599748c6dc07faf339ab3646ae3474e7d'


def test_two_historical_input_reports_sha_authenticated():
    d=load_physical_reports(REPORTS)
    assert d['68v']['center_s_range']==['0','1/64']
    assert d['68ac']['U4_sign_strict_negative'] is True


def test_original_six_pair_ward_and_secondary_symbolic_checks():
    assert all(x==0 for x in exact_physical_ward()['residuals'].values())
    assert all(x==0 for x in exact_f_momentum_ode()['identity_residuals'].values())


def test_original_G_exact_quadratic_and_positive_curvature():
    d=exact_quadratic_G_certificate()
    assert d['original_G_polynomial_degree_U_exact']==2
    assert d['G_UUU_identically_zero']
    assert d['G_UU_equals_s_times_C_exact']
    lo,hi=map(F,d['C_full_domain_outward_interval'])
    assert F('0.875')<lo<=hi<F('0.877')


def test_original_physical_center_partial_derivatives():
    p=physical_G_partials(old.I.c(0),old.U0)
    assert p['G_U'].lo<=-old.S<=p['G_U'].hi
    assert p['G_UU'].lo<=0<=p['G_UU'].hi
    assert p['G_UUU'].lo<=0<=p['G_UUU'].hi


def test_original_R2_center_matches_14U2():
    p=physical_G_partials(old.I.c(0),old.U0)
    r2=source_R2(p,old.U1)
    target=14*old.U2
    assert r2.lo<=target.lo<=target.hi<=r2.hi


def test_original_R3_center_contains_54U3():
    p=physical_G_partials(old.I.c(0),old.U0)
    r3=source_R3(p,old.U1,2*old.U2)
    ac=load_physical_reports(REPORTS)['68ac']
    a,b=map(F,ac['original_Step67b_U3_interval'])
    # Independent valid enclosures need overlap, not full containment.
    assert max(F(r3.lo,old.S),54*a)<=min(F(r3.hi,old.S),54*b)


def test_R2_and_Uss_negative_full_continuum(c32):
    assert F(c32['R2_global'][1])<0
    assert F(c32['U_ss_global'][1])<0
    assert F(c32['a2_global'][0])>0


def test_R3_and_Usss_negative_full_continuum(c32):
    assert F(c32['R3_global'][1])<0
    assert F(c32['U_sss_global'][1])<0
    assert F(c32['a3_global'][0])>0


def test_center_coefficient_inclusions(c32):
    assert c32['center_U_ss_2U2_included']
    assert c32['center_U_sss_6U3_included']


def test_all_closed_cells_cover_center_to_one_over_1024(c32):
    assert len(c32['R2_cells'])==len(c32['R3_cells'])==32
    assert c32['R2_cells'][0]['s_lo']==c32['R3_cells'][0]['s'][0]=='0'
    assert c32['R2_cells'][-1]['s_hi']==c32['R3_cells'][-1]['s'][1]=='1/1024'
    for i in range(32):
        assert c32['R2_cells'][i]['s_lo']==c32['R3_cells'][i]['s'][0]
        assert c32['R2_cells'][i]['s_hi']==c32['R3_cells'][i]['s'][1]
        if i:assert c32['R3_cells'][i-1]['s'][1]==c32['R3_cells'][i]['s'][0]


def test_64_cells_refine_32_cells_without_sign_reversal(c32,c64):
    assert c64['cells']==64
    for key in ('R2_global','R3_global','U_ss_global','U_sss_global'):
        a,b=map(F,c32[key]);c,d=map(F,c64[key])
        assert a<=c<=d<=b,(key,a,b,c,d)


def test_machine_report_equals_real_executed_certificate(c32):
    report=json.loads((REPORTS/'gate2b-step68ad-B2-original-G-Uss-Usss.json').read_text())
    assert report==c32


def test_invalid_cell_counts_fail_closed():
    for count in (0,7,2049):
        with pytest.raises(ValueError,match='cells'):
            certify(REPORTS,count)


def test_corrupt_historical_report_rejected(tmp_path):
    for filename in ('gate2b-step68v-global-monotone-radial-U.json',
                     'gate2b-step68ac-authentic-U4-report.json'):
        (tmp_path/filename).write_bytes((REPORTS/filename).read_bytes())
    p=tmp_path/'gate2b-step68v-global-monotone-radial-U.json'
    p.write_bytes(p.read_bytes()+b' ')
    with pytest.raises(ValueError,match='Git blob mismatch'):
        load_physical_reports(tmp_path)


def test_no_temporal_or_4D_claim(c32):
    assert c32['temporal_Step58_A_N_A_M']=='NOT_COMPUTED'
    assert c32['full_Dirac_rank']=='NOT_COMPUTED'
    assert c32['GATE_2B']=='OPEN' and c32['JANUS_R']=='NOT_VALIDATED'

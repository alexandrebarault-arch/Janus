"""Step68ac SHA-authentic ORIGINAL HR U4 coefficient and fail-closed checks."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha1
import json
import pytest
import sympy as sp
from numerics.hr_step68ac_authentic_original_U4 import (
    actual_U4, preflight, exact_GU_center_identity, original_jet_order4,
    EXTRA_BLOBS, as_frac)
from numerics import hr_step68n_interval_ode_jets as j
from numerics import hr_step55_global_barrier as original
from numerics.hr_step55_normalized_secondary import normalized_symbolic
from numerics.hr_step45_exact_physical_ward import exact_physical_ward
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
from numerics.hr_step68aa_canonical_center_radial_jets import authenticated_inputs

ROOT=Path(__file__).resolve().parents[1]
REPORTS=ROOT/'research'/'reports'


@pytest.fixture(scope='module')
def result():
    return actual_U4(REPORTS)


def test_all_six_original_python_sources_byte_authentic():
    proof=preflight()
    assert len(proof)==6
    assert proof['hr_step55_global_barrier.py']=='a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
    assert proof['hr_step68n_interval_ode_jets.py']==EXTRA_BLOBS['hr_step68n_interval_ode_jets.py']


def test_original_six_pair_ward_nine_exact_residuals():
    d=exact_physical_ward()
    assert len(d['Q'])==12
    assert len(d['residuals'])==9
    assert all(x==0 for x in d['residuals'].values())


def test_original_step46_affine_secondary_identification():
    d=exact_f_momentum_ode()
    assert len(d['identity_residuals'])==5
    assert all(x==0 for x in d['identity_residuals'].values())


def test_original_normalized_G_is_actual_symbolic():
    e,s,u,v=normalized_symbolic()
    assert e.has(u) and e.has(s)
    assert sp.count_ops(e)>1000


def test_exact_symbolic_GU_center_negative_one():
    d=exact_GU_center_identity()
    assert d['center_GU0_exact']=='-1'
    assert d['U4_divisor_exact']=='11'


def test_sequential_real_G_u1_u2_are_contained(result):
    rows=result['raw_sequential_recurrence']
    for index,name in [(0,'original_U1_interval'),(1,'original_U2_interval')]:
        a,b=map(F,rows[index]['U_n'])
        c,d=map(F,result[name])
        assert a<=c<=d<=b
    assert [r['divisor_exact'] for r in rows]==['5','7','9','11']


def test_original_U3_overlap_with_step67b(result):
    a,b=map(F,result['raw_sequential_recurrence'][2]['U_n'])
    c,d=map(F,result['original_Step67b_U3_interval'])
    assert max(a,c)<=min(b,d)<0
    assert c<=d


def test_rigorous_negative_U4_and_width(result):
    a,b=map(F,result['intersection_certified_U4'])
    assert a<=b<0
    assert b-a<F(1,10**21)
    assert -F(4,10**10)<a<b<-F(3,10**10)
    original_interval=list(map(F,result['pinned_input_U4_enclosure']))
    assert original_interval[0]<=a<=b<=original_interval[1]
    sequential=list(map(F,result['raw_sequential_recurrence'][3]['U_n']))
    assert sequential[0]<=a<=b<=sequential[1]


def test_original_ODE_rational_interval_coefficients_contain_zero(result):
    assert len(result['original_ODE_coefficient_residuals_contain_zero'])==5
    assert all(F(a)<=0<=F(b)
        for a,b in result['original_ODE_coefficient_residuals_contain_zero'])


def test_physical_f_momentum_r10_coefficient_and_scope(result):
    assert result['genuine_canonical_pLf_r10_coefficient_is_U4'] is True
    assert result['temporal_Step58_AN_AM']=='NOT_COMPUTED'
    assert result['full_Dirac_rank']=='NOT_COMPUTED'
    assert result['continuous_r_0_to_1over32_higher_jet_enclosures']=='NOT_COMPUTED'
    assert result['GATE_2B']=='OPEN' and result['JANUS_R']=='NOT_VALIDATED'


def test_original_jet_order_restored_after_exception():
    assert j.K==3
    with pytest.raises(RuntimeError,match='simulated'):
        with original_jet_order4():
            assert j.K==4
            raise RuntimeError('simulated')
    assert j.K==3


def test_fail_on_perturbed_original_jet_order():
    baseline=j.K
    try:
        j.K=5
        with pytest.raises(RuntimeError,match='K unexpectedly changed'):
            with original_jet_order4():pass
    finally:
        j.K=baseline
    assert j.K==3


def test_original_jet_src_drift_fails_closed(tmp_path):
    paths=['hr_step45_exact_physical_ward.py','hr_step46_exact_secondary_ode.py',
        'hr_step55_normalized_secondary.py','hr_step55_global_barrier.py',
        'hr_step68l_refined_global_barrier.py','hr_step68n_interval_ode_jets.py']
    import shutil
    for path in paths:shutil.copy(ROOT/'numerics'/path,tmp_path/path)
    p=tmp_path/'hr_step68n_interval_ode_jets.py'
    p.write_bytes(p.read_bytes()+b'\n#tamper\n')
    with pytest.raises(ValueError,match='source drift'):preflight(tmp_path)


def test_step55_original_spatial_global_256_cells():
    d=original.certify_global_barrier(cells=256)
    assert d['cells']==256 and d['Step54_positive_two_dust_and_JK_signs_apply'] is True
    assert d['Dirac_secondary_time_preservation']=='NOT_COMPUTED'


def test_machine_json_exact_and_original_68aa_crosscheck(result):
    expected=json.loads((REPORTS/'gate2b-step68ac-authentic-U4-report.json').read_text())
    assert result==expected
    assert result['source_68aa_U3_verified'] is True
    assert tuple(result['original_Step67b_U3_interval'])==tuple(map(str,authenticated_inputs(REPORTS)))

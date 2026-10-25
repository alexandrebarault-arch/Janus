"""Targeted simultaneous regression of authentic original Steps45-60 and physical point profile.

These tests certify byte provenance, original historical symbolic/interval
proofs, and *numerical* low-lapse exploratory values only. No Dirac rank proof.
"""
import pathlib
import hashlib
import mpmath as mp
import sympy as sp
import pytest
from numerics.hr_step68f_physical_pointwise import PINS,verified_sources,local_point,evaluate_report
from numerics.hr_step45_exact_physical_ward import exact_certificate_summary,exact_physical_ward
from numerics.hr_step46_exact_secondary_ode import exact_ode_certificate
from numerics.hr_step55_global_barrier import certify_global_barrier
from numerics.hr_step57_secondary_principal_symbol import physical_principal_symbol
from numerics.hr_step58_temporal_operator import physical_operator, highest_lapse_certificate
from numerics.hr_step59_third_jet_gate import third_jet_certificate
from numerics.hr_step60_full_constraint_prolongation import full_constraint_prolongation,verified_original_sources

@pytest.fixture(scope='module')
def joint():
    return (exact_certificate_summary(),exact_ode_certificate(),
            certify_global_barrier(cells=256),physical_principal_symbol(),
            highest_lapse_certificate(),third_jet_certificate(),
            full_constraint_prolongation())

def test_eight_actual_historical_git_blobs_match(joint):
    assert verified_sources()==PINS and len(PINS)==8
    assert len(verified_original_sources())==4

def test_hash_mutation_must_fail(tmp_path,monkeypatch):
    import numerics.hr_step68f_physical_pointwise as m
    old=m.__file__
    src=pathlib.Path(old).parent
    fake=tmp_path/'numerics';fake.mkdir()
    for n in PINS:(fake/n).write_bytes((src/n).read_bytes())
    with (fake/'hr_step58_temporal_operator.py').open('ab') as f:f.write(b'\n# tamper\n')
    monkeypatch.setattr(m,'__file__',str(fake/'hr_step68f_physical_pointwise.py'))
    with pytest.raises(ValueError,match='byte-source mismatch'):m.verified_sources()

def test_original_Ward_and_radial_affine(joint):
    assert joint[0]['exact_symbolic_residuals_all_zero']
    assert joint[1]['symbolic_C_affine_in_pLf_prime']=='EXACT'

def test_original_256_cell_integer_barrier_reexecuted(joint):
    c=joint[2]
    assert c['cells']==256
    assert mp.mpf(c['strict_max_Fupper_rational'].split('/')[0])<0
    assert mp.mpf(c['strict_min_Flower_rational'].split('/')[0])>0

def test_original_full_temporal_shift_and_prolongation(joint):
    assert joint[4]['N2_and_M2_vanish_on_Fz_and_Hg']
    assert joint[6]['derivative_residuals']['BN']=={'Sg':0}
    assert joint[6]['derivative_residuals']['AM']=={'pLg':0,'Sg':0,'tg':0}

@pytest.mark.parametrize('radius',('0.2','0.4','0.6','0.8'))
def test_exploratory_physical_coefficient_scan(radius,joint):
    report=evaluate_report(radius)
    for c in ('Fz','Hg','Hf','C'):
        assert abs(report[c])<1e-11
    A=report['raw_temporal_coefficients']
    assert A['N']['0']>0 and A['M']['0']<0
    ratio=-A['N']['0']/A['M']['0']
    assert 0.51<ratio<0.53
    for k in ('N','M'):
        assert abs(A[k]['1'])<1e-10
        assert abs(A[k]['2'])<1e-10

@pytest.mark.parametrize('offset',('0.00001','-0.00001'))
def test_physical_point_stable_in_certified_tube(offset,joint):
    x=evaluate_report('0.4',offset)
    assert abs(x['C'])<1e-11
    assert 0.51<-x['raw_temporal_coefficients']['N']['0']/x['raw_temporal_coefficients']['M']['0']<0.53


def test_off_primary_pSf_change_breaks_secondary(joint):
    data=local_point('0.4');p=exact_physical_ward()
    syms=data['symbols']; vv=list(map(float,data['values']))
    bad=sp.lambdify(syms,p['C_exact'],'numpy',cse=True)
    initial=bad(*vv)
    vv[syms.index(p['q'][9])]+=0.001
    assert abs(initial)<1e-11 and abs(bad(*vv))>0.1


def test_no_globally_certified_rank_claim(joint):
    # Four nonzero lapse derivative-free coefficient values are an exploratory
    # *pointwise* diagnostic; alone they cannot establish global rank/ghost-freedom.
    assert joint[2]['Dirac_secondary_time_preservation']=='NOT_COMPUTED'
    assert joint[4]['N2_and_M2_vanish_on_Fz_and_Hg']

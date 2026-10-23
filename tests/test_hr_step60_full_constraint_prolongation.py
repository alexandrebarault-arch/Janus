"""Step60 real six-pair constraint prolongation: exact quotient, not rank."""
import pathlib
import shutil
import sympy as sp
import pytest
from numerics.hr_step60_full_constraint_prolongation import (
    full_constraint_prolongation,verified_original_sources,EXPECTED,manifest)
from numerics.hr_step58_temporal_operator import physical_operator
from numerics.hr_step57_secondary_principal_symbol import authenticated_step45
from numerics.hr_step59_third_jet_gate import constraint_prolongation_principal

@pytest.fixture(scope='module')
def cert():
    return full_constraint_prolongation()


def test_four_original_sixpair_source_blobs_verified():
    assert verified_original_sources()==EXPECTED and len(EXPECTED)==4
    assert len(authenticated_step45()['Q'])==12


def test_fail_closed_on_a_mutated_original_provider(tmp_path,monkeypatch):
    import numerics.hr_step60_full_constraint_prolongation as module
    # Keep test isolated; prove the fail-closed hash interface works.
    b=tmp_path/'fake.py'
    b.write_text('fake source mutation\n')
    for f in EXPECTED:
        (tmp_path/f).write_bytes(pathlib.Path(module.__file__).with_name(f).read_bytes())
    (tmp_path/'hr_step45_exact_physical_ward.py').write_bytes(b.read_bytes())
    monkeypatch.setattr(module,'__file__',str(tmp_path/'cert.py'))
    with pytest.raises(ValueError,match='Original physical dependency changed'):
        module.verified_original_sources()


def test_exact_Cred_prime_contains_stationary_shift_second_jet(cert):
    p=authenticated_step45();v=physical_operator()
    assert not v['C'].has(*v['qpp'])
    assert v['Czr']!=0
    assert not cert['C_red_prime'].has(v['zrr'])
    assert any(cert['C_red_prime'].has(j) for j in v['qppp'])


def test_shift_zprime_and_zdoubleprime_are_prolonged_not_frozen(cert):
    v=physical_operator()
    assert not any(cert['first_shift_zprime'].has(j) for j in v['qppp'])
    assert all(cert['second_shift_zdoubleprime'].has(v['qppp'][i])
               for i in (1,2,4)) # pLg,Sg,tg
    assert not cert['second_shift_zdoubleprime'].has(v['zrr'])


def test_zdoubleprime_has_exact_three_third_jet_coefficients(cert):
    p=authenticated_step45();v=physical_operator()
    q=dict(zip(p['Q'],p['q']));z=v['z'];R=sp.sqrt(1-z*z)
    ZD=R**3/v['K']
    for i,factor in ((1,-q['Lg']),(2,q['pSg']),(4,q['pg'])):
        assert sp.cancel(sp.diff(cert['second_shift_zdoubleprime'],v['qppp'][i])-ZD*factor)==0


def test_complete_primary_derivative_subtraction_removes_ALL_BN_third_jets(cert):
    for v in cert['derivative_residuals']['BN'].values(): assert v==0
    assert cert['derivative_residuals']['BN']=={'Sg':0}
    assert all(not cert['third_free_BN_on_Fz'].has(j) for j in cert['all_third_jets'].values())


def test_complete_secondary_derivative_subtraction_removes_ALL_AM_third_jets(cert):
    assert cert['derivative_residuals']['AM']=={'pLg':0,'Sg':0,'tg':0}
    assert all(not cert['third_free_AM_on_Fz'].has(j) for j in cert['all_third_jets'].values())


def test_original_unreduced_coefficient_has_nonzero_third_field_sensitivities(cert):
    v=physical_operator();p=authenticated_step45();q=dict(zip(p['Q'],p['q']))
    assert cert['original_BN'].has(v['qppp'][2])
    assert cert['original_AM'].has(v['qppp'][1])
    assert cert['original_AM'].has(v['qppp'][2])
    assert cert['original_AM'].has(v['qppp'][4])
    assert cert['alpha_Hgprime']!=0 and cert['beta_Credprime']!=0


def test_wrong_primary_constraint_subtraction_exposes_nonzero_obstruction(cert):
    p=authenticated_step45();v=physical_operator()
    q=dict(zip(p['Q'],p['q']));z=v['z'];j=v['qppp'][2]
    raw=cert['original_BN']-cert['alpha_Hgprime']*cert['Hg_prime']
    val=sp.factor(sp.diff(raw,j).subs(cert['stationarity_substitution']))
    expected=-4*p['parameters'][0]*q['Sg']*(1-z*z)/(q['Lf']*q['Lg']**2)
    assert sp.cancel(val-expected)==0 and val!=0


def test_frozen_zdoubleprime_exposes_nonzero_secondary_obstruction(cert):
    p=authenticated_step45();v=physical_operator()
    q=dict(zip(p['Q'],p['q']));z=v['z'];j=v['qppp'][1]
    # Incorrectly freeze z''=0 in C_red'; the pLg''' coefficient
    # in A_M should then survive even after the fake subtraction.
    fake=cert['original_AM']-cert['beta_Credprime']*v['Dt'](v['C']).subs(v['zrr'],0)
    value=sp.factor(sp.diff(fake,j).subs(cert['stationarity_substitution']))
    expected=z*(1-z*z)/q['Lf']**2
    assert sp.cancel(value-expected)==0 and value!=0


def test_step59_only_principal_vs_step60_full_subtraction(cert):
    old=constraint_prolongation_principal()
    assert old['exact_scope'].startswith('ONLY third')
    assert cert['raw_BN_remainder']!=0 and cert['raw_AM_remainder']!=0
    assert cert['derivative_residuals']['BN']=={'Sg':0}


def test_manifest_candidly_preserves_open_rank_and_lapse_question():
    r=manifest()
    assert r['Dirac_rank']=='NOT COMPUTED'
    assert r['lapse_fixing']=='NOT COMPUTED'
    assert r['GATE_2B']=='OPEN' and r['JANUS_R']=='NOT_VALIDATED'
    assert r['full_lower_jet_constraint_quotient']=='NOT COMPLETED'

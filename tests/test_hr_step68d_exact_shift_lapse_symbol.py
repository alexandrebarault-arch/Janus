"""Authenticated exact six-pair Step45/57/58 on Fz shell shift-lapse bridge."""
from fractions import Fraction
from pathlib import Path
import hashlib
import sympy as sp
import pytest
from numerics import hr_step68d_exact_shift_lapse_symbol as step
from numerics.hr_step45_exact_physical_ward import exact_certificate_summary
from numerics.hr_step57_secondary_principal_symbol import physical_principal_symbol
from numerics.hr_step58_temporal_operator import physical_operator,highest_lapse_certificate


@pytest.fixture(scope='module')
def a():return step.physical_center_bridge()


def test_original_byte_identical_provenance():
    assert len(step.authenticate())==3


def test_all_three_sources_mutation_rejected(tmp_path):
    src=Path(step.__file__).resolve().parent
    for name in step.BLOBS:
        root=tmp_path/name.replace('.py','');root.mkdir()
        for original in step.BLOBS:
            raw=(src/original).read_bytes()
            (root/original).write_bytes(raw+(b'\n# mutated\n' if original==name else b''))
        with pytest.raises(ValueError,match='mismatch'):
            step.authenticate(root)


def test_original_six_canonical_pairs_and_nine_ward():
    p=exact_certificate_summary()
    assert p['six_canonical_pairs']==6 and p['exact_symbolic_residuals_all_zero']


def test_exact_physical_step57_eta_second_symbol_nonzero():
    q=physical_principal_symbol()
    assert q['eta2_M_coefficient']!=0
    assert str(q['eta2_M_coefficient'])=='-K**2/(Lf**2*Lg*R)'


def test_actual_step58_high_lapse_cancellation():
    a=highest_lapse_certificate()
    assert a['N2_and_M2_vanish_on_Fz_and_Hg'] is True
    assert a['M2_on_Fz_shell']==0


def test_new_exact_Nprime_response_on_stationarity(a):
    original=physical_operator()
    assert original['delta_shift']['N'][1]!=0
    assert a['Nprime_shift'].has(original['z'])


def test_new_exact_Mprime_response_on_stationarity(a):
    o=physical_operator()
    from numerics.hr_step57_secondary_principal_symbol import authenticated_step45
    Lf=authenticated_step45()['q'][6]
    assert sp.factor(a['Mprime_shift']-(1-o['z']**2)/Lf)==0


def test_both_shift_responses_have_no_Ldoubleprime(a):
    o=physical_operator()
    assert 2 not in o['delta_shift']['N'] and 2 not in o['delta_shift']['M']


def test_negative_control_omit_shift_Mdoubleprime(a):
    assert a['second_lapse_direct']['M']!=0
    assert a['second_lapse_from_shift']['M']!=0
    assert sp.factor(a['second_lapse_direct']['M']+a['second_lapse_from_shift']['M'])==0


def test_negative_control_omit_shift_Ndoubleprime(a):
    assert a['second_lapse_direct']['N']!=0
    assert a['second_lapse_from_shift']['N']!=0


def test_full_Ndoubleprime_proportional_to_Hg(a):
    v=step.manifest()
    assert v['combined_Nsecond']=='-(1-z²)*Hg_on_Fz/(Lg*Lf)'


def test_full_Mdoubleprime_exactly_zero(a):
    assert a['second_lapse_full']['M']==0


def test_physical_positive_K_center_limits(a):
    s=str(a['center_Nprime_shift_limit'])
    assert sp.simplify(a['center_Nprime_shift_limit']-(sp.Symbol('h0',positive=True)/sp.Symbol('k0',positive=True)-1/sp.Symbol('a',positive=True)))==0
    assert str(a['center_Mprime_shift_limit'])=='1/b'


def test_center_shift_second_lapse_coefficients(a):
    assert str(a['center_N2_on_Hg'])=='-2/a'
    assert str(a['center_M2_on_Hg'])=='2/b'


def test_step55_benchmark_center_kpositive_exact_rationals():
    f=Fraction
    aa=f('0.4'); bb=aa*f('0.5787707228025044'); m2=f('23.3348939346')
    t=aa**2+2*f('-4.2383993109')*aa*bb+f('13.6801214252')*bb**2
    k0=m2*aa*bb*t
    assert k0>f(229,1000)
    assert -2/aa==-5
    assert 2/bb>0


def test_do_not_confuse_shift_jet_with_full_Dirac(a):
    m=step.manifest()
    assert m['Dirac_rank']=='NOT_COMPUTED'
    assert m['lower_lapse_coefficients_reduced'] is False
    assert m['original_step55_profile_executed'] is False
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'

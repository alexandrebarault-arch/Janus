"""Physical source authenticity and exact center shift-Hamiltonian jet tests."""
from pathlib import Path
import sympy as sp
import pytest
from numerics import hr_step68c_authentic_center_hamiltonian as h
from numerics.hr_step45_exact_physical_ward import exact_physical_ward,exact_certificate_summary

@pytest.fixture(scope='module')
def v():return h.original_center()

@pytest.fixture(scope='module')
def lead():return h.verify_leading()

@pytest.fixture(scope='module')
def shift():return h.center_shift_response()


def test_original_blob_exact():
    assert h.authenticate()=='66aa43841dccfe4a5d586a49be9c10af3a67a10e'


def test_tampered_copy_rejected(tmp_path,monkeypatch):
    # Patch the exact source path read within authenticate() and assert fail closed.
    original_path=Path(h.__file__).with_name('hr_step45_exact_physical_ward.py')
    changed=tmp_path/'hr_step45_exact_physical_ward.py'
    changed.write_bytes(original_path.read_bytes()+b'\n# extra\n')
    actual_read=Path.read_bytes
    def intercept(self):
        if self==original_path:return actual_read(changed)
        return actual_read(self)
    monkeypatch.setattr(Path,'read_bytes',intercept)
    with pytest.raises(ValueError,match='drift'):h.authenticate()


def test_actual_six_pairs():
    assert len(exact_physical_ward()['Q'])==12
    assert tuple(exact_physical_ward()['Q'])==h.Q


def test_original_nine_ward_identities():
    assert len(exact_physical_ward()['residuals'])==9
    assert all(x==0 for x in exact_physical_ward()['residuals'].values())


def test_real_physical_original_nonzero_secondary():
    assert exact_physical_ward()['C_exact']!=0


def test_original_H_g_shift_stationarity():
    p=exact_physical_ward()
    assert sp.cancel(sp.together(sp.diff(p['Hg'],p['parameters'][-3])-p['Fz']/p['q'][0]))==0

@pytest.mark.parametrize('sector',['N','M'])
def test_g_metric_center(lead,sector):
    a=lead['rows'][sector]; assert sp.factor(a['Lg']-a['Sg'])==0

@pytest.mark.parametrize('sector',['N','M'])
def test_g_momentum_center(lead,sector):
    a=lead['rows'][sector]; assert sp.factor(a['pSg']-2*a['pLg'])==0

@pytest.mark.parametrize('sector',['N','M'])
def test_f_metric_center_after_primary(lead,sector):
    a=lead['rows'][sector]; assert sp.factor(a['Lf']-a['Sf'])==0

@pytest.mark.parametrize('sector',['N','M'])
def test_f_momentum_center_after_primary(lead,sector):
    a=lead['rows'][sector]; assert sp.factor(a['pSf']-2*a['pLf'])==0


def test_off_f_primary_defect_is_nonzero(lead,v):
    q=lead['offshell']['M'];b,U,V,M0=v['b'],v['U'],v['V'],v['M0'];mf=v['p']['parameters'][1]
    assert sp.factor(q['f_metric']-M0*(2*U-V)/(2*b*mf))==0
    assert sp.factor(q['f_momentum']-M0*U*(2*U-V)/(2*b**2*mf))==0
    assert q['f_metric'].subs({M0:1,U:1,V:0,b:1,mf:1})==1


def test_n2_hamiltonian_metric_jet(lead,v):
    mg=v['p']['parameters'][0]
    assert sp.diff(lead['rows']['N']['pLg'],v['N2'])==-4*mg
    assert sp.diff(lead['rows']['N']['pSg'],v['N2'])==-8*mg


def test_m2_hamiltonian_metric_jet(lead,v):
    mf=v['p']['parameters'][1]
    assert sp.diff(lead['rows']['M']['pLf'],v['M2'])==-4*mf
    assert sp.diff(lead['rows']['M']['pSf'],v['M2'])==-8*mf


def test_original_center_K_nonzero_symbolically(shift):
    assert shift['k0']!=0 and shift['k0'].has(shift['result']['N']['ek_center']) is False


def test_true_Dg_shift_stationarity_third(v,shift):
    r=v['r'];p=v['p'];s=v['sub']
    D=v['profiles']['pSg']*s[p['dq'][h.Q.index('Sg')]]-v['profiles']['Lg']*s[p['dq'][h.Q.index('pLg')]]+v['profiles']['pg']*s[p['dq'][h.Q.index('tg')]]
    assert sp.factor(sp.expand(D).coeff(r,3).subs(v['P3'],shift['P3_on_shift_stationarity'])-shift['k0']*v['w'])==0

@pytest.mark.parametrize('sector',['N','M'])
def test_forbidden_delta_Dg_r_term_exactly_zero(shift,sector):
    assert shift['result'][sector]['forbidden_linear_Dg']==0

@pytest.mark.parametrize('sector',['N','M'])
def test_center_ed_ek_computed_as_true_Hamiltonian(shift,sector):
    ed=shift['result'][sector]['ed_center'];ek=shift['result'][sector]['ek_center'];dz=shift['result'][sector]['delta_zprime_center']
    assert sp.factor(shift['k0']*dz-ed+shift['result'][sector]['ek_center']*h.original_center()['w'])==0
    assert not ed.has(h.original_center()['N4'],h.original_center()['M4'])


def test_lapse_M2_universal_shift_response(shift,v):
    assert sp.simplify(sp.diff(shift['result']['M']['delta_zprime_center'],v['M2'])-2/v['b'])==0


def test_lapse_N2_shift_response_on_Hg_primary(shift,v):
    coeff=sp.diff(shift['result']['N']['delta_zprime_center'],v['N2'])
    assert sp.factor(coeff-(2*shift['Hg0']/shift['k0']-2/v['a']))==0
    assert sp.factor((coeff+2/v['a']).subs(shift['Hg0'],0))==0 or sp.factor(coeff+2/v['a']-2*shift['Hg0']/shift['k0'])==0


def test_cross_sector_second_lapse_jet_absent(shift,v):
    assert sp.diff(shift['result']['N']['delta_zprime_center'],v['M2'])==0
    assert sp.diff(shift['result']['M']['delta_zprime_center'],v['N2'])==0


def test_negative_control_freezing_delta_zprime_fails(shift,v):
    assert sp.diff(shift['result']['M']['delta_zprime_center'],v['M2'])!=0
    assert sp.diff(shift['result']['N']['delta_zprime_center'],v['N2'])!=0


def test_distinct_bf2_and_interaction_beta2(v):
    assert v['bf2']!=v['p']['parameters'][5]
    assert v['sub'][v['p']['dq'][h.Q.index('tf')]]==v['kf0']*v['r']*(v['b']+v['bf2']*v['r']**2)


def test_manifest_never_claims_rank():
    m=h.manifest()
    assert m['original_step45_six_pair_ward_reexecuted'] is True
    assert m['temporal_Dirac_rank']=='NOT_COMPUTED'
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'

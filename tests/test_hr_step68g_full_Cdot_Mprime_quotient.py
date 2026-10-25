"""Exact original six-pair full temporal Cdot coefficient Mprime quotient."""
from pathlib import Path
import pytest
import sympy as sp
from numerics import hr_step68g_full_Cdot_Mprime_quotient as h
from numerics.hr_step68f_physical_pointwise import local_point
from numerics.hr_step58_temporal_operator import physical_operator
from numerics.hr_step45_exact_physical_ward import exact_physical_ward

@pytest.fixture(scope='module')
def cert():return h.second_jet_quotient()

def test_three_original_git_sources_authenticated(cert):
    assert h.authenticate()==h.SOURCES and len(h.SOURCES)==3

def test_mutation_of_each_original_source_fails(tmp_path,monkeypatch):
    original=h.__file__; root=Path(original).parent
    for name in h.SOURCES:
        dest=tmp_path/name
        dest.write_bytes((root/name).read_bytes()+b'\n# changed\n')
        old=Path.read_bytes
        def replacement(self):
            return old(dest) if self==root/name else old(self)
        monkeypatch.setattr(Path,'read_bytes',replacement)
        with pytest.raises(ValueError,match='source drift'):h.authenticate()
        monkeypatch.setattr(Path,'read_bytes',old)

def test_original_Mprime_contains_exactly_three_second_jets(cert):
    assert set(cert['unreduced_second_coefficients'])=={'pLg','Sg','tg'}
    assert all(v!=0 for v in cert['unreduced_second_coefficients'].values())

def test_complete_Fzprime_quotient_cancels_all_twelve(cert):
    p=exact_physical_ward();v=physical_operator()
    assert all(v==0 for v in cert['exact_second_jet_residuals'].values())
    for jet in p['ddq']:
        assert not cert['representative_qsecond_free'].has(jet)
    for jet in v['qppp']:
        assert not cert['representative_qsecond_free'].has(jet)

def test_lapse_Mprime_quotient_sign_exact(cert):
    v=physical_operator();p=exact_physical_ward();Lg,Lf=p['q'][0],p['q'][6];z=v['z']
    assert sp.factor(cert['lambda']-3*z*(z*z-1)/(Lg*Lf**2))==0
    assert sp.factor(cert['lambda']+3*z*(1-z*z)/(Lg*Lf**2))==0

def test_negative_wrong_sign_leaves_second_jet(cert):
    p=exact_physical_ward()
    bad=cert['raw']+cert['lambda']*cert['Fzprime_full']
    assert sp.factor(sp.diff(bad,p['ddq'][1]).subs(cert['shell']))!=0

def test_negative_omit_Fzprime_leaves_second_jet(cert):
    p=exact_physical_ward()
    assert sp.factor(sp.diff(cert['raw'],p['ddq'][1]).subs(cert['shell']))!=0

def test_center_quotient_weight_regular_only_in_product():
    v=h.center_product_certificate()
    assert v['regular'] and v['product_center'].startswith('-3*r³')

def test_true_pointwise_physical_Mprime_is_very_small(cert):
    d=local_point('0.4','0');f=sp.lambdify(d['symbols'],cert['raw'],'mpmath',cse=True)
    f2=sp.lambdify(d['symbols'],cert['representative_qsecond_free'],'mpmath',cse=True)
    assert abs(f(*d['values']))<1e-30
    assert abs(f2(*d['values']))<1e-30

def test_manifest_does_not_claim_rank():
    r=h.manifest()
    assert r['B_M_on_exact_step55_background_zero_proven'] is False
    assert r['Dirac_rank']=='NOT_COMPUTED'
    assert r['GATE_2B']=='OPEN' and r['JANUS_R']=='NOT_VALIDATED'

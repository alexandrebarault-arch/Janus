"""Original Step45 full shift Hamiltonian Frechet response, center Fz' quotient."""
import hashlib
from pathlib import Path
from fractions import Fraction
import pytest
import sympy as sp
from numerics import hr_step68e_exact_shift_full_lapse_response as h
from numerics.hr_step45_exact_physical_ward import exact_physical_ward


@pytest.fixture(scope='module')
def v():return h.full_shift_operator()


@pytest.fixture(scope='module')
def quotient():return h.first_stationarity_quotient()


def test_original_git_source_exact_byte_hash():
    assert h.authenticate()==h.SOURCE_SHA


def test_tampered_original_git_source_fails_closed(tmp_path,monkeypatch):
    from pathlib import Path
    authentic=Path(h.__file__).with_name('hr_step45_exact_physical_ward.py')
    changed=tmp_path/'hr_step45_exact_physical_ward.py'
    changed.write_bytes(authentic.read_bytes()+b'\n# forbidden change\n')
    old=Path.read_bytes
    def replaced(self):
        if self==authentic:return old(changed)
        return old(self)
    monkeypatch.setattr(Path,'read_bytes',replaced)
    with pytest.raises(ValueError,match='drift'):h.authenticate()


def test_original_all_six_pairs_present(v):
    p=v['data']['p']
    assert len(p['Q'])==12
    assert p['Q']==('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')


def test_original_all_nine_ward_identities_reexecuted(v):
    p=v['data']['p']
    assert len(p['residuals'])==9
    assert all(x==0 for x in p['residuals'].values())
    assert p['C_exact']!=0


@pytest.mark.parametrize('sector',['N','M'])
def test_exact_full_shift_lapse_orders(v,sector):
    assert set(v[sector]['delta_z'])=={0,1}
    assert all(v[sector]['delta_z'][j]!=0 for j in (0,1))


def test_fz_Nprime_original_step68d_identity(v):
    d=v['data'];p=d['p'];z=p['parameters'][-3]
    Lg=d['q']['Lg'];K=d['K']
    rhs=(1-z*z)**sp.Rational(3,2)*d['Hg_shell'] if 'Hg_shell' in d else (1-z*z)**sp.Rational(3,2)*p['Hg'].subs(d['shell'])
    rhs=rhs/K-(1-z*z)/Lg
    assert sp.factor(sp.cancel(v['N']['delta_z'][1].subs(d['shell'])-rhs))==0


def test_fz_Mprime_original_step68d_identity(v):
    d=v['data'];z=d['p']['parameters'][-3]
    assert sp.factor(sp.cancel(v['M']['delta_z'][1].subs(d['shell'])-(1-z*z)/d['q']['Lf']))==0


def test_Nzero_has_no_second_canonical_jet(quotient):
    assert quotient['N0_no_second_jets'] is True


def test_Mzero_has_exact_three_second_jet_dependencies(quotient):
    assert set(quotient['present_jets'])=={'pLg','Sg','tg'}
    assert all(expr!=0 for expr in quotient['present_jets'].values())


def test_coefficient_is_exactly_minus_z_t32_over_Lf_K(quotient,v):
    z=v['data']['p']['parameters'][-3]
    K=v['data']['K'];Lf=v['data']['q']['Lf']
    assert sp.factor(sp.cancel(quotient['alpha']+z*(1-z*z)**sp.Rational(3,2)/(Lf*K)))==0


def test_full_stationarity_radial_derivative_quotient_kills_all_12_jet_derivatives(quotient,v):
    p=v['data']['p']
    assert not (set(p['ddq']) & quotient['after'].free_symbols)
    for jj in p['ddq']:
        assert sp.diff(quotient['after'],jj)==0


def test_nontrivial_three_exact_residuals_zero(quotient):
    assert set(quotient['second_jet_residuals'])=={'pLg','Sg','tg'}
    assert all(x==0 for x in quotient['second_jet_residuals'].values())


def test_negative_omit_Fzprime_leaves_nonzero_second_jet(quotient,v):
    p=v['data']['p'];jj=p['ddq'][1]
    assert sp.cancel(sp.diff(quotient['before'],jj))!=0


def test_negative_wrong_sign_Fzprime_leaves_nonzero_second_jet(quotient,v):
    p=v['data']['p'];jj=p['ddq'][1]
    bad=quotient['before']-quotient['alpha']*quotient['Fz_prime']
    assert sp.cancel(sp.diff(bad,jj))!=0


def test_center_quotient_parity_exact():
    a=h.center_regular_quotient()
    r=next(x for x in a['alpha'].free_symbols if x.name=='r')
    assert sp.limit(a['product'],r,0)==0
    assert sp.simplify(a['alpha']*a['Fz_prime']-a['product'])==0


def test_center_quotient_strict_rational_benchmark():
    a=h.center_regular_quotient()
    subs={sym:val for sym,val in
          [(next(x for x in a['alpha'].free_symbols if x.name=='w'),sp.Rational(1,250)),
           (next(x for x in a['alpha'].free_symbols if x.name=='k'),sp.Rational(1,4)),
           (next(x for x in a['alpha'].free_symbols if x.name=='Lf'),sp.Rational(1,5)),
           (next(x for x in a['alpha'].free_symbols if x.name=='s'),sp.Rational(1,4)),
           (next(x for x in a['Fz_prime'].free_symbols if x.name=='f'),sp.Integer(1)),
           (next(x for x in a['Fz_prime'].free_symbols if x.name=='fs'),sp.Integer(0))]}
    r=next(x for x in a['alpha'].free_symbols if x.name=='r')
    val=a['product'].subs(subs)
    assert sp.limit(val/r,r,0).is_finite and sp.limit(val/r,r,0)!=0


def test_manifest_no_temporal_rank_claim():
    x=h.manifest()
    assert x['M0_quotient_no_second_jets'] is True
    assert x['full_temporal_Cdot_low_lapse_operator']=='NOT_REDUCED'
    assert x['Step55_certified_radial_profile_used'] is False
    assert x['Dirac_rank']=='NOT_COMPUTED'
    assert x['GATE_2B']=='OPEN' and x['JANUS_R']=='NOT_VALIDATED'

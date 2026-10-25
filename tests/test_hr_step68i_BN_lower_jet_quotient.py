"""Step68i exact original Step60/58 full temporal B_N qthird/qsecond quotient."""
from pathlib import Path
from random import Random
import mpmath as mp
import pytest
import sympy as sp
from numerics import hr_step68i_BN_lower_jet_quotient as h
from numerics.hr_step45_exact_physical_ward import exact_physical_ward
from numerics.hr_step58_temporal_operator import physical_operator
from numerics.hr_step68f_physical_pointwise import local_point

@pytest.fixture(scope='module')
def cert():return h.physical_BN_second_jet_quotient()

def test_authenticated_five_original_sources(cert):
    assert cert['source_git_blobs']==h.ORIGINALS and len(h.ORIGINALS)==5

def test_original_source_mutation_rejected(monkeypatch,tmp_path):
    import numerics.hr_step68i_BN_lower_jet_quotient as m
    root=Path(m.__file__).parent
    raw=Path.read_bytes; orig=root/'hr_step60_full_constraint_prolongation.py'
    changed=tmp_path/'changed.py';changed.write_bytes(raw(orig)+b'\n#tamper\n')
    def intercepted(self):return raw(changed) if self==orig else raw(self)
    monkeypatch.setattr(Path,'read_bytes',intercepted)
    with pytest.raises(ValueError,match='source drift'):m.authenticate()

def test_correct_complete_Hgprime_subtraction_from_step60(cert):
    p=exact_physical_ward();o=physical_operator();q=dict(zip(p['Q'],p['q']));z=o['z']
    assert sp.factor(cert['H_g_prime_correction']-(1-z*z)/(q['Lg']*q['Lf']))==0
    assert sp.factor(cert['H_g_second_coefficient']-2*p['parameters'][0]*q['Sg']/q['Lg'])==0

def test_exact_beta_eliminates_all_twelve_second_jets(cert):
    p=exact_physical_ward()
    assert cert['second_derivative_residuals']=={'Lg':0,'pLg':0,'Sg':0,'tg':0}
    assert all(not cert['representative_qsecond_and_qthird_free'].has(j) for j in p['ddq'])

def test_exact_beta_eliminates_all_twelve_third_jets(cert):
    o=physical_operator()
    assert all(not cert['representative_qsecond_and_qthird_free'].has(j) for j in o['qppp'])

def test_wrong_beta_sign_reintroduces_Sg_second_jet(cert):
    p=exact_physical_ward();j=p['ddq'][2]
    wrong=cert['raw_quotient']+2*cert['beta']*cert['physical_Hg_stationary']
    assert sp.factor(sp.cancel(sp.diff(wrong,j)))!=0

def test_physically_constrained_local_point_remainder_small(cert):
    prof=local_point('0.4')
    fn=sp.lambdify(prof['symbols'],cert['representative_qsecond_and_qthird_free'],'mpmath',cse=True)
    assert abs(fn(*prof['values']))<mp.mpf('1e-40')

def test_generic_off_constraints_remainder_nonzero(cert):
    v=cert['representative_qsecond_and_qthird_free'];s=sorted(v.free_symbols,key=str)
    r=Random(23)
    point={x:mp.mpf(r.randrange(3,20))/10 for x in s}
    for x in s:
        if x.name=='z':point[x]=mp.mpf('0.2')
        if x.name=='zr':point[x]=mp.mpf('0.3')
        if x.name=='tgr':point[x]=mp.mpf(0)
    fn=sp.lambdify(s,v,'mpmath',cse=True)
    assert abs(fn(*[point[x] for x in s]))>mp.mpf('0.01')

def test_beta_center_separate_and_rank_undecided():
    a=h.manifest()
    assert a['beta_ops']>=100
    assert a['regular_center_beta_studied'] is False
    assert a['representative_is_identically_zero'].startswith('NOT_PROVED')
    assert a['Dirac_rank']=='NOT_COMPUTED'
    assert a['GATE_2B']=='OPEN' and a['JANUS_R']=='NOT_VALIDATED'

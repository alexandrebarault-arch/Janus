"""Exact original Step45/58 constrained flat-family lapse-rank witness."""
import sympy as sp
import pytest
from numerics.hr_step68k_exact_positive_lapse_family import exact_family,rational_witness,manifest

@pytest.fixture(scope='module')
def family():return exact_family()

def test_authentic_eight_original_module_blobs(family):
    assert len(family['original_pins'])==8

@pytest.mark.parametrize('name',['Fz','Hg','Hf','C','Dg','Df'])
def test_exact_original_constraints_all_r(family,name):
    assert family['constraints'][name]==0

@pytest.mark.parametrize('name',['Fz','Hg','Hf','C','Dg','Df'])
def test_exact_original_radial_constraint_prolongations(family,name):
    assert family['constraints'][name+'prime']==0

def test_k_positive_under_stated_assumptions(family):
    assert sp.factor(family['T']- (family['parameter_symbols'][1]+2*family['parameter_symbols'][2]+family['parameter_symbols'][3]))==0
    assert family['T'].subs(dict(zip(family['parameter_symbols'],(-5,1,0,0,-5))))==1

def test_eight_original_temporal_coefficients(family):
    assert sp.factor(family['coefficients']['N',0]-family['expected_N'])==0
    assert sp.factor(family['coefficients']['M',0]-family['expected_M'])==0
    assert all(family['coefficients'][sector,j]==0 for sector in ('N','M') for j in (1,2))

def test_exact_positive_lapse_ratio_and_rational_witness(family):
    w=rational_witness()
    assert w['ratio']=='2/3'
    assert w['rho_g']=='2' and w['rho_f']=='4'
    assert sp.factor(3*family['expected_N']+2*family['expected_M'])!=0  # only witness parameters

def test_dust_positivity_is_a_premise_not_automatic(family):
    b0,b1,b2,b3,b4=family['parameter_symbols']
    bad={b0:-5,b1:1,b2:0,b3:0,b4:1}
    assert family['rho_f'].subs(bad)==-2
    assert family['expected_M'].subs(bad)==0  # destroys nonzero lapse-rank hypothesis

def test_scope_honesty():
    doc=manifest()
    assert doc['GATE_2B']=='OPEN' and doc['JANUS_R']=='NOT_VALIDATED'
    assert 'NOT Step55 nonhomothetic branch' in doc['not_claimed']
    assert 'NOT general Dirac rank' in doc['not_claimed']

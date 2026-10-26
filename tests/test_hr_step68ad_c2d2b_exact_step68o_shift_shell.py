"""Independent tests of exact Step55/Step68o stationary shift identity."""
import sympy as sp
import pytest
from numerics.hr_step68ad_c2d2b_exact_step68o_shift_shell import identities, manifest, counterexample_negative_k

@pytest.fixture(scope='module')
def x():return identities()

def test_D_is_cubic(x): assert sp.cancel(x['D']-x['r']**3*x['dbar'])==0
def test_K_is_quadratic(x): assert sp.cancel(x['K']-x['r']**2*x['k'])==0
def test_norm_squared(x):
    assert sp.cancel((x['D']**2+x['K']**2)*(1-x['z1']**2*x['s'])-x['r']**4*x['k']**2)==0
def test_Fz_stationarity(x):
    assert sp.cancel(x['D']-x['K']*x['z']/sp.sqrt(1-x['z']**2))==0
def test_first_shift_jet(x): assert sp.diff(x['z'],x['r'])==x['z1']
def test_second_shift_jet(x): assert sp.diff(x['z'],x['r'],2)==0
def test_third_shift_jet(x): assert sp.diff(x['z'],x['r'],3)==0
def test_dust_density_cancels(x): assert sp.simplify(sp.diff(x['D'],x['rhog']))==0
def test_wrong_k_branch():
    assert counterexample_negative_k()['sign_of_D_over_root']==-1
def test_manifest_is_fail_closed():
    m=manifest();assert m['Step58_7_cells']=='NOT_EXECUTED' and m['new_temporal_signs']==0

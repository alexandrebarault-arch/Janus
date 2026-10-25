"""Original six-pair Step58 global Mprime lapse-derivative identity on Fz,Fzprime."""
from pathlib import Path
import sympy as sp
import pytest
from numerics import hr_step68h_BM_global_identity as h
from numerics.hr_step58_temporal_operator import physical_operator
from numerics.hr_step45_exact_physical_ward import exact_physical_ward

@pytest.fixture(scope='module')
def proof():return h.full_original_BM_identity()

def test_real_original_sources(proof):
    assert len(proof['source_git_blobs'])==3

def test_exact_24_independent_symbolic_partial_derivatives(proof):
    assert proof['num_independent_variables']==24
    assert set(proof['variables_checked'].values()) <= {'ZERO_RAW','EXACT_NUMERATOR_ZERO'}

def test_exact_rational_zero_reference(proof):
    assert proof['reference_exact_zero']==0
    pt=proof['rational_chart'];assert any(x.name=='z' and y==sp.Rational(3,5) for x,y in pt.items())

def test_original_BM_coefficient_precise_identity(proof):
    o=physical_operator();p=exact_physical_ward();z=o['z'];Lg,Lf=p['q'][0],p['q'][6]
    assert proof['lambda']==sp.factor(3*z*(z*z-1)/(Lg*Lf**2))
    assert proof['original_expression']==o['operator']['M'][1]

def test_requires_first_stationarity_prolongation(proof):
    p=exact_physical_ward(); o=physical_operator()
    assert sp.diff(proof['original_expression'],p['ddq'][1])!=0
    assert sp.diff(proof['Fz_radial_derivative'],p['ddq'][1])==-p['q'][0]

def test_independent_exact_off_other_primaries_original_BM(proof):
    """A rational canonical point satisfying ONLY Fz=Fz'=0 makes B_M=0.

    All Hg,Hf,C deliberately remain nonzero; this is a strong negative control
    against mistaking their enforcement for the source of the cancellation.
    """
    p=exact_physical_ward();o=physical_operator()
    pLgprime=p['dq'][1];pLgsecond=p['ddq'][1]
    Fzprime=o['Dt'](p['Fz'])
    solved_pLgsecond=sp.cancel(Fzprime.subs(proof['Fz_shell']).subs(pLgsecond,0)/p['q'][0])
    symbols=set().union(o['operator']['M'][1].free_symbols,solved_pLgsecond.free_symbols,
                         p['Hg'].free_symbols,p['Hf'].free_symbols,p['C_exact'].free_symbols)
    point={x:sp.S.One for x in symbols}
    for x in symbols:
        if x.name=='z':point[x]=sp.Rational(3,5)
        if x.name=='zr':point[x]=sp.Rational(1,10)
        if x.name=='tgr':point[x]=sp.S.Zero
        if x.name=='beta2':point[x]=sp.Rational(-1,2)
        if x.name=='pLg':point[x]=sp.Rational(3,2)
        if x.name=='pSf':point[x]=sp.Rational(7,5)
        if x.name=='pg':point[x]=sp.Rational(9,10)
        if x.name=='pf':point[x]=sp.Rational(11,10)
    point[pLgprime]=sp.cancel(proof['Fz_shell'][pLgprime].subs(point))
    point[pLgsecond]=sp.cancel(solved_pLgsecond.subs(point))
    assert sp.cancel(p['Fz'].subs(point))==0
    assert sp.cancel(Fzprime.subs(point))==0
    assert sp.cancel(o['operator']['M'][1].subs(point))==0
    assert p['Hg'].subs(point)!=0
    assert p['Hf'].subs(point)!=0
    assert p['C_exact'].subs(point)!=0


def test_wrong_sign_negative_control(proof):
    p=exact_physical_ward()
    wrong=proof['original_expression']+proof['lambda']*proof['Fz_radial_derivative']
    assert sp.factor(sp.diff(wrong,p['ddq'][1]).subs(proof['Fz_shell']))!=0


def test_manifest_does_not_claim_rank():
    r=h.manifest()
    assert r['on_Fz_and_Fzprime_zero']=='B_M=EXACT_ZERO'
    assert r['B_N_on_complete_shell']=='NOT_YET_ANALYTICALLY_REDUCED'
    assert r['Dirac_rank']=='NOT_COMPUTED'
    assert r['GATE_2B']=='OPEN' and r['JANUS_R']=='NOT_VALIDATED'

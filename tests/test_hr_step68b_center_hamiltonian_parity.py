"""Step68b fixed-center parity, independently reconstructed from Step45 densities.

These targeted tests do not claim full original temporal Dirac rank or
physical-on-shell evaluation of lapse coefficients.
"""
import pytest
import sympy as sp
from numerics import hr_step68b_center_hamiltonian_parity as h

@pytest.fixture(scope='module')
def audit():
    return h.center_audit()


def test_six_pairs_preserved_in_model():
    assert len(h.Q)==12
    assert h.Q==('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')


def test_true_g_lapse_post_ibp_metric_density():
    assert h.sp.simplify(h.Bg+2*h.mg*h.Sg*h.Sgr/h.Lg-h.z*h.plg)==0


def test_true_f_lapse_post_ibp_metric_density():
    assert h.sp.simplify(h.Bf+2*h.mf*h.Sf*h.Sfr/h.Lf-h.z*h.Lg*h.plg/h.Lf)==0

@pytest.mark.parametrize('lapse',['N','M'])
def test_g_center_metric_parity(audit,lapse):
    assert sp.factor(audit[lapse]['Sg']-audit[lapse]['Lg'])==0

@pytest.mark.parametrize('lapse',['N','M'])
def test_g_center_momentum_parity(audit,lapse):
    assert sp.factor(audit[lapse]['pSg']-2*audit[lapse]['pLg'])==0

@pytest.mark.parametrize('lapse',['N','M'])
def test_f_center_metric_parity_on_f_primary(audit,lapse):
    assert sp.factor(audit[lapse]['Sf']-audit[lapse]['Lf'])==0

@pytest.mark.parametrize('lapse',['N','M'])
def test_f_center_momentum_parity_on_f_primary(audit,lapse):
    assert sp.factor(audit[lapse]['pSf']-2*audit[lapse]['pLf'])==0

@pytest.mark.parametrize('lapse',['N','M'])
def test_Dg_leading_radial_variation_zero(audit,lapse):
    assert audit[lapse]['delta_Dg_over_r_at_center']==0


def test_nonzero_lapse_second_jet_must_not_be_omitted(audit):
    assert sp.diff(audit['N']['pLg'],h.N2)==-4*h.mg
    assert sp.diff(audit['N']['pSg'],h.N2)==-8*h.mg
    assert sp.diff(audit['M']['pLf'],h.M2)==-4*h.mf
    assert sp.diff(audit['M']['pSf'],h.M2)==-8*h.mf


def test_independent_lapse_gauge_no_required_ratio(audit):
    assert not audit['N']['Lg'].has(h.M0,h.M2)
    assert not audit['M']['Lg'].has(h.N0,h.N2)
    assert audit['N']['Lg']!=0 and audit['M']['Lg']!=0


def test_negative_off_f_primary_generates_metric_parity_defect(audit):
    err=audit['f_offshell_defects']['M']['metric']
    assert sp.factor(err-h.M0*(2*h.U-h.V)/(2*h.b*h.mf))==0
    assert sp.factor(err.subs(h.V,2*h.U))==0
    assert sp.factor(err.subs({h.V:0,h.U:1,h.M0:1,h.b:1,h.mf:1}))==1


def test_negative_off_f_primary_generates_momentum_parity_defect(audit):
    err=audit['f_offshell_defects']['M']['momentum']
    assert sp.factor(err-h.M0*h.U*(2*h.U-h.V)/(2*h.b**2*h.mf))==0
    assert sp.factor(err.subs(h.V,2*h.U))==0


def test_f_primary_center_from_original_radial_momentum_relation():
    # Step46: pSf=(-Dg+Lf*pLf'-pf*tfr)/Sfr;
    # Dg=O(r^3), pLf'=2U*r+O(r^3), pf*tfr=O(r^3)
    r=sp.symbols('r',positive=True)
    expression=(-r**3*h.w+(h.b+h.b2*r*r)*(2*h.U*r+4*h.G2*r**3)
                -h.rhof*r*r*h.kf0*r*(h.b+h.b2*r*r))/(h.b+3*h.b2*r*r)
    assert sp.limit(expression/r,r,0)==2*h.U


def test_no_frozen_metric_variation(audit):
    assert audit['M']['Lg']==h.M0*h.a*h.w/h.b
    assert audit['M']['Sg']==h.M0*h.a*h.w/h.b

@pytest.mark.parametrize('kwargs',[{'principal_g_momentum_factor':1},
                                    {'principal_f_momentum_factor':1},
                                    {'even_lapse':False}])
def test_fail_closed_unphysical_chart(kwargs):
    with pytest.raises(ValueError,match='BOTH'):
        h.fail_closed(**kwargs)


def test_status_and_provider_provenance_fail_closed():
    m=h.manifest()
    assert m['physical_original_Step45_byte_imported'] is False
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'
    assert 'no lapse rank' in m['not_proved']

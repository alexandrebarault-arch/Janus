from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import pytest
import sympy as sp
from numerics.hr_step68ad_c1_center_momentum_jet import (
    PINS, S_MAX, pair, git_blob, certify_from_reports, read_pinned)

@pytest.fixture
def authentic_fields():
    # Values transcribed from SHA-verified GitHub original reports;
    # standalone tests of pure algebra, not substitutes for read_pinned().
    return {
      '68v':{'step':'68v','center_s_range':['0','1/64'],
        'U_s_strict_positive_inner':True,
        'U_s_center_lower_rational':'3947151372926460534852373/5000000000000000000000000000',
        'U_s_center_upper_rational':'7897452509337401302640553/10000000000000000000000000000',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'},
      '68ac':{'step':'68ac','center_U0_interval':[
        '-10504853793521470008293157/2000000000000000000000000000',
        '-26262134483803675020732891/5000000000000000000000000000'],
        'center_exact_symbolic_GU':{'center_GU0_exact':'-1'},
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'},
      'B2':{'step':'68ad-B2','s_domain':['0','1/1024'],'r_domain':['0','1/32'],
        'strict_negative_R2_U_ss_R3_U_sss':True,
        'original_report_sha':{'68v':PINS['68v'][1],'68ac':PINS['68ac'][1]},
        'U_ss_global':['-1414170375015186192017477/69938619264706447051250697260',
                       '-281308311835510868820846/14012170704330665327521777975'],
        'U_sss_global':['-3660344913192819744137/44969309632353223525625348630',
                        '-6226026282646364646283/90060853521653326637608889875'],
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    }

@pytest.fixture
def proof(authentic_fields):return certify_from_reports(authentic_fields)

def test_original_report_shas_pinned():
    assert len(PINS)==3
    assert PINS['B2'][1]=='ac961b5b83667a83497497d22a701c24584cb561'

def test_fraction_interval_exact():
    assert pair(['1/3','2/3'])==(F(1,3),F(2,3))
    with pytest.raises(ValueError):pair(['2','1'])
    with pytest.raises(ValueError):pair(['1'])

def test_git_blob_matches_git_definition():
    assert git_blob(b'hello\n')=='ce013625030ba8dba906f756967f9e9ca394464a'

def test_symbolic_chain_rules_are_exact():
    r=sp.symbols('r',positive=True);U=sp.Function('U');s=sp.symbols('s')
    p=r**2*U(r**2)
    derivatives=[2*r*(U(s)+s*sp.diff(U(s),s)),
        2*U(s)+10*s*sp.diff(U(s),s)+4*s**2*sp.diff(U(s),s,2),
        r*(24*sp.diff(U(s),s)+36*s*sp.diff(U(s),s,2)+8*s**2*sp.diff(U(s),s,3))]
    for k,v in enumerate(derivatives,1):
        assert sp.simplify(sp.diff(p,r,k)-v.subs(s,r**2))==0

def test_symbolic_composite_U_third_over_r():
    r=sp.symbols('r',positive=True);s=sp.symbols('s');U=sp.Function('U')
    assert sp.simplify(sp.diff(U(r**2),r,3)-r*(12*sp.diff(U(s),s,2)+8*s*sp.diff(U(s),s,3)).subs(s,r**2))==0

def test_certified_canonical_signs(proof):
    assert proof['pLf_prime_over_r_strict_negative']
    assert proof['pLf_second_strict_negative']
    assert proof['pLf_third_over_r_strict_positive']
    assert proof['U_of_r_third_over_r_strict_negative']
    for k,sign in [('pLf_prime_over_r_continuum',-1),('pLf_second_continuum',-1),
                   ('pLf_third_over_r_continuum',1),('U_of_r_third_over_r_continuum',-1)]:
        lo,hi=map(F,proof[k]);assert lo<=hi
        assert (hi<0) if sign<0 else (lo>0)

def test_bounds_numeric_sanity(proof):
    a,b=map(F,proof['pLf_third_over_r_continuum'])
    assert F(189,10000)<a<b<F(19,1000)
    a,b=map(F,proof['pLf_second_continuum'])
    assert -F(11,1000)<a<b<-F(10,1000)

def test_no_interval_derivative_shortcut(proof):
    assert proof['identities']['pLf_third_over_r']=='24 U_s+36s U_ss+8s² U_sss'
    assert proof['remaining_seven_temporal_cells']=='PENDING'
    assert proof['temporal_original_A_N_A_M']=='NOT_COMPUTED'
    assert proof['GATE_2B']=='OPEN' and proof['JANUS_R']=='NOT_VALIDATED'

def test_reject_reversed_higher_derivative(authentic_fields):
    authentic_fields['B2']['U_ss_global']=['1','2']
    with pytest.raises(ArithmeticError):certify_from_reports(authentic_fields)

def test_reject_forged_original_report_sha(authentic_fields):
    authentic_fields['B2']['original_report_sha']['68v']='0'*40
    with pytest.raises(ValueError):certify_from_reports(authentic_fields)

def test_reject_wrong_domain(authentic_fields):
    authentic_fields['B2']['s_domain']=['0','1/64']
    with pytest.raises(ValueError):certify_from_reports(authentic_fields)

def test_reject_premature_validated_gate(authentic_fields):
    authentic_fields['B2']['JANUS_R']='VALIDATED'
    with pytest.raises(ValueError):certify_from_reports(authentic_fields)

def test_reject_tampered_report_bytes(tmp_path):
    for key,(name,_) in PINS.items():
        (tmp_path/name).write_text('{}')
    with pytest.raises(ValueError,match='SHA mismatch'):read_pinned(tmp_path)

def test_center_values_are_not_temporal_coefficients(proof):
    assert proof['center_pLf_second_equals_2U0']
    assert proof['center_pLf_third_equals_zero']
    assert proof['full_Dirac_rank']=='NOT_COMPUTED'

def test_published_certificate_matches_exact_fraction_computation(authentic_fields):
    import json
    p=Path(__file__).resolve().parents[1]/'research'/'reports'/'gate2b-step68ad-C1-original-canonical-pLf-third-jet.json'
    assert json.loads(p.read_text())==certify_from_reports(authentic_fields)

"""Exact and rational tests for Step68ad-A; NO physical R_n continuum claim."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha1
from math import factorial
import json
import shutil
import pytest
import sympy as sp
from numerics.hr_step68ad_center_derivative_transport import (
    SOURCE_REPORTS, EXPECTED_PHYSICAL_ORIGINALS, blob_sha, interval,
    load_physical_reports, damping_bounds, ratio_enclosure,
    center_source_intervals, symbolic_transport_identities, certificate,
)

ROOT=Path(__file__).resolve().parents[1]
REPORTS=ROOT/'research'/'reports'

@pytest.fixture(scope='module')
def sources():return load_physical_reports(REPORTS)

@pytest.fixture(scope='module')
def result():return certificate(REPORTS)


def test_both_original_reports_byte_exact():
    for _,(name,sha) in SOURCE_REPORTS.items():
        assert blob_sha((REPORTS/name).read_bytes())==sha


def test_physical_provenance_chain_matches_all_four_originals(sources):
    assert sources['68v']['original_physical_shas']==EXPECTED_PHYSICAL_ORIGINALS
    assert all(sources['68ac']['original_source_git_blob_shas'][k]==v
               for k,v in EXPECTED_PHYSICAL_ORIGINALS.items())


def test_fail_closed_step68v_report_tamper(tmp_path):
    for name,_ in SOURCE_REPORTS.values():shutil.copy(REPORTS/name,tmp_path/name)
    p=tmp_path/SOURCE_REPORTS['68v'][0]
    p.write_bytes(p.read_bytes()+b'\n')
    with pytest.raises(ValueError,match='Step68v Git blob mismatch'):
        load_physical_reports(tmp_path)


def test_fail_closed_step68ac_report_tamper(tmp_path):
    for name,_ in SOURCE_REPORTS.values():shutil.copy(REPORTS/name,tmp_path/name)
    p=tmp_path/SOURCE_REPORTS['68ac'][0]
    p.write_bytes(p.read_bytes().replace(b'"U4_sign_strict_negative": true',
                                         b'"U4_sign_strict_negative": false'))
    with pytest.raises(ValueError,match='Step68ac Git blob mismatch'):
        load_physical_reports(tmp_path)


def test_physical_GU_negative_strict_and_contains_center_minus_one(sources):
    lo,hi=interval(sources['68v']['G_U_center_interval'])
    assert lo<-1<hi<0
    assert F('-1.007')<lo<F('-1.005')
    assert F('-.995')<hi<F('-.993')


@pytest.mark.parametrize('n,lower,upper',[(1,4,6),(2,6,8),(3,8,10),(4,10,12)])
def test_all_physical_damping_coefficients_positive(sources,n,lower,upper):
    lo,hi=damping_bounds(sources['68v']['G_U_center_interval'],n)
    assert F(lower)<lo<hi<F(upper)
    assert lo>0


def test_damping_invalid_inputs_fail():
    with pytest.raises(ValueError):damping_bounds((-1,1),0)
    with pytest.raises(ArithmeticError):damping_bounds((10,11),1)
    with pytest.raises(ValueError):interval(('2','1'))


def test_exact_symbolic_transport_n1_to_n4():
    identities=symbolic_transport_identities()
    assert list(identities)==['1','2','3','4']
    assert [identities[str(n)]['source_term_count'] for n in range(1,5)]==[1,4,9,17]
    assert all(v['source_excludes_U_n'] and v['symbolic_identity_exact'] for v in identities.values())


def test_exact_original_center_source_signs_and_factors(sources):
    r=center_source_intervals(sources['68ac'])
    assert [r[str(n)]['sign'] for n in range(1,5)]==['POSITIVE','NEGATIVE','NEGATIVE','NEGATIVE']
    for n,key in [(1,'original_U1_interval'),(2,'original_U2_interval'),
                  (3,'original_Step67b_U3_interval'),(4,'intersection_certified_U4')]:
        a,b=interval(sources['68ac'][key]);c,d=interval(r[str(n)]['R_n_at_center'])
        factor=(2*n+3)*factorial(n)
        assert (c,d)==(factor*a,factor*b)


def test_original_U4_center_source_is_strict_negative(sources):
    lo,hi=interval(center_source_intervals(sources['68ac'])['4']['R_n_at_center'])
    assert -F(1,10**7)<lo<hi<-F(1,10**8)


def test_ratio_interval_signed_positive_and_mixed():
    assert ratio_enclosure((2,8),(2,4))==(F(1,2),F(4))
    assert ratio_enclosure((-8,-2),(2,4))==(F(-4),F(-1,2))
    assert ratio_enclosure((-8,2),(2,4))==(F(-4),F(1))
    assert ratio_enclosure((0,0),(1,3))==(F(0),F(0))


def test_ratio_invalid_zero_crossing_and_reversed():
    with pytest.raises(ValueError):ratio_enclosure((1,2),(-1,2))
    with pytest.raises(ValueError):ratio_enclosure((1,2),(0,2))
    with pytest.raises(ValueError):ratio_enclosure((3,2),(1,2))


def test_manufactured_nonlinear_s_transport_exact():
    """Exact algebra, not an oracle for original JANUS G."""
    s,u=sp.symbols('s u')
    U=F(2,7)+2*s-3*s**2+4*s**3-5*s**4
    H=sp.expand(2*s*sp.diff(U,s)+(3+s)*U)
    G=-(1+s)*u+H
    assert sp.expand(2*s*sp.diff(U,s)+2*U-G.subs(u,U))==0
    for n in range(1,5):
        un=sp.diff(U,s,n)
        Rn=sp.expand(sp.diff(G.subs(u,U),s,n)-sp.diff(G,u).subs(u,U)*un)
        an=2*n+2-sp.diff(G,u)
        assert sp.expand(2*s*sp.diff(un,s)+an*un-Rn)==0
        assert sp.simplify(an.subs(s,0)-(2*n+3))==0


def test_exact_constant_damping_unique_bounded_center():
    """General solution y=R/a + C*s^(-a/2), bounded iff C=0."""
    s=sp.symbols('s',positive=True)
    a=sp.Rational(9,2);R=sp.Rational(-7,3)
    C=sp.symbols('C')
    y=R/a+C*s**(-a/2)
    assert sp.simplify(2*s*sp.diff(y,s)+a*y-R)==0
    assert sp.limit(y.subs(C,0),s,0)==R/a
    assert sp.limit(y.subs(C,1),s,0)==sp.oo
    assert ratio_enclosure((R,R),(a,a))==(R/a,R/a)


def test_certified_damping_is_not_mistaken_for_physical_high_jets(result):
    assert result['physical_U_ss_and_U_sss_on_positive_radius']=='NOT_CERTIFIED'
    assert result['temporal_original_Step58_A_N_A_M']=='NOT_COMPUTED'
    assert result['full_Dirac_rank']=='NOT_COMPUTED'
    assert result['missing_physical_Rn_continuum_enclosures']==['R2','R3','R4']
    assert result['GATE_2B']=='OPEN' and result['JANUS_R']=='NOT_VALIDATED'


def test_report_exactly_matches_executed_code(result):
    stored=json.loads((REPORTS/'gate2b-step68ad-A-derivative-transport.json').read_text())
    assert stored==result

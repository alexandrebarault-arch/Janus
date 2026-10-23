"""Exact real 6-pair Step59 third radial-jet multiplier gates (not lapse rank)."""
import sympy as sp
import pytest
from numerics.hr_step59_third_jet_gate import (
    third_jet_certificate,shift_jet_prolongation,manifest)
from numerics.hr_step58_temporal_operator import physical_operator,highest_lapse_certificate
from numerics.hr_step57_secondary_principal_symbol import authenticated_step45


@pytest.fixture(scope='module')
def cert():return third_jet_certificate()


@pytest.fixture(scope='module')
def shift():return shift_jet_prolongation()


def test_original_physical_Step45_byte_authenticated_and_full_six_pairs(cert):
    p=authenticated_step45()
    assert len(p['Q'])==12 and len(p['eg'])==len(p['ef'])==3
    assert cert['source_original_step45_sha']=='66aa43841dccfe4a5d586a49be9c10af3a67a10e'


def test_actual_N0_and_M1_independent_of_all_canonical_third_jets_on_Fz(cert):
    assert cert['actual']['N0']=={}
    assert cert['actual']['M1']=={}


def test_exact_Nprime_Sg_third_derivative_sensitivity(cert):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']));z=p['parameters'][-3]
    expected=-2*p['parameters'][0]*q['Sg']*(1-z*z)/(q['Lf']*q['Lg']**2)
    assert sp.cancel(cert['actual']['N1']['Sg']-expected)==0
    assert set(cert['actual']['N1'])=={'Sg'}


def test_exact_M_three_third_jet_coefficients(cert):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']));z=p['parameters'][-3]
    alpha=z*(1-z*z)/q['Lf']**2
    assert set(cert['actual']['M0'])=={'pLg','Sg','tg'}
    assert sp.factor(cert['actual']['M0']['pLg']-alpha)==0
    assert sp.factor(cert['actual']['M0']['Sg']+q['pSg']*alpha/q['Lg'])==0
    assert sp.factor(cert['actual']['M0']['tg']+q['pg']*alpha/q['Lg'])==0


def test_Dg_second_principal_exactly_explains_M_third_jets(cert):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']))
    assert cert['Dg_second_principal']=={'pLg':-q['Lg'],'Sg':q['pSg'],'tg':q['pg']}
    for key,val in cert['Dg_second_principal'].items():
        assert sp.cancel(cert['actual']['M0'][key]-cert['M0_principal_via_Dg_second']*val)==0


def test_positive_metric_branch_Nprime_coefficient_strictly_negative(cert):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']));z=p['parameters'][-3]
    # Physically admissible positive Lg,Lf,Sg,Mg2 and 0<=z<1.
    x=cert['actual']['N1']['Sg'].subs({q['Lg']:sp.Rational(2,5),
      q['Lf']:sp.Rational(1,4),q['Sg']:sp.Rational(1,6),
      p['parameters'][0]:1,z:sp.Rational(1,100)})
    assert x<0


def test_nonzero_shift_M_coefficient_positive_at_generic_inner_radius(cert):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']));z=p['parameters'][-3]
    val=cert['actual']['M0']['pLg'].subs({q['Lf']:sp.Rational(1,4),z:sp.Rational(1,100)})
    assert val>0
    assert cert['actual']['M0']['pLg'].subs(z,0)==0


def test_stationary_shift_positive_root_exact_for_two_prolongations(shift):
    assert shift['positive_K_stationarity_exact']
    D,K,D1,K1,D2,K2=[shift[k] for k in ('D','K','Dprime','Kprime','Dsecond','Ksecond')]
    R=sp.sqrt(D*D+K*K)
    z=shift['z']
    total=lambda e:sum(sp.diff(e,u)*v for u,v in [(D,D1),(K,K1),(D1,D2),(K1,K2)])
    assert sp.simplify(total(z)-shift['zprime'])==0
    assert sp.simplify(total(shift['zprime'])-shift['zsecond'])==0


def test_finite_difference_shift_jet_consistency_has_nonzero_curvature(shift):
    D,K,D1,K1,D2,K2=[shift[k] for k in ('D','K','Dprime','Kprime','Dsecond','Ksecond')]
    values={D:2,K:3,D1:sp.Rational(1,5),K1:sp.Rational(-1,8),
            D2:sp.Rational(1,13),K2:sp.Rational(1,11)}
    assert shift['zprime'].subs(values)!=0
    assert shift['zsecond'].subs(values)!=0
    assert sp.simplify(shift['z'].subs(values)-2/sp.sqrt(13))==0


def test_center_parity_proves_shift_second_radial_jet_vanishes_linearly(shift):
    x=shift['center'];r,s=sp.symbols('r s',positive=True)
    assert sp.simplify(x['zsecond']-r*(6*sp.diff(x['w'],s)+4*s*sp.diff(x['w'],s,2)))==0
    assert not x['zsecond'].has(1/r)


def test_shift_second_derivative_requires_D_and_K_second_jets(shift):
    assert sp.diff(shift['zsecond'],shift['Dsecond'])==shift['K']**2/(shift['D']**2+shift['K']**2)**sp.Rational(3,2)
    assert sp.diff(shift['zsecond'],shift['Ksecond'])==-shift['D']*shift['K']/(shift['D']**2+shift['K']**2)**sp.Rational(3,2)


def test_step58_second_lapse_jets_still_cancel_on_physical_primaries(cert):
    c=highest_lapse_certificate()
    assert c['M2_on_Fz_shell']==0 and c['N2_and_M2_vanish_on_Fz_and_Hg']
    assert len(cert['actual']['N1'])==1 and len(cert['actual']['M0'])==3


def test_third_jet_dependence_not_removable_by_pointwise_Fz_alone(cert):
    assert cert['actual']['N1']['Sg']!=0
    assert cert['actual']['M0']['pLg']!=0
    # Further constraints and their radial prolongations have NOT been used.
    assert 'NOT imposed' in cert['claim']


def test_manifest_does_not_claim_lapse_fixing_or_ghost_freedom():
    m=manifest()
    assert m['Dirac_rank']=='NOT_COMPUTED'
    assert m['lapse_fixing']=='NOT_COMPUTED'
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'


def test_Nprime_high_field_jets_exactly_match_differentiated_Hg_primary():
    from numerics.hr_step59_third_jet_gate import constraint_prolongation_principal
    x=constraint_prolongation_principal()
    cert=third_jet_certificate()
    assert set(x['Hg_prime_third_principal'])=={'Sg'}
    assert sp.cancel(cert['actual']['N1']['Sg']-
                     x['Nprime_relative_Hg_prime']*x['Hg_prime_third_principal']['Sg'])==0


def test_M_high_field_jets_exactly_match_differentiated_true_secondary():
    from numerics.hr_step59_third_jet_gate import constraint_prolongation_principal
    x=constraint_prolongation_principal()
    cert=third_jet_certificate()
    assert set(x['Cred_prime_third_principal'])=={'pLg','Sg','tg'}
    for key,val in x['Cred_prime_third_principal'].items():
        assert sp.cancel(cert['actual']['M0'][key]-x['M_relative_Cred_prime']*val)==0


def test_prolongation_identity_only_principal_not_false_full_rank_claim():
    from numerics.hr_step59_third_jet_gate import constraint_prolongation_principal
    x=constraint_prolongation_principal()
    assert 'ONLY third' in x['exact_scope']
    assert x['constraint_derivative_required']=='Hg_prime=0 and C_red_prime=0 along an exact radial solution'

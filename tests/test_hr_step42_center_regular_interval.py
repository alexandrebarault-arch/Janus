"""Step42 restricted centre-parity and exact-rational interval controls."""
from fractions import Fraction as F
from pathlib import Path
import json, math
import pytest
from numerics.hr_step42_center_regular_interval import (
    Interval, A, B, Y, M2, MG2, MF2, BETA, CG, CF, Z, THETA_G,
    THETA_F, RMAX, STEP41_COEFFICIENT_SHA256, actual_coefficients,
    reference_h2,canonical_regularized,certify_center_and_dust,report)


@pytest.fixture(scope='module')
def step41_path():
    return Path(__file__).resolve().parents[1]/'research/reports/gate2b-step41-report.json'

@pytest.fixture(scope='module')
def coeffs(step41_path):return actual_coefficients(step41_path)

@pytest.fixture(scope='module')
def cert(coeffs):return certify_center_and_dust(coeffs,256)


def midpoint(interval):return float((interval.lo+interval.hi)/2)


def direct_original(r,coeffs):
    """Separate numerical original non-IBP spherical ADM canonical reconstruction.

    Calculate pLi, pLi', S', 3-curvature, Dg, HR potentials, dust p_i and pSi
    WITHOUT the interval-regularized equations. At r>0 it must agree.
    """
    r=float(r);s=r*r;a=float(A);b=float(B)
    b0,b1,b2,b3,b4=map(float,BETA)
    m2=float(M2);mg=float(MG2);mf=float(MF2)
    H=math.sqrt(float(reference_h2()))
    P_g=-2*a*a*H
    P_f=-2*mf*b*a*H
    def metric(ai,c,Pi,ds):
        u=1+c*s
        L=ai*u*u; S=r*L;Spr=ai*u*(1+5*c*s)
        q=Pi+sum(float(ds[k])*s**k for k in range(len(ds)))
        ph=Pi*(1+2.5*c*s)+sum(float(d)*(s**k/(k+1)+5*c*s**(k+1)/(k+2)) for k,d in enumerate(ds))
        pL=s*ph; pLp=2*r*(1+5*c*s)*q
        R3=-48*c/(ai*ai*u**5)
        return L,S,Spr,pL,pLp,R3
    gl,gS,gSp,gpL,gpLp,gR=metric(a,float(CG),P_g,())
    fl,fS,fSp,fpL,fpLp,fR=metric(b,float(CF),P_f,coeffs[::2])
    At=b1*gS*gS+2*b2*gS*fS+b3*fS*fS
    A0=b0*gS*gS+2*b1*gS*fS+b2*fS*fS
    Af=b2*gS*gS+2*b3*gS*fS+b4*fS*fS
    z=float(Z)*r; root=math.sqrt(1-z*z)
    K=m2*mg*gl*fl*At
    D=K*z/root
    Wg=m2*mg*(gl*A0+fl*At*root)
    Wf=m2*mg*(fl*Af+gl*At*root)
    def source(L,S,Sp,pL,pLp,R3,mi,k,Dsector,Wi):
        phasep=k*r*L
        fac=pL/(2*mi*S*Sp)
        kin=L*pL*pL/(4*mi*S*S)
        pot=-mi*L*S*S*R3/2
        const=kin-fac*(Dsector+L*pLp)+pot+z*D/L+Wi
        coefficient=math.sqrt(1+(phasep/L)**2)+fac*phasep
        p=-const/coefficient
        pS=(Dsector+L*pLp-p*phasep)/Sp
        residual=kin-pL*pS/(2*mi*S)+pot+p*math.sqrt(1+(phasep/L)**2)+z*D/L+Wi
        return p,pS,residual
    pg,pSg,Hg=source(gl,gS,gSp,gpL,gpLp,gR,mg,float(THETA_G),D,Wg)
    pf,pSf,Hf=source(fl,fS,fSp,fpL,fpLp,fR,mf,float(THETA_F),-D,Wf)
    return {'pg_over_r2':pg/s,'pf_over_r2':pf/s,'pLg_over_r2':gpL/s,
            'pLf_over_r2':fpL/s,'pSg_over_r':pSg/r,'pSf_over_r':pSf/r,
            'Dg_over_r3':D/r**3,'K_over_r2':K/s,
            'primaries':(Hg,Hf)}


def test_authenticated_coefficient_sha_handles_json_integer_zeros(step41_path,coeffs):
    assert STEP41_COEFFICIENT_SHA256=='bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d'
    assert len(coeffs)==9 and all(coeffs[i]==0 for i in (1,3,5,7))
    assert max(abs(coeffs[i]) for i in (0,2,4,6,8))<F('0.0016')
    assert json.loads(step41_path.read_text())['actual_f_delta'][1]==0


def test_corrupt_report_coefficient_is_rejected(step41_path,tmp_path):
    d=json.loads(step41_path.read_text())
    d['actual_f_delta'][2]+=1e-7
    p=tmp_path/'tampered.json';p.write_text(json.dumps(d))
    with pytest.raises(ValueError,match='digest'):
        actual_coefficients(p)


def test_odd_parity_tampering_fails_closed_even_with_modified_hash(step41_path,tmp_path):
    import hashlib
    d=json.loads(step41_path.read_text())
    d['actual_f_delta'][1]=1e-7
    canonical=json.dumps([float(c) for c in d['actual_f_delta']],separators=(',',':'))
    d['coefficients_sha256']=hashlib.sha256(canonical.encode()).hexdigest()
    p=tmp_path/'tampered.json';p.write_text(json.dumps(d))
    with pytest.raises(ValueError):actual_coefficients(p)


def test_interval_arithmetic_never_under_bounds_sqrt():
    sq=Interval.point(2).sqrt()
    assert sq.lo**2<=2<=sq.hi**2
    assert (Interval(F(-1),F(2))**2)==Interval(F(0),F(4))
    assert Interval(F(-1),F(2))*Interval(F(-2),F(3))==Interval(F(-4),F(6))
    with pytest.raises(ValueError): Interval(F(-1),F(2)).reciprocal()
    with pytest.raises(ValueError): Interval.point(-1).sqrt()


def test_actual_coefficient_continuum_dust_bound_improved(cert):
    mins=cert['strict_positive_lower_exact']
    assert F(mins['pg_over_r2'])>F('.885')
    assert F(mins['pf_over_r2'])>F('.1114') # vs .039 in prior 5-coeff ball
    assert cert['cells']==256 and cert['domain_r'][1]==str(RMAX)


def test_curved_chart_dust_coefficient_and_shift_factors_nonzero(cert):
    mins=cert['strict_positive_lower_exact']
    for name in ('J','K_over_r2','shift_root','dust_beta_g','dust_beta_f','Sprime_g','Sprime_f'):
        assert F(mins[name])>0
    assert F(mins['J'])>F('.659')
    assert F(mins['K_over_r2'])>F('.229')


def test_canonical_center_normalized_momenta_finite(cert):
    for name,v in cert['finite_signed_bounds_float'].items():
        assert len(v)==2 and all(math.isfinite(t) for t in v)
        assert abs(v[0])<10 and abs(v[1])<10
    # pL=r²*analytic(s), pS=r*analytic(s), Dg=r³*analytic(s)
    assert cert['centre_parity']['pS_i'].startswith('r times')


@pytest.mark.parametrize('r',('.025','.043','.1','.43','.75','.85'))
def test_against_original_unsimplified_primary_hamiltonians(r,coeffs):
    v=canonical_regularized(Interval.point(F(r)**2),coeffs)
    independent=direct_original(r,coeffs)
    for name,val in independent.items():
        if name=='primaries':
            assert max(abs(x) for x in val)<1e-13
        else:
            assert abs(val-midpoint(v[name]))<2e-11,(r,name,val,midpoint(v[name]))


def test_center_analytic_limits_exist_and_are_finite(coeffs):
    vals=canonical_regularized(Interval.point(0),coeffs)
    assert vals['pg_over_r2'].lo>0 and vals['pf_over_r2'].lo>0
    assert vals['pSg_over_r'].lo>F(-10)
    assert vals['pSf_over_r'].hi<F(10)
    assert vals['K_over_r2'].lo>0
    # geometric K(r)=r² K/r² vanishes at r=0 (coordinate factor)
    assert 0*vals['K_over_r2'].lo==0


def test_cover_refinement_strengthens_lower_bound(coeffs):
    bound64=certify_center_and_dust(coeffs,64)['strict_positive_lower_exact']
    bound128=certify_center_and_dust(coeffs,128)['strict_positive_lower_exact']
    bound256=certify_center_and_dust(coeffs,256)['strict_positive_lower_exact']
    assert F(bound64['pf_over_r2'])<F(bound128['pf_over_r2'])<F(bound256['pf_over_r2'])


def test_no_exact_local_secondary_or_full_dirac_claim(cert):
    assert 'pointwise exact C_local=0' in cert['not_proved']
    assert 'full Dirac time preservation' in cert['not_proved']
    assert cert['GATE_2B']=='OPEN' and cert['JANUS_R']=='NOT_VALIDATED'


def test_invalid_interval_and_bad_cover_are_rejected(coeffs):
    with pytest.raises(ValueError):canonical_regularized(Interval(F(-1),F(0)),coeffs)
    with pytest.raises(ValueError):canonical_regularized(Interval(F(0),RMAX**2+F('1/1000')),coeffs)
    with pytest.raises(ValueError):certify_center_and_dust(coeffs,2)

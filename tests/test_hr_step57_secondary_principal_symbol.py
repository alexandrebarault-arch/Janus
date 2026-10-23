"""Step57 exact six-pair physical SECOND-jets and eta'' pullback controls.

Uses byte-original Step45 source and never asserts complete Dirac preservation.
"""
import shutil
import sympy as sp
import pytest
from numerics.hr_step57_secondary_principal_symbol import (
    authenticated_step45,physical_principal_symbol,abstract_pullback_coefficients,
    SOURCE_SHA,manifest)

@pytest.fixture(scope='module')
def physical():
    return physical_principal_symbol()


def test_authentic_original_sixpair_git_blob():
    src=authenticated_step45()
    assert len(src['Q'])==12
    assert src['residuals'] and all(x==0 for x in src['residuals'].values())


def test_physical_C_explicit_zprime_coefficient_is_not_zero(physical):
    assert physical['C_zprime']!=0
    assert sp.diff(physical['C_zprime'],
            authenticated_step45()['parameters'][-2])==0


def test_physical_C_zprime_off_shell_shift_constraint_factorization(physical):
    src=authenticated_step45();z=src['parameters'][-3]
    q=dict(zip(src['Q'],src['q']))
    root=sp.sqrt(1-z*z);Lg,Lf=q['Lg'],q['Lf']
    K=physical['K'];Fz=physical['Fz']
    residual=sp.cancel(sp.together(physical['C_zprime']+
                (K/root+z*Fz)/(Lg*Lf)))
    assert residual==0


def test_all_twelve_physical_second_canonical_jet_coefficients(physical):
    b=physical['second_jet_coefficients']
    assert len(b)==12
    assert {k for k,v in b.items() if v!=0}=={'pLg','Sg','tg'}
    q=dict(zip(authenticated_step45()['Q'],authenticated_step45()['q']))
    Lg,Lf=q['Lg'],q['Lf'];K=physical['symbols']['K'];R=physical['symbols']['R']
    assert sp.cancel(b['pLg']-K*K/(Lf*R*R))==0
    assert sp.cancel(b['Sg']+q['pSg']*K*K/(Lg*Lf*R*R))==0
    assert sp.cancel(b['tg']+q['pg']*K*K/(Lg*Lf*R*R))==0


def test_second_jet_eta_second_derivative_M_nonzero_exact(physical):
    q=dict(zip(authenticated_step45()['Q'],authenticated_step45()['q']))
    Lg,Lf=q['Lg'],q['Lf'];K=physical['symbols']['K'];R=physical['symbols']['R']
    assert physical['eta2_M_coefficient']==-K*K/(Lg*Lf*Lf*R)
    # K,Lg,Lf,R positive => coefficient strictly negative, not zero.
    assert physical['eta2_M_coefficient'].subs({K:3,Lg:2,Lf:4,R:5})==sp.Rational(-9,160)


def test_eta_second_derivative_Nprime_exact_and_sign(physical):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']));qp=dict(zip(p['Q'],p['dq']))
    Mg=p['parameters'][0];Lg,Lf=q['Lg'],q['Lf'];Sg=q['Sg'];K=physical['symbols']['K'];R=physical['symbols']['R']
    expected=-2*Mg*Sg*qp['Sg']*K*K/(Lg*Lg*Lf*R*R)
    assert sp.cancel(physical['eta2_Nprime_coefficient']-expected)==0


def test_actual_six_pair_H_euler_jet_contractions(physical):
    T=physical['eta2_Euler_H_contractions'];p=authenticated_step45()
    q=dict(zip(p['Q'],p['q']));qp=dict(zip(p['Q'],p['dq']))
    Lg,Lf=q['Lg'],q['Lf'];Mg=p['parameters'][0]
    assert sp.cancel(T['N1']-2*Mg*q['Sg']*qp['Sg']/Lg)==0
    for key in ('N2','M1','M2'):
        assert T[key]==0
    assert sp.cancel(T['M0']+(Lg*Lf)*physical['C_zprime']/Lf)==0


def test_source_exact_C_has_no_fixed_shift_second_canonical_jets(physical):
    p=authenticated_step45()
    assert not physical['original_C'].free_symbols.intersection(set(p['ddq']))
    assert physical['C_zprime']!=0
    # Eliminating derivative-dependent shift creates exactly 3 nonzero q''s.
    assert len([a for a in physical['second_jet_coefficients'].values() if a!=0])==3


def test_eta_pullback_formula_against_direct_second_order_euler():
    # Independent exact jet toy, testing COMPLETE eta0/eta1/eta2 pullback.
    x=sp.symbols('x',real=True)
    q,p,eta=(sp.Function(t)(x) for t in ('q','p','eta'))
    qr=sp.diff(q,x);pr=sp.diff(p,x);qrr=sp.diff(qr,x);prr=sp.diff(pr,x)
    Z=q+p*qr+pr*pr
    Zr=sp.diff(Z,x)
    u,v,w,t,z,zr=sp.symbols('u v w t z zr')
    C=u**2+w*v+z**2*v+zr*(u+v+w+t)
    replace={u:q,v:qr,w:p,t:pr,z:Z,zr:Zr}
    density=eta*C.subs(replace)
    for field,fieldprime,sym,symprime in ((q,qr,u,v),(p,pr,w,t)):
        A=sp.diff(C,sym).subs(replace)
        B=sp.diff(C,symprime).subs(replace)
        Cz=sp.diff(C,z).subs(replace)
        F=sp.diff(C,zr).subs(replace)
        Zq=sp.diff(Z,field)
        Zqp=sp.diff(Z,fieldprime)
        pull=abstract_pullback_coefficients(A,B,Cz,F,Zq,Zqp,
                                             lambda h:sp.diff(h,x))
        by_formula=sum(sp.diff(eta,x,j)*pull[j] for j in (0,1,2))
        direct=sp.diff(density,field)-sp.diff(sp.diff(density,fieldprime),x)
        direct+=sp.diff(sp.diff(density,sp.diff(fieldprime,x)),x,2)
        assert sp.simplify(sp.expand(by_formula-direct))==0
        assert pull[2]!=0


def test_frozen_shift_omits_eta_double_prime_term(physical):
    C=physical['original_C'];p=authenticated_step45()
    assert all(sp.diff(C,v)==0 for v in p['ddq'])
    assert any(v!=0 for v in physical['second_jet_coefficients'].values())


def test_positive_K_stationary_symbol_is_finite_at_nonzero_chart(physical):
    symbols=physical['symbols']; q=dict(zip(authenticated_step45()['Q'],authenticated_step45()['q']))
    sample={symbols['K']:sp.Rational(3,2),symbols['R']:sp.Rational(5,2),
            q['Lg']:sp.Rational(2),q['Lf']:sp.Rational(4)}
    assert physical['eta2_M_coefficient'].subs(sample)==-sp.Rational(9,320)


def test_manifest_never_claims_full_temporal_result():
    m=manifest()
    assert m['source_blob']==SOURCE_SHA
    assert m['full_eta0_eta1_and_temporal_multiplier_operator']=='NOT_COMPUTED'
    assert m['Dirac_rank']=='NOT_COMPUTED'
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'

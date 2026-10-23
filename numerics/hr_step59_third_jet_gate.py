"""Step59: exact THIRD canonical radial jet gate in the REAL six-pair Dirac-time operator.

Uses authentic original Step45 physical C and Step58 *complete* factored
six-pair temporal bracket. Applies algebraic relative-shift stationarity Fz=0,
not the remaining primaries or their radial prolongations. Demonstrates WHY
pointwise constraint enforcement alone is insufficient to fix lapses:
physical N' and M coefficients retain independent third field derivatives.

Also supplies exact twice-prolonged positive-K shift formula for z,z',z'';
this is a consistency *input* to the still-unresolved full multiplier rank.
"""
from __future__ import annotations
from functools import lru_cache
import sympy as sp
from .hr_step58_temporal_operator import physical_operator, highest_lapse_certificate
from .hr_step57_secondary_principal_symbol import authenticated_step45


@lru_cache(1)
def third_jet_certificate():
    v=physical_operator();p=authenticated_step45()
    q=dict(zip(p['Q'],p['q'])); Lg,Lf,Sg=q['Lg'],q['Lf'],q['Sg']
    z=v['z'];mg=p['parameters'][0]
    sub={p['dq'][1]:highest_lapse_certificate()['shift_elimination_pLg_prime']}
    third=dict(zip(p['Q'],v['qppp']))
    actual={}
    for lapse in ('N','M'):
        for order in (0,1):
            key=f'{lapse}{order}'
            base=v['operator'][lapse][order]
            actual[key]={field:sp.factor(sp.diff(base,j).subs(sub))
                         for field,j in third.items() if base.has(j)}
            actual[key]={k:x for k,x in actual[key].items() if x!=0}
    expected={
        'N0':{},
        'N1':{'Sg':-2*mg*Sg*(1-z*z)/(Lf*Lg**2)},
        'M0':{
            'pLg':z*(1-z*z)/Lf**2,
            'Sg':-q['pSg']*z*(1-z*z)/(Lg*Lf**2),
            'tg':-q['pg']*z*(1-z*z)/(Lg*Lf**2)},
        'M1':{}}
    for key,coefficients in expected.items():
        assert set(actual[key])==set(coefficients),(key,actual[key])
        for field,e in coefficients.items():
            assert sp.cancel(sp.together(actual[key][field]-e))==0,(key,field)

    # The derivative combination is exactly minus (1/Lg) times the
    # THIRD-JET PRINCIPAL part of the twice-differentiated Dg density.
    D2=v['Dt'](v['Dt'](v['Dg']))
    d2principal={k:sp.diff(D2,t) for k,t in third.items() if D2.has(t)}
    assert d2principal=={'pLg':-Lg,'Sg':q['pSg'],'tg':q['pg']}
    alpha=-z*(1-z*z)/(Lg*Lf**2)
    assert all(sp.cancel(actual['M0'][i]-alpha*d2principal[i])==0
               for i in d2principal)
    return {'third':third,'actual':actual,'expected':expected,
            'Dg_second_principal':d2principal,
            'M0_principal_via_Dg_second':alpha,
            'source_original_step45_sha':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
            'claim':'exact on Fz=0 in positive-K chart only; Hg,Hf,Ddiag,C and their prolongations NOT imposed'}


@lru_cache(1)
def constraint_prolongation_principal():
    """Exact leading third-field-jet quotient by differentiated constraints.

    This identity concerns the principal third-jet parts only, not the full
    lower-order coefficients of the temporal multiplier operator.
    """
    t=third_jet_certificate()
    p=authenticated_step45();v=physical_operator()
    q=dict(zip(p['Q'],p['q']));z=v['z'];Lg,Lf=q['Lg'],q['Lf']
    hg_high={name:sp.factor(sp.diff(p['Hg'],second))
             for name,second in zip(p['Q'],v['qpp']) if p['Hg'].has(second)}
    cred_high={'pLg':(1-z*z)/Lf,
               'Sg':-q['pSg']*(1-z*z)/(Lg*Lf),
               'tg':-q['pg']*(1-z*z)/(Lg*Lf)}
    pref_N=-(1-z*z)/(Lg*Lf)
    pref_M=z/Lf
    assert hg_high=={'Sg':2*p['parameters'][0]*q['Sg']/Lg}
    assert set(t['actual']['N1'])==set(hg_high)
    assert set(t['actual']['M0'])==set(cred_high)
    for key,value in hg_high.items():
        assert sp.cancel(t['actual']['N1'][key]-pref_N*value)==0
    for key,value in cred_high.items():
        assert sp.cancel(t['actual']['M0'][key]-pref_M*value)==0
    return dict(Hg_prime_third_principal=hg_high,
                Cred_prime_third_principal=cred_high,
                Nprime_relative_Hg_prime=pref_N,
                M_relative_Cred_prime=pref_M,
                exact_scope='ONLY third canonical radial jet principal; full lapse coefficient remainders NOT reduced',
                constraint_derivative_required='Hg_prime=0 and C_red_prime=0 along an exact radial solution')

@lru_cache(1)
def shift_jet_prolongation():
    """Exact z,z',z'' from D(r),K(r), K>0; no derivative shortcuts."""
    D,K,D1,K1,D2,K2=sp.symbols('D K D1 K1 D2 K2',real=True)
    Kpos=sp.symbols('Kpositive',positive=True)
    R=sp.sqrt(D*D+K*K)
    Z=D/R
    A=K*K*D1-D*K*K1
    Z1=A/R**3
    Aprime=K*K*D2+K*K1*D1-D*K1*K1-D*K*K2
    Z2=Aprime/R**3-3*A*(D*D1+K*K1)/R**5
    def total(expr):
        return sum(sp.diff(expr,var)*new for var,new in
                   [(D,D1),(K,K1),(D1,D2),(K1,K2)])
    assert sp.simplify(total(Z)-Z1)==0
    assert sp.simplify(total(Z1)-Z2)==0
    # Root is K/R on K>0; the stationary relation and its first and
    # second total derivatives are exactly zero.
    root_positive=K/R
    Fz=sp.cancel(D-K*Z/root_positive)
    assert Fz==0 and total(Fz)==0 and total(total(Fz))==0
    # Exact even-center normalized radial parity under D=r³ d(s),
    # K=r² k(s), s=r² and k(s)>0.
    r,s=sp.symbols('r s',positive=True)
    d,k=sp.Function('d')(s),sp.Function('k')(s)
    w=d/sp.sqrt(k*k+s*d*d)
    wr=sp.diff(w,s)
    wrr=sp.diff(wr,s)
    zcenter=r*w
    zcenter1=w+2*s*wr
    zcenter2=r*(6*wr+4*s*wrr)
    # Chain rule d/dr f(r²)=2r f_s
    def Dr_center(expr):
        return sp.diff(expr,r)+2*r*sp.diff(expr,s)
    assert sp.simplify((Dr_center(zcenter)-zcenter1).subs(r**2,s))==0
    assert sp.simplify(Dr_center(zcenter1)-zcenter2)==0
    return dict(D=D,K=K,Dprime=D1,Kprime=K1,Dsecond=D2,Ksecond=K2,
                z=Z,zprime=Z1,zsecond=Z2,positive_K_stationarity_exact=True,
                center=dict(w=w,z=zcenter,zprime=zcenter1,zsecond=zcenter2,
                            note='zsecond/r finite if d,k have two smooth s derivatives and k>0'))


def manifest():
    a=third_jet_certificate();s=shift_jet_prolongation();c=constraint_prolongation_principal()
    return {'step':59,'physical_original_sixpair':True,
            'on_Fz_0_higher_field_jet_sensitivities':{
                key:{field:str(coeff) for field,coeff in values.items()}
                for key,values in a['actual'].items()},
            'M0_third_jet_is_Dg_second_jet':'-z(1-z²)/(Lg Lf²) times Dg_second_high',
            'constraint_prolongation_principal':{
              'Nprime_high':'-(1-z²)/(Lg Lf) * (Hg_prime)_third',
              'M_high':'z/Lf * (C_red_prime)_third',
              'scope':c['exact_scope']},
            'shift_prolonged_to_second_radial_order':'EXACT',
            'shift_zprime':str(s['zprime']),'shift_zsecond':str(s['zsecond']),
            'center_parity':'z=r*w(r²), zprime=w+2s*w_s, zsecond=r*(6w_s+4s*w_ss)',
            'warning':'Nonzero third-field-jet sensitivities do NOT establish lapse rank. Need exact Step55 profile jets, full first-order N,Nprime,M,Mprime and constraint prolongations.',
            'Dirac_rank':'NOT_COMPUTED','lapse_fixing':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

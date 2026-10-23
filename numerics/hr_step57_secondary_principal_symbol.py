"""Step57: exact SECOND-JET and smeared-test principal symbols of true HR C_red.

Uses BYTE-AUTHENTIC Step45 six-pair positive-EH two-dust local secondary C.
The original C(q,q',z,z') has C_z' != 0. After eliminating the relative
shift z= Dg/sqrt(Dg**2+K**2) (K>0), the true reduced local secondary depends
on q'' even though the original fixed-z representative did not. Hence
Euler gradients of int eta*C_red contain eta'' terms. These terms MUST be
included in the temporal Dirac bracket. Results are only a highest-eta-jet
symbol and exact pullback rule, NOT full multiplier rank/time preservation.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
from functools import lru_cache
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward

SOURCE_SHA='66aa43841dccfe4a5d586a49be9c10af3a67a10e'

def authenticated_step45():
    raw=Path(__file__).with_name('hr_step45_exact_physical_ward.py').read_bytes()
    sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
    if sha!=SOURCE_SHA:
        raise ValueError('Original Step45 physical 6-pair source mismatch: '+sha)
    return exact_physical_ward()

@lru_cache(1)
def physical_principal_symbol():
    p=authenticated_step45()
    q=dict(zip(p['Q'],p['q'])); qp=dict(zip(p['Q'],p['dq']))
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=p['parameters']
    Lg,Lf,Sg,Sf=q['Lg'],q['Lf'],q['Sg'],q['Sf']
    D=q['pSg']*qp['Sg']-Lg*qp['pLg']+q['pg']*qp['tg']
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    K=m2*mg*Lg*Lf*At
    root=sp.sqrt(1-z*z)
    Fz=D-K*z/root
    C=p['C_exact']
    Czprime=sp.diff(C,zr)
    assert sp.cancel(sp.together(Czprime+(K*root+D*z)/(Lg*Lf)))==0
    assert sp.diff(Czprime,zr)==0
    assert sp.cancel(sp.together(Czprime+K/(Lg*Lf*root)+z*Fz/(Lg*Lf)))==0

    # z(D,K) Frechet derivative on K>0; R positive.  Keep (D,K)
    # symbolic rather than dubious sqrt cancellations with unconstrained K.
    DS,KS,R=sp.symbols('D K R',real=True,positive=True)
    ZD=KS**2/R**3
    # On Fz=0, R=sqrt(D²+K²) and root=K/R (K>0).
    C_zprime_shell=-R/(Lg*Lf)
    Bbase=sp.factor(C_zprime_shell*ZD)
    assert Bbase==-KS**2/(Lg*Lf*R**2)
    Bsecond={k:sp.Integer(0) for k in p['Q']}
    for k,v in [('pLg',-Lg),('Sg',q['pSg']),('tg',q['pg'])]:
        Bsecond[k]=sp.factor(Bbase*v)
    # Exact second-jet chain pullback: C_red(q,q',q'') =
    # C(q,q',z(q,q'), z_r(q,q',q'')); only D has q' dependence,
    # because interaction K contains no canonical first derivatives.
    expected={
      'pLg':Lg*KS**2/(Lg*Lf*R**2),
      'Sg':-q['pSg']*KS**2/(Lg*Lf*R**2),
      'tg':-q['pg']*KS**2/(Lg*Lf*R**2)}
    for key,value in expected.items():
        assert sp.simplify(Bsecond[key]-value)==0

    # CONTRACT with REAL ORIGINAL six-pair Hamiltonian Euler jets.
    # In {int eta C_red, H[N,M]}, the eta'' coefficient for each lapse
    # jet is sum_a (B_q[a] E_H,p[a] - B_p[a] E_H,q[a]).
    # For this special B it equals Bbase*(Lg E_H,Lg + pSg E_H,pSg + pg E_H,pg).
    contractions={}
    for sector,eu in [('N',p['eg']),('M',p['ef'])]:
        for order in range(3):
            T=sp.cancel(sp.together(Lg*eu[order][0]+q['pSg']*eu[order][3]
                                   +q['pg']*eu[order][5]))
            contractions[f'{sector}{order}']=T
    independent_identity={
      'N1':2*mg*Sg*qp['Sg']/Lg,
      'N2':sp.Integer(0),
      'M0':(K*root+D*z)/Lf,
      'M1':sp.Integer(0),
      'M2':sp.Integer(0)}
    for key,rhs in independent_identity.items():
        assert sp.cancel(sp.together(contractions[key]-rhs))==0,(key,contractions[key])
    # On Fz=0 and R>0, the coefficient of eta'' multiplying M is
    # Bbase*(R/Lf) = -K²/(Lg Lf² R), nonzero if chart Lg,Lf,K>0.
    actual_eta2_M=sp.factor(Bbase*(R/Lf))
    assert sp.simplify(actual_eta2_M+KS**2/(Lg*Lf**2*R))==0
    # Corresponding N' coefficient is Bbase*(2 Mg² Sg Sg'/Lg).
    actual_eta2_Nprime=sp.factor(Bbase*2*mg*Sg*qp['Sg']/Lg)
    assert sp.simplify(actual_eta2_Nprime+
                       2*mg*Sg*qp['Sg']*KS**2/(Lg**2*Lf*R**2))==0
    # N0 remains explicit and depends on physical local momenta/dust,
    # but all N'' and M',M'' eta'' coefficients vanish identically.
    return {'Q':p['Q'],'original_C':C,'Dg':D,'K':K,'Fz':Fz,
            'C_zprime':Czprime,'C_zprime_stationary':C_zprime_shell,
            'second_jet_coefficients':Bsecond,
            'eta2_Euler_H_contractions':contractions,
            'eta2_M_coefficient':actual_eta2_M,
            'eta2_Nprime_coefficient':actual_eta2_Nprime,
            'eta2_N_coefficient':sp.factor(Bbase*contractions['N0']),
            'symbols':{'D':DS,'K':KS,'R':R},
            'certified_conditions':'K>0,Lg>0,Lf>0,R=sqrt(Dg²+K²)>0,Fz=0; compact lapse/eta tests'}


def abstract_pullback_coefficients(A,B,Cz,F,Zq,Zqp,D):
    """Exact Euler coefficient of eta^0,eta^1,eta^2 for one field.

    Input A=C_q|z fixed, B=C_q'|z fixed, Cz=C_z, F=C_z',
    Zq=dz/dq, Zqp=dz/dq' and D=FULL total radial derivative.
    All input expressions must be evaluated on the eliminated shift shell
    AFTER the required external derivatives have been taken.
    Formula R= eta*C_q - (eta*C_q')' + T*Zq - (T*Zqp)',
    T=eta*Cz-(eta*F)'. There may be higher q-jets in coefficient D(D(F)).
    """
    return {
      2:sp.expand(Zqp*F),
      1:sp.expand(-B-Zq*F+D(Zqp)*F-Zqp*Cz+2*Zqp*D(F)),
      0:sp.expand(A-D(B)+(Zq-D(Zqp))*(Cz-D(F))-
                  Zqp*D(Cz-D(F)))
    }


def manifest():
    x=physical_principal_symbol()
    return {'step':57,'source':'authentic original Step45 full 6-pair C',
      'source_blob':SOURCE_SHA,'C_zprime_exact':'-(K*sqrt(1-z²)+Dg*z)/(Lg*Lf)',
      'C_zprime_on_Fz_zero':'-R/(Lg*Lf), R=sqrt(Dg²+K²), K>0',
      'C_red_second_jet_nonzero':True,
      'nonzero_second_canonical_jets':{'pLg_rr':'K²/(Lf*R²)',
          'Sg_rr':'-pSg*K²/(Lg*Lf*R²)',
          'tg_rr':'-pg*K²/(Lg*Lf*R²)'},
      'physical_eta_second_derivative_M_coefficient':'-K²/(Lg*Lf²*R)',
      'physical_eta_second_derivative_Nprime_coefficient':'-2 Mg² Sg Sg_prime K²/(Lg² Lf R²)',
      'physical_eta_second_derivative_Nprimeprime_and_Mprime_Mprimeprime':'EXACT_ZERO',
      'physical_eta_second_derivative_N_coefficient':'COMPUTED_SYMBOLICALLY_NOT_SIMPLIFIED',
      'full_eta0_eta1_and_temporal_multiplier_operator':'NOT_COMPUTED',
      'Dirac_rank':'NOT_COMPUTED','lapse_fixing':'NOT_COMPUTED',
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

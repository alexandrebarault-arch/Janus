"""Exact radial jet lifting for the Step55 constrained initial-data ODE.

This is a rigorously symbolic bridge, NOT an execution of the original
six-pair temporal operator on Step55 data.  The REAL Step55 radial ODE is
2*s*U_s=G(s,U)-2U, P=pLf=r**2 U(r**2), with G(0,U)=3 U0-U.

It supplies chain-consistent P'',P''' and z',z'' formulas, an exact
center Frobenius recursion, and a necessary warning: bounds on U and
P'/r alone do NOT control higher derivatives. To evaluate Step60 one
must supply derivatives of the actual original physical G(s,U).
"""
from functools import lru_cache
from fractions import Fraction as F
import sympy as sp

STEP55_SOURCE_GIT_BLOB='a54a6acf2f7ad2f64c500faecfa1406ecbf7b862'
STEP60_SOURCE_GIT_BLOB='9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509'
S_MAX=F('0.7225');R_MAX=F('0.85')
U_TUBE=F('0.0001');V_TUBE=F('0.00205')

@lru_cache(None)
def ode_jet_formulas():
    s,U,r=sp.symbols('s U r',real=True)
    G=sp.Function('G')(s,U)
    Phi=G-2*U
    Us=Phi/(2*s)
    H=sp.factor(G+2*s*sp.diff(G,s)+Phi*sp.diff(G,U))
    Hs=sp.diff(H,s)
    Hu=sp.diff(H,U)
    Pprime=r*G
    Psecond=H
    Pthird=2*r*(Hs+Hu*Us)
    # Check both forms against a formal solution U(r²) whose first
    # derivative is constrained by the ODE, not an arbitrary U.
    u=sp.Function('u')(s)
    P=r**2*u
    radial_sub={r*r:s}
    first=sp.diff(P,r)+2*r*sp.diff(P,s)
    first=sp.expand(first.subs(sp.diff(u,s),Us.subs(U,u)))
    assert sp.simplify(sp.factor((first-Pprime.subs(U,u))/r).subs(radial_sub))==0
    second=sp.diff(P,r,2)+4*r*sp.diff(P,r,s)+4*r*r*sp.diff(P,s,2)+2*sp.diff(P,s)
    assert sp.simplify((second-(2*u+10*s*sp.diff(u,s)+4*s*s*sp.diff(u,s,2))).subs(radial_sub))==0
    # Differentiate P' along constrained ODE, using full G_s and G_U:
    alongG=2*r*(sp.diff(G,s)+sp.diff(G,U)*Us)
    assert sp.simplify((G+r*alongG-H).subs(r*r,s))==0
    alongH=2*r*(sp.diff(H,s)+sp.diff(H,U)*Us)
    assert sp.simplify(Pthird-alongH)==0
    return dict(s=s,U=U,r=r,G=G,Pprime=Pprime,Psecond=Psecond,
                Pthird=Pthird,Phi=Phi,Us=Us,H=H,
                formulas='Pprime=rG; Psecond=G+2s G_s+(G-2U)G_U; Pthird=2r(H_s+H_U*(G-2U)/(2s))')


def center_frobenius_recurrence(degree=5):
    """FORMAL nonresonant coefficient-extraction rule for the Step55 center.

    G(s,U)=3U0-U+s*A(s,U). If a_(n-1) denotes the coefficient of
    s^(n-1) in the COMPOSED series A(s,U(s)), then
       u_n=a_(n-1)/(2n+3).
    It is a recurrence specification, NOT an evaluation of the actual
    physical Step55 A or the nontrivial composite coefficients. Higher
    coefficients must be evaluated after supplying the physical A.
    """
    if not 1<=degree<=100:raise ValueError('degree 1..100')
    s,u0=sp.symbols('s u0',real=True)
    composed_coefficient_symbols=sp.symbols('a0:'+str(degree))
    coefficients={n:composed_coefficient_symbols[n-1]/(2*n+3)
                  for n in range(1,degree+1)}
    return dict(degree=degree,coefficients=coefficients,
                formal_polynomial=u0+sum(coefficients[n]*s**n for n in coefficients),
                resonance_denominators=[2*n+3 for n in range(1,degree+1)],
                not_own_physical_coefficients=True)


def center_coefficients_from_G_jets():
    gs,gss,gsu,u0=sp.symbols('G_s G_ss G_sU U0')
    u1=gs/5
    u2=(gsu*u1+gss/2)/7
    return dict(U0=u0,U1=u1,U2=u2,
                P_second_center=2*u0,
                P_third_over_r_center=24*u1,
                condition='G(0,U)=3U0-U on the radial normalized chart')


def certified_position_momentum_enclosures():
    """Use ACTUAL Step55 proven rational U and V tube, not a sample."""
    return dict(r_interval=(F(0),R_MAX),s_interval=(F(0),S_MAX),
                bound_P_minus_Pstar=S_MAX*U_TUBE,
                bound_Pprime_minus_Pstar_prime=R_MAX*V_TUBE,
                bound_Psecond='NOT FROM U,V TUBE ALONE; NEED G_s,G_U',
                bound_Pthird='NOT FROM U,V TUBE ALONE; NEED G_ss,G_sU,G_UU',
                strict=True)


def shift_second_jet_consistency():
    """Diagnose exact missing zr=Z1 substitution in Step60 Z2 evaluation.

    Step60 correctly builds Z2 with externally-independent zr symbol;
    for PHYSICAL radial evaluation, zr MUST be replaced by Z1. The
    un-substituted lower-jet remainder is NOT YET the physical value.
    """
    z,zr,D1,K1,K=sp.symbols('z zr D1 K1 K',real=True)
    root=sp.sqrt(1-z*z)
    ZD=root**3/K
    ZK=-z*(1-z*z)/K
    Z1=ZD*D1+ZK*K1
    # Difference from evaluating Dt(ZD), Dt(ZK) with external zr.
    defect=sp.factor((zr-Z1)*(sp.diff(ZD,z)*D1+sp.diff(ZK,z)*K1))
    explicit=(zr-Z1)*(-3*z*root*D1+(3*z*z-1)*K1)/K
    assert sp.simplify(defect-explicit)==0
    assert sp.factor(defect.subs(zr,Z1))==0
    assert defect!=0
    return dict(z=z,zr=zr,K=K,D1=D1,K1=K1,ZD=ZD,ZK=ZK,Z1=Z1,
                defect_Z2_unsubstituted=defect,
                defect_explicit=explicit,
                fix='Substitute zr=Z1 in Step60 Z2 and all lower-jet temporal residuals before evaluating on Step55',
                qrrr_cancellation_unaffected=True)


def manifest():
    x=ode_jet_formulas();c=center_coefficients_from_G_jets();t=certified_position_momentum_enclosures();z=shift_second_jet_consistency()
    return {'step':61,'original_step55_source_sha_reference':STEP55_SOURCE_GIT_BLOB,
        'original_step60_source_sha_reference':STEP60_SOURCE_GIT_BLOB,
        'original_imported_in_this_standalone_run':False,
        'ODE':'2s U_s=G(s,U)-2U; P(r)=r² U(r²); G(0,U)=3U0-U',
        'Pprime':str(x['Pprime']),'Psecond':str(x['Psecond']),
        'Pthird':str(x['Pthird']),'center_U1':str(c['U1']),'center_U2':str(c['U2']),
        'exact_Step55_tube_implies_P_abs_error_le':str(t['bound_P_minus_Pstar']),
        'exact_Step55_tube_implies_Pprime_abs_error_le':str(t['bound_Pprime_minus_Pstar_prime']),
        'Psecond_and_Pthird_bounds':'NOT CERTIFIED WITHOUT PHYSICAL G DERIVATIVES',
        'Step60_external_zr_consistency_defect':str(z['defect_explicit']),
        'Step60_zr_substitution_needed':True,
        'full_physical_step60_operator_evaluated_on_exact_step55_profile':False,
        'Dirac_rank':'NOT_COMPUTED','lapse_fixing':'NOT_COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

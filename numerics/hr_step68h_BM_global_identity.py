"""Step68h: exact full six-pair temporal Mprime identity on Fz=0.

The original Step58 B_M=[Cdot]_{M'} obeys
 B_M = 3*z*(z**2-1)/(Lg*Lf**2) * d_r(Fz)
on the algebraic shift-shell Fz=0, K>0. This is proved with no global
Step55 trajectory, no sampling, no Hg/Hf/C constraints, and no lapse ratio.

Proof path: authenticate Step45/57/58, use verified Step68g full Fzprime
quotient to eliminate ALL second canonical jets, differentiate the
remaining expression exactly w.r.t. its 24 independent symbols, prove every
rational numerator zero, and evaluate an exact rational non-singular chart
reference point to fix the constant of integration to zero. Symbolic
rational numerator identities are global where algebraic factors are defined.
"""
from functools import lru_cache
import sympy as sp
from .hr_step68g_full_Cdot_Mprime_quotient import second_jet_quotient,authenticate


@lru_cache(1)
def full_original_BM_identity():
    git_blobs=authenticate()
    q=second_jet_quotient()
    r=q['representative_qsecond_free']
    symbols=sorted(r.free_symbols,key=str)
    assert len(symbols)==24
    partials={}
    for variable in symbols:
        expr=sp.diff(r,variable)
        if expr==0:
            partials[str(variable)]='ZERO_RAW'
        else:
            numerator,denominator=sp.fraction(sp.together(expr))
            assert denominator!=0
            assert sp.expand(numerator)==0,('nonzero derivative',variable,numerator)
            partials[str(variable)]='EXACT_NUMERATOR_ZERO'
    # Fix the locally constant analytic rational/radical expression at a
    # non-singular real chart point where the square roots are rational.
    point={x:sp.Rational(1) for x in symbols}
    for x in symbols:
        if x.name=='z':point[x]=sp.Rational(3,5)
        if x.name=='zr':point[x]=sp.Rational(1,10)
        if x.name=='tgr':point[x]=sp.S.Zero
        if x.name=='beta2':point[x]=sp.Rational(-1,2)
    ref=sp.cancel(r.subs(point))
    assert ref==0
    assert all(v==0 for v in q['exact_second_jet_residuals'].values())
    return {'reference_exact_zero':ref,'rational_chart':point,
            'variables_checked':partials,'num_independent_variables':len(symbols),
            'source_git_blobs':git_blobs,
            'lambda':q['lambda'],
            'original_expression':q['raw'],
            'Fz_radial_derivative':q['Fzprime_full'],
            'Fz_shell':q['shell'],
            'statement':'On Fz=0, B_M=3*z*(z²-1)/(Lg Lf²) * Fzprime; on Fz=Fzprime=0, B_M=0',
            'sector':'K>0, |z|<1, Lg,Lf nonzero and regular denominators; positive radical branch'}


def manifest():
    x=full_original_BM_identity()
    return {'step':'68h','source_git_blobs':x['source_git_blobs'],
        'physical_source':'ORIGINAL Step58 Cdot full six canonical pairs',
        'on_Fz0':'B_M=3*z*(z²-1)/(Lg Lf²)*Fzprime',
        'on_Fz_and_Fzprime_zero':'B_M=EXACT_ZERO',
        'independent_partial_derivatives_checked':x['num_independent_variables'],
        'derivative_results':x['variables_checked'],
        'exact_reference_value':str(x['reference_exact_zero']),
        'no_Hg_Hf_C_used_in_BM_identity':True,
        'B_N_on_complete_shell':'NOT_YET_ANALYTICALLY_REDUCED',
        'A_N_A_M_sign_on_global_exact_Step55':'NOT_CERTIFIED',
        'lapse_ratio_global':'NOT_CERTIFIED',
        'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
 import json
 print(json.dumps(manifest(),indent=2))

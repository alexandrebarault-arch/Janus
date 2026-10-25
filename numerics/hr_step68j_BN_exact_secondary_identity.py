"""Step68j: original full six-pair Cdot N' identity on Fz=0.

Prove R_BN == (z/Lg)*C using independent exact numerator-derivative
certificates and a rational reference point. Step68i ALREADY proved the
third and second canonical radial jets vanish in R_BN. This new proof
handles every lower-jet independent symbol. The derivative proof is split
into four reproducible groups to avoid long symbolic runtimes.

Domain: regular K>0, |z|<1 positive shift root, nonzero Lg,Lf,Sg,
nonzero denominators including beta. This is NOT a full 4D Dirac rank,
lapse boundary-value problem, or non-IBP oracle.
"""
from __future__ import annotations
from functools import lru_cache
import hashlib
import sympy as sp
from .hr_step68i_BN_lower_jet_quotient import physical_BN_second_jet_quotient, authenticate
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step60_full_constraint_prolongation import full_constraint_prolongation

GROUPS={
 'canonical_and_gradients':('pLf','pLg','pSf','pSg','pSgr','pg','pgr','Lfr','Lgr','Sfr','Sgr','zr','tgr'),
 'metrics_a':('Sg','Sf'),
 'metrics_b':('Lg','Lf'),
 'couplings_and_z':('Mf2','Mg2','m2','beta0','beta1','beta2','beta3','z'),
}
assert len({s for v in GROUPS.values() for s in v})==25

@lru_cache(1)
def original_remainder():
    authenticate()
    d=physical_BN_second_jet_quotient()
    p=exact_physical_ward(); c=full_constraint_prolongation()
    q=dict(zip(p['Q'],p['q']))
    z=p['parameters'][-3];Lg=q['Lg']
    cred=p['C_exact'].subs(c['stationarity_substitution'])
    reduced=d['representative_qsecond_and_qthird_free']
    remainder=reduced-z/Lg*cred
    names={str(x):x for x in remainder.free_symbols}
    all_symbols={name for group in GROUPS.values() for name in group}
    if set(names)!=all_symbols:
        raise AssertionError('Different lower-jet independent symbols: '+str(set(names)^all_symbols))
    return {'R_BN':reduced,'C_on_Fz':cred,'remainder':remainder,
            'q':q,'z':z,'names':names,'beta':d['beta'],
            'original_sha':d['source_git_blobs']}


def group_certificate(group):
    if group not in GROUPS:raise ValueError('unrecognized derivative group '+str(group))
    a=original_remainder();rem=a['remainder']
    result={}
    for name in GROUPS[group]:
        numerator,den=sp.fraction(sp.together(sp.diff(rem,a['names'][name])))
        if den==0 or sp.expand(numerator)!=0:
            raise AssertionError('NONZERO original Nprime remainder derivative: '+name)
        result[name]='EXACT_NUMERATOR_ZERO'
    return result


def rational_reference():
    a=original_remainder();s=a['names']
    point={sym:sp.S.One for sym in s.values()}
    point[s['z']]=sp.Rational(3,5)
    point[s['zr']]=sp.Rational(1,10)
    point[s['tgr']]=sp.S.Zero
    point[s['beta2']]=sp.Rational(-1,2)
    val=sp.cancel(a['remainder'].subs(point))
    if val!=0:raise AssertionError('R_BN - z/Lg*C nonzero at rational anchor: '+str(val))
    other=sp.cancel(a['C_on_Fz'].subs(point))
    # Reference point must demonstrate C itself has NOT been set zero.
    if other==0:raise AssertionError('reference point accidentally satisfies C=0')
    wrong=sp.diff(a['R_BN']+a['z']/a['q']['Lg']*a['C_on_Fz'],a['q']['pSf'])
    if sp.expand(sp.fraction(sp.together(wrong))[0])==0:
        raise AssertionError('wrong sign should NOT be an identity')
    return {'point':{name:str(point[sym]) for name,sym in s.items()},
            'remainder_exact_zero':str(val),'C_on_Fz_nonzero':str(other),
            'wrong_sign_not_an_identity':True}


def manifest(results):
    expected={name for group in GROUPS.values() for name in group}
    if set(results)!=expected or any(v!='EXACT_NUMERATOR_ZERO' for v in results.values()):
        raise AssertionError('Incomplete 25-derivative proof; no conclusion allowed')
    ref=rational_reference();a=original_remainder()
    return {
        'step':'68j','source':'byte-original Step45/57/58/59/60 six-pair full Cdot',
        'authenticated_sources':a['original_sha'],
        'identity_on_Fz0':'B_N=-(1-z²)/(Lg Lf)*Hgprime + beta*Hg + z/Lg*C',
        'exact_beta_definition':'beta=partial_(Sg'') of [B_N+(1-z²)/(Lg Lf)*Hgprime] / [2 Mg² Sg/Lg]',
        'num_remaining_lower_jet_partials':len(results),'derivatives':results,
        'anchor':ref,'no_second_or_third_jets':'ALREADY_PROVED Step68i, rerun as prerequisite',
        'on_full_Fz_Hg_Hgprime_C_zero':'B_N=0',
        'Bm':'Step68h B_M=3z(z²-1)/(Lg Lf²)*Fzprime => B_M=0 when Fzprime=0',
        'lower_lapse_AN_AM_sign':'NOT_CERTIFIED_GLOBAL',
        'global_lapse_ratio_positive':'NOT_CERTIFIED',
        'independent_nonIBP_oracle':'NOT_COMPUTED',
        'Dirac_rank':'NOT_COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

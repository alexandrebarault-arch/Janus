"""Step68aa: authentic Step67b U3 -> regular ORIGINAL f momentum center jets.

A conditional central Taylor-limit certificate, NOT an interval bound for
r>0 and NOT an original Step58 temporal Dirac or lapse calculation.

The regular analytic Step49 radial branch solves the ORIGINAL Step45/46/55
ODE 2*s*U_s=G(s,U)-2*U and has U(s)=U0+U1*s+U2*s**2+U3*s**3+O(s**4).
This converts rigorously to original canonical pLf(r)=r**2*U(r**2).
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
import sympy as sp
from .hr_step68z_invariant_center_cone import original_reports, tightened_bounds, SOURCES

BLOB68Z_SOURCE='8c3a46b44e5c55c7b8f464668f9e8dc7d17eae8b'
BLOB68Z_REPORT='38f55aabf7a7c47c812f32db684f50ffbaf16374'
LIMIT_MULTIPLIERS = {
    'U_minus_Ustar_over_s3': 1,
    'U_s_minus_Ustar_s_over_s2': 3,
    'U_ss_minus_2U2_over_s': 6,
    'U_sss_at_s0': 6,
    'pLf_minus_r2Ustar_over_r8': 1,
    'pLf_prime_over_r_minus_Vstar_over_s3': 8,
    'pLf_doubleprime_minus_2U0_12U1s_30U2s2_over_s3': 56,
    'pLf_tripleprime_over_r_minus_24U1_120U2s_over_s2': 336,
    'pLf_8th_r_derivative_at_center': 40320,
}


def git_blob(path):
    raw=Path(path).read_bytes()
    return sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def authenticated_inputs(folder):
    folder=Path(folder)
    src=Path(__file__).with_name('hr_step68z_invariant_center_cone.py')
    if git_blob(src) != BLOB68Z_SOURCE:
        raise ValueError('Step68z original code SHA drift')
    filename=folder/'gate2b-step68z-invariant-center-cone.json'
    if git_blob(filename) != BLOB68Z_REPORT:
        raise ValueError('Step68z original certificate SHA drift')
    up=original_reports(folder)  # independently checks all original 68u/v/y blobs
    z=json.loads(filename.read_text())
    a=tightened_bounds(up)
    if not (z['step']=='68z'
            and z['center_invariant_cone_h_equals_U_minus_Ustar_over_s_cubed']==list(map(str,a['h']))
            and z['G_minus_Vstar_over_s_cubed']==list(map(str,a['v']))
            and z['original_blob_shas']=={k:v[1] for k,v in SOURCES.items()}
            and z['GATE_2B']=='OPEN' and z['JANUS_R']=='NOT_VALIDATED'):
        raise ValueError('Step68z report does not match exact rational reconstruction')
    u3lo,u3hi=a['u3']
    if not u3lo <= u3hi < 0:
        raise ArithmeticError('U3 sign not certified')
    # At r=0 the signed Step68z enclosures must contain the analytic limit.
    if not (a['h'][0] <= u3lo <= u3hi <= a['h'][1]
            and a['ds'][0] <= 3*u3lo <= 3*u3hi <= a['ds'][1]
            and a['v'][0] <= 8*u3lo <= 8*u3hi <= a['v'][1]):
        raise ArithmeticError('Center jet incompatible with original Step68z continuum')
    return u3lo,u3hi


def center_limits(u3lo,u3hi):
    lo,hi=F(u3lo),F(u3hi)
    if not lo <= hi < 0:
        raise ValueError('Only certified strictly negative U3 range')
    return {name:[str(m*lo),str(m*hi)] for name,m in LIMIT_MULTIPLIERS.items()}


def formal_radial_jet_audit():
    """Independent exact three-radial-derivative polynomial oracle."""
    r=sp.symbols('r',real=True)
    U0,U1,U2,U3,U4=sp.symbols('U0 U1 U2 U3 U4')
    s=r**2
    p=s*(U0+U1*s+U2*s**2+U3*s**3+U4*s**4)
    tests={
        'U_minus_Ustar_over_s3':(p/s-(U0+U1*s+U2*s**2))/s**3,
        'U_s_minus_Ustar_s_over_s2':(sp.diff(p/s,r)/(2*r)-(U1+2*U2*s))/s**2,
        'U_ss_minus_2U2_over_s':(sp.diff(sp.diff(p/s,r)/(2*r),r)/(2*r)-2*U2)/s,
        'U_sss_at_s0':sp.diff(sp.diff(sp.diff(p/s,r)/(2*r),r)/(2*r),r)/(2*r),
        'pLf_minus_r2Ustar_over_r8':(p-s*(U0+U1*s+U2*s**2))/r**8,
        'pLf_prime_over_r_minus_Vstar_over_s3':(sp.diff(p,r)/r-(2*U0+4*U1*s+6*U2*s**2))/s**3,
        'pLf_doubleprime_minus_2U0_12U1s_30U2s2_over_s3':(sp.diff(p,r,2)-(2*U0+12*U1*s+30*U2*s**2))/s**3,
        'pLf_tripleprime_over_r_minus_24U1_120U2s_over_s2':(sp.diff(p,r,3)/r-(24*U1+120*U2*s))/s**2,
        'pLf_8th_r_derivative_at_center':sp.diff(p,r,8),
    }
    proof={}
    for name,expr in tests.items():
        v=sp.simplify(sp.limit(sp.cancel(expr),r,0))
        target=LIMIT_MULTIPLIERS[name]*U3
        if sp.simplify(v-target)!=0:
            raise ArithmeticError(f'Wrong canonical center jet {name}: {v} != {target}')
        proof[name]=int(LIMIT_MULTIPLIERS[name])
    return proof


def nonzero_radius_ode_identities():
    """Exact symbolic identities ONLY; not enclosures of G derivatives."""
    s=sp.symbols('s',positive=True)
    u=sp.Function('U')(s)
    G=sp.Function('G')(s,u)
    us=sp.diff(u,s);uss=sp.diff(u,s,2);usss=sp.diff(u,s,3)
    gs=sp.Derivative(G,s,evaluate=False)  # partial derivative with u held fixed
    gu=sp.Derivative(G,u,evaluate=False)
    # Explicit total derivatives from chain rule; do not freeze U during differentiation.
    Gs=gs+gu*us
    Gss=(sp.Derivative(G,s,2,evaluate=False)
         +2*sp.Derivative(G,s,u,evaluate=False)*us
         +sp.Derivative(G,u,2,evaluate=False)*us**2+gu*uss)
    return {'second_rhs':Gs-4*us, 'third_rhs':Gss-6*uss,
            'second_identity':'2*s*U_ss=G_s+(G_U-4)*U_s',
            'third_identity':'2*s*U_sss=G_ss+2*G_sU*U_s+G_UU*U_s^2+(G_U-6)*U_ss',
            'center_denominator_proof':'2*n+2-G_U(0,U0)>0 for n>=1 since authenticated Step68v G_U<0'}


def report(folder):
    lo,hi=authenticated_inputs(folder)
    proof=formal_radial_jet_audit()
    if proof != LIMIT_MULTIPLIERS:
        raise AssertionError('Formal oracle mismatch')
    return {'step':'68aa', 'type':'EXACT_AUTHENTIC_F_CANONICAL_CENTER_LIMITS_ONLY',
            'analytic_spatial_origin':'Step49 and original Step45/46/55, conditional on original published certificates',
            'input_authentic_Git_blobs':{
                '68z_source':BLOB68Z_SOURCE,'68z_report':BLOB68Z_REPORT,
                **{k:v[1] for k,v in SOURCES.items()}},
            'strictly_negative_Step67b_U3':[str(lo),str(hi)],
            'exact_center_limit_intervals':center_limits(lo,hi),
            'independent_sympy_polynomial_oracle_multipliers':proof,
            'regularized_ode_derivative_identities':{
                k:v for k,v in nonzero_radius_ode_identities().items() if isinstance(v,str)},
            'crucial_scope':'Limits at r=0, NOT uniform bounds for 0<r<=1/32. Higher radial derivatives require actual G partial-derivative interval certificates.',
            'temporal_Step58_AN_AM_near_center':'NOT_COMPUTED',
            'annulus_r_1over64_1over32':'NOT_CERTIFIED',
            'full_Dirac_rank':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:
        raise SystemExit('usage: python -m numerics.hr_step68aa_canonical_center_radial_jets research/reports')
    print(json.dumps(report(sys.argv[1]),ensure_ascii=False,indent=2))

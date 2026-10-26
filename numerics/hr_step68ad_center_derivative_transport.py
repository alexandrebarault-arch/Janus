"""Step68ad-A: desingularized derivative transport for ORIGINAL physical radial ODE.

Physical numerical input is strictly the SHA-authenticated Step68v G_U tube
and Step68ac center U1..U4 enclosures. This module does NOT claim to have
computed original G_ss, G_sss, G_ssss on the positive-radius tube. The
comparison lemma becomes a physical U''/U'''/U'''' enclosure ONLY once the
original R_n(s) are rigorously bounded on the same continuous domain.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from math import factorial
import json
import sympy as sp

SOURCE_REPORTS={
    '68v':('gate2b-step68v-global-monotone-radial-U.json',
           'd83a3b80862a2e990a4c4879ec8745a4e91c8b34'),
    '68ac':('gate2b-step68ac-authentic-U4-report.json',
            '16ae8dab3563c17134e4e20f886fb7306dc2e4ba'),
}
PHYSICAL_SMAX=F(1,64)
EXPECTED_PHYSICAL_ORIGINALS={
    'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}


def blob_sha(raw:bytes)->str:
    return sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def interval(pair):
    if len(pair)!=2:raise ValueError('Two rational interval endpoints required')
    a,b=map(F,pair)
    if a>b:raise ValueError('Reversed interval')
    return a,b


def load_physical_reports(folder:Path|str):
    folder=Path(folder)
    data={}
    for name,(file,wanted) in SOURCE_REPORTS.items():
        raw=(folder/file).read_bytes()
        if blob_sha(raw)!=wanted:
            raise ValueError(f'Original Step{name} Git blob mismatch: {blob_sha(raw)}')
        data[name]=json.loads(raw)
    v,ac=data['68v'],data['68ac']
    if (v.get('step')!='68v' or ac.get('step')!='68ac'
        or v.get('center_s_range')!=['0','1/64']
        or v.get('original_physical_shas')!=EXPECTED_PHYSICAL_ORIGINALS
        or any(ac['original_source_git_blob_shas'].get(k)!=val
               for k,val in EXPECTED_PHYSICAL_ORIGINALS.items())
        or ac.get('center_exact_symbolic_GU',{}).get('center_GU0_exact')!='-1'
        or ac.get('U4_sign_strict_negative') is not True
        or any(x.get('GATE_2B')!='OPEN' or x.get('JANUS_R')!='NOT_VALIDATED'
               for x in (v,ac))):
        raise ValueError('Original physical center report identity/status mismatch')
    gl,gh=interval(v['G_U_center_interval'])
    if not gl<=F(-1)<=gh<0:
        raise ValueError('Physical Step68v G_U tube does not contain exact -1')
    for k in ('original_U1_interval','original_U2_interval',
              'original_Step67b_U3_interval','intersection_certified_U4'):
        interval(ac[k])
    return data


def damping_bounds(g_interval,n):
    """For 2s y_n' + a_n(s)y_n=R_n(s), a_n=2(n+1)-G_U.

    n>=1; requires genuine G_U interval on the SAME physical domain.
    """
    if not isinstance(n,int) or n<1:raise ValueError('Positive derivative order')
    gl,gh=interval(g_interval)
    alo=2*n+2-gh
    ahi=2*n+2-gl
    if alo<=0:raise ArithmeticError('No positive derivative damping')
    return alo,ahi


def ratio_enclosure(r_interval,a_interval):
    """Universal range of R/a for R∈[rlo,rhi], 0<alo<=a<=ahi.

    The bounded-center solution of 2s y'+a(s)y=R(s) is a POSITIVE
    weighted average of R/a on [0,s], so this interval encloses y(s)
    for ALL s>0, assuming a,R continuous, a>=alo>0, y bounded at 0.
    This function does not certify the physical R interval itself.
    """
    rl,rh=interval(r_interval);al,ah=interval(a_interval)
    if al<=0:raise ValueError('Strict positive damping required')
    corners=[rl/al,rl/ah,rh/al,rh/ah]
    return min(corners),max(corners)


def center_source_intervals(ac):
    """Exact R_n(0)=(2n+3)*n!*U_n for original G_U(0)=-1.

    Here R_n is D_s^n[G(s,U(s))]-G_U(s,U(s))*U^(n)(s),
    i.e. no highest unknown derivative in the source.
    """
    keys={1:'original_U1_interval',2:'original_U2_interval',
          3:'original_Step67b_U3_interval',4:'intersection_certified_U4'}
    rows={}
    for n,key in keys.items():
        ul,uh=interval(ac[key]);mult=(2*n+3)*factorial(n)
        a,b=mult*ul,mult*uh
        rows[str(n)]={'multiplier_exact':str(mult),
                      'R_n_at_center':[str(a),str(b)],
                      'sign':'POSITIVE' if a>0 else 'NEGATIVE' if b<0 else 'UNRESOLVED'}
    if [rows[str(i)]['sign'] for i in range(1,5)]!=['POSITIVE','NEGATIVE','NEGATIVE','NEGATIVE']:
        raise ArithmeticError('Original center derivative source signs not proven')
    return rows


def symbolic_transport_identities():
    """Independently verify the full chain rule for n=1..4, exactly.

    E=2sU_s+2U-G(s,U); D^n E =
    2s U^(n+1)+(2n+2-G_U)U^(n)-R_n.
    """
    s=sp.symbols('s');U=sp.Function('U')(s)
    u=sp.symbols('u');G=sp.Function('G')(s,u)
    composed=G.subs(u,U)
    E=2*s*sp.diff(U,s)+2*U-composed
    out={}
    for n in range(1,5):
        Gn=sp.diff(composed,s,n)
        GU=sp.diff(G,u).subs(u,U)
        R=sp.expand(Gn-GU*sp.diff(U,s,n))
        if R.has(sp.diff(U,s,n)):
            raise AssertionError(f'R_{n} contains forbidden highest U derivative')
        expected=2*s*sp.diff(U,s,n+1)+(2*n+2-GU)*sp.diff(U,s,n)-R
        if sp.simplify(sp.diff(E,s,n)-expected)!=0:
            raise AssertionError(f'Exact chain-rule transport fails n={n}')
        out[str(n)]={'damping':'2n+2-G_U','source_excludes_U_n':True,
                     'symbolic_identity_exact':True,
                     'source_term_count':len(sp.Add.make_args(R))}
    return out


def certificate(folder:Path|str):
    reports=load_physical_reports(folder)
    v,ac=reports['68v'],reports['68ac']
    gl,gh=interval(v['G_U_center_interval'])
    damping={}
    for n in range(1,5):
        alo,ahi=damping_bounds((gl,gh),n)
        damping[str(n)]={'a_n_interval':[str(alo),str(ahi)],
                        'a_n_strict_positive':True}
    return {'step':'68ad-A',
        'type':'EXACT_DERIVATIVE_TRANSPORT_AND_ORIGINAL_PHYSICAL_DAMPING',
        'original_git_blob_sha_reports':{k:sha for k,(_,sha) in SOURCE_REPORTS.items()},
        'original_physical_source_blobs':EXPECTED_PHYSICAL_ORIGINALS,
        'physical_domain_s':['0','1/64'],
        'physical_domain_r':['0','1/8'],
        'original_G_U_continuum_interval':[str(gl),str(gh)],
        'transport_identity_symbolic_n1_to_n4':symbolic_transport_identities(),
        'damping_original_physical':damping,
        'center_source_terms_original_physical':center_source_intervals(ac),
        'transport_theorem':('If a_n(s)=2(n+1)-G_U(s,U(s))>=amin>0 and R_n(s) '
            'is continuous with rigorous interval [Rlo,Rhi] on [0,S], '
            'the unique bounded-center solution y=U^(n) of '
            '2s*y_prime+a_n*y=R_n lies in the rational interval '
            'range([Rlo,Rhi]/[amin,amax]) at EVERY s in [0,S]. '
            'Proof: integrating factor yields a positive normalized kernel '
            'with weights a_n(t)/(2t)*exp(-integral_t^s a_n(v)/(2v)dv), '
            'whose integral from 0 to s equals 1 because amin>0. '
            'No division by an interval containing s=0.'),
        'missing_physical_Rn_continuum_enclosures':['R2','R3','R4'],
        'physical_U_ss_and_U_sss_on_positive_radius':'NOT_CERTIFIED',
        'temporal_original_Step58_A_N_A_M':'NOT_COMPUTED',
        'full_Dirac_rank':'NOT_COMPUTED',
        'next_step':'68ad-B: original Step55/68n interval mixed partials of fixed G on [0,1/1024], then bound R2,R3,R4 with certified U,U_s and recursively apply comparison lemma; evaluate original Step58 temporal operator only after higher canonical jets are enclosed.',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def main():
    import sys
    if len(sys.argv)!=2:raise SystemExit('usage: python -m numerics.hr_step68ad_center_derivative_transport research/reports')
    print(json.dumps(certificate(sys.argv[1]),indent=2,ensure_ascii=False))

if __name__=='__main__':main()

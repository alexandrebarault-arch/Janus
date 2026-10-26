"""JANUS 68ad-C1: exact-rational, center-safe third jet of physical pLf=r²U(r²).

Consumes Git-blob-pinned ORIGINAL physical Step68v, Step68ac, Step68ad-B2
reports. A rigorous conditional spatial consequence, NOT a Step58 temporal
coefficient/rank proof. No differentiation of interval bounds is performed.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json

PINS={
    '68v':('gate2b-step68v-global-monotone-radial-U.json','d83a3b80862a2e990a4c4879ec8745a4e91c8b34'),
    '68ac':('gate2b-step68ac-authentic-U4-report.json','16ae8dab3563c17134e4e20f886fb7306dc2e4ba'),
    'B2':('gate2b-step68ad-B2-original-G-Uss-Usss.json','ac961b5b83667a83497497d22a701c24584cb561'),
}
S_MAX=F(1,1024)

def git_blob(raw:bytes)->str:
    return sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def pair(raw):
    if not isinstance(raw,(list,tuple)) or len(raw)!=2:
        raise ValueError('Expected exactly two interval endpoints')
    lo,hi=map(F,raw)
    if lo>hi:raise ValueError('Reversed interval')
    return lo,hi

def read_pinned(folder):
    folder=Path(folder)
    reports={}
    for key,(filename,sha) in PINS.items():
        raw=(folder/filename).read_bytes()
        if git_blob(raw)!=sha:
            raise ValueError(f'Original physical Step{key} report Git SHA mismatch')
        reports[key]=json.loads(raw)
    return reports

def certify_from_reports(reports):
    """All inequalities are algebraic consequences of pinned continuum tubes.

    Input authentication is performed by read_pinned; this pure function
    is separately testable with exact rational fixtures and perturbations.
    """
    v,ac,b=reports['68v'],reports['68ac'],reports['B2']
    if (v.get('step')!='68v' or ac.get('step')!='68ac'
        or b.get('step')!='68ad-B2'
        or v.get('center_s_range')!=['0','1/64']
        or b.get('s_domain')!=['0','1/1024']
        or b.get('r_domain')!=['0','1/32']
        or v.get('U_s_strict_positive_inner') is not True
        or b.get('strict_negative_R2_U_ss_R3_U_sss') is not True
        or ac.get('center_exact_symbolic_GU',{}).get('center_GU0_exact')!='-1'
        or b.get('original_report_sha',{}).get('68v')!=PINS['68v'][1]
        or b.get('original_report_sha',{}).get('68ac')!=PINS['68ac'][1]
        or any(x.get('GATE_2B')!='OPEN' or x.get('JANUS_R')!='NOT_VALIDATED'
               for x in (v,ac,b))):
        raise ValueError('Invalid physical source scope or cross-provenance')
    u0=pair(ac['center_U0_interval'])
    us=pair([v['U_s_center_lower_rational'],v['U_s_center_upper_rational']])
    uss=pair(b['U_ss_global']);usss=pair(b['U_sss_global'])
    if not (u0[1]<0<us[0] and uss[1]<0 and usss[1]<0):
        raise ArithmeticError('Required original physical strict signs lost')
    # Since U_s>0, U0_lo <= U(s) <= U0_hi+smax*U_s_hi.
    U=(u0[0],u0[1]+S_MAX*us[1])
    # Exact chain rule pLf=r²U(s): pLf'/r=2(U+sUs).
    first_over_r=(2*u0[0],2*(u0[1]+2*S_MAX*us[1]))
    # pLf'''/r = 24 Us + 36s Uss + 8s² Usss. Both higher jets <0.
    third_over_r=(24*us[0]+36*S_MAX*uss[0]+8*S_MAX*S_MAX*usss[0],24*us[1])
    # pLf''(0)=2U0; pLf'''/r>0 proves pLf'' strictly increasing for r>0.
    # Upper: 2U + 10sUs + 4s²Uss <= 2U0_hi+12*smax*Us_hi.
    second=(2*u0[0],2*u0[1]+12*S_MAX*us[1])
    # Third derivative of the composite U(r²), not of pLf.
    Uthird_over_r=(12*uss[0]+8*S_MAX*usss[0],12*uss[1])
    if not (U[1]<0 and first_over_r[1]<0 and second[1]<0
            and third_over_r[0]>0 and Uthird_over_r[1]<0):
        raise ArithmeticError('No strict sign certificate on full center interval')
    def as_strings(x):return [str(x[0]),str(x[1])]
    return {
        'step':'68ad-C1',
        'kind':'CONDITIONAL_EXACT_RATIONAL_ORIGINAL_CANONICAL_P_LF_THIRD_JET',
        'pinned_original_report_blobs':{k:sha for k,(_,sha) in PINS.items()},
        'physical_domain_s':['0','1/1024'],'physical_domain_r':['0','1/32'],
        'U_center':as_strings(u0),'U_s_continuum':as_strings(us),
        'U_ss_continuum':as_strings(uss),'U_sss_continuum':as_strings(usss),
        'U_continuum':as_strings(U),
        'pLf_prime_over_r_continuum':as_strings(first_over_r),
        'pLf_second_continuum':as_strings(second),
        'pLf_third_over_r_continuum':as_strings(third_over_r),
        'U_of_r_third_over_r_continuum':as_strings(Uthird_over_r),
        'pLf_prime_over_r_strict_negative':True,
        'pLf_second_strict_negative':True,
        'pLf_third_over_r_strict_positive':True,
        'U_of_r_third_over_r_strict_negative':True,
        'center_pLf_second_equals_2U0':True,
        'center_pLf_third_equals_zero':True,
        'identities':{
            'pLf':'r² U(s), s=r²',
            'pLf_prime_over_r':'2(U+s U_s)',
            'pLf_second':'2U+10s U_s+4s² U_ss',
            'pLf_third_over_r':'24 U_s+36s U_ss+8s² U_sss',
            'U_of_r_third_over_r':'12 U_ss+8s U_sss',
        },
        'scope':'Original Step45/46/55 radial physical branch, conditional on Step49/68v/68ad-B2 certificates. Only pLf canonical jet; other 11 canonical jets and Step58 temporal coefficients not yet evaluated.',
        'temporal_original_A_N_A_M':'NOT_COMPUTED',
        'remaining_seven_temporal_cells':'PENDING',
        'full_Dirac_rank':'NOT_COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
        'next_step':'68ad-C2: inject these center-safe original pLf third-jet bounds into all 12 canonical jets, original non-frozen-shift Step58/60; bound A_N/r²,A_M/r² on seven pending cells and continue to r=0.'
    }

def certify(folder):return certify_from_reports(read_pinned(folder))

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:raise SystemExit('usage: python -m numerics.hr_step68ad_c1_center_momentum_jet research/reports')
    print(json.dumps(certify(sys.argv[1]),indent=2,ensure_ascii=False))

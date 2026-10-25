"""Step68z: exact invariant-cone refinement of certified center radial ODE.

Conditional on SHA-authenticated 68u/v/y certificates and analytic Step49
solution, NOT a temporal lapse, Dirac-rank, or 4D cosmology certificate.
"""
from __future__ import annotations
import json
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path

S_MAX = F(1, 1024)
SOURCES = {
    '68u': ('gate2b-step68u-center-cubic-barrier.json', 'aaacd0064e04cb0f5d596aa3df042a4c9a4c751d'),
    '68v': ('gate2b-step68v-global-monotone-radial-U.json', 'd83a3b80862a2e990a4c4879ec8745a4e91c8b34'),
    '68y': ('gate2b-step68y-signed-center-residual.json', '04271c360f2245142e171a5979db139ac4bdaf79'),
}


def original_reports(folder):
    folder = Path(folder)
    reports = {}
    for name, (filename, blob) in SOURCES.items():
        raw = (folder / filename).read_bytes()
        actual = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if actual != blob:
            raise ValueError(f'Step{name} source blob drift {actual}')
        reports[name] = json.loads(raw)
    u, v, y = (reports[k] for k in ('68u', '68v', '68y'))
    if not (u['step'] == '68u' and v['step'] == '68v' and y['step'] == '68y'
            and u['s_range'] == ['0', '1/1024']
            and v['center_s_range'] == ['0', '1/64']
            and y['domain_s'] == ['0', '1/1024']
            and y['F0_strict_negative_for_s_positive'] is True
            and y['authenticated_original_blobs']['68u'] == SOURCES['68u'][1]
            and y['authenticated_original_blobs']['68v'] == SOURCES['68v'][1]
            and all(t['GATE_2B'] == 'OPEN' and t['JANUS_R'] == 'NOT_VALIDATED'
                    for t in (u, v, y))):
        raise ValueError('Unmatched radial domain or provenance')
    return reports


def tightened_bounds(reports):
    u, v, y = (reports[k] for k in ('68u', '68v', '68y'))
    flo, fhi = map(F, y['F0_over_s_cubed_intersection'])
    glo, ghi = map(F, v['G_U_center_interval'])
    u3lo = F(u['U3_lower_from_published_Step67b'])
    u3hi = F(u['U3_upper_from_published_Step67b'])
    kappa = F(y['kappa'])
    if not (flo <= fhi < 0 and glo <= ghi < 0 and 0 < kappa
            and F(y['U_minus_Ustar_over_s_cubed'][0]) == -kappa
            and F(y['U_minus_Ustar_over_s_cubed'][1]) == 0):
        raise ValueError('Signed input hypotheses violated')
    # With d=U-Ustar=s^3*h and g(s) a mean value of G_U:
    #     2*s*h_s=f(s)+(g(s)-8)*h,
    #     f(s)=F0(s)/s^3 in [flo,fhi], g in [glo,ghi].
    # For constant lower/upper barriers the residual signs are >=0/<=0.
    hlo, hhi = flo/(8-ghi), fhi/(8-glo)
    if not (-kappa <= hlo <= u3lo <= u3hi <= hhi < 0):
        raise ArithmeticError('Center Taylor coefficient not captured by invariant cone')
    # (g-2)*h is positive; monotone in (-g) and (-h).
    dslo, dshi = (flo+(ghi-2)*hhi)/2, (fhi+(glo-2)*hlo)/2
    vlo, vhi = ghi*hhi, glo*hlo
    if not (dslo <= dshi < 0 < vlo <= vhi):
        raise ArithmeticError('Strict signed derivatives not certified')
    # Require strict containment in older published weak signed envelopes.
    old_ds = list(map(F, y['U_s_minus_Ustar_s_over_s_squared']))
    old_v = list(map(F, y['G_minus_Vstar_over_s_cubed']))
    if not (old_ds[0] <= dslo <= dshi <= old_ds[1]
            and old_v[0] <= vlo <= vhi <= old_v[1]):
        raise ArithmeticError('Refinement not contained in source certificate')
    return {'h':(hlo,hhi), 'ds':(dslo,dshi), 'v':(vlo,vhi),
            'f':(flo,fhi),'g':(glo,ghi),'u3':(u3lo,u3hi)}


def report(folder):
    a = tightened_bounds(original_reports(folder))
    out = {'step':'68z', 'domain_s':['0','1/1024'], 'domain_r':['0','1/32'],
           'original_blob_shas':{key:sha for key, (_, sha) in SOURCES.items()},
           'center_invariant_cone_h_equals_U_minus_Ustar_over_s_cubed':list(map(str,a['h'])),
           'U_s_minus_Ustar_s_over_s_squared':list(map(str,a['ds'])),
           'G_minus_Vstar_over_s_cubed':list(map(str,a['v'])),
           'signs_for_every_s_gt_zero':{
                'U_minus_Ustar':'NEGATIVE',
                'U_s_minus_Ustar_s':'NEGATIVE',
                'G_minus_Vstar':'POSITIVE'},
           'center_U3_Step67b_interval':list(map(str,a['u3'])),
           'center_s_samples':{str(s):{
               'U_minus_Ustar':[str(q*s**3) for q in a['h']],
               'U_s_minus_Ustar_s':[str(q*s**2) for q in a['ds']],
               'G_minus_Vstar':[str(q*s**3) for q in a['v']]}
               for s in (F(1,1024),F(1,4096))},
           'proof':'Comparison for 2*s*h_s=f+(g-8)*h, h(0)=U3; constant cone [flo/(8-ghi), fhi/(8-glo)] invariant; exact arithmetic.',
           'temporal_A_N_A_M_near_center':'NOT_COMPUTED',
           'full_Dirac_rank':'NOT_COMPUTED',
           'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    return out

if __name__ == '__main__':
    import sys
    if len(sys.argv)!=2:
        raise SystemExit('usage: python -m numerics.hr_step68z_invariant_center_cone research/reports')
    print(json.dumps(report(sys.argv[1]), indent=2, ensure_ascii=False))

"""Step68g exact FULL ORIGINAL temporal Cdot M'-coefficient q'' quotient.

On the positive-K stationary shift shell Fz=0, B_M := [Cdot]_{M'}
contains exactly the three canonical second radial jets pLg'', Sg'', theta_g''.
The COMPLETE radial derivative Fz'=D_r Fz cancels them, with coefficient
lambda=3*z*(z*z-1)/(Lg*Lf**2); B_M-lambda*Fz' is free of all 12 q''.
This removes only second canonical spatial jets in one full Cdot lapse
coefficient, NOT the zero/positivity/rank of the physical multiplier system.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
from hashlib import sha1
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator, highest_lapse_certificate

SOURCES={
 'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'hr_step57_secondary_principal_symbol.py':'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f',
 'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
}

def authenticate():
    for name,expected in SOURCES.items():
        b=Path(__file__).with_name(name).read_bytes()
        actual=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        if actual!=expected:raise ValueError('Historical source drift '+name)
    return SOURCES.copy()

@lru_cache(1)
def second_jet_quotient():
    authenticate()
    p=exact_physical_ward(); v=physical_operator()
    z=v['z']; q=dict(zip(p['Q'],p['q']))
    Lg,Lf=q['Lg'],q['Lf']
    lam=3*z*(z*z-1)/(Lg*Lf**2)
    full_fzprime=v['Dt'](p['Fz'])
    raw=v['operator']['M'][1]
    shell={p['dq'][1]:highest_lapse_certificate()['shift_elimination_pLg_prime']}
    before={}
    after={}
    for name,jet in zip(p['Q'],v['qpp']):
        if raw.has(jet):before[name]=sp.factor(sp.diff(raw,jet).subs(shell))
        if raw.has(jet) or full_fzprime.has(jet):
            after[name]=sp.factor(sp.cancel(sp.diff(raw-lam*full_fzprime,jet).subs(shell)))
    assert set(before)=={'pLg','Sg','tg'}
    assert set(after)=={'pLg','Sg','tg'}
    assert all(x!=0 for x in before.values())
    assert all(x==0 for x in after.values())
    for jet in v['qpp']:
        if raw.has(jet):
            for other in v['qpp']:
                assert sp.diff(raw,jet,other)==0
    wrong=raw+lam*full_fzprime
    assert sp.factor(sp.diff(wrong,p['ddq'][1]).subs(shell))!=0
    # First impose Fz=0, then subtract the full Fz' and erase q'' ONLY
    # after proving the residual is affine in q'' with all coefficients 0.
    reduced=(raw-lam*full_fzprime).subs(shell).subs({x:sp.S.Zero for x in v['qpp']})
    assert not any(reduced.has(x) for x in v['qpp'])
    assert not any(reduced.has(x) for x in v['qppp'])
    return {'lambda':sp.factor(lam),'raw':raw,'Fzprime_full':full_fzprime,
            'shell':shell,'unreduced_second_coefficients':before,
            'exact_second_jet_residuals':after,
            'representative_qsecond_free':reduced,
            'original_full_Cdot_coefficient':'Mprime',
            'scope':'Fz=Fzprime=0,K>0; no other primary/secondary imposed'}


def center_product_certificate():
    r,s,w,k,a,b,f,fs=sp.symbols('r s w k a b f fs',real=True,positive=True)
    z=r*w; t=1-s*w*w
    lam=3*z*(z*z-1)/(a*b*b)
    Fr=r*r*(3*f+2*s*fs)
    expected=-3*r**3*w*t*(3*f+2*s*fs)/(a*b*b)
    assert sp.simplify((lam*Fr).subs(r*r,s)-expected.subs(r*r,s))==0
    assert sp.limit(expected,r,0)==0
    return {'lambda_center':'-3*r*w*(1-s*w²)/(a*b²)',
            'Fzprime_center':'r²*(3*f+2*s*f_s)',
            'product_center':'-3*r³*w*(1-s*w²)*(3*f+2*s*f_s)/(a*b²)',
            'regular':True}


def manifest():
    q=second_jet_quotient()
    return {'step':'68g','original_git_blobs':authenticate(),
            'physical_full_temporal_operator':'original Step58 six canonical pairs',
            'Cdot_Mprime_second_jet_set':sorted(q['unreduced_second_coefficients']),
            'lambda':str(q['lambda']),
            'all_twelve_second_jet_derivatives_zero_on_Fz':True,
            'remaining_second_jet_residuals':{k:str(v) for k,v in q['exact_second_jet_residuals'].items()},
            'fully_second_jet_free_representative':True,
            'center_regular_correction':center_product_certificate(),
            'full_primary_secondary_shell_reduced':False,
            'B_M_on_exact_step55_background_zero_proven':False,
            'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
 import json
 print(json.dumps(manifest(),indent=2))

"""Step68i exact ORIGINAL full Cdot Nprime quotient removing q'',q'''.

Step60 proved B_N+(1-z²)/(Lg Lf)*H_g' has zero third canonical
radial jets on Fz=0 after the complete H_g' prolongation. Here the
remaining second-jet dependence is exactly one-dimensional, along Sg''.
A full H_g subtraction removes it, leaving only q,q' and z,z' jets.

DO NOT claim the resulting lower-jet representative vanishes without
imposing all remaining primaries/secondary; symbolic random points show it
is generally NONZERO off those constraints. At center Sg=0 the beta
coefficient has an apparent division by Sg, requiring parity normalization.
"""
from __future__ import annotations
from functools import lru_cache
from hashlib import sha1,sha256
from pathlib import Path
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step60_full_constraint_prolongation import full_constraint_prolongation,verified_original_sources
from .hr_step58_temporal_operator import physical_operator

ORIGINALS={
 'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'hr_step57_secondary_principal_symbol.py':'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f',
 'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
 'hr_step59_third_jet_gate.py':'ae26a79cbfa7bb50fbb398d7d6c18478adf7627e',
 'hr_step60_full_constraint_prolongation.py':'9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509'}

def authenticate():
    for n,expected in ORIGINALS.items():
        b=Path(__file__).with_name(n).read_bytes()
        sha=sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        if sha!=expected:raise ValueError('Original Dirac source drift '+n)
    assert verified_original_sources()=={k:v for k,v in ORIGINALS.items() if 'step60_' not in k}
    return ORIGINALS.copy()

@lru_cache(1)
def physical_BN_second_jet_quotient():
    authenticate()
    p=exact_physical_ward();o=physical_operator();q=dict(zip(p['Q'],p['q']))
    c=full_constraint_prolongation()
    Sg=q['Sg'];Lg=q['Lg'];mg=p['parameters'][0];Sg2=p['ddq'][2]
    BNthirdfree=c['third_free_BN_on_Fz']
    Hg=p['Hg'].subs(c['stationarity_substitution'])
    Hg_second_coefficient=sp.diff(Hg,Sg2)
    assert sp.factor(Hg_second_coefficient-2*mg*Sg/Lg)==0
    target_second_coefficient=sp.diff(BNthirdfree,Sg2)
    beta=target_second_coefficient/Hg_second_coefficient
    assert not any(beta.has(j) for j in p['ddq'])
    assert not any(beta.has(j) for j in o['qppp'])
    raw=BNthirdfree-beta*Hg
    second_residuals={}
    for name,j in zip(p['Q'],p['ddq']):
        if raw.has(j):
            residual=sp.factor(sp.cancel(sp.diff(raw,j)))
            if residual!=0:raise AssertionError(f'Nonzero second jet {name}: {residual}')
            second_residuals[name]=residual
    assert second_residuals=={'Lg':0,'pLg':0,'Sg':0,'tg':0}
    assert not any(raw.has(j) for j in o['qppp'])
    second_zero={j:sp.S.Zero for j in p['ddq']}
    representative=raw.subs(second_zero)
    assert not any(representative.has(j) for j in p['ddq'])
    assert not any(representative.has(j) for j in o['qppp'])
    wrong=BNthirdfree+beta*Hg
    assert sp.factor(sp.cancel(sp.diff(wrong,Sg2)))!=0
    return {'full_BN':o['operator']['N'][1],
            'H_g_prime_correction':c['alpha_Hgprime'],
            'H_g_second_coefficient':Hg_second_coefficient,
            'beta':beta,
            'raw_quotient':raw,
            'representative_qsecond_and_qthird_free':representative,
            'second_derivative_residuals':second_residuals,
            'physical_Hg_stationary':Hg,
            'source_git_blobs':authenticate(),
            'proof_scope':'On Fz=Hg=Hgprime=0, positive regular chart Sg,Lg,Lf,mg nonzero, B_N equals this lower q,qprime representative. It is not proven zero.'}


def manifest():
    c=physical_BN_second_jet_quotient()
    return {'step':'68i','authenticated_originals':c['source_git_blobs'],
        'original_full_Cdot_coefficient':'Nprime',
        'exact_identity_on_Fz':'R_BN=B_N+(1-z²)/(Lg Lf)*Hgprime-beta*Hg is independent of all qsecond/qthird',
        'beta_formula':'beta = partial_Sgrr(B_N+(1-z²)/(Lg Lf)*Hgprime on Fz)/(2 Mg² Sg/Lg)',
        'beta_ops':sp.count_ops(c['beta']),
        'beta_srepr_sha256':sha256(sp.srepr(c['beta']).encode()).hexdigest(),
        'remaining_partial_second_jet_residuals':{k:str(v) for k,v in c['second_derivative_residuals'].items()},
        'representative_ops':sp.count_ops(c['representative_qsecond_and_qthird_free']),
        'representative_is_identically_zero':'NOT_PROVED; numerical generic point NEGATIVE',
        'regular_center_beta_studied':False,
        'step55_complete_primary_secondary_shell_substituted':False,
        'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
 import json
 print(json.dumps(manifest(),indent=2))

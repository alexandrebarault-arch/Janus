"""Step60 exact FULL radial constraint-prolongation quotient of physical time Dirac.

Import the BYTE-ORIGINAL Step45 six-pair HR/two-dust Hamiltonian, genuine Step58
full local temporal operator, and differentiate the ENTIRE constraints Hg and
C_red.  On Fz=0 (positive K chart) prove that subtracting COMPLETE Hg' and
C_red' from B_N and A_M cancels EVERY 3rd canonical radial jet identically.

This proves only a differential-order reduction, not lapse rank/fixing,
constraint preservation, cosmic evolution or BD ghost absence. In particular
setting q'''=0 in an UNREDUCED temporal equation would be erroneous.
"""
from __future__ import annotations
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import sympy as sp
from .hr_step58_temporal_operator import physical_operator, highest_lapse_certificate
from .hr_step57_secondary_principal_symbol import authenticated_step45

EXPECTED = {
  'hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
  'hr_step57_secondary_principal_symbol.py': 'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f',
  'hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
  'hr_step59_third_jet_gate.py': 'ae26a79cbfa7bb50fbb398d7d6c18478adf7627e'
}


def verified_original_sources():
    root=Path(__file__).resolve().parent
    for path,expected in EXPECTED.items():
        raw=(root/path).read_bytes()
        actual=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=expected:
            raise ValueError(f'Original physical dependency changed: {path} {actual}')
    return EXPECTED.copy()


@lru_cache(maxsize=1)
def full_constraint_prolongation():
    """Exactly cancel q''' with FULL, not principal-only, Hg' and Cred'.

    C_red' = Dt(C(q,q',z,z')) evaluated with z'' from the real positive-K
    stationary shift. The q''' cancellation is first checked on Fz=0 by
    eliminating ONLY the canonical pLg' jet, with all q''/q''' retained.
    We do not incorrectly impose Hg'=Cred'=0 without their lower jets.

    The external shift z,z' must be consistently prolonged on a physical
    profile when remaining lower-jet expressions are evaluated later.
    """
    verified_original_sources()
    p=authenticated_step45()
    o=physical_operator()
    q=dict(zip(p['Q'],p['q']))
    Lg,Lf=q['Lg'],q['Lf']
    z,zr=o['z'],o['zr']
    Dt=o['Dt']
    D,K=o['Dg'],o['K']
    root=sp.sqrt(1-z*z)
    ZD=root**3/K
    ZK=-z*(1-z*z)/K
    C=p['C_exact']
    D1=Dt(D);K1=Dt(K)
    D2=Dt(D1);K2=Dt(K1)
    Z1=ZD*D1+ZK*K1
    Z2=ZD*D2+ZK*K2+Dt(ZD)*D1+Dt(ZK)*K1
    # The coefficient of q''' comes exclusively from ZD*D2.
    # Z2 does contain external zr through Dt(ZD),Dt(ZK); its on-shell
    # value uses zr=Z1, as required for physical evaluation.
    Hgprime=Dt(p['Hg'])
    Credprime=Dt(o['C']).subs(o['zrr'],Z2)
    alpha=(1-z*z)/(Lg*Lf)
    beta=z/Lf
    original_BN=o['operator']['N'][1]
    original_AM=o['operator']['M'][0]
    raw_remainder_BN=original_BN+alpha*Hgprime
    raw_remainder_AM=original_AM-beta*Credprime
    sub={p['dq'][1]:highest_lapse_certificate()['shift_elimination_pLg_prime']}
    jets=dict(zip(p['Q'],o['qppp']))
    coefficient_residuals={}
    for label,raw in [('BN',raw_remainder_BN),('AM',raw_remainder_AM)]:
        coefficient_residuals[label]={}
        for name,j in jets.items():
            if raw.has(j):
                residual=sp.factor(sp.diff(raw,j).subs(sub))
                if residual!=0:
                    raise AssertionError(f'{label}/{name}: uncancelled qrrr: {residual}')
                coefficient_residuals[label][name]=residual
        # Trilinear higher q''' products are absent by construction;
        # test by differentiating every existing q''' coefficient twice.
        for j in jets.values():
            if raw.has(j) and any(sp.diff(sp.diff(raw,j),k)!=0
                                   for k in jets.values()):
                raise AssertionError(f'{label} is not affine in third jets')

    # All four residual coefficients N0,B_N',A_M,B_M' are now q''' free
    # either originally (Step59) or after complete constraint subtraction.
    # Remove third canonical radial jets only AFTER proving affine dependence and all
    # coefficients zero on the stationary-shift shell. These representatives
    # retain ALL lower canonical jets for subsequent Dirac-rank analysis.
    zero_third={j:sp.S.Zero for j in jets.values()}
    lower_BN=raw_remainder_BN.subs(sub).subs(zero_third)
    lower_AM=raw_remainder_AM.subs(sub).subs(zero_third)
    assert not any(lower_BN.has(j) or lower_AM.has(j) for j in jets.values())
    return {'C_red_prime':Credprime, 'Hg_prime':Hgprime,
            'original_BN':original_BN,'original_AM':original_AM,
            'raw_BN_remainder':raw_remainder_BN,
            'raw_AM_remainder':raw_remainder_AM,
            'third_free_BN_on_Fz':lower_BN,'third_free_AM_on_Fz':lower_AM,
            'first_shift_zprime':Z1,'second_shift_zdoubleprime':Z2,
            'stationarity_pLg_prime':sub[p['dq'][1]],
            'stationarity_substitution':sub,'all_third_jets':jets,
            'derivative_residuals':coefficient_residuals,
            'alpha_Hgprime':alpha,'beta_Credprime':beta,
            'on_Fz_zero':True,
            'status':'FULL THIRD-JET QUOTIENT EXACT; LOWER JETS AND LAPSUS RANK STILL OPEN'}


def manifest():
    r=full_constraint_prolongation()
    return {'step':60,'physical_model':'Original six canonical pairs, positive EH HR, 2 moving dusts',
        'authenticated_git_blobs':verified_original_sources(),
        'zprime':'ZD*Dgprime+ZK*Kprime on Fz=0',
        'zsecond':'ZD*Dgsecond+ZK*Ksecond+Dr(ZD)*Dgprime+Dr(ZK)*Kprime',
        'exact_full_prolongation_quotients':{
            'BN':'BN + (1-z²)/(Lg Lf)*Hgprime is qrrr-free on Fz=0',
            'AM':'AM - z/Lf*Credprime is qrrr-free on Fz=0'},
        'checked_qrrr_derivative_residuals':{name:{k:str(v) for k,v in vals.items()}
            for name,vals in r['derivative_residuals'].items()},
        'remaining_first_lapse_operator':'NOT evaluated on exact Step55 spatial profile',
        'full_lower_jet_constraint_quotient':'NOT COMPLETED',
        'Dirac_rank':'NOT COMPUTED','lapse_fixing':'NOT COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

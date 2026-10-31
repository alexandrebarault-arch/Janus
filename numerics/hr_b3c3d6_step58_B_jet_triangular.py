"""Exact *principal-jet* coefficients of original Step58 B, NOT full factorization.

Authentic Step45/58 are imported with a minimal Step57 shim. The identities
below hold OFF the primary shell, and therefore are stronger than numerical
point probes, but only for selected high-jet partial derivatives.
"""
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import sympy as S
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator

BLOBS={'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
       'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f'}

def authenticate():
    for name,expected in BLOBS.items():
        b=Path(__file__).with_name(name).read_bytes()
        assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==expected
    return True

@lru_cache(1)
def certificate():
    authenticate()
    p=exact_physical_ward();o=physical_operator()
    q=dict(zip(p['Q'],p['q']))
    Lg,Lf,Sg=q['Lg'],q['Lf'],q['Sg']
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=p['parameters']
    K=o['K'];F=o['Fz'];C=o['C']
    R=S.sqrt(1-z*z)
    v=o['qpp'][1] # pLg_rr
    w=o['qppp'][2] # Sg_rrr
    bm=o['operator']['M'][1]
    delta=o['operator']['N'][1]-z*C/Lg
    H=p['Hg'];Fr=o['Dt'](F);Hr=o['Dt'](H)
    # These formulas use the exact Fz, not Fz=0. Their RHS are rational
    # combinations of chart fields, Fz and sqrt(1-z^2).
    J=K/R+z*F
    expected={
      'bm_v':3*z*R**3*J/(Lf**3*Lg*mg*m2*(b1*Sg*Sg+2*b2*Sg*q['Sf']+b3*q['Sf']**2)),
      'delta_v':z*R**3*J/(Lf**2*Lg**2*mg*m2*(b1*Sg*Sg+2*b2*Sg*q['Sf']+b3*q['Sf']**2)),
      'delta_w':-2*Sg*R**3*J/(Lf**2*Lg**3*m2*(b1*Sg*Sg+2*b2*Sg*q['Sf']+b3*q['Sf']**2)),
    }
    observed={'bm_v':S.diff(bm,v),'delta_v':S.diff(delta,v),'delta_w':S.diff(delta,w)}
    residuals={k:S.factor(S.cancel(observed[k]-e)) for k,e in expected.items()}
    assert all(x==0 for x in residuals.values()),residuals
    assert S.diff(bm,w)==0
    assert S.diff(Fr,v)==-Lg and S.diff(Fr,w)==0
    assert S.diff(Hr,v)==-z and S.diff(Hr,w)==2*mg*Sg/Lg
    # On Fz=0, the exact upper-jet derivatives are independent of all
    # other canonical fields and even of the dust parameters.
    plgr=(q['pSg']*dict(zip(p['Q'],p['dq']))['Sg']+q['pg']*dict(zip(p['Q'],p['dq']))['tg']-K*z/R)/Lg
    shell={k:S.factor(S.cancel(x.subs(dict(zip(p['Q'],p['dq']))['pLg'],plgr)))
           for k,x in observed.items()}
    targets={'bm_v':3*z*(1-z*z)/Lf**2,
             'delta_v':z*(1-z*z)/(Lg*Lf),
             'delta_w':-2*mg*Sg*(1-z*z)/(Lg**2*Lf)}
    assert all(S.factor(shell[k]-targets[k])==0 for k in targets)
    # Canonical triangularization: after subtracting Fr from B_M and Hr
    # from B_N-z*C/Lg, their selected highest jet coefficients vanish.
    alpha=-3*z*(1-z*z)/(Lg*Lf**2)
    beta=-(1-z*z)/(Lg*Lf)
    assert S.factor(shell['bm_v']+alpha*Lg)==0
    assert S.factor(shell['delta_w']-beta*2*mg*Sg/Lg)==0
    assert S.factor(shell['delta_v']+beta*z)==0
    # FULL universal B_M reduction, not just a principal-symbol identity.
    # The pLg' elimination enforces Fz=0 exactly; the result is identically
    # zero for arbitrary remaining canonical jets, dust, potentials and z.
    # Expanding first prevents a costly monolithic radical simplification.
    bm_remainder=(bm-alpha*Fr).subs(dict(zip(p['Q'],p['dq']))['pLg'],plgr)
    bm_remainder=S.cancel(S.collect(S.powsimp(S.expand(bm_remainder),force=True),[R,1/R]))
    assert bm_remainder==0, 'Universal B_M factor on Fz=0 failed'
    assert S.diff(bm-alpha*Fr,dict(zip(p['Q'],p['dq']))['pLg'],3)==0
    return {'original_blobs':BLOBS,
            'off_shell_high_jet_partial_identities':3,
            'universal_BM_on_Fz_zero':'B_M=-3*z*(1-z**2)/(Lg*Lf**2)*Fz_r',
            'universal_BM_on_Fz_and_Fzr_zero':'EXACT_ZERO',
            'on_Fz_zero_derivatives':{k:str(v) for k,v in targets.items()},
            'triangular_coefficients':{'B_M_minus_alpha_Fzr':str(alpha),
                                       'BN_minus_zC_over_Lg_minus_beta_Hgr':str(beta)},
            'scope':'B_M fully reduced on Fz=0; B_N only principal jets; lower-jet B_N residual NOT proved zero',
            'universal_B_factorization':'B_M PROVED; B_N-z*C/Lg NOT_PROVED',
            'physical_Step55_six_coefficients':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(certificate(),indent=2))

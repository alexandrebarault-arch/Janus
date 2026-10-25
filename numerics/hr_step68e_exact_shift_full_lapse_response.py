"""Step68e physical original Step45: full relative-shift response N,N',M,M'.

Unlike earlier Step68d, also derives lower N,M lapse responses, at fixed
canonical Hamiltonian envelope on stationary K>0 chart. All six original
pairs and both dusts are retained. Does NOT evaluate temporal secondary
operator, impose full constraints or compute Dirac rank.
"""
from __future__ import annotations
from functools import lru_cache
from hashlib import sha1,sha256
from pathlib import Path
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward

SOURCE_SHA='66aa43841dccfe4a5d586a49be9c10af3a67a10e'

def authenticate():
    raw=Path(__file__).with_name('hr_step45_exact_physical_ward.py').read_bytes()
    sha=sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
    if sha!=SOURCE_SHA:raise ValueError('original Step45 SHA drift: '+sha)
    return sha

def plus(a,b):
    return {i:a.get(i,sp.S.Zero)+b.get(i,sp.S.Zero) for i in set(a)|set(b)}

def scale(expr,a):
    return {i:expr*v for i,v in a.items() if expr!=0}

@lru_cache(1)
def full_shift_operator():
    authenticate()
    p=exact_physical_ward()
    assert all(v==0 for v in p['residuals'].values())
    q=dict(zip(p['Q'],p['q'])); qp=dict(zip(p['Q'],p['dq']))
    Lg,Lf,Sg,Sf=q['Lg'],q['Lf'],q['Sg'],q['Sf']
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=p['parameters']
    D=q['pSg']*qp['Sg']-Lg*qp['pLg']+q['pg']*qp['tg']
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    K=m2*mg*Lg*Lf*At
    root=sp.sqrt(1-z*z)
    zd=root**3/K
    zk=-z*(1-z*z)/K
    Dt=p['total_derivative']
    result={}
    for lapse, E in [('N',p['eg']),('M',p['ef'])]:
        dD={};dK={}
        for i,(name,field) in enumerate(zip(p['Q'],p['q'])):
            partner=i+1 if i%2==0 else i-1
            symp=sp.S.One if i%2==0 else -sp.S.One
            X={j:symp*E[j][partner] for j in range(3)}
            Xr={j:Dt(v)+X.get(j-1,sp.S.Zero) for j,v in X.items()}
            Xr[3]=X[2]
            dD=plus(dD,plus(scale(sp.diff(D,field),X),scale(sp.diff(D,p['dq'][i]),Xr)))
            dK=plus(dK,scale(sp.diff(K,field),X))
        shift=plus(scale(zd,dD),scale(zk,dK))
        # Must vanish for all derivatives >= 2 as Step58 independently found.
        for i in (2,3):
            assert sp.cancel(sp.together(shift.get(i,0)))==0,(lapse,i,shift.get(i))
        shift={i:sp.cancel(sp.together(v)) for i,v in shift.items() if i<=1}
        result[lapse]={'delta_D':dD,'delta_K':dK,'delta_z':shift}
    # Standalone independent original Step45 derivation; do NOT depend on the
    # transcribed 68b/68c or the Step58 implementation for the coefficient.
    stationarity_sub={qp['pLg']:(q['pSg']*qp['Sg']+q['pg']*qp['tg']-K*z/root)/Lg}
    Hg=p['Hg'].subs(stationarity_sub)
    # Reproduce Step68d N',M' identity as independent tests.
    targetN=zd*Hg-(1-z*z)/Lg
    targetM=(1-z*z)/Lf
    assert sp.factor(sp.cancel(result['N']['delta_z'][1].subs(stationarity_sub)-targetN))==0
    assert sp.factor(sp.cancel(result['M']['delta_z'][1].subs(stationarity_sub)-targetM))==0
    result['data']={'p':p,'D':D,'K':K,'zd':zd,'zk':zk,'shell':stationarity_sub,
                    'Hg_shell':Hg,'q':q,'qp':qp}
    return result


@lru_cache(1)
def first_stationarity_quotient():
    """Complete q'' removal from the physical M-lapse delta-z coefficient.

    On Fz=0, the M (undifferentiated lapse) shift response carries exactly
    three independent second canonical jets: pLg'', Sg'', theta_g''.
    Subtracting the *complete* radial derivative of shift stationarity
    Fz', with its specific coefficient, removes ALL of them.  One cannot
    set second jets to zero in the unreduced operator instead.
    """
    v=full_shift_operator();p=v['data']['p'];q=v['data']['q']; shell=v['data']['shell']
    Lg,Lf=q['Lg'],q['Lf'];z=p['parameters'][-3];K=v['data']['K']
    Dt=p['total_derivative']
    F1=Dt(p['Fz']).subs(shell)
    n0=v['N']['delta_z'][0].subs(shell)
    m0=v['M']['delta_z'][0].subs(shell)
    # Alpha is a coefficient of F_z' (NOT a lapse multiplier).
    alpha=-z*(1-z*z)**sp.Rational(3,2)/(Lf*K)
    jet=p['ddq']; names=p['Q']
    assert all(not n0.has(j) for j in jet)
    present={names[i]:sp.factor(sp.diff(m0,j))
             for i,j in enumerate(jet) if m0.has(j)}
    assert set(present)=={'pLg','Sg','tg'}
    assert sp.factor(sp.cancel(sp.diff(m0,jet[names.index('pLg')])-alpha*Lg))==0
    # The whole q''-dependence must cancel, not merely its principal part.
    remainder=m0+alpha*F1
    residuals={names[i]:sp.factor(sp.cancel(sp.diff(remainder,j)))
               for i,j in enumerate(jet) if remainder.has(j)}
    assert all(value==0 for value in residuals.values()),residuals
    # Check the dependence is genuinely linear in the independent second
    # canonical jets (no hidden quadratic terms).
    for j in jet:
        if m0.has(j):
            assert all(sp.diff(m0,j,k)==0 for k in jet)
    reduced=sp.factor(sp.cancel(remainder))
    assert not any(reduced.has(j) for j in jet)
    # Negative controls: missing or wrong Fz' term leaves all three jets.
    wrong=m0-alpha*F1
    assert sp.cancel(sp.diff(wrong,jet[names.index('pLg')]))!=0
    assert sp.cancel(sp.diff(m0,jet[names.index('pLg')]))!=0
    return {'alpha':alpha,'Fz_prime':F1,'before':m0,'after':reduced,
            'N0_no_second_jets':True,'present_jets':present,
            'second_jet_residuals':residuals,'shift_stationarity_shell':shell}


def center_regular_quotient():
    """Exact scaling of apparently singular alpha*Fz' on analytic parity.

    Fz=r^3 f(s), K=r^2 k(s), z=r w(s); the quotient is O(r),
    provided the normalised residual and its first s-derivative exist.
    """
    r,s=sp.symbols('r s',positive=True)
    w,k,Lf=sp.symbols('w k Lf',positive=True)
    f,fs=sp.symbols('f fs',real=True)
    t=1-s*w*w
    alpha=-w*t**sp.Rational(3,2)/(r*Lf*k)
    F1=r*r*(3*f+2*s*fs)
    product=sp.factor(alpha*F1)
    scaled=-r*w*t**sp.Rational(3,2)*(3*f+2*s*fs)/(Lf*k)
    assert sp.simplify(product-scaled)==0
    assert sp.limit(product,r,0)==0
    return {'alpha':alpha,'Fz_prime':F1,'product':product,
            'regular_center_limit':sp.S.Zero}


def manifest():
    v=full_shift_operator()
    quotient=first_stationarity_quotient(); center=center_regular_quotient()
    return {'step':'68e','original_step45_blob':authenticate(),
            'full_relative_shift_variation_order':{x:sorted(v[x]['delta_z']) for x in ('N','M')},
            'lower_lapse_coefficients_on_Fz':{x:{'opcount':sp.count_ops(v[x]['delta_z'][0].subs(v['data']['shell'])),
                 'srepr_sha256':sha256(sp.srepr(v[x]['delta_z'][0].subs(v['data']['shell'])).encode()).hexdigest()}
                 for x in ('N','M')},
            'Nprime_exact_on_Fz':'sqrt(1-z²)^3*Hg/K-(1-z²)/Lg',
            'Mprime_exact_on_Fz':'(1-z²)/Lf',
            'six_original_canonical_pairs':True,
            'M0_shift_second_jet_preconstraint':sorted(quotient['present_jets']),
            'M0_quotient_alpha_times_Fz_prime':str(quotient['alpha']),
            'M0_residual_second_jets':{k:str(x) for k,x in quotient['second_jet_residuals'].items()},
            'M0_quotient_no_second_jets':True,
            'N0_has_no_second_jets':quotient['N0_no_second_jets'],
            'M0_quotient_opcount':sp.count_ops(quotient['after']),
            'Fz_prime_center_quotient_product':str(center['product']),
            'Fz_prime_quotient_regular_at_center':True,
            'full_temporal_Cdot_low_lapse_operator':'NOT_REDUCED',
            'Step55_certified_radial_profile_used':False,
            'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

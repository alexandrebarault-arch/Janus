"""Step68c original-byte-authentic Step45 six-pair Hamiltonian center parity audit.

Use EXACT historical original hr_step45_exact_physical_ward.py bytes and its
precomputed six-pair Euler jets, not re-entered formulas. The central family
is analytic, with independent N and M even lapses and specified initial
radial primaries, but it does NOT establish full secondary time consistency.
"""
from __future__ import annotations
import hashlib
import json
from functools import lru_cache
from pathlib import Path
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward

SOURCE_BLOB = "66aa43841dccfe4a5d586a49be9c10af3a67a10e"
Q = ('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')


def authenticate():
    raw = Path(__file__).with_name('hr_step45_exact_physical_ward.py').read_bytes()
    sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if sha != SOURCE_BLOB:
        raise ValueError('Step45 source drift: expected authentic '+SOURCE_BLOB+' actual '+sha)
    return sha


@lru_cache(1)
def original_center():
    authenticate()
    p = exact_physical_ward()
    if p['Q'] != Q or any(v != 0 for v in p['residuals'].values()):
        raise AssertionError('six-pair source or Ward identities broken')
    r = sp.symbols('r',positive=True)
    a,a2,b,bf2,G,G2,P3,rhog,rhof,U,V,kg0,kf0,w = sp.symbols(
        'a a2 b bf2 G G2 P3 rhog rhof U V kg0 kf0 w',real=True)
    N0,N2,N4,M0,M2,M4 = sp.symbols('N0 N2 N4 M0 M2 M4',real=True)
    metrics = {'Lg': a+a2*r**2,'Lf':b+bf2*r**2,
               'Sg':a*r+a2*r**3,'Sf':b*r+bf2*r**3}
    profiles = {**metrics,'pLg':G*r**2+G2*r**4,
                'pSg':2*G*r+P3*r**3,'pg':rhog*r**2,
                'pLf':U*r**2,'pSf':V*r,'pf':rhof*r**2,
                'tg':sp.S.Zero,'tf':sp.S.Zero}
    sub={}
    for name,value in profiles.items():
        i=Q.index(name)
        sub[p['q'][i]]=value
        sub[p['dq'][i]]=sp.diff(value,r)
        sub[p['ddq'][i]]=sp.diff(value,r,2)
    for name,k,metric in [('tg',kg0,metrics['Lg']),('tf',kf0,metrics['Lf'])]:
        i=Q.index(name)
        sub[p['dq'][i]]=k*r*metric
        sub[p['ddq'][i]]=sp.diff(k*r*metric,r)
    sub.update(zip(p['parameters'][-3:],(w*r,w,sp.S.Zero)))
    X={}
    for label,grads,l0,l2,l4 in [('N',p['eg'],N0,N2,N4),('M',p['ef'],M0,M2,M4)]:
        lapses=(l0+l2*r*r+l4*r**4,2*l2*r+4*l4*r**3,2*l2+12*l4*r*r)
        for i,name in enumerate(Q):
            other=i+1 if i%2==0 else i-1
            sign=1 if i%2==0 else -1
            expression=sign*sum(grads[j][other]*lapses[j] for j in range(3))
            X[label,name]=expression.subs(sub)
    symbols=locals()
    return symbols


def at_order(expr,r,n):
    """Coefficient of r^n, asserting no lower singular/power terms."""
    return sp.simplify(sp.limit(expr/r**n,r,0))


@lru_cache(1)
def verify_leading():
    v=original_center();r=v['r']; X=v['X']
    a,b,G,U,V,mg,mf=(v['a'],v['b'],v['G'],v['U'],v['V'],
                       v['p']['parameters'][0],v['p']['parameters'][1])
    rows={}; off={}
    for sector in ('N','M'):
        lead={f:sp.factor(at_order(X[sector,f],r,n))
              for f,n in [('Lg',0),('Sg',1),('pLg',2),('pSg',1),
                          ('Lf',0),('Sf',1),('pLf',2),('pSf',1)]}
        assert sp.factor(lead['Lg']-lead['Sg']) == 0
        assert sp.factor(lead['pSg']-2*lead['pLg']) == 0
        off[sector]={
            'f_metric':sp.factor(lead['Lf']-lead['Sf']),
            'f_momentum':sp.factor(lead['pSf']-2*lead['pLf'])}
        assert all(sp.factor(x.subs(V,2*U))==0 for x in off[sector].values())
        # The genuine f-sector primary imposes V=2U in the center chart.
        for f in ('Lf','Sf','pLf','pSf'):
            lead[f]=sp.factor(lead[f].subs(V,2*U))
        assert sp.factor(a*(lead['pSg']-2*lead['pLg'])
                         +2*G*(lead['Sg']-lead['Lg']))==0
        rows[sector]=lead
    assert sp.factor(off['M']['f_metric'] - v['M0']*(2*U-V)/(2*b*mf))==0
    assert sp.factor(off['M']['f_momentum'] - v['M0']*U*(2*U-V)/(2*b*b*mf))==0
    assert sp.factor(sp.diff(rows['N']['pLg'],v['N2'])+4*mg)==0
    assert sp.factor(sp.diff(rows['N']['pSg'],v['N2'])+8*mg)==0
    assert sp.factor(sp.diff(rows['M']['pLf'],v['M2'])+4*mf)==0
    assert sp.factor(sp.diff(rows['M']['pSf'],v['M2'])+8*mf)==0
    return {'rows':rows,'offshell':off,'source_sha':authenticate()}



@lru_cache(1)
def center_shift_response():
    """Genuine Step45 Hamiltonian first variations of normalised shift jets.

    The full 12-component original symplectic field is used. The g shift
    stationarity fixes the central third jet P3, and f radial momentum
    primary fixes V=2U. This IS NOT a proof of time preservation of C.
    """
    v=original_center(); p=v['p'];r=v['r']; X=v['X'];pr=v['profiles']
    a,b,G,G2,U,V,w,P3=(v[t] for t in ('a','b','G','G2','U','V','w','P3'))
    mg,mf,m2,b0,b1,b2,b3,b4=p['parameters'][:8]
    T=b1*a*a+2*b2*a*b+b3*b*b
    k0=m2*mg*a*b*T
    # From Dg=pSg Sg' - Lg pLg' + pg theta_g',
    # the coefficient r^3 is the displayed polynomial.
    d3_background=4*G*v['a2']+a*P3-4*a*v['G2']+a*v['kg0']*v['rhog']
    stationary_P3=sp.solve(d3_background-k0*w,P3)[0]
    Hg0=sp.factor(at_order(p['Hg'].subs(v['sub']),r,2))
    result={}
    for label in ('N','M'):
        orders={'pSg':3,'Sg':3,'Lg':2,'pLg':4,'pg':2,'tg':2}
        # This extracts every Hamiltonian radial jet required by delta Dg;
        # no third-derivative field is frozen, and dust is retained.
        x={field:sp.series(X[label,field],r,0,n+1).removeO().expand()
           for field,n in orders.items()}
        shift_change=sp.expand(
            x['pSg']*sp.diff(pr['Sg'],r)
            +pr['pSg']*sp.diff(x['Sg'],r)
            -x['Lg']*sp.diff(pr['pLg'],r)
            -pr['Lg']*sp.diff(x['pLg'],r)
            +x['pg']*v['sub'][p['dq'][Q.index('tg')]]
            +pr['pg']*sp.diff(x['tg'],r))
        linear=sp.factor(shift_change.coeff(r,1))
        if linear!=0:raise AssertionError('delta Dg contains forbidden r term')
        ed=sp.factor(shift_change.coeff(r,3).subs(P3,stationary_P3).subs(V,2*U))
        da=at_order(X[label,'Lg'],r,0)
        db=at_order(X[label,'Lf'],r,0).subs(V,2*U)
        ek=sp.factor(sp.diff(k0,a)*da+sp.diff(k0,b)*db)
        dzprime=sp.factor((ed-w*ek)/k0)
        assert all(sp.diff(dzprime,j)==0 for j in (v['N4'],v['M4']))
        result[label]={'ed_center':ed,'ek_center':ek,'delta_zprime_center':dzprime,
                       'forbidden_linear_Dg':linear}
    # New universal highest-lapse-jet coefficients at center.
    assert sp.factor(sp.diff(result['M']['delta_zprime_center'],v['M2'])-2/b)==0
    assert sp.factor(sp.diff(result['N']['delta_zprime_center'],v['N2'])
                     -(2*Hg0/k0-2/a))==0
    assert sp.factor(sp.diff(result['N']['delta_zprime_center'],v['M2']))==0
    assert sp.factor(sp.diff(result['M']['delta_zprime_center'],v['N2']))==0
    assert k0 != 0
    return {'result':result,'k0':k0,'Hg0':Hg0,'P3_on_shift_stationarity':stationary_P3,
            'M2_coeff':sp.S(2)/b,'N2_coeff':sp.factor(2*Hg0/k0-2/a),
            'N2_on_Hg_primary':-2/a,'M2_on_Hg_primary':2/b,
            'conditions':'K/r²=k0 !=0, a,b !=0, Fz=0 at r³, f radial momentum primary V=2U, even lapse and regular analytic parity at r=0'}

def manifest():
    x=verify_leading(); shifted=center_shift_response()
    return {'step':'68c','historical_source_blob':x['source_sha'],
            'original_step45_six_pair_ward_reexecuted':True,
            'all_nine_original_ward_residuals_exact_zero':True,
            'original_euler_jet_center_parity':True,
            'required_f_primary':'pSf/r=2U',
            'N_M_lapses_independent_even_at_center':True,
            'negative_off_f_primary':{k:{j:str(z) for j,z in vals.items()}
                                     for k,vals in x['offshell'].items()},
            'jet_signs_N2_M2_verified':True,
            'shift_stationarity_coefficient_P3':str(shifted['P3_on_shift_stationarity']),
            'center_normalized_k0':str(shifted['k0']),
            'N2_in_delta_zprime_general':str(shifted['N2_coeff']),
            'N2_in_delta_zprime_on_Hg0':str(shifted['N2_on_Hg_primary']),
            'M2_in_delta_zprime':str(shifted['M2_on_Hg_primary']),
            'center_e_d_and_e_k_from_authentic_Hamiltonian':True,
            'full_trajectory_e_d_e_k':'NOT_COMPUTED; ONLY exact center coefficients computed',
            'temporal_Dirac_rank':'NOT_COMPUTED',
            'original_non_IBP_independent_oracle':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(manifest(),indent=2))

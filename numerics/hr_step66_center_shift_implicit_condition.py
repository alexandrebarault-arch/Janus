"""Step66: exact center-normalized implicit-function and C2 sensitivity of HR shift.

Physics input (previously certified, NOT rerun here): original positive-EH,
6-canonical-pair, 2-moving-dust Step55 interval benchmark: r in [0,17/20],
K/r**2 = k > 229/1000 for r>0, continuous positive k at r=0,
and z/r = w = 1/250. On parity charts Dg=r**3*d, K=r**2*k,
Fz=Dg-K*z/sqrt(1-z*z), z=r*w.  This supplies a previously missing
center-safe UNIFORM quantitative implicit-function estimate, including
second Frechet derivatives, but NOT the full Dirac temporal rank.

All inequalities in the certificate are Fraction EXACT, no floating point.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sympy as sp

S_MAX=F(289,400)
R_MAX=F(17,20)
K_LOWER=F(229,1000)
W_BENCH=F(1,250)
STEP55_PHYSICAL_CERTIFIED_REPORT='research/reports/gate2b-step55-report.json'
STEP55_CERTIFICATES_ALREADY_ASSUMED={
    'K_over_r2_gt':'229/1000',
    'z_over_r':'1/250',
    'r_in':'[0,17/20]',
    'scope':'positive regular fixed Step55 benchmark ONLY',
}

@lru_cache(maxsize=1)
def normalized_shift_identity():
    """Derive the physical Fz root and ALL first/second normalized jets."""
    s,d,k,w=sp.symbols('s d k w',real=True)
    root=sp.sqrt(k*k+s*d*d)
    W=d/root
    t=1-s*w*w
    # Exact normalized algebraic stationarity on its positive chart:
    # original Fz/r**3=d-k*w/sqrt(1-s*w**2).
    Fhat=d-k*w/sp.sqrt(t)
    Fhat_w=sp.factor(sp.diff(Fhat,w))
    assert sp.simplify(Fhat_w+k/t**sp.Rational(3,2))==0
    Wd=sp.diff(W,d);Wk=sp.diff(W,k)
    Wdd=sp.factor(sp.diff(Wd,d))
    Wdk=sp.factor(sp.diff(Wd,k))
    Wkk=sp.factor(sp.diff(Wk,k))
    assert sp.simplify(Wd-k*k/root**3)==0
    assert sp.simplify(Wk+k*d/root**3)==0
    assert sp.simplify(Wdd+3*s*k*k*d/root**5)==0
    assert sp.simplify(Wdk-k*(2*s*d*d-k*k)/root**5)==0
    assert sp.simplify(Wkk-d*(2*k*k-s*d*d)/root**5)==0
    # On w=d/R, k>0, |w|<1/sqrt(s),
    # d=k*w/sqrt(1-s*w²). Avoid SymPy's sqrt(k²) sign ambiguity;
    # work directly with w,k and positive t.
    wd=t**sp.Rational(3,2)/k
    wk=-w*t/k
    wdd=-3*s*w*t*t/(k*k)
    wdk=(3*s*w*w-1)*t**sp.Rational(3,2)/(k*k)
    wkk=w*(2-3*s*w*w)*t/(k*k)
    # The normalized implicit-function theorem is regular AT s=0.
    assert sp.factor(Fhat_w.subs(s,0)+k)==0
    assert sp.factor(wd.subs(s,0)-1/k)==0
    assert sp.factor(wk.subs(s,0)+w/k)==0
    # Differentiate the stationary identity Fhat(s,d,k,W(s,d,k))
    # at fixed s, holding k>0 and w on the regular branch.
    assert sp.simplify(sp.diff(Fhat,d)+Fhat_w*wd)==0
    assert sp.simplify(sp.diff(Fhat,k)+Fhat_w*wk)==0
    return dict(s=s,d=d,k=k,w=w,root=root,W=W,Fhat=Fhat,
                Fhat_w=Fhat_w,Wd=Wd,Wk=Wk,Wdd=Wdd,Wdk=Wdk,Wkk=Wkk,
                wd=wd,wk=wk,wdd=wdd,wdk=wdk,wkk=wkk,
                t=t)


def exact_global_bounds():
    """Strict RATIONAL inequalities valid at every point of Step55 benchmark.

    These bounds rely on (do NOT recompute) the Step55 K/r² positivity
    and prescribed w=0.004. End-point s=0 is included using w=z/r.
    """
    assert S_MAX==R_MAX*R_MAX
    tmin=1-S_MAX*W_BENCH*W_BENCH
    assert F(9999,10000)<tmin<=1
    k=K_LOWER; w=W_BENCH;s=S_MAX
    # |∂w/∂d| <= 1/k; |∂w/∂k| <= w/k.
    wd_cap=1/k
    wk_cap=w/k
    # Hessian on actual constrained family (w=1/250):
    # t∈[tmin,1], t^(3/2) <=1, |3s w²-1|<1,
    # 0<2-3s w²<2, all using only rational algebra.
    assert 0<3*s*w*w<1
    wdd_cap=3*s*w/(k*k)
    wdk_cap=1/(k*k)
    wkk_cap=2*w/(k*k)
    assert wdd_cap<F(1,5)
    assert wdk_cap<F(20)
    assert wkk_cap<F(1,5)
    assert wd_cap<F(22,5)
    assert wk_cap<F(1,50)
    # Normalized stationarity dFhat/dw=-k/t^(3/2), so
    # |dFhat/dw| >= k > 229/1000 even at s=0.
    assert tmin>0
    return {
        's_interval':['0',str(S_MAX)],
        'r_interval':['0',str(R_MAX)],
        't_min_exact':str(tmin),
        'shift_stationarity_normalized_derivative_abs_gt':str(K_LOWER),
        'dw_dd_abs_le':str(wd_cap),
        'dw_dk_abs_le':str(wk_cap),
        'wdd_abs_lt':'1/5',
        'wdk_abs_lt':'20',
        'wkk_abs_lt':'1/5',
        'computational_witness_hessian_caps':{
           'wdd':str(wdd_cap),'wdk':str(wdk_cap),'wkk':str(wkk_cap)},
        'strict_wd_lt':'22/5',
        'strict_wk_lt':'1/50',
        'center_included':True,
        'uncertainty':'Depends on certified original Step55 k>229/1000 and imposed z/r=1/250 benchmark; does NOT hold for K=0 or arbitrary HR model.'
    }


def parity_preserving_shift_variation():
    """On Dg=r³d,K=r²k,z=r*w, derive bounded delta(z/r)."""
    p=normalized_shift_identity()
    w,k,s=p['w'],p['k'],p['s']
    dd,dk=sp.symbols('delta_d delta_k',real=True)
    t=1-s*w*w
    delta_w=p['wd']*dd+p['wk']*dk
    delta_z=sp.Symbol('r',nonnegative=True)*delta_w
    return {'delta_w':delta_w,'delta_z':delta_z,
            'delta_d':dd,'delta_k':dk,
            'bound':'|delta(z/r)| <= (|delta d|+|delta k|/250)/(229/1000) on the prescribed constrained background',
            'origin':'Dg=r³d, K=r²k, z=r w; normalized implicit map regular at center',
            'full_rank_warning':'Pointwise invertibility of shift Fz does not establish Dirac constraint rank or lapse fixing.'}


def fail_closed_parameters(s_lo,s_hi,k_lower,w_fixed):
    if (F(s_lo),F(s_hi))!=(F(0),S_MAX):
        raise ValueError('Unsupported radial chart; cannot claim Step55 certificate')
    if F(k_lower)!=K_LOWER or F(w_fixed)!=W_BENCH:
        raise ValueError('Benchmark shift/K lower bound mismatch')
    return exact_global_bounds()


def manifest():
    a=normalized_shift_identity();b=exact_global_bounds();c=parity_preserving_shift_variation()
    return {'step':66,'claim':'CENTER-REGULAR NORMALIZED physical HR relative-shift implicit map is uniformly C2 conditioned on fixed certified Step55 radial initial-data benchmark',
            'data_dependencies':STEP55_CERTIFICATES_ALREADY_ASSUMED,
            'physical_original_Step45_55_imported_in_this_module':False,
            'analytic_Fhat':'d - k*w/sqrt(1-s*w²)',
            'Fhat_w':str(a['Fhat_w']),
            'w_root':str(a['W']),
            'w_gradient':{'d':str(a['wd']),'k':str(a['wk'])},
            'w_hessian':{'dd':str(a['wdd']),'dk':str(a['wdk']),'kk':str(a['wkk'])},
            'rigorous_rational_benchmark_enclosures':b,
            'delta_w':str(c['delta_w']),
            'original_full_temporal_Dirac_on_Step55':'NOT_COMPUTED',
            'lapse_rank_and_fixing':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

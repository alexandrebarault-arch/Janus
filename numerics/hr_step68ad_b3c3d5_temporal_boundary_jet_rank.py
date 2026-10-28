"""b3c3d5: exact local Step58 lapse-jet projection and boundary-curvature test.

The algebraic theorem concerns one point of the Step58 temporal equation,
not global solutions or the physical Dirac/gauge quotient. The optional
original-source probe must be run inside the complete research checkout.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha1
import json
import sympy as sp

PINNED = {
    'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
    'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
    'hr_step68o_temporal_interval_annulus.py':'c99caebc17f243784450ddff94fb061767e6d8e7',
}

def classify(A_N,A_M,B_N,B_M,c_N,c_M):
    """Exact pointwise projection of A_N N+A_M M+B_N N'+B_M M'=0.

    All arguments must be exact numbers, not uncertified interval midpoints.
    A rank-2 projection means arbitrary endpoint values are compatible with
    some FIRST jets at that point, not a global smooth positive-lapse solution.
    """
    if any(isinstance(z,float) for z in (A_N,A_M,B_N,B_M,c_N,c_M)):
        raise ValueError('Floating coefficients are not certified exact')
    a,b,u,v,x,y=map(sp.sympify,(A_N,A_M,B_N,B_M,c_N,c_M))
    if any(z.free_symbols for z in (a,b,u,v,x,y)):
        raise ValueError('Use exact instantiated coefficients')
    if u!=0 or v!=0:
        return {'jet_equation_rank':1,'endpoint_projection_rank':2,
                'derivative_to_solve':"Mprime" if v!=0 else "Nprime",
                'curvature_zero_for_all_endpoint_variations':x==0 and y==0}
    if a!=0 or b!=0:
        return {'jet_equation_rank':1,'endpoint_projection_rank':1,
                'endpoint_tangent':[str(b),str(-a)],
                'curvature_on_tangent':str(sp.cancel(x*b-y*a)),
                'curvature_zero_for_all_endpoint_variations':sp.cancel(x*b-y*a)==0,
                'positive_lapse_pair_possible':bool(a*b<0)}
    return {'jet_equation_rank':0,'endpoint_projection_rank':2,
            'curvature_zero_for_all_endpoint_variations':x==0 and y==0}

def center_clock_drift():
    """Strict consequence of the previously published b3c2 center ratio.

    Assumes N(0)>0, smooth even lapses, regular shift, authentic Step58
    preservation on Step55, and (for the MVT) clock-rate stationarity at R.
    Does not assert existence of a global Step58 lapse solution.
    """
    rho_lo,rho_hi=F(1037,2000),F(2593,5000)
    R=F(17,20)
    return {'center_clock_rate_over_N0_strict': [str(1-rho_hi),str(1-rho_lo)],
            'some_radial_derivative_over_N0_strict_upper':str(-(1-rho_hi)/R),
            'assumptions':'b3c2 central Step58 coefficient, N0>0, regular clocks/shift; w(R)=0 and w C1 for MVT'}

def algebraic_checks():
    q,a,b,T,U,sg,sf,z,N,M=sp.symbols('q a b T U sg sf z N M',positive=True)
    Lg,Lf=sp.symbols('Lg Lf',positive=True)
    H=Lg*a+Lf*b
    cN=-z*a+H*(sg+z*T/Lg)/(T+U)
    cM=-z*q*a-H*(sf-z*T/Lf)/(T+U)
    cM=sp.factor(cM.subs(q,Lg/Lf));q=Lg/Lf
    AN,AM,BN,BM,Np,Mp=sp.symbols('AN AM BN BM Np Mp')
    rho=sp.symbols('rho')
    n=sp.symbols('n')
    m=sp.Function('m')(n)
    Fboundary=cN*n+cM*m
    eq=AN*N+AM*M+BN*Np+BM*Mp
    checks={
      'lapse_combination':cM-q*cN+H*(sf+q*sg)/(T+U),
      'graph_pullback':sp.diff(Fboundary,n)-(cN+cM*sp.diff(m,n)),
      'ratio_pullback':sp.diff(Fboundary.subs(m,rho*n),n)-(cN+rho*cM),
      'Mprime_solves':eq.subs(Mp,-(AN*N+AM*M+BN*Np)/BM),
      'Nprime_solves':eq.subs(Np,-(AN*N+AM*M+BM*Mp)/BN),
      'algebraic_null_vector':(AN*N+AM*M).subs({N:AM,M:-AN}),
      'algebraic_tangent_curvature':(cN*N+cM*M).subs({N:AM,M:-AN})-(cN*AM-cM*AN),
      'ratio_cancellation':(cN+rho*cM).subs(rho,-cN/cM),
      'two_lapse_jet_freedom':eq.subs({BN:1,BM:0,Np:-AN*N-AM*M}),
      'clock_drift_center_lower':sp.Rational(1)-sp.Rational(2593,5000)-sp.Rational(2407,5000),
      'clock_drift_center_upper':sp.Rational(1)-sp.Rational(1037,2000)-sp.Rational(963,2000),
      'mean_value_threshold':sp.Rational(2407,5000)/sp.Rational(17,20)-sp.Rational(2407,4250),
    }
    failed={k:str(sp.factor(v)) for k,v in checks.items() if sp.simplify(v)!=0}
    if failed:raise AssertionError(failed)
    assert classify(2,3,1,0,4,5)['endpoint_projection_rank']==2
    assert classify(2,-3,0,0,3,2)['endpoint_projection_rank']==1
    assert classify(0,0,0,0,1,0)['endpoint_projection_rank']==2
    assert classify(2,-3,0,0,3,2)['curvature_zero_for_all_endpoint_variations'] is False
    assert classify(2,-3,0,0,2,-3)['curvature_zero_for_all_endpoint_variations'] is True
    assert classify(2,3,0,0,3,2)['positive_lapse_pair_possible'] is False
    return {'step':'b3c3d5','symbolic_zero_residuals':len(checks),
            'exact_classification_checks':6,'clock_drift':center_clock_drift(),
            'scope':'POINTWISE_TEMPORAL_JET_RANK_AND_CONDITIONAL_CENTER_DRIFT_NOT_GLOBAL_DIRAC',
            'original_step58_probe_executed':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

def probe_original_outer():
    """Optional genuine Step58 coefficient probe at R=17/20 (not a sign proof).

    Requires complete SHA-pinned repo checkout. Outward interval results
    crossing zero are explicitly INCOMPLETE, never replaced by midpoint.
    """
    base=Path(__file__).resolve().parent
    for name,expected in PINNED.items():
        raw=(base/name).read_bytes()
        got=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if got!=expected:raise ValueError(f'Source drift {name}: {got}')
    from . import hr_step68o_temporal_interval_annulus as annulus
    from . import hr_step55_global_barrier as old
    from .hr_step58_temporal_operator import physical_operator
    from .hr_step45_exact_physical_ward import exact_physical_ward
    from .hr_step68n_interval_ode_jets import I
    data,R,_,_=annulus.canonical_jets_cell(F(17,20),F(17,20))
    op=physical_operator();p=exact_physical_ward()
    vals={}
    for keys,degree in ((op['q'],0),(op['qp'],1),(op['qpp'],2),(op['qppp'],3)):
        for symbol,name in zip(keys,p['Q']):
            vals[symbol]=data[name].a[degree]*(1,1,2,6)[degree]
    for name,value in (('z',R*old.Z1),('zr',old.Z1),('zrr',I.c(0)),('zrrr',I.c(0))):
        vals[op[name]]=value
    for symbol,name in zip(p['parameters'][:8],('MG','MF','M2','B0','B1','B2','B3','B4')):
        vals[symbol]=getattr(old,name)
    result={}
    for label in ('N','M'):
        if any(k>2 for k in op['operator'][label]):
            raise ValueError('Unexpected higher lapse jets: extend probe before using')
        result[label]={}
        for degree in (0,1,2):
            expr=op['operator'][label].get(degree,sp.S.Zero)
            if any(expr.has(s) for s in op['q4']):
                raise ValueError('Fourth canonical jet required: do not replace by zero')
            safe=expr.replace(lambda x:x.is_Pow and x.exp.is_Rational and x.exp.q==2,
                              lambda x:sp.Function('interval_halfpow')(x.base,sp.Integer(x.exp.p)))
            symbols=sorted(expr.free_symbols,key=str)
            fn=sp.lambdify(symbols,safe,modules=[{'interval_halfpow':lambda x,k:x.sqrt()**int(k),
                                                  'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
            missing=[str(s) for s in symbols if s not in vals]
            if missing:raise ValueError('Missing original symbols: '+str(missing))
            v=I.c(fn(*[vals[s] for s in symbols]))
            result[label][str(degree)]={'lower':str(F(v.lo,old.S)),
                                       'upper':str(F(v.hi,old.S)),
                                       'sign':'POS' if v.lo>0 else 'NEG' if v.hi<0 else 'INCOMPLETE'}
    return {'radius':'17/20','original_sources':PINNED,'coefficients':result,
            'interpretation':'OUTWARD_INTERVAL_POINTWISE_JET_PROBE; NOT LAPSING SOLUTION OR DIRAC TANGENCY',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--probe-original',action='store_true')
    args=parser.parse_args()
    print(json.dumps(probe_original_outer() if args.probe_original else algebraic_checks(),indent=2))

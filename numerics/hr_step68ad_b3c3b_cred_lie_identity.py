"""Exact radial Lie covariance of Step45 C and its positive-K reduced pullback.
Run: python -m numerics.hr_step68ad_b3c3b_cred_lie_identity
This reuses the byte-pinned b3c3a source-faithful Step45 transcription;
it does NOT rerun the original Step45/55/58 engines or certify Dirac boundaries.
"""
import hashlib
from pathlib import Path
import sympy as s
from . import hr_step68ad_b3c3a_diagonal_shift_covariance as a

PARENT_BLOB='e7f068a7c4063a27af2456515b58f8732b3b3343'

def check_parent():
    b=Path(a.__file__).read_bytes()
    got=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert got==PARENT_BLOB, (got,PARENT_BLOB)
    return got

q,qp=a.q,a.qp
qpp=s.symbols(' '.join(name+'rr' for name in a.Q))
zrr=s.Symbol('zrr')
vars=(*q,*qp,*qpp,a.z,a.zr,zrr)

def Dt(e):
    return (sum(s.diff(e,u)*v for u,v in zip(q,qp) if e.has(u))
            +sum(s.diff(e,u)*v for u,v in zip(qp,qpp) if e.has(u))
            +s.diff(e,a.z)*a.zr+s.diff(e,a.zr)*zrr)

def euler(A,B):
    return ([s.diff(A,u)-Dt(s.diff(A,v)) for u,v in zip(q,qp)],
            [s.diff(B,u)-s.diff(A,v)-Dt(s.diff(B,v)) for u,v in zip(q,qp)])

def bracket(g,f):
    return sum(g[k]*f[k+1]-g[k+1]*f[k] for k in range(0,12,2))

def vertical(e,order):
    w=a.weights
    if order==1:
        changes=(*[w[i]*q[i] for i in range(12)],
                 *[(w[i]+1)*qp[i] for i in range(12)],
                 *[(w[i]+2)*qpp[i] for i in range(12)],0,a.zr,2*zrr)
    elif order==2:
        changes=(*([0]*12),*[w[i]*q[i] for i in range(12)],
                 *[(2*w[i]+1)*qp[i] for i in range(12)],0,0,a.zr)
    elif order==3:
        changes=(*([0]*24),*[w[i]*q[i] for i in range(12)],0,0,0)
    else:raise ValueError(order)
    return sum(s.diff(e,u)*v for u,v in zip(vars,changes) if v!=0 and e.has(u))

def zero(e):
    return s.cancel(s.together(e))==0

def run():
    check_parent();passed=1
    for expr,weight in ((a.Ag,1),(a.Bg,0),(a.Am,1),(a.Bm,0)):
        a.verify(expr,weight);passed+=2
    eg=euler(a.Ag,a.Bg);ef=euler(a.Am,a.Bm)
    K00=bracket(eg[0],ef[0]);K01=bracket(eg[0],ef[1])
    C=K00-Dt(K01)
    for expr,weight in ((K00,1),(K01,0),(C,1)):
        for order in (1,2,3):
            residual=vertical(expr,order)-(weight*expr if order==1 else 0)
            assert zero(residual),(str(order),str(weight),str(residual)[:150]);passed+=1
    for x in qpp:
        assert zero(s.diff(C,x)),x;passed+=1
    assert zero(s.diff(C,a.zr)-a.Czr);passed+=1
    # The positive-K stationary relative shift is a scalar: Dg and K are
    # weight-two densities. Its true radial derivative is a weight-one density.
    d,k,dp,kp=s.symbols('d k dp kp',real=True)
    R=s.sqrt(d*d+k*k)
    Z=d/R
    Zp=s.diff(Z,d)*dp+s.diff(Z,k)*kp
    assert zero(2*d*s.diff(Z,d)+2*k*s.diff(Z,k));passed+=1
    assert zero(2*d*s.diff(Zp,dp)+2*k*s.diff(Zp,kp));passed+=1
    assert zero(2*d*s.diff(Zp,d)+2*k*s.diff(Zp,k)
                +3*dp*s.diff(Zp,dp)+3*kp*s.diff(Zp,kp)-Zp);passed+=1
    # Chain-rule composition: C has weight 1 with z scalar, zr weight 1;
    # Z(D,K) has weight 0, Dt Z weight 1. Therefore C_red has weight 1
    # for all smooth canonical jets on K>0, including nonzero second jets.
    return {'exact_assertions':passed,'K00_weight':1,'K01_weight':0,
            'C_weight':1,'C_red_weight':1,'positive_K_reduction':'chain_rule_exact',
            'source_transcription_git_blob':PARENT_BLOB,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'limits':'No original Step45/55/58 engine replay, boundary charge, lapse rank, or Dirac theorem'}

if __name__=='__main__':
    import json
    print(json.dumps(run(),indent=2,ensure_ascii=False))

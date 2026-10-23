"""Step58: six-pair local Dirac-time bracket as full lapse differential operator.

Derived via the adjoint of complete (q,q',z(q,q'),z'(q,q',q'')) variation.
This is a FORMAL local expression for {C_red,H_tot}, retaining ALL lapse
jets and all shift response. Actual lapse fixing/rank of the differential
operator on the exact Step55 background is not established here.

The q,q',q'',q''' and z,z',z'',z''' are independent jet symbols, but the
returned operator is meaningful ONLY on the stationary positive-K shift
jet shell (z=Z(D,K), z'=D(Z), ...), on which the Hamiltonian envelope holds.
"""
from __future__ import annotations
from functools import lru_cache
import sympy as sp
from .hr_step57_secondary_principal_symbol import authenticated_step45


def add(A,B):
    return {j:A.get(j,sp.S.Zero)+B.get(j,sp.S.Zero)
            for j in set(A)|set(B) if A.get(j,sp.S.Zero)+B.get(j,sp.S.Zero)!=0}


def mul(a,A):
    if a==0: return {}
    return {j:a*x for j,x in A.items() if x!=0}


def differentiate_lapse_operator(A,dt):
    """If f=Σ a_j L^(j), (d/dr)f=Σ [D a_j+a_(j-1)] L^(j)."""
    out={}
    for j,x in A.items():
        out[j]=out.get(j,sp.S.Zero)+dt(x)
        out[j+1]=out.get(j+1,sp.S.Zero)+x
    return {j:v for j,v in out.items() if v!=0}


@lru_cache(1)
def physical_operator():
    p=authenticated_step45()
    q=p['q']; qp=p['dq']; qpp=p['ddq']
    qppp=sp.symbols(' '.join(n+'rrr' for n in p['Q']))
    q4=sp.symbols(' '.join(n+'rrrr' for n in p['Q']))
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=p['parameters']
    zrrr=sp.Symbol('zrrr')
    fulljets=(*q,*qp,*qpp,*qppp, *q4,z,zr,zrr,zrrr)
    nextjets=(*qp,*qpp,*qppp,*q4, *([sp.S.Zero]*len(q4)),zr,zrr,zrrr,sp.S.Zero)
    assert len(fulljets)==len(nextjets)
    def Dt(expr):
        return sp.Add(*(sp.diff(expr,k)*v for k,v in zip(fulljets,nextjets) if expr.has(k) and v!=0))

    Q={key:val for key,val in zip(p['Q'],q)}
    Qp={key:val for key,val in zip(p['Q'],qp)}
    Lg,Lf,Sg,Sf=Q['Lg'],Q['Lf'],Q['Sg'],Q['Sf']
    D=Q['pSg']*Qp['Sg']-Lg*Qp['pLg']+Q['pg']*Qp['tg']
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    K=m2*mg*Lg*Lf*At
    root=sp.sqrt(1-z*z)
    Fz=D-K*z/root
    # Exactly on Fz=0 for K>0: Z_D=(1-z²)^(3/2)/K,
    # Z_K=-z*(1-z²)/K. Functions of q and z; Dt uses z'=zr.
    ZD=root**3/K
    ZK=-z*(1-z*z)/K
    C=p['C_exact']
    assert all(not C.has(v) for v in qpp)
    Cz=sp.diff(C,z);Czr=sp.diff(C,zr)
    Cq=[sp.diff(C,u) for u in q]
    Cqp=[sp.diff(C,u) for u in qp]
    Dq=[sp.diff(D,u) for u in q]
    Dqp=[sp.diff(D,u) for u in qp]
    Kq=[sp.diff(K,u) for u in q]

    lapse_out={}
    lapse_vectors={};shift_variations={};shift_D={};shift_K={};direct_parts={}
    for label,E in [('N',p['eg']),('M',p['ef'])]:
        # Hamiltonian vector field for all six FULL canonical pairs.
        # x_{q_i}=+E_{p_i} H; x_{p_i}=-E_{q_i} H.
        X=[]
        for i in range(12):
            row=i+1 if i%2==0 else i-1
            sign=1 if i%2==0 else -1
            X.append({j:sign*E[j][row] for j in range(3) if E[j][row]!=0})
        Xr=[differentiate_lapse_operator(v,Dt) for v in X]
        deltaD={};deltaK={};direct={}
        for i in range(12):
            deltaD=add(deltaD,add(mul(Dq[i],X[i]),mul(Dqp[i],Xr[i])))
            deltaK=add(deltaK,mul(Kq[i],X[i]))
            direct=add(direct,add(mul(Cq[i],X[i]),mul(Cqp[i],Xr[i])))
        deltaZ=add(mul(ZD,deltaD),mul(ZK,deltaK))
        lapse_vectors[label]=X
        shift_variations[label]=deltaZ
        shift_D[label]=deltaD
        shift_K[label]=deltaK
        direct_parts[label]=direct
        # COMPLETE true temporal bracket including shift and zprime response.
        out=add(add(direct,mul(Cz,deltaZ)),mul(Czr,differentiate_lapse_operator(deltaZ,Dt)))
        lapse_out[label]=out

    return {'operator':lapse_out,'vectors':lapse_vectors,'delta_shift':shift_variations,
            'delta_Dg':shift_D,'delta_K':shift_K,'direct_parts':direct_parts,'Dt':Dt,'C':C,'Dg':D,'K':K,'Fz':Fz,'q':q,'qp':qp,
            'qpp':qpp,'qppp':qppp,'q4':q4,'z':z,'zr':zr,'zrr':zrr,'zrrr':zrrr,
            'Cz':Cz,'Czr':Czr,'source':'byte-authentic Step45 original physical six-pair fixed-z first variation',
            'limits':'Operator is factorized, unexpanded and not evaluated on exact Step55 radial constrained profile; enforce Fz and its radial jet consequences before physical interpretation; boundary compact.'}



@lru_cache(1)
def highest_lapse_certificate():
    """EXACT cancellation of both highest lapse jets on physical primaries.

    First impose Fz=0 in the positive-K chart by solving for the genuine
    canonical first jet pLg_prime, without substituting any numerical profile.
    Then show the full temporal Cdot coefficient of M'' vanishes EXACTLY,
    and the coefficient of N'' equals (z²-1)*Hg/(Lg*Lf). So BOTH highest
    lapse jets vanish on the joint Fz=0,Hg=0 primary surface.

    This does NOT simplify N,N',M,M', determine lapse rank or prove that
    the temporal equation admits positive physically compatible lapses.
    """
    v=physical_operator();original=authenticated_step45()
    q=dict(zip(original['Q'],original['q']))
    qp=dict(zip(original['Q'],original['dq']))
    Lg,Lf=q['Lg'],q['Lf'];z=v['z']
    root=sp.sqrt(1-z*z)
    solved_pLgr=(q['pSg']*qp['Sg']+q['pg']*qp['tg']-v['K']*z/root)/Lg
    sub={qp['pLg']:solved_pLgr}
    M2=v['operator']['M'][2].subs(sub)
    N2=v['operator']['N'][2].subs(sub)
    Hg=original['Hg'].subs(sub)
    assert sp.factor(M2)==0, 'M second lapse derivative persists on Fz=0'
    ratio=sp.factor(sp.cancel(N2/Hg))
    expected=(z*z-1)/(Lg*Lf)
    assert sp.factor(ratio-expected)==0, 'N second lapse derivative not proportional to Hg'
    return {'shift_elimination_pLg_prime':solved_pLgr,
            'M2_on_Fz_shell':sp.S.Zero,
            'N2_on_Fz_shell':expected*Hg,
            'N2_to_Hg_factor':expected,
            'N2_and_M2_vanish_on_Fz_and_Hg':True,
            'remaining_lapse_operators':{label:{j:e for j,e in coeff.items() if j<=1}
                                         for label,coeff in v['operator'].items()},
            'qualifiers':'Exact equality on Fz=0, Hg=0, K>0 and regular metrics, before any check of Hf,C=0 or full Dirac rank.'}


def manifest():
    op=physical_operator()
    high=highest_lapse_certificate()
    return {'step':58,'source':'byte-original Step45 full six-pair Hamiltonian and C',
            'lapse_jet_orders':{k:sorted(v) for k,v in op['operator'].items()},
            'actual_coefficient_counts':{k:{str(j):sp.count_ops(c,visual=False) for j,c in v.items()}
                                         for k,v in op['operator'].items()},
            'assembly':'Complete directional derivative of true C(q,qprime,z,zprime) with canonical X_H and shift Z(Dg,K), retained as exact factored SymPy expression with up to 4 lapse derivatives',
            'highest_lapse_result':{'M_second':'EXACT_ZERO_ON_Fz', 'N_second':'(z²-1)*Hg/(Lg Lf) ON_Fz', 'both_zero_on_Fz_and_Hg':high['N2_and_M2_vanish_on_Fz_and_Hg']},
            'remaining_lapse_operator':'N,Nprime,M,Mprime EXACT FACTORED, NOT REDUCED ON FULL PRIMARY+SECONDARY SHELL',
            'rank_and_lapse_fixing':'NOT_DETERMINED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

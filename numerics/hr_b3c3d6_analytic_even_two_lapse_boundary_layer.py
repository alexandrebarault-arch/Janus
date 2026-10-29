"""Exact NONPHYSICAL two-lapse analytic boundary-layer counterexample.

This construction refutes any inference that analytic/even regularity of BOTH
lapses alone excludes small-B singular boundary layers. It is NOT Step58.
"""
import sympy as sp

r, eps = sp.symbols('r eps', real=True, positive=True)
R = sp.Rational(17, 20)
k = sp.Rational(10371, 20000)
a = k / (1-k)
b = 1 / (1-k)


def witness():
    N = sp.exp((R**2-r**2)/(2*eps*R**4))
    M = N * (k + (1-k)*(r/R)**4)
    AN, AM = a*r**2, -b*r**2
    BN, BM, EN, EM = -eps*r**5, sp.S.Zero, sp.S.Zero, sp.S.Zero
    operator = AN*N + AM*M + BN*sp.diff(N, r)
    return dict(r=r, eps=eps, R=R, k=k, a=a, b=b,
                N=N, M=M, AN=AN, AM=AM, BN=BN, BM=BM, EN=EN, EM=EM,
                operator=operator)


def certificate():
    w = witness()
    N, M = w['N'], w['M']
    return {
        'operator_exact_zero': sp.simplify(w['operator']),
        'N_outer': sp.simplify(N.subs(r,R)),
        'M_outer': sp.simplify(M.subs(r,R)),
        'center_ratio': sp.simplify((M/N).subs(r,0)),
        'N_prime_center': sp.simplify(sp.diff(N,r).subs(r,0)),
        'M_prime_center': sp.simplify(sp.diff(M,r).subs(r,0)),
        'endpoint_derivative': sp.simplify(sp.diff(N,r).subs(r,R)),
        'endpoint_BN_Nprime': sp.simplify((w['BN']*sp.diff(N,r)).subs(r,R)),
        'endpoint_A_sum': sp.simplify((w['AN']+w['AM']).subs(r,R)),
        'N_center': sp.simplify(N.subs(r,0)),
        'algebraic_limit_ratio': sp.simplify(-w['AN']/w['AM']),
    }

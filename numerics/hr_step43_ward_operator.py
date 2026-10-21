"""Step43 exact smearing-adjoint/Ward decomposition for mixed ADM Poisson jets.

Given the full six-pair mixed Hamiltonian bracket in 3+3 smearing jets,
B[N,M] = integral sum_{i,j=0..2} N^(i) K_ij(r) M^(j) dr,
construct its exact formal adjoint and identify the CONDITIONAL reduction
B = integral N*C*M.  This is symbolic operator algebra, not verification
that any Hassan--Rosen solution satisfies the required Ward identities.

Why needed: the Step37/39 residual C=K00-(K01)' is a complete physical
secondary coefficient only if the actual full Poisson kernel passes the
other exact jet Ward and high-derivative cancellation gates.
"""
from __future__ import annotations
from math import comb
import sympy as sp

r = sp.Symbol('r', real=True)
ZERO = sp.Integer(0)


def adjoint_coefficients(K):
    """Return A_p so B=integral N sum_p A_p M^(p), modulo boundary.

    A_p = sum_{i,j; j<=p<=i+j} (-1)^i binomial(i,p-j)
            (d/dr)^(i+j-p) K_ij.
    Require compact test functions or vanishing boundary traces N,N' at
    integration endpoints.  No truncation of p>2 is permitted.
    """
    if not isinstance(K,dict) or any(not(isinstance(t,tuple) and len(t)==2
            and all(isinstance(v,int) and 0<=v<=2 for v in t)) for t in K):
        raise ValueError('coefficients must have (i,j) in 0..2')
    A={p:ZERO for p in range(5)}
    for (i,j),coefficient in K.items():
        k=sp.sympify(coefficient)
        for p in range(j,j+i+1):
            A[p]+=(-1)**i*comb(i,p-j)*sp.diff(k,r,i+j-p)
    return {p:sp.factor(a) for p,a in A.items()}


def restricted_local_gates(K):
    """Exact C,W,D and excluded high smearing coefficients.

    When only K00,K01,K10,K11,K20 may be nonzero:
       B = integral N [ C*M + (W*M)' + (D*M')' ],
       C=K00-K01',  W=K01-K10+K20',  D=K20-K11.

    Therefore C=0 does NOT suffice without independent W=D=0 and
    excluded coefficients K02=K12=K21=K22=0 (or equivalent full-operator
    cancellations). The latter particular vanishing is sufficient, not a
    universally necessary condition for every imaginable kernel.
    """
    if not isinstance(K,dict):raise ValueError('kernel must be a dict')
    x=lambda i,j:sp.sympify(K.get((i,j),ZERO))
    return {'C':sp.factor(x(0,0)-sp.diff(x(0,1),r)),
            'W':sp.factor(x(0,1)-x(1,0)+sp.diff(x(2,0),r)),
            'D':sp.factor(x(2,0)-x(1,1)),
            'excluded':{(i,j):x(i,j) for i,j in ((0,2),(1,2),(2,1),(2,2))}}


def exact_reduction_gate(K):
    """Check FULL operator equals multiplication by C exactly.

    For nontrivial K02/etc we insist on actual adjoint coefficient
    cancellation rather than merely imposing five-jet sparsity.
    This is a check on symbolic K(r) supplied to the routine, *not* a
    proof that real HR numerical K(r) satisfies it.
    """
    adj=adjoint_coefficients(K)
    gates=restricted_local_gates(K)
    return {'C':gates['C'],
            'operator_residuals':{p:sp.factor(adj[p]-(gates['C'] if p==0 else 0)) for p in range(5)},
            'C_only_valid':all(sp.simplify(adj[p]-(gates['C'] if p==0 else 0))==0 for p in range(5)),
            'jet_W':gates['W'], 'jet_D':gates['D'],
            'high_jets':gates['excluded']}


def polynomial_integral(expr, a=sp.Rational(1,5), b=sp.Rational(7,10)):
    """Exact rational definite integral for polynomial test coefficients."""
    a,b=sp.Rational(a),sp.Rational(b)
    if a>=b:raise ValueError('nonempty integration interval required')
    p=sp.Poly(sp.expand(expr),r,domain='QQ')
    primitive=p.integrate()
    return sp.factor(primitive.eval(b)-primitive.eval(a))


def compact_smears(a=sp.Rational(1,5),b=sp.Rational(7,10),variant=1):
    """Compact polynomial patch; N and M vanish with first 3 derivatives."""
    a,b=sp.Rational(a),sp.Rational(b)
    if a>=b:raise ValueError('nonempty integration interval required')
    N=(r-a)**4*(b-r)**4
    M=N*(1+sp.Rational(variant,7)*(r-a)/(b-a))
    return sp.expand(N),sp.expand(M)


def bracket_as_polynomial(K,N,M):
    return sp.expand(sum(sp.diff(N,r,i)*sp.sympify(k)*sp.diff(M,r,j)
                       for (i,j),k in K.items()))


def adjoint_as_polynomial(K,N,M):
    a=adjoint_coefficients(K)
    return sp.expand(N*sum(a[p]*sp.diff(M,r,p) for p in range(5)))


def local_as_polynomial(K,N,M):
    return sp.expand(N*restricted_local_gates(K)['C']*M)


def exact_compact_integral_controls(K,variant=1):
    """Return exact rational integrals of original, adjoint and C-only.

    The equality original=adjoint holds for ANY polynomial K with the
    test lapse boundary conditions. Equality with C-only is a
    SEPARATE Ward/jet property, and is not silently assumed.
    """
    N,M=compact_smears(variant=variant)
    return {'original':polynomial_integral(bracket_as_polynomial(K,N,M)),
            'adjoint':polynomial_integral(adjoint_as_polynomial(K,N,M)),
            'C_only':polynomial_integral(local_as_polynomial(K,N,M))}


def ward_example(C=r**2*(r-sp.Rational(2,5))):
    """Manufactured exactly closed Ward kernel with nontrivial K11,K20."""
    k01=2*r**2+3*r
    k20=1+r**3
    return {(0,0):sp.expand(C+sp.diff(k01,r)),
            (0,1):k01, (1,0):k01+sp.diff(k20,r),
            (1,1):k20,(2,0):k20}


if __name__=='__main__':
    import json
    good=ward_example()
    check=exact_reduction_gate(good)
    sums=exact_compact_integral_controls(good)
    print(json.dumps({'step':43,'formal_adjoint_gate_pass':check['C_only_valid'],
       'exact_example_original_integral':str(sums['original']),
       'exact_example_C_integral':str(sums['C_only']),
       'physics':'No actual HR Ward/full-Dirac proof in this module',
       'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'},indent=2))

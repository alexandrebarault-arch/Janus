"""Exact regular-chart shift-elimination/boundary chain rule; NOT full Dirac."""
import sympy as sp

D,K,Lg,Lf,N,M,P=sp.symbols('D K Lg Lf N M P', real=True)
Z=sp.symbols('Z', real=True)
Q=N+M*Lg/Lf
Z_POS=D/sp.sqrt(K*K+D*D)  # explicitly K>0
B_SHIFT=-Q*P*Z_POS
F=D-K*Z/sp.sqrt(1-Z*Z)


def exact_checks():
    den=(K*K+D*D)**sp.Rational(3,2)
    identities={
        'z_D_positive_K':sp.diff(Z_POS,D)-K*K/den,
        'z_K_positive_K':sp.diff(Z_POS,K)+D*K/den,
        'F_z':sp.diff(F,Z)+K/(1-Z*Z)**sp.Rational(3,2),
        'boundary_pLg_prime':-Lg*sp.diff(B_SHIFT,D)-Q*P*Lg*K*K/den,
    }
    return {key:sp.simplify(value) for key,value in identities.items()}


def rational_witness():
    values={D:4,K:3,Lg:2,Lf:3,N:1,M:1,P:7}
    return {
        'K_positive':sp.Integer(3),
        'D':sp.Integer(4),
        'z_star':sp.simplify(Z_POS.subs(values)),
        'F_positive':sp.simplify(F.subs({D:4,K:3,Z:sp.Rational(4,5)})),
        'dz_dpLg_prime':sp.simplify((-Lg*sp.diff(Z_POS,D)).subs(values)),
        'dB_dpLg_prime':sp.simplify((-Lg*sp.diff(B_SHIFT,D)).subs(values)),
        'F_negative_K_correct':sp.simplify(F.subs({D:4,K:-3,Z:-sp.Rational(4,5)})),
        'F_negative_K_wrong':sp.simplify(F.subs({D:4,K:-3,Z:sp.Rational(4,5)})),
        'F_K_zero_D_nonzero':sp.simplify(F.subs({D:4,K:0,Z:sp.Rational(1,2)})),
        'F_K_zero_D_zero':sp.simplify(F.subs({D:0,K:0,Z:sp.Rational(1,2)})),
    }


if __name__=='__main__':
    assert all(v==0 for v in exact_checks().values())
    print({k:str(v) for k,v in rational_witness().items()})

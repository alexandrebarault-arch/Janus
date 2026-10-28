"""b3c3d: exact rank criterion for the Step45 reduced z'-boundary sector.

The sector alpha=P dZ is not the full original non-IBP boundary one-form.
No physical boundary condition, Dirac tangency, or charge is certified.
Source: Step45 Git blob 66aa43841dccfe4a5d586a49be9c10af3a67a10e.
Run: python -m numerics.hr_step68ad_b3c3d_boundary_sector_rank
"""
import json
import sympy as s

Lg,Lf,N,M,K=s.symbols('Lg Lf N M K', positive=True)
p,pr,ps,Sr,pg,tr=s.symbols('p pr ps Sr pg tr', real=True)
c0,c1,c2=s.symbols('c0 c1 c2', real=True)
u,v=s.symbols('u v', real=True)
A=N+M*Lg/Lf
P=p*A
D=ps*Sr-Lg*pr+pg*tr
Z=D/s.sqrt(D**2+K**2)
F=c0+c1*P+c2*P**2
B=s.expand(c1*P**2/s.Integer(2)+2*c2*P**3/s.Integer(3))
curvature=s.factor(s.diff(P,p)*s.diff(Z,pr)-s.diff(P,pr)*s.diff(Z,p))
expected=-Lg*A*K**2/(D**2+K**2)**s.Rational(3,2)

def run():
    checks={
        'Step45_shift_derivative_coefficient':s.simplify(P-p*(N+M*Lg/Lf)),
        'Z_D_derivative':s.simplify(s.diff(Z,pr)+Lg*K**2/(D**2+K**2)**s.Rational(3,2)),
        'restricted_two_form':s.simplify(curvature-expected),
        'P_independent_of_pprime':s.diff(P,pr),
        'P_derivative_p':s.simplify(s.diff(P,p)-A),
        'Z_independent_of_p':s.diff(Z,p),
        'integrable_graph_primitive':s.simplify(s.diff(B,p)-P*s.diff(F,p)),
        'constant_shift_graph':s.simplify(s.diff(B,c0)),
        'fixed_P_primitive':s.diff(P*s.Symbol('w'),s.Symbol('w'))-P,
        'monotone_D':s.simplify(s.diff(Z,pr)/(-Lg)-K**2/(D**2+K**2)**s.Rational(3,2)),
        'graph_rank_zero':s.det(s.Matrix([[s.diff(P,p),s.diff(P,pr)],
                          [s.diff(F,p),s.diff(F,pr)]])),
        'free_rank_nonzero_witness':s.simplify(expected.subs({Lg:s.Rational(2,5),Lf:s.Rational(3,5),N:1,M:1,K:4,D:3})+s.Rational(32,375)),
        'realizable_graph_squared':s.factor((1-F**2)*(K*F/s.sqrt(1-F**2))**2-K**2*F**2),
    }
    for key,expr in checks.items():
        assert expr==0,(key,expr)
    assert len(checks)==13
    assert s.simplify(s.diff(Z,pr)).is_negative is True
    assert s.simplify(s.diff(P,p)).is_positive is True
    # Direct exact positive-K rational realization: Z=1/3 when D=K/(2 sqrt(2)).
    assert s.simplify((D/s.sqrt(D**2+K**2)).subs(D,K/(2*s.sqrt(2)))-s.Rational(1,3))==0
    return {'exact_sympy_assertions':len(checks)+3,
            'sector':'alpha=P dZ, P=pLg*(N+M*Lg/Lf), Z=D/sqrt(D**2+K**2)',
            'closed_on_submanifold_iff':'pullback(dP wedge dZ)=0; rank(P,Z)<=1',
            'graph_example':'Z=c0+c1*P+c2*P**2; primitive B=c1*P**2/2+2*c2*P**3/3',
            'free_slice_curvature_witness_non_step55':'-32/375',
            'scope':'exact Step45 shift-derivative boundary sector only, K>0; NOT full boundary one-form',
            'original_step45_55_58_import_replay':False,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(run(),indent=2))

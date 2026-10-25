"""Step68ab: exact insufficiency of 68u/v/y/z bands for third derivative.

Construct analytic OTHER ODEs obeying every stated aggregate signed band,
with the SAME admissible U3 and G_U=-1, but unbounded U_sss at a fixed
positive radius. This is a logical insufficiency certificate, NOT a
counterexample to the fixed physical Step55 G and NOT a temporal sign proof.
Also derive the correct nonresonant U4 recurrence with unfrozen G_U.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp
from .hr_step68z_invariant_center_cone import original_reports, tightened_bounds
from .hr_step68aa_canonical_center_radial_jets import authenticated_inputs

EPS=F(1,10**11)
S_MAX=F(1,1024)
G_SLOPE=F(-1)


def certified_underdetermination(folder: str | Path):
    """Check bounds for ALL frequencies n>=1, using only |sin|,|cos|<=1."""
    authenticated_inputs(folder)
    bands=tightened_bounds(original_reports(folder))
    c=sum(bands['u3'],F(0))/2
    if not bands['g'][0] < G_SLOPE < bands['g'][1]:
        raise ArithmeticError('Constructed G_U is not in original chart')
    # h=c+(eps/n)*sin(n*s), n>=1. f=9*h+2s*h_s,
    # ds=3*h+s*h_s; G(U)-Vstar=s^3*(8*h+2s*h_s).
    # G(U)-G(Ustar)=s^3*(-h). No differentiation of enclosures.
    centers={'h':c,'f':9*c,'ds':3*c,'v':8*c,'aux':-c}
    widths={'h':EPS,'f':(9+2*S_MAX)*EPS,
            'ds':(3+S_MAX)*EPS,'v':(8+2*S_MAX)*EPS,'aux':EPS}
    strict={}
    for key in ('h','f','ds','v','aux'):
        lo,hi=bands[key]; mid=centers[key]; width=widths[key]
        if not lo < mid-width <= mid+width < hi:
            raise ArithmeticError('Source band cannot contain family: '+key)
        strict[key]={'whole_family_enclosure':[str(mid-width),str(mid+width)],
                     'original_band':[str(lo),str(hi)],
                     'strictly_interior':True}
    # U3=c at s=0; high-frequency ripple has order s4 there.
    if not bands['u3'][0]<c<bands['u3'][1]:
        raise ArithmeticError('center U3 excluded')
    return {'step':'68ab','domain_s':['0','1/1024'],
            'verified_original_step68aa_and_68z':True,
            'analytic_family':'h_n(s)=c+epsilon*sin(n*s)/n; U_n=Ustar+s^3*h_n',
            'analytic_family_G':'G_n(s,u)=2*(U_n+s*U_n_prime)-(u-U_n), with G_n_U=-1',
            'c_center_U3':str(c),'epsilon':str(EPS),'G_U':str(G_SLOPE),
            'valid_for_all_real_frequencies_n_at_least_1':True,
            'bands':strict,
            'unbounded_third_derivative_formula_at_smax':
                'U_n_sss(smax)-6*c = epsilon*smax*(18-4*pi*pi*k*k) for n=2*pi*k/smax, k>=1',
            'third_derivative_supremum':'UNBOUNDED_BELOW_OVER_ADMISSIBLE_OTHER_G',
            'IMPORTANT':'The actual original Step55 G is fixed and could constrain higher jets; this only disproves inferring higher jets from published interval bands alone.',
            'physical_Step55_G_higher_partials':'NOT_YET_INTERVAL_CERTIFIED',
            'temporal_Step58_AN_AM':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def symbolic_oracle():
    s,u0,c,e,n=sp.symbols('s U0 c eps n',real=True)
    U1,U2=sp.symbols('U1 U2',real=True)
    us=u0+U1*s+U2*s**2
    h=c+e*sp.sin(n*s)/n
    actual=us+s**3*h
    u=sp.symbols('u')
    G=2*(actual+s*sp.diff(actual,s))-(u-actual)
    check_ode=sp.simplify((G.subs(u,actual)-2*actual-2*s*sp.diff(actual,s)))
    f=sp.simplify((G.subs(u,us)-2*(us+s*sp.diff(us,s)))/s**3)
    expected_f=9*h+2*s*sp.diff(h,s)
    if check_ode!=0 or sp.simplify(f-expected_f)!=0 or sp.diff(G,u)!=-1:
        raise ArithmeticError('Analytic family does not solve a regular ODE')
    k=sp.symbols('k',positive=True,integer=True)
    s0=sp.Rational(1,1024)
    expression=sp.diff(actual,s,3)-6*c
    at=sp.simplify(expression.subs({s:s0,n:2*sp.pi*k/s0}))
    target=e*s0*(18-4*sp.pi**2*k**2)
    if sp.simplify(at-target)!=0:
        raise ArithmeticError('Counterexample does not grow quadratically')
    if sp.simplify(sp.limit((actual-us)/s**3,s,0)-c)!=0:
        raise ArithmeticError('Counterexample changes original U3')
    return {'ode_identity':'EXACT_ZERO','slope_G_U':'-1',
            'F0_over_s3':'9*h+2*s*h_prime',
            'U_sss_minus_6c_at_special_frequencies':str(target)}


def original_G_center_U4_recurrence():
    """Actual G must be inserted later; its higher partials are NOT known here."""
    s,y=sp.symbols('s y')
    u0,u1,u2,u3,u4=sp.symbols('U0 U1 U2 U3 U4')
    # c_ij=[s^i*(u-U0)^j]G; j=1,i=0 means G_U(0,U0).
    c={(i,j):sp.symbols(f'g{i}{j}') for i in range(5) for j in range(5-i)}
    gy=sum(coeff*s**i*y**j for (i,j),coeff in c.items())
    lower=u1*s+u2*s*s+u3*s**3
    rhs=sp.expand(gy.subs(y,lower)).coeff(s,4)
    formula=sp.factor(rhs/(10-c[0,1]))
    exact_u4=sp.expand(gy.subs(y,lower+u4*s**4)).coeff(s,4)
    if sp.simplify(exact_u4-rhs-c[0,1]*u4)!=0:
        raise ArithmeticError('G_U U4 dependence omitted')
    if sp.simplify(((10-c[0,1])*u4-rhs).subs(u4,formula))!=0:
        raise ArithmeticError('Wrong U4 recursion')
    if u4 in rhs.free_symbols:
        raise ArithmeticError('U4 must not enter numerator')
    return {'numerator':str(sp.factor(rhs)), 'denominator':'10-g01',
            'coefficients':'gij=[s^i*(u-U0)^j] G_original(s,u) at center',
            'G_U_negative_implies_positive_denominator':True,
            'actual_G_original_coefficients':'NOT_EVALUATED',
            'actual_U4_interval':'NOT_CERTIFIED'}


def report(folder):
    out=certified_underdetermination(folder)
    out['independent_sympy_oracle']=symbolic_oracle()
    out['formal_original_U4_recurrence']=original_G_center_U4_recurrence()
    return out


def three_curve_barrier_oracle(folder):
    """Stronger countermodel: preserve EXACT F0,Fplus,Fminus third derivatives.

    The *different* analytic G_n is a cubic polynomial in u at each s.
    Oscillatory correction vanishes identically on Ustar and Ustar+-kappa*s^3.
    Its s-derivatives may be arbitrarily large while G_U remains bounded.
    """
    authenticated_inputs(folder)
    reports=original_reports(folder)
    bands=tightened_bounds(reports)
    c=sum(bands['u3'],F(0))/2
    kappa=F(reports['68y']['kappa'])
    f0=9*c
    fp=f0-9*kappa
    fm=f0+9*kappa
    ulo,uhi=map(F,reports['68u']['upper_F_third_over_6_interval'])
    dlo,dhi=map(F,reports['68u']['lower_F_third_over_6_interval'])
    fzero_lo,fzero_hi=map(F,reports['68v']['F0_third_over6'])
    if not (ulo<fp<uhi<0<dlo<fm<dhi and fzero_lo<f0<fzero_hi):
        raise ArithmeticError('Three authentic ORIGINAL derivative certificates not covered')
    dh=EPS*S_MAX  # |h-c| <= EPS*s*(s/Smax)^6, for all frequencies n>=1
    cmin=abs(c)-dh
    cmax=abs(c)+dh
    if not 0<cmin<=cmax<kappa:
        raise ArithmeticError('Analytic interpolation denominator near zero')
    alpha_max=23*EPS*S_MAX
    max_gu_correction=alpha_max*2*kappa*kappa/(cmin*(kappa*kappa-cmax*cmax))
    if not bands['g'][0] < -1-max_gu_correction < -1+max_gu_correction < bands['g'][1]:
        raise ArithmeticError('Analytic G_U family not certified on entire tube')
    centers={'h':c,'f':f0,'ds':3*c,'v':8*c,'aux':-c}
    widths={'h':dh,'f':F(0),'ds':10*dh,'v':22*dh,'aux':22*dh}
    for name in centers:
        lo,hi=bands[name]
        if not lo<=centers[name]-widths[name]<=centers[name]+widths[name]<=hi:
            raise ArithmeticError('Refined full-family interval missing: '+name)
    return {'analytic_other_G_and_branch':'U_n=Ustar+s^3*h_n, h_n=c+epsilon*(s/Smax)^6*sin(n*s)/n; G_n=Vstar+9*c*s^3-(u-Ustar)+A_n(s)*(u-Ustar)*((u-Ustar)^2-kappa^2*s^6)',
            'A_n(s)':'epsilon*(21*sin(n*s)/n+2*s*cos(n*s))/(Smax^6*h_n*(h_n^2-kappa^2))',
            'all_frequencies_n_greater_equal_1':True,
            'Fzero_third_over_6':str(f0),
            'Fplus_third_over_6':str(fp),
            'Fminus_third_over_6':str(fm),
            'original_step68u_upper':[str(ulo),str(uhi)],
            'original_step68u_lower':[str(dlo),str(dhi)],
            'original_step68v_Fzero':[str(fzero_lo),str(fzero_hi)],
            'G_U_correction_max':[str(-max_gu_correction),str(max_gu_correction)],
            'bounded_h_deltas':{name:str(width) for name,width in widths.items()},
            'third_derivative_at_smax_for_n_2pi_k_over_smax':
                'U_n_sss(smax)-6*c = epsilon*smax*(216-4*pi*pi*k*k)',
            'interpretation':'Even all published F0/Fplus/Fminus THIRD derivative certificates and G_U band do not bound the true solution U_sss without fixed-G derivative controls. These G_n are NOT original physical Step55 G.'}


def symbolic_three_curve_oracle():
    s,u,n=sp.symbols('s u n', positive=True)
    k=sp.symbols('k', positive=True, integer=True)
    c,eps,kappa,U0,U1,U2=sp.symbols('c eps kappa U0 U1 U2',real=True)
    smax=sp.Rational(1,1024)
    star=U0+U1*s+U2*s*s
    h=c+eps*s**6*sp.sin(n*s)/(n*smax**6)
    un=star+s**3*h
    d=u-star
    A=eps*(21*sp.sin(n*s)/n+2*s*sp.cos(n*s))/(smax**6*h*(h*h-kappa*kappa))
    vstar=2*(star+s*sp.diff(star,s))
    G=vstar+9*c*s**3-d+A*d*(d*d-kappa*kappa*s**6)
    F0=sp.simplify((G.subs(u,star)-vstar)/s**3)
    if F0 !=9*c:
        raise ArithmeticError('Fzero cubic mismatch')
    for sign in (-1,1):
        barrier=star+sign*kappa*s**3
        F=sp.cancel((G.subs(u,barrier)-2*(barrier+s*sp.diff(barrier,s)))/s**3)
        if sp.simplify(F-(9*c-sign*9*kappa))!=0:
            raise ArithmeticError('One of exact barrier third derivatives drifted')
    on_shell=sp.cancel((G.subs(u,un)-2*(un+s*sp.diff(un,s)))/s**3)
    if sp.simplify(on_shell)!=0:
        raise ArithmeticError('Prescribed analytic U_n is not true solution')
    # Evaluating at sine zeros prevents uncontrolled floating-point signs.
    der=sp.diff(un,s,3)-6*c
    special=sp.simplify(der.subs({s:smax,n:2*sp.pi*k/smax}))
    expected=eps*smax*(216-4*sp.pi**2*k*k)
    if sp.simplify(special-expected)!=0:
        raise ArithmeticError('Unbounded derivative coefficient wrong')
    return {'Fzero':'9*c','Fplus':'9*c-9*kappa','Fminus':'9*c+9*kappa',
            'on_shell_residual':'EXACT_ZERO',
            'Usss_special':str(expected),
            'analytic_GU_at_Ustar':str(sp.simplify(sp.diff(G,u).subs(u,star)))}


def enhanced_report(folder):
    out=report(folder)
    out['all_original_third_derivative_boundary_certificate_countermodel']=three_curve_barrier_oracle(folder)
    out['stronger_independent_symbolic_oracle']=symbolic_three_curve_oracle()
    out['scope_clarification']='Countermodels G_n vary with n; original Step55 G does not. Uniform original temporal bounds need additional actual-G derivative computations.'
    return out

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:
        raise SystemExit('usage: python -m numerics.hr_step68ab_derivative_data_obstruction research/reports')
    print(json.dumps(enhanced_report(sys.argv[1]),indent=2,ensure_ascii=False))

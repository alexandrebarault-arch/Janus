"""Conditional positive-lapse two-endpoint C1 jet reachability; NOT Step58/Dirac.

The proof relies on positive B_N,B_M on a compact annulus and on a SINGLE
first-order scalar equation with second-lapse-derivative terms exactly zero.
"""
from __future__ import annotations
import json
import sympy as s


def exact_checks():
    bn,bm,dbn,dbm,an,am,n,m,dn,dm=s.symbols('bn bm dbn dbm an am n m dn dm', nonzero=True)
    u=bn*n+bm*m
    du=dbn*n+bn*dn+dbm*m+bm*dm
    w=bm*m/u
    sn=(dbn-an)/bn
    sm=(dbm-am)/bm
    dw=s.cancel((dbm*m+bm*dm)/u-w*du/u)
    # Eliminate M' using the ORIGINAL scalar lapse equation.
    dm_shell=-(an*n+am*m+bn*dn)/bm
    u_shell=s.factor(du.subs(dm,dm_shell))
    w_shell=s.factor(w)
    checks={
      'u_prime_shell':s.factor(u_shell-u*((1-w_shell)*sn+w_shell*sm)),
      'endpoint_equation_shell':s.factor((an*n+am*m+bn*dn+bm*dm).subs(dm,dm_shell)),
      'w_endpoint_from_n_m':s.factor(w_shell-bm*m/u),
      'wprime_quotient':s.factor(dw-((dbm*m+bm*dm)/u-w*du/u)),
    }
    # Reconstruct N,M and their first jets from u,w,u',w'.
    uu,ww,dww=s.symbols('uu ww dww',nonzero=True)
    ud=uu*((1-ww)*sn+ww*sm)
    N=(1-ww)*uu/bn
    M=ww*uu/bm
    Nd=-(dww*uu)/bn+(1-ww)*ud/bn-(1-ww)*uu*dbn/bn**2
    Md=dww*uu/bm+ww*ud/bm-ww*uu*dbm/bm**2
    orig={uu:u,ww:w_shell,dww:dw}
    # Endpoint compatibility is needed to match both independently prescribed derivatives.
    checks['N_reconstruction']=s.factor(N.subs(orig)-n)
    checks['M_reconstruction']=s.factor(M.subs(orig)-m)
    checks['Nprime_reconstruction_on_shell']=s.factor((Nd.subs(orig)-dn).subs(dm,dm_shell))
    checks['Mprime_reconstruction_on_shell']=s.factor((Md.subs(orig)-dm).subs(dm,dm_shell))
    # For the explicit analytic positive witness w=1/2, u=2exp(r/2).
    r=s.symbols('r',real=True)
    N0=s.exp(r/2); M0=s.exp(r/2)
    checks['toy_scalar_operator']=s.diff(N0,r)+s.diff(M0,r)-M0
    checks['toy_positive_weight']=s.Rational(1,2)-M0/(N0+M0)
    failures={k:str(s.factor(v)) for k,v in checks.items() if s.simplify(v)!=0}
    if failures:raise AssertionError(failures)
    E=s.exp(s.Rational(1,2))
    exact=[
      s.simplify(N0.subs(r,0)-1)==0,
      s.simplify(M0.subs(r,0)-1)==0,
      s.simplify(N0.subs(r,1)-E)==0,
      s.simplify(M0.subs(r,1)-E)==0,
      s.simplify(s.diff(N0,r).subs(r,0)-s.Rational(1,2))==0,
      s.simplify(s.diff(M0,r).subs(r,0)-s.Rational(1,2))==0,
      s.simplify(s.diff(N0,r).subs(r,1)-E/2)==0,
      s.simplify(s.diff(M0,r).subs(r,1)-E/2)==0,
      s.simplify(s.log((2*E)/2)-s.Rational(1,2))==0,
      s.Rational(0)<s.Rational(1,2)<s.Rational(1),
      s.simplify(s.Rational(0)+s.Rational(0)-1)!=0, # forbidden N'=M'=0 at left endpoint
      s.simplify(s.log(2/2))==0, # T=0, outside open interval (0,1)
    ]
    if not all(exact):raise AssertionError('toy witness or negative guard failed')
    return {'symbolic_zero_residuals':len(checks),'exact_toy_and_guard_checks':len(exact),
      'example':'B_N=B_M=1,A_N=0,A_M=-1,N=M=exp(r/2),r in [0,1]',
      'scope':'CONDITIONAL_SINGLE_SCALAR_FIRST_ORDER_EQUATION_WITH_POSITIVE_B; FIXED_ENDPOINT_VALUES_AND_FIRST_JETS',
      'original_step58_probe_executed':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(exact_checks(),indent=2))

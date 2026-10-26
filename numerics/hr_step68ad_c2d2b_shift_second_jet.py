"""Conditional exact regularization of the ORIGINAL Step58/60 shift jets.

No original Step58 seven-cell or Step60 quotient is executed here.
On Fz=0, K>0, assume D=r**3*d(s), K=r**2*k(s), s=r**2,
with k>0 and d,k C^3. Then z=r*A(s) is regular at r=0.
"""
from __future__ import annotations
import sympy as sp


def certify():
    D,D1,K1,D2,K2=sp.symbols('D D1 K1 D2 K2',real=True)
    K=sp.symbols('K',positive=True)
    z,zr=sp.symbols('z zr',real=True)
    R=sp.sqrt(D**2+K**2)
    Z=D/R                       # Positive-K stationary shift chart
    Dt=lambda f:sp.diff(f,D)*D1+sp.diff(f,K)*K1
    Z1=Dt(Z)
    Z2=Dt(Z1)+sp.diff(Z1,D1)*D2+sp.diff(Z1,K1)*K2
    W=K*D1-D*K1
    Z1_closed=K*W/R**3
    Z2_closed=(K1*W+K*(K*D2-D*K2))/R**3-3*K*W*(D*D1+K*K1)/R**5
    ZD=(1-z*z)**sp.Rational(3,2)/K
    ZK=-z*(1-z*z)/K
    shift_dt=lambda f:sp.diff(f,K)*K1+sp.diff(f,z)*zr
    step60_z2=ZD*D2+ZK*K2+shift_dt(ZD)*D1+shift_dt(ZK)*K1
    on_shell={z:Z,zr:Z1}
    r,s=sp.symbols('r s',positive=True)
    A=sp.Function('A')(s)
    radial=lambda f:sp.diff(f,r)+2*r*sp.diff(f,s)
    zp=radial(r*A)
    zpp=radial(zp)
    zppp=radial(zpp)
    d0,d1,k0,k1=sp.symbols('d0 d1 k0 k1',real=True)
    k0pos=sp.symbols('k0pos',positive=True)
    center_A=(d0+d1*s)/sp.sqrt((k0+k1*s)**2+s*(d0+d1*s)**2)
    checks={
      'positive_K_ZD':sp.simplify(ZD.subs(z,Z)-sp.diff(Z,D)),
      'positive_K_ZK':sp.simplify(ZK.subs(z,Z)-sp.diff(Z,K)),
      'Zprime_closed':sp.simplify(Z1-Z1_closed),
      'Zdoubleprime_closed':sp.simplify(Z2-Z2_closed),
      'Step60_Zdoubleprime_on_shell':sp.simplify(step60_z2.subs(on_shell,simultaneous=True)-Z2),
      'scaled_Zprime':sp.simplify(sp.factor(zp-(A+2*s*sp.diff(A,s))).subs(r**2,s)),
      'scaled_Zdoubleprime':sp.simplify(sp.factor(zpp-r*(6*sp.diff(A,s)+4*s*sp.diff(A,s,2))).subs(r**2,s)),
      'scaled_Ztripleprime':sp.simplify(sp.factor(zppp-(6*sp.diff(A,s)+24*s*sp.diff(A,s,2)+8*s*s*sp.diff(A,s,3))).subs(r**2,s)),
      'center_A':sp.simplify(center_A.subs(s,0).subs(k0,k0pos)-d0/k0pos),
      'center_Aprime':sp.simplify(sp.diff(center_A,s).subs(s,0).subs(k0,k0pos)-(d1/k0pos-d0*k1/k0pos**2-d0**3/(2*k0pos**3))),
    }
    bad={key:str(v) for key,v in checks.items() if v!=0}
    if bad:raise AssertionError(bad)
    return {'symbolic_identities':len(checks),'all_exact':True,
            'center_zprime':'d0/k0', 'center_zdoubleprime':'0',
            'center_ztripleprime':'6*(d1/k0-d0*k1/k0**2-d0**3/(2*k0**3))',
            'assumptions':'Fz=0, K>0, D=r^3*d(r^2), K=r^2*k(r^2), k(0)>0, d,k C^3',
            'original_step58_seven_cells':'NOT_EXECUTED',
            'original_step60_quotient':'NOT_EXECUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(certify(),indent=2))

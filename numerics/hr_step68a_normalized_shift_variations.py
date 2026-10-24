"""Step68a: center-regular Hamiltonian shift-response JETS, Step55 chart only.

Algebraic pullback of the authentic Step58 equation delta z = Z_D delta Dg
+ Z_K delta K, using Step55 radial parity. Historical HR providers are NOT
imported or executed here. This is not a temporal constraint-rank proof.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import sympy as sp

RMAX = F(17, 20)
KMIN = F(229, 1000)
W0 = F(1, 250)


def exact_variation_jets():
    s, w = sp.symbols('s w', nonnegative=True)
    k, k1, k2 = sp.symbols('k k1 k2', positive=True)
    ed, ek, ed1, ek1, ed2, ek2 = sp.symbols('ed ek ed1 ek1 ed2 ek2', real=True)
    t = 1-s*w*w
    A = t**sp.Rational(3,2)/k
    B = -w*t/k
    # Total s derivative on the prescribed w(s)=constant background.
    def ds(e):
        return sp.diff(e,s)+sp.diff(e,k)*k1+sp.diff(e,k1)*k2
    A1=sp.simplify(ds(A)); B1=sp.simplify(ds(B))
    A2=sp.simplify(ds(A1)); B2=sp.simplify(ds(B1))
    delta_w = A*ed+B*ek
    delta_w_s = A1*ed+B1*ek+A*ed1+B*ek1
    delta_w_ss = (A2*ed+B2*ek+2*A1*ed1+2*B1*ek1+A*ed2+B*ek2)
    delta_zprime=sp.expand(delta_w+2*s*delta_w_s)
    delta_zsecond_over_r=sp.expand(6*delta_w_s+4*s*delta_w_ss)
    # Exact original Step58 Z_D and Z_K on Fz=0, after parity scaling.
    r=sp.symbols('r',positive=True)
    ZD=t**sp.Rational(3,2)/(r*r*k)
    ZK=-r*w*t/(r*r*k)
    assert sp.simplify(ZD*r**3*ed+ZK*r**2*ek-r*delta_w)==0
    # Independent implicit differentiation of stationary Fhat.
    implicit_residual=sp.simplify(ed-w/sp.sqrt(t)*ek-k/t**sp.Rational(3,2)*delta_w)
    assert implicit_residual==0
    return locals()


def exact_certificates():
    v=exact_variation_jets()
    k,k1,k2,s,w=(v[x] for x in ('k','k1','k2','s','w'))
    t=v['t']
    expect_A1=-3*w*w*sp.sqrt(t)/(2*k)-t**sp.Rational(3,2)*k1/k**2
    expect_B1=w**3/k+w*t*k1/k**2
    expect_A2=(3*w**4/(4*k*sp.sqrt(t)) + 3*w*w*sp.sqrt(t)*k1/k**2
               +t**sp.Rational(3,2)*(2*k1**2/k**3-k2/k**2))
    expect_B2=-2*w**3*k1/k**2+w*t*(k2/k**2-2*k1**2/k**3)
    for actual,expected in ((v['A1'],expect_A1),(v['B1'],expect_B1),
                            (v['A2'],expect_A2),(v['B2'],expect_B2)):
        assert sp.simplify(actual-expected)==0
    # The center shift variation is generally NONZERO even though
    # its fixed background has z''=0; this is the missing Step58 safeguard.
    center={s:0,w:sp.Rational(1,250),k:sp.Rational(1,2),k1:0,k2:0,
            v['ed']:1,v['ek']:0,v['ed1']:0,v['ek1']:0,
            v['ed2']:0,v['ek2']:0}
    assert sp.simplify(v['delta_zprime'].subs(center)-2)==0
    assert sp.simplify(v['delta_zsecond_over_r'].subs(center)+18*sp.Rational(1,250)**2)==0
    assert sp.simplify(v['delta_zsecond_over_r'].subs(s,0)-6*v['delta_w_s'].subs(s,0))==0
    tmin=1-RMAX*RMAX*W0*W0
    assert tmin==F(24999711,25000000)>F(9999,10000)
    return {'linearized_Fhat_exactly_zero':True,
            'original_Step58_ZD_ZK_radial_pullback_exact':True,
            'center_delta_zprime_for_ed_1_k_half':str(v['delta_zprime'].subs(center)),
            'center_delta_zsecond_over_r_for_ed_1_k_half':str(v['delta_zsecond_over_r'].subs(center)),
            'A_s':str(expect_A1),'B_s':str(expect_B1),
            'A_ss':str(expect_A2),'B_ss':str(expect_B2),
            't_min_exact':str(tmin)}


def manifest():
    c=exact_certificates()
    return {'step':'68a','date':'2026-10-24',
            'branch':'research/gate2b-nonhomothetic-transfer',
            'headline':'Exact center regular Frechet response of z,zprime,zsecond on prescribed Step55 radial shift chart',
            'premises':'Genuine Step58 shift algebra; K=r²k, Dg=r³d, z=r/250, k>229/1000 on fixed Step55 initial data; historical physical module NOT imported in this run',
            'delta_w':'A ed+B ek, A=t^(3/2)/k, B=-w*t/k, t=1-sw²',
            'delta_w_s':'A_s ed+B_s ek+A ed_s+B ek_s',
            'delta_w_ss':'A_ss ed+B_ss ek+2A_s ed_s+2B_s ek_s+A ed_ss+B ek_ss',
            'delta_z':'r delta_w',
            'delta_zprime':'delta_w+2s delta_w_s',
            'delta_zsecond':'2r(3 delta_w_s+2s delta_w_ss)',
            'certificates':c,
            'restriction':'Prescribed constant w background, parity-preserving canonical perturbations; need k_s,k_ss bounds and original Hamiltonian X_H for complete lapse operator',
            'original_HR_provider_imported':False,
            'full_temporal_operator_assembled':False,'Dirac_rank':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(manifest(),indent=2,ensure_ascii=False))

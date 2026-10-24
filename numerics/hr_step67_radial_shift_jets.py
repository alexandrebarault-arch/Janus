"""Step67: center-regular first/second radial jets of the authentic HR shift algebra.

Conditional on Step55's fixed initial profile, NOT a time-evolution/Dirac proof.
The original input is Fz=Dg-K*z/sqrt(1-z*z)=0 with
Dg=r**3*d(s), K=r**2*k(s), z=r*w(s), s=r**2, k>0.
No original physical module is re-imported or run by this standalone step.
"""
from __future__ import annotations
from fractions import Fraction
import json
import sympy as sp

S_MAX=Fraction(289,400)
K_MIN=Fraction(229,1000)
W0=Fraction(1,250)


def shift_jet_algebra():
    """All derivatives are exact, at fixed s or along smooth radial inputs."""
    s,d,k,w,ds,ks,dss,kss=sp.symbols('s d k w d_s k_s d_ss k_ss',real=True)
    t=1-s*w*w
    root=d/sp.sqrt(k*k+s*d*d)  # on positive k chart
    partials={
        's':-w**3/2,
        'd':t**sp.Rational(3,2)/k,
        'k':-w*t/k,
        'ss':3*w**5/4,
        'sd':-3*w*w*t**sp.Rational(3,2)/(2*k),
        'sk':3*w**3*t/(2*k),
        'dd':-3*s*w*t*t/(k*k),
        'dk':(3*s*w*w-1)*t**sp.Rational(3,2)/(k*k),
        'kk':w*(2-3*s*w*w)*t/(k*k),
    }
    # Compare the exact root derivatives to the on-shell formulas using
    # positive numerical rational k,w,s to settle square-root signs.
    q={s:sp.Rational(1,4),k:sp.Rational(1,2),w:sp.Rational(1,250)}
    d_on=k*w/sp.sqrt(t)
    for tag,v in partials.items():
        indices={'s':(s,),'d':(d,),'k':(k,),
                 'ss':(s,s),'sd':(s,d),'sk':(s,k),
                 'dd':(d,d),'dk':(d,k),'kk':(k,k)}[tag]
        exact=sp.diff(root,*indices).subs(d,d_on).subs(q)
        assert sp.simplify(exact-v.subs(q))==0, tag
    first=sp.expand(partials['s']+partials['d']*ds+partials['k']*ks)
    second=(partials['ss']+2*partials['sd']*ds+2*partials['sk']*ks+
            partials['dd']*ds**2+2*partials['dk']*ds*ks+partials['kk']*ks**2+
            partials['d']*dss+partials['k']*kss)
    # d=k*w0/sqrt(1-s*w0²) forces these s derivatives if w0 is constant.
    ds_profile=w*ks/sp.sqrt(t)+k*w**3/(2*t**sp.Rational(3,2))
    dss_profile=(w*kss/sp.sqrt(t)+w**3*ks/t**sp.Rational(3,2)+
                 3*k*w**5/(4*t**sp.Rational(5,2)))
    return {'s':s,'d':d,'k':k,'w':w,'ds':ds,'ks':ks,'dss':dss,'kss':kss,
            't':t,'root':root,'partials':partials,'first':first,'second':second,
            'ds_profile':ds_profile,'dss_profile':dss_profile,
            'zprime':w+2*s*first,'zsecond_over_2r':3*first+2*s*second}


def check_profile_cancellations():
    """Proof of w'=w''=0 for a stationary linear shift z=r*w0."""
    a=shift_jet_algebra()
    ds,ks,dss=a['ds'],a['ks'],a['dss']
    rules={ds:a['ds_profile'],dss:a['dss_profile']}
    first=sp.simplify(a['first'].subs(ds,rules[ds]))
    second=sp.simplify(a['second'].subs(rules))
    assert first==0,first
    assert second==0,second
    # Deliberately omit the explicit s derivative to expose the false jet.
    bad=sp.simplify((a['first']-a['partials']['s']).subs(ds,rules[ds]))
    assert sp.simplify(bad-a['w']**3/2)==0
    return {'first_exactly_zero':first==0,'second_exactly_zero':second==0,
            'missing_explicit_s_term_error':str(bad)}


def exact_bounds():
    """Rational coefficient bounds ON the constrained Step55 baseline only.

    No bounds for d_s,k_s,d_ss,k_ss are asserted here.
    """
    w=W0;k=K_MIN;s=S_MAX
    tmin=1-s*w*w
    ws= w**3/2
    wss=3*w**5/4
    wsd=(Fraction(3,2)*w*w)/k  # t^(3/2)<=1
    wsk=(Fraction(3,2)*w**3)/k  # t<=1
    assert tmin>Fraction(9999,10000)
    assert ws<Fraction(1,30000000)
    assert wss<Fraction(1,1000000000000)
    assert wsd<Fraction(1,9000)
    assert wsk<Fraction(1,2000000)
    return {'t_min':str(tmin),
            'abs_partial_s':str(ws),'abs_partial_ss':str(wss),
            'abs_partial_sd_lt':str(wsd),'abs_partial_sk_lt':str(wsk),
            'scope':'pointwise baseline coefficients, not total radial jet estimates'}


def fail_closed(s_hi,k_lower,w_bench):
    if (Fraction(s_hi),Fraction(k_lower),Fraction(w_bench)) != (S_MAX,K_MIN,W0):
        raise ValueError('Not the certified fixed Step55 radial benchmark')
    return exact_bounds()


def manifest():
    checks=check_profile_cancellations()
    return {'step':67,'date':'2026-10-24',
            'title':'Exact radial shift chain rule and prescribed-profile jet compatibility',
            'branch':'research/gate2b-nonhomothetic-transfer',
            'premises':'Step55 positive k>229/1000, z=r/250; previous physical module not rerun',
            's_partial_at_fixed_dk':'-w**3/2',
            's_second_at_fixed_dk':'3*w**5/4',
            'total_w_s':'W_s+W_d*d_s+W_k*k_s',
            'total_w_ss':'W_ss+2W_sd*d_s+2W_sk*k_s+W_dd*d_s**2+2W_dk*d_s*k_s+W_kk*k_s**2+W_d*d_ss+W_k*k_ss',
            'profile_d_s':'w*k_s/sqrt(t)+k*w**3/(2*t**(3/2))',
            'profile_d_ss':'w*k_ss/sqrt(t)+w**3*k_s/t**(3/2)+3*k*w**5/(4*t**(5/2))',
            'exact_physical_shift_jets':'z(r)=r/250, z_prime(r)=1/250, z_second(r)=0',
            'profile_cancellation_tests':checks,'rational_caps':exact_bounds(),
            'radial_k_d_derivatives_bounded':False,
            'original_physical_Step45_55_imported':False,
            'temporal_preservation_oracle':'NOT_COMPUTED',
            'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(manifest(),indent=2,ensure_ascii=False))

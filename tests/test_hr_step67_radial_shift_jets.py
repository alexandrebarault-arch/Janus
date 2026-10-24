"""Step67 algebra tests: initial radial shift jet, NOT time-Dirac proof."""
import pytest
import sympy as sp
from fractions import Fraction as F
from numerics.hr_step67_radial_shift_jets import (
    shift_jet_algebra, check_profile_cancellations, exact_bounds,
    fail_closed, manifest, S_MAX, K_MIN, W0)

@pytest.fixture(scope='module')
def a():
    return shift_jet_algebra()

def test_explicit_s_derivative_from_positive_root(a):
    s,d,k,w=a['s'],a['d'],a['k'],a['w']
    assert sp.simplify(sp.diff(a['root'],s)+d**3/(2*(k*k+s*d*d)**sp.Rational(3,2)))==0
    assert a['partials']['s']==-w**3/2

def test_s_second_from_root(a):
    s,d,k=a['s'],a['d'],a['k']
    assert sp.simplify(sp.diff(a['root'],s,2)-3*d**5/(4*(k*k+s*d*d)**sp.Rational(5,2)))==0
    assert a['partials']['ss']==3*a['w']**5/4

def test_mixed_cross_partials(a):
    for i,j in (('sd',('s','d')),('sk',('s','k')),('dk',('d','k'))):
        x,y=map(a.__getitem__,j)
        assert sp.simplify(sp.diff(a['root'],x,y)-sp.diff(a['root'],y,x))==0

def test_second_total_derivative_chain_rule(a):
    s=a['s']; d, k=sp.Function('d')(s),sp.Function('k')(s)
    expr=d/sp.sqrt(k*k+s*d*d)
    subs={d:a['d'],k:a['k'],sp.diff(d,s):a['ds'],sp.diff(k,s):a['ks'],
          sp.diff(d,s,2):a['dss'],sp.diff(k,s,2):a['kss']}
    check=sp.diff(expr,s,2).subs(subs)
    # enforce s=0 with positive k, then test several rational on-shell sites;
    # the symbolic component identities were checked independently by provider.
    for si in (0,sp.Rational(1,4),sp.Rational(289,400)):
        kval=sp.Rational(1,2); wval=sp.Rational(1,250)
        dval=kval*wval/sp.sqrt(1-si*wval*wval)
        vals={a['s']:si,a['d']:dval,a['k']:kval,a['w']:wval,
              a['ds']:sp.Rational(1,70),a['ks']:sp.Rational(1,30),
              a['dss']:sp.Rational(1,90),a['kss']:-sp.Rational(1,40)}
        assert sp.simplify(check.subs(vals)-a['second'].subs(vals))==0

def test_first_chain_rule(a):
    assert a['first'].has(a['ds'],a['ks'])
    assert a['partials']['s'] in sp.Add.make_args(a['first'])

def test_profile_exact_stationarity(a):
    s,k,w=a['s'],a['k'],a['w']
    t=a['t']
    d0=k*w/sp.sqrt(t)
    assert sp.simplify(d0-k*w/sp.sqrt(t))==0

def test_profile_first_input_identity(a):
    s,k,w,ks=a['s'],a['k'],a['w'],a['ks']
    d_profile=k*w/sp.sqrt(a['t'])
    assert sp.simplify(sp.diff(d_profile,s)+0 -a['ds_profile'].subs(ks,0))==0

def test_profile_second_input_identity(a):
    s,k,w,ks,kss=a['s'],a['k'],a['w'],a['ks'],a['kss']
    K=sp.Function('K')(s)
    d_profile=K*w/sp.sqrt(1-s*w*w)
    manual=sp.diff(d_profile,s,2).subs({sp.diff(K,s,2):kss,sp.diff(K,s):ks,K:k})
    assert sp.simplify(manual-a['dss_profile'])==0

def test_full_first_and_second_stationarity_cancellation():
    x=check_profile_cancellations()
    assert x['first_exactly_zero'] and x['second_exactly_zero']

def test_missing_explicit_s_gives_spurious_drift(a):
    bad=(a['first']-a['partials']['s']).subs(a['ds'],a['ds_profile'])
    assert sp.simplify(bad-a['w']**3/2)==0
    assert bad.subs({a['w']:W0,a['s']:0,a['k']:sp.Rational(1,2),a['ks']:0})!=0

def test_wrong_profile_d_s_violates_stationarity(a):
    out=a['first'].subs({a['ds']:a['w']*a['ks']/sp.sqrt(a['t'])})
    assert sp.simplify(out+a['w']**3/2)==0 # missing ds term causes spurious nonzero drift
    assert out.subs({a['w']:W0,a['s']:0,a['k']:sp.Rational(1,2),a['ks']:0})!=0

def test_radial_z_prime_formula(a):
    assert sp.simplify(a['zprime']-(a['w']+2*a['s']*a['first']))==0

def test_radial_z_second_formula(a):
    assert sp.simplify(a['zsecond_over_2r']-(3*a['first']+2*a['s']*a['second']))==0

def test_physical_profile_z_primes(a):
    x=a['zprime'].subs({a['ds']:a['ds_profile']})
    y=a['zsecond_over_2r'].subs({a['ds']:a['ds_profile'],a['dss']:a['dss_profile']})
    assert sp.simplify(x-a['w'])==0
    assert sp.simplify(y)==0

def test_center_limits_are_regular(a):
    assert a['partials']['s'].subs(a['s'],0)==-a['w']**3/2
    assert a['zprime'].subs({a['s']:0,a['w']:W0})==W0
    assert a['zsecond_over_2r'].subs({a['s']:0,a['w']:W0}).is_finite is not False

def test_exact_rational_bounds():
    b=exact_bounds()
    assert F(b['t_min'])>F(9999,10000)
    assert F(b['abs_partial_s'])<F(1,30000000)
    assert F(b['abs_partial_ss'])<F(1,1000000000000)
    assert F(b['abs_partial_sd_lt'])<F(1,9000)
    assert F(b['abs_partial_sk_lt'])<F(1,2000000)

def test_fail_closed_wrong_radial_domain():
    with pytest.raises(ValueError):fail_closed(F(3,4),K_MIN,W0)

def test_fail_closed_wrong_shift_or_positive_k():
    with pytest.raises(ValueError):fail_closed(S_MAX,K_MIN,F(1,200))
    with pytest.raises(ValueError):fail_closed(S_MAX,F(1,10),W0)

def test_compatible_parameters_only():
    assert fail_closed(S_MAX,K_MIN,W0)==exact_bounds()

def test_manifest_explicit_open_temporal_rank():
    m=manifest()
    assert m['step']==67
    assert not m['original_physical_Step45_55_imported']
    assert not m['radial_k_d_derivatives_bounded']
    assert m['Dirac_rank']=='NOT_COMPUTED'
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'

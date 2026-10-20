"""Independent non-IBP ADM mixed bracket on curved, two-moving-dust primary data."""
import numpy as np
import pytest
from numerics import hr_independent_collocation_bracket as b

@pytest.fixture(scope='module')
def baseline():
    x,w,D=b.grid(26)
    q=b.curved_primary_arrays(x,D)
    return x,w,D,q


def test_gauss_barycentric_differentiation_reproduces_polynomials():
    x,w,D=b.grid(20)
    np.testing.assert_allclose(D@(x**5),5*x**4,rtol=1e-10,atol=2e-11)
    np.testing.assert_allclose(D@(D@(x**5)),20*x**3,rtol=1e-9,atol=2e-9)


def test_both_independent_curved_spatial_ricci_scalars_from_original_adm(baseline):
    x,w,D,q=baseline
    for sec,mass,curv in [('g',b.A,.015),('f',b.A*b.Y,-.012)]:
        u=1+curv*x*x
        independent=-48*curv/(mass**2*u**5)
        np.testing.assert_allclose(b._curvature(q['L'+sec],q['S'+sec],D),independent,rtol=3e-9,atol=4e-11)
        assert max(abs(independent))>2


def test_original_both_hamiltonian_and_radial_constraints_vanish(baseline):
    x,w,D,q=baseline
    Hg,Hf,Ddiag,Fz,z=b._calc(q,D)
    assert max(max(abs(v)) for v in (Hg,Hf,Ddiag,Fz))<8e-13
    assert min(q['pg'])>.005 and min(q['pf'])>.001
    assert max(abs(z))>.03
    assert max(abs(D@q['tg']))>.002
    assert max(abs(D@q['tf']))>.001


def test_nonzero_original_mixed_functional_bracket_independent_of_old_sympy(baseline):
    x,w,D,q=baseline
    B,components=b.bracket(q,D,w,b.smear(x,kind='N'),b.smear(x,kind='M'))
    assert B==pytest.approx(4.2129335e-6,rel=3e-5)
    assert len(components)==6 and np.sum(components)==pytest.approx(B,abs=1e-18)
    assert abs(components[2])>1.e-8
    assert abs(components[5])<1.e-12   # f dust remains separate, direct mixed term zero
    assert abs(components[0])>1e-7 and abs(components[4])>1e-7


@pytest.mark.parametrize('n', [14,18,22,28,34])
def test_original_non_ibp_bracket_converges_in_radial_resolution(n):
    out=b.witness(n)
    assert out['primary_residual']<2.e-12
    assert out['minimum_pg']>0 and out['minimum_pf']>0
    assert out['bracket']==pytest.approx(4.2129335e-6,rel=3e-5)


@pytest.mark.parametrize('h', [3.e-6,1.e-6,3.e-7])
def test_finite_difference_derivative_step_refinement(h,baseline):
    x,w,D,q=baseline
    B,_=b.bracket(q,D,w,b.smear(x),b.smear(x,kind='M'),h=h)
    assert B==pytest.approx(4.2129335e-6,rel=5e-5)


@pytest.mark.parametrize('pair', [('N','M'),('P','Q')])
def test_smeared_mixed_bracket_is_symmetric_in_smearings_on_primary_surface(pair,baseline):
    x,w,D,q=baseline
    n,m=pair;N=b.smear(x,kind=n);M=b.smear(x,kind=m)
    lhs,_=b.bracket(q,D,w,N,M)
    rhs,_=b.bracket(q,D,w,M,N)
    assert abs(lhs-rhs)<6.e-11
    assert abs(lhs)>1e-7


def test_off_primary_perturbation_breaks_smearing_swap_identity(baseline):
    x,w,D,q=baseline
    q={k:v.copy() for k,v in q.items()}
    q['pg']+=.02*x*x
    Hg,Hf,DD,Fz,z=b._calc(q,D)
    assert max(abs(Hg))>.01
    N=b.smear(x);M=b.smear(x,kind='M')
    lhs,_=b.bracket(q,D,w,N,M);rhs,_=b.bracket(q,D,w,M,N)
    assert abs(lhs-rhs)>5.e-11


def test_localized_lapse_smearing_approaches_prior_local_secondary_value():
    x,w,D=b.grid(62)
    q=b.curved_primary_arrays(x,D)
    profile=b.smear(x)*np.exp(-((x-.43)/.04)**2)
    numerator,_=b.bracket(q,D,w,profile,profile)
    local=numerator/(w@(profile*profile))
    # From the independent earlier Step33g symbolic local calculation: ~+0.47.
    assert .46<local<.53


def test_mixed_poisson_fails_to_vanish_on_primary_surface(baseline):
    x,w,D,q=baseline
    c=b._calc(q,D)
    assert max(max(abs(v)) for v in c[0:4])<1.e-12
    B,_=b.bracket(q,D,w,b.smear(x),b.smear(x,kind='M'))
    assert abs(B)>4.e-6
    # Thus this primary-constrained state has not passed a SECONDARY.


def test_slight_curved_secondary_tuning_is_not_automatic():
    x,w,D=b.grid(18)
    vals=[]
    for gf in (-.18,-.08,0.,.1,.18):
        q=b.curved_primary_arrays(x,D,grav_f=gf)
        assert min(q['pg'])>0 and min(q['pf'])>0
        v,_=b.bracket(q,D,w,b.smear(x),b.smear(x,kind='M'))
        vals.append(v)
    assert all(v>2e-6 for v in vals)
    assert vals==sorted(vals)


def test_invalid_radial_grid_rejected():
    with pytest.raises(ValueError):b.grid(8)
    with pytest.raises(ValueError):b.grid(16,interval=(0,.9))

@pytest.mark.parametrize('n,width,lo,hi',[
    (80,.03,.47,.495),
    (128,.015,.465,.485),
])
def test_independent_local_secondary_probe_has_radial_resolution_control(n,width,lo,hi):
    x,w,D=b.grid(n)
    q=b.curved_primary_arrays(x,D)
    p=b.smear(x)*np.exp(-((x-.43)/width)**2)
    numerator,_=b.bracket(q,D,w,p,p)
    ratio=numerator/(w@(p*p))
    assert lo<ratio<hi

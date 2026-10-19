"""Independent radial functional derivative tests for each canonical dust."""
import numpy as np
import pytest
import sympy as sp
from numerics.hr_spherical_dust_smeared_bracket import (
    sample_dust_radial,discrete_action,bracket_from_functional_variations,
    continuum_momentum_bracket,continuum_hamiltonian_bracket,
    nonrelativistic_wrong_bracket,crossed_dust_sector_bracket,
    DustRadialData,
)


def test_symbolic_square_root_closure_condition():
    u,L=sp.symbols('u L',real=True,positive=True)
    h=sp.sqrt(1+u*u/(L*L))
    assert sp.simplify(h*sp.diff(h,u)-u/(L*L))==0
    wrong=1+u*u/(2*L*L)
    assert sp.simplify(wrong*sp.diff(wrong,u)-u/(L*L))==u**3/(2*L**4)


@pytest.mark.parametrize('shift',[0.,.5,-.8])
def test_radial_momentum_bracket_nontrivial_and_two_derivations(shift):
    data=sample_dust_radial(241,seed_shift=shift)
    exact=continuum_momentum_bracket(data)
    integrated=continuum_hamiltonian_bracket(data)
    assert abs(exact)>1e-4
    assert integrated==pytest.approx(exact,abs=3e-6,rel=2e-4)


@pytest.mark.parametrize('shift',[0.,.5])
def test_independent_canonical_finite_difference_bracket_converges(shift):
    coarse=sample_dust_radial(33,seed_shift=shift)
    fine=sample_dust_radial(129,seed_shift=shift)
    C=bracket_from_functional_variations(coarse)
    F=bracket_from_functional_variations(fine)
    direct=continuum_momentum_bracket(fine)
    assert abs(C-direct)>abs(F-direct)
    assert F==pytest.approx(direct,rel=2e-3,abs=2e-5)


def test_exact_unnormalized_canonical_nodal_p_and_dust_hamiltonian():
    d=sample_dust_radial(25)
    h=d.r[1]-d.r[0]
    w=np.full(len(d.r),h);w[[0,-1]]*=.5
    one=discrete_action(d,d.N)
    two=discrete_action(d,d.N,P=w*d.p)
    assert one==two
    assert one>0


def test_two_separately_conserved_dust_pairs_and_cross_zero():
    g=sample_dust_radial(65,seed_shift=.4)
    f=sample_dust_radial(65,seed_shift=-.9)
    assert abs(bracket_from_functional_variations(g))>1e-4
    assert abs(bracket_from_functional_variations(f))>1e-4
    assert crossed_dust_sector_bracket()==0


def test_exact_sqrt_not_quadratic_truncation():
    d=sample_dust_radial(161,seed_shift=.3)
    expected=continuum_momentum_bracket(d)
    wrong=nonrelativistic_wrong_bracket(d)
    assert abs(wrong-expected)>1e-4


def test_homogeneous_theta_has_zero_radial_constraint_bracket():
    d=sample_dust_radial(65)
    h=DustRadialData(d.r,d.L,np.full_like(d.r,.3),d.p,d.N,d.M)
    assert continuum_momentum_bracket(h)==pytest.approx(0.,abs=1e-15)
    assert bracket_from_functional_variations(h)==pytest.approx(0.,abs=2e-8)


def test_smearing_bracket_antisymmetry_and_selfzero():
    d=sample_dust_radial(65)
    flipped=DustRadialData(d.r,d.L,d.theta,d.p,d.M,d.N)
    expected=continuum_momentum_bracket(d)
    assert continuum_momentum_bracket(flipped)==pytest.approx(-expected,abs=1e-12)
    assert bracket_from_functional_variations(flipped)==pytest.approx(-bracket_from_functional_variations(d),abs=1e-8)
    same=DustRadialData(d.r,d.L,d.theta,d.p,d.N,d.N)
    assert continuum_momentum_bracket(same)==0
    assert bracket_from_functional_variations(same)==pytest.approx(0.,abs=1e-10)


def test_bad_data_rejected():
    d=sample_dust_radial(33)
    with pytest.raises(ValueError):sample_dust_radial(5)
    with pytest.raises(ValueError):crossed_dust_sector_bracket(independent=False)
    with pytest.raises(ValueError):bracket_from_functional_variations(d,step=0)
    with pytest.raises(ValueError):discrete_action(d,np.ones(5))
    with pytest.raises(ValueError):continuum_momentum_bracket(DustRadialData(d.r,-d.L,d.theta,d.p,d.N,d.M))
    with pytest.raises(ValueError):continuum_momentum_bracket(DustRadialData(d.r,d.L,d.theta,d.p,d.N+1,d.M))

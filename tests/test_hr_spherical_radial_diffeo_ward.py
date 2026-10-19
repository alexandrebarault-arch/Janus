"""Radially varying diffeomorphism Ward and D[eta] functional PB algebra.

Necessary spatial gauge-closure witness with both dust pairs. It is NOT the
mixed Hamiltonian bracket or Hassan--Rosen BD secondary.
"""
import numpy as np
import pytest
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_radial_diffeo_ward import (
    default_fields,spatial_generator,transformed,densities,radial_ward,
    smeared_momentum,momentum_gradient,smeared_momentum_poisson,
    CANONICAL_PAIRS,WEIGHTS,
)


def _xi():
    return .11*Poly([0,1])*Poly([1,-1])**2*Poly([1,.3])


@pytest.mark.parametrize('r', [.26,.31,.48,.63,.84])
def test_all_coupled_hamiltonian_densities_and_momentum_have_correct_weights(r):
    w=radial_ward(r=r)
    np.testing.assert_allclose(w.metric_hamiltonian_residual,0,atol=2e-10)
    assert abs(w.diagonal_momentum_residual)<1e-11
    np.testing.assert_allclose(w.curvature_residual,0,atol=2e-8)
    assert abs(w.relative_shift_root_residual)<2e-10
    assert abs(w.relative_shift_equation_residual)<2e-11


def test_near_origin_curvature_cancellation_known_numerical_conditioning():
    # 3-curvature has subtraction of ~1/r² terms; don't fake 1e-12 there.
    w=radial_ward(r=.14)
    assert np.max(abs(w.curvature_residual))<3e-7
    assert np.max(abs(w.metric_hamiltonian_residual))<2e-10


def test_exact_compact_momentum_constraint_functional_pb_closes():
    data=default_fields();eta=spatial_generator();xi=_xi()
    bracket=smeared_momentum_poisson(data,eta,xi)
    rhs=smeared_momentum(data,eta*xi.deriv()-xi*eta.deriv())
    assert abs(bracket)>1e-8
    assert bracket==pytest.approx(rhs,abs=1e-15)
    # Antisymmetry is independent of the compact angular measure convention.
    assert smeared_momentum_poisson(data,xi,eta)==pytest.approx(-bracket,abs=1e-15)
    assert smeared_momentum_poisson(data,eta,eta)==pytest.approx(0,abs=1e-17)


@pytest.mark.parametrize('field',[p for pair in CANONICAL_PAIRS for p in pair])
def test_functional_derivative_of_smeared_D_for_every_canonical_field(field):
    data=default_fields();eta=spatial_generator()
    # A deliberate compact independent perturbation of each radial field.
    variation=Poly([0,.031,-.05,.019])*Poly([1,-1])**2
    step=2e-5
    plus={k:v+(step*variation if k==field else Poly([0.])) for k,v in data.items()}
    minus={k:v-(step*variation if k==field else Poly([0.])) for k,v in data.items()}
    derivative=(smeared_momentum(plus,eta)-smeared_momentum(minus,eta))/(2*step)
    grad=momentum_gradient(data,eta)[field]
    nodes,weights=np.polynomial.legendre.leggauss(56)
    r=(nodes+1)/2
    independent=float(np.dot(weights*.5,grad(r)*variation(r)))
    assert derivative==pytest.approx(independent,abs=1e-12)


def test_two_dust_functional_momenta_not_combined_in_gradient():
    grad=momentum_gradient(default_fields(),spatial_generator())
    assert 'thetag' in grad and 'pg' in grad
    assert 'thetaf' in grad and 'pf' in grad
    assert max(abs(grad['pg'](.3)),abs(grad['pf'](.3)))>0
    assert grad['pg'](.3)!=pytest.approx(grad['pf'](.3),abs=1e-6)
    assert len(CANONICAL_PAIRS)==6


def test_smeared_generator_direct_field_transform_canonical_weights():
    data=default_fields();eta=spatial_generator()
    h=2e-5
    transformed_data=transformed(data,eta,h)
    for name in data:
        w=WEIGHTS[name]
        expected=(eta*data[name].deriv()+w*eta.deriv()*data[name])(.41)
        assert (transformed_data[name](.41)-data[name](.41))/h == pytest.approx(expected,abs=1e-11)


def test_relative_shift_solution_is_scalar_under_spatial_diffeo():
    # The relative-shift equation is a density weight-2 object; solving it
    # algebraically yields a scalar z_root, not a radial lapse or momentum.
    base=default_fields();eta=spatial_generator();r=.47
    h=1e-5;dr=1e-5
    zp=densities(transformed(base,eta,h),r)[2]
    zm=densities(transformed(base,eta,-h),r)[2]
    dz=(zp-zm)/(2*h)
    rderiv=(densities(base,r+dr)[2]-densities(base,r-dr)[2])/(2*dr)
    assert dz==pytest.approx(eta(r)*rderiv,abs=3e-10)


def test_spatial_diff_guards():
    base=default_fields();eta=spatial_generator()
    with pytest.raises(ValueError):transformed({"Lg":Poly([1])},eta,.1)
    with pytest.raises(ValueError):transformed(base,eta,float('nan'))
    with pytest.raises(ValueError):radial_ward(r=.01,dr=.1)
    with pytest.raises(ValueError):radial_ward(epsilon=0)
    with pytest.raises(ValueError):radial_ward(dr=-1)
    with pytest.raises(ValueError):densities(base,-.01)
    with pytest.raises(ValueError):smeared_momentum(base,eta,order=4)
    with pytest.raises(ValueError):momentum_gradient(base,Poly([.1]))

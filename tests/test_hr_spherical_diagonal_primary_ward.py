"""Full spherical primary spatial Ward and two wrong-density negative controls."""
import numpy as np
import pytest
from numerics.hr_spherical_diagonal_primary_ward import (
    smeared_primary_diagonal_ward,smeared_primary_hamiltonians,
)
from numerics.hr_spherical_radial_diffeo_ward import (
    default_fields,spatial_generator,transformed,densities,radial_ward,
)
from numerics.hr_spherical_adm_primary import relative_shift_constraint


def test_two_full_smeared_primary_hamiltonians_under_common_radial_generator():
    got,expected=smeared_primary_diagonal_ward(order=64)
    assert max(abs(expected))>1e-7
    np.testing.assert_allclose(got,expected,atol=3e-11,rtol=2e-8)
    for n in (48,80):
        a,b=smeared_primary_diagonal_ward(order=n)
        np.testing.assert_allclose(a,b,atol=4e-11,rtol=3e-8)
    with pytest.raises(ValueError):smeared_primary_diagonal_ward(epsilon=0.)
    from numpy.polynomial import Polynomial as P
    with pytest.raises(ValueError):smeared_primary_hamiltonians(default_fields(),P([1.]))


def test_wrong_f_dust_momentum_scalar_weight_is_detected():
    data=default_fields();eta=spatial_generator();r=.43;h=1e-5
    assert abs(radial_ward(r=r).metric_hamiltonian_residual[1])<1e-10
    def wrong(eps):
        fields=transformed(data,eta,eps)
        fields['pf']=data['pf']+eps*eta*data['pf'].deriv() # forgot eta' p_f!
        return densities(fields,r)[0][1]
    slope=(wrong(h)-wrong(-h))/(2*h)
    s=2e-5
    base=densities(data,r)[0][1]
    dr=(densities(data,r+s)[0][1]-densities(data,r-s)[0][1])/(2*s)
    assert abs(slope-(eta(r)*dr+eta.deriv()(r)*base))>1e-5


def test_wrong_relative_shift_density_weight_fails_covariant_equation():
    data=default_fields();eta=spatial_generator();r=.47;h=1e-5
    def eq(fields,radius):
        gg,ff,h=densities(fields,radius)[3]
        return relative_shift_constraint(gg,ff,Dg=h.Dg,z=float(fields['z'](radius)),
                                         betas=(.2,1.3,-.35,.4,-.17),m2=.91)
    def wrong(eps):
        fields=transformed(data,eta,eps)
        fields['z']+=eps*eta.deriv()*data['z'] # z is a scalar, NOT density!
        return eq(fields,r)
    actual=(wrong(h)-wrong(-h))/(2*h)
    step=2e-5
    expected=eta(r)*(eq(data,r+step)-eq(data,r-step))/(2*step)+2*eta.deriv()(r)*eq(data,r)
    assert abs(actual-expected)>1e-5

"""Time and native-radius displaced-field quadratic chain-rule gate."""
from dataclasses import replace
import numpy as np
import pytest
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet
from numerics.hr_native_field_sampling import (
    SAMPLED_ORDER, add_native_field_sampling, sampled_native_hr_stueckelberg_jet,
)

P=dict(N=1.,a=.92,n=1.13,alpha=.84,k=2.2,m2=.7,Mg2=1.2,
       betas=(.31,1.,-.4,.2,.13),mu=-.25,sigma_r=-.11,
       sigma_dot=.15,mu_dot=.14,n_dot=.09,alpha_dot=-.07,
       n_ddot=.025,alpha_ddot=-.02)


def test_sampling_dimensions_and_original_principal_block():
    native=native_hr_stueckelberg_jet(r=.17,**P)
    ext=sampled_native_hr_stueckelberg_jet(r=.17,**P)
    assert ext.hessian.shape==(22,22)
    assert len(SAMPLED_ORDER)==22
    np.testing.assert_array_equal(ext.hessian[:14,:14],native.hessian)
    np.testing.assert_array_equal(ext.gradient[:14],native.gradient)
    assert np.max(np.abs(ext.gradient[14:]))==0
    assert ext.value==native.value


def test_native_time_and_radius_sampling_cross_hessian():
    r=.19
    native=native_hr_stueckelberg_jet(r=r,**P)
    ext=add_native_field_sampling(native,r=r)
    for j in range(4):
        coeff=native.gradient[4+j]
        assert ext.hessian[8,14+j]==pytest.approx(coeff)
        assert ext.hessian[13,18+j]==pytest.approx(r*coeff)
        assert ext.hessian[14+j,8]==pytest.approx(coeff)
        assert ext.hessian[18+j,13]==pytest.approx(r*coeff)
    # All other couplings to the derivative columns are exactly zero.
    H=ext.hessian.copy()
    for j in range(4):
        H[8,14+j]=H[14+j,8]=0.
        H[13,18+j]=H[18+j,13]=0.
    np.testing.assert_array_equal(H[:,14:],np.zeros((22,8)))


def test_direct_second_order_chain_rule_with_field_displacement():
    r=.19
    native=native_hr_stueckelberg_jet(r=r,**P)
    ext=add_native_field_sampling(native,r=r)
    x=np.zeros(22)
    x[:14]=np.array([.1,.05,-.07,.02,.15,-.09,.04,.12,
                      -.11,.03,.18,-.02,.13,-.06])
    x[14:]=np.array([.12,-.13,.07,-.02,.04,.05,-.03,.09])
    z=x[:14].copy()
    # Explicit Taylor substitution (q_f evaluated at displaced native chart).
    for j in range(4):
        z[4+j]+=x[14+j]*x[8]+x[18+j]*r*x[13]
    # Only compare all terms of total perturbative order <=2.
    rhs=(native.gradient@z+
         .5*x[:14]@native.hessian@x[:14])
    lhs=ext.gradient@x+.5*x@ext.hessian@x
    assert lhs==pytest.approx(rhs,abs=5e-14)


def test_beta0_decoupling_and_center_radial_regular_limit():
    p=dict(P,betas=(1.,0.,0.,0.,0.))
    b0=sampled_native_hr_stueckelberg_jet(r=.2,**p)
    np.testing.assert_allclose(b0.hessian[14:,:],0,atol=1e-14)
    general=sampled_native_hr_stueckelberg_jet(r=0.,**P)
    assert np.max(np.abs(general.hessian[18:,:]))==0
    assert np.max(np.abs(general.hessian[8,14:18]))>0


def test_invalid_radius_and_wrong_source_dimensions():
    local=native_hr_stueckelberg_jet(r=0.,**P)
    with pytest.raises(ValueError): add_native_field_sampling(local,r=-1.)
    with pytest.raises(ValueError): add_native_field_sampling(local,r=float('nan'))
    with pytest.raises(ValueError):
        add_native_field_sampling(replace(local,hessian=np.zeros((13,13))),r=0.)

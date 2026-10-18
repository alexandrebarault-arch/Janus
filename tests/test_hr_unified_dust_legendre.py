"""Independent algebraic canonical Legendre check for BOTH native dust sectors."""
import numpy as np
import pytest
from numerics.hr_unified_dust_legendre import native_dust_legendre
from numerics.hr_unified_spacetime_offshell import (
    native_geometry_and_densities,_background,
)


def _inputs(sector):
    T=np.array([-.2,.0,.23]); R=np.array([.19,.35,.46])
    x=(.021,-.018,.012,.009,.036,-.025)
    _,L,metric=native_geometry_and_densities(T,R,sector,x)
    n,a,_,_,rc=_background(T,sector)
    rho=(rc/a**3)*(1+x[5]*(1+.12*T+.08*R*R))
    qt=n+x[4]*.16*(1+.1*R*R)
    qr=x[4]*(1+.16*T)*.2*R
    return metric,rho,qt,qr,L


def test_both_native_dust_sectors_have_exact_phase_legendre_transform():
    for sector in ('g','f'):
        m,rho,qt,qr,original=_inputs(sector)
        result=native_dust_legendre(m,rho,qt,qr)
        np.testing.assert_allclose(result.lagrangian,original,rtol=0,atol=1e-14)
        np.testing.assert_allclose(result.momentum*qt-result.hamiltonian,
                                   original,rtol=0,atol=1e-14)
        assert np.all(result.momentum>0)


def test_density_elimination_exact_for_future_oriented_on_shell_clock():
    for sector in ('g','f'):
        m,rho,qt,qr,_=_inputs(sector)
        a=native_dust_legendre(m,rho,qt,qr)
        grr=m[2]
        qt_shell=a.native_lapse*np.sqrt(1+qr*qr/grr)+a.native_shift*qr
        b=native_dust_legendre(m,rho,qt_shell,qr)
        np.testing.assert_allclose(b.stationary_rho,rho,rtol=3e-15,atol=3e-15)
        np.testing.assert_allclose(b.hamiltonian,b.reduced_hamiltonian,
                                   rtol=3e-15,atol=3e-15)


def test_separate_canonical_phase_momenta_have_rank_two():
    # Native phase velocities are independent; the combined momenta have
    # two separate positive velocity derivatives in the pressureless action.
    deriv=[]
    for sector in ('g','f'):
        m,rho,qt,qr,_=_inputs(sector)
        p=native_dust_legendre(m,rho,qt,qr)
        expected=p.spatial_measure*rho/p.native_lapse
        assert np.all(expected>0)
        h=2e-5
        derivative=(native_dust_legendre(m,rho,qt+h,qr).momentum
                   -native_dust_legendre(m,rho,qt-h,qr).momentum)/(2*h)
        np.testing.assert_allclose(derivative,expected,rtol=2e-10,atol=1e-12)
        deriv.append(float(derivative[1]))
    two=np.diag(deriv)
    assert np.linalg.matrix_rank(two)==2


def test_density_constraint_is_not_automatically_on_shell():
    m,rho,qt,qr,_=_inputs('f')
    out=native_dust_legendre(m,rho,qt,qr)
    assert np.max(np.abs(out.stationary_rho-rho))>1e-4
    assert np.max(np.abs(out.hamiltonian-out.reduced_hamiltonian))>1e-7


def test_native_dust_legendre_guards():
    m,rho,qt,qr,_=_inputs('g')
    with pytest.raises(ValueError):native_dust_legendre(m[:3],rho,qt,qr)
    with pytest.raises(ValueError):native_dust_legendre(m,-rho,qt,qr)
    with pytest.raises(ValueError):native_dust_legendre(m,rho,-qt*3,qr)
    with pytest.raises(ValueError):native_dust_legendre((m[0],m[1],-m[2],m[3]),rho,qt,qr)

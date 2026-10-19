"""Step33f: local differential kernel and a TRUE radial primary-surface witness.

These are neither a general local HR BD secondary nor lapse-preservation proof.
"""
import numpy as np
import pytest
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_local_mixed_kernel import (
    default_fields,compact_smearings,local_mixed_kernel,
    evaluate_kernel,integrate_kernel,
)
from numerics.hr_spherical_mixed_hamiltonian_bracket import mixed_smeared_poisson
from numerics.hr_spherical_radial_primary_surface import (
    radial_primary_witness,primary_residuals,constrained_local_kernel,
    local_secondary_candidate,dust_candidate_y,
)


def test_nine_coefficients_exactly_reproduce_arbitrary_smearing_jets():
    r=.43;N,M=compact_smearings()
    k=local_mixed_kernel(r=r)
    assert k.coefficients.shape==(3,3)
    g=k.g_gradient_by_njet
    f=k.f_gradient_by_mjet
    assert g.shape==f.shape==(3,12)
    actual=evaluate_kernel(k,N,M)
    # Independent original first-variation Euler derivatives of full primaries.
    from numerics.hr_spherical_mixed_hamiltonian_bracket import functional_gradients_at
    gg,ff=functional_gradients_at(default_fields(),N,M,r)
    expected=sum(gg[2*i]*ff[2*i+1]-gg[2*i+1]*ff[2*i]
                 for i in range(6))
    assert actual==pytest.approx(expected,abs=3e-13)


@pytest.mark.parametrize('mode',('root','fixed'))
@pytest.mark.parametrize('r',(.22,.43,.71))
def test_local_differential_order_and_genuine_second_derivative_cancellation(mode,r):
    k=local_mixed_kernel(r=r,z_mode=mode,
             z_fixed=Poly([.08,.03,-.01]) if mode=='fixed' else None).coefficients
    np.testing.assert_allclose(k[:,2],0.,atol=1e-14)
    np.testing.assert_allclose(k[2,1:],0.,atol=1e-14)
    assert k[2,0]==pytest.approx(k[1,1],abs=5e-14)
    assert abs(k[0,0])>.05


def test_radial_integration_of_local_kernel_matches_FULL_mixed_poisson():
    for N,M in (compact_smearings(),tuple(reversed(compact_smearings()))):
        out=integrate_kernel(N=N,M=M,order=40)
        direct=mixed_smeared_poisson(N=N,M=M,order=40)
        assert out.sum()==pytest.approx(direct.bracket,rel=2e-9,abs=3e-13)
        assert abs(out[1,1])>1e-7
        assert abs(out[2,0])>1e-7


def test_kernel_remains_genuinely_radial_not_pointwise_homogeneous_offshell():
    k=local_mixed_kernel(r=.43).coefficients
    assert abs(k[0,1])>.01
    assert abs(k[1,0])>.1
    assert abs(k[2,0])>.1


@pytest.mark.parametrize('a',(1.,.4,.2,.05,.03))
def test_independent_radial_primary_surface_and_closed_form_secondary(a):
    w=radial_primary_witness(a=a)
    for r in (.2,.43,.72):
        # Separate exact ORIGINAL non-IBP ADM primary reconstruction.
        assert max(abs(primary_residuals(w,r)))<2e-11
        assert min(w.fields['pg'](r),w.fields['pf'](r))>0
        ker=constrained_local_kernel(w,r).coefficients
        assert abs(ker[0,0]-local_secondary_candidate(w,r))<3e-12
        np.testing.assert_allclose(ker[1:,:],0,atol=2e-11)
        np.testing.assert_allclose(ker[0,1:],0,atol=2e-11)
        assert abs(ker[0,0])>1e-5


def test_radially_varying_primary_surface_is_not_just_homogeneous_chi():
    w=radial_primary_witness(a=.4)
    r=.43; x=w.P_g/(w.mg2*w.a)-w.P_f/(w.mf2*w.b)
    J=w.betas[1]+2*w.betas[2]*w.b/w.a+w.betas[3]*(w.b/w.a)**2
    homogeneous_naive=.5*w.m2*w.mg2*w.a**2*J*r*r*(3*x(r))
    exact=local_secondary_candidate(w,r)
    assert abs(exact-homogeneous_naive)>.01
    assert exact==pytest.approx(-.11307718948650095,rel=2e-11)


def test_spherical_constrained_radial_bracket_matches_independent_FULL_integration():
    w=radial_primary_witness(a=.4)
    n,m=compact_smearings()
    direct=mixed_smeared_poisson(w.fields,n,m,order=40,
              betas=w.betas,m2=w.m2,mg2=w.mg2,mf2=w.mf2)
    local=integrate_kernel(w.fields,n,m,order=40,
              betas=w.betas,m2=w.m2,mg2=w.mg2,mf2=w.mf2)
    assert local.sum()==pytest.approx(-7.916775842392439e-7,abs=4e-15)
    assert local.sum()==pytest.approx(direct.bracket,abs=3e-15)
    np.testing.assert_allclose(local[1:,:],0.,atol=2e-13)
    np.testing.assert_allclose(local[0,1:],0.,atol=2e-13)
    assert direct.shift_equation_max<1e-12


def test_secondary_synchronized_momenta_can_cancel_with_independent_dust_sources():
    w=radial_primary_witness(a=.4,synchronized=True)
    for r in (.19,.43,.77):
        np.testing.assert_allclose(primary_residuals(w,r),0.,atol=4e-13)
        k=constrained_local_kernel(w,r)
        np.testing.assert_allclose(k.coefficients,0.,atol=3e-12)
    # Both dust momenta remain separate positive functions of radius.
    assert w.fields['pg'](.43)>0 and w.fields['pf'](.43)>0
    assert w.fields['pg'](.43)!=pytest.approx(w.fields['pf'](.43))


def test_homogeneous_subset_recovers_previous_minisuperspace_Poisson_secondary():
    w=radial_primary_witness(a=.4,eps_g=0.,eps_f=0.,momentum_fraction=.015)
    r=.43; Pg=w.P_g(r);Pf=w.P_f(r)
    chi=3*(Pg/(w.mg2*w.a)-Pf/(w.mf2*w.b))
    J=w.betas[1]+2*w.betas[2]*w.b/w.a+w.betas[3]*(w.b/w.a)**2
    previous_homogeneous=.5*w.m2*w.mg2*w.a*w.a*J*chi
    assert constrained_local_kernel(w,r).coefficients[0,0]/r**2==pytest.approx(previous_homogeneous,abs=3e-12)


def test_physically_homogeneous_candidate_chi_zero_on_seven_epoch_controls():
    for a in (1.,.8,.4,.2,.09,.05,.03):
        w=radial_primary_witness(a=a,eps_g=0.,eps_f=0.)
        for r in (.25,.6):
            np.testing.assert_allclose(primary_residuals(w,r),0,atol=6e-12)
            assert abs(local_secondary_candidate(w,r))<3e-11
            assert abs(constrained_local_kernel(w,r).coefficients[0,0])<3e-11


def test_two_independent_dust_perturbations_remain_positive_in_constraints():
    for eg,ef,shift in ((.1,.07,.02),(-.09,-.08,-.02),(.01,-.12,.03)):
        w=radial_primary_witness(a=.4,eps_g=eg,eps_f=ef,momentum_fraction=shift)
        for r in (.15,.35,.63,.85):
            assert min(w.fields['pg'](r),w.fields['pf'](r))>0
            assert max(abs(primary_residuals(w,r)))<4e-11
            k=constrained_local_kernel(w,r).coefficients
            assert abs(k[0,0]-local_secondary_candidate(w,r))<7e-12


def test_invalid_domains_and_degenerate_relative_shift_rejected():
    with pytest.raises(ValueError):local_mixed_kernel(r=0.)
    with pytest.raises(ValueError):local_mixed_kernel(r=.5,complex_step=0.)
    with pytest.raises(ValueError):evaluate_kernel(local_mixed_kernel(),None,Poly([1]))
    with pytest.raises(ValueError):radial_primary_witness(a=.01)
    with pytest.raises(ValueError):radial_primary_witness(eps_g=.9)
    with pytest.raises(ValueError):radial_primary_witness(eps_g=float('nan'))
    with pytest.raises(ValueError):local_secondary_candidate(radial_primary_witness(),r=0.)
    with pytest.raises(ValueError):local_mixed_kernel(m2=0.)
    with pytest.raises(ValueError):integrate_kernel(N=Poly([1]))

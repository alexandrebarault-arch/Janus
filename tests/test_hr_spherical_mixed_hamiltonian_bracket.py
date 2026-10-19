"""Mixed functional spherical Hamiltonian bracket with both canonical dusts.

Independently finite-difference the ORIGINAL (second-radial-derivative)
ADM+HR+dust primary action against the derivative-after-IBP Euler oracle.
Do not confuse this off-shell bracket with the BD secondary or 4D counting.
"""
import math
import numpy as np
import pytest
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_mixed_hamiltonian_bracket import (
    Q,CANONICAL_PAIRS,BOUNDS,DEFAULT_BETAS,DEFAULT_M2,DEFAULT_MG2,
    DEFAULT_MF2,default_fields,compact_smearings,relative_shift_jet,
    functional_gradients_at,mixed_smeared_poisson,smeared_primary,
)


def direct_original_primary(fields,N,M,*,order=48,z_mode='root',z_fixed=None,
                            betas=DEFAULT_BETAS,m2=DEFAULT_M2,
                            mg2=DEFAULT_MG2,mf2=DEFAULT_MF2,interval=BOUNDS):
    """Independent original unintegrated spherical Hamiltonian densities.

    Uses full native 3-curvature with S'' and L', and -L pL' BEFORE radial
    integration by parts. The source code under test instead uses a purely
    FIRST-derivative compact variational integrand.
    """
    x,w=np.polynomial.legendre.leggauss(order)
    a,b=interval
    x=(a+b)/2+(b-a)*x/2;w=(b-a)*w/2
    vals=np.zeros(2)
    for r,weight in zip(x,w):
        d={k:fields[k](r) for k in Q}
        dr={k:fields[k].deriv()(r) for k in Q}
        d2={k:fields[k].deriv(2)(r) for k in Q}
        z=relative_shift_jet(fields,betas=betas,m2=m2,mg2=mg2,r=r)[0] if z_mode=='root' else z_fixed(r)
        ell=d['Sf']/d['Sg'];b0,b1,b2,b3,b4=betas
        A0=b0+2*b1*ell+b2*ell**2
        As=b2+2*b3*ell+b4*ell**2
        At=b1+2*b2*ell+b3*ell**2
        root=math.sqrt(1-z*z)
        fac=m2*mg2*d['Sg']**2
        Wg=fac*(d['Lg']*A0+d['Lf']*At*root)
        Wf=fac*(d['Lf']*As+d['Lg']*At*root)
        def c_sector(tag,planck):
            L,S,pL,pS,p,theta=(d['L'+tag],d['S'+tag],d['pL'+tag],
                                 d['pS'+tag],d['p'+tag],d['t'+tag])
            Lr,Sr,Srr=dr['L'+tag],dr['S'+tag],d2['S'+tag]
            W=Sr/L; Wr=Srr/L-Sr*Lr/L**2
            R3=2/S**2*(1-W*W-2*S/L*Wr)
            return (L*pL**2/(4*planck*S**2)-pL*pS/(2*planck*S)
                    -planck*L*S*S*R3/2+p*math.sqrt(1+dr['t'+tag]**2/L**2))
        Dg=d['pSg']*dr['Sg']-d['Lg']*dr['pLg']+d['pg']*dr['tg']
        Hg=c_sector('g',mg2)+z*Dg/d['Lg']+Wg
        Hf=c_sector('f',mf2)+z*Dg/d['Lf']+Wf
        vals+=weight*np.array([N(r)*Hg,M(r)*Hf])
    return vals


def _variation(fields,name,delta,h):
    new=dict(fields)
    new[name]=fields[name]+h*delta
    return new


def _projected_gradient(fields,N,M,name,delta,*,order=44):
    x,w=np.polynomial.legendre.leggauss(order)
    a,b=BOUNDS
    r=(a+b)/2+(b-a)*x/2;w=(b-a)*w/2
    p=Q.index(name)
    return np.array([sum(wi*functional_gradients_at(fields,N,M,ri)[k,p]*delta(ri)
                         for ri,wi in zip(r,w)) for k in range(2)])


def test_exact_relative_shift_jet_and_stationary_saddle():
    fields=default_fields()
    for r in (.13,.21,.41,.75,.87):
        z,zr,zrr=relative_shift_jet(fields,r=r)
        D=(fields['pSg']*fields['Sg'].deriv()-fields['Lg']*fields['pLg'].deriv()
           +fields['pg']*fields['tg'].deriv())(r)
        b0,b1,b2,b3,b4=DEFAULT_BETAS
        K=(DEFAULT_M2*DEFAULT_MG2*fields['Lg']*fields['Lf']*
           (b1*fields['Sg']**2+2*b2*fields['Sg']*fields['Sf']+b3*fields['Sf']**2))(r)
        assert abs(z)<1
        assert D-K*z/math.sqrt(1-z*z)==pytest.approx(0,abs=1e-13)
        h=2.e-5
        zp=relative_shift_jet(fields,r=r+h)[0]
        zm=relative_shift_jet(fields,r=r-h)[0]
        assert (zp-zm)/(2*h)==pytest.approx(zr,rel=2e-7,abs=5e-9)
        assert (zp+zm-2*z)/h**2==pytest.approx(zrr,rel=3e-4,abs=1e-4)


@pytest.mark.parametrize('mode',["root","fixed"])
def test_independent_original_curvature_and_momentum_matches_IBP_action(mode):
    fields=default_fields();N,M=compact_smearings()
    zfixed=Poly([.08,.035,-.01])
    direct=direct_original_primary(fields,N,M,z_mode=mode,z_fixed=zfixed)
    compact=smeared_primary(fields,N,M,z_mode=mode,z_fixed=zfixed)
    np.testing.assert_allclose(compact,direct,atol=4e-12,rtol=3e-11)


@pytest.mark.parametrize('field',Q)
def test_all_twelve_field_euler_derivatives_vs_independent_action_differences(field):
    fields=default_fields();N,M=compact_smearings()
    a,b=BOUNDS
    delta=(Poly([-a,1])**3*Poly([b,-1])**3)*(1/((.5-a)**3*(b-.5)**3))
    h=3.e-5
    # This varies the *algebraically eliminated* z*(canonical fields) too.
    plus=direct_original_primary(_variation(fields,field,delta,h),N,M,order=52)
    minus=direct_original_primary(_variation(fields,field,delta,-h),N,M,order=52)
    fd=(plus-minus)/(2*h)
    functional=_projected_gradient(fields,N,M,field,delta,order=52)
    np.testing.assert_allclose(fd,functional,atol=2e-9,rtol=2e-5)


def test_nonhomogeneous_mixed_bracket_root_two_dust_and_quadrature():
    x=mixed_smeared_poisson(order=30)
    y=mixed_smeared_poisson(order=48)
    z=mixed_smeared_poisson(order=60)
    assert y.bracket==pytest.approx(1.2437914369616798e-6,abs=2e-12)
    assert x.bracket==pytest.approx(y.bracket,abs=3e-10)
    assert z.bracket==pytest.approx(y.bracket,abs=3e-10)
    assert y.shift_equation_max<1e-13
    assert y.independent_dust_pairs==2
    assert abs(y.sector_contributions[2])>1e-9
    assert abs(y.sector_contributions[4])>1e-8
    assert y.sector_contributions[5]==0
    assert y.bracket==pytest.approx(sum(y.sector_contributions),abs=1e-14)


def test_eliminated_relative_shift_is_not_fixed_external_field():
    root=mixed_smeared_poisson()
    fixed=mixed_smeared_poisson(z_mode='fixed',z_fixed=Poly([.08,.035,-.01]))
    assert abs(root.bracket-fixed.bracket)>7e-7
    assert root.hg_integral!=pytest.approx(fixed.hg_integral,abs=1e-7)


def test_smeared_derivative_terms_prevent_naive_ultralocal_secondary():
    N,M=compact_smearings()
    first=mixed_smeared_poisson(N=N,M=M)
    switched=mixed_smeared_poisson(N=M,M=N)
    assert abs(first.bracket-switched.bracket)>3e-8
    # Changing smear ordering is not {Hg,Hf} -> -{Hf,Hg}: it diagnoses
    # radial derivatives of the smearing in a genuinely local bracket.


def test_degenerate_K_no_root_and_decoupled_zero_HR_case():
    with pytest.raises(ValueError):
        mixed_smeared_poisson(betas=(1.,0.,0.,0.,1.))
    with pytest.raises(ValueError):
        mixed_smeared_poisson(m2=0)
    free=mixed_smeared_poisson(m2=0,z_mode='fixed',z_fixed=Poly([0.]))
    assert free.bracket==pytest.approx(0.,abs=1e-15)


def test_compact_smearings_and_parameter_guards():
    fields=default_fields();N,M=compact_smearings()
    assert abs(N(.1))+abs(N(.9))+abs(M(.1))+abs(M(.9))<1e-12
    with pytest.raises(ValueError):mixed_smeared_poisson(order=4)
    with pytest.raises(ValueError):mixed_smeared_poisson(mg2=0)
    with pytest.raises(ValueError):mixed_smeared_poisson(fields={'Lg':Poly([1])})
    with pytest.raises(ValueError):mixed_smeared_poisson(N=Poly([1]))
    with pytest.raises(ValueError):mixed_smeared_poisson(z_mode='nonsense')


def test_dust_f_canonical_gradients_remain_independent():
    fields=default_fields();N,M=compact_smearings()
    grads=functional_gradients_at(fields,N,M,.35)
    assert grads.shape==(2,12)
    assert np.all(grads[0,10:12]==0)
    assert abs(grads[1,10])+abs(grads[1,11])>1e-6
    assert abs(grads[0,4])+abs(grads[0,5])>1e-6
    assert abs(grads[1,4])+abs(grads[1,5])>1e-6


@pytest.mark.parametrize('name',('Lg','Sg','pLg','pg','Lf','Sf','pLf','pf'))
def test_fixed_z_functional_gradients_vs_direct_undifferentiated_action(name):
    fields=default_fields();N,M=compact_smearings()
    zz=Poly([.08,.035,-.01]);a,b=BOUNDS
    delta=Poly([-a,1])**3*Poly([b,-1])**3/(.4**6)
    h=2.e-5
    plus=direct_original_primary(_variation(fields,name,delta,h),N,M,
                                 z_mode='fixed',z_fixed=zz)
    minus=direct_original_primary(_variation(fields,name,delta,-h),N,M,
                                  z_mode='fixed',z_fixed=zz)
    x,w=np.polynomial.legendre.leggauss(40);r=(a+b)/2+(b-a)*x/2;w=(b-a)*w/2
    proj=np.array([sum(wi*functional_gradients_at(fields,N,M,ri,
                     z_mode='fixed',z_fixed=zz)[k,Q.index(name)]*delta(ri)
                     for ri,wi in zip(r,w)) for k in range(2)])
    np.testing.assert_allclose((plus-minus)/(2*h),proj,atol=5e-9,rtol=2e-5)


def test_radial_complex_step_robustness_and_independent_matter_channels():
    f=default_fields();N,M=compact_smearings()
    a=functional_gradients_at(f,N,M,.42,complex_step=1e-16)
    b=functional_gradients_at(f,N,M,.42,complex_step=1e-20)
    np.testing.assert_allclose(a,b,atol=2e-10,rtol=2e-10)
    assert np.linalg.norm(a[:,[4,5,10,11]])>0
    assert a[0,10]==a[0,11]==0


def test_mixed_poisson_changes_with_nonhomogeneous_radial_matter_gradient():
    fields=default_fields()
    first=mixed_smeared_poisson(fields=fields)
    varied=dict(fields)
    varied['tg']=fields['tg']+Poly([0.,.12,.03])
    varied['pg']=fields['pg']*1.08
    changed=mixed_smeared_poisson(fields=varied)
    assert abs(first.bracket-changed.bracket)>1e-9
    assert changed.shift_equation_max<1e-12
    assert changed.sector_contributions[5]==0

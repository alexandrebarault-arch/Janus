"""Independent local interaction-Hessian controls for finite-mu spherical maps."""
import numpy as np
import pytest

from numerics.hr_native_quadratic_jet import native_hr_scalar_jet


def published_de_felice_quadratic(x, *, N, a, n, alpha, k, betas, m2, Mg2):
    """Independent transcription of the published quadratic HR Eq. (45)-(46)."""
    Pg,Bg,sg,Eg,Pf,Bf,sf,Ef=x
    b0,b1,b2,b3,b4=betas
    xi=alpha/a; c=n*a/(N*alpha)
    J=b1+2*b2*xi+b3*xi*xi
    Gamma=xi*J+(c-1)*xi*xi*(b2+b3*xi)
    rg=b0+3*b1*xi+3*b2*xi**2+b3*xi**3
    rf=b4+3*b3/xi+3*b2/xi**2+b1/xi**3
    k2=k*k; k4=k2*k2
    tg,tf=6*sg,6*sf
    hg=12*sg*sg+(2/3)*k4*Eg*Eg
    hf=12*sf*sf+(2/3)*k4*Ef*Ef
    vg=-.5*Pg*Pg+.5*k2*Bg*Bg+.125*(tg*tg-2*hg)+.5*Pg*tg
    vf=-.5*Pf*Pf+.5*k2*Bf*Bf+.125*(tf*tf-2*hf)+.5*Pf*tf
    delta=(Pg-c*Pf)*(tg-tf)+k2*(Bg-c*Bf)**2/(c+1)-.25*(c-1)*(tg*tg-tf*tf-2*(hg-hf))
    cross=12*sg*sf+(2/3)*k4*Eg*Ef
    gamma=(tg-tf)**2 - (hg+hf-2*cross)
    return m2*Mg2*(-N*a**3*rg*vg-n*alpha**3*rf*vf+.5*N*a**3*xi*J*delta+.125*N*a**3*Gamma*gamma)


def published_hessian(**kw):
    e=np.eye(8)
    d=np.array([2*published_de_felice_quadratic(e[i],**kw) for i in range(8)])
    H=np.diag(d)
    for i in range(8):
        for j in range(i+1,8):
            Hij=(published_de_felice_quadratic(e[i]+e[j],**kw)-published_de_felice_quadratic(e[i]-e[j],**kw))/2
            H[i,j]=H[j,i]=Hij
    return H


@pytest.mark.parametrize('mu,r,sigma_dot,sigma_r,mu_dot',[
    (0.0,0.,0.,0.,0.),
    (0.0,.7,0.,0.,0.),
    (-.3,0.,12.,-1.7,.9),
])
def test_center_limit_matches_all_eight_de_felice_quadratic_variables(mu,r,sigma_dot,sigma_r,mu_dot):
    p=dict(N=1.,a=.8,n=1.17*.86,alpha=.8*1.17,k=2.2,
           m2=.7,Mg2=1.3,betas=(.2,.41,-.23,.17,.31))
    out=native_hr_scalar_jet(**p,mu=mu,r=r,sigma_dot=sigma_dot,sigma_r=sigma_r,mu_dot=mu_dot)
    expected=published_hessian(**{**p,'alpha':p['alpha']*(1+mu)})
    # At r=0, derivatives in time/r do not enter the central potential.
    if r == 0 or (mu==0 and sigma_dot==sigma_r==mu_dot==0):
        np.testing.assert_allclose(out.hessian,expected,rtol=2e-11,atol=2e-11)
    np.testing.assert_allclose(out.hessian,out.hessian.T,atol=1e-14)


def test_beta4_piece_does_not_depend_on_any_g_metric_field_even_off_center():
    out=native_hr_scalar_jet(N=1,a=.8,n=1.16,alpha=.9,k=2.,
        m2=.7,Mg2=1,betas=(0,0,0,0,1),mu=-.45,r=.13,
        sigma_r=-.8,sigma_dot=.21,mu_dot=.03)
    assert np.max(np.abs(out.gradient[:4]))<2e-11
    assert np.max(np.abs(out.hessian[:4,:]))<2e-11


def test_beta0_piece_does_not_depend_on_any_f_metric_field():
    out=native_hr_scalar_jet(N=1,a=.8,n=1.16,alpha=.9,k=2.,
        m2=.7,Mg2=1,betas=(1,0,0,0,0),mu=-.45,r=.13,
        sigma_r=-.8,sigma_dot=.21,mu_dot=.03)
    assert np.max(np.abs(out.gradient[4:]))<2e-11
    assert np.max(np.abs(out.hessian[4:,:]))<2e-11


def test_finite_radius_hr_hessian_not_identical_to_frozen_center():
    p=dict(N=1,a=.8,n=1.16,alpha=.9,k=2.3,
           m2=.7,Mg2=1,betas=(0.,1.,-.5,.24,0.),mu=-.4,
           sigma_r=-.6,sigma_dot=.17,mu_dot=.14)
    center=native_hr_scalar_jet(**p,r=0)
    radial=native_hr_scalar_jet(**p,r=.08)
    assert np.isfinite(radial.hessian).all()
    assert np.max(np.abs(radial.hessian-center.hessian)) > 1e-5
    np.testing.assert_allclose(radial.hessian,radial.hessian.T,atol=1e-13)


def test_zero_mass_and_invalid_jacobian():
    p=dict(N=1,a=.8,n=1.16,alpha=.9,k=2.3,
           m2=0,Mg2=1,betas=(0.,1.,-.5,.24,0.),mu=-.4,r=.1)
    v=native_hr_scalar_jet(**p)
    assert np.max(abs(v.hessian))==0
    with pytest.raises(ValueError):
        native_hr_scalar_jet(**{**p,'mu':-1.})


@pytest.mark.parametrize('mu,r,sigma_r,sigma_dot,mu_dot',[
    (0.,0.,0.,0.,0.),
    (-.42,.11,-.72,.19,.13),
])
def test_independent_jax_second_derivative_of_exact_pullback(mu,r,sigma_r,sigma_dot,mu_dot):
    """Independent AD oracle: no shared second-order Taylor-jet arithmetic."""
    jax=pytest.importorskip('jax')
    import jax.numpy as jnp
    jax.config.update('jax_enable_x64', True)
    p=dict(N=1.,a=.8,n=1.16,alpha=.9,k=2.3,m2=.7,Mg2=1.3,
           betas=(.2,1.,-.5,.24,.31))
    Tt=1+0.5*sigma_dot*r*r; Tr=sigma_r*r
    Rt=mu_dot*r; Rr=1+mu
    jf=jnp.array([[Tt,Tr],[Rt,Rr]])
    def exact(x):
        Pg,Bg,sg,Eg,Pf,Bf,sf,Ef=x
        k=p['k'];k2=k*k
        N,a,n,alpha=p['N'],p['a'],p['n'],p['alpha']
        gn=jnp.array([[-N*N*(1+2*Pg),N*a*k*Bg],
                      [N*a*k*Bg,a*a*(1+2*sg-2*k2*Eg/3)]])
        fn=jnp.array([[-n*n*(1+2*Pf),n*alpha*k*Bf],
                      [n*alpha*k*Bf,alpha*alpha*(1+2*sf-2*k2*Ef/3)]])
        fc=jf.T@fn@jf
        angg=a*a*(1+2*sg+k2*Eg/3)
        angf=alpha*alpha*Rr*Rr*(1+2*sf+k2*Ef/3)
        A=jnp.linalg.solve(gn,fc)
        sd=jnp.sqrt(jnp.linalg.det(A))
        ts=jnp.sqrt(jnp.trace(A)+2*sd)
        ell=jnp.sqrt(angf/angg)
        es=jnp.array([1.,ts+2*ell,sd+2*ell*ts+ell*ell,
                      2*ell*sd+ell*ell*ts,ell*ell*sd])
        return -p['m2']*p['Mg2']*jnp.sqrt(-jnp.linalg.det(gn))*angg*jnp.dot(jnp.array(p['betas']),es)
    H_ref=np.asarray(jax.hessian(exact)(jnp.zeros(8)))
    H_new=native_hr_scalar_jet(**p,mu=mu,r=r,sigma_r=sigma_r,
                               sigma_dot=sigma_dot,mu_dot=mu_dot).hessian
    np.testing.assert_allclose(H_new,H_ref,rtol=3e-12,atol=3e-12)


def test_finite_radius_parity_separates_linear_shift_mixing_from_quadratic_even_block():
    """A pointwise radial Hessian is not a phase-averaged Fourier action."""
    p=dict(N=1,a=.8,n=1.16,alpha=.9,k=2.3,m2=.7,Mg2=1,
           betas=(0.,1.,-.5,.24,0.),mu=-.4,
           sigma_r=-.6,sigma_dot=.17,mu_dot=.14)
    center=native_hr_scalar_jet(**p,r=0).hessian
    aa=native_hr_scalar_jet(**p,r=.025).hessian
    bb=native_hr_scalar_jet(**p,r=.05).hessian
    no_shift=[0,2,3,4,6,7]; shifts=[1,5]
    ea=np.linalg.norm((aa-center)[np.ix_(no_shift,no_shift)])
    eb=np.linalg.norm((bb-center)[np.ix_(no_shift,no_shift)])
    oa=np.linalg.norm(aa[np.ix_(no_shift,shifts)])
    ob=np.linalg.norm(bb[np.ix_(no_shift,shifts)])
    assert 3.9 < eb/ea < 4.1
    assert 1.95 < ob/oa < 2.05

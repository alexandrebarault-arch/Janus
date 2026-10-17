"""Finite-mu native-HR Stueckelberg-Jacobian perturbation checks."""
import numpy as np
import pytest
from numerics.hr_native_quadratic_jet import native_hr_scalar_jet
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet

PARAM=dict(N=1.,a=.8,n=1.16,alpha=.9,k=2.3,m2=.7,Mg2=1.3,
           betas=(.2,1.,-.5,.24,.31),mu=-.42,r=.11,
           sigma_r=-.72,sigma_dot=.19,mu_dot=.13,
           n_dot=.34,alpha_dot=-.17,n_ddot=.25,alpha_ddot=-.08)


def test_metric_submatrix_matches_independently_tested_native_eight_field_jet():
    a=native_hr_stueckelberg_jet(**PARAM)
    b=native_hr_scalar_jet(**PARAM)
    assert a.hessian.shape==(14,14)
    np.testing.assert_allclose(a.hessian[:8,:8],b.hessian,rtol=4e-12,atol=4e-12)
    np.testing.assert_allclose(a.gradient[:8],b.gradient,rtol=4e-12,atol=4e-12)
    np.testing.assert_allclose(a.hessian,a.hessian.T,atol=1e-13)


def test_beta0_has_no_f_or_stueckelberg_columns():
    a=native_hr_stueckelberg_jet(**{**PARAM,'betas':(1,0,0,0,0)})
    assert np.max(abs(a.hessian[4:,:]))<1e-10
    assert np.max(abs(a.gradient[4:]))<1e-10


def test_beta4_is_pure_f_even_with_finite_stueckelberg_jacobian():
    a=native_hr_stueckelberg_jet(**{**PARAM,'betas':(0,0,0,0,1)})
    assert np.max(abs(a.hessian[:4,:]))<1e-10
    assert np.max(abs(a.gradient[:4]))<1e-10


def test_deltaT_without_any_background_rate_is_unobservable_as_constant_shift():
    p={**PARAM,'n_dot':0.,'alpha_dot':0.,'n_ddot':0.,'alpha_ddot':0.}
    a=native_hr_stueckelberg_jet(**p)
    # Column 8 is delta T, not delta T_t (column 9).
    assert np.max(abs(a.hessian[8,:]))<1e-11
    assert abs(a.gradient[8])<1e-11


def test_center_linearized_pullback_gradient_matches_native_f_perturbations():
    p={**PARAM,'r':0.,'mu':0.,'sigma_r':0.,'sigma_dot':0.,'mu_dot':0.,
       'n_dot':0.,'alpha_dot':0.,'n_ddot':0.,'alpha_ddot':0.}
    a=native_hr_stueckelberg_jet(**p)
    # delta(T_t) multiplies the f lapse exactly as Phi_f at first order.
    assert abs(a.gradient[9]-a.gradient[4])<5e-12
    # For a regular uniform radial dilation, delta R_r=delta R/r
    # has the same first-order effect as the isotropic f trace psi_f.
    assert abs(a.gradient[12]+a.gradient[13]-a.gradient[6])<5e-12


@pytest.mark.parametrize('mu,r',[(0.,0.),(-.42,.11)])
def test_independent_jax_hessian_for_metric_plus_six_stueckelberg_perturbations(mu,r):
    jax=pytest.importorskip('jax')
    import jax.numpy as jnp
    jax.config.update('jax_enable_x64',True)
    p={**PARAM,'mu':mu,'r':r}
    Tt=1+.5*p['sigma_dot']*r*r; Tr=p['sigma_r']*r
    Rt=p['mu_dot']*r; Rr=1+mu
    u0=.5*p['sigma_r']*r*r
    def exact(x):
        Pg,Bg,sg,Eg,Pf,Bf,sf,Ef,dT,dTt,dTr,dRt,dRr,dRratio=x
        u=u0+dT
        n=p['n']+p['n_dot']*u+.5*p['n_ddot']*u*u
        al=p['alpha']+p['alpha_dot']*u+.5*p['alpha_ddot']*u*u
        k=p['k'];k2=k*k;N=p['N'];a=p['a']
        gn=jnp.array([[-N*N*(1+2*Pg),N*a*k*Bg],
                      [N*a*k*Bg,a*a*(1+2*sg-2*k2*Eg/3)]])
        fn=jnp.array([[-n*n*(1+2*Pf),n*al*k*Bf],
                      [n*al*k*Bf,al*al*(1+2*sf-2*k2*Ef/3)]])
        J=jnp.array([[Tt+dTt,Tr+dTr],[Rt+dRt,Rr+dRr]])
        fc=J.T@fn@J
        gang=a*a*(1+2*sg+k2*Eg/3)
        fang=al*al*(Rr+dRratio)**2*(1+2*sf+k2*Ef/3)
        A=jnp.linalg.solve(gn,fc)
        ds=jnp.sqrt(jnp.linalg.det(A))
        ts=jnp.sqrt(jnp.trace(A)+2*ds)
        ell=jnp.sqrt(fang/gang)
        es=jnp.array([1.,ts+2*ell,ds+2*ell*ts+ell*ell,
                      2*ell*ds+ell*ell*ts,ell*ell*ds])
        return -p['m2']*p['Mg2']*jnp.sqrt(-jnp.linalg.det(gn))*gang*jnp.dot(jnp.array(p['betas']),es)
    ref=np.array(jax.hessian(exact)(jnp.zeros(14)))
    got=native_hr_stueckelberg_jet(**p).hessian
    np.testing.assert_allclose(got,ref,rtol=2e-11,atol=2e-11)

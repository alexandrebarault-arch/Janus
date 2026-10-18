"""PENDING actual GitHub-worktree full provider integration acceptance tests.

Unlike the local MOCK-backed structural tests, this imports the real HR and
both-dust action. Not executed in the focused local environment lacking
its prerequisites. Until run on a full worktree, treat as an OPEN gate.
"""
import numpy as np
import pytest
from numerics.hr_full_scalar_eh_two_dust_untilted import assemble_untilted_scalar_eh_hr_two_dust
from numerics.hr_two_dust_preconstraint import assemble_hr_two_dust_preconstraint
from numerics.hr_full_scalar_eh_homothetic import integrate_untilted_native_scalar_eh

HP=dict(N=1.03,a=.85,n=1.16,alpha=.74,k=2.2,m2=.7,Mg2=1.2,
        betas=(.31,1.,-.4,.2,.13),mu=-.24,sigma_r=0.,sigma_dot=0.,
        mu_dot=0.,n_dot=.09,alpha_dot=-.07,n_ddot=.025,alpha_ddot=-.02)

def test_real_full_scalar_eh_hr_dust_action_block_addition_and_momenta():
    kw=dict(radius=.23,quadrature_order=16,rho_g=.9,rho_f=.6,
            g_scale_rate=.04,planck_ratio=1.2,
            log_phidot_rate_g=.12,log_phidot_rate_f=-.17)
    joined=assemble_untilted_scalar_eh_hr_two_dust(**kw,**HP)
    old=assemble_hr_two_dust_preconstraint(radius=kw['radius'],
            quadrature_order=kw['quadrature_order'],rho_g=kw['rho_g'],
            rho_f=kw['rho_f'],log_phidot_rate_g=kw['log_phidot_rate_g'],
            log_phidot_rate_f=kw['log_phidot_rate_f'],**HP)
    eh=integrate_untilted_native_scalar_eh(radius=kw['radius'],
            quadrature_order=kw['quadrature_order'],k=HP['k'],
            N=HP['N'],a=HP['a'],a_rate=kw['g_scale_rate'],
            n=HP['n'],alpha=HP['alpha'],alpha_rate=HP['alpha_dot'],
            mu=HP['mu'],planck_ratio=kw['planck_ratio'])
    assert joined.hessian.shape==(24,24)
    np.testing.assert_allclose(joined.hessian[:22,:22],old.hessian+eh.hessian[:22,:22],
                               rtol=0,atol=2e-12)
    np.testing.assert_allclose(joined.hessian[22:,:],eh.hessian[22:,:],
                               rtol=0,atol=2e-12)
    np.testing.assert_allclose(joined.gradient[:22],old.gradient+eh.gradient[:22],
                               rtol=0,atol=2e-12)
    assert joined.hessian[17,20]==pytest.approx(old.hessian[17,20],abs=2e-13)
    assert joined.hessian[19,21]==pytest.approx(old.hessian[19,21],abs=2e-13)
    assert joined.hessian[19,10]==pytest.approx(-old.hessian[19,21],abs=2e-13)
    assert len(joined.amplitude_order)==24
    assert joined.amplitude_order[22:]==('psi_g_dot','E_g_dot')
    assert abs(joined.hessian[22,22])>1e-9
    assert abs(joined.hessian[23,23])>1e-9


def test_real_full_scalar_eh_hr_dust_planck_ratio_changes_only_eh_f():
    kw=dict(radius=.23,quadrature_order=16,rho_g=.9,rho_f=.6,g_scale_rate=.04)
    one=assemble_untilted_scalar_eh_hr_two_dust(**kw,planck_ratio=1.,**HP)
    two=assemble_untilted_scalar_eh_hr_two_dust(**kw,planck_ratio=2.,**HP)
    np.testing.assert_allclose(two.hr_hessian,one.hr_hessian,atol=0,rtol=0)
    np.testing.assert_allclose(two.dust_hessian,one.dust_hessian,atol=0,rtol=0)
    assert np.linalg.norm(two.eh_hessian-one.eh_hessian)>1e-8

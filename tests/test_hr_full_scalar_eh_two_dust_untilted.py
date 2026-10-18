"""Strict domain / interface structure tests. HR provider mocked LOCALLY."""
import sys
import types
from types import SimpleNamespace
import numpy as np
import pytest
from numerics.hr_full_scalar_eh_two_dust_untilted import assemble_untilted_scalar_eh_hr_two_dust

HP=dict(N=1.01,a=.9,n=1.07,alpha=.86,k=2.,m2=.5,Mg2=1.,
       betas=(.2,1.,-.2,.12,.03),mu=-.19,mu_dot=0.,sigma_r=0.,
       sigma_dot=0.,alpha_dot=.08)

def test_full_scalar_eh_assembly_requires_identity_time_chart():
    kw=dict(radius=.3,rho_g=.8,rho_f=.7,g_scale_rate=.06)
    for name in ('sigma_r','sigma_dot','mu_dot'):
        with pytest.raises(ValueError):
            assemble_untilted_scalar_eh_hr_two_dust(**kw,**dict(HP,**{name:.05}))

def test_preconstraint_two_dust_hr_block_preserved_on_24_slot_assembly(monkeypatch):
    # The complete two-dust dependency is verified by its OWN original suite;
    # this strictly local test controls index and block addition, not physical HR.
    fake=types.ModuleType('numerics.hr_two_dust_preconstraint')
    fake.PRECONSTRAINT_ORDER=tuple(f'a{i}' for i in range(22))
    def factory(**params):
        H=np.zeros((22,22));Hint=np.zeros((22,22));Hd=np.zeros((22,22))
        Hint[0,0]=3.;Hd[17,20]=Hd[20,17]=2.;Hd[19,21]=Hd[21,19]=4.
        H=Hint+Hd
        return SimpleNamespace(hessian=H,interaction_hessian=Hint,dust_hessian=Hd,
                               gradient=np.zeros(22))
    fake.assemble_hr_two_dust_preconstraint=factory
    monkeypatch.setitem(sys.modules,'numerics.hr_two_dust_preconstraint',fake)
    out=assemble_untilted_scalar_eh_hr_two_dust(radius=.3,quadrature_order=16,
         rho_g=.8,rho_f=.7,g_scale_rate=.06,**HP)
    assert out.hessian.shape==(24,24)
    assert len(out.amplitude_order)==24
    assert out.amplitude_order[-2:]==('psi_g_dot','E_g_dot')
    assert out.hessian[17,20]==2. and out.hessian[19,21]==4.
    assert out.hessian[0,0]==pytest.approx(3.+out.eh_hessian[0,0])
    assert abs(out.hessian[22,22])>1e-8 and abs(out.hessian[23,23])>1e-8
    np.testing.assert_allclose(out.hessian,out.eh_hessian+out.hr_hessian+out.dust_hessian,
                               rtol=0,atol=1e-11)

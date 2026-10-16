import numpy as np


def _vf_vg_time(beta1,beta2,beta3,t,x):
    vg = 3.0*beta1*x + 3.0*beta2*x*x + beta3*x**3
    xi = 1.0/x
    vf = 3.0*beta3*xi + 3.0*beta2*xi*xi + beta1*xi**3
    return vg, vf


def test_finite_mu_lapse_tadpoles_match_independent_diagonal_hr_sources():
    from numerics.nonhomothetic_hr_relative_native import relative_native_hr_correction_density
    beta1,beta2,beta3 = 1.0,-1.7,0.8
    K=0.63; mu=-0.31; r=0.8
    betas=(0.0,beta1,beta2,beta3,0.0)
    common=dict(a=1.0,n=K,alpha=K,r=r,mu=mu,mu_dot=0.0,s=0.0,s_dot=0.0,
                betas=betas,m2=1.0,Mg2=1.0)
    h=1e-6
    def derivative(name):
        plus=dict(common); minus=dict(common)
        plus[name]=h; minus[name]=-h
        return (
            relative_native_hr_correction_density(**plus)
            - relative_native_hr_correction_density(**minus)
        )/(2.0*h)

    vg0,vf0=_vf_vg_time(beta1,beta2,beta3,K,K)
    vgm,vfm=_vf_vg_time(beta1,beta2,beta3,K,K*(1.0+mu))
    expected_g=r*r*(vgm-vg0)
    expected_f=r*r*K**4*((1.0+mu)**3*vfm-vf0)
    assert np.isclose(derivative('Phi_g'),expected_g,rtol=2e-9,atol=2e-10)
    assert np.isclose(derivative('Phi_f'),expected_f,rtol=2e-9,atol=2e-10)

import math
import numpy as np


def test_native_radial_density_matches_de_felice_fourier_phase_block_locally():
    from numerics.spherical_flat_dust_phase_action import flat_spherical_dust_phase_density
    from numerics.de_felice_dust_phase_action import dust_phase_density
    a=1.7; n=0.83; r=0.91; rho=2.4; phi=-0.07
    q=0.13; qdot=-0.21; p=0.44; k=3.2; B=-0.05
    U=k*B; qr=k*q
    out=flat_spherical_dust_phase_density(
        scale_factor=a,lapse=n,r=r,rho=rho,Phi=phi,shift=U,
        q=q,q_t=qdot,q_r=qr,momentum=p,log_phidot_rate=0.0)
    local=p*qdot+dust_phase_density(
        rho=rho,lapse=n,scale_factor=a,k=k,Phi=phi,B=B,
        psi=0.0,E=0.0,q=q,momentum=p)
    expected=n*a**3*r**2*local
    assert math.isclose(out,expected,rel_tol=0,abs_tol=2e-14)


def test_log_phidot_drift_enters_only_as_measure_times_p_rate_q():
    from numerics.spherical_flat_dust_phase_action import flat_spherical_dust_phase_density
    common=dict(scale_factor=0.9,lapse=1.3,r=0.7,rho=1.8,Phi=0.02,shift=-0.08,
                q=0.12,q_t=-0.04,q_r=0.3,momentum=-0.6)
    rphi=0.17
    a=flat_spherical_dust_phase_density(log_phidot_rate=rphi,**common)
    b=flat_spherical_dust_phase_density(log_phidot_rate=0.0,**common)
    expected=common['lapse']*common['scale_factor']**3*common['r']**2*common['momentum']*rphi*common['q']
    assert math.isclose(a-b,expected,rel_tol=0,abs_tol=2e-14)


def test_pulled_back_density_uses_covector_gradient_and_measure_jacobian():
    from numerics.spherical_flat_dust_phase_action import (
        flat_spherical_dust_phase_density,pulled_back_flat_spherical_dust_phase_density)
    J=np.array([[1.1,0.2],[-0.15,0.85]])
    qt,qr=0.31,-0.27
    native=np.linalg.solve(J.T,np.array([qt,qr]))
    common=dict(scale_factor=1.2,lapse=0.95,native_r=0.8,rho=2.1,Phi=-0.03,shift=0.06,
                q=0.11,q_t_common=qt,q_r_common=qr,momentum=0.7,log_phidot_rate=-0.09,jacobian=J)
    out=pulled_back_flat_spherical_dust_phase_density(**common)
    direct=flat_spherical_dust_phase_density(
        scale_factor=1.2,lapse=0.95,r=0.8,rho=2.1,Phi=-0.03,shift=0.06,
        q=0.11,q_t=native[0],q_r=native[1],momentum=0.7,log_phidot_rate=-0.09)
    assert math.isclose(out,abs(np.linalg.det(J))*direct,rel_tol=0,abs_tol=2e-14)


def test_f_sector_common_normalization_matches_production_two_dust_formula():
    from numerics.spherical_flat_dust_phase_action import flat_spherical_dust_phase_density
    from numerics.de_felice_dust_phase_action import dust_phase_density
    a_g=1.6; xi=0.72; alpha=a_g*xi; n=0.88; r=0.77
    rho=1.9; phi=0.035; q=-0.14; qdot=0.09; k=2.7; B=0.04
    p_common=0.63; ndot_over_n=-0.11
    pref=n*xi**3
    p_local=p_common/pref
    native=flat_spherical_dust_phase_density(
        scale_factor=alpha,lapse=n,r=r,rho=rho,Phi=phi,shift=k*B,
        q=q,q_t=qdot,q_r=k*q,momentum=p_local,log_phidot_rate=ndot_over_n)
    common_normalized=native/(a_g**3*r**2)
    expected=(
        p_common*qdot+p_common*ndot_over_n*q
        +pref*dust_phase_density(rho=rho,lapse=n,scale_factor=alpha,k=k,
            Phi=phi,B=B,psi=0.0,E=0.0,q=q,momentum=p_local)
    )
    assert math.isclose(common_normalized,expected,rel_tol=0,abs_tol=3e-14)

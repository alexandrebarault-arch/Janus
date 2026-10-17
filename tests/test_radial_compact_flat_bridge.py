import numpy as np


def test_radial_compact_eh_lapse_shift_hessian_matches_de_felice_at_keff():
    from numerics.radial_compact_flat_bridge import radial_compact_profile_data, radial_compact_eh_lapse_shift_hessian
    from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
    N=0.91; a=1.37; H=-0.12; R=0.8
    prof=radial_compact_profile_data(R=R,order=80)
    got=radial_compact_eh_lapse_shift_hessian(lapse=N,scale_factor=a,H=H,R=R,order=80,amplitude_step=1e-3)
    k=np.sqrt(prof.k2_eff)
    def L(x):
        phi,B=x
        dens=eh_scalar_quadratic_density_flat(lapse=N,scale_factor=a,H=H,Hdot_over_lapse=0.0,k=k,
            Phi=phi,B=B,psi=0.0,E=0.0,psi_dot=0.0,E_dot=0.0)
        return 0.5*N*a**3*prof.norm*dens
    e=np.eye(2); expected=np.zeros((2,2))
    expected[0,0]=2*L(e[0]); expected[1,1]=2*L(e[1])
    expected[0,1]=expected[1,0]=(L(e[0]+e[1])-L(e[0]-e[1])-L(-e[0]+e[1])+L(-e[0]-e[1]))/4
    assert np.allclose(got,expected,rtol=3e-7,atol=2e-9)


def test_radial_profile_keff_scales_as_inverse_radius_squared():
    from numerics.radial_compact_flat_bridge import radial_compact_profile_data
    a=radial_compact_profile_data(R=0.7,order=80)
    b=radial_compact_profile_data(R=1.4,order=80)
    assert np.isclose(a.k2_eff/b.k2_eff,4.0,rtol=2e-12,atol=0)


def test_radial_compact_dust_phase_matches_fourier_at_keff_with_independent_rate():
    from numerics.radial_compact_flat_bridge import radial_compact_profile_data, radial_compact_dust_phase_value
    from numerics.de_felice_dust_phase_action import dust_phase_density
    N=.84; a=1.22; R=.9; rho=2.3; Phi=-.04; B=.035
    q=.17; qdot=-.13; p=.52; drift=-.09
    prof=radial_compact_profile_data(R=R,order=90); k=np.sqrt(prof.k2_eff)
    got=radial_compact_dust_phase_value(lapse=N,scale_factor=a,R=R,rho=rho,
        Phi=Phi,B=B,q=q,q_rate=qdot,momentum=p,log_phidot_rate=drift,order=90)
    expected=N*a**3*prof.norm*(p*qdot+p*drift*q+dust_phase_density(
        rho=rho,lapse=N,scale_factor=a,k=k,Phi=Phi,B=B,psi=0,E=0,q=q,momentum=p))
    assert np.isclose(got,expected,rtol=2e-13,atol=2e-14)

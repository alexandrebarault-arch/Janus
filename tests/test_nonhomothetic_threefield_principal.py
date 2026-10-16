import numpy as np


def test_decoupled_compact_principal_fit_recovers_both_matter_speeds_and_null_pi():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    from numerics.nonhomothetic_threefield_principal import fit_threefield_principal_matrices
    jet=from_log_derivatives(a=1.0,Hc=0.0,Hc_N=0.0,xi=1.4,xi_N=0.0,xi_NN=0.0,c=0.8,c_N=0.0)
    out=fit_threefield_principal_matrices(
        betas=(0,1,-.7,.4,-.2),jet=jet,
        time_scales=(.18,.23,.29),radial_scales=(.30,.39,.50),
        interaction_mass2=0.0,planck_ratio=.7,rho_g=1.6,rho_f=1.1,
        cs2_g=.2,cs2_f=.3,amplitude_step=1e-4,quadrature_order=12)
    assert np.linalg.norm(out.kinetic[0]) < 2e-7
    assert np.linalg.norm(out.gradient[0]) < 2e-7
    speeds=np.sort(out.nonnull_squared_speeds)
    assert speeds.shape==(2,)
    assert np.allclose(speeds,np.sort([.2,.8**2*.3]),rtol=3e-3,atol=3e-4)
    assert out.fit_relative_residual < 5e-3

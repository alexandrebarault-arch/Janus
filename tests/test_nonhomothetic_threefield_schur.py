import numpy as np


def test_threefield_assembly_keeps_matter_coordinates_before_metric_schur():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    from numerics.nonhomothetic_threefield_schur import reduce_nonhomothetic_threefield_metric_block
    jet=from_log_derivatives(a=.03,Hc=3.2,Hc_N=-1.5,xi=1.9,xi_N=-1.4,xi_NN=1.2,c=.25,c_N=.08)
    out=reduce_nonhomothetic_threefield_metric_block(
        betas=(0,1,-4,12,-30),jet=jet,time_radius=.0015,radial_radius=.004,
        interaction_mass2=2.0,planck_ratio=.012,rho_g=10.,rho_f=4.,
        cs2_g=.2,cs2_f=.3,amplitude_step=2e-5,quadrature_order=12)
    assert out.reduced_physical_hessian.shape == (3,3)
    assert np.allclose(out.reduced_physical_hessian,out.reduced_physical_hessian.T,rtol=0,atol=1e-12)
    assert np.all(np.isfinite(out.reduced_physical_hessian))
    assert out.metric_rank == 4

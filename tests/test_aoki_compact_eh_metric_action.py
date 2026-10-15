import numpy as np


def test_minkowski_compact_scalar_eh_hessian_has_constraint_structure():
    from numerics.aoki_compact_eh_metric_action import compact_eh_metric_hessian
    H = compact_eh_metric_hessian(
        hubble=0.0, w=0.0, T=1.0, R=1.0,
        amplitude_step=4e-4, quadrature_order=32,
    )
    assert H.shape == (2, 2)
    assert np.allclose(H, H.T, rtol=0.0, atol=1e-12)
    scale=max(1.0, np.max(np.abs(H)))
    assert abs(H[0,0]) < 5e-6*scale
    assert np.isclose(H[1,1], 2.0*H[0,1], rtol=2e-4, atol=2e-7)


def test_compact_eh_hessian_is_stable_under_step_refinement():
    from numerics.aoki_compact_eh_metric_action import compact_eh_metric_hessian
    H1=compact_eh_metric_hessian(hubble=0.03,w=0.0,T=1.0,R=1.0,amplitude_step=8e-4,quadrature_order=32)
    H2=compact_eh_metric_hessian(hubble=0.03,w=0.0,T=1.0,R=1.0,amplitude_step=4e-4,quadrature_order=32)
    assert np.all(np.isfinite(H1)) and np.all(np.isfinite(H2))
    assert np.linalg.norm(H1-H2) < 2e-3*max(1.0,np.linalg.norm(H2))

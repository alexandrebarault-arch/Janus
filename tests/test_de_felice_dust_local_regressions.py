import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_dust_dae_generator_preserves_differentiated_algebraic_constraint():
    from numerics.de_felice_dust_local_modes import dust_dae_local_system
    rng = np.random.default_rng(1234)
    # Build a symmetric physical phase Hessian in order (Y[3],p[2],Ydot[3]).
    M = np.array([
        [4.0,.2,-.1,.3,-.2], [.2,3.0,.1,-.1,.25], [-.1,.1,2.5,.15,.05],
        [.3,-.1,.15,1.7,.12], [-.2,.25,.05,.12,1.3],
    ])
    C = np.array([
        [.2,-.1,.05], [.1,.3,-.07], [-.04,.02,.25],
        [1.0,.1,-.2], [.05,.8,.15],
    ])
    K = np.array([[2.0,.1,0.0],[.1,1.6,.05],[0.0,.05,1.2]])
    H = np.block([[M,C],[C.T,K]])
    Md = rng.normal(scale=.03,size=(5,5)); Md=.5*(Md+Md.T)
    Cd = rng.normal(scale=.02,size=(5,3))
    Kd = rng.normal(scale=.03,size=(3,3)); Kd=.5*(Kd+Kd.T)
    HN = np.block([[Md,Cd],[Cd.T,Kd]])
    Hg = .7
    out = dust_dae_local_system(H, HN, H_g=Hg)
    w = np.array([.2,-.1,.07,.03,-.04,.02])
    Y, V = w[:3], w[3:]
    p = out.momentum_map @ w
    wdot = out.generator_cosmic @ w
    Vdot = wdot[3:]
    pdot = out.momentum_rate_map @ w
    # d/dt(Mpy Y + Mpp p + Cp V)=0 by construction.
    Hd = Hg * HN
    M0, C0 = H[:5,:5], H[:5,5:8]
    Mdot, Cdot = Hd[:5,:5], Hd[:5,5:8]
    residual = (
        Mdot[3:5,:3]@Y + M0[3:5,:3]@V
        + Mdot[3:5,3:5]@p + M0[3:5,3:5]@pdot
        + Cdot[3:5]@V + C0[3:5]@Vdot
    )
    assert np.linalg.norm(residual, ord=np.inf) < 2e-12


def test_candidate_dust_local_dae_recovers_principal_gravity_and_zero_sound_dust():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.de_felice_action_principal import gravity_principal_action
    from numerics.de_felice_dust_local_modes import candidate_c_dust_local_squared_speeds
    a = 0.5
    kh = 0.2  # k/H0 ~= 600: high-k but still inside the production scale set.
    point = candidate_c_dust_background_point(a, k_hmpc=kh)
    target = gravity_principal_action(
        point.metric, rho_f_plus_p_f=point.rho_f_m,
    ).cs2
    speeds = candidate_c_dust_local_squared_speeds(
        a, k_hmpc=kh, action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    )
    # Two pressureless branches have vanishing principal sound speed; the
    # gravity branch must agree at the ~0.2% double-precision derivative floor.
    assert speeds.shape == (3,)
    assert max(abs(speeds[0]), abs(speeds[1])) < 4e-4
    assert math.isclose(speeds[2], target, rel_tol=2e-3, abs_tol=2e-5)


def test_dust_dae_accepts_structural_pdot_rows_but_rejects_nonzero_pdot_dynamics():
    from numerics.de_felice_dust_local_modes import dust_dae_local_system
    M = np.diag([4.0, 3.0, 2.0, 1.7, 1.3])
    C = np.array([
        [.2,-.1,.05], [.1,.3,-.07], [-.04,.02,.25],
        [1.0,.1,-.2], [.05,.8,.15],
    ])
    K = np.diag([2.0, 1.6, 1.2])
    H8 = np.block([[M,C],[C.T,K]])
    HN8 = 0.03 * H8
    # Production DustCanonicalAction keeps two structural pdot rows/columns.
    active = [0,1,2,3,4,5,6,7]
    H10 = np.zeros((10,10), dtype=float)
    HN10 = np.zeros((10,10), dtype=float)
    H10[np.ix_(active,active)] = H8
    HN10[np.ix_(active,active)] = HN8
    ref = dust_dae_local_system(H8, HN8, H_g=.7)
    padded = dust_dae_local_system(H10, HN10, H_g=.7)
    assert np.allclose(padded.generator_cosmic, ref.generator_cosmic, rtol=0, atol=1e-14)
    assert np.allclose(padded.momentum_map, ref.momentum_map, rtol=0, atol=1e-14)

    bad = H10.copy()
    bad[8,0] = bad[0,8] = 1e-3
    with np.testing.assert_raises_regex(np.linalg.LinAlgError, "pdot"):
        dust_dae_local_system(bad, HN10, H_g=.7)


def test_candidate_dust_local_gravity_branch_converges_at_late_start():
    from numerics.candidate_c_dust_background import candidate_c_dust_linear_start
    from numerics.de_felice_dust_local_modes import candidate_c_dust_local_squared_speeds
    a = candidate_c_dust_linear_start()
    coarse = candidate_c_dust_local_squared_speeds(
        a, k_hmpc=0.2, action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    )
    fine = candidate_c_dust_local_squared_speeds(
        a, k_hmpc=0.2, action_derivative_step_N=1e-3,
        trajectory_derivative_step_N=1e-3,
    )
    assert math.isclose(coarse[2], fine[2], rel_tol=1e-2, abs_tol=2e-4)

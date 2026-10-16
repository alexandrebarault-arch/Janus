import math


def test_flat_gauge_stueckelberg_bridge_inverts_metric_relations():
    from numerics.nonhomothetic_linear_stueckelberg_bridge import flat_gauge_to_relative_stueckelberg
    A = 0.5920714865071928
    A_dot = -0.041
    k = 37.0
    psi = -0.23
    E = 0.004
    psi_dot = 0.17
    E_dot = -0.006
    out = flat_gauge_to_relative_stueckelberg(
        psi_f=psi, E_f=E, psi_f_dot=psi_dot, E_f_dot=E_dot,
        k=k, inv_nHf=A, inv_nHf_dot=A_dot,
    )
    C = k*k/6.0
    assert math.isclose(out.L, -0.5*E, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(out.L_dot, -0.5*E_dot, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(out.T, -A*(psi+C*E), rel_tol=0.0, abs_tol=1e-15)
    expected = -(A_dot*(psi+C*E) + A*(psi_dot+C*E_dot))
    assert math.isclose(out.T_dot, expected, rel_tol=0.0, abs_tol=1e-15)


def test_pure_stueckelberg_matter_variable_matches_eq72():
    from numerics.nonhomothetic_linear_stueckelberg_bridge import pure_stueckelberg_qf
    A = 0.4
    psi = 0.2
    E = -0.03
    k = 5.0
    T = -A*(psi+k*k*E/6.0)
    assert math.isclose(
        pure_stueckelberg_qf(psi_f=psi, E_f=E, k=k, inv_nHf=A),
        -T, rel_tol=0.0, abs_tol=1e-15,
    )


def test_induced_f_auxiliaries_follow_native_background_lie_derivative():
    from numerics.nonhomothetic_linear_stueckelberg_bridge import induced_f_auxiliaries
    out = induced_f_auxiliaries(
        T=0.12, T_dot=-0.08, L_dot=0.03,
        n=0.7, alpha=0.9, n_dot_over_n=0.05,
    )
    assert math.isclose(out.Phi_f, -(-0.08+0.05*0.12), rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(out.B_f, (0.7/0.9)*0.12-(0.9/0.7)*0.03, rel_tol=0.0, abs_tol=1e-15)

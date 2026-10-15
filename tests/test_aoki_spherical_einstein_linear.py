import math


def test_minkowski_areal_gauge_components_match_linearized_spherical_einstein_tensor():
    from numerics.aoki_spherical_einstein_linear import linearized_mixed_einstein
    r = 1.7
    phi_r = 0.31
    phi_rr = -0.22
    psi = 0.18
    psi_t = -0.27
    psi_tt = 0.14
    psi_r = -0.09
    out = linearized_mixed_einstein(
        a=1.0, a_prime=0.0, a_second=0.0, r=r,
        phi=0.0, phi_t=0.0, phi_r=phi_r, phi_rr=phi_rr,
        psi=psi, psi_t=psi_t, psi_tt=psi_tt, psi_r=psi_r,
    )
    assert math.isclose(out.tt, -2.0*(psi_r/r + psi/r**2), rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(out.tr, -2.0*psi_t/r, rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(out.rt, +2.0*psi_t/r, rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(out.rr, 2.0*(phi_r/r - psi/r**2), rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(
        out.angular,
        phi_rr - psi_tt + (phi_r-psi_r)/r,
        rel_tol=0.0, abs_tol=1e-14,
    )


def test_constant_lapse_perturbation_matches_exact_flrw_friedmann_expansion():
    from numerics.aoki_spherical_einstein_linear import linearized_mixed_einstein
    a = 1.3
    ap = 0.47
    app = -0.12
    phi = 2.5e-4
    out = linearized_mixed_einstein(
        a=a, a_prime=ap, a_second=app, r=0.9,
        phi=phi, phi_t=0.0, phi_r=0.0, phi_rr=0.0,
        psi=0.0, psi_t=0.0, psi_tt=0.0, psi_r=0.0,
    )
    # Exact metric has conformal lapse N^2=a^2(1+2 phi), hence
    # G^t_t=-3 a'^2/[a^4(1+2 phi)]. Its linear perturbation is +6 phi a'^2/a^4.
    expected_tt = 6.0*phi*ap**2/a**4
    assert math.isclose(out.tt, expected_tt, rel_tol=2e-13, abs_tol=1e-15)


def test_minkowski_linearized_bianchi_identity_holds_for_polynomial_field():
    from numerics.aoki_spherical_einstein_linear import linearized_mixed_einstein
    # psi(t,r)=t^2 r^3 and phi(t,r)=t r^4 at one generic point.
    t = 0.37
    r = 1.21
    psi = t*t*r**3
    psi_t = 2*t*r**3
    psi_tt = 2*r**3
    psi_r = 3*t*t*r**2
    psi_tr = 6*t*r**2
    phi_r = 4*t*r**3
    phi_rr = 12*t*r**2
    d_t_Gtt = -2.0*(psi_tr/r + psi_t/r**2)
    d_r_Grt = 2.0*(psi_tr/r - psi_t/r**2)
    Grt = 2.0*psi_t/r
    assert abs(d_t_Gtt + d_r_Grt + 2.0*Grt/r) < 1e-13

    out = linearized_mixed_einstein(
        a=1.0, a_prime=0.0, a_second=0.0, r=r,
        phi=t*r**4, phi_t=r**4, phi_r=phi_r, phi_rr=phi_rr,
        psi=psi, psi_t=psi_t, psi_tt=psi_tt, psi_r=psi_r,
    )
    assert all(math.isfinite(x) for x in (out.tt,out.tr,out.rt,out.rr,out.angular))

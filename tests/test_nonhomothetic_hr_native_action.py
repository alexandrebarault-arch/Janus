import math
import numpy as np


def test_native_hr_density_matches_diagonal_analytic_eigenvalues():
    from numerics.nonhomothetic_hr_native_action import native_hr_potential_density
    a = 1.3
    r = 0.7
    temporal = 0.81
    spatial = 1.22
    betas = (0.2, 1.1, -0.4, 0.8, 0.3)
    g = np.diag([-a*a, a*a])
    f = np.diag([-(a*temporal)**2, (a*spatial)**2])
    out = native_hr_potential_density(
        g_radial_native=g, f_radial_native=f,
        g_angular_native=a*a*r*r,
        f_angular_native=(a*spatial)**2*r*r,
        jacobian_g=np.eye(2), jacobian_f=np.eye(2),
        betas=betas, m2=0.7, Mg2=1.4,
    )
    e = (
        1.0,
        temporal + 3.0*spatial,
        3.0*temporal*spatial + 3.0*spatial**2,
        3.0*temporal*spatial**2 + spatial**3,
        temporal*spatial**3,
    )
    expected = 0.7*1.4*a**4*r*r*sum(b*q for b, q in zip(betas, e))
    assert math.isclose(out, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_native_hr_density_carries_common_chart_jacobian():
    from numerics.nonhomothetic_hr_native_action import native_hr_potential_density
    g = np.diag([-1.0, 1.0])
    f = np.diag([-0.8**2, 1.2**2])
    kwargs = dict(
        g_radial_native=g, f_radial_native=f,
        g_angular_native=1.0, f_angular_native=1.2**2,
        betas=(0.0, 1.0, -0.2, 0.3, 0.0), m2=1.0, Mg2=1.0,
    )
    base = native_hr_potential_density(
        jacobian_g=np.eye(2), jacobian_f=np.eye(2), **kwargs,
    )
    P = np.array([[1.1, 0.08], [-0.04, 0.93]])
    transformed = native_hr_potential_density(
        jacobian_g=P, jacobian_f=P, **kwargs,
    )
    assert math.isclose(
        transformed, abs(np.linalg.det(P))*base,
        rel_tol=3e-14, abs_tol=3e-14,
    )


def test_native_hr_density_matches_existing_weak_nonhomothetic_pullback():
    from numerics.nonhomothetic_hr_native_action import native_hr_potential_density
    from numerics.nonhomothetic_hr_weak_spherical import standard_beta_potential_reduced_density

    a = 0.83
    b = 1.14
    c = 0.72
    r = 0.61
    Phi_g, Psi_g = 0.012, -0.008
    Phi_f, Psi_f = -0.006, 0.011
    sigma_dot, sigma_prime = 0.031, -0.024
    mu, mu_dot, mu_prime = -0.27, 0.018, -0.013
    betas = (0.15, 1.0, -0.7, 0.45, -0.2)
    m2 = 0.37
    Mg2 = 1.6

    # Historical helper is reduced by r^2 sin(theta); the generic native
    # density below is reduced only by sin(theta), so compare actual/r^2.
    expected = standard_beta_potential_reduced_density(
        a=a, b=b, c_background=c, r=r,
        betas=betas, m2=m2, Mg2=Mg2,
        Phi_g=Phi_g, Psi_g=Psi_g,
        Phi_f=Phi_f, Psi_f=Psi_f,
        sigma_dot=sigma_dot, sigma_prime=sigma_prime,
        mu=mu, mu_dot=mu_dot, mu_prime=mu_prime,
    )

    g_native = a*a*np.diag([
        -(1.0 + 2.0*Phi_g),
        1.0 - 2.0*Psi_g,
    ])
    f_native = b*b*np.diag([
        -(1.0 + 2.0*Phi_f),
        1.0 - 2.0*Psi_f,
    ])
    Jf = np.array([
        [c + sigma_dot, sigma_prime],
        [r*mu_dot, 1.0 + mu + r*mu_prime],
    ])
    actual = native_hr_potential_density(
        g_radial_native=g_native,
        f_radial_native=f_native,
        g_angular_native=a*a*(1.0 - 2.0*Psi_g)*r*r,
        f_angular_native=b*b*(1.0 - 2.0*Psi_f)*(1.0 + mu)**2*r*r,
        jacobian_g=np.eye(2), jacobian_f=Jf,
        betas=betas, m2=m2, Mg2=Mg2,
    )
    assert math.isclose(actual/(r*r), expected, rel_tol=3e-13, abs_tol=3e-13)

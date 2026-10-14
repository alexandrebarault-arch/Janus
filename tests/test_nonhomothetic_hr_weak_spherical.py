import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_zero_weak_potentials_reduce_to_exact_radial_square_root():
    from numerics.nonhomothetic_hr_weak_spherical import weak_square_root_invariants

    inv = weak_square_root_invariants(
        a=0.9, b=1.1, c_background=0.6, r=0.7,
        Phi_g=0.0, Psi_g=0.0, Phi_f=0.0, Psi_f=0.0,
        sigma_dot=0.03, sigma_prime=-0.04,
        mu=0.2, mu_dot=0.05, mu_prime=-0.02,
    )
    assert np.allclose(
        inv.radial_square_root @ inv.radial_square_root,
        inv.radial_g_inverse_f,
        rtol=2.0e-13, atol=2.0e-13,
    )


def test_background_weak_potentials_give_expected_diagonal_eigenvalues():
    from numerics.nonhomothetic_hr_weak_spherical import weak_square_root_invariants

    a, b, c = 0.8, 1.12, 0.47
    Phi_g, Psi_g, Phi_f, Psi_f = 0.03, -0.02, -0.01, 0.04
    inv = weak_square_root_invariants(
        a=a, b=b, c_background=c, r=1.3,
        Phi_g=Phi_g, Psi_g=Psi_g, Phi_f=Phi_f, Psi_f=Psi_f,
        sigma_dot=0.0, sigma_prime=0.0,
        mu=0.0, mu_dot=0.0, mu_prime=0.0,
    )
    lambda_t = (b/a)*c*np.sqrt((1.0 + 2.0*Phi_f)/(1.0 + 2.0*Phi_g))
    lambda_s = (b/a)*np.sqrt((1.0 - 2.0*Psi_f)/(1.0 - 2.0*Psi_g))
    eig = [lambda_t, lambda_s, lambda_s, lambda_s]
    expected = np.array([
        1.0,
        sum(eig),
        sum(eig[i]*eig[j] for i in range(4) for j in range(i + 1, 4)),
        sum(eig[i]*eig[j]*eig[k]
            for i in range(4) for j in range(i + 1, 4)
            for k in range(j + 1, 4)),
        np.prod(eig),
    ])
    assert np.allclose(inv.elementary_symmetric, expected, rtol=2e-13, atol=2e-13)


def test_standard_beta_potential_background_matches_direct_eigenvalue_sum():
    from numerics.nonhomothetic_hr_weak_spherical import standard_beta_potential_reduced_density

    a, b, c = 0.75, 1.05, 0.52
    betas = (0.2, 1.1, -0.4, 0.3, -0.2)
    got = standard_beta_potential_reduced_density(
        a=a, b=b, c_background=c, r=1.0,
        betas=betas, m2=2.3, Mg2=1.7,
        Phi_g=0.0, Psi_g=0.0, Phi_f=0.0, Psi_f=0.0,
        sigma_dot=0.0, sigma_prime=0.0,
        mu=0.0, mu_dot=0.0, mu_prime=0.0,
    )
    x = b/a
    eig = [x*c, x, x, x]
    es = [
        1.0,
        sum(eig),
        sum(eig[i]*eig[j] for i in range(4) for j in range(i + 1, 4)),
        sum(eig[i]*eig[j]*eig[k]
            for i in range(4) for j in range(i + 1, 4)
            for k in range(j + 1, 4)),
        np.prod(eig),
    ]
    expected = 2.3*1.7*a**4*sum(beta*e for beta, e in zip(betas, es))
    assert abs(got - expected) < 2.0e-12


def test_homothetic_g_lapse_source_reproduces_aoki_mass_polynomial():
    from numerics.nonhomothetic_hr_weak_spherical import standard_beta_potential_reduced_density

    a = 0.83
    K = 1.21
    mu = 0.37
    m2 = 1.7
    Mg2 = 1.4
    betas = (0.2, 0.9, -0.35, 0.18, -0.11)
    b = a*K
    h = 2.0e-6

    def potential(Phi_g: float, u: float) -> float:
        return standard_beta_potential_reduced_density(
            a=a, b=b, c_background=1.0, r=1.0,
            betas=betas, m2=m2, Mg2=Mg2,
            Phi_g=Phi_g, Psi_g=0.0, Phi_f=0.0, Psi_f=0.0,
            sigma_dot=0.0, sigma_prime=0.0,
            mu=u, mu_dot=0.0, mu_prime=0.0,
        )

    def lapse_derivative(u: float) -> float:
        return (potential(h, u) - potential(-h, u))/(2.0*h)

    measured = lapse_derivative(mu) - lapse_derivative(0.0)
    _, beta1_raw, beta2_raw, beta3_raw, _ = betas
    denominator = beta1_raw + 2.0*K*beta2_raw + K*K*beta3_raw
    beta2_aoki = (K*beta2_raw + K*K*beta3_raw)/denominator
    beta3_aoki = K*K*beta3_raw/denominator
    expected = (
        m2*Mg2*a**4*3.0*K*denominator
        * (mu + beta2_aoki*mu**2 + (beta3_aoki/3.0)*mu**3)
    )
    assert abs(measured - expected) <= 2.0e-8*max(1.0, abs(expected))


def test_homothetic_radial_source_combines_with_lapse_to_aoki_phi_polynomial():
    from numerics.nonhomothetic_hr_weak_spherical import static_anisotropic_standard_beta_potential

    a = 0.83
    K = 1.21
    mu = 0.37
    m2 = 1.7
    Mg2 = 1.4
    betas = (0.2, 0.9, -0.35, 0.18, -0.11)
    b = a*K
    h = 2.0e-6

    def potential(Phi_g: float, Psi_g_radial: float, u: float) -> float:
        return static_anisotropic_standard_beta_potential(
            a=a, b=b, c_background=1.0,
            betas=betas, m2=m2, Mg2=Mg2,
            Phi_g=Phi_g,
            Psi_g_radial=Psi_g_radial,
            Psi_g_angular=0.0,
            Phi_f=0.0,
            Psi_f_radial=0.0,
            Psi_f_angular=0.0,
            mu=u,
        )

    def lapse_derivative(u: float) -> float:
        return (potential(h, 0.0, u) - potential(-h, 0.0, u))/(2.0*h)

    def radial_derivative(u: float) -> float:
        return (potential(0.0, h, u) - potential(0.0, -h, u))/(2.0*h)

    lapse_source = lapse_derivative(mu) - lapse_derivative(0.0)
    radial_source = radial_derivative(mu) - radial_derivative(0.0)

    _, beta1_raw, beta2_raw, beta3_raw, _ = betas
    denominator = beta1_raw + 2.0*K*beta2_raw + K*K*beta3_raw
    beta3_aoki = K*K*beta3_raw/denominator
    measured = lapse_source/3.0 + radial_source
    expected = (
        m2*Mg2*a**4*K*denominator
        * (-mu + (beta3_aoki/3.0)*mu**3)
    )
    assert abs(measured - expected) <= 3.0e-8*max(1.0, abs(expected))

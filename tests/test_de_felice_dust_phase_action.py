import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.de_felice_matter_action import kessence_scalar_quadratic_density


def test_finite_cs2_legendre_form_matches_eq54():
    import numerics.de_felice_dust_phase_action as dust
    cases = (
        dict(rho=4.7, pressure=0.8, cs2=0.37, lapse=1.23, scale_factor=0.74,
             k=2.1, Phi=0.09, B=-0.12, psi=0.07, E=-0.035, q=0.041, momentum=-0.83),
        dict(rho=3.1, pressure=0.0, cs2=0.2, lapse=1.0, scale_factor=0.61,
             k=5.3, Phi=-0.04, B=0.03, psi=-0.02, E=0.014, q=-0.07, momentum=1.17),
        dict(rho=7.2, pressure=1.4, cs2=0.81, lapse=0.91, scale_factor=1.12,
             k=0.8, Phi=0.03, B=-0.08, psi=0.011, E=-0.02, q=0.09, momentum=0.34),
    )
    for c in cases:
        enthalpy = c['rho'] + c['pressure']
        qdot = c['Phi'] + c['cs2'] * (c['momentum']/enthalpy - 3.0*c['psi'])
        direct = kessence_scalar_quadratic_density(
            rho=c['rho'], pressure=c['pressure'], cs2=c['cs2'], lapse=c['lapse'],
            scale_factor=c['scale_factor'], k=c['k'], Phi=c['Phi'], B=c['B'],
            psi=c['psi'], E=c['E'], delta_phi_over_phidot=c['q'],
            delta_phidot_over_phidot=qdot,
        )
        reconstructed = c['momentum'] * qdot + dust.finite_cs2_phase_density(**c)
        assert math.isclose(reconstructed, direct, rel_tol=2e-13, abs_tol=2e-13)


def test_exact_dust_phase_density_is_finite_limit():
    import numerics.de_felice_dust_phase_action as dust
    args = dict(rho=5.4, lapse=1.07, scale_factor=0.82, k=3.6,
                Phi=0.06, B=-0.025, psi=0.013, E=-0.01,
                q=0.047, momentum=0.91)
    exact = dust.dust_phase_density(**args)
    assert math.isfinite(exact)
    for s in (1e-2, 1e-4, 1e-6):
        finite = dust.finite_cs2_phase_density(pressure=0.0, cs2=s, **args)
        enthalpy = args['rho']
        vanishing = -s * (args['momentum'] - 3.0*enthalpy*args['psi'])**2 / (2.0*enthalpy)
        assert math.isclose(finite - vanishing, exact, rel_tol=2e-13, abs_tol=2e-13)


def test_phase_momentum_reconstructs_physical_density():
    import numerics.de_felice_dust_phase_action as dust
    rho, psi, delta_rho = 7.1, -0.023, 0.44
    momentum = delta_rho + 3.0*rho*psi
    measured = dust.physical_density_from_phase_momentum(
        momentum_local=momentum, rho=rho, psi=psi,
    )
    assert math.isclose(measured, delta_rho, rel_tol=0.0, abs_tol=1e-15)


def test_common_normalized_momentum_round_trips_g_and_f_prefactors():
    import numerics.de_felice_dust_phase_action as dust
    local = -0.731
    for prefactor in (1.0, 0.10001030727876269 * 0.050002067707041**3):
        common = dust.common_normalized_momentum(momentum_local=local, prefactor=prefactor)
        recovered = dust.local_momentum_from_common(momentum_common=common, prefactor=prefactor)
        assert math.isclose(recovered, local, rel_tol=1e-14, abs_tol=1e-14)

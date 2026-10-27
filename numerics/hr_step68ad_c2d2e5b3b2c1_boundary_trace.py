"""Exact conditional boundary-trace audit of the original Step55 Pg family.

Only original Step55 g-momentum reconstruction and Step49 center U0 are used.
This is NOT a solution of the f-secondary ODE, a Dirac rank, or a physical
choice of boundary conditions. All rational results use Fraction.
"""
from fractions import Fraction as F

A = F('0.4')
Y = F('0.5787707228025044')
B = A * Y
MF2 = F('0.10879548725') ** 2
MG2 = F(1)
CG = F('0.0015')
Z1 = F('0.004')
R_OUT = F(17, 20)
S_OUT = R_OUT ** 2
ORIGINAL_BLOBS = {
    'numerics/hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step46_exact_secondary_ode.py': 'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step49_analytic_center.py': 'd570948912885d45a625fa2db31c6a5435b6a654',
    'numerics/hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}


def trace_coefficients(r=R_OUT):
    """Derivatives wrt lambda for Pg -> Pg+lambda, at fixed geometry."""
    r = F(r)
    s = r * r
    return {
        'delta_pLg_over_lambda': s * (1 + F(5, 2) * CG * s),
        'delta_pLg_prime_over_lambda': 2 * r * (1 + 5 * CG * s),
        'delta_U0_over_lambda': MF2 * B / (MG2 * A),
    }


def reconstruction_Dg_residual(r, Lg, rho, kg, Gprime, Dbar):
    """Identity for Step55: pSg*Sgr=r(sDbar+Lg Gprime-s rho kg Lg)."""
    r, Lg, rho, kg, Gprime, Dbar = map(F, (r, Lg, rho, kg, Gprime, Dbar))
    s = r * r
    pSg_times_Sgr = r * (s * Dbar + Lg * Gprime - s * rho * kg * Lg)
    pLg_prime = r * Gprime
    pg = s * rho
    tg_prime = r * kg * Lg
    return pSg_times_Sgr - Lg * pLg_prime + pg * tg_prime - r ** 3 * Dbar


def certificate():
    c = trace_coefficients()
    assert c['delta_pLg_over_lambda'] == F(92730563, 128000000)
    assert c['delta_pLg_prime_over_lambda'] == F(2734739, 1600000)
    assert c['delta_U0_over_lambda'] == F(274023815147385251710689588080861, 40000000000000000000000000000000000)
    assert all(v > 0 for v in c.values())
    return {
        'step': '68ad-C2d2e5b3b2c1',
        'scope': 'Exact conditional boundary traces of Step55 Pg-parameter family; no original G execution',
        'outer_r': str(R_OUT),
        'coefficients': {k: str(v) for k, v in c.items()},
        'fixed_pLg_outer_boundary': 'forces lambda=0 for this one-parameter family',
        'fixed_pLg_prime_outer_boundary': 'forces lambda=0 for this one-parameter family',
        'fixed_U0_center': 'forces lambda=0 for this one-parameter family',
        'unfixed_momentum_or_mixed_boundary': 'NOT_DECIDED; boundary data must be specified',
        'original_source_git_blobs': ORIGINAL_BLOBS,
        'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED',
    }


if __name__ == '__main__':
    import json
    print(json.dumps(certificate(), indent=2, ensure_ascii=False))

"""Exact *partial* reduction of the Step58 N' lower residual.

For R = B_N-z*C/Lg+(1-z**2)/(Lg*Lf)*D_r(Hg), four high-jet
coefficients are exact multiples of Fz, with no gauge or Step55 ansatz.
The fifth high jet Sg_rr survives affinely and is eliminated by Hg=0.
This does NOT prove that the remaining first-jet residual vanishes.

The caller must supply Ward and operator dictionaries from authentic
Step45/58 (or explicitly label an independent transcription). This
module does not silently substitute reconstructed physics engines.
"""
import sympy as sp


def verify_high_jet_elimination(ward, op):
    """Check four universal symbolic identities, return a bounded audit."""
    q = dict(zip(ward['Q'], ward['q']))
    qp = dict(zip(ward['Q'], ward['dq']))
    mg = ward['parameters'][0]
    z = op['z']
    root = sp.sqrt(1 - z*z)
    Lg, Lf, Sg = q['Lg'], q['Lf'], q['Sg']
    Sgr, tgr, pg = qp['Sg'], qp['tg'], q['pg']
    K, Fz = op['K'], op['Fz']
    beta = -(1-z*z)/(Lg*Lf)
    residual = op['operator']['N'][1] - z*op['C']/Lg - beta*op['Dt'](ward['Hg'])

    coefficients = {
        op['qppp'][2]: -2*mg*Sg*z*root**3/(Lf*Lg**2*K)*Fz,
        op['qpp'][1]: z*z*root**3/(Lf*Lg*K)*Fz,
        op['qpp'][0]: 2*mg*Sg*Sgr*z*root**3/(Lf*Lg**3*K)*Fz,
        op['qpp'][4]: (
            -pg*z*root**3*(Lg**2*z + Lg*tgr*sp.sqrt(1+tgr**2/Lg**2)
                              + tgr**2*z)
            /(Lf*Lg**2*K*(Lg**2+tgr**2))*Fz
        ),
    }
    for jet, predicted in coefficients.items():
        difference = sp.cancel(sp.diff(residual, jet) - predicted)
        if difference != 0:
            raise AssertionError(('incorrect_high_jet_factor', str(jet), difference))

    high_jets = (*op['qpp'], *op['qppp'], *op['q4'])
    actual = {str(j) for j in high_jets if residual.has(j)}
    expected = {str(op['qpp'][0]), str(op['qpp'][1]), str(op['qpp'][2]),
                str(op['qpp'][4]), str(op['qppp'][2])}
    if actual != expected:
        raise AssertionError(('unexpected_high_jet_dependence', actual, expected))
    if sp.cancel(sp.diff(residual, op['qpp'][2], 2)) != 0:
        raise AssertionError('Sg_rr dependence not affine')
    hg_slope = sp.cancel(sp.diff(ward['Hg'], op['qpp'][2]))
    if sp.cancel(hg_slope - 2*mg*Sg/Lg) != 0:
        raise AssertionError('Hg cannot eliminate Sg_rr')
    return {
        'scope': 'EXACT_FORMAL_STEP45_STEP58_K_POSITIVE_SHIFT_CHART',
        'coefficient_identities_proved': 4,
        'high_jet_dependencies_before_Fz': sorted(actual),
        'remaining_after_Fz_zero': str(op['qpp'][2]),
        'remaining_jet_affine': True,
        'Hg_Sg_rr_coefficient': str(hg_slope),
        'conclusion': 'Fz=Hg=0 reduces R to a first-jet-only algebraic residual; its vanishing is NOT proved',
        'on_full_primary': 'Fz=Fz_r=Hg=Hg_r=0 implies B_N-z*C/Lg equals that unproved first-jet residual',
        'physical_step55_enclosures': 'NOT_CERTIFIED',
        'two_boundary_positive_lapse_BVP': 'NOT_CERTIFIED',
        'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED',
    }

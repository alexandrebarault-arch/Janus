"""Validate authentic paired Step55/Step58 numerical replay, not an enclosure.

Requires the SHA-guarded five original modules and full paired runner. The
22-digit strings come from original probe stdout; floats alone lose detail.
"""
import json
from pathlib import Path
import mpmath as mp
from . import hr_b3c3d6_corrected_step58_point_probe_candidate as physical
from .hr_b3c3d6_ode_consistent_jet_map import endpoint_jets
from .hr_b3c3d6_paired_original_step58_four_radii import MODES, RADII

KEYS = ('N0', 'N1', 'N2', 'M0', 'M1', 'M2')


def printed_coefficients(report):
    parsed = {}
    for line in report['original_probe_stdout'].splitlines():
        parts = line.split()
        if len(parts) == 3 and parts[0] in ('N', 'M') and parts[1] in ('0', '1', '2'):
            key = parts[0] + parts[1]
            if key in parsed:
                raise AssertionError('duplicate coefficient ' + key)
            parsed[key] = mp.mpf(parts[2])
    if set(parsed) != set(KEYS):
        raise AssertionError('incomplete original Step58 six coefficients')
    return parsed


def physical_sensitivity(radius, u):
    """On Fz=0, exact analytic d(A_M)/d(U_ss) from Step58 jet audit."""
    r = physical.F(radius)
    s = r*r
    g = physical.geometry(s)
    gr = physical.G(s, u)
    fields = physical.physical_fields(r, u, gr)
    Lg, Lf, Sf, Sfr = g['Lg0'], g['Lf0'], fields['Sf'], g['Sfr0']
    z = physical.Z1*r
    K = physical.M2*physical.MG*Lg*Lf*(
        physical.B1*fields['Sg']**2 + 2*physical.B2*fields['Sg']*Sf
        + physical.B3*Sf**2)
    tfr = r*g['tf0']
    fac = fields['pLf']/(2*physical.MF*Sf*Sfr)
    beta = mp.sqrt(1+tfr**2/Lf**2)
    return -2*r**4*z*mp.sqrt(1-z*z)*K*beta / (
        Lg*Lf*physical.MF*Sf*Sfr*(beta+fac*tfr))


def validate(result):
    if result['GATE_2B'] != 'OPEN' or result['JANUS_R'] != 'NOT_VALIDATED':
        raise AssertionError('scientific gate unexpectedly altered')
    if len(result['radii']) != 4:
        raise AssertionError('four physical radii required')
    summary = []
    for expected, row in zip(RADII, result['radii']):
        if float(row['radius']) != expected or row['nfev'] <= 0:
            raise AssertionError('radius / solver trace mismatch')
        reports = row['reports']
        if set(reports) != set(MODES):
            raise AssertionError('missing jet mode')
        coeff = {mode: printed_coefficients(reports[mode]) for mode in MODES}
        for mode in MODES:
            report = reports[mode]
            if not report['original_step58_executed'] or not report['paired_state_from_one_DOP853']:
                raise AssertionError('not an original paired physical run')
            if report['source_blobs'] != physical.SOURCE_SHA:
                raise AssertionError('original source SHA guard mismatch')
            if max(abs(mp.mpf(v)) for v in report['shell_residuals'].values()) >= mp.mpf('1e-35'):
                raise AssertionError('pointwise physical shell failed')
        base = coeff['historical_mixed_affine']
        for mode in ('holonomic_quadratic', 'holonomic_cubic'):
            if coeff[mode] != base:
                raise AssertionError('mixed affine vs '+mode+' mismatch at printed 22 digits')
        negative = coeff['holonomic_affine']
        if any(negative[key] != base[key] for key in KEYS if key != 'M0'):
            raise AssertionError('holonomic affine changed coefficient other than M0')
        observed = negative['M0'] - base['M0']
        if observed >= 0:
            raise AssertionError('holonomic affine negative control M0 sign')
        with mp.workdps(50):
            r = physical.F(row['radius'])
            u = mp.mpf(row['shared_U'])
            uss = endpoint_jets(physical.G, r*r, u)['U_ss']
            predicted = physical_sensitivity(row['radius'], u)*(-uss)
            if not predicted < 0 or abs(observed/predicted - 1) >= mp.mpf('2e-10'):
                raise AssertionError('physical Step58 analytic sensitivity disagreement')
            summary.append({
                'r':row['radius'], 'solver_nfev':row['nfev'],
                'U':row['shared_U'],
                'A_N':mp.nstr(base['N0'],22), 'A_M':mp.nstr(base['M0'],22),
                'B_N':mp.nstr(base['N1'],22), 'E_N':mp.nstr(base['N2'],22),
                'B_M':mp.nstr(base['M1'],22), 'E_M':mp.nstr(base['M2'],22),
                'B_E_max_abs':mp.nstr(max(abs(base[k]) for k in ('N1','N2','M1','M2')),8),
                'minus_A_N_over_A_M':mp.nstr(-base['N0']/base['M0'],17),
                'holonomic_affine_delta_M0':mp.nstr(observed,22),
                'sensitivity_predicted_delta_M0':mp.nstr(predicted,22),
                'sensitivity_ratio':mp.nstr(observed/predicted,17),
                'mixed_quadratic_cubic_identical_22digit':True,
                'negative_control_only_M0_changed_22digit':True,
                'pointwise_shell_max_abs':max(abs(v) for mode in MODES
                    for v in reports[mode]['shell_residuals'].values()),
            })
    return {'scope':'PHYSICAL_ORIGINAL_STEP58_NUMERICAL_FOUR_RADII_NOT_CERTIFIED',
            'radii':summary, 'original_sources_sha':physical.SOURCE_SHA,
            'step57':'minimal_import_shim', 'original_global_barrier':'REPLAYED_SEPARATELY_256_CELLS',
            'DOP853_continuous_residual':'NOT_CERTIFIED',
            'coefficient_interval_enclosures':'NOT_CERTIFIED',
            'positive_lapse_two_boundary_BVP':'NOT_TESTED',
            'Dirac_4D_stability_observables':'NOT_TESTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def main():
    from .hr_b3c3d6_paired_original_step58_four_radii import run_all
    return validate(run_all())


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))

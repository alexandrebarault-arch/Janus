"""Exact rational center-chart bounds for the ORIGINAL Step58 stationary shift.

Only a denominator/regularization lemma; not temporal constraint preservation.
Original Step55 and Step58/68o sources are Git-blob pinned for full-clone CLI.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json

SOURCE_PINS = {
    'hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
    'hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
    'hr_step68o_temporal_interval_annulus.py': 'c99caebc17f243784450ddff94fb061767e6d8e7',
}
# Literal source constants from SHA-pinned Step55, interpreted as exact decimals.
A = F('.4')
Y = F('.5787707228025044')
B = A * Y
CG = F('.0015')
CF = F('-.0012')
KF = F('-.0016')
Z1 = F('.004')
M2 = F('23.3348939346')
MG = F(1)
B1 = F(1)
B2 = F('-4.2383993109')
B3 = F('13.6801214252')
SMAX = F(1, 1024)
RMAX = F(1, 32)


def git_blob(raw: bytes) -> str:
    return sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def authenticate_sources(source_folder: Path | str) -> dict[str, str]:
    source_folder = Path(source_folder)
    for name, sha in SOURCE_PINS.items():
        if git_blob((source_folder / name).read_bytes()) != sha:
            raise ValueError(f'Original source changed: {name}')
    return SOURCE_PINS.copy()


def q(y: F) -> F:
    return B1 + 2 * B2 * y + B3 * y * y


def center_shift_chart(u0_upper: F, us_upper: F) -> dict:
    """Rational bounds valid simultaneously for 0<=r<=1/32.

    U(s)<=U0_upper+us_upper*s follows from the certified global U_s bound;
    the two input bounds MUST be obtained from authenticated 68ac/68v.
    """
    u0_upper, us_upper = F(u0_upper), F(us_upper)
    if not (u0_upper < 0 and us_upper > 0 and u0_upper + us_upper * SMAX < 0):
        raise ValueError('Certified U<0 prerequisites not established')
    # y=Lf/Lg=Y*(1+CF*s)^2/(1+CG*s)^2; y_min <= y <= Y.
    ymin = Y * ((1 + CF * SMAX) / (1 + CG * SMAX)) ** 2
    if not (F(1, 2) < ymin <= Y):
        raise AssertionError('positive-K ratio chart invalid')
    qprime_half = 2 * B2 + B3
    if qprime_half <= 0 or B3 <= 0:
        raise AssertionError('q not increasing on [1/2,Y]')
    qmin, qmax = q(ymin), q(Y)
    if not (0 < qmin <= qmax):
        raise AssertionError('positive-K quadratic invalid')
    lgmin, lgmax = A, A * (1 + CG * SMAX) ** 2
    lfmin, lfmax = B * (1 + CF * SMAX) ** 2, B
    # K=m2*mg*Lg*Lf*(B1*Sg^2+2*B2*Sg*Sf+B3*Sf^2)
    # and Sg=r*Lg, Sf=r*Lf. Thus K/r^2=m2*mg*Lg^3*Lf*q(Lf/Lg).
    klo = M2 * MG * lgmin ** 3 * lfmin * qmin
    khi = M2 * MG * lgmax ** 3 * lfmax * qmax
    zmax = Z1 * RMAX
    if not (0 < klo <= khi and zmax < 1):
        raise AssertionError('positive stationary shift chart invalid')
    # Z_D=(1-z^2)^(3/2)/K; Z_K=-z*(1-z^2)/K.
    # For 0<=z^2<=zmax^2<1: (1-z^2)^2 <= (1-z^2)^(3/2) <= 1.
    zdlo = (1 - zmax * zmax) ** 2 / khi
    zdhi = 1 / klo
    zkabs = zmax / klo
    # rho_f denominator is beta_f+s*Ffac*KF*Lf, with
    # Ffac=U/(2*MF*Lf*Sfr)<0, KF<0, Lf>0, s>=0, beta_f>=1.
    # Hence rho_f denominator >=1 exactly (strictly >1 when r>0).
    assert KF < 0 and CF < 0 and (1 + 5 * CF * SMAX) > 0
    return {
        'step': '68ad-C2c-chart', 'radius': ['0', str(RMAX)],
        'y_lower': str(ymin), 'y_upper': str(Y),
        'q_lower': str(qmin), 'q_upper': str(qmax),
        'K_over_r2_lower': str(klo), 'K_over_r2_upper': str(khi),
        'z_absolute_upper': str(zmax),
        'r2_ZD_lower': str(zdlo), 'r2_ZD_upper': str(zdhi),
        'r2_ZK_absolute_upper': str(zkabs),
        'f_dust_denominator_lower': '1',
        'K_center': '0', 'K_positive_for_r_positive': True,
        'unscaled_ZD_at_center': 'SINGULAR_IN_RAW_FORMULA',
        'temporal_operator_Step58_60_executed': False,
        'seven_temporal_signs': 'PENDING',
        'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED',
    }


def main():
    root = Path(__file__).resolve().parents[1]
    authenticate_sources(root / 'numerics')
    from .hr_step68ad_c2b_center_boxes import load_pinned, validate_reports
    reports = load_pinned(root / 'research' / 'reports')
    u0, _, _, us, _, _ = validate_reports(reports)
    print(json.dumps(center_shift_chart(u0.hi, us.hi), indent=2))


if __name__ == '__main__':
    main()

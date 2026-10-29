"""Audit the actual Step55->Step58 candidate's float initial-value conversion.

Reproduces only the public candidate's center constants and its s0=1e-4
quadratic initial condition. It does NOT execute original Step55/Step58,
bound the unknown Taylor remainder, or certify physical lapse coefficients.
"""
from __future__ import annotations
import mpmath as mp

# Verbatim decimal literals/formulas from the authenticated candidate blob
# numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py
# 8162e35deed964a5ec2cbca53bc32cc5c875e420 (read 2026-10-30).
SOURCE_CANDIDATE_BLOB = '8162e35deed964a5ec2cbca53bc32cc5c875e420'


def center_initial_value(dps: int = 100):
    """Compute the *truncated* center value at s0, before binary rounding."""
    if dps < 70:
        raise ValueError('at least 70 decimal digits required for this audit')
    with mp.workdps(dps):
        f = mp.mpf
        a = f('.4')
        y = f('.5787707228025044')
        b = a*y
        mf = f('.10879548725')**2
        m2 = f('23.3348939346')
        b0,b1,b2,b3 = [f(x) for x in ('0','1','-4.2383993109','13.6801214252')]
        z1 = f('.004')
        h2 = f('.9')/(3*a**3) + m2*(b0+3*b1*y+3*b2*y*y+b3*y**3)/3
        if h2 <= 0:
            raise AssertionError('original center root not positive')
        pg = -2*a*a*mp.sqrt(h2)
        u0 = mf*b*(pg/a-2*z1)
        u1 = f('0.0007897451667202464909325108904961683602148118201691')
        u2 = f('-0.00001007385348674382817573689095286393593388364194376377343')
        s0 = f('0.0001')
        value = u0 + u1*s0 + u2*s0**2
        return +value


def diagnostics(dps: int = 100):
    with mp.workdps(dps):
        f = mp.mpf
        y = center_initial_value(dps)
        y_float = float(y)  # exactly what original solve_ivp receives
        y_binary = f(y_float)  # exact binary64 value represented in mp
        y_shortest_decimal = f(str(y_float))  # how original F(y[0]) sees it
        return {
            'y_truncated': mp.nstr(y, dps-10),
            'float_repr': repr(y_float),
            'binary_rounding_error': mp.nstr(abs(y_binary-y), 50),
            'shortest_decimal_error': mp.nstr(abs(y_shortest_decimal-y), 50),
            'binary_vs_shortest_decimal': mp.nstr(abs(y_binary-y_shortest_decimal), 50),
            'relative_binary_rounding_error': mp.nstr(abs(y_binary-y)/abs(y), 50),
            'binary_rounding_error_over_1e_minus_44': mp.nstr(abs(y_binary-y)/f('1e-44'), 50),
        }


if __name__ == '__main__':
    import json
    print(json.dumps(diagnostics(), indent=2))

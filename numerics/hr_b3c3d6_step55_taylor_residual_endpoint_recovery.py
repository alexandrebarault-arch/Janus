"""Recover Step55 Taylor residual at four exact radii from archived endpoint boxes.

Exact rational consequence of the *previously executed* physical Step55
monotonicity certificate. No original Step45/46/55/58 engine is rerun here.
No claim of a continuous residual bound or Step58 A/B/E enclosures.
"""
from fractions import Fraction as F
from hashlib import sha1
from math import isqrt
from pathlib import Path
import json

ARCHIVE = 'research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json'
ARCHIVE_SHA = 'e74057dcf741bcdb655c7d9be48c6a9650d7ff3f'
RADII = (F(1, 4), F(1, 2), F(7, 10), F(17, 20))
DELTA = F(1, 10000)
U1 = (F('0.0007897451667202464909325108904961683602148118201690'),
      F('0.0007897451667202464909325108904961683602148118201692'))
U2 = (F('-0.00001007385348674382817573689095286393593388364194376377344'),
      F('-0.00001007385348674382817573689095286393593388364194376377342'))


def u0_interval():
    a, y, m2 = F('.4'), F('.5787707228025044'), F('23.3348939346')
    h2 = F('.9')/(3*a**3) + m2*(3*y + 3*F('-4.2383993109')*y*y
                                       + F('13.6801214252')*y**3)/3
    scale = 10**40
    n = isqrt(h2.numerator*scale**2//h2.denominator)
    assert F(n,scale)**2 <= h2 < F(n+1,scale)**2
    fac = F('.10879548725')**2*a*y
    return (fac*(-2*a*F(n+1,scale)-2*F('.004')),
            fac*(-2*a*F(n,scale)-2*F('.004')))


def recover_center_from_endpoints(glo, ghi, gu_hi, delta):
    """MVT: G(Ustar+delta)>=glo, G(Ustar-delta)<=ghi, G_U<=gu_hi<0.

    Hence G(Ustar) in [glo-gu_hi*delta, ghi+gu_hi*delta].
    The same Ustar is used on both sides (correlated, not interval hull).
    """
    glo,ghi,gu_hi,delta = map(F,(glo,ghi,gu_hi,delta))
    if not glo <= ghi or not gu_hi < 0 or not delta > 0:
        raise ValueError('missing endpoint ordering or negative derivative')
    lo,hi = glo-gu_hi*delta, ghi+gu_hi*delta
    if lo > hi:
        raise ValueError('incompatible endpoint and derivative certificates')
    return lo,hi


def certify_rows(rows):
    if len(rows) != 4:
        raise ValueError('requires all four exact radii')
    u0 = u0_interval()
    output=[]
    for r,row in zip(RADII,rows):
        s=r*r
        if F(row['r'])!=r or F(row['s'])!=s:
            raise ValueError('archive exact radius mismatch')
        glo,ghi=map(F,row['G_monotone'])
        gu_lo,gu_hi=map(F,row['G_U'])
        if not gu_lo <= gu_hi < 0:
            raise ValueError('uncertified G_U monotonicity')
        gstar = recover_center_from_endpoints(glo,ghi,gu_hi,DELTA)
        vstar_lo=2*u0[0]+4*U1[0]*s+6*U2[0]*s*s
        vstar_hi=2*u0[1]+4*U1[1]*s+6*U2[1]*s*s
        residual=(gstar[0]-vstar_hi,gstar[1]-vstar_lo)
        width_before=ghi-glo
        width_after=gstar[1]-gstar[0]
        assert 0<width_after<width_before
        assert width_before/width_after>900
        assert -s/F(4000000)<residual[0]<=0<=residual[1]<s/F(4000000)
        output.append({'r':str(r),'s':str(s),
                       'G_at_Ustar':list(map(str,gstar)),
                       'Rstar_G_minus_2Ustar_minus_2sUstar_s':list(map(str,residual)),
                       'width_shrink_factor_strictly_above_900':True,
                       'residual_abs_strict_less_than':str(s/F(4000000)),
                       'residual_sign':'UNRESOLVED'})
    return {'scope':'FOUR_EXACT_POINTS_ONLY_CONDITIONAL_ON_ARCHIVED_PHYSICAL_ENDPOINT_G_AND_GU',
            'archive_blob':ARCHIVE_SHA,'four_points':output,
            'continuous_residual':'NOT_CERTIFIED',
            'Step58_six_A_B_E':'NOT_CERTIFIED','BVP':'NOT_CERTIFIED',
            'original_physical_engines_replayed_this_run':False,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def certify(root=None):
    root=Path(root) if root is not None else Path(__file__).resolve().parents[1]
    raw=(root/ARCHIVE).read_bytes()
    blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob!=ARCHIVE_SHA:
        raise ValueError(f'archive Git blob SHA mismatch {blob}')
    return certify_rows(json.loads(raw)['radii'])


if __name__=='__main__':
    print(json.dumps(certify(),indent=2))

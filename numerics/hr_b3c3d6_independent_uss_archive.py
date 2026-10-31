"""Independent exact-rational Step55 U_ss budget from archived physical boxes.

No original physical Step45/46/55/58 execution here. The archival boxes
are taken as certified inputs only after their Git blob SHA is checked.
Four radii are isolated points, not a continuous radial certificate.
"""
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ARCHIVE = 'research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json'
ARCHIVE_SHA = 'e74057dcf741bcdb655c7d9be48c6a9650d7ff3f'
RADII = (F(1, 4), F(1, 2), F(7, 10), F(17, 20))
U1 = (F('0.0007897451667202464909325108904961683602148118201690'),
      F('0.0007897451667202464909325108904961683602148118201692'))
U2 = (F('-0.00001007385348674382817573689095286393593388364194376377344'),
      F('-0.00001007385348674382817573689095286393593388364194376377342'))
LIMITS = (F(1, 10), F(1, 160), F(1, 590), F(1, 1200))


def original_u0_interval():
    """Reconstruct Step55 U0 from rational constants; sqrt enclosed exactly."""
    a = F('.4'); y = F('.5787707228025044'); b = a*y
    m2 = F('23.3348939346')
    b0,b1,b2,b3 = map(F, ('0','1','-4.2383993109','13.6801214252'))
    h2 = F('.9')/(3*a**3) + m2*(b0+3*b1*y+3*b2*y*y+b3*y**3)/3
    scale = 10**40
    n = isqrt(h2.numerator * scale**2 // h2.denominator)
    assert F(n,scale)**2 <= h2 < F(n+1,scale)**2
    fac = F('.10879548725')**2 * b
    return (fac*(-2*a*F(n+1,scale)-2*F('.004')),
            fac*(-2*a*F(n,scale)-2*F('.004')))


def mul(a,b):
    p = [x*y for x in a for y in b]
    return (min(p),max(p))


def derive(report):
    if len(report['radii']) != 4:
        raise ValueError('exactly four physical records required')
    u0 = original_u0_interval()
    out=[]
    for r, limit, row in zip(RADII,LIMITS,report['radii']):
        s = r*r
        if F(row['r']) != r or F(row['s']) != s:
            raise ValueError('radius mismatch')
        g = tuple(map(F,row['G_monotone']))
        gs = tuple(map(F,row['G_s_composed']))
        gu = tuple(map(F,row['G_U']))
        if not (g[0]<=g[1] and 0<gs[0]<=gs[1] and gu[0]<=gu[1]<0):
            raise ValueError('missing physical sign guard')
        u=(u0[0]+U1[0]*s+U2[0]*s*s-F(1,10000),
           u0[1]+U1[1]*s+U2[1]*s*s+F(1,10000))
        f=((g[0]-2*u[1])/(2*s),(g[1]-2*u[0])/(2*s))
        term=mul((gu[0]-4,gu[1]-4),f)
        uss=((gs[0]+term[0])/(2*s),(gs[1]+term[1])/(2*s))
        if not (-limit<uss[0]<=uss[1]<limit):
            raise ArithmeticError('U_ss budget failed')
        # Exact identity: pLf''=G+2sG_s+G_U(G-2U).
        term2=mul(gu,(2*s*f[0],2*s*f[1]))
        plf2=(g[0]+2*s*gs[0]+term2[0],g[1]+2*s*gs[1]+term2[1])
        published=tuple(map(F,row['pLf_second']))
        if not (published[0]<=plf2[0]<=plf2[1]<=published[1]<0):
            raise ArithmeticError('archived pLf second derivative inconsistency')
        out.append({'r':str(r),'s':str(s),'U_ss':[str(x) for x in uss],
                    'U_s':[str(x) for x in f],
                    'U_ss_abs_strict_bound':str(limit),
                    'U_ss_sign':'UNRESOLVED',
                    'pLf_second_strictly_negative_independent_check':True})
    return {'scope':'INDEPENDENT_RATIONAL_RECOMBINATION_OF_AUTHENTICATED_ARCHIVED_POINTWISE_STEP55_BOXES',
            'archive_blob':ARCHIVE_SHA,'radii':out,'physical_originals_executed_this_run':False,
            'Step58_six_A_B_E':'NOT_CERTIFIED', 'BVP':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def load_and_derive(root=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    raw=(root/ARCHIVE).read_bytes()
    got=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if got != ARCHIVE_SHA:
        raise ValueError(f'archive blob mismatch {got} != {ARCHIVE_SHA}')
    return derive(json.loads(raw))

if __name__ == '__main__':
    print(json.dumps(load_and_derive(),indent=2))

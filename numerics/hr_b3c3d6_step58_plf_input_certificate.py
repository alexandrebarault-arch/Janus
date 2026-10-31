"""Exact Step55 pointwise pLf jets 0/1/2, NOT six Step58 coefficients."""
from fractions import Fraction as F
from .hr_b3c3d6_independent_uss_archive import (
    ARCHIVE, ARCHIVE_SHA, RADII, U1, U2, original_u0_interval,
    load_and_derive,
)
import json
from pathlib import Path


def certify(root=None):
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    checked=load_and_derive(root)  # Verifies byte-identical physical archive SHA.
    data=json.loads((root/ARCHIVE).read_bytes())
    u0=original_u0_interval()
    out=[]
    for r,row in zip(RADII,data['radii']):
        s=r*r
        u=(u0[0]+U1[0]*s+U2[0]*s*s-F(1,10000),
           u0[1]+U1[1]*s+U2[1]*s*s+F(1,10000))
        g=tuple(map(F,row['G_monotone']))
        p0=(s*u[0],s*u[1])
        p1=(r*g[0],r*g[1])
        p2=tuple(map(F,row['pLf_second']))
        assert F(row['r'])==r and F(row['s'])==s
        assert p0[0]<=p0[1]<0 and p1[0]<=p1[1]<0 and p2[0]<=p2[1]<0
        assert checked['radii'][len(out)]['pLf_second_strictly_negative_independent_check']
        out.append({'r':str(r),'pLf':[str(v) for v in p0],
                    'pLf_r':[str(v) for v in p1],
                    'pLf_rr':[str(v) for v in p2]})
    return {'archive_blob':ARCHIVE_SHA,'pointwise_radii':out,
            'all_three_jets_strictly_negative_at_four_points':True,
            'third_jet':'NOT_ENCLOSED', 'six_Step58_A_B_E':'NOT_CERTIFIED',
            'original_engine_replayed':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(certify(),indent=2))

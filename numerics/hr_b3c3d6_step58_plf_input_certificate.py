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


def certify_correlated_growth(root=None):
    """Global U<0 via Step55 barrier; pointwise d_s G>0 by correlated boxes."""
    from .hr_b3c3d6_independent_uss_archive import mul
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    certify(root)  # authenticates archive and original three radial jets
    rows=json.loads((root/ARCHIVE).read_bytes())['radii']
    u0=original_u0_interval()
    S,delta=F(289,400),F(1,10000)
    assert U1[0]>0 and U2[1]<0
    ulo=u0[0]+U2[0]*S*S-delta
    uhi=u0[1]+U1[1]*S+delta
    assert -F(67,12500)<ulo<=uhi<-F(229,50000)<0
    out=[]
    for r,row in zip(RADII,rows):
        s=r*r
        assert F(row['r'])==r and F(row['s'])==s
        u=(u0[0]+U1[0]*s+U2[0]*s*s-delta,
           u0[1]+U1[1]*s+U2[1]*s*s+delta)
        g,gs,gu=(tuple(map(F,row[k])) for k in
                 ('G_monotone','G_s_composed','G_U'))
        assert g[1]<0 and gs[0]>0 and gu[1]<0
        us=((g[0]-2*u[1])/(2*s),(g[1]-2*u[0])/(2*s))
        product=mul(gu,us)
        total=(gs[0]+product[0],gs[1]+product[1])
        assert total[0]>F(1,2000) and total[0]<=total[1]
        out.append({'r':str(r),'U_s':[str(x) for x in us],
                    'dG_ds_total':[str(x) for x in total],
                    'dG_dr':[str(2*r*x) for x in total],
                    'pLf_rr_minus_pLf_r_over_r':[str(2*s*x) for x in total]})
    return {'archive_blob':ARCHIVE_SHA,
            'global_U_actual':[str(ulo),str(uhi)],
            'global_U_strict':['-67/12500','-229/50000'],
            'four_exact_radii':out,'Step58_A_B_E':'NOT_CERTIFIED',
            'BVP':'NOT_CERTIFIED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

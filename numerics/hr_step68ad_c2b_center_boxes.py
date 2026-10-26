"""68ad-C2b: rigorous s-center input boxes for original Step68o physical jets.

Inputs are the SHA-pinned Step68v/68ac/B2 physical certificates. The output
is a set of exact rational enclosures of U, U_s, U_ss, U_sss on closed
radius cells, suitable for constructing Step68n Jets WITHOUT (G-2U)/(2s).

This is a preparatory enclosure, NOT evaluation of Step58/60 temporal signs.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json

PINS = {
    '68v': ('gate2b-step68v-global-monotone-radial-U.json', 'd83a3b80862a2e990a4c4879ec8745a4e91c8b34'),
    '68ac': ('gate2b-step68ac-authentic-U4-report.json', '16ae8dab3563c17134e4e20f886fb7306dc2e4ba'),
    'B2': ('gate2b-step68ad-B2-original-G-Uss-Usss.json', 'ac961b5b83667a83497497d22a701c24584cb561'),
}
SMAX=F(1,1024)

@dataclass(frozen=True)
class Q:
    lo:F
    hi:F
    def __post_init__(self):
        object.__setattr__(self,'lo',F(self.lo))
        object.__setattr__(self,'hi',F(self.hi))
        if self.lo>self.hi:raise ValueError('Reversed rational interval')
    @classmethod
    def from_pair(cls, pair):
        if len(pair)!=2:raise ValueError('Expected two rational endpoints')
        return cls(F(pair[0]),F(pair[1]))
    @classmethod
    def c(cls,x):return cls(F(x),F(x))
    def __add__(self,b):
        b=b if isinstance(b,Q) else Q.c(b)
        return Q(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return Q(-self.hi,-self.lo)
    def __sub__(self,b):return self+-b if isinstance(b,Q) else self+(-F(b))
    def __mul__(self,b):
        b=b if isinstance(b,Q) else Q.c(b)
        corners=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return Q(min(corners),max(corners))
    __rmul__=__mul__
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('Only nonnegative integer powers')
        if n==0:return Q.c(1)
        if n%2==0 and self.lo<=0<=self.hi:
            return Q(F(0),max(abs(self.lo),abs(self.hi))**n)
        if n%2==0:
            return Q(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
        return Q(self.lo**n,self.hi**n)
    def pair(self):return [str(self.lo),str(self.hi)]


def git_blob(data:bytes):return sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def load_pinned(folder:Path|str):
    folder=Path(folder)
    out={}
    for label,(name,sha) in PINS.items():
        raw=(folder/name).read_bytes()
        if git_blob(raw)!=sha:raise ValueError('Pinned physical report drift: '+label)
        out[label]=json.loads(raw)
    return out


def validate_reports(reports):
    v,ac,b=(reports[k] for k in ('68v','68ac','B2'))
    if (v.get('step')!='68v' or ac.get('step')!='68ac' or b.get('step')!='68ad-B2'
        or v.get('center_s_range')!=['0','1/64']
        or b.get('s_domain')!=['0','1/1024']
        or b.get('r_domain')!=['0','1/32']
        or v.get('center_cubic_barrier_kappa')!='1/10000000'
        or v.get('U_s_strict_positive_inner') is not True
        or b.get('strict_negative_R2_U_ss_R3_U_sss') is not True
        or b.get('original_report_sha')!={'68v':PINS['68v'][1],'68ac':PINS['68ac'][1]}
        or ac.get('center_exact_symbolic_GU',{}).get('center_GU0_exact')!='-1'
        or any(x.get('GATE_2B')!='OPEN' or x.get('JANUS_R')!='NOT_VALIDATED' for x in (v,ac,b))):
        raise ValueError('Physical reports do not establish required chart')
    u0=Q.from_pair(ac['center_U0_interval'])
    u1=Q.from_pair(ac['original_U1_interval'])
    u2=Q.from_pair(ac['original_U2_interval'])
    us=Q(F(v['U_s_center_lower_rational']),F(v['U_s_center_upper_rational']))
    uss=Q.from_pair(b['U_ss_global'])
    usss=Q.from_pair(b['U_sss_global'])
    if not (u0.hi<0 and u1.lo>0 and u2.hi<0 and us.lo>0 and uss.hi<0 and usss.hi<0):
        raise ValueError('Historical sign prerequisites failed')
    return u0,u1,u2,us,uss,usss


def center_cell_box(reports,rlo,rhi):
    u0,u1,u2,us,uss,usss=validate_reports(reports)
    rlo,rhi=F(rlo),F(rhi)
    if rlo<0 or rlo>rhi or rhi>F(1,32):
        raise ValueError('Radius outside certified B2 center domain')
    s=Q(rlo*rlo,rhi*rhi)
    k=F(1,10000000)
    star=u0+u1*s+u2*s**2
    err=Q(-k*s.hi**3,k*s.hi**3)
    U=star+err
    # Independently valid monotone interval from the original Step68v U_s>0.
    monotone=Q(u0.lo+us.lo*s.lo,u0.hi+us.hi*s.hi)
    U=Q(max(U.lo,monotone.lo),min(U.hi,monotone.hi))
    if U.lo>U.hi:raise ArithmeticError('Cubic and slope tubes inconsistent')
    return {'r':[str(rlo),str(rhi)],'s':s.pair(),
            'U':U.pair(),'U_s':us.pair(),'U_ss':uss.pair(),'U_sss':usss.pair(),
            'cubic_barrier_error_abs':str(k*s.hi**3),
            's_denominator_division':False}


def certify_cells(reports,edges=None):
    if edges is None:
        edges=[F(1,64)+F(i,7)*F(1,64) for i in range(8)]
    edges=[F(x) for x in edges]
    if len(edges)<2 or edges[0]<0 or edges[-1]>F(1,32) or any(a>=b for a,b in zip(edges,edges[1:])):
        raise ValueError('Invalid ordered closed-cell cover')
    rows=[center_cell_box(reports,a,b) for a,b in zip(edges,edges[1:])]
    if rows[0]['r'][0]!=str(edges[0]) or rows[-1]['r'][1]!=str(edges[-1]):
        raise AssertionError('Incomplete interval cover')
    return {'step':'68ad-C2b','kind':'RIGOROUS_CENTER_SAFE_ORIGINAL_U_JET_INPUT_BOXES',
            'pinned_original_report_git_blobs':{k:v[1] for k,v in PINS.items()},
            'closed_radius_domain':[str(edges[0]),str(edges[-1])],
            'cell_count':len(rows),'cells':rows,
            'input_U_derivative_orders':[0,1,2,3],
            'Taylor_coefficients_for_original_Step68n_Jet':'[U,U_s,U_ss/2,U_sss/6]',
            'source':'Original Step68v cubic barrier plus Step68ac U0/U1/U2 and B2 continuum higher derivatives; exact rational arithmetic',
            'ten_profiles_dependency':'Original Step68o explicit jet_geometry(s), jet_G(s,U), rho_f(s,U,G), pSf(s,U,G,rho_f); all are algebraic compositions and require no U derivative above order 3 for third radial jets.',
            'original_Step58_Step60_temporal_operator':'NOT_EXECUTED',
            'seven_temporal_cell_signs':'PENDING',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def main():
    import sys
    if len(sys.argv)!=2:raise SystemExit('usage: python -m numerics.hr_step68ad_c2b_center_boxes research/reports')
    print(json.dumps(certify_cells(load_pinned(sys.argv[1])),indent=2))

if __name__=='__main__':main()

"""Experimental mean-value enclosure of original Step60 lower-jet AM/BN.

No conclusion from failure. The exact mean-value theorem requires that the
input derivative intervals bound the physical C^1 radial branch on each cell.
"""
from fractions import Fraction as F
from . import hr_step68o_temporal_interval_annulus as annulus
from . import hr_step55_global_barrier as old
from .hr_step68n_interval_ode_jets import I,Jet
from .hr_step68ad_c2d2a_temporal_replay import box_for_rounded_s,inject_s_jet
from .hr_step68ad_c2b_center_boxes import Q,validate_reports
from .hr_step68ad_c2d2c_step60_lower_quotient_replay import compiled_lower_quotient
from .hr_step58_temporal_operator import physical_operator
from .hr_step45_exact_physical_ward import exact_physical_ward

class Dual:
    __slots__=('v','d')
    def __init__(self,v,d=0):self.v=I.c(v);self.d=I.c(d)
    @staticmethod
    def c(x):return x if isinstance(x,Dual) else Dual(x)
    def __add__(self,x):
        x=self.c(x);return Dual(self.v+x.v,self.d+x.d)
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,-self.d)
    def __sub__(self,x):return self+-self.c(x)
    def __rsub__(self,x):return self.c(x)+-self
    def __mul__(self,x):
        x=self.c(x);return Dual(self.v*x.v,self.d*x.v+self.v*x.d)
    __rmul__=__mul__
    def inv(self):return Dual(self.v.inv(),-self.d/(self.v**2))
    def __truediv__(self,x):return self*self.c(x).inv()
    def __rtruediv__(self,x):return self.c(x)*self.inv()
    def sqrt(self):
        root=self.v.sqrt()
        return Dual(root,self.d/(2*root))
    def __pow__(self,n):
        if n==F(1,2):return self.sqrt()
        if n==F(-1,2):return self.sqrt().inv()
        if int(n)!=n:raise ValueError(f'unsupported exponent {n}')
        n=int(n)
        if n<0:return self.inv()**(-n)
        if n==0:return Dual(1)
        return Dual(self.v**n,n*self.v**(n-1)*self.d)
    def __abs__(self):
        if self.v.lo>0:return self
        if self.v.hi<0:return -self
        raise ValueError('Absolute value nondifferentiable on interval')


def radial_duals(lo,hi,reports):
    lo,hi=F(lo),F(hi)
    si=I.hull(lo,hi)**2
    box=box_for_rounded_s(reports,si,{'r':[str(lo),str(hi)]},Q,validate_reports)
    with inject_s_jet(annulus,box,Jet,I,si):
        canonical,R,_,_=annulus.canonical_jets_cell(lo,hi)
    o=physical_operator();p=exact_physical_ward()
    vals={}
    for keys,degree in ((o['q'],0),(o['qp'],1),(o['qpp'],2)):
        for sym,name in zip(keys,p['Q']):
            jet=canonical[name].a
            fac=(1,1,2)[degree]
            der=(1,2,6)[degree]
            vals[sym]=Dual(jet[degree]*fac,jet[degree+1]*der)
    for sym,name in zip((o['z'],o['zr'],o['zrr']),('z','zr','zrr')):
        if name=='z': vals[sym]=Dual(R*old.Z1,old.Z1)
        elif name=='zr': vals[sym]=Dual(old.Z1)
        else: vals[sym]=Dual(0)
    for sym,name in zip(p['parameters'][:8],('MG','MF','M2','B0','B1','B2','B3','B4')):
        vals[sym]=Dual(getattr(old,name))
    return vals


def value_and_derivative(lo,hi,reports,labels=("AM",)):
    vals=radial_duals(lo,hi,reports)
    out={}
    for name,(syms,fn) in compiled_lower_quotient().items():
        if name not in labels:continue
        missing=[str(s) for s in syms if s not in vals]
        if missing:raise ValueError('Missing jets: '+str(missing))
        v=fn(*[vals[s] for s in syms]);
        if isinstance(v,list):v=v[0]
        v=Dual.c(v)
        out[name]=v
    return out


def mean_value_cell(lo,hi,reports):
    lo,hi=F(lo),F(hi);mid=(lo+hi)/2
    center=value_and_derivative(mid,mid,reports)
    derivative=value_and_derivative(lo,hi,reports)
    h=I.hull(-((hi-lo)/2),((hi-lo)/2))
    return {name:{'center':center[name].v,'derivative':derivative[name].d,
                  'mean_value':center[name].v+h*derivative[name].d}
            for name in ('AM',)}


def main():
    import json,argparse
    from pathlib import Path
    from .hr_step68ad_c2b_center_boxes import load_pinned
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--parts',type=int,default=32)
    args=parser.parse_args()
    reports=load_pinned(args.repo/'research/reports')
    result=compact_certificate(certify_AM_fixed_grid(reports,args.parts))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'leaves':result['total_leaves'],
       'AM_negative_cells':result['continuous_AM_negative_cells'],
       'max_depth':max(row['max_depth'] for row in result['cells']),
       'out':str(args.out)}))



def certify_AM_fixed_grid(reports, parts=32):
    """Uniform rational partition with mean-value derivative enclosures."""
    from .hr_step68ad_c2b_center_boxes import certify_cells
    from .hr_step68ad_c2d2a_temporal_replay import verify_original_files
    from .hr_step60_full_constraint_prolongation import verified_original_sources
    from pathlib import Path
    if not isinstance(parts,int) or parts<1 or parts>4096:
        raise ValueError('Invalid partition size')
    original=certify_cells(reports)
    if original['cell_count']!=7 or original['closed_radius_domain']!=['1/64','1/32']:
        raise AssertionError('Unexpected original domain')
    sources=verify_original_files(Path(__file__).parent)
    sources.update(verified_original_sources())
    rows=[]
    for index,cell in enumerate(original['cells']):
        lo,hi=map(F,cell['r']); edges=[lo+(hi-lo)*j/parts for j in range(parts+1)]
        leaves=[]
        for j,(a,b) in enumerate(zip(edges,edges[1:])):
            bounds=mean_value_cell(a,b,reports)
            am=bounds['AM']['mean_value']
            if am.hi>=0:
                raise ArithmeticError(f'AM mean-value INCOMPLETE at cell {index} subcell {j} [{a},{b}], upper={am.hi}')
            leaves.append({'r':[str(a),str(b)],
                  'center_AM':[str(F(bounds['AM']['center'].lo,old.S)),str(F(bounds['AM']['center'].hi,old.S))],
                  'derivative_AM':[str(F(bounds['AM']['derivative'].lo,old.S)),str(F(bounds['AM']['derivative'].hi,old.S))],
                  'mean_value_AM':[str(F(am.lo,old.S)),str(F(am.hi,old.S))]})
        rows.append({'original_r':[str(lo),str(hi)],'leaves':leaves,'leaf_count':len(leaves)})
        print(f'certified original cell {index+1}/7, leaves {len(leaves)}',flush=True)
    return {'step':'68ad-C2d2d-correlated-mean-value-Step60-AM',
            'source_git_blobs':sources,'original_report_git_blobs':original['pinned_original_report_git_blobs'],
            'method':'Original Step60 lower-jet AM evaluated by forward-mode interval AD on exact Step68o radial jets, first-order mean-value enclosure centered at each rational subcell midpoint',
            'cells':rows,'total_leaves':parts*7,'continuous_AM_negative_cells':7,
            'BN_continuum':'INCOMPLETE','Step58_continuum':'INCOMPLETE',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'limitations':'Conditional on pinned original physical spatial profile and derivative tubes. Only Step60 AM<0 on r in [1/64,1/32] is certified. BN, original Step58 continuum, Dirac rank, lapse existence, boundary, 4D, stability and observables remain open.'}


def compact_certificate(full):
    """Publish small, independently checkable rational mean-value witnesses."""
    if full['continuous_AM_negative_cells']!=7 or full['total_leaves']!=224:
        raise AssertionError('Only exact 7x32 validated default certificate')
    cells=[];upper=[];lower=[]
    for row in full['cells']:
        leaves=[]
        for leaf in row['leaves']:
            a,b=map(F,leaf['mean_value_AM'])
            if a>b or b>=0:raise AssertionError('Invalid strict-negative witness')
            leaves.append({'r':leaf['r'],'AM':[str(a),str(b)]})
            lower.append(a);upper.append(b)
        cells.append({'r':row['original_r'],'leaves':leaves})
    return {'step':full['step'],'method':full['method'],
            'original_source_git_blobs':full['source_git_blobs'],
            'original_report_git_blobs':full['original_report_git_blobs'],
            'original_cells':cells,'total_subcells':len(upper),
            'continuous_AM_negative_original_cells':len(cells),
            'max_AM_upper':str(max(upper)),'min_AM_lower':str(min(lower)),
            'Step60_BN_continuum':'INCOMPLETE','Step58_continuum':'INCOMPLETE',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'limitations':full['limitations']}

if __name__=='__main__':main()
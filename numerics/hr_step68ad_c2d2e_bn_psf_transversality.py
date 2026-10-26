"""68ad-C2d2e: conditional continuum transversality of original Step60 BN in pSf.

Exact algebra: d²(BN)/d(pSf)²=0 for the ORIGINAL third-jet-free Step60
representative, so BN=B0+J*pSf.  This module certifies J<0, not BN=0.

Mean-value enclosures are conditional on the original SHA-pinned Step68o
spatial branch and the U,U_s,U_ss,U_sss tubes from the three physical reports.
No Dirac rank, lapse or full JANUS validation is inferred.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import argparse, json
import sympy as sp

from .hr_step60_full_constraint_prolongation import full_constraint_prolongation, verified_original_sources
from .hr_step68ad_c2d2d_correlated_mean_value import radial_duals, Dual
from .hr_step68ad_c2b_center_boxes import load_pinned, certify_cells
from .hr_step68ad_c2d2a_temporal_replay import verify_original_files
from .hr_step68n_interval_ode_jets import I

@lru_cache(maxsize=1)
def original_bn_affine():
    original = full_constraint_prolongation()['third_free_BN_on_Fz']
    psf = next((s for s in original.free_symbols if str(s)=='pSf'),None)
    if psf is None:raise AssertionError('Original BN has no pSf')
    if sp.diff(original,psf,2)!=0:
        raise AssertionError('Original BN is not affine in pSf')
    slope = sp.diff(original,psf)
    if slope.has(psf):raise AssertionError('BN slope still depends on pSf')
    return original,psf,slope

@lru_cache(maxsize=1)
def compiled_slope():
    _,_,slope=original_bn_affine()
    half=sp.Function('interval_halfpow')
    safe=slope.replace(lambda x:x.is_Pow and x.exp.is_Rational and x.exp.q==2,
        lambda x:half(x.base,sp.Integer(x.exp.p)))
    syms=tuple(sorted(slope.free_symbols,key=str))
    fn=sp.lambdify(syms,safe,modules=[{'interval_halfpow':lambda x,p:x.sqrt()**int(p),
        'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
    return syms,fn

def slope_dual(lo,hi,reports):
    lo,hi=F(lo),F(hi)
    if not F(1,64)<=lo<=hi<=F(1,32):
        raise ValueError('Outside authenticated positive radial chart')
    vals=radial_duals(lo,hi,reports)
    syms,fn=compiled_slope()
    if any(s not in vals for s in syms):raise AssertionError('Missing physical canonical jet')
    v=fn(*[vals[s] for s in syms])
    if isinstance(v,list):
        if len(v)!=1:raise AssertionError('Unexpected slope result arity')
        v=v[0]
    return Dual.c(v)

def mean_value_slope(lo,hi,reports):
    lo,hi=F(lo),F(hi)
    if not lo<hi:raise ValueError('Strictly positive subcell required')
    mid=(lo+hi)/2
    center=slope_dual(mid,mid,reports).v
    derivative=slope_dual(lo,hi,reports).d
    h=I.hull(-(hi-lo)/2,(hi-lo)/2)
    return {'center':center,'derivative':derivative,'mean_value':center+h*derivative}

def git_blob(raw):return sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def certify(reports,parts=32):
    if not isinstance(parts,int) or parts<1 or parts>4096:raise ValueError('Invalid rational partition')
    verified=verify_original_files(Path(__file__).parent)
    verified.update(verified_original_sources())
    original=certify_cells(reports)
    if original['cell_count']!=7 or original['closed_radius_domain']!=['1/64','1/32']:
        raise AssertionError('Unexpected physical radial cover')
    expr,psf,slope=original_bn_affine()
    if sp.diff(expr,psf,2)!=0 or slope.has(psf):raise AssertionError('Affine identity failed')
    cells=[];upper=[];lower=[]
    for idx,row in enumerate(original['cells']):
        a,b=map(F,row['r']);leaves=[]
        for j in range(parts):
            lo=a+(b-a)*j/parts;hi=a+(b-a)*(j+1)/parts
            box=mean_value_slope(lo,hi,reports)
            v=box['mean_value']
            if v.hi>=0:
                raise ArithmeticError(f'BN/pSf slope INCOMPLETE cell={idx} subcell={j} upper={v.hi}')
            l,u=F(v.lo,10**28),F(v.hi,10**28)
            leaves.append({'r':[str(lo),str(hi)],'J':[str(l),str(u)]})
            lower.append(l);upper.append(u)
        cells.append({'original_r':row['r'],'leaves':leaves})
    return {
        'step':'68ad-C2d2e-Step60-BN-pSf-transversality',
        'source_git_blobs':verified,
        'original_report_git_blobs':original['pinned_original_report_git_blobs'],
        'exact_identity':'BN=B0+J*pSf; J=d(BN)/d(pSf); d2(BN)/d(pSf)^2=0, for original Step60 third_free_BN_on_Fz',
        'proof_method':'Original Step60 symbolic affine differentiation plus outward rational interval AD and mean-value theorem for J(r) on each closed rational subcell',
        'cells':cells,'original_cells':len(cells),'subcells':len(upper),
        'max_J_upper':str(max(upper)),'min_J_lower':str(min(lower)),
        'J_strictly_negative_continuum':all(x<0 for x in upper),
        'BN_zero_on_shell':'NOT_PROVED',
        'Step58_continuum':'INCOMPLETE',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
        'limitations':'J<0 means BN is strictly decreasing in independent pSf on this conditional shell. It neither proves BN=0 on the constrained physical profile nor the Dirac rank, lapse existence, boundary compatibility, 4D dynamics, stability, or observables.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path.cwd());p.add_argument('--out',type=Path,required=True);p.add_argument('--parts',type=int,default=32)
    args=p.parse_args();reports=load_pinned(args.repo/'research'/'reports')
    result=certify(reports,args.parts)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'subcells':result['subcells'],'max_J_upper':result['max_J_upper'],
       'J_negative':result['J_strictly_negative_continuum'],'out':str(args.out)}))
if __name__=='__main__':main()

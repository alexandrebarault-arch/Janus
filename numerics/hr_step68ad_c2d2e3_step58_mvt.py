"""Correlated rigorous MVT bounds for the authentic Step58 zeroth lapse coefficients.

Scope: the regular positive-K Step68o shell and authenticated Step68v/68ac/B2
center tubes. Uses a fourth radial jet inferred from the ORIGINAL Step55 ODE.
A failed enclosure is INCOMPLETE, not a counterexample. No Dirac rank claim.
"""
from __future__ import annotations
from contextlib import contextmanager
from fractions import Fraction as F
from pathlib import Path
from . import hr_step68n_interval_ode_jets as jets
from . import hr_step55_global_barrier as old
from . import hr_step68o_temporal_interval_annulus as annulus
from .hr_step68ad_c2b_center_boxes import load_pinned,validate_reports,Q,certify_cells
from .hr_step68ad_c2d2a_temporal_replay import box_for_rounded_s,validated_s_jet,verify_original_files
from .hr_step68ad_c2d2b_executed_temporal_probe import factored_compiled
from .hr_step68ad_c2d2d_correlated_mean_value import Dual
from .hr_step58_temporal_operator import physical_operator
from .hr_step45_exact_physical_ward import exact_physical_ward

I=jets.I

@contextmanager
def fourth_jet_order():
    previous=jets.K
    jets.K=4
    try: yield
    finally: jets.K=previous


def canonical_jets4(lo,hi,reports):
    """Extend authentic Step68o formulas by one radial Taylor order.

    The Step55 equation U_s=(G-2U)/(2s) supplies U_ssss/24 as
    coefficient 3 of RHS divided by 4. All computations outward interval.
    """
    lo,hi=F(lo),F(hi)
    if not F(0)<lo<=hi<=F(1,32): raise ValueError('Outside physical chart')
    R=I.hull(lo,hi); si=R**2
    box=box_for_rounded_s(reports,si,{'r':[str(lo),str(hi)]},Q,validate_reports)
    Jet=jets.Jet
    uj=validated_s_jet(box,Jet,I)
    if len(uj.a)!=5: raise AssertionError('Must use fourth-order jet')
    sj=Jet([si,I.c(1)])
    # The t^3 coefficient of RHS does NOT depend on U_ssss, because
    # G(s,U) contains U but no U derivatives.
    ode_rhs=(jets.jet_G(sj,uj)-2*uj)/(2*sj)
    uj.a[4]=ode_rhs.a[3]/4
    us,uss,usss,ussss=uj.a[1],2*uj.a[2],6*uj.a[3],24*uj.a[4]
    u=Jet([uj.a[0],2*R*us,us+2*R**2*uss,
           2*R*uss+F(4,3)*R**3*usss,
           uss/2+2*R**2*usss+F(2,3)*R**4*ussss])
    rr=Jet([R,I.c(1)]); s=rr**2
    ge=jets.jet_geometry(s); gv=jets.jet_G(s,u)
    c={name:Jet(getattr(old,name)) for name in ('MG','MF','KG','KF','Z1','M2')}
    mg,mf,kg,kf,z1=(c[x] for x in ('MG','MF','KG','KF','Z1'))
    lg,lf=ge['Lg0'],ge['Lf0']
    Ffac=u/(2*mf*lf*ge['Sfr0'])
    betaf=(1+kf**2*s).sqrt()
    rhof=-(u*u/(4*mf*lf)-Ffac*(-s*ge['Dbar']+lf*gv)-mf*lf**3*ge['Rf']/2+s*z1*ge['Dbar']/lf+ge['Wfbar'])/(betaf+s*Ffac*kf*lf)
    psf=(-s*ge['Dbar']+lf*gv-rhof*s*ge['tf0'])/ge['Sfr0']
    data={'Lg':lg,'pLg':s*ge['Gmom'],'Sg':rr*lg,'pSg':rr*ge['Psg0'],
          'tg':Jet(0),'pg':s*ge['Rhog'],'Lf':lf,'pLf':s*u,'Sf':rr*lf,
          'pSf':rr*psf,'tf':Jet(0),'pf':s*rhof}
    for name,k,metric in (('tg',kg,lg),('tf',kf,lf)):
        tp=rr*k*metric
        data[name]=Jet([I.c(0),tp.a[0],tp.a[1]/2,tp.a[2]/3,tp.a[3]/4])
    return data,uj,box


def original_step58_duals(lo,hi,reports):
    with fourth_jet_order():
        canonical,uj,box=canonical_jets4(lo,hi,reports)
        o=physical_operator();p=exact_physical_ward()
        vals={}
        for keys,degree in ((o['q'],0),(o['qp'],1),(o['qpp'],2),(o['qppp'],3)):
            for sym,name in zip(keys,p['Q']):
                fac=(1,1,2,6)[degree]
                der=(1,2,6,24)[degree]
                vals[sym]=Dual(canonical[name].a[degree]*fac,canonical[name].a[degree+1]*der)
        for sym in o['q4']: vals[sym]=Dual(0)
        R=I.hull(lo,hi)
        for name,value,der in (('z',R*old.Z1,old.Z1),('zr',old.Z1,0),('zrr',0,0),('zrrr',0,0)):
            vals[o[name]]=Dual(value,der)
        for sym,name in zip(p['parameters'][:8],('MG','MF','M2','B0','B1','B2','B3','B4')):
            vals[sym]=Dual(getattr(old,name))
        return vals,uj,canonical,box


def step58_value_derivative(lo,hi,reports,compiled=None):
    vals,uj,canonical,box=original_step58_duals(lo,hi,reports)
    if compiled is None: _,compiled=factored_compiled()
    out={}
    for name,(syms,fn) in compiled.items():
        missing=[str(x) for x in syms if x not in vals]
        if missing:raise ValueError('Missing original jets: '+str(missing))
        v=fn(*[vals[s] for s in syms]);v=v[0] if isinstance(v,list) and len(v)==1 else v
        out[name]=Dual.c(v)
    return out


def mean_value_step58(lo,hi,reports,compiled=None):
    lo,hi=F(lo),F(hi);mid=(lo+hi)/2
    center=step58_value_derivative(mid,mid,reports,compiled)
    derivative=step58_value_derivative(lo,hi,reports,compiled)
    h=I.hull(-(hi-lo)/2,(hi-lo)/2)
    return {name:{'center':center[name].v,'derivative':derivative[name].d,
                  'mean_value':center[name].v+h*derivative[name].d}
            for name in ('N','M')}



def certified_step58_continuum(reports, initial_parts=32, max_extra_depth=3):
    """Adaptive rational partition. A failed sign is bisected, never accepted.

    An interval bound is valid for the whole subcell because the physical
    Step55 solution is C^4 and the fourth radial jet follows its exact ODE.
    """
    if initial_parts<1 or initial_parts>1024 or max_extra_depth<0 or max_extra_depth>10:
        raise ValueError('Invalid rational grid')
    original=certify_cells(reports)
    if original['cell_count']!=7 or original['closed_radius_domain']!=['1/64','1/32']:
        raise AssertionError('Unexpected original radial domain')
    verified=verify_original_files(Path(__file__).parent)
    annulus.certify_sources();verified.update(annulus.verified_sources())
    _,compiled=factored_compiled()
    cells=[];worst_n=None;worst_m=None;num_extra=0
    def check(lo,hi,depth):
        nonlocal num_extra,worst_n,worst_m
        bounds=mean_value_step58(lo,hi,reports,compiled)
        n=bounds['N']['mean_value'];m=bounds['M']['mean_value']
        if n.lo<=0 or m.hi>=0:
            if depth>=max_extra_depth:
                raise ArithmeticError(f'Step58 INCOMPLETE on [{lo},{hi}], N={n}, M={m}')
            num_extra+=1
            mid=(lo+hi)/2
            return check(lo,mid,depth+1)+check(mid,hi,depth+1)
        lower=F(n.lo,old.S);upper=F(m.hi,old.S)
        worst_n=lower if worst_n is None else min(worst_n,lower)
        worst_m=upper if worst_m is None else max(worst_m,upper)
        return [{'r':[str(lo),str(hi)],
                 'N':[str(F(n.lo,old.S)),str(F(n.hi,old.S))],
                 'M':[str(F(m.lo,old.S)),str(F(m.hi,old.S))]}]
    for i,c in enumerate(original['cells']):
        a,b=map(F,c['r']);leaves=[]
        for j in range(initial_parts):
            lo=a+(b-a)*j/initial_parts;hi=a+(b-a)*(j+1)/initial_parts
            leaves+=check(lo,hi,0)
        if leaves[0]['r'][0]!=str(a) or leaves[-1]['r'][1]!=str(b):
            raise AssertionError('Coverage endpoints mismatch')
        for x,y in zip(leaves,leaves[1:]):
            if x['r'][1]!=y['r'][0]:raise AssertionError('Coverage gap')
        cells.append({'r':[str(a),str(b)],'leaves':leaves})
        print(f'Step58 certified original cell {i+1}/7 ({len(leaves)} leaves)',flush=True)
    return {'step':'68ad-C2d2e3','kind':'CONDITIONAL_CONTINUUM_STEP58_ORIGINAL_ZEROTH_LAPSE_COEFFICIENTS',
            'method':'Original Step58 zeroth operator with exact Step68o-shell CSE factorization, fourth radial jets from original Step55 ODE, outward-integer interval forward AD and mean-value theorem on rational cells',
            'physical_sources_git_blobs':verified,
            'physical_reports_git_blobs':original['pinned_original_report_git_blobs'],
            'initial_parts_per_cell':initial_parts,'adaptive_bisections':num_extra,
            'total_leaves':sum(len(x['leaves']) for x in cells),
            'cells':cells,'N_positive_continuum':True,'M_negative_continuum':True,
            'min_N_lower':str(worst_n),'max_M_upper':str(worst_m),
            'covered_r':['1/64','1/32'],
            'hypotheses':['Step55 genuine smooth center branch and original pinned 68v/68ac/B2 enclosures',
              'Step68o positive-K stationary shell, original regular metrics and nonzero interaction denominator',
              'No lapse boundary or full Dirac-rank conclusion'],
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'remaining':'Full Dirac matrix rank, lapse positivity and boundary conditions, K=0/J=0 charts, 4D evolution, stability, observables.'}


def main():
    import argparse,json
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    reports=load_pinned(args.repo/'research/reports')
    result=certified_step58_continuum(reports)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'total_leaves':result['total_leaves'],
        'min_N_lower':result['min_N_lower'],'max_M_upper':result['max_M_upper'],
        'GATE_2B':result['GATE_2B'],'out':str(args.out)}))

if __name__=='__main__':main()

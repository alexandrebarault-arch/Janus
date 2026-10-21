"""Step43 explicit two-stage verification: selftest vs ACTUAL HR provider diagnostic.

--selftest does not import the physical solver. --physical actually builds
Step39 fifth-order profile and evaluates all nine original Poisson coefficients
on it, including two unrelated compact lapse pairs; can take some time.
All findings are NUMERICAL, never a proof of exact Dirac time preservation.
"""
from __future__ import annotations
import argparse
import json
import pathlib
import sys
import numpy as np
from numerics.hr_step43_physical_ward_gate import physical_ward_sample,full_jet_gauss_vs_C


def _polynomial_reference(_w,r):
    K=np.zeros((3,3))
    p=2*r*r+3*r;q=1+r**3
    K[0,0]=4*r+3;K[0,1]=p;K[1,0]=p+3*r*r
    K[1,1]=q;K[2,0]=q
    return K


def _polynomial_smears(r,lo=.2,hi=.7):
    a=r-lo;b=hi-r
    N=a**4*b**4
    Nr=4*a**3*b**4-4*a**4*b**3
    Nrr=12*a*a*b**4-32*a**3*b**3+12*a**4*b*b
    M=N*(1+a)
    return np.array([N,Nr,Nrr]),np.array([M,Nr*(1+a)+N,Nrr*(1+a)+2*Nr])


def selftest():
    site=physical_ward_sample(None,.43,kernel=_polynomial_reference)
    pair=full_jet_gauss_vs_C(None,points=48,kernel=_polynomial_reference,
                              smears=_polynomial_smears)
    if abs(site['C'])>1e-10 or abs(site['W'])>1e-10 or abs(pair['difference'])>1e-14:
        raise ArithmeticError('analytic reference failed: diagnostic unusable')
    return {'step':43,'mode':'SELFTEST_NOT_PHYSICAL','site':site,'pair':pair,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def physical():
    from numerics.hr_step39_highorder_secondary import solve_five_point
    from numerics.hr_step39_cross_oracle import lapse_jets
    w,sol=solve_five_point(scale=.1,degree=4,iterations=6,h=.001)
    sites=[physical_ward_sample(w,r) for r in (.11,.21,.31,.43,.61,.71,.83)]
    compact={}
    for pair,lo,hi in [('A',.2,.7),('B',.25,.73)]:
        compact[pair]=full_jet_gauss_vs_C(w,lo=lo,hi=hi,points=48,
                                         smears=lambda x,p=pair:lapse_jets(x,p))
    return {'step':43,'mode':'PHYSICAL_SIX_PAIR_NUMERICAL_DIAGNOSTIC',
            'source':'original Step33g/37/39 modules from active GitHub worktree',
            'points':sites,'independent_lapse_pairs':compact,
            'max_fit_C_step39':sol['history'][-1]['max_abs_C_sample'],
            'interpretation':'Finite 5-point Ward stencils and 48 Gauss nodes only; not a symbolic HR Ward identity, exact C=0 or Dirac time preservation',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    g=parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--selftest',action='store_true')
    g.add_argument('--physical',action='store_true')
    parser.add_argument('--output',type=pathlib.Path)
    args=parser.parse_args(argv)
    result=selftest() if args.selftest else physical()
    raw=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(raw,encoding='utf-8')
    sys.stdout.write(raw)
    return 0


if __name__=='__main__':raise SystemExit(main())

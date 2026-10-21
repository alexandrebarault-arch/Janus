"""STEP44 original-provider physical mixed-Ward plus independent unintegrated oracle.

Pin source Git blob hashes and refuse silent compatibility adapters. Physical
output is finite-resolution evidence, NEVER a proof of exact secondary or Dirac
constraint preservation. From repository root:

  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step44.py \
      --full --output research/reports/gate2b-step44-physical-verification.json

The full run checks original source, two lapse pairs, four radial grids and
original unintegrated 12-variable nodal Hamiltonian with independent shift.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path
from numerics.hr_curved_moving_dust_primary import build_primary
from numerics.hr_step39_cross_oracle import original_nonibp_extended, lapse_jets
from numerics.hr_step43_physical_ward_gate import physical_ward_sample, full_jet_gauss_vs_C
from numerics.hr_step39_highorder_secondary import solve_five_point

ROOT=Path(__file__).resolve().parents[1]
EXPECTED_BLOBS={
    'numerics/hr_curved_moving_dust_primary.py':'ee801e324ae0282f764e29c2b39ff34b1efb73f1',
    'numerics/hr_curved_primary_mixed_kernel.py':'45ccd73177cc1588efaf1d53e3dd0179d41ec30b',
    'numerics/hr_step37_curved_solver.py':'ce627177d7fa97bad21a7689b292ee24a63930cc',
    'numerics/hr_step37_original_nonibp_oracle.py':'005449ade6e3582e3b9a5c3374a881a77e73e3f6',
    'numerics/hr_step39_cross_oracle.py':'5b66a1fd416cfa0eaaaef7e43601b6a497b8e8c0',
    'numerics/hr_step39_highorder_secondary.py':'0da008cc7d5810235ad1bd73549ef1ac1957f656',
    'numerics/hr_step43_physical_ward_gate.py':'386febaa9b805cf423efd6feb7a8027a2069301b',
}


def git_blob_sha(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def verify_sources(root=ROOT):
    out={}
    for rel,expected in EXPECTED_BLOBS.items():
        path=root/rel
        actual=git_blob_sha(path.read_bytes())
        if actual!=expected:
            raise ValueError(f'original provider mismatch: {rel}: {actual} != {expected}')
        out[rel]=actual
    return out


def richardson(values):
    """Exploratory h²/h⁴ elimination on n=161/321/641(/1281).

    Not a rigorous error bound. Binary float values are converted via exact
    printed decimal to avoid extra cancellation in the extrapolation itself.
    """
    with localcontext() as ctx:
        ctx.prec=45
        b=[Decimal(str(t)) for t in values]
        r2=[(4*b[i+1]-b[i])/3 for i in range(len(b)-1)]
        r4=[(16*r2[i+1]-r2[i])/15 for i in range(len(r2)-1)]
        return {'R2':[float(x) for x in r2], 'R4':[float(x) for x in r4]}


def numerical_physical_report(grids=(161,321,641,1281)):
    verified=verify_sources()
    if any(x<80 or (x-1)%160 for x in grids) or len(grids)<3:
        raise ValueError('grids must be original dyadic 161, 321, 641, 1281...')
    if any(grids[i+1]!=2*grids[i]-1 for i in range(len(grids)-1)):
        raise ValueError('grid spacing must halve at each successive step')
    w,fit=solve_five_point(scale=.1,degree=4,iterations=6,h=.001)
    pairs={}
    for label,lo,hi in [('A',.2,.7),('B',.25,.73)]:
        jets={str(order):full_jet_gauss_vs_C(w,lo=lo,hi=hi,
            points=order,smears=lambda r,p=label:lapse_jets(r,p)) for order in (48,96)}
        nodal=[original_nonibp_extended(w,label,n) for n in grids]
        fit_extrap=richardson([x['bracket'] for x in nodal])
        pairs[label]={'jet_integrals':jets,'original_nonIBP_by_grid':nodal,
                      'richardson_exploratory':fit_extrap,
                      'last_R4_minus_96_gauss':fit_extrap['R4'][-1]-jets['96']['full_jet_bracket']}
    sites={str(r):physical_ward_sample(w,r) for r in (.11,.21,.31,.43,.61,.71,.83)}
    # Deliberately distinct unconstrained-secondary primary families:
    # the Ward near-identities should persist even when C is large.
    primary_variations=[]
    for label,kw in [
        ('uncorrected_same_geometry',dict(curv_g=.0015,curv_f=-.0012,
                  z_slope=.004,theta_g=.0012,theta_f=-.0016,
                  grav_g=0.,grav_f=0.)),
        ('different_curvature_and_gravity',dict(curv_g=.003,curv_f=-.002,
                  z_slope=.006,theta_g=.002,theta_f=-.003,
                  grav_g=.009,grav_f=-.01)),
        ('flat_spatial_noncomoving',dict(curv_g=0.,curv_f=0.,
                  z_slope=.005,theta_g=.002,theta_f=-.001,
                  grav_g=.008,grav_f=-.008))]:
        v=build_primary(**kw)
        samples=[physical_ward_sample(v,r) for r in (.21,.43,.71)]
        primary_variations.append({'label':label,'params':kw,'samples':samples})
    return {
        'step':44,'experiment':'TRUE ORIGINAL PROVIDER PHYSICAL WARD AND INDEPENDENT NON-IBP SIX-PAIR POISSON',
        'provider_byte_pins':verified,
        'test_profile':'h=.001 degree=4, six fifth-order corrections',
        'coefficients':fit['history'][-1]['f_delta'],
        'max_local_C_original_9_heldout':fit['history'][-1]['max_abs_C_sample'],
        'seven_physical_points':sites,
        'independent_smeared_pairs':pairs,
        'off_secondary_primary_variations':primary_variations,
        'limits':['All numerical, finite double precision; Ward near-zero does not imply symbolic identity',
          'Dyadic Richardson intercept is not a rigorous continuum error bound',
          'Original nodal primary constraints have O(dr²) discretization error',
          'No proof pointwise C(r)=0 exactly','No {C,H_total} or lapse fixing computed'],
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true',help='add N=1281 to original N=161,321,641')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(argv)
    r=numerical_physical_report(grids=(161,321,641,1281) if args.full else (161,321,641))
    payload=json.dumps(r,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(payload,encoding='utf-8')
    print(payload)

if __name__=='__main__':main()

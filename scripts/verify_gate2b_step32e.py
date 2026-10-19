"""Reproducible focused Gate2B Step32e verification (not physics/CI)."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE_TESTS=(
 'numerics/hr_full_onshell_tadpole.py','tests/test_hr_full_onshell_tadpole.py',
 'numerics/hr_two_dust_common_time_canonical.py','tests/test_hr_two_dust_common_time_canonical.py',
 'numerics/hr_common_time_metric_rates.py','tests/test_hr_common_time_metric_rates.py',
 'numerics/hr_metric_auxiliary_restricted.py','tests/test_hr_metric_auxiliary_restricted.py',
 'numerics/hr_integrable_metric_time_basis.py','tests/test_hr_integrable_metric_time_basis.py',
 'numerics/hr_integrable_two_dust_phase.py','tests/test_hr_integrable_two_dust_phase.py',
 'scripts/verify_gate2b_step32e.py',
)
TESTS=tuple(p for p in SOURCE_TESTS if p.startswith('tests/'))
# Prior published byte-for-byte Git blob identities (NOT a full Git checkout).
EXPECTED_PUBLISHED={
 'numerics/hr_full_onshell_tadpole.py':'e05d8f54cf4eff76a92c278ffdd971612d1ec56b',
 'numerics/hr_two_dust_common_time_canonical.py':'6b6c8a8e8f5373005ff51cf169b0360fc9caec37',
 'numerics/hr_common_time_metric_rates.py':'c317c3a10af286a03b0d2590775ca83498b10a64',
 'numerics/hr_metric_auxiliary_restricted.py':'de568fa5b64f0195eaad5d60acbaf13996c912f6',
 'numerics/hr_integrable_metric_time_basis.py':'d6d8200ef583c25c232dd79b0e5aba1a206d41e5',
}


def _blob(data):
    import hashlib
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def _git(*args):
    try:
        r=subprocess.run(['git',*args],cwd=ROOT,text=True,check=False,
                         capture_output=True,timeout=6)
        return r.stdout.strip() if r.returncode==0 else None
    except (FileNotFoundError,subprocess.TimeoutExpired):return None


def main():
    missing=[p for p in SOURCE_TESTS if not (ROOT/p).is_file()]
    if missing:raise SystemExit('Missing exact focused files: '+', '.join(missing))
    blob={p:_blob((ROOT/p).read_bytes()) for p in SOURCE_TESTS}
    mismatches={p:{'expected':sha,'actual':blob[p]} for p,sha in EXPECTED_PUBLISHED.items()
                if sha!=blob[p]}
    if mismatches:raise SystemExit('Previously published source mismatch: '+str(mismatches))
    git_root=_git('rev-parse','--show-toplevel')
    git_checkout=git_root is not None and Path(git_root).resolve()==ROOT
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    r=subprocess.run([sys.executable,'-m','pytest','-q',*TESTS],cwd=ROOT,
                     env=env,capture_output=True,text=True,check=False)
    data={
     'step':'32e-FULLY-INTEGRABLE-COMPACT-METRIC-AND-DUAL-DUST-PHASE-FIELDS',
     'gate2b':'OPEN',
     'scientific_background':'radiation-free-Candidate-C-PHYSICALLY-HOMOGENEOUS-on-shell',
     'physically_nonhomothetic_on_shell_solution':'NOT_FOUND',
     'all_18_compact_parent_fields_time_integrable':r.returncode==0,
     'true_hamiltonian_ADM_auxiliary_constraints':'NOT_DERIVED',
     'HR_time_dependent_BD_null':'NOT_DERIVED',
     'DeFelice_physical_scalar_oracle':'NOT_RUN',
     'Aoki_physical_scalar_oracle':'NOT_RUN',
     'scalar_ghost_gradient_fold_physical_verdict':'NOT_DERIVED',
     'full_repository_regression':False,
     'workspace_origin':'git_checkout' if git_checkout else 'focused_non_git_workspace',
     'git_head':_git('rev-parse','HEAD') if git_checkout else None,
     'python':sys.version.split()[0],
     'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCE_TESTS},
     'git_blob_sha1':blob,
     'previously_published_exact_blob_mismatches':mismatches,
     'tests_exit_code':r.returncode,
     'tests_output':(r.stdout+r.stderr)[-4000:].strip(),
    }
    if r.returncode==0:
        import numpy as np
        sys.path.insert(0,str(ROOT))
        from numerics.hr_full_onshell_tadpole import Trajectory,CG,CF
        from numerics.hr_integrable_two_dust_phase import (
            first_variations,analytic_integrable_pair_block,
            finite_canonical_pair_block,phase_integration_by_parts,action
        )
        from numerics.hr_integrable_metric_time_basis import action as old
        bg=Trajectory.solve(width=.04)
        grad=first_variations(trajectory=bg,quadrature_order=20,step=2e-5)
        H=finite_canonical_pair_block(trajectory=bg,quadrature_order=20,step=.009)
        ref=analytic_integrable_pair_block(quadrature_order=20)
        old_grad=[]
        for j in (6,13):
            v=np.zeros(18);v[j]=2e-5
            old_grad.append(float((old(v,trajectory=bg,quadrature_order=20).total-
                        old(-v,trajectory=bg,quadrature_order=20).total)/(4e-5)))
        left,right=phase_integration_by_parts(charge=CG,theta_amp=.2,
                                 theta_extra=.3,p_amp=.25)
        data.update({
            'tests_passed_count':len(TESTS), # number of TEST FILES, not pytest functions
            'focused_test_files':len(TESTS),
            'all_18_compact_first_variations_max_abs':float(np.max(np.abs(grad))),
            'new_two_dust_phase_parent_first_variations':grad[[6,13]].tolist(),
            'old_disconnected_two_dust_rate_first_variations':old_grad,
            'integrable_projected_canonical_block':H.tolist(),
            'projected_canonical_rank':int(np.linalg.matrix_rank(H,tol=1e-8)),
            'projected_canonical_block_error_max':float(np.max(np.abs(H-ref))),
            'single_dust_compact_time_IBP_difference':float(left-right),
            'two_dust_symplectic_pairs_preserved':bool(np.linalg.matrix_rank(H,tol=1e-8)==2),
        })
        # The field counts are not the count of test functions; derive from pytest.
        import re
        match=re.search(r'(\d+) passed',r.stdout)
        data['tests_passed_count']=int(match.group(1)) if match else None
    else:
        data['tests_passed_count']=0
    s=json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)
    print(s)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(s+'\n',encoding='utf-8')
    return r.returncode

if __name__=='__main__':raise SystemExit(main())

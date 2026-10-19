"""Step32c reproducible 71-test RESTRICTED auxiliary Schur regression.

A finite Galerkin 4x4 inverse is NOT a physical ADM/BD reduction.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,json,os,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
FILES=(
 'numerics/hr_full_onshell_tadpole.py','tests/test_hr_full_onshell_tadpole.py',
 'numerics/hr_two_dust_common_time_canonical.py','tests/test_hr_two_dust_common_time_canonical.py',
 'numerics/hr_common_time_metric_rates.py','tests/test_hr_common_time_metric_rates.py',
 'numerics/hr_metric_auxiliary_restricted.py','tests/test_hr_metric_auxiliary_restricted.py',
 'scripts/verify_gate2b_step32c.py',
)
TARGETS=(
 'tests/test_hr_full_onshell_tadpole.py',
 'tests/test_hr_two_dust_common_time_canonical.py',
 'tests/test_hr_common_time_metric_rates.py',
 'tests/test_hr_metric_auxiliary_restricted.py',
)

def main():
    missing=[f for f in FILES if not (ROOT/f).is_file()]
    if missing:raise SystemExit('Missing targeted source: '+', '.join(missing))
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    p=subprocess.run([sys.executable,'-m','pytest','-q',*TARGETS],cwd=ROOT,env=env,
        capture_output=True,text=True,check=False)
    data={
        'step':'32c-RESTRICTED-GALERKIN-FOUR-AUXILIARY-SCHUR',
        'gate2b':'OPEN','full_repository_regression':False,
        'workspace_origin':'focused_exact_step31_step32a_step32b_sources_no_complete_git_checkout',
        'on_shell_background':'HOMOGENEOUS-dust-only-no-radiation-CandidateC',
        'genuine_nonhomothetic_background_on_shell':False,
        'restricted_4x4_auxiliary_schur_tested':p.returncode==0,
        'true_canonical_ADM_constraints_reduced':False,
        'time_dependent_BD_null_reduced':False,
        'time_integrable_metric_rate_trial_basis':False,
        'de_felice_physical_oracle':'NOT_RUN',
        'aoki_physical_oracle':'NOT_RUN',
        'physical_kinetic_ghost_speeds_fold':'NOT_DERIVED',
        'python':sys.version.split()[0],
        'files_sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in FILES},
        'tests_exit_code':p.returncode,
        'tests_output':(p.stdout+p.stderr)[-4000:].strip(),
    }
    if p.returncode==0:
        sys.path.insert(0,str(ROOT))
        from numerics.hr_metric_auxiliary_restricted import restricted_auxiliary_schur
        import numpy as np
        result=restricted_auxiliary_schur(step=.012,quadrature_order=20)
        data.update({
            'result':'RESTRICTED_4_AUXILIARY_SCHUR_ALGEBRA_GREEN_ONLY',
            'full_trial_hessian_shape':list(result.hessian.shape),
            'restricted_auxiliary_indices':[0,1,7,8],
            'restricted_auxiliary_matrix':result.auxiliary.tolist(),
            'restricted_auxiliary_eigenvalues':np.linalg.eigvalsh(result.auxiliary).tolist(),
            'restricted_auxiliary_condition':result.condition,
            'restricted_auxiliary_rank':result.auxiliary_rank,
            'algebraic_schur_shape':list(result.schur.shape),
            'canonical_dust_symplectic_rank':int(np.linalg.matrix_rank(result.symplectic,tol=1e-8)),
            'dust_momentum_phase_rate_block':result.symplectic.tolist(),
            'restricted_schur_is_physical_kinetic':'NO',
            'restriction_reason':'Metric rate jets not integrable compact fields; gauge/ADM/BD constraint basis incomplete.',
        })
    else:data['result']='FAILED'
    report=json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)
    print(report)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(report+'\n',encoding='utf-8')
    return p.returncode

if __name__=='__main__':raise SystemExit(main())

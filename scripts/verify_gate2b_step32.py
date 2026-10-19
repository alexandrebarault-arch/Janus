"""Step32 focused reproducible 49-test canonical two-dust acceptance runner.

Explicitly records that 14x14 is UNREDUCED, and metric velocity/BD and
both physical scalar acceptance oracles remain OPEN. No independent full
GitHub checkout/CI claim is made.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,json,os,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
FILES=(
 'numerics/hr_full_onshell_tadpole.py',
 'tests/test_hr_full_onshell_tadpole.py',
 'numerics/hr_two_dust_common_time_canonical.py',
 'tests/test_hr_two_dust_common_time_canonical.py',
 'scripts/verify_gate2b_step32.py',
)

def main():
    missing=[p for p in FILES if not (ROOT/p).is_file()]
    if missing:raise SystemExit('missing exact source: '+', '.join(missing))
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    proc=subprocess.run([sys.executable,'-m','pytest','-q',
        'tests/test_hr_full_onshell_tadpole.py',
        'tests/test_hr_two_dust_common_time_canonical.py'],
        cwd=ROOT,env=env,capture_output=True,text=True,check=False)
    # Import as genuinely tested sources, but only when test run succeeded.
    sys.path.insert(0,str(ROOT))
    from numerics.hr_two_dust_common_time_canonical import (
        analytic_canonical_pair_integrals,kinetic_pair_block,derivative,
        full_preconstraint_hessian, ORDER)
    import numpy as np
    if proc.returncode==0:
        ana=analytic_canonical_pair_integrals(quadrature_order=20)
        H=full_preconstraint_hessian(quadrature_order=20)
        K=H[np.ix_([5,12],[6,13])]
        max_field_grad=float(max(abs(derivative(i)) for i in
                        (0,1,2,3,4,5,7,8,9,10,11,12)))
        row_nonzero=[[int(j),float(H[i,j])] for i in (6,13)
                     for j in range(14) if abs(H[i,j])>1e-11]
    else:
        ana=np.full((2,2),float('nan'));K=ana.copy()
        max_field_grad=float('nan');row_nonzero=[]
    report={
      'gate2b':'OPEN',
      'step':'32-EXACT-CANONICAL-TWO-DUST-PAIRS-PRECONSTRAINT',
      'science_verdict':'CANONICAL_TWO_DUST_BRIDGE_GREEN' if proc.returncode==0 else 'FAILED',
      'physical_background':'radiation_free_CandidateC_HOMOGENEOUS_on_shell_only',
      'genuine_nonhomothetic_on_shell_background':False,
      'time_dependent_metric_velocities_independent':False,
      'metric_auxiliaries_reduced':False,
      'bd_null_mode_reduced':False,
      'de_felice_physical_oracle':'NOT_RUN',
      'aoki_physical_oracle':'NOT_RUN',
      'first_relative_mu_fold':'NOT_RUN',
      'full_repo_test_suite':False,
      'workspace_origin':'focused_exact_step31_plus_step32_modules_NOT_complete_git_clone',
      'python':sys.version.split()[0],
      'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in FILES},
      'tests_exit_code':proc.returncode,
      'tests_stdout':(proc.stdout+proc.stderr)[-6000:].strip(),
      'amplitude_order':list(ORDER),
      'dust_canonical_p_phase_rate_block':K.tolist(),
      'analytic_pair_block':ana.tolist(),
      'dust_pair_rank':int(np.linalg.matrix_rank(K,tol=1e-8)),
      'compact_field_tadpole_max_abs':max_field_grad,
      'phase_rate_rows_nonzero_entries':row_nonzero,
    }
    text=json.dumps(report,indent=2,sort_keys=True,ensure_ascii=False)
    print(text)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(text+'\n',encoding='utf-8')
    return proc.returncode

if __name__=='__main__':raise SystemExit(main())

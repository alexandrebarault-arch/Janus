"""Reproducible 60-test Step32b: 2 dust pairs AND 4 native EH metric rates.

Still preconstraint and on a homogeneous on-shell dust-only Candidate-C
background; BD, genuinely nonhomothetic backgrounds, both physical
stability oracles and first relative-mu fold are NOT yet tested.
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
 'numerics/hr_common_time_metric_rates.py',
 'tests/test_hr_common_time_metric_rates.py',
 'scripts/verify_gate2b_step32b.py',
)

def main():
    missing=[f for f in FILES if not (ROOT/f).is_file()]
    if missing:raise SystemExit('missing prerequisite source: '+', '.join(missing))
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    p=subprocess.run([sys.executable,'-m','pytest','-q',
        'tests/test_hr_full_onshell_tadpole.py',
        'tests/test_hr_two_dust_common_time_canonical.py',
        'tests/test_hr_common_time_metric_rates.py'],
        cwd=ROOT,env=env,capture_output=True,text=True,check=False)
    data={
        'gate2b':'OPEN',
        'step':'32b-TWO-DUST-CANONICAL-FOUR-EH-METRIC-RATE-JETS',
        'workspace_origin':'focused_exact_step31_and_step32_files_not_complete_git_checkout',
        'full_repository_regression':False,
        'homogeneous_background_is_on_shell_dust_only':True,
        'genuine_nonhomothetic_background_on_shell':False,
        'metric_lapse_shift_auxiliaries_reduced':False,
        'time_dependent_bd_null_reduced':False,
        'de_felice_physical_oracle':'NOT_RUN',
        'aoki_physical_oracle':'NOT_RUN',
        'physical_ghost_speed_fold_verdict':'NOT_DERIVED',
        'python':sys.version.split()[0],
        'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in FILES},
        'tests_exit_code':p.returncode,
        'tests_output':(p.stdout+p.stderr)[-6000:].strip(),
    }
    if p.returncode==0:
        sys.path.insert(0,str(ROOT))
        from numerics.hr_two_dust_common_time_canonical import analytic_canonical_pair_integrals
        from numerics.hr_common_time_metric_rates import analytic_background_rate_hessian,extra_rate_hessian
        import numpy as np
        matter=analytic_canonical_pair_integrals(quadrature_order=20)
        rate=analytic_background_rate_hessian(quadrature_order=20)
        numeric=extra_rate_hessian(quadrature_order=20,step=.03)
        data.update({
            'result':'METRIC_RATE_JETS_PRECONSTRAINT_GREEN_TWO_MATTER_PAIRS_GREEN',
            'matter_pair_rank':int(np.linalg.matrix_rank(matter,tol=1e-8)),
            'matter_symplectic_block':matter.tolist(),
            'metric_rate_unreduced_block':rate.tolist(),
            'max_abs_rate_quadratic_vs_independent_analytic':float(np.max(np.abs(rate-numeric))),
            'metric_rate_block_is_physical_kinetic':'NO',
        })
    else:data['result']='FAILED'
    s=json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)
    print(s)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(s+'\n',encoding='utf-8')
    return p.returncode

if __name__=='__main__':raise SystemExit(main())

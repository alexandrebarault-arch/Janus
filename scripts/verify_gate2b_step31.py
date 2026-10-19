"""Reproducible Gate2B step31 common-chart full 12-field action test runner.

Exact fresh verification of the named targeted suite only. Historical steps
and external physical scalar oracles MUST NOT be counted as passed here.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
FILES=('numerics/hr_full_onshell_tadpole.py',
       'tests/test_hr_full_onshell_tadpole.py',
       'scripts/verify_gate2b_step31.py')


def main():
    import numpy as np
    if not all((ROOT/f).is_file() for f in FILES):
        raise SystemExit('missing one or more exact-source files')
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    p=subprocess.run([sys.executable,'-m','pytest','-q','tests/test_hr_full_onshell_tadpole.py'],
           cwd=ROOT,capture_output=True,text=True,env=env,check=False)
    sys.path.insert(0,str(ROOT))
    from numerics.hr_full_onshell_tadpole import action,gradient,ORDER,background,metric_physical_witness
    grad=gradient(step=2e-5) if p.returncode==0 else np.full(12,float('nan'))
    metadata={
      'gate':'GATE_2B_OPEN',
      'step':'31-on-shell-homogeneous-common-chart-full-spherical-scalar-tadpoles',
      'verdict':'HOMOGENEOUS_12_FIELD_TADPOLES_GREEN_ONLY' if p.returncode==0 else 'TEST_FAILURE',
      'on_shell_genuinely_nonhomothetic_background':False,
      'full_repo_test_suite':False,
      'historical_test_suites_rerun':False,
      'de_felice_physical_oracle':'NOT_RUN',
      'aoki_physical_oracle':'NOT_RUN',
      'bd_constraint_reduced':'NO',
      'workspace_origin':'standalone_focused_workspace',
      'python':sys.version.split()[0],
      'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in FILES},
      'tests_exit_code':p.returncode,
      'tests_output':(p.stdout+p.stderr)[-4000:].strip(),
      'gradient_field_order':list(ORDER),
      'gradient':np.asarray(grad).tolist(),
      'max_abs_tadpole':float(np.max(np.abs(grad))),
      'action_components':action().contributions.tolist(),
      'on_shell_background_a0_4':np.asarray(background(.4)).tolist(),
      'independent_f_psi_witness':list(metric_physical_witness()),
    }
    text=json.dumps(metadata,sort_keys=True,indent=2,ensure_ascii=False)
    print(text)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(text+'\n',encoding='utf-8')
    return p.returncode

if __name__=='__main__':raise SystemExit(main())

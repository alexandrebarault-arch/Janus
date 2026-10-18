"""Run exactly the Step30 on-shell coordinate-compensation acceptance gate.

This does NOT certify a new nonhomothetic physical solution or the
JANUS Gate2B constrained-scalar research milestones.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import os

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
SOURCE='numerics/hr_compensated_native_chart.py'
TEST='tests/test_hr_compensated_native_chart.py'


def _git(*args):
    try:
        p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,text=True,
                         check=False,timeout=5)
        return p.stdout.strip() if p.returncode==0 else None
    except (FileNotFoundError,subprocess.TimeoutExpired):return None


def main():
    paths=[SOURCE,TEST,'scripts/verify_gate2b_step30.py']
    missing=[p for p in paths if not (ROOT/p).is_file()]
    if missing:raise SystemExit(f'missing required source files: {missing}')
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    git_root=_git('rev-parse','--show-toplevel')
    clean_git=git_root is not None and Path(git_root).resolve()==ROOT
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    p=subprocess.run([sys.executable,'-m','pytest','-q',TEST],cwd=ROOT,
                     env=env,capture_output=True,text=True,check=False)
    count=re.search(r'(\d+) passed',p.stdout+p.stderr)
    record={
       'step':30,
       'science_result':'EXACT_COORDINATE_COMPENSATION_IS_PURE_RELABELING',
       'on_shell_nonhomothetic_relative_mode':'NOT_DERIVED',
       'scalar_constraints_and_BD':'NOT_RUN',
       'candidate_fold_crossing':'NOT_RUN',
       'de_felice_oracle':'NOT_RUN',
       'aoki_oracle':'NOT_RUN',
       'gate2b':'OPEN',
       'full_repository_regression':False,
       'previous_step29_tests_rerun':False,
       'workspace_origin':'git_worktree' if clean_git else 'standalone_focused_workspace',
       'git_head':_git('rev-parse','HEAD') if clean_git else None,
       'git_dirty':bool(_git('status','--porcelain')) if clean_git else None,
       'python':sys.version.split()[0],
       'sha256':hashes,
       'tests_exit_code':p.returncode,
       'tests_passed':int(count.group(1)) if count else 0,
       'pytest_tail':(p.stdout+p.stderr).strip()[-2500:],
    }
    if p.returncode==0:
        from numerics.hr_compensated_native_chart import (HomogeneousDustTrajectory,Chart,
            compact_g_lapse_tadpole,physical_f_metric,native_compensated_f,
            pull_native_to_common,direct_g_lapse_residual,uncompensated_native_flrw)
        bg=HomogeneousDustTrajectory.solve();chart=Chart()
        t,r=0.,.2
        T,R,J,D=chart.forward(t,r)
        z=native_compensated_f(T,R,bg,chart)
        f,af=pull_native_to_common(z['native'],z['angular'],J)
        diag,area=uncompensated_native_flrw(T,R,bg,chart)
        wrong,wrong_area=pull_native_to_common(diag,area,J)
        record['witness']={
            'a':bg.at(0.)['a'],
            'radius':r,
            'lambda':chart.lam0,
            'sigma':chart.sig0,
            'native_f_shift_offdiagonal':float(z['native'][0,1]),
            'corrected_g_lapse_residual':direct_g_lapse_residual(bg.at(0.),r,f,af),
            'scale_only_g_lapse_residual':direct_g_lapse_residual(bg.at(0.),r,wrong,wrong_area),
            'compact_time_radial_g_lapse_tadpole_compensated':compact_g_lapse_tadpole(bg,chart,order=20),
            'compact_time_radial_g_lapse_tadpole_scale_only':compact_g_lapse_tadpole(bg,chart,order=20,scale_only=True),
        }
    s=json.dumps(record,indent=2,sort_keys=True,ensure_ascii=False)
    print(s)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(s+'\n',encoding='utf-8')
    return p.returncode

if __name__=='__main__':raise SystemExit(main())

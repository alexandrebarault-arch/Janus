"""One-command Step29 focused obstruction/reproducibility manifest.

Usage: python scripts/verify_gate2b_step29.py [result.json]
Does not claim a clean full repository test or a physical viability verdict.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
TARGET='tests/test_hr_nonhomothetic_center_obstruction.py'
SOURCE='numerics/hr_nonhomothetic_center_obstruction.py'


def _git(*args):
    try:
        proc=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,
                            text=True,check=False,timeout=6)
    except (FileNotFoundError,subprocess.TimeoutExpired):
        return None
    return proc.stdout.strip() if proc.returncode==0 else None


def main():
    if not (ROOT/TARGET).is_file() or not (ROOT/SOURCE).is_file():
        raise SystemExit('missing mandatory Step29 source or test file')
    manifest={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
              for path in (SOURCE,TARGET,'scripts/verify_gate2b_step29.py')}
    gitroot=_git('rev-parse','--show-toplevel')
    checkout=bool(gitroot and Path(gitroot).resolve()==ROOT)
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    test=subprocess.run([sys.executable,'-m','pytest','-q',TARGET],cwd=ROOT,
                        env=env,text=True,capture_output=True,check=False)
    output=(test.stdout+test.stderr).strip()
    match=re.search(r'(?P<n>\d+) passed',output)
    if test.returncode==0:
        sys.path.insert(0,str(ROOT))
        from numerics.hr_nonhomothetic_center_obstruction import (
            snapshot_on_homogeneous_g_constraint,center_g_lapse_source,
            central_linearized_chart_sensitivity,compact_g_lapse_first_variation)
        q=snapshot_on_homogeneous_g_constraint(
            a=.4,y=.5787707228025044,Nf=.5185264338279018)
        center=center_g_lapse_source(q,radial_scale=.78)
        witness={
          'a':.4,'radial_scale_lambda':.78,'original_lapse_residual':center.g_lapse_original,
          'naive_mapped_lapse_residual':center.g_lapse_mapped,
          'linearized_lambda_sensitivity_at_one':central_linearized_chart_sensitivity(q),
          'compact_lapse_variation_radius_0p035':compact_g_lapse_first_variation(
              q,support_radius=.035,radial_scale=.78),
        }
    else:
        witness=None
    report={
       'gate':'Step29 naive homogeneous Candidate-C dust-only background substitution',
       'status':'NAIVE_INSERTION_FAIL_NEEDS_BACKGROUND_RESOLUTION',
       'full_nonhomothetic_onshell_action':'NOT_DERIVED',
       'gate2b':'OPEN','JANUS_R_validated':False,
       'physical_oracles':{'DeFelice':'NOT_RUN','Aoki':'NOT_RUN'},
       'full_repository_regression':False,
       'workspace_origin':'git_checkout' if checkout else 'standalone_focused_workspace',
       'git_head':_git('rev-parse','HEAD') if checkout else None,
       'git_worktree_dirty':bool(_git('status','--porcelain')) if checkout else None,
       'python':sys.version.split()[0],
       'sha256':manifest,
       'test_exit_code':test.returncode,
       'tests_passed':int(match.group('n')) if match else 0,
       'tests_output':output[-4000:],
       'witness':witness,
    }
    result=json.dumps(report,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    print(result)
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(result,encoding='utf-8')
    return test.returncode

if __name__=='__main__':
    raise SystemExit(main())

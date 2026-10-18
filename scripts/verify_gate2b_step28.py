"""Focused background-only Step28 reproducibility runner.

Runs 17 new tests, NOT the earlier 75 tests or full repository tests.
It records source hashes, git checkout status, numerical environment and
explicit limits of the on-shell homogeneous dust-only Candidate-C gate.
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
FILES=('numerics/hr_minisuperspace_onshell.py',
       'tests/test_hr_minisuperspace_onshell.py')


def _git(*args):
    try:
        r=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,
                         text=True,timeout=8)
    except (FileNotFoundError,subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode==0 else None


def main():
    missing=[p for p in FILES if not (ROOT/p).is_file()]
    if missing:
        raise SystemExit('missing Step28 files: '+', '.join(missing))
    gitroot=_git('rev-parse','--show-toplevel')
    is_git=gitroot is not None and Path(gitroot).resolve()==ROOT
    cmd=[sys.executable,'-m','pytest','-q',str(ROOT/FILES[1])]
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    result=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True)
    output=(result.stdout+result.stderr).strip()
    m=re.search(r'(\d+) passed',output)
    info={
       'title':'JANUS Gate2B Step28 exact minisuperspace background/tadpoles',
       'test_scope':'NEW 17 TESTS ONLY; earlier 75 were not rerun in this workspace',
       'tests_return_code':result.returncode,
       'tests_passed':int(m.group(1)) if m else 0,
       'test_output':output[-5000:],
       'python':sys.version.split()[0],
       'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in FILES},
       'workspace_origin':'verified_git_checkout' if is_git else 'standalone_focused_workspace',
       'git_head':_git('rev-parse','HEAD') if is_git else None,
       'git_dirty':bool(_git('status','--porcelain')) if is_git else None,
       'physical_stability_oracles':{'DeFelice':'NOT_RUN','Aoki':'NOT_RUN'},
       'radiation_sector':'REMOVED_FOR_DUST_ONLY_BENCHMARK',
       'full_nonhomothetic_five_sector_candidate_c':'NOT_ASSEMBLED_ON_SHELL',
       'full_repository_regression':False,
       'gate2b':'OPEN',
    }
    doc=json.dumps(info,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    print(doc)
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(doc,encoding='utf-8')
    return result.returncode

if __name__=='__main__':
    raise SystemExit(main())

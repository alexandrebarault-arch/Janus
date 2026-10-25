"""Safe job deadlines and recoverable state, including resistant grandchildren."""
import json
from pathlib import Path
import sys
import subprocess
import time

WRAPPER = Path(__file__).resolve().parents[1] / 'scripts' / 'janus_bounded_job.py'


def launch(tmp_path, name, seconds, cmd):
    state = tmp_path / (name + '.json')
    log = tmp_path / (name + '.log')
    proc = subprocess.run([sys.executable, str(WRAPPER),
        '--timeout-seconds', str(seconds), '--grace-seconds', '0.1',
        '--state', str(state), '--log', str(log), '--label', name,
        '--', *cmd], check=False, capture_output=True, text=True, timeout=12)
    return proc, json.loads(state.read_text()), log.read_text()


def test_pass(tmp_path):
    p,s,log=launch(tmp_path, 'pass', 2,
                   [sys.executable,'-c','print("CALC_OK")'])
    assert p.returncode==0 and s['status']=='PASSED' and s['exit_code']==0
    assert 'CALC_OK' in log and s['finished_at_utc']


def test_nonzero_exit_retained(tmp_path):
    p,s,log=launch(tmp_path,'fail',2,
                   [sys.executable,'-c','raise SystemExit(7)'])
    assert p.returncode==7 and s['status']=='FAILED' and s['exit_code']==7
    assert 'JANUS JOB END' in log


def test_timeout_hard_stops_job_and_saves_json(tmp_path):
    p,s,log=launch(tmp_path,'deadline',0.2,
                   [sys.executable,'-c','import time;print("STARTED",flush=True);time.sleep(9)'])
    assert p.returncode==124 and s['status']=='TIMED_OUT'
    assert s['elapsed_seconds']<2 and 'STARTED' in log
    assert 'TIMED_OUT' in log


def test_timeout_kills_ignoring_sigterm(tmp_path):
    cmd='import signal,time;signal.signal(signal.SIGTERM,signal.SIG_IGN);print("READY",flush=True);time.sleep(9)'
    p,s,log=launch(tmp_path,'resistant',0.2,[sys.executable,'-c',cmd])
    assert p.returncode==124 and s['status']=='TIMED_OUT'
    assert s['elapsed_seconds']<3 and 'READY' in log


def test_rejects_invalid_deadline_without_launch(tmp_path):
    p,s,log=launch(tmp_path,'invalid',0,[sys.executable,'-c','print("NEVER")'])
    assert p.returncode==125 and s['status']=='WRAPPER_ERROR'
    assert 'NEVER' not in log

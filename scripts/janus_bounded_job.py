#!/usr/bin/env python3
"""Run one JANUS job under a hard wall-clock budget and save atomic state.

Exit statuses: 0=passed, child code=failed, 124=deadline exceeded,
128+signal=interrupted. Child is started in its own process group so timeout
covers subprocess descendants. The state file survives ordinary interruption.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def utcnow():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def atomic_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp.' + str(os.getpid()))
    try:
        with temp.open('w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=2, sort_keys=True)
            fh.write('\n')
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def stop_tree(proc: subprocess.Popen, grace: float):
    if proc.poll() is not None:
        return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        proc.wait(timeout=grace)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait()


def run(argv: list[str], timeout_sec: float, grace_sec: float,
        log: Path, state: Path, label: str) -> int:
    log.parent.mkdir(parents=True, exist_ok=True)
    log.touch(exist_ok=True)
    started = time.monotonic()
    status = {'schema': 'janus-bounded-job-v1', 'label': label, 'argv': argv,
              'working_directory': os.getcwd(), 'timeout_seconds': timeout_sec,
              'termination_grace_seconds': grace_sec, 'started_at_utc': utcnow(),
              'status': 'RUNNING', 'exit_code': None, 'log_path': str(log)}
    atomic_json(state, status)
    child = None
    old_handlers = {}

    class Interrupted(Exception):
        def __init__(self, sig):
            self.sig = sig

    def on_signal(signum, _frame):
        raise Interrupted(signum)

    try:
        if not argv or not 0 < timeout_sec <= 3600 or not 0 <= grace_sec <= 60:
            raise ValueError('invalid command/deadline; hard cap = 3600 seconds')
        with log.open('a', encoding='utf-8') as output:
            output.write(f'\n--- JANUS JOB {label} at {status["started_at_utc"]} '
                         f'deadline={timeout_sec}s argv={argv!r} ---\n')
            output.flush()
            child = subprocess.Popen(argv, stdin=subprocess.DEVNULL,
                stdout=output, stderr=subprocess.STDOUT,
                start_new_session=True, env={**os.environ, 'PYTHONUNBUFFERED': '1'})
            status['child_pid'] = child.pid
            atomic_json(state, status)
            for sig in (signal.SIGINT, signal.SIGTERM):
                old_handlers[sig] = signal.getsignal(sig)
                signal.signal(sig, on_signal)
            try:
                rc = child.wait(timeout=timeout_sec)
                status['status'] = 'PASSED' if rc == 0 else 'FAILED'
                status['exit_code'] = rc
            except subprocess.TimeoutExpired:
                stop_tree(child, grace_sec)
                status['status'] = 'TIMED_OUT'
                status['exit_code'] = 124
            except Interrupted as exc:
                stop_tree(child, grace_sec)
                status['status'] = 'INTERRUPTED'
                status['signal'] = exc.sig
                status['exit_code'] = 128 + exc.sig
            output.write(f'\n--- JANUS JOB END {label}: '
                         f'{status["status"]}, exit={status["exit_code"]} ---\n')
            output.flush()
    except Exception as exc:
        if child is not None:
            stop_tree(child, grace_sec)
        status['status'] = 'WRAPPER_ERROR'
        status['exit_code'] = 125
        status['error'] = repr(exc)
    finally:
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)
        status['finished_at_utc'] = utcnow()
        status['elapsed_seconds'] = round(time.monotonic() - started, 3)
        atomic_json(state, status)
    return status['exit_code']


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout-seconds', type=float, required=True)
    parser.add_argument('--grace-seconds', type=float, default=2)
    parser.add_argument('--state', type=Path, required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('--label', required=True)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    a = parser.parse_args(argv)
    cmd = a.command[1:] if a.command and a.command[0] == '--' else a.command
    if not cmd:
        parser.error('expected command following --')
    return run(cmd, a.timeout_seconds, a.grace_seconds, a.log, a.state, a.label)


if __name__ == '__main__':
    sys.exit(main())

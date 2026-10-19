"""Reproducible Step32d exact integrable compact metric-field/rate basis.

Tests include earlier restricted Step32c as a regression, NOT a physical
constraint result. Homogeneous Candidate-C dust-only background only.
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
 'numerics/hr_integrable_metric_time_basis.py','tests/test_hr_integrable_metric_time_basis.py',
 'scripts/verify_gate2b_step32d.py',
)
TARGETS=(
 'tests/test_hr_full_onshell_tadpole.py',
 'tests/test_hr_two_dust_common_time_canonical.py',
 'tests/test_hr_common_time_metric_rates.py',
 'tests/test_hr_metric_auxiliary_restricted.py',
 'tests/test_hr_integrable_metric_time_basis.py',
)

def main():
    missing=[x for x in FILES if not (ROOT/x).is_file()]
    if missing:raise SystemExit('Missing Step32d input files: '+', '.join(missing))
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    p=subprocess.run([sys.executable,'-m','pytest','-q',*TARGETS],cwd=ROOT,
        env=env,capture_output=True,text=True,check=False)
    data={
        'gate2b':'OPEN',
        'step':'32d-EXACT-TIME-INTEGRABLE-COMPACT-METRIC-PARENT-FIELDS',
        'workspace_origin':'focused_exact_earlier_sources_not_full_clean_Git_checkout',
        'full_repository_regression':False,
        'background':'radiation-free-CandidateC-PHYSICALLY-HOMOGENEOUS-on-shell',
        'genuinely_nonhomothetic_physical_background':False,
        'time_integrable_four_metric_fields':'TESTED' if p.returncode==0 else 'FAILED',
        'legal_compact_metric_and_matter_field_variations':16,
        'extra_dust_phase_rate_local_jets_are_independently_integrable':False,
        'true_ADM_metric_auxiliary_constraints_reduced':False,
        'BD_null_constraint_reduced':False,
        'DeFelice_physical_oracle':'NOT_RUN',
        'Aoki_physical_oracle':'NOT_RUN',
        'physical_scalar_ghost_speed_fold_verdict':'NOT_DERIVED',
        'python':sys.version.split()[0],
        'source_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in FILES},
        'tests_exit_code':p.returncode,
        'tests_output':(p.stdout+p.stderr)[-5000:].strip(),
    }
    if p.returncode==0:
        sys.path.insert(0,str(ROOT))
        from numerics.hr_integrable_metric_time_basis import first_variations
        from numerics.hr_two_dust_common_time_canonical import analytic_canonical_pair_integrals
        from numerics.hr_common_time_metric_rates import action as disconnected_rate_action
        from numerics.hr_integrable_metric_time_basis import action as integrable_action
        import numpy as np
        grad=first_variations(quadrature_order=20,step=2e-5)
        legal=np.array([i for i in range(18) if i not in (6,13)])
        h=2e-5
        z=np.zeros(18);z[14]=h
        old_first=(disconnected_rate_action(z,quadrature_order=20).total
                   -disconnected_rate_action(-z,quadrature_order=20).total)/(2*h)
        new_first=(integrable_action(z,quadrature_order=20).total
                   -integrable_action(-z,quadrature_order=20).total)/(2*h)
        symplectic=analytic_canonical_pair_integrals(quadrature_order=20)
        data.update({
          'result':'FOUR_COMPACT_PARENT_METRIC_FIELDS_AND_DUST_SYMPLECTIC_GREEN',
          'max_abs_legal_compact_first_variation':float(np.max(np.abs(grad[legal]))),
          'four_integrable_extra_field_first_variations':grad[14:18].tolist(),
          'two_nonlegal_dust_theta_rate_jet_first_variations':grad[[6,13]].tolist(),
          'old_disconnected_g_metric_rate_first':float(old_first),
          'new_integrable_g_parent_first':float(new_first),
          'canonical_dust_pair_rank':int(np.linalg.matrix_rank(symplectic,tol=1e-8)),
          'canonical_dust_symplectic_pair_coefficients':np.diag(symplectic).tolist(),
          'integrable_basis_is_full_gauge_closed':'NO',
          'integrable_basis_is_physical_kinetic_operator':'NO',
        })
    else:data['result']='FAILED'
    s=json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)
    print(s)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(s+'\n',encoding='utf-8')
    return p.returncode

if __name__=='__main__':raise SystemExit(main())

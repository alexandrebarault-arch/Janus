import math
import sys
from pathlib import Path
import numpy as np
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))


def test_boundary_momentum_pullback_round_trips():
    from numerics.de_felice_dust_observables import undo_bd_boundary_momentum_shift
    x=np.array([0.2,-0.1,0.05,0.3,0.4,-0.2])
    c=np.array([0.7,-0.4,0.2,0.9,0.1,-0.3])
    before=np.array([1.1,-0.8,0.4,0.7,-0.2,0.6])
    z=3
    grad=np.empty(6)
    grad[:] = c*x[z]
    grad[z] = np.dot(c,x)
    after=before-grad
    recovered=undo_bd_boundary_momentum_shift(after,coordinates=x,zdot_column=c,z_index=z)
    assert np.allclose(recovered,before,rtol=0,atol=1e-13)


def test_candidate_dust_observables_match_raw_phase_momentum_and_common_weighting():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    from numerics.de_felice_dust_observables import reconstruct_dust_observables
    point=candidate_c_dust_background_point(0.5,k_hmpc=0.05)
    action=candidate_c_dust_canonical_action(0.5,k_hmpc=0.05,derivative_step_N=2e-4)
    Y=np.array([0.027,-0.014,0.009])
    Pi=np.array([0.31,-0.22,0.18])
    obs=reconstruct_dust_observables(action,Y=Y,Pi=Pi,rho_g=point.rho_g_m,rho_f=point.rho_f_m,bg=point.metric)
    phase=np.r_[Y,Pi]
    p=action.matter_momentum_map@phase
    Z=float(action.bd_state_map@phase)
    n=point.metric.xi*point.metric.c
    pref=n*point.metric.xi**3
    drg=p[0]
    drf=p[1]/pref-3.0*point.rho_f_m*Z
    dg=drg/point.rho_g_m; df=drf/point.rho_f_m
    wg=point.rho_g_m; wf=pref*point.rho_f_m
    common=(wg*dg+wf*df)/(wg+wf)
    assert math.isclose(obs.delta_rho_g,drg,rel_tol=2e-12,abs_tol=2e-12)
    assert math.isclose(obs.delta_rho_f,drf,rel_tol=2e-12,abs_tol=2e-12)
    assert math.isclose(obs.delta_common,common,rel_tol=2e-12,abs_tol=2e-12)
    assert math.isclose(obs.delta_relative,dg-df,rel_tol=2e-12,abs_tol=2e-12)


def test_finite_cs2_phase_momentum_recovers_direct_density_identity():
    from numerics.de_felice_dust_observables import density_from_phase_momentum
    for rho,cs2,Phi,psi,qdot in ((4.2,0.2,0.07,-0.03,-0.11),(2.8,0.6,-0.04,0.08,0.09)):
        delta_rho_direct=rho/cs2*(qdot-Phi)
        momentum=rho*((qdot-Phi)/cs2+3.0*psi)
        measured=density_from_phase_momentum(momentum_local=momentum,enthalpy=rho,psi=psi)
        assert math.isclose(measured,delta_rho_direct,rel_tol=2e-13,abs_tol=2e-13)


def test_observables_scale_linearly_and_reject_nonpositive_densities():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    from numerics.de_felice_dust_observables import reconstruct_dust_observables
    point=candidate_c_dust_background_point(0.5,k_hmpc=0.1)
    action=candidate_c_dust_canonical_action(0.5,k_hmpc=0.1,derivative_step_N=2e-4)
    Y=np.array([0.02,-0.01,0.015]); Pi=np.array([0.2,-0.17,0.11])
    base=reconstruct_dust_observables(action,Y=Y,Pi=Pi,rho_g=point.rho_g_m,rho_f=point.rho_f_m,bg=point.metric)
    for fac in (0.1,3.0,-2.0):
        out=reconstruct_dust_observables(action,Y=fac*Y,Pi=fac*Pi,rho_g=point.rho_g_m,rho_f=point.rho_f_m,bg=point.metric)
        assert math.isclose(out.delta_g,fac*base.delta_g,rel_tol=2e-12,abs_tol=2e-12)
        assert math.isclose(out.delta_f,fac*base.delta_f,rel_tol=2e-12,abs_tol=2e-12)
        assert math.isclose(out.delta_common,fac*base.delta_common,rel_tol=2e-12,abs_tol=2e-12)
        assert math.isclose(out.delta_relative,fac*base.delta_relative,rel_tol=2e-12,abs_tol=2e-12)
    with pytest.raises(ValueError,match='positive'):
        reconstruct_dust_observables(action,Y=Y,Pi=Pi,rho_g=0.0,rho_f=point.rho_f_m,bg=point.metric)

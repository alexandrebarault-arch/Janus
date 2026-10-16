import math
import numpy as np


def test_selected_early_branch_is_more_negative_real_root_and_satisfies_polynomial():
    from numerics.candidate_c_adiabatic_stueckelberg_jets import candidate_c_adiabatic_stueckelberg_jets
    out=candidate_c_adiabatic_stueckelberg_jets(.02,k_hmpc=.1,step_N=6e-4)
    assert out.mu < -0.8
    assert out.other_mu > out.mu
    assert abs(np.polyval(out.polynomial,out.mu)) < 2e-10
    assert abs(np.polyval(out.polynomial,out.other_mu)) < 2e-10


def test_temporal_shift_matches_exact_nonhomothetic_relation():
    from numerics.candidate_c_adiabatic_stueckelberg_jets import candidate_c_adiabatic_stueckelberg_jets
    from numerics.nonhomothetic_stueckelberg import temporal_shift_coefficient
    out=candidate_c_adiabatic_stueckelberg_jets(.025,k_hmpc=.1,step_N=6e-4)
    expected=temporal_shift_coefficient(
        a=out.a,H_g=out.H_g,c=out.c,mu=out.mu,mu_dot=out.mu_dot,
    )
    assert math.isclose(out.s,expected,rel_tol=0,abs_tol=2e-12)
    assert math.isclose(out.mu_dot,out.H_g*out.mu_N,rel_tol=0,abs_tol=2e-12)


def test_early_branch_mu_and_shift_jets_are_step_converged():
    from numerics.candidate_c_adiabatic_stueckelberg_jets import candidate_c_adiabatic_stueckelberg_jets
    x=candidate_c_adiabatic_stueckelberg_jets(.025,k_hmpc=.1,step_N=8e-4)
    y=candidate_c_adiabatic_stueckelberg_jets(.025,k_hmpc=.1,step_N=4e-4)
    for u,v in ((x.mu,y.mu),(x.mu_N,y.mu_N),(x.s,y.s),(x.s_dot,y.s_dot)):
        assert np.isfinite(u) and np.isfinite(v)
        assert abs(u-v)/max(1.0,abs(v)) < 3e-5

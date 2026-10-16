import math
import numpy as np


def test_five_point_cosmic_jet_matches_exponential_control():
    from numerics.candidate_c_native_hr_jets import cosmic_jet_from_log_samples
    h=5e-3; p=.37; u=-.22
    ns={j:math.exp(p*j*h) for j in (-2,-1,0,1,2)}
    hs={j:math.exp(u*j*h) for j in (-2,-1,0,1,2)}
    rate,acc=cosmic_jet_from_log_samples(ns,hs,h)
    assert math.isclose(rate,p,rel_tol=0,abs_tol=2e-12)
    assert math.isclose(acc,p*p+u*p,rel_tol=0,abs_tol=2e-10)


def test_candidate_c_native_first_rates_match_exact_background_identities():
    from numerics.candidate_c_native_hr_jets import candidate_c_native_hr_jets
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    a=.5; kh=.2
    out=candidate_c_native_hr_jets(a,k_hmpc=kh,step_N=5e-4)
    point=candidate_c_dust_background_point(a,k_hmpc=kh)
    bg=point.metric; d=point.derivatives
    expected_n=(d.xi_prime/bg.xi+d.c_prime/bg.c)/bg.a
    expected_alpha=bg.H_omega/bg.a
    assert math.isclose(out.n_dot_over_n,expected_n,rel_tol=2e-8,abs_tol=2e-10)
    assert math.isclose(out.alpha_dot_over_alpha,expected_alpha,rel_tol=2e-8,abs_tol=2e-10)


def test_candidate_c_native_second_rates_are_step_converged():
    from numerics.candidate_c_native_hr_jets import candidate_c_native_hr_jets
    x=candidate_c_native_hr_jets(.5,k_hmpc=.2,step_N=8e-4)
    y=candidate_c_native_hr_jets(.5,k_hmpc=.2,step_N=4e-4)
    for a,b in ((x.n_ddot_over_n,y.n_ddot_over_n),(x.alpha_ddot_over_alpha,y.alpha_ddot_over_alpha)):
        assert np.isfinite(a) and np.isfinite(b)
        assert abs(a-b)/max(1.0,abs(b)) < 2e-5

"""Five-point secondary continuation with authentic original Step33g providers."""
import pytest
from numerics.hr_curved_moving_dust_primary import build_primary
from numerics.hr_step37_curved_solver import local_candidate
from numerics.hr_step39_cross_oracle import gauss_jet_bracket
from numerics.hr_step39_highorder_secondary import local_five_point,solve_five_point

@pytest.fixture(scope='module')
def cases():
    return [(h,*solve_five_point(scale=.1,degree=4,iterations=6,h=h))
            for h in (.004,.002,.001)]


def test_fivepoint_ward_improves_over_central_difference():
    w=build_primary()
    _,w2=local_candidate(w,.43,.004)
    _,w4=local_five_point(w,.43,.004)
    assert abs(w4)<abs(w2)/200


def test_refined_local_candidate_close_with_independent_stencils():
    w=build_primary()
    a=local_five_point(w,.43,.004)[0]
    b=local_five_point(w,.43,.002)[0]
    assert abs(a-b)<1e-8
    assert a==pytest.approx(.471663864165,abs=3e-9)


def test_fivepoint_curved_positive_two_dust_convergence(cases):
    assert len(cases)==3
    for h,w,meta in cases:
        x=meta['history'][-1]
        assert x['max_abs_C_sample']<6e-11
        assert x['max_primary_sample']<1e-12
        assert x['min_pg_sample']>0 and x['min_pf_sample']>0
        assert x['max_abs_C_sample']<meta['history'][0]['max_abs_C_sample']/1e9
        assert all(x['f_delta'][i]==0 for i in range(1,len(x['f_delta']),2))


def test_two_lapse_pairs_gauss_stay_below_quadratic_stencil_floor(cases):
    for h,w,meta in cases:
        a=gauss_jet_bracket(w,'A',96)
        b=gauss_jet_bracket(w,'B',96)
        assert abs(a)<3e-13
        assert abs(b)<3e-13


def test_highorder_guard():
    with pytest.raises(ValueError):solve_five_point(h=.02)
    with pytest.raises(ValueError):solve_five_point(degree=0)
    with pytest.raises(ValueError):local_five_point(build_primary(),r=.028,h=.002)

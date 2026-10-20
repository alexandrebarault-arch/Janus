"""Step39 independent lapse smearing / IBP-vs-unintegrated action checks."""
import numpy as np
import pytest
from numerics.hr_curved_moving_dust_primary import build_primary
from numerics.hr_step37_original_nonibp_oracle import original_pb
from numerics.hr_step39_cross_oracle import (
    lapse_jets,gauss_jet_bracket,original_nonibp_extended,witness,h_scan,PARAMS)

@pytest.fixture(scope='module')
def corrected():
    return witness(h=.001,degree=4,iterations=5)[0]

@pytest.fixture(scope='module')
def scan():
    return h_scan()

@pytest.mark.parametrize('pair',('A','B'))
def test_analytic_compact_lapse_jets_match_finite_differences(pair):
    for radius in (.3,.41,.61):
        n,m=lapse_jets(radius,pair)
        h=1e-5
        np.testing.assert_allclose([n[1],m[1]],
            [(lapse_jets(radius+h,pair)[i][0]-lapse_jets(radius-h,pair)[i][0])/(2*h) for i in (0,1)],rtol=1e-7,atol=1e-7)
    assert np.all(lapse_jets(.1,pair)[0]==0)
    assert np.all(lapse_jets(.8,pair)[1]==0)


def test_two_lapse_pairs_are_distinct_and_not_accidentally_equal():
    _,ma=lapse_jets(.4,'A');_,mb=lapse_jets(.4,'B')
    assert np.max(abs(ma-mb))>0.01


@pytest.mark.parametrize('pair,expected',(('A',5.3617022e-9),('B',3.3387069e-9)))
def test_gauss_full_jet_bracket_matches_independent_nodal_extrapolation(corrected,pair,expected):
    v=[gauss_jet_bracket(corrected,pair,n) for n in (48,96,192)]
    assert all(abs(z-expected)<1e-14 for z in v)
    assert max(v)-min(v)<1e-15
    assert abs(v[-1])>1e-9  # Step37 C not exactly zero for this frozen profile


def test_original_nodal_321_algebra_is_unchanged_for_historical_lapses(corrected):
    prev=original_pb(corrected,n=321)
    alt=original_nonibp_extended(corrected,'A',321)
    assert alt['bracket']==pytest.approx(prev['bracket'],abs=4e-16)
    assert alt['min_pg']>0 and alt['min_pf']>0
    assert len(alt['contributions'])==6


def test_distinct_lapse_pair_nodal_two_grid_extrapolation(corrected):
    coarse=original_nonibp_extended(corrected,'B',321)
    fine=original_nonibp_extended(corrected,'B',641)
    assert coarse['bracket']<0 and fine['bracket']<0
    estimate=(4*fine['bracket']-coarse['bracket'])/3
    assert estimate==pytest.approx(3.3387069e-9,abs=2e-11)


def test_rigorous_physics_is_not_deduced_from_h_dependent_collocation(scan):
    assert len(scan)==5
    assert scan[-1]['max_C_local_sample']<5e-10
    assert scan[-1]['max_primary_sample']<1e-12
    assert scan[-1]['min_pg_sample']>0 and scan[-1]['min_pf_sample']>0
    for pair in ('A','B'):
        key='IBP_'+pair
        for i in range(3):
            ratio=abs(scan[i][key]/scan[i+1][key])
            assert 3.9<ratio<4.1
        assert abs(scan[-1][key])<3e-11
    assert scan[0]['max_C_local_sample']>scan[-1]['max_C_local_sample']*100


def test_input_guard_and_no_unknown_smear(corrected):
    with pytest.raises(ValueError):lapse_jets(.4,'C')
    with pytest.raises(ValueError):gauss_jet_bracket(corrected,'A',7)
    with pytest.raises(ValueError):original_nonibp_extended(corrected,'B',5000)
    with pytest.raises(ValueError):original_nonibp_extended(corrected,'C',81)

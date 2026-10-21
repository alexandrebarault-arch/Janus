"""Step44 real six-canonical-pair HR original-provider verification.

Requires seven actual pinned GitHub historical modules in a coherent worktree.
A numerical PASS never implies exact Ward, secondary or full Dirac closure.
"""
import copy
import pytest
from scripts import verify_gate2b_step44 as phys


@pytest.fixture(scope='module')
def run():
    return phys.numerical_physical_report(grids=(161,321,641))


def test_seven_genuine_historical_provider_git_blobs():
    assert phys.verify_sources()==phys.EXPECTED_BLOBS
    assert len(phys.EXPECTED_BLOBS)==7


def test_fail_closed_on_any_changed_historical_provider_hash(monkeypatch):
    expected=copy.copy(phys.EXPECTED_BLOBS)
    tampered=dict(expected)
    first=next(iter(tampered))
    tampered[first]='0'*40
    monkeypatch.setattr(phys,'EXPECTED_BLOBS',tampered)
    with pytest.raises(ValueError,match='original provider mismatch'):
        phys.verify_sources()


def test_step44_actual_corrected_profile_and_primaries(run):
    assert run['GATE_2B']=='OPEN' and run['JANUS_R']=='NOT_VALIDATED'
    assert len(run['coefficients'])==9
    assert run['coefficients'][2]==pytest.approx(.0015479757723131573,abs=2e-12)
    assert run['max_local_C_original_9_heldout']<1e-10


def test_actually_physical_W_D_and_high_jets_small_but_not_a_proof(run):
    vals=list(run['seven_physical_points'].values())
    assert len(vals)==7
    assert max(abs(x['W']) for x in vals)<1e-12
    assert max(abs(x['D']) for x in vals)<1e-12
    assert max(x['max_excluded_abs'] for x in vals)<1e-12
    assert max(abs(x['C']) for x in vals)<1e-10
    assert all(x['numerical_not_symbolic'] for x in vals)


@pytest.mark.parametrize('pair',('A','B'))
def test_physical_two_lapse_pairs_direct_vs_reduced_and_nonibp(run,pair):
    data=run['independent_smeared_pairs'][pair]
    a,b=data['jet_integrals']['48'],data['jet_integrals']['96']
    assert abs(a['difference'])<5e-15 and abs(b['difference'])<5e-15
    assert abs(a['full_jet_bracket']-b['full_jet_bracket'])<1e-15
    raw=[x['bracket'] for x in data['original_nonIBP_by_grid']]
    assert all(x<0 for x in raw)
    assert 3.8<raw[0]/raw[1]<4.2
    assert 3.8<raw[1]/raw[2]<4.2
    first_r4=data['richardson_exploratory']['R4'][0]
    assert abs(first_r4-b['full_jet_bracket'])<2e-14


def test_original_nonibp_grid_primary_roundoff_is_not_exact_constraint(run):
    for x in run['independent_smeared_pairs'].values():
        grids=x['original_nonIBP_by_grid']
        assert [row['n'] for row in grids]==[161,321,641]
        assert grids[0]['max_original_discrete_primary']>grids[-1]['max_original_discrete_primary']>1e-9
        assert all(len(row['contributions'])==6 for row in grids)


def test_Ward_nearzero_not_due_to_secondary_fitting(run):
    assert len(run['off_secondary_primary_variations'])==3
    for sample in run['off_secondary_primary_variations']:
        sites=sample['samples']
        assert max(abs(x['C']) for x in sites)>.1
        assert max(abs(x['W']) for x in sites)<1e-12
        assert max(abs(x['D']) for x in sites)<1e-12
        assert all(x['max_excluded_abs']==0 for x in sites)


def test_invalid_richardson_grids_rejected_before_solving():
    for grids in ((161,321), (160,320,640), (161,321,640)):
        with pytest.raises(ValueError):
            phys.numerical_physical_report(grids=grids)


def test_extrapolation_algebra_and_inherent_nonrigorous_scope():
    ans=phys.richardson([16.,4.,1.,.25])
    assert ans['R2']==[0.,0.,0.]
    assert ans['R4']==[0.,0.]

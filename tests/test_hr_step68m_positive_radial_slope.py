"""Step68m certified monotonicity on the outer radial annulus only."""
from pathlib import Path
from fractions import Fraction as F
import pytest
from numerics import hr_step68m_positive_radial_slope as m

@pytest.fixture(scope='module')
def theorem():
    return m.certify_positive_Us(cells=8192,lo_s='1/64',hi_s='289/400',delta_U='1/1000000',rerun_global=True)


def test_verify_exact_original_chain_sha():
    assert len(m.authenticate_chain())==4


def test_reject_tampered_inference_parameters():
    with pytest.raises(ValueError,match='requires certified'):
        m.certify_positive_Us(delta_U='1/10000',rerun_global=False)
    with pytest.raises(ValueError,match='strictly positive s'):
        m.certify_positive_Us(lo_s='0',rerun_global=False)
    with pytest.raises(ValueError,match='bad cell'):
        m.certify_positive_Us(cells=12,rerun_global=False)


def test_positive_global_derivative_on_closed_annulus(theorem):
    assert theorem['Step68l_certification_reexecuted']
    assert theorem['grid_cells']==8192
    assert theorem['r_interval']==['1/8','17/20']
    assert F(theorem['strict_lower_U_s'])>0
    assert F(theorem['upper_U_s'])>F(theorem['strict_lower_U_s'])
    assert theorem['whole_closed_interval_positive']


def test_no_claim_near_center_or_temporal_rank(theorem):
    assert theorem['small_center_r_below_1_8_covered'] is False
    assert theorem['temporal_lapse_A_coefficients_certified'] is False
    assert theorem['Dirac_rank']=='NOT_COMPUTED'
    assert theorem['JANUS_R']=='NOT_VALIDATED'


def test_coarse_grid_explicitly_fails_same_microtube():
    with pytest.raises(ArithmeticError,match='slab'):
        m.certify_positive_Us(cells=256,lo_s='1/64',delta_U='1/1000000',rerun_global=False)

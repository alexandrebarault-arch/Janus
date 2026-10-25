"""Step68l verified original 16k-cell continuum tube, strict margins and fail closed."""
from pathlib import Path
from fractions import Fraction as F
import pytest
from numerics import hr_step68l_refined_global_barrier as step
from numerics.hr_step55_global_barrier import certify_global_barrier

@pytest.fixture(scope='module')
def full():
    return step.narrowed_global_barrier(cells=16384,delta_U='0.000001',delta_V='0.00005')


def test_four_byte_authentic_source_blobs():
    assert step.authentic_originals()==step.EXPECTED


def test_refuse_source_tampering(tmp_path):
    root=Path(step.__file__).parent
    for name in step.EXPECTED:
        (tmp_path/name).write_bytes((root/name).read_bytes())
    f=tmp_path/'hr_step55_global_barrier.py'
    f.write_bytes(f.read_bytes()+b'\n# tampered\n')
    with pytest.raises(ValueError,match='mismatch'):
        step.authentic_originals(tmp_path)


def test_historic_barrier_still_passes():
    historic=certify_global_barrier(cells=256)
    assert historic['cells']==256
    assert F(historic['strict_max_Fupper_rational'])<0
    assert F(historic['strict_min_Flower_rational'])>0


def test_refined_continuum_certificate(full):
    assert full['rational_slabs']==16384
    assert full['continuous_s_domain']==['0','289/400']
    assert full['continuous_r_domain']==['0','17/20']
    assert full['outward_integer_scale']==10**28
    assert full['GATE_2B']=='OPEN'
    assert full['JANUS_R']=='NOT_VALIDATED'


def test_strict_global_inward_barrier_signs(full):
    assert F(full['strict_max_Fupper'])<0
    assert F(full['strict_min_Flower'])>0
    assert F(full['U_minus_Ustar_abs_lt'])==F(1,1000000)
    assert F(full['factor_stronger_than_historical'])==100


def test_strict_global_velocity_enclosure(full):
    assert -F(full['V_minus_Vstar_abs_lt'])<F(full['strict_V_minus_Vstar_lower'])
    assert F(full['strict_V_minus_Vstar_upper'])<F(full['V_minus_Vstar_abs_lt'])
    assert F(full['V_actual_min_enclosure'])<F(full['V_actual_max_enclosure'])


def test_coarse_resolution_refuses_uncertified_microtube():
    # This is an outward interval resolution failure, NOT physical divergence.
    with pytest.raises(ArithmeticError,match='slab 0'):
        step.narrowed_global_barrier(cells=8192,delta_U='0.000001',delta_V='0.00005')


def test_invalid_settings_rejected():
    with pytest.raises(ValueError):step.narrowed_global_barrier(cells=100)
    with pytest.raises(ValueError):step.narrowed_global_barrier(delta_U='-0.000001')
    with pytest.raises(ValueError):step.narrowed_global_barrier(delta_V='0.02')
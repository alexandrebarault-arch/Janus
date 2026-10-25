"""Independent exact-arithmetic and fail-closed tests for Step68y."""
from fractions import Fraction as F
from pathlib import Path
import json
import shutil
import pytest
from numerics.hr_step68y_signed_center_residual import (
    ORIGINAL, MAX_S, KAPPA, bounds, load_originals, at_s, blob_sha)

ROOT=Path(__file__).resolve().parents[1]/'research'/'reports'


def test_both_original_git_blobs_authenticated():
    for filename, wanted in ORIGINAL.values():
        assert blob_sha((ROOT/filename).read_bytes()) == wanted
    load_originals(ROOT)


def test_strict_negative_residual_entire_small_center():
    a=bounds(ROOT)
    lo,hi=map(F,a['F0_over_s_cubed_intersection'])
    assert lo < hi < 0
    assert lo == F(-104671973400629476166791119,800000000000000000000000000000000)
    assert hi == F(-473550521560821294562534863,5000000000000000000000000000000000)
    assert a['F0_strict_negative_for_s_positive'] is True


def test_new_bounds_stronger_than_step68x():
    a=bounds(ROOT)
    lo,hi=map(F,a['U_s_minus_Ustar_s_over_s_squared'])
    old_C=F(551901551914723209073991119,1600000000000000000000000000000000)
    assert -old_C < lo < 0 < hi < old_C
    vlo,vhi=map(F,a['G_minus_Vstar_over_s_cubed'])
    assert vlo < 0 < vhi
    assert max(abs(vlo),abs(vhi)) < F(391901551914723209073991119,800000000000000000000000000000000)
    assert a['U_minus_Ustar_over_s_cubed']==[str(-KAPPA),'0']


def test_physical_momentum_boundary_consistency():
    a=bounds(ROOT)
    x=a['at_r_1_over_32']
    assert F(x['pLf_minus_s_Ustar'][0]) == -F(1,10995116277760000000)
    assert x['pLf_prime_over_r_minus_Vstar']==x['G_minus_Vstar']
    assert F(x['U_minus_Ustar'][0]) == -F(1,10737418240000000)
    assert a['temporal_A_N_A_M_near_center']=='NOT_COMPUTED'
    assert a['JANUS_R']=='NOT_VALIDATED'


@pytest.mark.parametrize('s', [-F(1,100), F(1,1023)])
def test_outside_chart_rejected(s):
    with pytest.raises(ValueError): at_s(s,(F(-1),F(1)),(F(-1),F(1)))


def test_tampered_step68u_certificate_is_rejected(tmp_path):
    for filename,_ in ORIGINAL.values(): shutil.copy(ROOT/filename, tmp_path/filename)
    filename=ORIGINAL['68u'][0]
    p=tmp_path/filename
    p.write_bytes(p.read_bytes().replace(b'"step": "68u"',b'"step": "68t"'))
    with pytest.raises(ValueError,match='SHA drift'):
        bounds(tmp_path)


def test_tampered_step68v_certificate_is_rejected(tmp_path):
    for filename,_ in ORIGINAL.values(): shutil.copy(ROOT/filename, tmp_path/filename)
    filename=ORIGINAL['68v'][0]
    p=tmp_path/filename
    p.write_bytes(p.read_bytes().replace(b'"G_U_center_interval"',b'"G_W_center_interval"'))
    with pytest.raises(ValueError,match='SHA drift'):
        bounds(tmp_path)

import math
import pytest


def test_two_native_conformal_taylor_jets_obey_branch_kinematics():
    from numerics.nonhomothetic_compact_background import native_conformal_taylor_jets
    out = native_conformal_taylor_jets(
        a=0.5, xi=0.5682425064594762, c=0.9370846292570983,
        H=1.7, H_prime=-0.42,
    )
    b = 0.5*0.5682425064594762
    assert math.isclose(out.g.a0, 0.5, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.g.ap0, 0.5*1.7, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.g.app0, 0.5*(1.7**2-0.42), rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.f.a0, b, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.f.ap0, b*1.7, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.f.app0, b*(1.7**2-0.42/0.9370846292570983), rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.eta_f_prime, 0.9370846292570983, rel_tol=0, abs_tol=1e-15)


def test_homothetic_limit_gives_scaled_identical_native_jets():
    from numerics.nonhomothetic_compact_background import native_conformal_taylor_jets
    out = native_conformal_taylor_jets(a=1.2, xi=0.7, c=1.0, H=0.4, H_prime=-0.03)
    assert math.isclose(out.f.a0/out.g.a0, 0.7, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.f.ap0/out.g.ap0, 0.7, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(out.f.app0/out.g.app0, 0.7, rel_tol=0, abs_tol=1e-15)


def test_invalid_nonhomothetic_jet_inputs_are_rejected():
    from numerics.nonhomothetic_compact_background import native_conformal_taylor_jets
    with pytest.raises(ValueError):
        native_conformal_taylor_jets(a=1.0, xi=1.0, c=0.0, H=1.0, H_prime=0.0)

import math

from numerics.lapse_matter_duality import g_matter_blocks, f_matter_blocks, dual_state


def sample():
    return dict(
        Ag=1.13, Af=0.91, R=1.27, p=0.31,
        b1=0.8, b2=-0.17, b3=0.23,
        kg=1.4, kf=0.7,
        Dg=0.12, Sg=-0.03, Tg=0.02, vg=-0.11,
        Df=0.08, Sf=0.025, Tf=0.01, vf=0.09,
    )


def test_f_matter_vanishes_when_f_state_zero():
    s = sample() | dict(Df=0.0, Sf=0.0, Tf=0.0, vf=0.0)
    dg, df = f_matter_blocks(**s)
    assert dg == 0.0
    assert df == 0.0


def test_sector_duality_maps_g_contribution_to_minus_f_contribution():
    s = sample()
    wg_g, wf_g = g_matter_blocks(**s)
    sd = dual_state(s)
    wg_f_dual, wf_f_dual = f_matter_blocks(**sd)
    assert math.isclose(wg_g, -wf_f_dual, rel_tol=2e-12, abs_tol=2e-12)
    assert math.isclose(wf_g, -wg_f_dual, rel_tol=2e-12, abs_tol=2e-12)


def test_time_symmetric_rest_dust_blocks_are_finite():
    s = sample() | dict(p=0.0, Sg=0.0, Sf=0.0, vg=0.0, vf=0.0)
    vals = g_matter_blocks(**s) + f_matter_blocks(**s)
    assert all(math.isfinite(v) for v in vals)

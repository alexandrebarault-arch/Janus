import math
import numpy as np

from numerics.de_felice_candidate_c_reduction import (
    candidate_c_raw_background, candidate_c_three_mode_extrapolation, physical_matrices,
)


def test_candidate_c_physical_kinetic_matrix_has_three_positive_modes():
    _,red=physical_matrices(0.5,150.0)
    eig=np.linalg.eigvalsh(red.K)
    assert eig.shape==(3,)
    assert np.all(eig>0.0)


def test_candidate_c_a05_recovers_three_independent_high_k_speeds():
    bg=candidate_c_raw_background(0.5)
    out=candidate_c_three_mode_extrapolation(0.5)
    expected_f=bg.ctilde*math.sqrt(0.3)
    expected_g=math.sqrt(0.4)
    expected_gravity=math.sqrt(0.6920799927)
    assert abs(out.extrapolated[0]-expected_f)<5e-4
    assert abs(out.extrapolated[1]-expected_g)<5e-4
    assert abs(out.extrapolated[2]-expected_gravity)<5e-4


def test_candidate_c_a02_keeps_three_finite_high_k_scalar_branches():
    """RED: early-time production reduction must stay finite and mode-complete.

    The Candidate-C probe sound speeds are deliberately diagnostic and are not a
    self-consistent single-P(X) embedding of the matter+radiation/dust background,
    so Eq. (86) is not used here as an exact gravity-speed oracle.  That oracle is
    tested separately by the self-consistent P(X) control.
    """
    from numerics.de_felice_candidate_c_reduction import mode_speeds

    bg=candidate_c_raw_background(0.2)
    rows=[]
    for k in (600.0,1000.0):
        speeds=mode_speeds(0.2,k)
        assert speeds.shape==(3,)
        assert np.all(np.isfinite(speeds))
        assert np.max(speeds)<1.5
        rows.append(speeds)

        expected_f=bg.ctilde*math.sqrt(0.3)
        expected_g=math.sqrt(0.4)
        assert np.min(np.abs(speeds-expected_f))<5e-3
        assert np.min(np.abs(speeds-expected_g))<5e-3

    leftovers=[]
    for speeds in rows:
        pool=list(speeds)
        for target in (bg.ctilde*math.sqrt(0.3), math.sqrt(0.4)):
            j=min(range(len(pool)), key=lambda i:abs(pool[i]-target))
            pool.pop(j)
        leftovers.append(pool[0])
    assert abs(leftovers[1]-leftovers[0])<0.05

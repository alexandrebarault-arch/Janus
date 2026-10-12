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

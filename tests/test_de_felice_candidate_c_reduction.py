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
    """Early-time production reduction must stay finite and mode-complete.

    The Candidate-C probe sound speeds are deliberately diagnostic and are not a
    self-consistent single-P(X) embedding of the matter+radiation/dust background,
    so Eq. (86) is not used here as an exact gravity-speed oracle. That oracle is
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


def _principal_gravity_quantities(a):
    from numerics.candidate_c_transfer import candidate_c_background_point

    pt=candidate_c_background_point(a,k_hmpc=0.0)
    m=pt.metric
    xi=m.xi
    J=m.f2/xi
    H2=(m.H/m.a)**2
    W=m.m2*(1.0+m.kappa*xi*xi)*J/(2.0*m.kappa*xi)-H2
    B=2.0*W+xi*xi*pt.rho_f_m/m.kappa
    cs2=(
        m.m2/(3.0*B)*(1.0+1.0/(m.kappa*xi*xi))
        *(4.0*m.f1-xi*J*(m.c+1.0))
        +(m.c-4.0*H2*m.f1/(xi*J*B))/3.0
    )
    kinetic=3.0/8.0*m.m2*m.a**4*xi*J*B
    return math.sqrt(cs2),kinetic


def test_candidate_c_a1_recovers_three_high_k_characteristics():
    bg=candidate_c_raw_background(1.0)
    out=candidate_c_three_mode_extrapolation(
        1.0,
        k_values=(250.0,400.0,600.0),
    )
    expected_gravity,_=_principal_gravity_quantities(1.0)
    expected=np.array(sorted((
        bg.ctilde*math.sqrt(0.3),
        math.sqrt(0.4),
        expected_gravity,
    )))
    assert np.allclose(np.array(sorted(out.extrapolated)),expected,rtol=0.0,atol=1e-4)


def test_candidate_c_physical_kinetic_signs_match_principal_no_ghost_sign():
    for a in (1.0,0.5,0.2):
        _,red=physical_matrices(a,600.0)
        eig=np.linalg.eigvalsh(red.K)
        _,principal_kinetic=_principal_gravity_quantities(a)
        assert np.all(eig>0.0)
        assert principal_kinetic>0.0

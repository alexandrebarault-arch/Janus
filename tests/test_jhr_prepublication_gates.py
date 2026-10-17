"""Falsification of stronger-than-supported statements in supplied JHR note."""
import math
import numpy as np
import pytest
from numerics.jhr_independent_audit import (
    tensor_kinetic_matrix, eft_lambda3_eV,
    stellar_weighted_divergences, toy_acoustic_peak_amplitudes,
)

def test_opposite_eh_has_indefinite_tensor_kinetic_signature():
    # Same common-time action, positive chi_g and chi_f, inverted f EH sign.
    K=tensor_kinetic_matrix(chig=1.7,chif=.9,relative_f_sign=-1.)
    eigen=np.linalg.eigvalsh(K)
    assert eigen[0]<0<eigen[1]
    assert np.linalg.det(K)<0
    # An invertible field change cannot change inertia (Sylvester law).
    A=np.array([[1.3,.2],[-.4,1.2]])
    assert np.linalg.det(A)!=0
    eig2=np.linalg.eigvalsh(A.T@K@A)
    assert eig2[0]<0<eig2[1]

def test_lambda3_at_cosmological_mass_not_mev():
    cutoff=eft_lambda3_eV(1e-32)
    assert cutoff==pytest.approx(6.244528544839634e-13,rel=2e-14)
    assert 1e-3/cutoff>1e9
    required_mass=math.sqrt((1e-3)**3/2.435e27)
    assert required_mass==pytest.approx(6.408413361120015e-19,rel=1e-12)

def test_combined_stellar_noether_check_does_not_verify_separate_bianchi_constraints():
    dg,df=stellar_weighted_divergences(compactness=.05)
    assert np.max(np.abs(dg+df))<1e-12
    assert np.max(np.abs(dg))>.1
    assert np.max(np.abs(df))>.1
    # The combined identity holds numerically; neither model-coded channel vanishes.

def test_hand_forced_cmb_oscillator_is_parameter_dependent():
    _,zero=toy_acoustic_peak_amplitudes(alpha=0.,rtol=1e-8,atol=1e-10)
    _,forced=toy_acoustic_peak_amplitudes(alpha=4.4,rtol=1e-8,atol=1e-10)
    assert np.all(zero>0) and np.all(forced>0)
    assert not np.allclose(zero,forced,rtol=1e-4)
    # Changing manually specified psi forcing is not a CMB Boltzmann transfer proof.

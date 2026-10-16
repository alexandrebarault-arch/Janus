import numpy as np


def test_phase_averaged_metric_schur_recovers_fierz_pauli_light_cone():
    from numerics.minkowski_fp_wkb_oracle import scan_fierz_pauli_light_cone
    out=scan_fierz_pauli_light_cone(
        k=24.0,kr0=50.0,speeds=(0.99,0.995,1.0,1.005,1.01),
        interaction_mass2=0.2,amplitude_step=2e-4,nphase=12,
    )
    assert abs(out.minimum_speed-1.0) < 4e-4
    center=abs(out.reduced_coefficients[2])
    flank=min(abs(out.reduced_coefficients[0]),abs(out.reduced_coefficients[-1]))
    assert center/flank < 8e-4
    assert np.max(out.metric_condition_numbers) < 10.0

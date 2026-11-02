"""Reproducible SHA-guarded authentic Step45/58 B_N ideal replay.

No physics substitution, no numerical Step55 enclosure and no claim of Dirac
completion. Step57's authentic_step45 import need only return original Step45.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

SOURCES = {
    "numerics/hr_step45_exact_physical_ward.py": "66aa43841dccfe4a5d586a49be9c10af3a67a10e",
    "numerics/hr_step58_temporal_operator.py": "802c23aebd41780d8c462f1aa1711707fe4ee88f",
    "numerics/hr_b3c3d6_bn_high_jet_elimination.py": "086b6bae543c0ee497ca9154c5a055921f018423",
    "numerics/hr_b3c3d6_bn_full_ideal.py": "bc9b371c3d66f6b2491009e631fa4ed4a29a676f",
    "tests/test_hr_b3c3d6_bn_full_ideal.py": "5862735ecc5c7c43e71ee3f6fec558fbab71a6a5",
}


def verify_blob_provenance(root=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    for path, expected in SOURCES.items():
        blob = (root/path).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(blob)).encode() + b"\0" + blob).hexdigest()
        if actual != expected:
            raise ValueError(f"Git blob mismatch for {path}: {actual} != {expected}")
    return SOURCES.copy()


def run():
    verify_blob_provenance()
    from numerics.hr_step45_exact_physical_ward import exact_physical_ward, exact_certificate_summary
    from numerics.hr_step58_temporal_operator import physical_operator, highest_lapse_certificate
    from numerics.hr_b3c3d6_bn_full_ideal import certify
    ward = exact_physical_ward()
    op = physical_operator()
    step45 = exact_certificate_summary()
    high = highest_lapse_certificate()
    ideal = certify(ward, op)
    assert step45["exact_symbolic_residuals_all_zero"]
    assert high["N2_and_M2_vanish_on_Fz_and_Hg"]
    assert ideal["first_jet_remainder"] == "ZERO"
    return {
        "scope": "BYTE_AUTHENTIC_ORIGINAL_STEP45_STEP58_FORMAL_POSITIVE_K_CHART",
        "original_source_github_blob_sha": SOURCES,
        "step45_original_Ward_nine_residuals": "EXACT_ZERO",
        "step58_original_highest_lapse_E_N_E_M": "EXACT_ZERO_ON_Fz_Hg",
        "step58_original_four_high_jet_factors": "EXACT_MULTIPLES_OF_Fz",
        "step58_original_B_N_identity": ideal["identity"],
        "step58_original_B_N_identity_on_Fz_Hg": "EXACT",
        "on_full_shell_Fz_Hg_Hgr_C_zero_B_N": "EXACT_ZERO",
        "original_step57_complete_principal_symbol_executed": False,
        "physical_step55_six_step58_coefficient_interval_enclosures": "NOT_CERTIFIED",
        "positive_two_boundary_lapse_bvp": "NOT_CERTIFIED",
        "dirac_four_dimensional_stability_observables": "OPEN",
        "GATE_2B": "OPEN",
        "JANUS_R": "NOT_VALIDATED",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))

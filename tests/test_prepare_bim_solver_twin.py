from pathlib import Path

import tools.prepare_bim_solver_twin as prep


def test_prepare_calls_verification_then_all_patchers(monkeypatch, tmp_path: Path):
    calls = []
    monkeypatch.setattr(
        prep, "verify_manifest", lambda root: calls.append(("verify", root))
    )
    monkeypatch.setattr(
        prep,
        "patch_state_checkout",
        lambda root, require_pinned=False: calls.append(("state", root)),
    )
    monkeypatch.setattr(
        prep,
        "patch_equations_checkout",
        lambda root, require_pinned=False: calls.append(("equations", root)),
    )
    monkeypatch.setattr(
        prep,
        "patch_lapse_checkout",
        lambda root, require_pinned=False: calls.append(("lapse", root)),
    )

    prep.prepare_checkout(tmp_path)

    assert [call[0] for call in calls] == [
        "verify",
        "state",
        "equations",
        "lapse",
    ]

from __future__ import annotations

from pathlib import Path
import argparse

from tools.verify_upstream_manifest import verify_manifest
from tools.apply_twin_fluid_state_patch import patch_checkout as patch_state_checkout
from tools.apply_twin_fluid_patch import patch_checkout as patch_equations_checkout
from tools.apply_twin_lapse_patch import patch_checkout as patch_lapse_checkout


def prepare_checkout(root: Path) -> None:
    root = Path(root)
    verify_manifest(root)
    patch_state_checkout(root, require_pinned=False)
    patch_equations_checkout(root, require_pinned=False)
    patch_lapse_checkout(root, require_pinned=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare pinned bim-solver STD checkout for JANUS-R twin dust."
    )
    parser.add_argument("checkout", type=Path)
    args = parser.parse_args()
    prepare_checkout(args.checkout)
    print("Twin-fluid source preparation complete.")
    print("Compilation/regression is still required before any physics run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

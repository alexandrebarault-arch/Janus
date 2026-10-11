from __future__ import annotations

from pathlib import Path
import hashlib


class ManifestError(RuntimeError):
    pass


UPSTREAM_COMMIT = "8852e8e9921edeeedf1a447d3bf27b82ec24433c"

UPSTREAM_BLOBS = {
    "src/bim-solver-std.cpp": "11dc8d92d3ff04838ea8efd9a4107e008968ef18",
    "include/eom-std/eomMatter.h": "82e1900093e20ccb2be71c7469827e432bc0b5f9",
    "include/eom-std/eomSources.h": "6d162c65f190077508612eeac561f2a64396ae40",
    "include/eom-std/eomConstraints.h": "daf6d899bc9949afee7cc016bc0984a2c9dc5f82",
    "include/eom-std/eomMiscEquations.h": "73abd05261cfe039949c0f4c49040068f6b3fc43",
    "include/eom-std/eomEvolution.h": "463efcd0d3c1eb6223b47a0b80f3c9caf4d57b07",
    "include/eom-std/eomLapseRatios.h": "0f340a43694f55b7210f3c250211bbfb9d120391",
}


def git_blob_sha(path: Path) -> str:
    data = Path(path).read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def verify_manifest(
    root: Path, manifest: dict[str, str] = UPSTREAM_BLOBS
) -> None:
    root = Path(root)
    failures = []
    for rel, expected in manifest.items():
        path = root / rel
        if not path.is_file():
            failures.append(f"{rel}: missing")
            continue
        actual = git_blob_sha(path)
        if actual != expected:
            failures.append(f"{rel}: expected {expected}, got {actual}")
    if failures:
        raise ManifestError("upstream source mismatch:\n" + "\n".join(failures))

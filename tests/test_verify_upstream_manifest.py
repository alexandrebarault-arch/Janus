from pathlib import Path

import pytest

from tools.verify_upstream_manifest import ManifestError, git_blob_sha, verify_manifest


def test_git_blob_sha_matches_git_definition(tmp_path: Path):
    path = tmp_path / "x.txt"
    path.write_bytes(b"hello\n")
    assert git_blob_sha(path) == "ce013625030ba8dba906f756967f9e9ca394464a"


def test_manifest_reports_mismatch(tmp_path: Path):
    path = tmp_path / "a.txt"
    path.write_text("x")
    with pytest.raises(ManifestError):
        verify_manifest(tmp_path, {"a.txt": "0" * 40})

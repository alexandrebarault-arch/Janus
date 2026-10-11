from __future__ import annotations

from pathlib import Path
import subprocess

PINNED_COMMIT = "8852e8e9921edeeedf1a447d3bf27b82ec24433c"


class PatchError(RuntimeError):
    pass


def _find_function(text: str, signature: str):
    start = text.find(signature)
    if start < 0:
        raise PatchError(f"{signature}: not found")
    brace = text.find("{", start)
    if brace < 0:
        raise PatchError(f"{signature}: opening brace not found")
    depth = 0
    end = None
    for i in range(brace, len(text)):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        raise PatchError(f"{signature}: closing brace not found")
    return start, brace, end


def _augment_return(text: str, signature: str, delta: str) -> str:
    _, brace, end = _find_function(text, signature)
    body = text[brace:end]
    marker = "return "
    r = body.find(marker)
    if r < 0:
        raise PatchError(f"{signature}: return not found")
    expr_start = r + len(marker)
    semi = body.find(";", expr_start)
    if semi < 0:
        raise PatchError(f"{signature}: return semicolon not found")
    expr = body[expr_start:semi].strip()
    new_body = body[:expr_start] + "(" + expr + ") + (" + delta + ")" + body[semi:]
    return text[:brace] + new_body + text[end:]


DELTA_G = r"""-(k_f * pow2(gA(m,n)) * pow2(fA(m,n)) * (1 + pow2(p(m,n)))
        * (b_1 + R(m,n) * (2 * b_2 + b_3 * R(m,n)))
        * (b_1 + b_2 * R(m,n)) * (pfFD(m,n) + pfFtau(m,n)))
        / (pow2(R(m,n)) * pow3(R(m,n)))"""

DELTA_F = r"""k_f * pow2(gA(m,n)) * pow2(fA(m,n)) * (1 + pow2(p(m,n)))
        * (b_1 + R(m,n) * (2 * b_2 + b_3 * R(m,n)))
        * (Lt(m,n) * (b_1 - b_3 * pow2(R(m,n)))
            * (pfFD(m,n) - pfFS(m,n) * pfFv(m,n) + pfFtau(m,n))
           + 2 * gA(m,n) * R(m,n) * (b_1 + b_2 * R(m,n))
            * (pfFS(m,n) * pfFv(m,n)
               + pow2(p(m,n)) * (pfFD(m,n) + pfFS(m,n) * pfFv(m,n) + pfFtau(m,n))))
        / (2. * pow3(R(m,n)) * pow3(R(m,n)))"""


def patch_lapse_source(text: str) -> str:
    if "JANUS_R_TWIN_F_LAPSE_PATCH" in text:
        raise PatchError("lapse source already appears twin-fluid patched")
    text = _augment_return(
        text, "Real BimetricEvolve::eq_gW_2( Int m, Int n )", DELTA_G
    )
    text = _augment_return(
        text, "Real BimetricEvolve::eq_fW_2( Int m, Int n )", DELTA_F
    )
    anchor = "/** @file  eomLapseRatios.h"
    if anchor in text:
        text = text.replace(anchor, "// JANUS_R_TWIN_F_LAPSE_PATCH\n" + anchor, 1)
    else:
        text = "// JANUS_R_TWIN_F_LAPSE_PATCH\n" + text
    return text


def git_head(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception as exc:
        raise PatchError(f"cannot read git HEAD for {root}") from exc


def patch_checkout(root: Path, *, require_pinned: bool = True) -> Path:
    root = Path(root)
    if require_pinned:
        head = git_head(root)
        if head != PINNED_COMMIT:
            raise PatchError(f"checkout is not pinned at {PINNED_COMMIT}; got {head}")
    path = root / "include/eom-std/eomLapseRatios.h"
    if not path.is_file():
        raise PatchError("missing include/eom-std/eomLapseRatios.h")
    path.write_text(patch_lapse_source(path.read_text()))
    return path

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess

PINNED_COMMIT = "8852e8e9921edeeedf1a447d3bf27b82ec24433c"


class PatchError(RuntimeError):
    pass


def _replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise PatchError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def _replace_function_return_prefix(text: str, signature: str, prefix: str) -> str:
    marker = signature + "\n{\n    return "
    if marker not in text:
        raise PatchError(f"{signature}: function return marker not found")
    return text.replace(marker, signature + "\n{\n    return " + prefix, 1)


F_MATTER_BLOCK = r"""

// Twin-fluid extension: independent f-sector pressureless Valencia fluid.
Real BimetricEvolve::eq_pf_FD_t( Int m, Int n )
{
    return fBet_r(m,n) * pfFD(m,n) + fBet(m,n) * pfFD_r(m,n) + fAlp(m,n) * (-(fDAlp(m,n)
    /*2*/  * pfFD(m,n) * pfFv(m,n)) - pfFD_r(m,n) * pfFv(m,n) - pfFD(m,n) * pfFv_r(m,n))
    /*0*/  + (2 * fBet(m,n) * pfFD(m,n) - 2 * fAlp(m,n) * pfFD(m,n) * pfFv(m,n)) / r(m,n);
}

Real BimetricEvolve::eq_pf_FS_t( Int m, Int n )
{
    return 2 * fBet_r(m,n) * pfFS(m,n) + fBet(m,n) * pfFS_r(m,n) + fAlp(m,n) * (fDA(m,n)
    /*1*/  * pfFS(m,n) * pfFv(m,n) - pfFS_r(m,n) * pfFv(m,n) - pfFS(m,n) * pfFv_r(m,n)
    /*1*/  - fDAlp(m,n) * (pfFD(m,n) + pfFS(m,n) * pfFv(m,n) + pfFtau(m,n))) + (2
    /*1*/  * fBet(m,n) * pfFS(m,n) - 2 * fAlp(m,n) * pfFS(m,n) * pfFv(m,n)) / r(m,n);
}

Real BimetricEvolve::eq_pf_Ftau_t( Int m, Int n )
{
    return fBet_r(m,n) * pfFtau(m,n) + fBet(m,n) * pfFtau_r(m,n) + fAlp(m,n) * (fK1(m,n)
    /*1*/  * pfFS(m,n) * pfFv(m,n) - fDAlp(m,n) * pfFv(m,n) * pfFtau(m,n) - pfFv_r(m,n)
    /*1*/  * pfFtau(m,n) - pfFv(m,n) * pfFtau_r(m,n) - (fDAlp(m,n) * pfFS(m,n))
    /*1*/  / pow2(fA(m,n))) + (2 * fBet(m,n) * pfFtau(m,n) - 2 * fAlp(m,n) * pfFv(m,n)
    /*1*/  * pfFtau(m,n)) / r(m,n);
}

Real BimetricEvolve::eq_pf_Fv( Int m, Int n )
{
    return pfFS(m,n) / ((TINY_Real + pfFD(m,n) + pfFtau(m,n)) * pow2(fA(m,n)));
}

Real BimetricEvolve::eq_pf_Fv_r( Int m, Int n )
{
    return (-2 * fDA(m,n) * pfFS(m,n) * (pfFD(m,n) + pfFtau(m,n)) + pfFS_r(m,n)
    /*1*/  * (pfFD(m,n) + pfFtau(m,n)) - pfFS(m,n) * (pfFD_r(m,n) + pfFtau_r(m,n)))
    /*0*/  / (pow2(fA(m,n)) * pow2(TINY_Real + pfFD(m,n) + pfFtau(m,n)));
}

Real BimetricEvolve::eq_pf_Frho( Int m, Int n )
{
    return (pfFD(m,n) + pfFtau(m,n)) / (fA(m,n) * pow2(fB(m,n)));
}

Real BimetricEvolve::eq_pf_Fj( Int m, Int n )
{
    return pfFS(m,n) / (fA(m,n) * pow2(fB(m,n)));
}

Real BimetricEvolve::eq_pf_FJ1( Int m, Int n )
{
    return (pfFS(m,n) * pfFv(m,n)) / (fA(m,n) * pow2(fB(m,n)));
}

Real BimetricEvolve::eq_pf_FJ2( Int m, Int n )
{
    return 0;
}
"""


def _patch_matter(text: str) -> str:
    if "eq_pf_FD_t" in text:
        raise PatchError("eomMatter.h already appears twin-fluid patched")
    return text.rstrip() + F_MATTER_BLOCK + "\n"


def _patch_sources(text: str) -> str:
    text = _replace_function_return_prefix(
        text,
        "Real BimetricEvolve::eq_f_rho( Int m, Int n )",
        "(pfFD(m,n) + pfFtau(m,n)) / (fA(m,n) * pow2(fB(m,n))) + ",
    )
    text = _replace_function_return_prefix(
        text,
        "Real BimetricEvolve::eq_f_j( Int m, Int n )",
        "pfFS(m,n) / (fA(m,n) * pow2(fB(m,n))) + ",
    )
    text = _replace_function_return_prefix(
        text,
        "Real BimetricEvolve::eq_f_JK( Int m, Int n )",
        "(fAlp(m,n) * (3 * pfFD(m,n) - pfFS(m,n) * pfFv(m,n) + 3 * pfFtau(m,n))) / (2. * fA(m,n) * pow2(fB(m,n))) + ",
    )
    text = _replace_function_return_prefix(
        text,
        "Real BimetricEvolve::eq_f_JKD( Int m, Int n )",
        "(fAlp(m,n) * pfFS(m,n) * pfFv(m,n)) / (fA(m,n) * pow2(fB(m,n))) + ",
    )
    return text


def _patch_constraints(text: str) -> str:
    return _replace_once(
        text,
        "(k_g * pfS(m,n)) / (2. * pow2(gB(m,n)))",
        "(k_g * (pfS(m,n) + pfFS(m,n))) / (2. * pow2(gB(m,n)))",
        label="eq_C_3 twin momentum",
    )


def _patch_misc(text: str) -> str:
    sig = "Real BimetricEvolve::eq_base_p_f( Int m, Int n )"
    marker = sig + "\n{\n    return "
    if marker not in text:
        raise PatchError("eq_base_p_f marker not found")
    start = text.index(marker) + len(marker)
    end = text.index(";\n}", start)
    expr = text[start:end]
    addition = " - pfFS(m,n) / (fA(m,n) * gA(m,n) * pow2(gB(m,n)) * P_2_1(R(m,n)))"
    return text[:start] + expr + addition + text[end:]


def _patch_evolution(text: str) -> str:
    sig = "Real BimetricEvolve::eq_fSig_t( Int m, Int n )"
    marker = sig + "\n{\n    return "
    if marker not in text:
        raise PatchError("eq_fSig_t marker not found")
    start = text.index(marker) + len(marker)
    end = text.index(";\n}", start)
    expr = text[start:end]
    addition = " - (k_f * fAlp(m,n) * pfFS(m,n)) / (2. * pow3(fB(m,n)))"
    return text[:start] + expr + addition + text[end:]


PATCHERS = {
    "include/eom-std/eomMatter.h": _patch_matter,
    "include/eom-std/eomSources.h": _patch_sources,
    "include/eom-std/eomConstraints.h": _patch_constraints,
    "include/eom-std/eomMiscEquations.h": _patch_misc,
    "include/eom-std/eomEvolution.h": _patch_evolution,
}


def patch_text(path: str, text: str) -> str:
    try:
        fn = PATCHERS[path]
    except KeyError as exc:
        raise PatchError(f"unsupported patch target: {path}") from exc
    return fn(text)


def git_head(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception as exc:
        raise PatchError(f"cannot read git HEAD for {root}") from exc


def patch_checkout(root: Path, *, require_pinned: bool = True) -> list[Path]:
    root = Path(root)
    head = git_head(root) if require_pinned else None
    if require_pinned and head != PINNED_COMMIT:
        raise PatchError(
            f"checkout is not pinned upstream {PINNED_COMMIT}; got {head}"
        )
    changed = []
    for rel in PATCHERS:
        path = root / rel
        if not path.is_file():
            raise PatchError(f"missing upstream file: {rel}")
        original = path.read_text()
        updated = patch_text(rel, original)
        path.write_text(updated)
        changed.append(path)
    return changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("checkout", type=Path)
    ap.add_argument("--allow-unpinned", action="store_true")
    args = ap.parse_args()
    changed = patch_checkout(args.checkout, require_pinned=not args.allow_unpinned)
    for path in changed:
        print(path)
    print("Equation/source twin-fluid patch applied.")
    print("NOTE: state registration and full lapse W2 runtime patch are separate gates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

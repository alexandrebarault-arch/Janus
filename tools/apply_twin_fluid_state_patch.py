from __future__ import annotations

from pathlib import Path
import argparse
import subprocess

PINNED_COMMIT = "8852e8e9921edeeedf1a447d3bf27b82ec24433c"


class PatchError(RuntimeError):
    pass


def _once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise PatchError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def patch_state_source(text: str) -> str:
    if "pfFD, pfFS, pfFtau" in text:
        raise PatchError("state source already appears twin-fluid patched")

    replacements = [
        (
            "pfD, pfS, pftau,                  //!< State variables for the PF",
            "pfD, pfS, pftau,                  //!< State variables for the g-sector PF\n"
            "        pfFD, pfFS, pfFtau,               //!< State variables for the f-sector PF",
            "enum conserved state",
        ),
        (
            "pfv,                       //!< The three-velocity of the PF",
            "pfv,                       //!< The three-velocity of the g PF\n"
            "        pfFv,                      //!< The three-velocity of the f PF",
            "enum primitive velocities",
        ),
        ("mpiBoundary = pfv", "mpiBoundary = pfFv", "mpi boundary"),
        (
            "pfD_t, pfS_t, pftau_t, p_t,",
            "pfD_t, pfS_t, pftau_t,\n        pfFD_t, pfFS_t, pfFtau_t, p_t,",
            "rhs state",
        ),
        (
            "pfD_r, pfS_r, pftau_r, pfv_r,",
            "pfD_r, pfS_r, pftau_r, pfv_r,\n        pfFD_r, pfFS_r, pfFtau_r, pfFv_r,",
            "cached radial derivatives",
        ),
        (
            "pfD, pfS, pftau\n    };",
            "pfD, pfS, pftau,\n        pfFD, pfFS, pfFtau\n    };",
            "input state",
        ),
        (
            "{ pfD, pfD_t },  { pfS, pfS_t },  { pftau, pftau_t }",
            "{ pfD, pfD_t },  { pfS, pfS_t },  { pftau, pftau_t },\n"
            "        { pfFD, pfFD_t }, { pfFS, pfFS_t }, { pfFtau, pfFtau_t }",
            "evolved state",
        ),
        (
            '{ pftau_t,  "pftau_t",  "\\\\partial_t \\\\hat\\\\tau"          },',
            '{ pftau_t,  "pftau_t",  "\\\\partial_t \\\\hat\\\\tau"          },\n'
            '        { pfFD,     "pfFD",     "Df" },\n'
            '        { pfFS,     "pfFS",     "Sf" },\n'
            '        { pfFtau,   "pfFtau",   "tauf" },\n'
            '        { pfFv,     "pfFv",     "vf" },\n'
            '        { pfFD_t,   "pfFD_t",   "Df_t" },\n'
            '        { pfFS_t,   "pfFS_t",   "Sf_t" },\n'
            '        { pfFtau_t, "pfFtau_t", "tauf_t" },',
            "output state",
        ),
        (
            '{ pfv_r,    "pfv_r",    "\\\\partial_r \\\\hat v"             },',
            '{ pfv_r,    "pfv_r",    "\\\\partial_r \\\\hat v"             },\n'
            '        { pfFD_r,   "pfFD_r",   "Df_r" },\n'
            '        { pfFS_r,   "pfFS_r",   "Sf_r" },\n'
            '        { pfFtau_r, "pfFtau_r", "tauf_r" },\n'
            '        { pfFv_r,   "pfFv_r",   "vf_r" },',
            "diagnostic derivatives",
        ),
        (
            "emitField(pfv)     emitField(pfv_r)",
            "emitField(pfv)     emitField(pfv_r)\n"
            "    emitField(pfFD)    emitField(pfFD_t)\n"
            "    emitField(pfFS)    emitField(pfFS_t)\n"
            "    emitField(pfFtau)  emitField(pfFtau_t)\n"
            "    emitField(pfFv)    emitField(pfFv_r)",
            "field accessors",
        ),
        (
            "emitDerivative_r( pftau )",
            "emitDerivative_r( pftau )\n"
            "    emitDerivative_r( pfFD   )\n"
            "    emitDerivative_r( pfFS   )\n"
            "    emitDerivative_r( pfFtau )",
            "derivative accessors",
        ),
        (
            "Real eq_pf_J2     ( Int m, Int n );",
            "Real eq_pf_J2     ( Int m, Int n );\n\n"
            "    Real eq_pf_Fv      ( Int m, Int n );\n"
            "    Real eq_pf_Fv_r    ( Int m, Int n );\n"
            "    Real eq_pf_FD_t    ( Int m, Int n );\n"
            "    Real eq_pf_FS_t    ( Int m, Int n );\n"
            "    Real eq_pf_Ftau_t  ( Int m, Int n );\n"
            "    Real eq_pf_Frho    ( Int m, Int n );\n"
            "    Real eq_pf_Fj      ( Int m, Int n );\n"
            "    Real eq_pf_FJ1     ( Int m, Int n );\n"
            "    Real eq_pf_FJ2     ( Int m, Int n );",
            "f-fluid declarations",
        ),
        (
            "pfv(m,n) = pfS(m,n) == 0 ? 0 : eq_pf_v(m,n);",
            "pfv(m,n) = pfS(m,n) == 0 ? 0 : eq_pf_v(m,n);\n"
            "        pfFv(m,n) = pfFS(m,n) == 0 ? 0 : eq_pf_Fv(m,n);",
            "derived f velocity",
        ),
        (
            "pfD   (m,n) = pfD    (m,nR);\n"
            "        pfS   (m,n) = -pfS   (m,nR);\n"
            "        pftau (m,n) = pftau  (m,nR);",
            "pfD   (m,n) = pfD    (m,nR);\n"
            "        pfS   (m,n) = -pfS   (m,nR);\n"
            "        pftau (m,n) = pftau  (m,nR);\n"
            "        pfFD   (m,n) = pfFD    (m,nR);\n"
            "        pfFS   (m,n) = -pfFS   (m,nR);\n"
            "        pfFtau (m,n) = pfFtau  (m,nR);",
            "left conserved parity",
        ),
        (
            "pfv   (m,n) = -pfv   (m,nR);",
            "pfv   (m,n) = -pfv   (m,nR);\n        pfFv  (m,n) = -pfFv  (m,nR);",
            "left primitive parity",
        ),
        (
            "extrapolate_R( fld::pftau, m, n );",
            "extrapolate_R( fld::pftau, m, n );\n"
            "        extrapolate_R( fld::pfFD,   m, n );\n"
            "        extrapolate_R( fld::pfFS,   m, n );\n"
            "        extrapolate_R( fld::pfFtau, m, n );",
            "right conserved extrapolation",
        ),
        (
            "extrapolate_R( fld::pfv, m, n );",
            "extrapolate_R( fld::pfv,  m, n );\n        extrapolate_R( fld::pfFv, m, n );",
            "right primitive extrapolation",
        ),
        (
            "pftau_r(m,n) = GF_r( pftau, m,n );",
            "pftau_r(m,n) = GF_r( pftau, m,n );\n"
            "        pfFD_r  (m,n) = GF_r( pfFD,   m,n );\n"
            "        pfFS_r  (m,n) = GF_r( pfFS,   m,n );\n"
            "        pfFtau_r(m,n) = GF_r( pfFtau, m,n );",
            "f radial conserved derivatives",
        ),
        (
            "pfv_r(m,n) = pfS(m,n) == 0 ? 0 : eq_pf_v_r( m, n );",
            "pfv_r(m,n)  = pfS(m,n)  == 0 ? 0 : eq_pf_v_r( m, n );\n"
            "        pfFv_r(m,n) = pfFS(m,n) == 0 ? 0 : eq_pf_Fv_r( m, n );",
            "f radial primitive derivative",
        ),
        (
            "pftau_t (m,n) = eq_pf_tau_t(m,n);",
            "pftau_t (m,n) = eq_pf_tau_t(m,n);\n"
            "        pfFD_t   (m,n) = eq_pf_FD_t   (m,n);\n"
            "        pfFS_t   (m,n) = eq_pf_FS_t   (m,n);\n"
            "        pfFtau_t (m,n) = eq_pf_Ftau_t (m,n);",
            "f fluid rhs",
        ),
    ]

    for old, new, label in replacements:
        text = _once(text, old, new, label)
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
    head = git_head(root) if require_pinned else None
    if require_pinned and head != PINNED_COMMIT:
        raise PatchError(f"checkout is not pinned at {PINNED_COMMIT}; got {head}")
    path = root / "src/bim-solver-std.cpp"
    if not path.is_file():
        raise PatchError("missing src/bim-solver-std.cpp")
    path.write_text(patch_state_source(path.read_text()))
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("checkout", type=Path)
    ap.add_argument("--allow-unpinned", action="store_true")
    args = ap.parse_args()
    changed = patch_checkout(args.checkout, require_pinned=not args.allow_unpinned)
    print(changed)
    print("Twin-fluid standard-3+1 state registration patch applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

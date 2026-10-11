from __future__ import annotations

from pathlib import Path
import argparse
import json
import shutil
import subprocess
import numpy as np


PINNED_UPSTREAM = "8852e8e9921edeeedf1a447d3bf27b82ec24433c"


def std_build_command(checkout: Path, binary: Path, *, compiler: str = "g++") -> list[str]:
    checkout = Path(checkout)
    binary = Path(binary)
    return [
        compiler,
        "-std=c++14",
        "-O3",
        "-fopenmp",
        "-m64",
        "-DV_SIGN=-",
        "-DCFDS_ORDER=4",
        f"-I{checkout / 'include'}",
        str(checkout / "src" / "bim-solver-std.cpp"),
        "-o",
        str(binary),
    ]


def make_zero_f_inputs(full_patched_rows: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return patched-zero-f and exact-upstream input arrays from one common state."""
    from numerics.upstream_baseline_input import patched_to_upstream_rows

    rows = np.asarray(full_patched_rows, dtype=float)
    if rows.ndim != 2 or rows.shape[1] != 26:
        raise ValueError("full patched input must have 26 columns including radius")
    patched = np.array(rows, copy=True)
    patched[:, -3:] = 0.0
    upstream = patched_to_upstream_rows(patched)
    return patched, upstream


def physical_domain_ok(summary: dict) -> bool:
    required = (
        "all_finite",
        "same_oriented_lapse",
        "metric_positive",
        "density_nonnegative",
        "fluid_subluminal",
    )
    return all(bool(summary.get(key, False)) for key in required)


def _run(command: list[str], *, cwd: Path, label: str) -> None:
    proc = subprocess.run(command, cwd=Path(cwd), text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed with exit code {proc.returncode}: {command}")


def _build(checkout: Path, binary: Path, *, compiler: str) -> None:
    if shutil.which(compiler) is None:
        raise RuntimeError(f"compiler not found: {compiler}")
    binary = Path(binary)
    binary.parent.mkdir(parents=True, exist_ok=True)
    _run(std_build_command(checkout, binary, compiler=compiler), cwd=checkout, label="C++ build")
    if not binary.exists():
        raise RuntimeError(f"build returned success but binary is missing: {binary}")


def _write_rows(path: Path, rows: np.ndarray) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(Path(path), np.asarray(rows, dtype=float), fmt="%.17g")


def _write_config(
    directory: Path,
    *,
    n: int,
    delta_r: float,
    input_name: str,
    output_name: str,
    steps: int,
    cfl: float,
) -> Path:
    from numerics.bim_solver_reference_config import reference_config_text

    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "config.ini"
    path.write_text(
        reference_config_text(
            n=n,
            delta_r=delta_r,
            input_file=input_name,
            output_file=output_name,
            steps=steps,
            cfl=cfl,
        )
    )
    return path


def execute_a1(
    checkout: Path,
    workdir: Path,
    *,
    n: int = 500,
    delta_r: float = 0.05,
    solve_points: int = 1200,
    steps: int = 20,
    cfl: float = 0.1,
    compiler: str = "g++",
    regression_abs_tol: float = 1.0e-11,
    regression_rel_tol: float = 1.0e-11,
) -> dict:
    """Execute the first real twin-fluid standard-3+1 gate in a local GPL checkout.

    The checkout is verified while pristine, compiled once, then patched in place
    and compiled again.  The untouched executable is retained, so upstream and
    patched zero-f runs use two genuinely different binaries against the exact
    same common initial state.
    """
    from numerics.reference_bim_solver_twin_input import reference_wall_rows
    from tools.verify_upstream_manifest import verify_manifest
    from tools.prepare_bim_solver_twin import prepare_checkout
    from tools.compare_bim_solver_outputs import compare_output_files, require_regression
    from tools.analyze_bim_solver_output import parse_text_output, short_run_summary

    checkout = Path(checkout).resolve()
    workdir = Path(workdir).resolve()
    if not checkout.is_dir():
        raise ValueError(f"checkout does not exist: {checkout}")
    if n < 4 or delta_r <= 0 or steps <= 0 or not (0 < cfl <= 0.5):
        raise ValueError("invalid A1 grid/time configuration")

    # Prove that the source tree is exactly the audited upstream before mutation.
    verify_manifest(checkout)

    bin_dir = workdir / "bin"
    upstream_binary = bin_dir / "bim-solver-std-upstream"
    patched_binary = bin_dir / "bim-solver-std-twin"
    _build(checkout, upstream_binary, compiler=compiler)

    # One constrained Janus-like geometry is used to derive all three run inputs.
    ref = reference_wall_rows(
        n=n,
        delta_r=delta_r,
        solve_points=solve_points,
    )
    full_rows = np.asarray(ref["rows"], dtype=float)
    patched_zero_rows, upstream_zero_rows = make_zero_f_inputs(full_rows)

    upstream_dir = workdir / "upstream_zero_f"
    patched_zero_dir = workdir / "patched_zero_f"
    twin_dir = workdir / "patched_twin"

    _write_rows(upstream_dir / "initial.txt", upstream_zero_rows)
    _write_config(
        upstream_dir,
        n=n,
        delta_r=delta_r,
        input_name="initial.txt",
        output_name="output.txt",
        steps=steps,
        cfl=cfl,
    )
    _run([str(upstream_binary), "config.ini"], cwd=upstream_dir, label="untouched upstream zero-f run")

    # Patch only after the untouched binary and reference output exist.
    prepare_checkout(checkout)
    _build(checkout, patched_binary, compiler=compiler)

    _write_rows(patched_zero_dir / "initial.txt", patched_zero_rows)
    _write_config(
        patched_zero_dir,
        n=n,
        delta_r=delta_r,
        input_name="initial.txt",
        output_name="output.txt",
        steps=steps,
        cfl=cfl,
    )
    _run([str(patched_binary), "config.ini"], cwd=patched_zero_dir, label="patched zero-f run")

    comparison = compare_output_files(
        upstream_dir / "output.txt",
        patched_zero_dir / "output.txt",
        n_ghost=10,
    )
    require_regression(
        comparison,
        abs_tol=regression_abs_tol,
        rel_tol=regression_rel_tol,
    )

    _write_rows(twin_dir / "initial.txt", full_rows)
    _write_config(
        twin_dir,
        n=n,
        delta_r=delta_r,
        input_name="initial.txt",
        output_name="output.txt",
        steps=steps,
        cfl=cfl,
    )
    _run([str(patched_binary), "config.ini"], cwd=twin_dir, label="patched twin-wall run")

    twin_summary = short_run_summary(
        parse_text_output(twin_dir / "output.txt"),
        n_ghost=10,
    )

    return {
        "pinned_upstream": PINNED_UPSTREAM,
        "upstream_binary": str(upstream_binary),
        "patched_binary": str(patched_binary),
        "reference_W_min": float(ref["W_min"]),
        "reference_W_max": float(ref["W_max"]),
        "zero_f_regression": {
            "worst_abs_field": comparison.worst_abs_field,
            "worst_abs": comparison.worst_abs,
            "worst_rel_field": comparison.worst_rel_field,
            "worst_rel": comparison.worst_rel,
            "common_field_count": len(comparison.fields),
        },
        "twin_physical_domain_ok": physical_domain_ok(twin_summary),
        "twin_summary": twin_summary,
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Compile/run the local JANUS-R A1 twin-fluid standard-3+1 gate."
    )
    ap.add_argument("checkout", type=Path, help="pristine pinned nubirel/bim-solver checkout")
    ap.add_argument("workdir", type=Path, help="separate output/build directory")
    ap.add_argument("--n", type=int, default=500)
    ap.add_argument("--delta-r", type=float, default=0.05)
    ap.add_argument("--solve-points", type=int, default=1200)
    ap.add_argument("--steps", type=int, default=20)
    ap.add_argument("--cfl", type=float, default=0.1)
    ap.add_argument("--compiler", default="g++")
    ap.add_argument("--regression-abs-tol", type=float, default=1.0e-11)
    ap.add_argument("--regression-rel-tol", type=float, default=1.0e-11)
    args = ap.parse_args()

    report = execute_a1(
        args.checkout,
        args.workdir,
        n=args.n,
        delta_r=args.delta_r,
        solve_points=args.solve_points,
        steps=args.steps,
        cfl=args.cfl,
        compiler=args.compiler,
        regression_abs_tol=args.regression_abs_tol,
        regression_rel_tol=args.regression_rel_tol,
    )
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=True))
    if not report["twin_physical_domain_ok"]:
        print("A1 hard physical-domain gate: FAIL")
        return 2
    print("A1 hard physical-domain gate: PASS (constraints/convergence still require A2)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Generate the complete first-run bundle for patched bim-solver STD."""
from __future__ import annotations

from pathlib import Path
import argparse

from numerics.reference_bim_solver_twin_input import write_reference_wall_input
from numerics.bim_solver_reference_config import reference_config_text


def generate_reference_run(
    directory: Path,
    *,
    n: int,
    delta_r: float,
    solve_points: int = 600,
    steps: int = 20,
):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    initial_path = directory / "initial.txt"
    config_path = directory / "config.ini"

    result = write_reference_wall_input(
        initial_path,
        n=n,
        delta_r=delta_r,
        solve_points=solve_points,
    )
    config_path.write_text(
        reference_config_text(
            n=n,
            delta_r=delta_r,
            input_file=initial_path.name,
            output_file="output.txt",
            steps=steps,
        )
    )
    result = dict(result)
    result.update(initial_path=initial_path, config_path=config_path)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("directory", type=Path)
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--delta-r", type=float, default=0.05)
    ap.add_argument("--solve-points", type=int, default=1200)
    ap.add_argument("--steps", type=int, default=20)
    args = ap.parse_args()
    result = generate_reference_run(
        args.directory,
        n=args.n,
        delta_r=args.delta_r,
        solve_points=args.solve_points,
        steps=args.steps,
    )
    print(result["initial_path"])
    print(result["config_path"])
    print(f"W_min={result['W_min']:.12g} W_max={result['W_max']:.12g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

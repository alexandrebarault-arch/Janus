"""Reference short-run configuration for the patched bim-solver STD gate."""
from __future__ import annotations


def _fmt(x: float) -> str:
    return f"{float(x):.15g}"


def reference_config_text(
    *,
    n: int,
    delta_r: float,
    input_file: str,
    output_file: str,
    steps: int = 20,
    cfl: float = 0.1,
) -> str:
    if n <= 0 or delta_r <= 0 or steps <= 0 or not (0 < cfl <= 0.5):
        raise ValueError("invalid grid, step count or CFL fraction")
    dt = float(delta_r) * float(cfl)
    t1 = dt * int(steps)

    # Reference Gate-A0 interaction: beta=(-2.4, 1, -0.2, 0, -0.4)
    # multiplied by interaction=0.02, matching the constraint/lapse generator.
    b = (-0.048, 0.02, -0.004, 0.0, -0.008)
    lines = [
        "# JANUS-R reference twin-wall short-run configuration",
        "model.title = JANUS-R twin-wall A1 short gate",
        "model.k_g = 1",
        "model.k_f = 1",
        f"model.b_0 = {_fmt(b[0])}",
        f"model.b_1 = {_fmt(b[1])}",
        f"model.b_2 = {_fmt(b[2])}",
        f"model.b_3 = {_fmt(b[3])}",
        f"model.b_4 = {_fmt(b[4])}",
        "",
        f"grid.nLen = {int(n)}",
        "grid.nGhost = 10",
        f"grid.delta_r = {_fmt(delta_r)}",
        "",
        f"input.file = {input_file}",
        "input.binary = 0",
        "",
        f"output.file = {output_file}",
        "output.binary = 0",
        "out.diagnostics = 1",
        f"output.nOut = {int(n)}",
        "output.nSkip = 1",
        "output.mSkip = 1",
        "checkNaNs.nFrom = 0",
        f"checkNaNs.nTo = {int(n)}",
        "",
        "slicing.method = constg",
        "slicing.smooth = 0",
        "",
        "integ.t_0 = 0",
        f"integ.t_1 = {_fmt(t1)}",
        f"integ.delta_t = {_fmt(dt)}",
        "integ.method = RK4",
        "integ.dissip = 0",
        "adpt.enabled = 0",
        "",
    ]
    return "\n".join(lines)

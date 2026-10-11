from numerics.bim_solver_reference_config import reference_config_text


def parse_config(text):
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, value = line.split("=", 1)
        out[key.strip()] = value.strip()
    return out


def test_reference_config_matches_wall_model_and_short_control_run():
    cfg = parse_config(
        reference_config_text(
            n=400,
            delta_r=0.05,
            input_file="wall.txt",
            output_file="wall-out.txt",
            steps=20,
        )
    )
    assert cfg["grid.nLen"] == "400"
    assert cfg["grid.delta_r"] == "0.05"
    assert cfg["input.file"] == "wall.txt"
    assert cfg["input.binary"] == "0"
    assert cfg["output.file"] == "wall-out.txt"
    assert cfg["output.binary"] == "0"
    assert cfg["out.diagnostics"] == "1"
    assert cfg["slicing.method"] == "constg"
    assert cfg["integ.method"] == "RK4"
    assert float(cfg["integ.delta_t"]) == 0.005
    assert float(cfg["integ.t_1"]) == 0.1
    assert float(cfg["model.k_g"]) == 1.0
    assert float(cfg["model.k_f"]) == 1.0
    assert float(cfg["model.b_0"]) == -0.048
    assert float(cfg["model.b_1"]) == 0.02
    assert float(cfg["model.b_2"]) == -0.004
    assert float(cfg["model.b_3"]) == 0.0
    assert float(cfg["model.b_4"]) == -0.008


def test_reference_config_accepts_sector_dual_coefficients_and_title():
    dual = (-0.008, 0.0, -0.004, 0.02, -0.048)
    cfg = parse_config(
        reference_config_text(
            n=100,
            delta_r=0.1,
            input_file="dual.txt",
            output_file="dual-out.txt",
            steps=4,
            b=dual,
            title="JANUS-R f-only sector-dual control",
        )
    )
    assert cfg["model.title"] == "JANUS-R f-only sector-dual control"
    assert tuple(float(cfg[f"model.b_{i}"]) for i in range(5)) == dual

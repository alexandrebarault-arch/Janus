from numerics.reference_export_constraint_scan import scan_reference_constraints


def test_reference_export_constraint_error_decreases_with_resolution():
    result = scan_reference_constraints(
        n_values=(50, 100, 200),
        solve_points=500,
        tol=1e-6,
    )
    assert result["bvp_success"]
    vals = [x["core_max"] for x in result["levels"]]
    assert vals[0] > vals[1] > vals[2]
    assert vals[0] / vals[1] > 2.5
    assert vals[1] / vals[2] > 2.5

"""Reproducible parameter points used only as JANUS-R V2 controls.

These are exploratory scan points, not viable-model claims.  They are kept in
a separate module so regression tests can compare qualitatively different
parts of the stability/mixing tradeoff without promoting either point as a
preferred cosmology.
"""

from numerics.two_matter_flrw import Beta, Model


def v2_late_mixing_control_candidate() -> Model:
    """Control with stronger late mixing but only late W/Higuchi health.

    Exploratory diagnostics for this point give approximately:

    - beta0 = 0;
    - low-redshift H(z) within ~1% of flat Lambda-CDM in the scan;
    - present mixing proxy epsilon_mix ~ 0.044;
    - W crosses zero around z ~ 3.15 when followed backwards.

    The point is intentionally useful as a stress test: it demonstrates that a
    strong late twin-sector response can coexist with a reasonable background,
    while also making the early-stability problem explicit.
    """

    return Model(
        beta=Beta(
            beta0=0.0,
            beta1=42.23624761582522,
            beta2=-16.7813778305864,
            beta3=52.18063114248909,
            beta4=-57.30850726939942,
        ),
        alpha=0.0873167979632736,
        y0=2.457944555998458,
    ).calibrated()

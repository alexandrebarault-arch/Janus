"""Small stability/mixing diagnostics for JANUS-R V2.

The functions here are intentionally minimal and traceable to analytic
expressions used in the V2 gate. They are not a substitute for the full scalar
kinetic matrix.

Notation
--------
`alpha = M_f/M_g`, `y = a_f/a_g`, and

    J(y) = beta1 + 2 beta2 y + beta3 y^2.

For a spatially flat healthy-branch background, De Felice et al. write the
extended Higuchi quantity as

    W = m^2 (1 + kappa y^2) J / (2 kappa y) - H^2,

with `kappa = M_f^2/M_g^2 = alpha^2`.

`visible_massive_mixing_proxy` is only a bounded proxy for how far the visible
metric is from the small-alpha GR decoupling limit. On proportional
backgrounds the mass-eigenstate rotation is controlled by the combination
`alpha*y`; the massive-mode contribution to the visible metric is suppressed
by powers of this quantity as `alpha -> 0`.
"""


def higuchi_w_flat(*, m2: float, alpha: float, y: float, j: float, h2: float) -> float:
    if alpha <= 0 or y <= 0:
        raise ValueError("alpha and y must be positive")
    return 0.5 * m2 * (1.0 + alpha * alpha * y * y) * j / (alpha * alpha * y) - h2


def visible_massive_mixing_proxy(*, alpha: float, y: float) -> float:
    """Return q/(1+q), q=(alpha*y)^2, as a qualitative mixing indicator."""
    if alpha < 0 or y < 0:
        raise ValueError("alpha and y must be non-negative")
    q = (alpha * y) ** 2
    return q / (1.0 + q)

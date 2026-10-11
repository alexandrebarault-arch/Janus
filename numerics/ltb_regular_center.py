"""Regular-center consequences of the separable LTB-LTB constraints.

Nersisyan-Akrami-Amendola (2015) obtain, for their consistent LTB-LTB
subclass,

    s'^2/q^2 - 1 = C3 s^2
    s' q' - q s'' = C4 s q^3.

Solving the first equation for q and substituting in the second gives
`C4=-C3` away from the trivial center. With their separation
`A=C1 B_e q`, `B=B_e s`, a regular spherical center requires `C1=1`;
otherwise the proper radial distance and areal-radius circumference have a
conical mismatch. The same statement applies to the f metric.

For a regular center, after `chi=s(r)` the spatial metric becomes

    B_e(t)^2 [dchi^2/(1+C3 chi^2) + chi^2 dOmega^2],

which is a constant-curvature FLRW spatial metric with `k=-C3`.

Scope: this applies to the separable/comoving LTB-LTB subclass analyzed in
arXiv:1502.03988. It is not a no-go for every spherically symmetric bimetric
geometry.
"""


def required_c4(c3: float) -> float:
    return -float(c3)


def regular_center_defect(c1: float) -> float:
    """Absolute mismatch of proper-radius vs areal-radius normalization."""
    if c1 <= 0:
        raise ValueError("c1 must be positive")
    return abs(float(c1) - 1.0)


def radial_metric_factor(*, chi: float, c3: float, c1: float = 1.0) -> float:
    """Dimensionless radial coefficient after the coordinate `chi=s(r)`."""
    den = 1.0 + float(c3) * float(chi) ** 2
    if den <= 0:
        raise ValueError("outside coordinate patch")
    return float(c1) ** 2 / den

import math

from numerics.stability_mixing import higuchi_w_flat, visible_massive_mixing_proxy


def test_flat_higuchi_w_matches_v2_regression_today():
    m2 = 0.10817769352495572
    alpha = 0.67838201203862
    y = 1.4009642016702197
    beta1 = 2.879912363842445
    beta2 = 1.0433553612848283
    beta3 = 0.4228370163756705
    j = beta1 + 2.0 * beta2 * y + beta3 * y * y
    w = higuchi_w_flat(m2=m2, alpha=alpha, y=y, j=j, h2=1.0)
    assert math.isclose(w, 0.05913156224828087, rel_tol=0, abs_tol=1e-12)


def test_small_alpha_decouples_visible_massive_mode_proxy():
    proxy = visible_massive_mixing_proxy(alpha=1.0e-7, y=0.25)
    assert proxy < 1.0e-14


def test_order_one_alpha_y_gives_order_one_mixing_proxy():
    proxy = visible_massive_mixing_proxy(alpha=1.0, y=1.0)
    assert math.isclose(proxy, 0.5, rel_tol=0, abs_tol=1e-15)

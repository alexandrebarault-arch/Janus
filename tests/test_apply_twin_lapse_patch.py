import pytest

from tools.apply_twin_lapse_patch import PatchError, patch_lapse_source


def fixture():
    return """Real BimetricEvolve::eq_gW_2( Int m, Int n )
{
    return G_EXISTING;
}

Real BimetricEvolve::eq_fW_2( Int m, Int n )
{
    return F_EXISTING;
}
"""


def test_adds_missing_f_dust_blocks_to_both_W2_functions():
    out = patch_lapse_source(fixture())
    assert "G_EXISTING" in out
    assert "F_EXISTING" in out
    assert "pfFD(m,n) + pfFtau(m,n)" in out
    assert "pfFD(m,n) - pfFS(m,n) * pfFv(m,n) + pfFtau(m,n)" in out
    assert "pfFS(m,n) * pfFv(m,n)" in out
    assert "b_1 + b_2 * R(m,n)" in out
    assert "b_1 - b_3 * pow2(R(m,n))" in out


def test_zero_f_state_makes_added_blocks_symbolically_zero_by_factor_structure():
    out = patch_lapse_source(fixture())
    assert "(pfFD(m,n) + pfFtau(m,n))" in out
    assert out.count("pfFD(m,n)") >= 3
    assert out.count("pfFS(m,n)") >= 3


def test_refuses_double_patch():
    once = patch_lapse_source(fixture())
    with pytest.raises(PatchError):
        patch_lapse_source(once)


def test_generated_patch_has_balanced_delimiters():
    out = patch_lapse_source(fixture())
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in out:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            assert stack and stack[-1] == pairs[ch], (ch, stack[-3:])
            stack.pop()
    assert not stack

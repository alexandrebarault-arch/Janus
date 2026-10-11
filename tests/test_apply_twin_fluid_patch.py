import pytest

from tools.apply_twin_fluid_patch import PatchError, patch_text


def test_matter_header_adds_independent_f_valencia_state():
    src = """Real BimetricEvolve::eq_pf_J2( Int m, Int n )
{
    return 0;
}
"""
    out = patch_text("include/eom-std/eomMatter.h", src)
    assert "eq_pf_FD_t" in out
    assert "fBet_r(m,n) * pfFD(m,n)" in out
    assert "eq_pf_Fv" in out
    assert "pow2(fA(m,n))" in out


def test_sources_add_f_matter_exactly_once():
    src = """Real BimetricEvolve::eq_f_rho( Int m, Int n )
{
    return -INTERACTION_RHO;
}
Real BimetricEvolve::eq_f_j( Int m, Int n )
{
    return INTERACTION_J;
}
Real BimetricEvolve::eq_f_JK( Int m, Int n )
{
    return INTERACTION_JK;
}
Real BimetricEvolve::eq_f_JKD( Int m, Int n )
{
    return INTERACTION_JKD;
}
"""
    out = patch_text("include/eom-std/eomSources.h", src)
    assert out.count("(pfFD(m,n) + pfFtau(m,n)) / (fA(m,n) * pow2(fB(m,n)))") == 1
    assert out.count("pfFS(m,n) / (fA(m,n) * pow2(fB(m,n)))") == 1
    assert "fAlp(m,n) * (3 * pfFD(m,n) - pfFS(m,n) * pfFv(m,n) + 3 * pfFtau(m,n))" in out
    assert "fAlp(m,n) * pfFS(m,n) * pfFv(m,n)" in out


def test_constraint_misc_and_evolution_receive_f_momentum():
    c = """Real BimetricEvolve::eq_C_3( Int m, Int n )
{
    return A - (k_g * pfS(m,n)) / (2. * pow2(gB(m,n))) + B;
}
"""
    out = patch_text("include/eom-std/eomConstraints.h", c)
    assert "(pfS(m,n) + pfFS(m,n))" in out

    m = """Real BimetricEvolve::eq_base_p_f( Int m, Int n )
{
    return BASE;
}
"""
    out = patch_text("include/eom-std/eomMiscEquations.h", m)
    assert "- pfFS(m,n) / (fA(m,n) * gA(m,n) * pow2(gB(m,n)) * P_2_1(R(m,n)))" in out

    e = """Real BimetricEvolve::eq_fSig_t( Int m, Int n )
{
    return GEOM - INTERACTION;
}
"""
    out = patch_text("include/eom-std/eomEvolution.h", e)
    assert "- (k_f * fAlp(m,n) * pfFS(m,n)) / (2. * pow3(fB(m,n)))" in out


def test_unknown_file_refuses_patch():
    with pytest.raises(PatchError):
        patch_text("unknown.cpp", "x")

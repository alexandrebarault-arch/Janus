"""Syntax-only C++ smoke test for generated twin-fluid source fragments."""
from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import tempfile

from tools.apply_twin_fluid_patch import F_MATTER_BLOCK
from tools.apply_twin_lapse_patch import DELTA_G, DELTA_F


def _harness() -> str:
    fields = [
        "fBet_r", "pfFD", "fBet", "pfFD_r", "fAlp", "fDAlp", "pfFv", "pfFv_r",
        "pfFS", "pfFS_r", "fDA", "pfFtau", "pfFtau_r", "fK1", "fA", "fB",
        "gA", "p", "R", "Lt", "r",
    ]
    field_methods = "\n".join(
        f"    Real {name}(Int,Int) const {{ return 1.0; }}" for name in fields
    )
    declarations = """
    Real eq_pf_FD_t(Int,Int); Real eq_pf_FS_t(Int,Int); Real eq_pf_Ftau_t(Int,Int);
    Real eq_pf_Fv(Int,Int); Real eq_pf_Fv_r(Int,Int); Real eq_pf_Frho(Int,Int);
    Real eq_pf_Fj(Int,Int); Real eq_pf_FJ1(Int,Int); Real eq_pf_FJ2(Int,Int);
    Real delta_g(Int m,Int n) { return DELTA_G_TOKEN; }
    Real delta_f(Int m,Int n) { return DELTA_F_TOKEN; }
""".replace("DELTA_G_TOKEN", DELTA_G).replace("DELTA_F_TOKEN", DELTA_F)
    return f"""#include <cmath>
using Real=double; using Int=int;
constexpr Real TINY_Real=1e-12;
template<class T> inline T pow2(T x){{return x*x;}}
template<class T> inline T pow3(T x){{return x*x*x;}}
class BimetricEvolve {{
public:
    Real k_f=1.0, b_1=1.0, b_2=0.1, b_3=0.01;
{field_methods}
{declarations}
}};
{F_MATTER_BLOCK}
int main(){{ BimetricEvolve b; return (int)(b.delta_g(0,0)+b.delta_f(0,0)); }}
"""


def compile_patch_fragments(
    compiler: str | None = None,
) -> subprocess.CompletedProcess[str]:
    compiler = compiler or shutil.which("g++") or shutil.which("clang++")
    if not compiler:
        raise RuntimeError("no C++ compiler available")
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "patch_smoke.cpp"
        path.write_text(_harness())
        return subprocess.run(
            [
                compiler,
                "-std=c++17",
                "-Wall",
                "-Wextra",
                "-pedantic",
                "-fsyntax-only",
                str(path),
            ],
            text=True,
            capture_output=True,
            check=False,
        )

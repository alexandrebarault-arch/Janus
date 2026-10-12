from tools.cxx_patch_syntax import compile_patch_fragments


def test_generated_twin_cpp_fragments_pass_syntax_only():
    result = compile_patch_fragments()
    assert result.returncode == 0, result.stderr

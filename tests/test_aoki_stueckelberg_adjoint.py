
def test_constant_coefficient_adjoint_matches_fourier_integration_by_parts():
    from numerics.aoki_stueckelberg_adjoint import pi_adjoint_residual
    A,B,C,D=-0.7,0.2,1.3,-0.4
    omega=2.1; k=3.4
    Ee=1.2-0.7j; Er=-0.3+0.8j
    out=pi_adjoint_residual(
        E_eta=Ee,E_r=Er,
        E_eta_t=-1j*omega*Ee,E_eta_r=1j*k*Ee,
        E_r_t=-1j*omega*Er,E_r_r=1j*k*Er,
        A=A,B=B,C=C,D=D,
        A_t=0.0,B_r=0.0,C_r=0.0,D_t=0.0,
    )
    expected=1j*omega*(A*Ee+D*Er)-1j*k*(B*Ee+C*Er)
    assert abs(out-expected)<1e-13


def test_variable_coefficient_adjoint_includes_required_product_rule_terms():
    from numerics.aoki_stueckelberg_adjoint import pi_adjoint_residual
    out=pi_adjoint_residual(
        E_eta=2.0,E_r=-3.0,
        E_eta_t=5.0,E_eta_r=7.0,E_r_t=11.0,E_r_r=13.0,
        A=17.0,B=19.0,C=23.0,D=29.0,
        A_t=31.0,B_r=37.0,C_r=41.0,D_t=43.0,
    )
    expected=-(31*2+17*5+43*(-3)+29*11+37*2+19*7+41*(-3)+23*13)
    assert out==expected

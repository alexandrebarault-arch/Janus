
def test_pi_mode_jet_reduces_to_pure_fourier_when_background_coefficients_are_constant():
    from numerics.aoki_stueckelberg_adjoint import homothetic_pi_mode_jet
    out=homothetic_pi_mode_jet(
        a=1.0,conformal_H=0.0,conformal_H_prime=0.0,r=0.7,
        mu=-0.2,omega=2.3,k=4.1,pi=1+0j,
    )
    assert abs(out.delta_eta - 1j*2.3)<1e-14
    assert abs(out.delta_r - 1j*4.1/0.8)<1e-14
    assert abs(out.delta_eta_t - (-1j*2.3)*out.delta_eta)<1e-14
    assert abs(out.delta_eta_r - (1j*4.1)*out.delta_eta)<1e-14
    assert abs(out.delta_r_t - (-1j*2.3)*out.delta_r)<1e-14
    assert abs(out.delta_r_r - (1j*4.1)*out.delta_r)<1e-14


def test_pi_mode_jet_keeps_background_derivative_corrections():
    from numerics.aoki_stueckelberg_adjoint import homothetic_pi_mode_jet
    kw=dict(
        a=1.2,conformal_H=0.17,conformal_H_prime=-0.023,r=0.8,
        mu=-0.4,omega=3.0,k=5.0,pi=1+0j,
    )
    out=homothetic_pi_mode_jet(**kw)
    assert abs(out.delta_eta_t - (-1j*kw['omega'])*out.delta_eta)>1e-3
    assert abs(out.delta_eta_r - (1j*kw['k'])*out.delta_eta)>1e-3
    assert abs(out.delta_r_t - (-1j*kw['omega'])*out.delta_r)>1e-3
    assert abs(out.delta_r_r - (1j*kw['k'])*out.delta_r)>1e-3

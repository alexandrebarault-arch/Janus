import numpy as np


def _target(raw,K,w=0.0):
    b1,b2,b3=raw
    D=b1*K+2*b2*K*K+b3*K**3
    B2=(b2*K*K+b3*K**3)/D
    B3=b3*K**3/D
    roots=np.roots([-2*B2+(1+3*w)*B3,6*w*B2-2*B2-2,3*(w-1)])
    mu=sorted(float(z.real) for z in roots if abs(z.imag)<1e-10 and z.real>-1)[0]
    common=(3*w-1)*(2+mu)*(1+2*B2*mu+B3*mu*mu)
    KS=0.75*common
    cs2=2*(3*(1-w)+(1-(3*w-1)*B2)*mu)/(3*common)
    return mu,-2*D*KS,cs2


def test_native_relative_hr_projection_recovers_aoki_nonlinear_dust_controls():
    from numerics.aoki_native_relative_hr_oracle import recover_native_relative_aoki_coefficients
    controls=[
        ((1.0,-4.2383993109,13.6801214252),1.0),
        ((1.0,-4.2383993109,13.6801214252),0.7),
        ((1.0,-2.0,6.0),1.0),
    ]
    signs=set()
    for raw,K in controls:
        mu,kinetic_target,cs2_target=_target(raw,K)
        out=recover_native_relative_aoki_coefficients(
            betas=(0,*raw,0),K=K,w=0.0,mu=mu,
            time_scales=(0.45,0.75,1.05),radius=0.8,
            hubble_step=0.006,amplitude_step=1.5e-3,quadrature_order=14,
        )
        assert np.isclose(out.kinetic_hessian_coefficient,kinetic_target,rtol=1.5e-2,atol=2e-3)
        assert np.isclose(out.sound_speed_squared,cs2_target,rtol=1.5e-2,atol=2e-3)
        assert out.fit_residual < 2e-3
        signs.add(np.sign(kinetic_target))
    assert signs=={-1.0,1.0}

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.bigravity_scalar_action import (
    RAW_FIELD_ORDER,
    hr_diagonal_scalar_potential_density,
    raw_kinetic_hessian,
    sector1_eh_velocity_lagrangian,
    sector2_eh_velocity_lagrangian,
    shift_interaction_lagrangian,
)
from numerics.lagos_bridge import LagosBackground


def _bg():
    return LagosBackground(
        a=0.7,
        b=0.91,
        Nbar=1.17,
        r=1.3,
        H=1.4,
        Hb=1.05,
        M1sq=1.0,
        M2sq=0.25,
        nu2=4.0,
        Z=0.62,
        Ztilde=0.81,
    )


def test_lagos_shift_terms_form_source_normalized_relative_shift_square():
    bg = _bg(); k = 2.3; B1, B2 = 0.17, -0.09
    measured = shift_interaction_lagrangian(bg, k=k, B1=B1, B2=B2)
    expected = bg.a * bg.M1sq * bg.Z * k**2 / (2.0*(bg.Nbar+bg.r)) * (
        bg.r*B1 - (bg.Nbar/bg.r)*B2
    )**2
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_raw_lagos_action_has_no_lapse_or_shift_velocities():
    bg = _bg(); k = 2.3
    K = raw_kinetic_hessian(bg, k=k)
    assert K.shape == (8, 8)
    assert np.allclose(K, K.T)
    for name in ("Phi1", "B1", "Phi2", "B2"):
        i = RAW_FIELD_ORDER.index(name)
        assert np.allclose(K[i, :], 0.0)
        assert np.allclose(K[:, i], 0.0)
    for name in ("Psi1", "E1", "Psi2", "E2"):
        assert np.linalg.norm(K[RAW_FIELD_ORDER.index(name), :]) > 0.0
    p1,e1,p2,e2 = map(RAW_FIELD_ORDER.index, ("Psi1","E1","Psi2","E2"))
    assert math.isclose(K[p1,e1], -2.0*k**2*bg.a**3*bg.M1sq)
    assert math.isclose(K[p2,e2], -2.0*k**2/bg.Nbar**2*(bg.Nbar*bg.b**3*bg.M2sq))


def test_sector1_eh_velocity_block_matches_lagos_eq_3_6():
    bg = _bg(); k=2.3; Phi1=.08; B1=-.13; Psi1_dot=.21; E1_dot=-.17
    measured = sector1_eh_velocity_lagrangian(
        bg,k=k,Phi1=Phi1,B1=B1,Psi1_dot=Psi1_dot,E1_dot=E1_dot
    )
    expected = bg.a**3*bg.M1sq*(
        -3*Psi1_dot**2 -6*bg.H*Psi1_dot*Phi1
        -2*k**2*E1_dot*(Psi1_dot+bg.H*Phi1)
        +2*k**2/bg.a**2*Psi1_dot*B1
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_sector2_eh_velocity_block_matches_lagos_eq_3_7():
    bg = _bg(); k=2.3; Phi2=-.06; B2=.11; Psi2_dot=-.19; E2_dot=.14
    measured = sector2_eh_velocity_lagrangian(
        bg,k=k,Phi2=Phi2,B2=B2,Psi2_dot=Psi2_dot,E2_dot=E2_dot
    )
    expected = bg.Nbar*bg.b**3*bg.M2sq*(
        -3*Psi2_dot**2/bg.Nbar**2
        -6*bg.Hb*Psi2_dot*Phi2/bg.Nbar**2
        -2*k**2*E2_dot*(Psi2_dot+bg.Hb*Phi2)/bg.Nbar**2
        +2*k**2*Psi2_dot*B2/(bg.Nbar*bg.b**2)
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def _mixed_second(fun, name1, name2, h=2e-5):
    def f(s1, s2):
        kw = dict(Phi1=0.0, Phi2=0.0, Psi1=0.0, E1=0.0, Psi2=0.0, E2=0.0)
        kw[name1] = s1
        kw[name2] = s2
        return fun(**kw)
    return (f(h,h)-f(h,-h)-f(-h,h)+f(-h,-h))/(4*h*h)


def _hr_test_params():
    a=0.73; r=1.21; Nbar=1.08; m2=0.67; M1sq=1.4; k=2.6
    betas=(0.19,0.41,-0.23,0.17,0.31)
    return a,r,Nbar,m2,M1sq,k,betas


def test_hr_potential_spatial_cross_terms_are_controlled_by_ztilde():
    a,r,Nbar,m2,M1sq,k,betas = _hr_test_params()
    beta0,beta1,beta2,beta3,beta4 = betas
    ztilde = m2*(beta1 + beta2*(r+Nbar) + beta3*r*Nbar)

    def potential(**kw):
        return hr_diagonal_scalar_potential_density(
            a=a,r=r,Nbar=Nbar,m2=m2,M1sq=M1sq,betas=betas,k=k,**kw
        )

    pp = _mixed_second(potential,"Psi1","Psi2")
    pe = _mixed_second(potential,"Psi1","E2")
    ep = _mixed_second(potential,"E1","Psi2")
    ee = _mixed_second(potential,"E1","E2")

    scale = a**3*M1sq*r*ztilde
    assert math.isclose(pp, 6.0*scale, rel_tol=2e-5, abs_tol=2e-6)
    assert math.isclose(pe, 2.0*k**2*scale, rel_tol=2e-5, abs_tol=2e-6)
    assert math.isclose(ep, 2.0*k**2*scale, rel_tol=2e-5, abs_tol=2e-6)
    assert abs(ee) < 2e-5*max(1.0, abs(scale)*k**4)


def test_hr_potential_lapse_spatial_cross_terms_are_controlled_by_z():
    a,r,Nbar,m2,M1sq,k,betas = _hr_test_params()
    beta0,beta1,beta2,beta3,beta4 = betas
    z = m2*(beta1 + 2.0*beta2*r + beta3*r*r)

    def potential(**kw):
        return hr_diagonal_scalar_potential_density(
            a=a,r=r,Nbar=Nbar,m2=m2,M1sq=M1sq,betas=betas,k=k,**kw
        )

    p1p2 = _mixed_second(potential,"Phi1","Phi2")
    p1s2 = _mixed_second(potential,"Phi1","Psi2")
    p2s1 = _mixed_second(potential,"Phi2","Psi1")
    p1e2 = _mixed_second(potential,"Phi1","E2")
    p2e1 = _mixed_second(potential,"Phi2","E1")

    scale = a**3*M1sq*z
    assert abs(p1p2) < 2e-5*max(1.0,abs(scale))
    assert math.isclose(p1s2, -1.5*r*scale, rel_tol=2e-5, abs_tol=2e-6)
    assert math.isclose(p2s1, -1.5*Nbar*scale, rel_tol=2e-5, abs_tol=2e-6)
    assert math.isclose(p1e2, -0.5*r*k**2*scale, rel_tol=2e-5, abs_tol=2e-6)
    assert math.isclose(p2e1, -0.5*Nbar*k**2*scale, rel_tol=2e-5, abs_tol=2e-6)

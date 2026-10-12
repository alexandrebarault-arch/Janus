import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_action_bridge import lagos_bigravity_parameters
from numerics.lagos_scalar_action import (
    INTERACTION_STATE_ORDER,
    RATE_ORDER,
    pure_metric_lagrangian_healthy,
    einstein_hilbert_lagrangian,
    interaction_lagrangian_healthy,
    velocity_hessian,
)


def _proportional_background():
    return ScalarBackground(a=1.0,m2=1.7,f1=1.0,f2=1.0,H=0.8,H_omega=0.8,c=1.0,xi=1.0,kappa=1.0,k2=9.0,G8pi=1.0)


def _nontrivial_background(*, a=0.63):
    return ScalarBackground(a=a,m2=1.7,f1=0.83,f2=0.91,H=0.74,H_omega=0.74*0.88,c=0.88,xi=1.27,kappa=0.61,k2=11.0,G8pi=1.0)


def _swap_metrics(x):
    x=np.asarray(x,float); out=x.copy()
    for a,b in (("Psi1","Psi2"),("E1","E2"),("Phi1","Phi2"),("B1","B2")):
        ia=INTERACTION_STATE_ORDER.index(a); ib=INTERACTION_STATE_ORDER.index(b); out[ia],out[ib]=x[ib],x[ia]
    return out


def _swap_rates(v):
    v=np.asarray(v,float); out=v.copy()
    for a,b in (("Psi1_dot","Psi2_dot"),("E1_dot","E2_dot")):
        ia=RATE_ORDER.index(a); ib=RATE_ORDER.index(b); out[ia],out[ib]=v[ib],v[ia]
    return out


def _mixed_rate_coefficient(bg,i,j):
    state=np.zeros(8); ei=np.zeros(4); ej=np.zeros(4); ei[i]=1; ej[j]=1
    L=lambda r: einstein_hilbert_lagrangian(bg,state,r)
    return L(ei+ej)-L(ei)-L(ej)+L(np.zeros(4))


def _mixed_state_coefficient(bg,name_i,name_j):
    ei=np.zeros(8); ej=np.zeros(8)
    ei[INTERACTION_STATE_ORDER.index(name_i)]=1.0
    ej[INTERACTION_STATE_ORDER.index(name_j)]=1.0
    L=lambda s: interaction_lagrangian_healthy(bg,s)
    return L(ei+ej)-L(ei)-L(ej)+L(np.zeros(8))


def test_sector1_Edot_Psidot_uses_background_metric_laplacian():
    for a in (0.41,0.73,1.37):
        bg=_nontrivial_background(a=a)
        measured=_mixed_rate_coefficient(bg,RATE_ORDER.index("Psi1_dot"),RATE_ORDER.index("E1_dot"))
        assert math.isclose(measured,-2.0*bg.k2,rel_tol=2e-13,abs_tol=2e-13)


def test_sector2_Edot_Psidot_uses_its_own_background_metric_laplacian():
    bg=_nontrivial_background(a=0.63); p=lagos_bigravity_parameters(bg)
    factor2=p.Nbar*p.r**3*bg.kappa
    expected=factor2*(-2.0*bg.k2/p.Nbar**2)
    measured=_mixed_rate_coefficient(bg,RATE_ORDER.index("Psi2_dot"),RATE_ORDER.index("E2_dot"))
    assert math.isclose(measured,expected,rel_tol=2e-13,abs_tol=2e-13)


def test_interaction_Psi1_E1_gradient_loses_explicit_a2_after_fourier_translation():
    for a in (0.41,0.73,1.37):
        bg=_nontrivial_background(a=a); p=lagos_bigravity_parameters(bg)
        measured=_mixed_state_coefficient(bg,"Psi1","E1")
        expected=2.0*p.r*p.Z_tilde*bg.k2
        assert math.isclose(measured,expected,rel_tol=2e-13,abs_tol=2e-13)


def test_interaction_cross_metric_E_gradients_use_each_fields_background_metric():
    bg=_nontrivial_background(a=0.63); p=lagos_bigravity_parameters(bg)
    expected=-2.0*p.r*p.Z_tilde*bg.k2
    assert math.isclose(_mixed_state_coefficient(bg,"Psi2","E1"),expected,rel_tol=2e-13,abs_tol=2e-13)
    assert math.isclose(_mixed_state_coefficient(bg,"Psi1","E2"),expected,rel_tol=2e-13,abs_tol=2e-13)


def test_interaction_B1_self_and_B1B2_cross_use_metric1_contraction():
    bg=_nontrivial_background(a=0.63); p=lagos_bigravity_parameters(bg)
    a2=bg.a**2
    e=np.zeros(8); e[INTERACTION_STATE_ORDER.index("B1")]=1.0
    measured_self=interaction_lagrangian_healthy(bg,e)
    expected_self=p.r*p.Z/(2.0*(p.Nbar+p.r))*bg.k2/a2
    assert math.isclose(measured_self,expected_self,rel_tol=2e-13,abs_tol=2e-13)
    expected_cross=-p.Z*p.Nbar/(p.Nbar+p.r)*bg.k2/a2
    measured_cross=_mixed_state_coefficient(bg,"B1","B2")
    assert math.isclose(measured_cross,expected_cross,rel_tol=2e-13,abs_tol=2e-13)


def test_pure_metric_action_is_exchange_symmetric_on_proportional_background():
    bg=_proportional_background(); state=np.array([0.13,-0.08,0.021,-0.017,0.032,-0.026,0.011,-0.014]); rates=np.array([0.041,-0.037,0.016,-0.012])
    lhs=pure_metric_lagrangian_healthy(bg,state,rates); rhs=pure_metric_lagrangian_healthy(bg,_swap_metrics(state),_swap_rates(rates))
    assert math.isclose(lhs,rhs,rel_tol=2e-12,abs_tol=2e-12)


def test_auxiliary_lapses_and_shifts_have_no_velocity_slots():
    bg=_proportional_background(); H=velocity_hessian(bg)
    assert RATE_ORDER==("Psi1_dot","Psi2_dot","E1_dot","E2_dot")
    assert H.shape==(4,4); assert np.all(np.isfinite(H)); assert np.allclose(H,H.T,rtol=1e-13,atol=1e-13)


def test_pure_metric_action_is_quadratic():
    bg=_proportional_background(); state=np.array([0.09,-0.05,0.018,0.006,-0.021,0.027,0.012,-0.008]); rates=np.array([0.031,-0.024,0.014,-0.009])
    l1=pure_metric_lagrangian_healthy(bg,state,rates); l2=pure_metric_lagrangian_healthy(bg,2.0*state,2.0*rates)
    assert math.isclose(l2,4.0*l1,rel_tol=2e-12,abs_tol=2e-12)

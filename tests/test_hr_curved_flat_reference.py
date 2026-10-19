"""Independent Step33f flat/comoving secondary cross-reference in fresh process."""
import numpy as np
import pytest
import sympy as sp
from numerics.hr_curved_moving_dust_primary import build_primary,R,BETA,M2,MG2,MF2
from numerics.hr_curved_primary_mixed_kernel import local_curved_bracket

def test_exact_flat_comoving_limit_matches_prior_closed_step33f_secondary():
    flat=build_primary(curv_g=0,curv_f=0,theta_g=0,theta_f=0,
                       z_slope=0,grav_g=.04,grav_f=-.035)
    r=.43
    K=local_curved_bracket(flat,r).coefficients
    P_g=flat.expr['pLg']/R**2;P_f=flat.expr['pLf']/R**2
    X=P_g/(MG2*flat.params['a'])-P_f/(MF2*flat.params['b'])
    y=flat.params['y'];J=BETA[1]+2*BETA[2]*y+BETA[3]*y*y
    expected=.5*M2*MG2*flat.params['a']**2*J*r*r*float((3*X+R*sp.diff(X,R)).subs(R,r))
    assert K[0,0]==pytest.approx(expected,rel=2e-11,abs=1e-12)
    np.testing.assert_allclose(K[1:,:],0,atol=1e-12)
    np.testing.assert_allclose(K[0,1:],0,atol=1e-12)
    assert abs(expected)>1e-3

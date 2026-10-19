"""Primary-surface mixed bracket: derivative smearings must be integrated by parts."""
import numpy as np
import subprocess,sys,json,os
import pytest
import sympy as sp
from numerics.hr_curved_moving_dust_primary import build_primary,R,BETA,M2,MG2,MF2
from numerics.hr_curved_primary_mixed_kernel import local_curved_bracket


@pytest.fixture(scope='module')
def curved():
    # One fresh subprocess runs the REAL SymPy kernel at three radii;
    # avoids building huge symbolic caches inside the pytest worker.
    code="""import json
from numerics.hr_curved_moving_dust_primary import build_primary
from numerics.hr_curved_primary_mixed_kernel import local_curved_bracket
w=build_primary()
d={str(r):local_curved_bracket(w,r).coefficients.tolist() for r in (.425,.43,.435)}
print(json.dumps(d))
"""
    done=subprocess.run([sys.executable,'-c',code],capture_output=True,
                        text=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'},
                        timeout=55,check=True)
    d=json.loads(done.stdout)
    return build_primary(),{float(k):np.array(v) for k,v in d.items()}


def test_curved_moving_two_dust_mixed_kernel_has_genuine_smearing_derivatives(curved):
    w,data=curved
    K=data[.43]
    assert K.shape==(3,3)
    assert abs(K[0,0])>.2
    assert abs(K[0,1])>1e-3
    assert abs(K[1,0])>.05
    assert abs(K[1,1])>.01
    np.testing.assert_allclose(K[2,0],K[1,1],atol=2e-13)
    np.testing.assert_allclose(K[0,2],0,atol=2e-13)
    np.testing.assert_allclose(K[1,2],0,atol=2e-13)
    np.testing.assert_allclose(K[2,1:],0,atol=2e-13)
    assert w.eval(.43,('Hg','Hf','Ddiag','Fz')).max()<1e-12


def test_curved_on_primary_derivative_smearing_coefficients_cancel_after_IBP(curved):
    # Integral of K20 N''M + K11 N'M' (K20=K11) equals
    # -integral K20' N'M. Together with K10 N'M, the coefficient of
    # independent N M' is K01-K10+K20'. It must vanish on this
    # restricted primary witness within numerical derivative error.
    _,data=curved
    h=.005
    km=data[.43-h]
    k0=data[.43]
    kp=data[.43+h]
    d20=(kp[2,0]-km[2,0])/(2*h)
    d01=(kp[0,1]-km[0,1])/(2*h)
    assert abs(k0[0,1]-k0[1,0]+d20)<3e-6
    # The (necessary) local scalar coefficient after compact IBP is
    # K00 - derivative(K01); *not* just K00, let alone homogeneous chi.
    scalar=k0[0,0]-d01
    assert abs(scalar)>.1
    assert abs(scalar-k0[0,0])>.02
    assert scalar==pytest.approx(.47,abs=.02)


def test_offshell_smeared_gradient_decomposition_is_nontrivial(curved):
    _,data=curved
    K=data[.43]
    # Setting N'=M'=N''=0 loses substantial local terms in the true
    # integrand for generic radial smearings before IBP.
    N=np.array([1.,.3,-.15]);M=np.array([.7,-.2,.12])
    actual=N@K@M
    naive=K[0,0]*N[0]*M[0]
    assert abs(actual-naive)>1e-3

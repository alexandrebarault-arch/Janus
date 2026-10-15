import numpy as np


def _diagonal_expected(betas, t, x):
    b0,b1,b2,b3,b4=betas
    vg_t=b0+3*b1*x+3*b2*x*x+b3*x**3
    vg_s=b0+b1*(t+2*x)+b2*(2*t*x+x*x)+b3*t*x*x
    ti=1/t; xi=1/x
    vf_t=b4+3*b3*xi+3*b2*xi*xi+b1*xi**3
    vf_s=b4+b3*(ti+2*xi)+b2*(2*ti*xi+xi*xi)+b1*ti*xi*xi
    return np.array([vg_t,vg_s,vf_t,vf_s])


def test_full_hr_interaction_tensor_reduces_to_diagonal_source_formulas():
    from numerics.nonhomothetic_hr_interaction_tensor import interaction_mixed_tensors
    betas=(0.4,1.2,-0.7,0.9,-1.1)
    t=0.63; x=1.47
    S=np.diag([t,x,x,x])
    vg,vf=interaction_mixed_tensors(S,betas)
    expected=_diagonal_expected(betas,t,x)
    assert np.allclose([vg[0,0],vg[1,1],vf[0,0],vf[1,1]],expected,rtol=0,atol=2e-13)
    assert np.allclose(vg-np.diag(np.diag(vg)),0,rtol=0,atol=2e-13)
    assert np.allclose(vf-np.diag(np.diag(vf)),0,rtol=0,atol=2e-13)


def test_interaction_tensor_is_similarity_covariant():
    from numerics.nonhomothetic_hr_interaction_tensor import interaction_mixed_tensors
    betas=(0.0,1.0,-2.0,6.0,0.3)
    S0=np.diag([0.8,1.2,1.2,1.2])
    P=np.eye(4); P[0,1]=0.17
    Pinv=np.linalg.inv(P)
    S=P@S0@Pinv
    vg,vf=interaction_mixed_tensors(S,betas)
    vg0,vf0=interaction_mixed_tensors(S0,betas)
    assert np.allclose(vg,P@vg0@Pinv,rtol=2e-13,atol=2e-13)
    assert np.allclose(vf,P@vf0@Pinv,rtol=2e-13,atol=2e-13)

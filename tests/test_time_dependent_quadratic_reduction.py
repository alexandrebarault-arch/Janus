import numpy as np

from numerics.time_dependent_quadratic_reduction import (
    eliminate_time_dependent_null_coordinate,
    euler_lagrange_matrices,
    de_felice_y2hat_map,
)


def test_null_coordinate_reduction_matches_completed_square():
    K=np.diag([2.0,3.0,0.0])
    C=np.array([[0.2,-0.1,0.7],[0.4,0.3,-0.2],[0.5,-0.6,0.8]])
    Q=np.array([[4.0,0.2,0.9],[0.2,5.0,-0.4],[0.9,-0.4,6.0]])
    Cdot=np.zeros((3,3)); Cdot[2,:]=[0.11,-0.07,0.13]
    red=eliminate_time_dependent_null_coordinate(K,C,Q,Cdot,null_index=2)
    d=np.array([0.7-0.5,-0.2-(-0.6)])
    r=np.array([0.9-0.11,-0.4-(-0.07)])
    qzz=6.0-0.13
    assert np.allclose(red.K, K[:2,:2]-np.outer(d,d)/qzz)
    assert np.allclose(red.C, C[:2,:2]-np.outer(d,r)/qzz)
    assert np.allclose(red.Q, Q[:2,:2]-np.outer(r,r)/qzz)


def test_euler_lagrange_matrices_keep_background_derivatives():
    K=np.eye(2); C=np.array([[0.0,2.0],[-1.0,0.0]]); Q=np.diag([3.0,4.0])
    Kdot=np.diag([0.2,-0.3]); Cdot=np.array([[0.1,0.4],[0.5,-0.2]])
    out=euler_lagrange_matrices(K,C,Q,Kdot,Cdot)
    assert np.allclose(out.D, Kdot+C-C.T)
    assert np.allclose(out.E, Cdot-Q)


def test_de_felice_y2hat_map_includes_Rdot():
    mapped=de_felice_y2hat_map(k=12.0,R=0.4,Rdot=-0.07,Y2hat=0.3,S=0.02,Sigma=-0.1,Y2hat_dot=-0.2,S_dot=0.04,Sigma_dot=0.05)
    combo=-0.1+12.0**2*0.02/6.0
    combo_dot=0.05+12.0**2*0.04/6.0
    assert np.isclose(mapped.u_f,0.3+0.4*combo)
    assert np.isclose(mapped.u_f_dot,-0.2+0.4*combo_dot-0.07*combo)


def test_null_coordinate_singularity_scale_is_local_to_null_block():
    K=np.diag([1.0,0.0])
    C=np.zeros((2,2))
    Q=np.diag([1.0e20,2.0])
    Cdot=np.zeros((2,2)); Cdot[1,1]=0.5
    red=eliminate_time_dependent_null_coordinate(K,C,Q,Cdot,null_index=1)
    assert red.K.shape==(1,1)
    assert np.isclose(red.K[0,0],1.0)

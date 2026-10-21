"""Execution controls for a planned real HR full nine-coefficient Ward test.

Only manufactured known polynomial Kij and polynomial lapse jets here.
No falsely claimed physical provider execution.
"""
import math
import numpy as np
import pytest
from numerics.hr_step43_physical_ward_gate import physical_ward_sample,full_jet_gauss_vs_C


def poly_smears(r,lo=.2,hi=.7):
    # Polynomial N=(r-lo)^4(hi-r)^4 and M=N*(1+(r-lo)); analytic jets.
    a=r-lo;b=hi-r
    n=a**4*b**4
    np1=4*a**3*b**4-4*a**4*b**3
    np2=12*a*a*b**4-32*a**3*b**3+12*a**4*b*b
    m=n*(1+a)
    mp=np1*(1+a)+n
    mpp=np2*(1+a)+2*np1
    return np.array([n,np1,np2]),np.array([m,mp,mpp])


def fake_ward_zero(witness,r):
    K=np.zeros((3,3))
    p=r*r*2+3*r
    q=1+r**3
    K[0,0]=4*r+3
    K[0,1]=p
    K[1,0]=p+3*r*r
    K[1,1]=q
    K[2,0]=q
    return K


def test_good_full_ward_and_C_vanish_at_sampling_sites():
    for rad in (.2,.43,.7):
        o=physical_ward_sample(None,rad,.001,kernel=fake_ward_zero)
        assert abs(o['C'])<1e-10
        assert abs(o['W'])<1e-10
        assert o['D']==0 and o['max_excluded_abs']==0


def test_full_smear_integral_matches_C_only_for_exact_ward():
    z=full_jet_gauss_vs_C(None,kernel=fake_ward_zero,smears=poly_smears,points=48)
    assert abs(z['full_jet_bracket'])<1e-16
    assert abs(z['difference'])<1e-16
    assert z['max_abs_D_samples']==0


def fake_W_violation(witness,r):
    k=fake_ward_zero(witness,r)
    k[1,0]+=r
    return k


def test_injected_nonzero_W_detected_even_though_C_is_zero():
    z=physical_ward_sample(None,.43,kernel=fake_W_violation)
    assert abs(z['C'])<1e-10
    assert abs(z['W']+.43)<1e-10
    val=full_jet_gauss_vs_C(None,kernel=fake_W_violation,smears=poly_smears)
    assert abs(val['difference'])>1e-18


def fake_D_violation(witness,r):
    k=fake_ward_zero(witness,r)
    k[1,1]+=1
    return k


def test_injected_nonzero_D_detected_even_though_C_and_W_are_zero():
    z=physical_ward_sample(None,.43,kernel=fake_D_violation)
    assert abs(z['C'])<1e-10 and abs(z['W'])<1e-10
    assert z['D']==-1
    val=full_jet_gauss_vs_C(None,kernel=fake_D_violation,smears=poly_smears)
    assert abs(val['difference'])>1e-18


def test_finite_stencil_convergence_for_degree_five_momentum_like_jet():
    def k(w,r):
        k=fake_ward_zero(w,r)
        k[2,0]=1+r**5
        k[1,0]=k[0,1]+5*r**4
        k[1,1]=k[2,0]
        return k
    errors=[abs(physical_ward_sample(None,.43,h,kernel=k)['W']) for h in (.02,.01,.005)]
    assert errors[0]>10*errors[1]>10*errors[2]


def test_malformed_kernel_and_chart_are_rejected():
    with pytest.raises(ArithmeticError):physical_ward_sample(None,kernel=lambda w,r:np.ones((2,2)))
    with pytest.raises(ArithmeticError):physical_ward_sample(None,kernel=lambda w,r:np.full((3,3),np.nan))
    with pytest.raises(ValueError):physical_ward_sample(None,r=.026,h=.002,kernel=fake_ward_zero)
    with pytest.raises(ValueError):full_jet_gauss_vs_C(None,points=8,kernel=fake_ward_zero,smears=poly_smears)


def test_injected_high_derivative_coefficient_is_visible():
    def k(w,r):
        out=fake_ward_zero(w,r)
        out[2,2]=.25
        return out
    z=physical_ward_sample(None,.43,kernel=k)
    assert z['max_excluded_abs']==.25
    val=full_jet_gauss_vs_C(None,kernel=k,smears=poly_smears)
    assert abs(val['difference'])>1e-20

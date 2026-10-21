"""Exact 3x3 mixed lapse-jet operator/counterexample tests."""
import sympy as sp
import pytest
from numerics.hr_step43_ward_operator import (
    r,adjoint_coefficients,restricted_local_gates,exact_reduction_gate,
    polynomial_integral,compact_smears,bracket_as_polynomial,
    adjoint_as_polynomial,local_as_polynomial,
    exact_compact_integral_controls,ward_example)


def test_all_nine_jets_are_retained_before_physical_Ward_assumptions():
    K={(i,j):r**(i+j+1)+sp.Rational(i+1,j+2) for i in range(3) for j in range(3)}
    a=adjoint_coefficients(K)
    assert set(a)==set(range(5))
    assert sp.simplify(a[4]-K[(2,2)])==0
    assert sp.simplify(a[3]-(2*sp.diff(K[(2,2)],r)+K[(2,1)]-K[(1,2)]))==0
    assert not exact_reduction_gate(K)['C_only_valid']


def test_abstract_exact_C_and_Ward_identity_for_restricted_kernel():
    C,U,V,W,D=[sp.Function(n)(r) for n in ('C','U','V','W','D')]
    K={(0,0):C+sp.diff(U,r),(0,1):U,
       (1,0):U+sp.diff(V,r)-W,(1,1):V-D,(2,0):V}
    a=adjoint_coefficients(K)
    g=restricted_local_gates(K)
    assert sp.simplify(g['C']-C)==0
    assert sp.simplify(g['W']-W)==0
    assert sp.simplify(g['D']-D)==0
    assert sp.simplify(a[0]-(C+sp.diff(W,r)))==0
    assert sp.simplify(a[1]-(W+sp.diff(D,r)))==0
    assert sp.simplify(a[2]-D)==0
    assert a[3]==0 and a[4]==0


def test_good_kernel_has_nontrivial_gradients_but_exact_C_only():
    K=ward_example()
    g=exact_reduction_gate(K)
    assert g['C_only_valid']
    assert g['jet_W']==0 and g['jet_D']==0
    assert all(v==0 for v in g['operator_residuals'].values())
    assert K[(1,1)]!=0 and K[(2,0)]!=0


@pytest.mark.parametrize('variant',[-3,0,1,5])
def test_exact_boundary_integral_matches_adjoint_and_C_only_if_Ward_closes(variant):
    vals=exact_compact_integral_controls(ward_example(),variant=variant)
    assert vals['original']==vals['adjoint']==vals['C_only']


def test_false_positive_if_W_not_zero_despite_C_zero():
    K=ward_example(C=0)
    K[(1,0)]+=r      # W=-r; no change to C
    control=exact_reduction_gate(K)
    assert control['C']==0 and control['jet_W']==-r
    assert not control['C_only_valid']
    values=exact_compact_integral_controls(K,variant=0)
    assert values['original']==values['adjoint']
    assert values['C_only']==0
    assert values['original']!=0


def test_false_positive_if_K11_not_K20_despite_C_and_W_zero():
    K=ward_example(C=0)
    K[(1,1)]+=1
    control=exact_reduction_gate(K)
    assert control['C']==0 and control['jet_W']==0
    assert control['jet_D']==-1
    assert not control['C_only_valid']
    values=exact_compact_integral_controls(K,variant=0)
    assert values['original']==values['adjoint']
    assert values['original']!=values['C_only']==0


def test_false_positive_if_unchecked_K22_high_jet_nonzero():
    K=ward_example(C=0);K[(2,2)]=sp.Rational(1,7)
    check=exact_reduction_gate(K)
    assert check['C']==0 and check['jet_W']==check['jet_D']==0
    assert check['operator_residuals'][4]==sp.Rational(1,7)
    assert not check['C_only_valid']
    values=exact_compact_integral_controls(K)
    assert values['original']==values['adjoint']
    assert values['original']!=0 and values['C_only']==0


def test_full_operator_gate_rejects_nonvanishing_higher_jets():
    K=ward_example()
    # Unchecked higher jets must be analyzed in the FULL adjoint;
    # this deliberately non-null perturbation must be rejected.
    K[(0,2)]=1
    K[(1,1)]+=2*r
    K[(2,0)]+=r**2
    # Find exact residual and keep this as an explicit countercontrol.
    check=exact_reduction_gate(K)
    assert check['C_only_valid'] is False
    assert any(x!=0 for x in check['operator_residuals'].values())


def test_operator_integral_uses_all_nine_coefficients():
    K={(i,j):sp.Rational(i+j+1,9)*r**(i+j) for i in range(3) for j in range(3)}
    for v in (0,1,3):
        x=exact_compact_integral_controls(K,variant=v)
        assert x['original']==x['adjoint']


def test_integration_by_parts_needs_boundary_conditions():
    K={(1,0):r}
    N=sp.Integer(1);M=r
    unadj=polynomial_integral(bracket_as_polynomial(K,N,M))
    adj=polynomial_integral(adjoint_as_polynomial(K,N,M))
    assert unadj==0 and adj!=0 # N does not vanish on boundaries


def test_compact_smears_have_fourth_order_boundary_zeros():
    a,b=sp.Rational(1,5),sp.Rational(7,10)
    N,M=compact_smears(variant=3)
    for f in (N,M):
        for k in range(4):
            assert sp.diff(f,r,k).subs(r,a)==0
            assert sp.diff(f,r,k).subs(r,b)==0


def test_reject_malformed_kernel_and_invalid_interval():
    with pytest.raises(ValueError):adjoint_coefficients({(3,0):r})
    with pytest.raises(ValueError):adjoint_coefficients({'bad':r})
    with pytest.raises(ValueError):polynomial_integral(r,1,0)
    with pytest.raises(ValueError):compact_smears(1,0)


def test_verdict_is_conditional_not_real_dirac_preservation():
    good=ward_example(C=0)
    assert exact_reduction_gate(good)['C_only_valid']
    # A manufactured polynomial identity doesn't calculate actual HR Kij.
    assert all(sp.simplify(e)==0 for e in exact_reduction_gate(good)['operator_residuals'].values())

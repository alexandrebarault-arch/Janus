"""Independent symbolic, numerical, and true spherical homogeneous-branch PB tests.

Homogeneous *analogue* of the HR BD secondary, NOT a local field-theory
constraint proof or propagation/kinetic/ghost determination.
"""
import math
import numpy as np
import pytest
from numerics.hr_homogeneous_poisson_secondary import (
    Parameters,PhasePoint,from_vector,beta_functions,homogeneous_constraints,
    primary_poisson_analytic,secondary_chi,secondary_preservation_brackets,
    preservation_lapse_ratio,canonical_bracket_fd,mini_hg,mini_hf,mini_chi,
    flat_spherical_embedding,candidate_dust_point,CANDIDATE_Y0,
)
from numerics.hr_spherical_adm_primary import Geometry,eh_hamiltonian_constraints

P=Parameters((.12,1.4,-.3,.45,-.2),.81,1.7,.55)
Q=PhasePoint(1.14,.87,-1.31,-.62,.17,-.22,.52,.13)


def test_canonical_eight_component_embedding_and_validation():
    np.testing.assert_allclose(from_vector(Q.canonical_vector()).canonical_vector(),Q.canonical_vector())
    with pytest.raises(ValueError):from_vector([1,2,3])
    with pytest.raises(ValueError):PhasePoint(1,1,0,0,0,0,-1,1).validate()
    with pytest.raises(ValueError):Parameters((1,2),1,1,1).validate()
    with pytest.raises(ValueError):Parameters((0,0,0,0,0),1,-1,1).validate()
    with pytest.raises(ValueError):candidate_dust_point(.02)


def test_exact_primary_bracket_symbolic_eight_dimensional_with_two_dust_pairs():
    import sympy as sp
    a,b,pa,pb,thg,thf,pg,pf,M,F,k=sp.symbols('a b pa pb thg thf pg pf M F k',nonzero=True)
    bb=sp.symbols('b0:5')
    u=k*(bb[0]*a**3+3*bb[1]*a*a*b+3*bb[2]*a*b*b+bb[3]*b**3)
    v=k*(bb[1]*a**3+3*bb[2]*a*a*b+3*bb[3]*a*b*b+bb[4]*b**3)
    hg=-pa**2/(12*M*a)+u+pg
    hf=-pb**2/(12*F*b)+v+pf
    q=(a,b,thg,thf);mom=(pa,pb,pg,pf)
    def pb_fun(x,y):
        return sum(sp.diff(x,qi)*sp.diff(y,pi)-sp.diff(x,pi)*sp.diff(y,qi)
                   for qi,pi in zip(q,mom))
    J=bb[1]+2*bb[2]*b/a+bb[3]*b*b/(a*a)
    chi=pa/(M*a)-pb/(F*b)
    assert sp.simplify(pb_fun(hg,hf)-k*a*a*J*chi/2)==0
    assert sp.simplify(pb_fun(chi,hg)-(
        pa**2/(12*M*M*a**3)-3*k*a*(bb[0]+2*bb[1]*b/a+bb[2]*(b/a)**2)/M+3*k*a*a*J/(F*b)))==0
    assert sp.simplify(pb_fun(chi,hf)-(
        -pb**2/(12*F*F*b**3)-3*k*a*J/M+3*k*a*a*(bb[2]+2*bb[3]*b/a+bb[4]*(b/a)**2)/(F*b)))==0
    assert pb_fun(pg,hg)==pb_fun(pf,hf)==pb_fun(pg,hf)==pb_fun(pf,hg)==0
    assert pb_fun(thg,hg)==1 and pb_fun(thf,hf)==1
    assert pb_fun(thg,hf)==0 and pb_fun(thf,hg)==0


def test_primary_poisson_matches_independent_centered_eight_variable_bracket():
    for s in (.4,.8,1.,1.6):
        q=PhasePoint(Q.a*s,Q.b*.9*s,Q.pa*1.1,Q.pb*.8,Q.theta_g,Q.theta_f,Q.pg,Q.pf)
        exact=primary_poisson_analytic(P,q)
        numeric=canonical_bracket_fd(mini_hg,mini_hf,P,q,step=3e-6)
        assert abs(exact)>1e-4
        assert numeric==pytest.approx(exact,rel=1e-8,abs=1e-9)


def test_secondary_time_preservation_brackets_independent_centered_poisson():
    for a in (.55,.9,1.3):
        q=PhasePoint(a,.73*a,-2.,-.9,.2,-.1,.7,.31)
        exact=secondary_preservation_brackets(P,q)
        independent=(canonical_bracket_fd(mini_chi,mini_hg,P,q,step=1e-6),
                     canonical_bracket_fd(mini_chi,mini_hf,P,q,step=1e-6))
        np.testing.assert_allclose(independent,exact,rtol=4e-9,atol=1e-8)


def test_offshell_two_primary_brackets_not_identically_zero():
    PB=primary_poisson_analytic(P,Q)
    assert abs(PB)>1e-3
    matrix=np.array([[0.,PB],[-PB,0.]])
    assert np.linalg.matrix_rank(matrix)==2
    with pytest.raises(ValueError,match='off the primary'):
        preservation_lapse_ratio(P,Q)


@pytest.mark.parametrize('a',[1.,.8,.4,.2,.09,.05,.03])
def test_candidate_dust_branch_both_friedmann_secondary_and_lapse_fixer(a):
    par,q,nf=candidate_dust_point(a)
    hg,hf=homogeneous_constraints(par,q)
    assert max(abs(hg),abs(hf))<3e-12
    assert abs(secondary_chi(par,q))<1e-12
    assert abs(primary_poisson_analytic(par,q))<1e-12
    bg,bf=secondary_preservation_brackets(par,q)
    assert abs(bg)>100 and abs(bf)>100
    assert (bg+nf*bf)==pytest.approx(0.,abs=3e-10)
    assert preservation_lapse_ratio(par,q)==pytest.approx(nf,rel=1e-11,abs=2e-12)
    assert .3<nf<.7


def test_relative_poisson_branch_j_zero_is_not_dynamical_secondary():
    # J(y)=beta1+2 beta2*y+beta3*y² =0 at y=1 (beta1=-2,beta2=1).
    par=Parameters((.2,-2.,1.,0.,.3),1.,1.,.7)
    q=PhasePoint(1.,1.,-1.2,-.5,0.,0.,.2,.4)
    assert beta_functions(par,q)[3]==0
    assert abs(secondary_chi(par,q))>.1
    assert primary_poisson_analytic(par,q)==0
    with pytest.raises(ValueError):preservation_lapse_ratio(par,q)


def test_zero_interaction_does_not_imply_secondary():
    par=Parameters(P.betas,0.,P.Mg2,P.Mf2)
    assert primary_poisson_analytic(par,Q)==0
    assert secondary_chi(par,Q)!=0
    with pytest.raises(ValueError):preservation_lapse_ratio(par,Q)


@pytest.mark.parametrize('a',[1.,.4,.09,.03])
@pytest.mark.parametrize('radius',[.12,.31,.47])
def test_true_spherical_adm_homogeneous_embedding_reproduces_mini_constraints(a,radius):
    par,q,nf=candidate_dust_point(a)
    g,f,diag=flat_spherical_embedding(par,q,radius=radius)
    mini=homogeneous_constraints(par,q)
    np.testing.assert_allclose([g,f],mini,rtol=0,atol=1e-11)
    assert abs(diag)<3e-13


def test_offshell_spherical_and_mini_potential_agree_exactly():
    g,f,d=flat_spherical_embedding(P,Q,radius=.27)
    np.testing.assert_allclose([g,f],homogeneous_constraints(P,Q),atol=1e-13,rtol=2e-13)
    assert abs(d)<1e-12


def test_spherical_radial_momentum_derivative_required_for_momentum_constraint():
    a=1.3;r=.23;pa=-2.
    g=Geometry(L=a,S=a*r,Sr=a,planck2=1.)
    corr=eh_hamiltonian_constraints(g,pL=pa*r*r/3,pS=2*pa*r/3,pLr=2*pa*r/3)
    wrong=eh_hamiltonian_constraints(g,pL=pa*r*r/3,pS=2*pa*r/3,pLr=0.)
    assert abs(corr[1])<1e-15
    assert abs(wrong[1])>1e-3


def test_fixed_dust_charges_are_two_independent_phase_space_momenta():
    assert canonical_bracket_fd(lambda p,q:q.theta_g,lambda p,q:q.pg,P,Q)==pytest.approx(1.,rel=1e-10)
    assert canonical_bracket_fd(lambda p,q:q.theta_f,lambda p,q:q.pf,P,Q)==pytest.approx(1.,rel=1e-10)
    for x,y in ((lambda p,q:q.theta_g,lambda p,q:q.pf),
                (lambda p,q:q.theta_f,lambda p,q:q.pg)):
        assert canonical_bracket_fd(x,y,P,Q)==pytest.approx(0,abs=1e-12)


def test_lapse_ratio_requires_both_constraints_even_when_chi_zero():
    p,q,n=candidate_dust_point(.4)
    bad=PhasePoint(q.a,q.b,q.pa,q.pb,q.theta_g,q.theta_f,q.pg*1.01,q.pf)
    assert abs(secondary_chi(p,bad))<1e-12
    assert homogeneous_constraints(p,bad)[0]!=pytest.approx(0.,abs=1e-6)
    with pytest.raises(ValueError):preservation_lapse_ratio(p,bad)


def test_lapse_ratio_rejects_bad_regularization():
    p,q,n=candidate_dust_point(.4)
    with pytest.raises(ValueError):preservation_lapse_ratio(p,q,min_denom=0)
    with pytest.raises(ValueError):preservation_lapse_ratio(p,q,on_shell_tol=0)


def test_analytical_conservation_independent_of_dust_clock_values():
    p,q,n=candidate_dust_point(.4)
    other=PhasePoint(q.a,q.b,q.pa,q.pb,91.,-12.5,q.pg,q.pf)
    assert homogeneous_constraints(p,q)==homogeneous_constraints(p,other)
    assert secondary_preservation_brackets(p,q)==secondary_preservation_brackets(p,other)
    assert preservation_lapse_ratio(p,q)==preservation_lapse_ratio(p,other)

@pytest.mark.parametrize('a',[1.,.4,.09,.03])
def test_homogeneous_three_constraint_dirac_matrix_has_one_null_direction(a):
    """Rank-two mini Dirac matrix on-shell; diagonal lapse combination is null.

    Not a statement about the functional Poisson algebra of inhomogeneous
    spherical perturbations, nor the 4D Hassan--Rosen BD secondary.
    """
    par,q,nf=candidate_dust_point(a)
    bg,bf=secondary_preservation_brackets(par,q)
    # Constraint order Hg,Hf,chi; on-shell {Hg,Hf}=0, {chi,Hg}=bg.
    D=np.array([[0.,0.,-bg],[0.,0.,-bf],[bg,bf,0.]])
    assert np.linalg.matrix_rank(D,tol=1e-7)==2
    np.testing.assert_allclose(D@np.array([1.,nf,0.]),0.,atol=4e-10)
    # Both dust momenta remain conserved and independent of the lapse ratio.
    for dust in (lambda p,q:q.pg,lambda p,q:q.pf):
        for constraint in (mini_hg,mini_hf,mini_chi):
            assert abs(canonical_bracket_fd(dust,constraint,par,q))<2e-9

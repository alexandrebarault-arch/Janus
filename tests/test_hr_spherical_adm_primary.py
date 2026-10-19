"""Independent spherical EH Legendre and full HR lapse-linear shift controls."""
import math
import numpy as np
import pytest
from numerics.hr_spherical_adm_primary import (
    Geometry,spatial_curvature,eh_adm_density,eh_canonical_momenta,
    eh_hamiltonian_constraints,dust_hamiltonian_constraints,hr_beta_combinations,
    hr_lagrangian,relative_shift,hr_linear_lapse_coefficients,
    relative_shift_constraint,solve_relative_shift,coupled_primary,
    coupled_hamiltonian,
)

G=Geometry(1.16,.74,.07,1.13,-.09,1.8)
F=Geometry(.83,.55,-.035,.92,.04,.91)
B=(.21,.78,-.35,.16,.11)
M2=.67


def independent_hr(g,f,Ng,Nf,Vg,Vf,betas=B,m2=M2):
    """Independent exact 2x2 ADM metric inverse and e0...e4 density."""
    g2=np.array([[-Ng**2+g.L**2*Vg**2,g.L**2*Vg],
                 [g.L**2*Vg,g.L**2]])
    f2=np.array([[-Nf**2+f.L**2*Vf**2,f.L**2*Vf],
                 [f.L**2*Vf,f.L**2]])
    Y=np.linalg.solve(g2,f2)
    s=np.sqrt(np.linalg.det(Y))
    tr=np.sqrt(np.trace(Y)+2*s)
    e=f.S/g.S
    en=(1.,tr+2*e,s+2*e*tr+e*e,2*e*s+e*e*tr,e*e*s)
    return -m2*g.planck2*Ng*g.L*g.S*g.S*sum(b*x for b,x in zip(betas,en))


def fdd(fun,x,h=1e-4):
    return (fun(x+h)+fun(x-h)-2*fun(x))/(h*h)


def test_3curvature_flat_spherical_and_nonzero_geometry():
    flat=Geometry(1.3,1.3*.63,0.,1.3,0.,.8)
    assert spatial_curvature(flat)==pytest.approx(0,abs=1e-13)
    assert abs(spatial_curvature(G))>.01


def test_gravitational_momenta_reproduce_independent_lagrangian_derivatives():
    N=1.24;V=.037;Vr=-.018;Ld=.11;Sd=.06
    pL,pS=eh_canonical_momenta(G,N=N,V=V,Vr=Vr,Ldot=Ld,Sdot=Sd)
    h=2e-6
    for which,p in [('L',pL),('S',pS)]:
        def val(q):
            return eh_adm_density(G,N=N,V=V,Vr=Vr,
                Ldot=q if which=='L' else Ld,Sdot=q if which=='S' else Sd)
        q=Ld if which=='L' else Sd
        assert (val(q+h)-val(q-h))/(2*h)==pytest.approx(p,rel=3e-9,abs=2e-10)


def test_legendre_gravity_local_exact_before_shift_integration_by_parts():
    N=1.17;V=.034;Vr=.021;Ld=.13;Sd=-.014
    pL,pS=eh_canonical_momenta(G,N=N,V=V,Vr=Vr,Ldot=Ld,Sdot=Sd)
    c,d=eh_hamiltonian_constraints(G,pL=pL,pS=pS,pLr=-.076)
    leg=pL*Ld+pS*Sd-eh_adm_density(G,N=N,V=V,Vr=Vr,Ldot=Ld,Sdot=Sd)
    expected=N*c+V*(pL*G.Lr+pS*G.Sr)+Vr*G.L*pL
    assert leg==pytest.approx(expected,abs=2e-14)
    assert d==pytest.approx(pS*G.Sr+G.L*.076,abs=1e-15)


def test_eh_constraints_kinetic_formula_matches_inverse_legendre():
    pL=-.18;pS=.34;N=1.1;V=-.025;Vr=.013
    Kt=-pL/(2*G.planck2*G.S**2)
    Kr=-pS/(2*G.planck2*G.L*G.S)-Kt
    Ldot=N*G.L*Kr+V*G.Lr+G.L*Vr
    Sdot=N*G.S*Kt+V*G.Sr
    pp=eh_canonical_momenta(G,N=N,V=V,Vr=Vr,Ldot=Ldot,Sdot=Sdot)
    assert pp==pytest.approx((pL,pS),abs=1e-14)


def test_two_independent_dust_constraints_exact_and_affine_in_true_adm():
    cg,rg=dust_hamiltonian_constraints(G,p=.23,theta_r=.075)
    cf,rf=dust_hamiltonian_constraints(F,p=.14,theta_r=-.044)
    assert cg>0 and cf>0
    assert cg==pytest.approx(.23*np.sqrt(1+(.075/G.L)**2),abs=1e-15)
    assert rg==pytest.approx(.23*.075)
    assert rf==pytest.approx(.14*(-.044))
    with pytest.raises(ValueError):dust_hamiltonian_constraints(G,p=0,theta_r=0)


@pytest.mark.parametrize('Ng,Nf,Vg,Vf',[(1.17,.91,.025,-.032),(.93,1.33,.041,.044),(1.8,.71,-.13,.15)])
def test_exact_hr_lagrangian_vs_independent_two_by_two_principal_root(Ng,Nf,Vg,Vf):
    s=hr_lagrangian(G,F,Ng=Ng,Nf=Nf,Vg=Vg,Vf=Vf,betas=B,m2=M2)
    assert s==pytest.approx(independent_hr(G,F,Ng,Nf,Vg,Vf),rel=3e-14,abs=2e-15)


@pytest.mark.parametrize('z',[-.41,0.,.33])
def test_hr_shift_redefinition_is_lapse_affine_at_fixed_z(z):
    for Ng,Nf,V in ((1.21,.85,.06),(.74,1.19,-.05),(1.53,1.41,.023)):
        Vg,Vf=relative_shift(G,F,Ng=Ng,Nf=Nf,V=V,z=z)
        lin=hr_linear_lapse_coefficients(G,F,z=z,betas=B,m2=M2)
        nonlinear=-hr_lagrangian(G,F,Ng=Ng,Nf=Nf,Vg=Vg,Vf=Vf,betas=B,m2=M2)
        assert nonlinear==pytest.approx(Ng*lin[0]+Nf*lin[1],abs=4e-15)
        assert nonlinear==pytest.approx(-independent_hr(G,F,Ng,Nf,Vg,Vf),rel=5e-14)


def test_fixed_original_shift_is_not_generically_lapse_affine():
    def h(n):return -hr_lagrangian(G,F,Ng=n,Nf=.92,Vg=.22,Vf=-.15,betas=B,m2=M2)
    assert abs(fdd(h,1.3,h=1e-3))>1e-4
    # New variables (V,z) instead yield exact ZERO second lapse derivative.
    def linear(n):
        a,b=relative_shift(G,F,Ng=n,Nf=.92,V=.04,z=.35)
        return -hr_lagrangian(G,F,Ng=n,Nf=.92,Vg=a,Vf=b,betas=B,m2=M2)
    assert abs(fdd(linear,1.3,h=1e-3))<3e-9


def test_all_five_betas_and_beta0_beta4_separate_lapse_coefficients():
    for i in range(5):
        bs=tuple(1. if j==i else 0. for j in range(5))
        wg,wf=hr_linear_lapse_coefficients(G,F,z=.24,betas=bs,m2=M2)
        Vg,Vf=relative_shift(G,F,Ng=1.05,Nf=.77,V=.08,z=.24)
        assert -hr_lagrangian(G,F,Ng=1.05,Nf=.77,Vg=Vg,Vf=Vf,betas=bs,m2=M2)==pytest.approx(1.05*wg+.77*wf,abs=1e-15)
        if i==0:assert wf==pytest.approx(0,abs=1e-14)
        if i==4:assert wg==pytest.approx(0,abs=1e-14)


def test_relative_shift_equation_lapse_independent_and_derivative_identity():
    params=dict(pLg=.19,pSg=-.27,pLrg=.043,
                pLf=-.17,pSf=.33,pLrf=-.012,pg=.18,thrg=.062,
                pf=.092,thrf=-.034,z=.29,betas=B,m2=M2)
    C=coupled_primary(G,F,**params)
    rhs=relative_shift_constraint(G,F,Dg=C.Dg,z=.29,betas=B,m2=M2)
    for Ng,Nf,V in ((1.4,.93,.04),(.86,1.21,-.018)):
        def H(z):
            p=dict(params,z=z)
            return coupled_hamiltonian(coupled_primary(G,F,**p),Ng=Ng,Nf=Nf,V=V)
        h=1e-6
        numerical=(H(.29+h)-H(.29-h))/(2*h)
        assert numerical==pytest.approx((Ng/G.L+Nf/F.L)*rhs,rel=3e-9,abs=3e-10)


def test_solve_relative_shift_and_decoupled_no_mass_limit():
    Dg=.18
    z=solve_relative_shift(G,F,Dg=Dg,betas=B,m2=M2)
    assert abs(z)<1
    assert relative_shift_constraint(G,F,Dg=Dg,z=z,betas=B,m2=M2)==pytest.approx(0,abs=1e-14)
    with pytest.raises(ValueError):solve_relative_shift(G,F,Dg=0.,betas=B,m2=0.)
    with pytest.raises(ValueError):solve_relative_shift(G,F,Dg=.1,betas=(0,0,0,0,0),m2=M2)


def test_full_coupled_hamiltonian_lapse_common_shift_affine_both_dust():
    params=dict(pLg=.19,pSg=-.27,pLrg=.043,pLf=-.17,pSf=.33,pLrf=-.012,
                pg=.18,thrg=.062,pf=.092,thrf=-.034,z=-.31,betas=B,m2=M2)
    C=coupled_primary(G,F,**params)
    for Ng,Nf,V in ((1.4,.93,.04),(.86,1.21,-.018)):
        v=coupled_hamiltonian(C,Ng=Ng,Nf=Nf,V=V)
        h=1e-5
        assert (coupled_hamiltonian(C,Ng=Ng+h,Nf=Nf,V=V)-coupled_hamiltonian(C,Ng=Ng-h,Nf=Nf,V=V))/(2*h)==pytest.approx(C.Hg,rel=4e-11,abs=2e-11)
        assert (coupled_hamiltonian(C,Ng=Ng,Nf=Nf+h,V=V)-coupled_hamiltonian(C,Ng=Ng,Nf=Nf-h,V=V))/(2*h)==pytest.approx(C.Hf,rel=4e-11,abs=2e-11)
        assert (coupled_hamiltonian(C,Ng=Ng,Nf=Nf,V=V+h)-coupled_hamiltonian(C,Ng=Ng,Nf=Nf,V=V-h))/(2*h)==pytest.approx(C.Ddiag,rel=4e-11,abs=2e-11)
        assert v==pytest.approx(Ng*C.Hg+Nf*C.Hf+V*C.Ddiag,abs=1e-15)


def test_two_dust_momenta_remain_distinct_in_primary_coefficients():
    base=dict(pLg=.19,pSg=-.27,pLrg=.043,pLf=-.17,pSf=.33,pLrf=-.012,
              pg=.18,thrg=.062,pf=.092,thrf=-.034,z=-.13,betas=B,m2=M2)
    C=coupled_primary(G,F,**base)
    gnew=coupled_primary(G,F,**dict(base,pg=base['pg']+.001))
    fnew=coupled_primary(G,F,**dict(base,pf=base['pf']+.001))
    assert abs(gnew.Hg-C.Hg)>1e-5
    # The lapse-dependent relative-shift redefinition has z*Dg/Lf in Hf.
    # Thus g dust momentum correctly enters the f-lapse COEFFICIENT through
    # the g radial momentum constraint, even though f's own dust pair is distinct.
    assert gnew.Hf-C.Hf==pytest.approx(base['z']*(gnew.Dg-C.Dg)/F.L,abs=1e-14)
    assert fnew.Hg==pytest.approx(C.Hg,abs=1e-14)
    assert abs(fnew.Hf-C.Hf)>1e-5


def test_guards_lapse_square_root_and_nonlorentzian_data():
    with pytest.raises(ValueError):Geometry(0.,1).check()
    with pytest.raises(ValueError):Geometry(1.,1.,planck2=-1).check()
    with pytest.raises(ValueError):hr_lagrangian(G,F,Ng=1,Nf=1,Vg=20,Vf=0,betas=B,m2=M2)
    with pytest.raises(ValueError):relative_shift(G,F,Ng=1,Nf=1,V=0,z=1.)
    with pytest.raises(ValueError):hr_linear_lapse_coefficients(G,F,z=1.01,betas=B,m2=M2)
    with pytest.raises(ValueError):hr_lagrangian(G,F,Ng=1,Nf=1,Vg=0,Vf=0,betas=(1,2),m2=M2)


def test_radial_shift_integrated_by_parts_with_compact_boundary():
    nodes,w=np.polynomial.legendre.leggauss(64)
    r=.5*(nodes+1)
    L=1+.2*r+.05*r*r;Lr=.2+.1*r
    S=.4+r+.1*r*r;Sr=1+.2*r
    pL=.07+.11*r+.04*r*r;pLr=.11+.08*r
    pS=-.03+.02*r
    V=.02*r*r*(1-r)**2
    Vr=.04*r*(1-r)*(1-2*r)
    original=np.sum(.5*w*(V*(pL*Lr+pS*Sr)+Vr*pL*L))
    integrated=np.sum(.5*w*V*(pS*Sr-L*pLr))
    assert original==pytest.approx(integrated,abs=3e-16)


def test_relative_shift_elimination_retains_exact_lapse_linearity():
    params=dict(pLg=.19,pSg=-.27,pLrg=.043,pLf=-.17,pSf=.33,pLrf=-.012,
                pg=.18,thrg=.062,pf=.092,thrf=-.034,betas=B,m2=M2)
    trial=coupled_primary(G,F,z=0.,**params)
    z=solve_relative_shift(G,F,Dg=trial.Dg,betas=B,m2=M2)
    C=coupled_primary(G,F,z=z,**params)
    assert relative_shift_constraint(G,F,Dg=C.Dg,z=z,betas=B,m2=M2)==pytest.approx(0,abs=5e-15)
    for Ng,Nf,V in ((1.2,.8,.07),(.75,1.5,-.032)):
        # z solution is exactly the SAME under both independent lapses.
        assert z==pytest.approx(solve_relative_shift(G,F,Dg=C.Dg,betas=B,m2=M2),abs=0)
        h=coupled_hamiltonian(C,Ng=Ng,Nf=Nf,V=V)
        assert h==pytest.approx(Ng*C.Hg+Nf*C.Hf+V*C.Ddiag,abs=2e-15)


def test_no_interaction_yields_two_independent_eh_plus_dust_constraints():
    kw=dict(pLg=.19,pSg=-.27,pLrg=.043,pLf=-.17,pSf=.33,pLrf=-.012,
            pg=.18,thrg=.062,pf=.092,thrf=-.034,z=0.,betas=B,m2=0.)
    c=coupled_primary(G,F,**kw)
    eg,dg=eh_hamiltonian_constraints(G,pL=kw['pLg'],pS=kw['pSg'],pLr=kw['pLrg'])
    ef,df=eh_hamiltonian_constraints(F,pL=kw['pLf'],pS=kw['pSf'],pLr=kw['pLrf'])
    mg,rg=dust_hamiltonian_constraints(G,p=kw['pg'],theta_r=kw['thrg'])
    mf,rf=dust_hamiltonian_constraints(F,p=kw['pf'],theta_r=kw['thrf'])
    assert (c.Hg,c.Hf,c.Ddiag)==pytest.approx((eg+mg,ef+mf,dg+df+rg+rf),abs=2e-15)

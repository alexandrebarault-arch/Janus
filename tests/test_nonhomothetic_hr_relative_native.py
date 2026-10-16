import math
import numpy as np


def test_static_finite_mu_square_root_has_expected_temporal_and_spatial_eigenvalues():
    from numerics.nonhomothetic_hr_relative_native import relative_native_geometry
    a=1.3; n=0.8; alpha=0.91; r=0.7; mu=-0.2
    out=relative_native_geometry(a=a,n=n,alpha=alpha,r=r,mu=mu)
    gc=out.g_radial_native
    fc=out.jacobian_f.T@out.f_radial_native@out.jacobian_f
    A=np.linalg.solve(gc,fc)
    det=float(np.linalg.det(A)); tr=float(np.trace(A)); sd=math.sqrt(det)
    S=(A+sd*np.eye(2))/math.sqrt(tr+2*sd)
    ell=math.sqrt(out.f_angular_native/out.g_angular_native)
    vals=np.array([S[0,0],S[1,1],ell,ell])
    xi=alpha/a
    assert np.allclose(vals, [n,xi*(1+mu),xi*(1+mu),xi*(1+mu)], rtol=0, atol=3e-14)


def test_mu_zero_lapse_and_shift_linearization_matches_prebd_native_bridge():
    from numerics.nonhomothetic_hr_relative_native import relative_native_geometry
    a=1.2; n=0.85; alpha=0.9; r=0.8
    ndn=-0.08; eps=1e-7
    T=.3*eps; Td=-.21*eps; Pf=.11*eps
    out=relative_native_geometry(
        a=a,n=n,alpha=alpha,r=r,n_dot_over_n=ndn,
        T=T,T_dot=Td,Phi_f=Pf,
    )
    fc=out.jacobian_f.T@out.f_radial_native@out.jacobian_f
    phi_common=.5*((-fc[0,0]/(n*n))-1.0)
    assert math.isclose(phi_common, Pf-Td-ndn*T, rel_tol=0, abs_tol=2e-14)

    Tr=.2*eps; Ldotr=-.13*eps; Bfr=.07*eps
    out=relative_native_geometry(
        a=a,n=n,alpha=alpha,r=r,
        T_r=Tr,L_dot_r=Ldotr,B_f_r=Bfr,
    )
    fc=out.jacobian_f.T@out.f_radial_native@out.jacobian_f
    b_common_r=fc[0,1]/(n*alpha)
    target=Bfr+(n/alpha)*Tr-(alpha/n)*Ldotr
    assert math.isclose(b_common_r,target,rel_tol=0,abs_tol=2e-14)


def test_finite_mu_correction_vanishes_identically_on_linear_background():
    from numerics.nonhomothetic_hr_relative_native import relative_native_hr_correction_density
    value=relative_native_hr_correction_density(
        a=1.2,n=.85,alpha=.9,r=.7,
        n_dot_over_n=-.08,n_ddot_over_n=.03,
        alpha_dot_over_alpha=.17,alpha_ddot_over_alpha=.04,
        T=.012,T_dot=-.021,T_r=.017,L_r=-.011,L_dot_r=.009,L_rr=.006,
        Phi_g=.003,B_g_r=-.004,Phi_f=-.002,B_f_r=.005,
        mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,
        betas=(0.0,1.0,-.7,.3,.1),m2=1.7,Mg2=.9,
    )
    assert value == 0.0

"""Actual four original byte-authentic HR providers; new exact U3 center coefficient."""
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
import pytest
from numerics import hr_step55_global_barrier as old
from numerics.hr_step45_exact_physical_ward import exact_physical_ward
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
from numerics.hr_step55_normalized_secondary import normalized_symbolic
from numerics.hr_step67_true_center_taylor_certificate import (
    PINNED,J,verify_bytes,geometry_taylor,true_center_U3,manifest,interval_encloses)


def test_01_all_four_original_physical_git_sha_match_actual_bytes():
    assert verify_bytes()==PINNED and len(PINNED)==4


def test_02_mutated_single_byte_source_fails_closed(tmp_path):
    for name in PINNED:
        (tmp_path/name).write_bytes((Path(__file__).resolve().parents[1]/'numerics'/name).read_bytes())
    p=tmp_path/'hr_step55_global_barrier.py'
    p.write_bytes(p.read_bytes()+b'\n')
    with pytest.raises(ValueError,match='authentic historical module mismatch'):
        verify_bytes(tmp_path)


def test_03_true_original_six_pair_ward_identities_not_fabricated():
    d=exact_physical_ward()
    assert len(d['Q'])==12 and len(d['K'])==9
    assert all(x==0 for x in d['residuals'].values())
    assert d['C_exact']!=0


def test_04_real_primary_reduced_secondary_exact_restoration():
    x=exact_f_momentum_ode()
    assert all(v==0 for v in x['identity_residuals'].values())


def test_05_real_normalized_G_quadratic_in_U():
    G,s,U,v=normalized_symbolic()
    assert sp.degree(G,U)==2 and sp.diff(G,U,3)==0
    assert len(G.free_symbols)==22


def test_06_repeat_original_256_cell_step55_full_interval_proof():
    r=old.certify_global_barrier(cells=256)
    assert r['Step54_tube_hypothesis_proved_for_exact_radial_solution']
    assert F(r['strict_max_Fupper_rational'])<0
    assert F(r['strict_min_Flower_rational'])>0
    assert F(r['V_minus_Vstar_lower_rational'])>-F('0.01')
    assert F(r['V_minus_Vstar_upper_rational'])<F('0.01')


def test_07_truncated_jet_exact_multiplication_rational():
    s=J(coeffs=(0,1,0,0))
    f=(1+2*s+3*s**2)
    p=f*(1-s)
    assert [F(x.lo,old.S) for x in p.a]==[F(1),F(1),F(1),F(-3)]
    assert all(x.lo==x.hi for x in p.a)


def test_08_taylor_jet_reciprocal_identity_to_order_three():
    s=J(coeffs=(0,1,0,0))
    f=1+s/4
    p=f*f.inv()
    assert all(z.lo<=int(n==0)*old.S<=z.hi for n,z in enumerate(p.a))


def test_09_taylor_sqrt_identity_and_positive_branch():
    s=J(coeffs=(0,1,0,0))
    q=(1+s/4).sqrt()
    p=q*q
    assert all(z.lo<=target<=z.hi for z,target in zip(p.a,[old.S,old.S//4,0,0]))


def test_10_square_root_rejects_bad_or_zero_branch():
    with pytest.raises(ValueError):J(-1).sqrt()
    with pytest.raises(ZeroDivisionError):J(0).sqrt()


def test_11_benchmark_center_geometry_matches_actual_historical_provider():
    d=geometry_taylor(J(coeffs=(0,1,0,0)))
    reference=old.geometry(old.I.c(0))
    assert set(d)==set(reference) and len(d)>20
    assert all(interval_encloses(d[k].a[0],reference[k]) for k in d)


def test_12_first_three_real_center_ODE_coefficients_enclose_zero():
    c=true_center_U3()
    assert len(c['residuals'])==3
    assert all(x.lo<=0<=x.hi for x in c['residuals'])


def test_13_new_real_third_coefficient_negative_and_rigorously_tight():
    c=true_center_U3();u=c['U3']
    assert u.hi<0 and u.lo<=u.hi
    assert F('-0.000000012530066') < F(u.lo,old.S)
    assert F(u.hi,old.S) < F('-0.000000012530065')
    assert u.hi-u.lo<old.S//10**19


def test_14_exact_formal_recurrence_sign_and_factor_nine():
    # Independent toy with exact analytical regular solution U=u0+a s+b s²+c s³.
    s,U,u0,a,b,c=sp.symbols('s U u0 a b c')
    S=u0+a*s+b*s*s+c*s**3
    # Manufacture G such that 2sU_s=G(s,U)-2U on this exact solution,
    # while G(0,U)=3u0-U for arbitrary U.
    G=3*u0-U+s*(5*a+7*b*s+9*c*s*s+3*a*(U-u0-a*s))
    # Instead use simply G=3u0-U+s*(5a+7b*s+9c*s²)
    # and verify the formal U3=G(s,Ulo) coefficient /9.
    G=3*u0-U+s*(5*a+7*b*s+9*c*s*s)
    Ulo=u0+a*s+b*s*s
    coeff=sp.expand(G.subs(U,Ulo)).coeff(s,3)
    assert coeff==9*c
    assert sp.expand(2*s*sp.diff(S,s)-(G.subs(U,S)-2*S))==0


def test_15_third_center_coefficient_in_momentum_r_eight_and_pthird_over_r():
    r=sp.symbols('r');u0,u1,u2,u3=sp.symbols('u0 u1 u2 u3')
    P=r*r*(u0+u1*r*r+u2*r**4+u3*r**6)
    assert sp.diff(P,r).subs(r,0)==0
    assert sp.expand(sp.diff(P,r,3)/r-24*u1-120*u2*r*r-336*u3*r**4)==0


def test_16_manifest_refuses_false_dirac_or_lapse_conclusions():
    m=manifest()
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'
    assert m['original_six_pair_time_dirac']=='NOT_EVALUATED'
    assert m['lapse_fixing']=='NOT_DETERMINED'
    assert len(m['source_git_blobs'])==4

"""Step40 conservative continuum bounds for independently positive 2 dusts."""
from fractions import Fraction as F
from math import sqrt
import pytest
from numerics.hr_step40_curvature_box import M2,MG2,B1,B2,B3,A0,Y0,R
from numerics.hr_step40_twodust_interval import (MF2,CG,CF,ZG,KG,KF,B0,B4,
    I,h2_rational,density_coeff_intervals,interval_two_dust_certificate)


def direct_orig_density_over_r2(r,delta=()):
    """Original unsimplified Hamiltonian and radial-primary reconstruction.

    This standalone finite-precision control deliberately uses unsimplified
    pLi,S',R3,Dg,W_i and separate sector z*Dg/L_i, not interval formulas.
    """
    import math
    r=float(r);s=r*r;a=float(A0);y=float(Y0);b=a*y
    mf=float(MF2);m2=float(M2);mg=float(MG2)
    b0,b1,b2,b3,b4=map(float,(B0,B1,B2,B3,B4))
    h2=float(h2_rational());H=math.sqrt(h2)
    Pgs=-2*a*a*H;Pfs=-2*mf*b*a*H
    def geometry(ai,ci,P0,extra):
        u=1+ci*s
        L=ai*u*u;S=r*L;Sprime=ai*u*(1+5*ci*s)
        q=P0+sum(float(v)*s**k for k,v in enumerate(extra))
        ph=P0*(1+2.5*ci*s)+sum(float(v)*(s**k/(k+1)+5*ci*s**(k+1)/(k+2)) for k,v in enumerate(extra))
        pL=s*ph
        pLprime=2*r*(1+5*ci*s)*q
        R3=-48*ci/(ai*ai*u**5)
        return L,S,Sprime,pL,pLprime,R3
    Lg,Sg,Sgr,pLg,pLgr,Rg=geometry(a,float(CG),Pgs,())
    Lf,Sf,Sfr,pLf,pLfr,Rf=geometry(b,float(CF),Pfs,delta)
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    A0g=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    z=float(ZG)*r;root=sqrt(1-z*z)
    K=m2*mg*Lg*Lf*At
    Dg=K*z/root
    Wg=m2*mg*(Lg*A0g+Lf*At*root)
    Wf=m2*mg*(Lf*Af+Lg*At*root)
    def source(ai,Li,Si,Spi,pl,plprime,mi2,ki,Di,Wi,R3):
        thp=ki*r*Li
        fac=pl/(2*mi2*Si*Spi)
        grav=Li*pl**2/(4*mi2*Si**2)-fac*(Di+Li*plprime)-mi2*Li*Si*Si*R3/2
        numerator=grav+z*Dg/Li+Wi
        coeff=sqrt(1+(thp/Li)**2)+fac*thp
        return -numerator/(coeff*s)
    return source(a,Lg,Sg,Sgr,pLg,pLgr,mg,float(KG),Dg,Wg,Rg),source(b,Lf,Sf,Sfr,pLf,pLfr,mf,float(KF),-Dg,Wf,Rf)


def test_exact_interval_arithmetic_and_sqrt_enclosures():
    x=I(F(-1),F(2));y=I(F(2),F(3))
    assert x*y==I(F(-3),F(6))
    assert x**2==I(F(0),F(4))
    assert x**3==I(F(-1),F(8))
    assert I.point(F(2)).sqrt().lo**2<=2<=I.point(F(2)).sqrt().hi**2
    with pytest.raises(ValueError):x.inv()
    with pytest.raises(ValueError):I.point(-1).sqrt()


@pytest.mark.parametrize('r',('0.025','0.1','0.43','0.7','0.85'))
def test_independent_original_unsimplified_hamiltonian_matches_interval(r):
    g,f=direct_orig_density_over_r2(F(r))
    gi,fi=density_coeff_intervals(I.point(F(r)**2))
    # Independent reference uses float sqrt/cancellation (~1e-15), whereas
    # the certified Fraction interval can be narrower than that rounding.
    assert abs(g-float((gi.lo+gi.hi)/2))<1e-12
    assert abs(f-float((fi.lo+fi.hi)/2))<1e-12
    assert min(g,f)>0


def test_continuous_baseline_two_dust_certificate_without_sampling():
    c=interval_two_dust_certificate(ncells=256)
    assert F(c['strict_pg_over_r2_lower'])>F('.88')
    assert F(c['strict_pf_over_r2_lower'])>F('.11')
    assert c['GATE_2B']=='OPEN'


def test_uniform_even_momentum_perturbation_ball_still_positive():
    c=interval_two_dust_certificate(ncells=256,f_delta_per_coefficient_bound=F('.005'))
    assert F(c['strict_pg_over_r2_lower'])>F('.88')
    assert F(c['strict_pf_over_r2_lower'])>F('.039')
    assert c['f_delta_per_coefficient_bound']=='1/200'


@pytest.mark.parametrize('r',('.1','.4','.8'))
def test_independent_polynomial_perturbed_f_source_contained(r):
    extra=(F('.004'),F('-.002'),F('.001'),F(0),F(0))
    g,f=direct_orig_density_over_r2(F(str(r)),extra)
    gi,fi=density_coeff_intervals(I.point(F(str(r))**2),F('.005'))
    # Independent reference uses float sqrt/cancellation (~1e-15), whereas
    # the certified Fraction interval can be narrower than that rounding.
    assert abs(g-float((gi.lo+gi.hi)/2))<1e-12
    # Finite uncertainty box intentionally surrounds MANY possible f moments;
    # its midpoint need not equal the specifically chosen nonzero delta.
    assert float(fi.lo)-1e-12<f<float(fi.hi)+1e-12
    assert f>0


def test_certificate_rejects_insufficiently_narrow_interval_cover():
    with pytest.raises((ValueError,ArithmeticError)):
        interval_two_dust_certificate(ncells=2)
    with pytest.raises(ValueError):
        interval_two_dust_certificate(f_delta_per_coefficient_bound=F(-1))


def test_fails_closed_if_correction_ball_too_large():
    with pytest.raises(ArithmeticError):
        interval_two_dust_certificate(ncells=256,f_delta_per_coefficient_bound=F('.007'))

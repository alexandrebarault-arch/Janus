"""Targeted rigorous signs for CONDITIONAL tube, original physical primary check."""
from fractions import Fraction as F
from pathlib import Path
import pytest
import mpmath as mp
from numerics.hr_step54_interval_tube import (
    I,S,authentic_sources,PINS,profiles,certify,U0,U1,U2,H2,A,B,MF,MG,M2,
    CG,CF,KG,KF,Z1,B0,B1,B2,B3,B4
)
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
import sympy as sp


def test_byte_exact_historical_physical_six_pair_sources():
    assert authentic_sources()==PINS


def test_tampered_source_pin_fails_closed(monkeypatch):
    from numerics import hr_step54_interval_tube as module
    altered=dict(PINS)
    altered['numerics/hr_step46_exact_secondary_ode.py']='0'*40
    monkeypatch.setattr(module,'PINS',altered)
    with pytest.raises(AssertionError,match='AUTHENTIC provider'):
        module.authentic_sources()


def test_integer_lattice_outward_rational_and_sqrt_bounds():
    x=I.c(F(1,3));y=I.c(F(2,7))
    assert F(x.lo,S)<=F(1,3)<=F(x.hi,S)
    assert F(y.lo,S)<=F(2,7)<=F(y.hi,S)
    for op,exact in ((x+y,F(13,21)),(x*y,F(2,21)),(x/y,F(7,6))):
        assert F(op.lo,S)<=exact<=F(op.hi,S)
    z=I.c(F(2)).sqrt()
    assert F(z.lo,S)**2<=2<=F(z.hi,S)**2
    neg=I.hull(-4,-2).inv()
    assert F(neg.lo,S)<=F(-1,2) and F(neg.hi,S)>=F(-1,4)
    with pytest.raises(ZeroDivisionError):I.hull(-1,1).inv()


def test_exact_lattice_cell_decomposition_covers_whole_interval():
    cells=256;end=F('.85')**2
    prior=F(0)
    for i in range(cells):
        slab=I.hull(end*i/cells,end*(i+1)/cells)
        assert F(slab.lo,S)<=prior<=F(slab.hi,S)
        prior=end*(i+1)/cells
        assert F(slab.lo,S)<=prior<=F(slab.hi,S)
    assert prior==F('0.7225')


def test_conditional_dust_chart_positive_everywhere_0_to_085_256_cells():
    result=certify(cells=256,delta='0.01')
    assert result['GLOBAL_CENTRE_TO_ENDPOINT_ODE_ERROR_TUBE_VERIFIED'] is False
    for k,lower in result['minima_lower_fixed_grid_exact'].items():
        assert F(lower)>0, k
    assert F(result['minima_lower_fixed_grid_exact']['rho_g'])>F('.8854')
    assert F(result['minima_lower_fixed_grid_exact']['rho_f'])>F('.063')
    assert F(result['minima_lower_fixed_grid_exact']['J'])>F('.659')
    assert F(result['minima_lower_fixed_grid_exact']['K_over_r2'])>F('.229')
    assert result['GATE_2B']=='OPEN' and result['JANUS_R']=='NOT_VALIDATED'


def test_increasing_subdivision_tightens_continuous_bounds():
    coarse=certify(cells=32,delta='.0001')
    fine=certify(cells=256,delta='.0001')
    for field in ('rho_g','rho_f','J','K_over_r2'):
        assert F(fine['minima_lower_fixed_grid_exact'][field])>=F(coarse['minima_lower_fixed_grid_exact'][field])


def test_frozen_polynomial_tube_is_not_an_ode_membership_proof():
    r=certify(64,delta='.01')
    assert r['GLOBAL_CENTRE_TO_ENDPOINT_ODE_ERROR_TUBE_VERIFIED'] is False
    assert 'IF |U' in r['logical_scope']
    assert 'Dirac' in r['full_six_pair_Dirac_time_preservation'] or r['full_six_pair_Dirac_time_preservation']=='NOT_COMPUTED'


def test_sign_certificate_rejects_wrong_radius_grid_precision():
    with pytest.raises(ValueError):certify(cells=10)
    with pytest.raises(ValueError):certify(cells=9000)
    with pytest.raises(ValueError):certify(radius='0.86')
    with pytest.raises(ValueError):certify(delta='-.01')
    with pytest.raises(ValueError):profiles(I.c(-1))


def test_original_spherical_f_primary_oracle_agrees_with_normalized_interval():
    """No Step54 dust formula in oracle: use authentic Step46 SymPy f-dust equation."""
    mp.mp.dps=75
    src=exact_f_momentum_ode()
    original=src['p_f']
    free=sorted(original.free_symbols,key=str)
    fn=sp.lambdify(free,original,'mpmath',cse=True)
    def M(x):return mp.mpf(str(x))
    a=M('.4');yy=M('.5787707228025044');b=a*yy
    mg=mp.mpf(1);mf=M('.10879548725')**2;m2=M('23.3348939346')
    b0,b1,b2,b3,b4=map(M,('0','1','-4.2383993109','13.6801214252','-38.5117901844'))
    cg=M('.0015');cf=M('-.0012');kg=M('.0012');kf=M('-.0016');z1=M('.004')
    hh=mp.sqrt(M('.9')/(3*a**3)+m2*(b0+3*b1*yy+3*b2*yy**2+b3*yy**3)/3)
    Pg=-2*a*a*hh
    u0=mf*b*(Pg/(mg*a)-2*z1)
    u1=M('0.0007897451667202464909325108904961683602148118201691')
    u2=M('-0.00001007385348674382817573689095286393593388364194376377343')
    for rtxt in ('.05','.3','.61','.85'):
        r=M(rtxt);s=r*r;ug=1+cg*s;uf=1+cf*s
        Lg=a*ug**2;Lf=b*uf**2;Sg=r*Lg;Sf=r*Lf;Sfr=b*uf*(1+5*cf*s)
        T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2
        Dg=m2*mg*Lg*Lf*(s*T)*z1*r/mp.sqrt(1-z1*z1*s)
        Tf=b2*Lg**2+2*b3*Lg*Lf+b4*Lf**2
        Wf=m2*mg*(Lf*s*Tf+Lg*s*T*mp.sqrt(1-z1*z1*s))
        Rf=-48*cf/(b*b*uf**5)
        U=u0+u1*s+u2*s*s;V=2*u0+4*u1*s+6*u2*s*s
        values={'Lg':Lg,'Lf':Lf,'Sg':Sg,'Sf':Sf,'pLf':s*U,'Sfr':Sfr,
          'tfr':kf*r*Lf,'z':z1*r,'V_pLf_prime':r*V,
          'Mf2':mf,'R3f_original':Rf,'Dg_original':Dg,'Wf_original':Wf}
        assert set(map(str,free))<=set(values),set(map(str,free))-set(values)
        original_pf=fn(*[values[str(x)] for x in free])/(r*r)
        interval=profiles(I.c(F(rtxt)**2),I.c(0))['rho_f']
        assert mp.mpf(interval.lo)/S<=original_pf<=mp.mpf(interval.hi)/S

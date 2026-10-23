"""Targeted physically pinned global radial barrier and exact integer checks.

Tests the independent Step54 dust positivity implications only as theorems
reported in that step; does not re-run every historical test module.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import pytest
import sympy as sp
from numerics.hr_step55_normalized_secondary import (
    normalized_symbolic, check_original_source_blobs, SOURCE_BLOBS
)
from numerics.hr_step55_global_barrier import (
    I,S,geometry,compiled,G,stars,residual,certify_global_barrier,U0,U1,U2
)

@pytest.fixture(scope='module')
def certified():return certify_global_barrier(256,'0.0001','0.01')

def test_original_six_pair_physical_sources_byte_exact():
    assert check_original_source_blobs()==SOURCE_BLOBS

def test_any_changed_historical_source_fails_closed(monkeypatch):
    import numerics.hr_step55_normalized_secondary as src
    corrupt=dict(SOURCE_BLOBS)
    corrupt['numerics/hr_step46_exact_secondary_ode.py']='0'*40
    monkeypatch.setattr(src,'SOURCE_BLOBS',corrupt)
    with pytest.raises(ValueError,match='Original six-pair source mismatch'):
        src.check_original_source_blobs()

def test_integer_outward_interval_contains_exact_rational_arithmetic():
    for a,b in ((F(3,7),F(7,9)),(F(-11,5),F(2,13)),(F(-3,11),F(-7,2))):
        x=I.c(a);y=I.c(b)
        for op,want in ((x+y,a+b),(x-y,a-b),(x*y,a*b),(x/y,a/b)):
            assert F(op.lo,S)<=want<=F(op.hi,S)
    rad=I.c(F(2)).sqrt()
    assert F(rad.lo,S)**2<=2<=F(rad.hi,S)**2
    with pytest.raises(ZeroDivisionError):I.hull(-1,1).inv()

def test_normalized_symbolic_rhs_has_no_remaining_r_singularity():
    expr,s,u,vars=normalized_symbolic()
    assert s in expr.free_symbols and u in expr.free_symbols
    assert len(expr.free_symbols)==22
    assert sp.count_ops(expr)<1500
    assert len(compiled()[0])==22

def test_original_center_implicit_identity_on_certified_branch():
    eps=I.c(F(1,10000))
    at0=I.c(0)
    # Step49 exact identity G(0,U0+e)=2U0-e, with outward intervals.
    for shift in (eps,-eps,I.c(0)):
        lhs=G(at0,U0+shift)
        target=2*U0-shift
        assert lhs.lo<=target.hi and lhs.hi>=target.lo
        assert max(abs(lhs.lo-target.lo),abs(lhs.hi-target.hi))<10**7

def test_every_s_cell_covered_and_barriers_strict(certified):
    end=F('0.85')**2
    for j in range(256):
        slab=I.hull(end*j/256,end*(j+1)/256)
        assert F(slab.lo,S)<=end*j/256<=F(slab.hi,S)
        assert F(slab.lo,S)<=end*(j+1)/256<=F(slab.hi,S)
    assert F(certified['strict_max_Fupper_rational'])<0
    assert F(certified['strict_min_Flower_rational'])>0
    assert certified['Step54_tube_hypothesis_proved_for_exact_radial_solution'] is True

def test_v_derivative_condition_entire_interval(certified):
    assert F(certified['V_minus_Vstar_lower_rational'])>F('-0.01')
    assert F(certified['V_minus_Vstar_upper_rational'])<F('0.01')
    # Stronger observed certified fractional bounds, not rounded floats:
    assert F(certified['V_minus_Vstar_lower_rational'])>F('-0.0021')
    assert F(certified['V_minus_Vstar_upper_rational'])<F('0.0021')

def test_finer_cells_improve_barrier_fraction_margins(certified):
    finer=certify_global_barrier(512,'0.0001','0.01')
    assert F(finer['strict_max_Fupper_rational'])<=F(certified['strict_max_Fupper_rational'])
    assert F(finer['strict_min_Flower_rational'])>=F(certified['strict_min_Flower_rational'])

def test_broad_u_tube_does_not_falsely_prove_derivative_tube():
    # U radius 0.001 is invariant but V enclosure is too wide at 256 cells;
    # fail-closed rather than declaring the Step54 derivative margin satisfied.
    with pytest.raises(ArithmeticError,match='normalized V missing Step54 tube'):
        certify_global_barrier(256,'0.001','0.01')

def test_invalid_grid_and_bounds_fail_closed():
    for inputs in ({'cells':16},{'cells':8193},{'delta_U':'-0.1'},
                   {'delta_U':'0.1'},{'delta_V':'.1'}):
        with pytest.raises(ValueError):certify_global_barrier(**inputs)

def test_dont_promote_spatial_barrier_to_Dirac_ghost_freedom(certified):
    assert certified['GATE_2B']=='OPEN'
    assert certified['JANUS_R']=='NOT_VALIDATED'
    assert certified['Dirac_secondary_time_preservation']=='NOT_COMPUTED'
    assert certified['lapse_fixing']=='NOT_COMPUTED'
    assert 'spatial' in certified['logical_scope']

def test_direct_original_nonsimplified_rhs_vs_normalized_kernel():
    """Independent computational path through original Step46 RHS on 3 radii."""
    from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
    expression=exact_f_momentum_ode()['pLf_prime_rhs']
    syms=sorted(expression.free_symbols,key=str)
    fn=sp.lambdify(syms,expression,
        modules=[{'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
    for rv in (F('.05'),F('.35'),F('.85')):
        r=I.c(rv);s=r*r
        source=geometry(s);u,_,_=stars(s)
        source.update({
         'Lg':source['Lg0'],'Lf':source['Lf0'],
         'Sg':r*source['Lg0'],'Sf':r*source['Lf0'],
         'pLg':r*r*source['Gmom'],'pLf':r*r*u,
         'pSg':r*source['Psg0'],'pg':r*r*source['Rhog'],
         'Lgr':r*source['Lgr0'],'Lfr':r*source['Lfr0'],
         'Sgr':source['Sgr0'],'Sfr':source['Sfr0'],
         'pLgr':r*source['Gprime'],
         'tgr':r*source['tg0'],'tfr':r*source['tf0'],
         'z':r*source['z1'],'zr':source['z1'],'zrr':I.c(0),
         'Dg_original':r**3*source['Dbar'],
         'Wf_original':r*r*source['Wfbar'],'R3f_original':source['Rf']})
        orig=fn(*[source[str(x)] for x in syms]);normalized=r*G(s,u)
        assert orig.lo<=normalized.hi and normalized.lo<=orig.hi
        # The raw symbolic expression suffers harmless dependency widening
        # in interval arithmetic; the normalized tighter enclosure must
        # nevertheless be fully contained in the unreduced original one.
        assert orig.lo<=normalized.lo<=normalized.hi<=orig.hi

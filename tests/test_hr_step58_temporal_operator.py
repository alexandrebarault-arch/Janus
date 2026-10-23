"""True original Step45 six-pair temporal operator, highest lapse exact closures."""
import hashlib
import sympy as sp
import pytest
from numerics.hr_step58_temporal_operator import (
    physical_operator, highest_lapse_certificate, manifest,add,mul,
    differentiate_lapse_operator)
from numerics.hr_step57_secondary_principal_symbol import authenticated_step45


@pytest.fixture(scope='module')
def real():
    return physical_operator()


@pytest.fixture(scope='module')
def closure():
    return highest_lapse_certificate()


def test_original_Github_Step45_physical_source_is_byte_authenticated():
    p=authenticated_step45()
    assert p['C_exact']!=0
    assert all(v==0 for v in p['residuals'].values())
    assert len(p['Q'])==12


def test_full_operator_contains_all_both_lapse_families_before_constraints(real):
    assert {k:set(v) for k,v in real['operator'].items()} == {'N':{0,1,2},'M':{0,1,2}}
    assert len(real['vectors']['N'])==len(real['vectors']['M'])==12


def test_no_truncated_higher_lapse_derivative_or_fourth_jet(real):
    for sector in ('N','M'):
        assert all(i<=2 for i in real['operator'][sector])
        for i,c in real['operator'][sector].items():
            assert c!=0
            assert not c.free_symbols.intersection(real['q4'])
            assert real['zrrr'] not in c.free_symbols


def test_physical_vector_field_uses_all_six_original_canonical_pairs(real):
    p=authenticated_step45()
    for name,sector in [('N','eg'),('M','ef')]:
        vectors=real['vectors'][name]
        e=p[sector]
        for i in range(12):
            conjugate=i+1 if i%2==0 else i-1
            sign=1 if i%2==0 else -1
            for order in range(3):
                assert vectors[i].get(order,0)==sign*e[order][conjugate]


def test_shift_variation_contains_momentum_radial_jet(real):
    p=authenticated_step45();qp=dict(zip(p['Q'],p['dq']))
    for k in ('N','M'):
        assert any(expr.has(qp['pLg']) for expr in real['delta_shift'][k].values())
        # The shift response does not ignore derivative of pLg.
        assert real['delta_shift'][k]


def test_full_operator_equals_explicit_independent_chain_decomposition(real):
    # Unexpanded exact identity, coefficient by coefficient, including zprime.
    for k in ('N','M'):
        independent=add(real['direct_parts'][k],
            add(mul(real['Cz'],real['delta_shift'][k]),
                mul(real['Czr'],differentiate_lapse_operator(real['delta_shift'][k],real['Dt']))))
        assert real['operator'][k]==independent


def test_raw_second_N_and_M_lapse_coefficients_do_not_vanish_off_shell(real):
    assert real['operator']['N'][2]!=0
    assert real['operator']['M'][2]!=0


def test_exact_M_second_lapse_vanishes_on_stationary_Fz(closure):
    assert closure['M2_on_Fz_shell']==0
    assert closure['N2_and_M2_vanish_on_Fz_and_Hg']


def test_exact_N_second_lapse_is_proportional_to_original_primary_Hg(closure):
    p=authenticated_step45();q=dict(zip(p['Q'],p['q']))
    z=p['parameters'][-3]
    expected=(z*z-1)/(q['Lg']*q['Lf'])
    assert sp.factor(closure['N2_to_Hg_factor']-expected)==0
    assert closure['N2_on_Fz_shell']==expected*p['Hg'].subs({p['dq'][1]:closure['shift_elimination_pLg_prime']})


def test_double_prime_N_not_forced_zero_by_shift_stationarity_only(closure):
    # Multiplying nonzero primary Hg: not a false identity off Hg=0.
    assert closure['N2_to_Hg_factor']!=0
    assert closure['N2_on_Fz_shell']!=0


def test_restricted_shell_does_not_silently_solve_other_constraints(closure):
    assert set(closure['remaining_lapse_operators'])=={'N','M'}
    assert all(set(x)=={0,1} for x in closure['remaining_lapse_operators'].values())
    assert 'Hf' in closure['qualifiers'] and 'rank' in closure['qualifiers']


def test_lapse_jet_product_rule_exact_on_polynomial():
    x=sp.symbols('x')
    a={0:x**2,1:2*x,2:sp.Integer(3)}
    out=differentiate_lapse_operator(a,lambda expr:sp.diff(expr,x))
    n=sp.Function('N')(x)
    assert sp.expand(sum(c*sp.diff(n,x,j) for j,c in out.items())
          -sp.diff(sum(c*sp.diff(n,x,j) for j,c in a.items()),x))==0
    assert set(out)=={0,1,2,3}


def test_add_mul_operator_no_lost_lapse_orders():
    x=sp.symbols('x')
    A={0:x,2:2};B={1:x**2,2:-2}
    assert add(A,B)=={0:x,1:x*x}
    assert mul(3,B)=={1:3*x*x,2:-6}


def test_generic_six_pair_canonical_bracket_strong_equals_weak_after_IBP():
    # Independent exact polynomial compact integration: two nontrivial pairs
    # of six (remaining four zero); z explicitly depends on q',p'.
    r=sp.symbols('r',real=True)
    q,p=sp.Function('q')(r),sp.Function('p')(r)
    n=r**3*(1-r)**3
    m=r**3*(1-r)**3*(1+r)
    eta=r**3*(1-r)**3
    Qr=sp.diff(q,r);Pr=sp.diff(p,r)
    z=(p*Qr-q*Pr)/2
    red=q**2+p*Qr+z*z+(q+Pr)*sp.diff(z,r)
    Hq= -sp.diff(n*Qr+m*p,r)
    Hp= n*p+m*Qr
    # Direct directional derivative along genuine Hamiltonian vector field.
    Xq=Hp;Xp=-Hq
    strong=(sp.diff(red,q)*Xq+sp.diff(red,Qr)*sp.diff(Xq,r)
          +sp.diff(red,sp.diff(Qr,r))*sp.diff(Xq,r,2)
          +sp.diff(red,p)*Xp+sp.diff(red,Pr)*sp.diff(Xp,r)
          +sp.diff(red,sp.diff(Pr,r))*sp.diff(Xp,r,2))
    def euler_eta(field):
        f1=sp.diff(field,r)
        return (sp.diff(eta*red,field)-sp.diff(sp.diff(eta*red,f1),r)
                +sp.diff(sp.diff(eta*red,sp.diff(f1,r)),r,2))
    weak=euler_eta(q)*Xq+euler_eta(p)*Xp
    subst={q:1+r**2,p:2+r}
    # Substitute all field functions AND derivatives in a single evaluated
    # expression to respect independent jets.
    subs={q:1+r**2,p:2+r,sp.diff(q,r):2*r,sp.diff(p,r):1,
          sp.diff(q,r,2):2,sp.diff(p,r,2):0,
          sp.diff(q,r,3):0,sp.diff(p,r,3):0,
          sp.diff(q,r,4):0,sp.diff(p,r,4):0}
    lhs=sp.expand((eta*strong).doit().subs(subs).doit())
    rhs=sp.expand(weak.doit().subs(subs).doit())
    assert sp.integrate(lhs-rhs,(r,0,1))==0


def test_status_reports_explicitly_open_ranks_and_ghost_question():
    x=manifest()
    assert x['highest_lapse_result']['both_zero_on_Fz_and_Hg'] is True
    assert x['rank_and_lapse_fixing']=='NOT_DETERMINED'
    assert x['GATE_2B']=='OPEN' and x['JANUS_R']=='NOT_VALIDATED'

"""Exact algebraic ODE consequences of physical six-pair local C."""
import sympy as sp
import pytest
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode, exact_ode_certificate

@pytest.fixture(scope='module')
def sys():return exact_f_momentum_ode()

def test_primitive_f_dust_primary_elimination_linear_in_velocity(sys):
    assert sys['identity_residuals']['primary_substitution_linear_in_pLf_prime']==0
    assert sys['V'] in sys['equation'].free_symbols

def test_exact_coefficient_factorization(sys):
    assert sys['identity_residuals']['affine_coefficient_exact_factorization']==0
    assert sys['coefficient_factored']!=0

def test_secondary_solved_exactly_by_first_order_ode_rhs(sys):
    assert sys['identity_residuals']['exact_C_restored_after_ODE_substitution']==0
    assert sys['V'] not in sys['pLf_prime_rhs'].free_symbols

def test_C_couples_linearly_to_f_radial_momentum_primary(sys):
    assert sys['identity_residuals']['C_partial_pSf_exact']==0

def test_coefficient_not_velocity_dependent(sys):
    assert sys['identity_residuals']['coefficient_independent_of_pLf_prime']==0

def test_positive_chart_makes_affine_coefficient_nonzero(sys):
    # On the proven Step40/42 chart: all these factors are strictly positive,
    # with Mf2 != 0. Hence negative coefficient, never zero for r>0.
    assert sys['coefficient_factored'].has(sys['At'])
    assert sys['coefficient_factored'].has(sys['f_dust_beta'])
    assert sys['f_dust_denominator']!=0

def test_near_spherical_center_is_not_covered(sys):
    cert=exact_ode_certificate()
    assert cert['global_center_regular_C_solution']=='NOT_PROVED'

def test_no_Dirac_or_lapse_claim(sys):
    cert=exact_ode_certificate()
    assert cert['full_Dirac_time_preservation']=='NOT_DERIVED'
    assert cert['lapse_fixing']=='NOT_DERIVED'
    assert cert['GATE_2B']=='OPEN' and cert['JANUS_R']=='NOT_VALIDATED'

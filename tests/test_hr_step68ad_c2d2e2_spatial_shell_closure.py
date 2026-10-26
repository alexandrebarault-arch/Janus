"""Independent exact regression checks for the conditional Step68o shell."""
import sympy as sp
from numerics.hr_step68ad_c2d2e2_spatial_shell_closure import (
    curvature_geometry,original_primary_density_reduction,primary_shell_algebra,
    secondary_ode_composition,dust_clock_primitives,prolongation_logic,manifest,
    stationary_shift_shell,lapse_derivative_shell_composition)

def test_curvature_identity(): assert curvature_geometry()
def test_original_primary_reduction(): assert original_primary_density_reduction()
def test_g_primary_exact(): assert primary_shell_algebra()['Hg']
def test_f_primary_exact(): assert primary_shell_algebra()['Hf']
def test_Dg_exact(): assert primary_shell_algebra()['Fz_Dg']
def test_stationary_shift(): assert stationary_shift_shell()
def test_lapse_derivative_composition():
    assert lapse_derivative_shell_composition()['vanishing_lapse_derivative_coefficients']==4
def test_prolongations_are_essential():
    assert lapse_derivative_shell_composition()['requires_Hgprime_and_Fzprime']
def test_C_affine_ODE_exact(): assert secondary_ode_composition()['C_on_ODE']
def test_off_ODE_negative_control(): assert secondary_ode_composition()['off_ODE_residual']=='2*r*s*C1*epsilon'
def test_dust_clocks_global_primitives(): assert dust_clock_primitives()['clock_primitives']==2
def test_dust_jet_orders(): assert dust_clock_primitives()['jet_orders_verified']==3
def test_prolongations(): assert prolongation_logic()
def test_manifest_fail_closed():
    x=manifest()
    assert x['GATE_2B']=='OPEN' and x['JANUS_R']=='NOT_VALIDATED'
    assert x['Step58_continuum']=='INCOMPLETE'
    assert x['reproduces_original_modules_byte_for_byte'] is False

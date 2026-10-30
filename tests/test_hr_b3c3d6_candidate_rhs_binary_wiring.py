"""Isolated AST-extracted u_solution tests; no original Step58 import/execution.

The real candidate source is parsed (rather than imported), avoiding expensive
Step45/46/55/58 dependencies. A toy G(s,u)=2u+6su makes U'=3U, so
SciPy DOP853, binary64 RHS conversions and endpoint transport are exercised.
This is NOT a physical Step58 integration test or coefficient certificate.
"""
import ast
import math
import unittest
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import mpmath as mp
from scipy.integrate import solve_ivp
from numerics.hr_b3c3d6_exact_binary_rhs_transport import (
    exact_binary, transport_endpoint, decimal_square_target, exact_fraction_mp)

CANDIDATE=Path(__file__).resolve().parents[1]/'numerics'/'hr_b3c3d6_corrected_step58_point_probe_candidate.py'

def isolated_probe(radius_calls=None, transport_calls=None):
    """Extract exact u_solution function body from the current candidate file."""
    tree=ast.parse(CANDIDATE.read_text(encoding='utf-8'),filename=str(CANDIDATE))
    nodes=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='u_solution']
    assert len(nodes)==1
    F=lambda x:mp.mpf(str(x))
    def endpoint_s(radius):
        t=Decimal(str(radius))**2
        return float(t),t
    def endpoint_record(radius):
        sf,t=endpoint_s(radius)
        gap=Fraction.from_float(sf)-Fraction(t)
        return {'binary_gap':str(gap),'half_ulp':str(Fraction.from_float(math.ulp(sf))/2)}
    def eb(x):
        result=exact_binary(x)
        if radius_calls is not None: radius_calls.append((x,result))
        return result
    def transport(*args,**kwargs):
        got=transport_endpoint(*args,**kwargs)
        if transport_calls is not None:transport_calls.append(got)
        return got
    globals_={'Fraction':Fraction,'F':F,'mp':mp,'G':lambda s,u:2*u+6*s*u,
              'endpoint_s':endpoint_s,'endpoint_record':endpoint_record,
              'U0':mp.mpf('0.4'),'U1':mp.mpf('0'),'U2':mp.mpf('0'),
              'solve_ivp':solve_ivp,'exact_binary':eb,'transport_endpoint':transport}
    module=ast.Module(body=nodes,type_ignores=[])
    exec(compile(ast.fix_missing_locations(module),str(CANDIDATE),'exec'),globals_)
    return globals_['u_solution']

class CandidateBinaryWiringTests(unittest.TestCase):
    def test_candidate_source_compiles_ast_without_original_imports(self):
        self.assertTrue(callable(isolated_probe()))

    def test_four_radii_toy_ode_integrated_and_transported(self):
        with mp.workdps(70):
            for r in (0.25,0.5,0.7,0.85):
                with self.subTest(radius=r):
                    transport_calls=[]
                    u,g,sol=isolated_probe(transport_calls=transport_calls)(r)
                    target=mp.mpf(str(Decimal(str(r))**2))
                    exact=mp.mpf('0.4')*mp.exp(3*(target-exact_binary(1e-4)))
                    self.assertTrue(sol.success)
                    self.assertEqual(len(transport_calls),1)
                    self.assertLess(abs(u-exact),mp.mpf('1e-11'))
                    self.assertLess(abs(g-(2+6*target)*u),mp.mpf('1e-60'))

    def test_scipy_rhs_uses_binary64_exact_values(self):
        with mp.workdps(70):
            conversions=[]
            isolated_probe(radius_calls=conversions)(0.85)
            self.assertGreater(len(conversions),20)
            self.assertTrue(all(isinstance(x,float) and y==exact_fraction_mp(Fraction.from_float(x)) for x,y in conversions))
            self.assertTrue(any(y!=mp.mpf(str(x)) for x,y in conversions))

    def test_transport_delta_exact_and_zero_for_dyadic_radii(self):
        for r,sign in ((0.25,0),(0.5,0),(0.7,1),(0.85,-1)):
            calls=[]
            isolated_probe(transport_calls=calls)(r)
            self.assertEqual(len(calls),1)
            d=calls[0]['delta']
            self.assertEqual((d>0)-(d<0),sign)
            self.assertEqual(d,decimal_square_target(r)-Fraction.from_float(float(Decimal(str(r))**2)))

    def test_binary64_initial_state_conversion_invoked(self):
        calls=[]
        isolated_probe(radius_calls=calls)(0.25)
        self.assertTrue(any(x==1e-4 for x,y in calls))

if __name__=='__main__': unittest.main()

"""Exact toy regression for off-shell cubic Step55-to-Step58 jet transport.

Not an execution of original Step55/58 physical sources or a Dirac certificate.
"""
import unittest
import sympy as sp

r=sp.symbols('r', positive=True)
r0=sp.Rational(1,2)
s=r**2
s0=r0**2
uc=sp.expand(s**4-(s-s0)**4)
# Toy Step55 ODE: 2*s*U_s=G(s,U)-2*U, G=2*U+8*s**4.
g_ode=2*uc+8*s**4
pLf=s*uc
pLfr_ode=r*g_ode
pLfr_hol=sp.diff(pLf,r)
fac=(r+1)/10
Lf=1+r/3
beta=2+r/7
tfr=r/5
Sfr=3+r/4
denom=beta+fac*tfr


def jets(expr, n=3):
    return [sp.factor(sp.diff(expr,r,k).subs(r,r0)) for k in range(n+1)]


def lapse_dependent_fields(pLfr):
    # Exact partial dependence of physical_fields on pLfr; other terms cancel.
    pf=fac*Lf*pLfr/denom
    pSf=(Lf*pLfr-pf*tfr)/Sfr
    return pf,pSf


class HolonomicCubicTransport(unittest.TestCase):
    def test_cubic_matches_true_step55_solution_through_three_s_jets(self):
        for k in range(4):
            self.assertEqual(sp.diff(uc,r,k).subs(r,r0),
                             sp.diff(s**4,r,k).subs(r,r0))

    def test_ode_extension_agrees_only_through_second_radial_jet(self):
        delta=pLfr_ode-pLfr_hol
        self.assertEqual(jets(delta)[:3],[0,0,0])
        self.assertEqual(jets(delta)[3],sp.Rational(6))

    def test_third_jet_defect_formula(self):
        defect=jets(pLfr_ode-pLfr_hol)[3]
        self.assertEqual(defect,16*r0**6*24)

    def test_pf_and_pSf_third_jets_inherit_defect(self):
        delta=sp.factor(pLfr_ode-pLfr_hol)
        # Exact partial dependence of original physical_fields on pLfr.
        dpf=delta*fac*Lf/denom
        dpSf=delta*Lf*beta/(Sfr*denom)
        self.assertEqual(jets(dpf)[:3],[0,0,0])
        self.assertEqual(jets(dpSf)[:3],[0,0,0])
        self.assertEqual(jets(dpf)[3],sp.factor(6*fac*Lf/denom).subs(r,r0))
        self.assertEqual(jets(dpSf)[3],sp.factor(6*Lf*beta/(Sfr*denom)).subs(r,r0))

    def test_holonomic_cubic_derivative_is_consistent_at_all_r(self):
        ds=s-s0
        u_s_c=4*s0**3+12*s0**2*ds+12*s0*ds**2
        self.assertEqual(sp.expand(2*r*uc+2*r*s*u_s_c-pLfr_hol),0)

    def test_negative_control_ode_extension_not_holonomic_off_endpoint(self):
        self.assertNotEqual(sp.expand(pLfr_ode-pLfr_hol),0)
        self.assertNotEqual(sp.factor((pLfr_ode-pLfr_hol).subs(r,sp.Rational(3,4))),0)


if __name__=='__main__':unittest.main()

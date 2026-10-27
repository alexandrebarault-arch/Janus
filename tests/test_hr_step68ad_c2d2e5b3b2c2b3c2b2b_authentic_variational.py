"""Physical G derivatives: source-authenticated tests and invariant barrier."""
import unittest
from fractions import Fraction as F
from numerics import hr_step55_global_barrier as b
from numerics.hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational import (
    Dual, original_g_dual, certify, authenticate_sources, ORIGINAL_BLOBS)

class TestPhysicalVariation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certify(256)
    def test_original_four_git_blobs(self):
        self.assertEqual(authenticate_sources(),ORIGINAL_BLOBS)
    def test_original_compiler_primal_exact_match(self):
        s=b.I.c(F(3,10));u=b.stars(s)[0]
        self.assertEqual((original_g_dual(s,u).v.lo,original_g_dual(s,u).v.hi),
                         (b.G(s,u).lo,b.G(s,u).hi))
    def test_dual_polynomial_derivatives(self):
        x=Dual(F(3,2),u=2,p=3)
        z=(x*x+5*x+2)
        self.assertTrue(z.u.lo<=16*b.S<=z.u.hi)
        self.assertTrue(z.p.lo<=24*b.S<=z.p.hi)
    def test_dual_sqrt_derivatives(self):
        x=Dual(4,u=2,p=4).sqrt()
        self.assertTrue(x.v.lo<=2*b.S<=x.v.hi)
        self.assertTrue(x.u.lo<=b.S//2<=x.u.hi)
        self.assertTrue(x.p.lo<=b.S<=x.p.hi)
    def test_independent_symbolic_partial_derivatives(self):
        # Independent SymPy partials of the ORIGINAL Step55 normalized G,
        # evaluated on a rational radial point (not a finite-difference proof).
        import sympy as sp
        expr,_,U,_=b.normalized_symbolic()
        syms,_=b.compiled()
        ss=b.I.c(F(1,3));uu=b.stars(ss)[0]
        d=b.geometry(ss);d['s']=ss;d['U']=uu
        values=[d[str(x)] for x in syms]
        def evaluate(e):
            fn=sp.lambdify(syms,e,modules=[{'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
            return fn(*values)
        dual=original_g_dual(ss,uu)
        gu=evaluate(sp.diff(expr,U))
        self.assertLessEqual(dual.u.lo,gu.hi)
        self.assertGreaterEqual(dual.u.hi,gu.lo)
        x={str(t):t for t in expr.free_symbols}
        lg,sgr,gm,gp=d['Lg0'],d['Sgr0'],d['Gmom'],d['Gprime']
        dgm=1+F(5,2)*b.CG*ss
        dgp=2*(1+5*b.CG*ss)
        fac=gm/(2*b.MG*lg*sgr)
        dfac=dgm/(2*b.MG*lg*sgr)
        beta=(1+b.KG**2*ss).sqrt()+ss*fac*b.KG*lg
        dbeta=ss*dfac*b.KG*lg
        drho=-(gm*dgm/(2*b.MG*lg)-dfac*(ss*d['Dbar']+lg*gp)-fac*lg*dgp+d['Rhog']*dbeta)/beta
        dpsg=(lg*dgp-drho*ss*b.KG*lg)/sgr
        gp_ind=(evaluate(sp.diff(expr,x['Gmom']))*dgm
                +evaluate(sp.diff(expr,x['Gprime']))*dgp
                +evaluate(sp.diff(expr,x['Rhog']))*drho
                +evaluate(sp.diff(expr,x['Psg0']))*dpsg)
        self.assertLessEqual(dual.p.lo,gp_ind.hi)
        self.assertGreaterEqual(dual.p.hi,gp_ind.lo)
    def test_center_GU_exact_identity_enclosed(self):
        d=original_g_dual(b.I.c(0),b.U0)
        self.assertLessEqual(d.u.lo,-b.S)
        self.assertGreaterEqual(d.u.hi,-b.S)
    def test_center_GP_exact_identity_enclosed(self):
        d=original_g_dual(b.I.c(0),b.U0)
        v0=b.MF*b.B/b.A
        self.assertLessEqual(d.p.lo,3*v0.lo)
        self.assertGreaterEqual(d.p.hi,3*v0.hi)
    def test_center_v_inside_barrier(self):
        v0=b.MF*b.B/b.A
        self.assertGreater(v0.lo,b.I.c(F(681,100000)).hi)
        self.assertLess(v0.hi,b.I.c(F(689,100000)).lo)
    def test_physical_GU_strict_negative(self):
        self.assertLess(F(self.cert['GU'][1]),0)
        self.assertGreater(F(self.cert['GU'][0]),F(-11,10))
    def test_physical_GP_strict_positive(self):
        self.assertGreater(F(self.cert['GP'][0]),0)
        self.assertLess(F(self.cert['GP'][1]),F(3,100))
    def test_lower_barrier_strictly_inward(self):
        self.assertGreater(F(self.cert['lower_inward_min']),0)
    def test_upper_barrier_strictly_inward(self):
        self.assertLess(F(self.cert['upper_inward_max']),0)
    def test_variational_enclosure_R(self):
        self.assertEqual(self.cert['v_R_enclosure'],['681/100000','689/100000'])
    def test_512_cells_confirm(self):
        x=certify(512)
        self.assertGreater(F(x['lower_inward_min']),0)
        self.assertLess(F(x['upper_inward_max']),0)
    def test_too_narrow_barrier_rejected(self):
        with self.assertRaises(ArithmeticError):
            certify(256,lower=F('0.00682'),upper=F('0.00688'))
    def test_radius_guard(self):
        with self.assertRaises(ValueError):certify(256,radius=F(1,4000))
    def test_no_Dirac_claim(self):
        self.assertEqual(self.cert['GATE_2B'],'OPEN')
        self.assertEqual(self.cert['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()

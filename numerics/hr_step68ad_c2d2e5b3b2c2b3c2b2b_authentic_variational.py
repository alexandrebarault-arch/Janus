"""Original Step45/46/55 physical G: exact interval dual Jacobian and variational barrier.

The derivatives are evaluated by forward-mode automatic differentiation of
Step55's *original compiled symbolic* G; Pg is propagated through ALL g
momentum/dust reconstructions. No finite differences or synthetic G.
"""
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from . import hr_step55_global_barrier as b

ORIGINAL_BLOBS={
 'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
 'numerics/hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
 'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}

def authenticate_sources():
    root=Path(__file__).resolve().parents[1]
    for name, expected in ORIGINAL_BLOBS.items():
        data=(root/name).read_bytes()
        actual=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if actual!=expected:
            raise AssertionError(f'Original physical source altered: {name}: {actual}')
    return ORIGINAL_BLOBS.copy()

class Dual:
    __slots__ = ('v','u','p')
    def __init__(self, v, u=0, p=0):
        self.v=b.I.c(v); self.u=b.I.c(u); self.p=b.I.c(p)
    @staticmethod
    def c(x): return x if isinstance(x,Dual) else Dual(x)
    def __add__(self,o):
        o=Dual.c(o);return Dual(self.v+o.v,self.u+o.u,self.p+o.p)
    __radd__=__add__
    def __neg__(self): return Dual(-self.v,-self.u,-self.p)
    def __sub__(self,o): return self+-Dual.c(o)
    def __rsub__(self,o): return Dual.c(o)+-self
    def __mul__(self,o):
        o=Dual.c(o);return Dual(self.v*o.v,self.u*o.v+self.v*o.u,self.p*o.v+self.v*o.p)
    __rmul__=__mul__
    def inv(self):
        inv=self.v.inv();sq=inv*inv
        return Dual(inv,-self.u*sq,-self.p*sq)
    def __truediv__(self,o):return self*Dual.c(o).inv()
    def __rtruediv__(self,o):return Dual.c(o)*self.inv()
    def __pow__(self,k):
        if k==0:return Dual(1)
        if k==F(1,2) or k==0.5:return self.sqrt()
        if k==F(-1,2) or k==-0.5:return self.sqrt().inv()
        if int(k)!=k:raise ValueError('unsupported fractional exponent '+str(k))
        n=int(k)
        if n<0:return (self**(-n)).inv()
        return Dual(self.v**n,n*self.v**(n-1)*self.u,n*self.v**(n-1)*self.p)
    def sqrt(self):
        root=self.v.sqrt()
        return Dual(root,self.u/(2*root),self.p/(2*root))
    def __abs__(self):
        if self.v.lo>=0:return self
        if self.v.hi<=0:return -self
        raise ArithmeticError('nondifferentiable Abs interval')


def original_g_dual(s,u):
    d=b.geometry(s)
    lg,sgr,gm,gp=d['Lg0'],d['Sgr0'],d['Gmom'],d['Gprime']
    dgm=1+F(5,2)*b.CG*s
    dgp=2*(1+5*b.CG*s)
    fac=gm/(2*b.MG*lg*sgr)
    dfac=dgm/(2*b.MG*lg*sgr)
    beta=(1+b.KG**2*s).sqrt()+s*fac*b.KG*lg
    dbeta=s*dfac*b.KG*lg
    # The exact original numerator is recovered using rho_g=-numerator/beta.
    rho=d['Rhog']
    dnum=gm*dgm/(2*b.MG*lg)-dfac*(s*d['Dbar']+lg*gp)-fac*lg*dgp
    drho=-(dnum+rho*dbeta)/beta
    dpsg=(lg*dgp-drho*s*b.KG*lg)/sgr
    grads={'Gmom':dgm,'Gprime':dgp,'Rhog':drho,'Psg0':dpsg}
    d['s']=s;d['U']=u
    syms,fn=b.compiled()
    result=fn(*[Dual(d[str(x)],int(str(x)=='U'),grads.get(str(x),0)) for x in syms])
    return result


def certify(cells=256,radius=F(1,5000),lower=F(681,100000),upper=F(689,100000)):
    if cells<16:raise ValueError('at least 16 cells')
    if radius<0 or radius>F(1,5000):raise ValueError('unsupported parameter interval')
    blobs=authenticate_sources()
    old_pg,old_u0=b.PG,b.U0
    try:
        b.PG=old_pg+b.I.hull(-radius,radius)
        b.U0=b.MF*b.B*(b.PG/b.A-2*b.Z1)
        lo_gu=10**80;hi_gu=-10**80;lo_gp=10**80;hi_gp=-10**80
        lo_lower=10**80;hi_upper=-10**80
        d=b.I.c(F(1,10000))
        for i in range(cells):
            s=b.I.hull(F(289,400)*i/cells,F(289,400)*(i+1)/cells)
            star,_,_=b.stars(s)
            u=b.I(star.lo-d.hi,star.hi+d.hi)
            result=original_g_dual(s,u)
            A=result.u-2
            B=result.p
            flo=A*lower+B
            fhi=A*upper+B
            lo_gu=min(lo_gu,result.u.lo);hi_gu=max(hi_gu,result.u.hi)
            lo_gp=min(lo_gp,result.p.lo);hi_gp=max(hi_gp,result.p.hi)
            lo_lower=min(lo_lower,flo.lo);hi_upper=max(hi_upper,fhi.hi)
            if flo.lo<=0 or fhi.hi>=0:
                raise ArithmeticError(f'variational invariant barrier fails cell {i}: {flo}, {fhi}, GU {result.u}, GP {result.p}')
        def fr(x):return str(F(x,b.S))
        v0=b.MF*b.B/b.A
        if not (v0.lo>b.I.c(lower).hi and v0.hi<b.I.c(upper).lo):
            raise AssertionError('analytic central derivative outside invariant barrier')
        return dict(step='68ad-C2d2e5b3b2c2b3c2b2b',cells=cells,lambda_radius=str(radius),
                    original_physics_sha=blobs,
                    v0_enclosure=[fr(v0.lo),fr(v0.hi)],
                    v_barrier=[str(lower),str(upper)],v_R_enclosure=[str(lower),str(upper)],
                    GU=[fr(lo_gu),fr(hi_gu)],GP=[fr(lo_gp),fr(hi_gp)],
                    lower_inward_min=fr(lo_lower),upper_inward_max=fr(hi_upper),
                    status='PHYSICAL_G_VARIATIONAL_INVARIANT_BARRIER',
                    GATE_2B='OPEN',JANUS_R='NOT_VALIDATED',
                    caveats=['Requires Step49 analytic regular center and original b2 U-tube',
                             'Bounds v(R) but does not compute its exact value or f trace sensitivities',
                             'Does not certify physical boundary conditions or Dirac time preservation'])
    finally:
        b.PG,b.U0=old_pg,old_u0

if __name__=='__main__':
    import json
    print(json.dumps(certify(),indent=2))

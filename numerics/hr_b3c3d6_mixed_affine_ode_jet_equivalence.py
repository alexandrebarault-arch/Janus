"""Exact point-jet comparison of the *actual* historical Step58 affine probe.

The historical `fields_at` computes U_affine(s), but computes pLf_r as
r*G(s,U_affine), not as d[r^2 U_affine]/dr off the evaluation point.
Consequently its pLf_r first radial jet is ODE-consistent despite the
nonholonomic affine extension. This matters because Step58's six point
coefficients only use order 0/1 radial jets of U-dependent fields.

Formal algebraic result, not a numerical physical four-radius replay.
"""
import sympy as sp


def exact_jet_identities():
    r, r0, u0, u1, gs, gu = sp.symbols('r r0 u0 u1 gs gu', real=True, nonzero=True)
    s0 = r0**2
    s = r**2
    g0 = 2*u0 + 2*s0*u1
    u2 = (gs+(gu-4)*u1)/(2*s0)
    delta = s-s0
    ua = u0+u1*delta
    uq = ua+u2*delta**2/2
    # A linear Taylor model of G is enough for its 0/1 jets.
    g_affine = g0+gs*delta+gu*(ua-u0)
    plf_a, plf_q = s*ua, s*uq
    # Historical affine: pLf_r is imposed by the Step55 ODE *off point*.
    pLfr_mixed = r*g_affine
    pLfr_quad = sp.diff(plf_q,r)
    pLfr_holonomic_affine = sp.diff(plf_a,r)
    at = lambda expr: sp.factor(expr.subs(r,r0))
    result = {
        'pLf_value_mixed_minus_quad': at(plf_a-plf_q),
        'pLf_first_mixed_minus_quad': at(sp.diff(plf_a-plf_q,r)),
        'pLfr_value_mixed_minus_quad': at(pLfr_mixed-pLfr_quad),
        'pLfr_first_mixed_minus_quad': at(sp.diff(pLfr_mixed-pLfr_quad,r)),
        'pLfr_first_holonomic_affine_minus_quad': at(sp.diff(pLfr_holonomic_affine-pLfr_quad,r)),
        'pLfr_first_mixed_minus_holonomic_affine': at(sp.diff(pLfr_mixed-pLfr_holonomic_affine,r)),
        'pLf_second_holonomic_affine_minus_quad': at(sp.diff(plf_a-plf_q,r,2)),
        'pLf_second_mixed_minus_quad': at(sp.diff(plf_a-plf_q,r,2)),
        'u2':u2,
        'r0':r0,
        'u0':u0,
        'u1':u1,
        'gs':gs,
        'gu':gu,
        'pLf_mixed':plf_a,
        'pLf_quad':plf_q,
        'pLfr_mixed':pLfr_mixed,
        'pLfr_quad':pLfr_quad,
        'pLfr_holonomic_affine':pLfr_holonomic_affine,
        'r':r,
    }
    for k in ('pLf_value_mixed_minus_quad','pLf_first_mixed_minus_quad',
              'pLfr_value_mixed_minus_quad','pLfr_first_mixed_minus_quad'):
        assert result[k] == 0, (k,result[k])
    assert sp.factor(result['pLfr_first_holonomic_affine_minus_quad']+4*r0**4*u2)==0
    assert sp.factor(result['pLfr_first_mixed_minus_holonomic_affine']-4*r0**4*u2)==0
    return result


def smooth_field_jet_guard():
    """Check an explicit nonlinear rational smooth physical_fields-like map.

    Any C1 function H(r,pLf,pLfr) shares value and radial first derivative
    when its three inputs do; this example tests nontrivial denominators.
    """
    d=exact_jet_identities()
    r,r0=d['r'],d['r0']
    x1,y1=d['pLf_mixed'],d['pLfr_mixed']
    x2,y2=d['pLf_quad'],d['pLfr_quad']
    # A nontrivial surrogate for the algebraic pf and pSf maps, not the
    # physical parameters of Step55; denominator assumed nonzero.
    def fields(x,y):
        lf=1+r*r
        sfr=2+r*r
        tfr=r/(3+r*r)
        fac=x/(1+r*r)
        beta=1+r*r/4
        pf=-(x*x/(1+r*r)+fac*(lf*y-r*r)+r)/(beta+fac*tfr)
        psf=(-r*r+lf*y-pf*tfr)/sfr
        return pf,psf
    differences={}
    for label,(a,b) in zip(('pf','pSf'),zip(fields(x1,y1),fields(x2,y2))):
        # Substitution at r0 before simplification avoids huge expressions.
        for order in (0,1):
            va=sp.diff(a,r,order).subs(r,r0)
            vb=sp.diff(b,r,order).subs(r,r0)
            difference=sp.factor(sp.together(va-vb))
            differences[f'{label}_{order}']=difference
            assert difference==0,(label,order,difference)
    return differences


if __name__=='__main__':
    out=exact_jet_identities()
    print('mixed_affine_vs_quadratic_value_and_first_jets',
          [out[k] for k in ('pLf_value_mixed_minus_quad','pLf_first_mixed_minus_quad',
                             'pLfr_value_mixed_minus_quad','pLfr_first_mixed_minus_quad')])
    print('nonholonomic_second_jet_gap',out['pLfr_first_mixed_minus_holonomic_affine'])
    print('rational_field_jets',smooth_field_jet_guard())

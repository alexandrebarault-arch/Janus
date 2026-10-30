"""Reproduce the Step55 physical DOP853 candidate and exact rational error ledger.

The original Step45/46/55 symbolic/interval sources are SHA authenticated.
The DOP853 candidate uses the midpoint of the original outward interval G
at binary64 solver arguments. It need not be a validated integrator: the
independent interval residual certifies the reconstructed dense polynomial.
This certifies ONLY the Step55 spatial radial ODE, not Step58 or Dirac/4D.
"""
from decimal import Decimal
from fractions import Fraction as Q
from hashlib import sha1
from pathlib import Path
import sympy as sp
from scipy.integrate import solve_ivp
from .hr_step55_normalized_secondary import normalized_symbolic, check_original_source_blobs
from .hr_step55_global_barrier import (
    I, S, G, U0, U1, U2, geometry, stars, certify_global_barrier)
from .hr_b3c3d6_dop853_dense_rational_defect import (
    dense_exact_domain, dense_boundary_jump, dop853_dense_coefficients)
from .hr_b3c3d6_correlated_tube_guard import (
    physical_center_intervals, difference_enclosure,
    physical_step55_dense_defect_correlated)

ORIGINAL_SHA = {
    'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}


def authenticate_originals(root=None):
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    check_original_source_blobs(root)
    for name, expected in ORIGINAL_SHA.items():
        data=(root/name).read_bytes()
        actual=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if actual!=expected:
            raise ValueError(f'original SHA mismatch {name}: {actual}')
    return ORIGINAL_SHA.copy()


def gu_on_original_tube(cells=256):
    """Independent outward Step55 G_U enclosure, same Ustar +/- 1/10000."""
    expr,s,u,_=normalized_symbolic()
    derivative=sp.diff(expr,u)
    syms=sorted(derivative.free_symbols,key=str)
    fn=sp.lambdify(syms,derivative,
                   modules=[{'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
    lo,hi=10**100,-10**100
    delta=I.c(Q(1,10000))
    for j in range(cells):
        sI=I.hull(Q(289,400)*j/cells,Q(289,400)*(j+1)/cells)
        star=stars(sI)[0]
        uI=I(star.lo-delta.hi,star.hi+delta.hi)
        values=geometry(sI);values['s']=sI;values['U']=uI
        v=fn(*[values[str(x)] for x in syms])
        lo=min(lo,v.lo);hi=max(hi,v.hi)
    if hi>=0:
        raise ArithmeticError('G_U<=0 not certified on original tube')
    return Q(lo,S),Q(hi,S)


def midpoint(v):
    return float(Q(v.lo+v.hi,2*S))


def physical_rhs(s,y):
    v=G(I.c(s),I.c(float(y[0])))
    return [(midpoint(v)-2*float(y[0]))/(2*s)]


def run(subcells=256):
    authenticate_originals()
    barrier=certify_global_barrier(cells=256)
    gu_lo,gu_hi=gu_on_original_tube(cells=256)
    s0=float(1e-4)
    sR=float(Decimal('0.85')**2)
    initial=midpoint(stars(I.c(s0))[0])
    sol=solve_ivp(physical_rhs,(s0,sR),[initial],method='DOP853',
                  rtol=1e-12,atol=1e-15,dense_output=True)
    if not sol.success or sol.sol is None:
        raise ArithmeticError(f'physical DOP853 candidate failed: {sol.message}')
    ds=sol.sol.interpolants
    center=physical_center_intervals(U0,U1,U2,S)
    rows=[]
    E0=None
    for i,d in enumerate(ds):
        certificate=physical_step55_dense_defect_correlated(d,subcells)
        a,b,h,xmax=dense_exact_domain(d)
        if i==0:
            delta=difference_enclosure(dop853_dense_coefficients(d),a,h,0,0,center)
            if delta.lo < -Q(1,10000) or delta.hi > Q(1,10000):
                raise ArithmeticError('initial candidate outside Step55 barrier')
            E0=Q(1,10000)+max(abs(delta.lo),abs(delta.hi))
        jump=dense_boundary_jump(d,ds[i+1]) if i+1<len(ds) else Q(0)
        rows.append((a,b,certificate['bound'],jump))
    if not rows or rows[0][0]!=Q.from_float(s0) or rows[-1][1]!=Q.from_float(sR):
        raise ArithmeticError('true binary64 domain mismatch')
    if any(rows[i][1]!=rows[i+1][0] for i in range(len(rows)-1)):
        raise ArithmeticError('discontinuous domains')
    integrated=sum((r[2]*(r[1]-r[0])/2 for r in rows),Q(0))
    jumps=sum((r[1]*abs(r[3]) for r in rows[:-1]),Q(0))
    terminal=(rows[0][0]*E0+integrated+jumps)/rows[-1][1]
    return {
        'original_sha':ORIGINAL_SHA,'step55_barrier_cells':barrier['cells'],
        'gu_interval_exact':[str(gu_lo),str(gu_hi)],
        'gu_upper_float':float(gu_hi),'DOP853_success':bool(sol.success),
        'DOP853_steps':len(rows),'DOP853_nfev':int(sol.nfev),
        'correlated_subcells_per_step':subcells,
        'total_correlated_cells':len(rows)*subcells,
        'initial_E0_exact':str(E0),
        'initial_contribution_float':float(rows[0][0]*E0/rows[-1][1]),
        'continuous_defect_contribution_float':float(integrated/rows[-1][1]),
        'jump_contribution_float':float(jumps/rows[-1][1]),
        'terminal_error_bound_exact':str(terminal),
        'terminal_error_bound_float':float(terminal),
        'nonzero_dense_jumps':sum(r[3]!=0 for r in rows[:-1]),
        'max_dense_jump_float':float(max(abs(r[3]) for r in rows)),
        'max_continuous_defect_float':float(max(r[2] for r in rows)),
        'scope':'CERTIFIED_STEP55_SPATIAL_ODE_ERROR_RELATIVE_TO_EXACT_REGULAR_CENTER_BRANCH',
        'Step58_A_B_E':'NOT_CERTIFIED','positive_lapse_BVP':'NOT_CERTIFIED',
        'Dirac_4D_stability_observables':'NOT_CERTIFIED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(run(),indent=2))

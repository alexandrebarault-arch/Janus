"""Step 38 independent audit: exact radial J/K sign and PB Richardson limit.

Reads numerical data already RECORDED by Step37; it does NOT rerun the
full original non-IBP Hamiltonian or establish vanishing Dirac constraints.
The interval positivity proof is exact rational arithmetic conditional on
specified terminating-decimal metric parameters at the Step37 witness.
"""
from __future__ import annotations
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path
import json

A = F('0.4')
Y = F('0.5787707228025044')
B = A * Y
CG = F('0.0015')
CF = F('-0.0012')
M2 = F('23.3348939346')
MG2 = F('1')
BETA1 = F('1')
BETA2 = F('-4.2383993109')
BETA3 = F('13.6801214252')
RMAX = F('0.85')


def J(y: F) -> F:
    return BETA1 + 2*BETA2*y + BETA3*y*y


def eta_at_s(s: F) -> F:
    """Exact S_f/S_g=y*((1+c_f*s)/(1+c_g*s))^2 for s=r^2."""
    if not F(0) <= s <= RMAX*RMAX:
        raise ValueError('outside certified radial interval')
    ug, uf = 1+CG*s, 1+CF*s
    if ug<=0 or uf<=0:raise ValueError('metric conformal factor singular')
    return Y*(uf/ug)**2


def K_over_r2_at_s(s: F) -> F:
    """Actual exact algebraic HR shift coefficient divided by r^2."""
    ug,uf=1+CG*s,1+CF*s
    lg=A*ug*ug
    lf=B*uf*uf
    return M2*MG2*lg**3*lf*J(eta_at_s(s))


def continuous_sign_certificate() -> dict:
    """Prove J(Sf/Sg)>0 and K(r)/r²>0 continuously, by monotonicity.

    For s in [0,R²], (uf/ug)'=(CF-CG)/(1+CG*s)^2 <0.
    J'(eta)=2*(BETA2+BETA3*eta)>0 throughout if positive at min eta.
    All conformal factors positive. Therefore J>=J(eta_min) and
    K/r² >= M2*MG2*A³*B*uf(R²)^2*J(eta_min) >0.
    Both inequalities are exact Fractions, not a grid scan.
    """
    s=RMAX*RMAX
    assert CG>0 and CF<0 and 1+CF*s>0
    assert CF-CG<0
    eta_min=eta_at_s(s)
    eta_max=eta_at_s(F(0))
    assert eta_min<eta_max
    assert BETA2+BETA3*eta_min>0
    jmin=J(eta_min)
    assert jmin>F('0.6')
    jmax=J(eta_max)
    assert jmax>jmin
    kbar_min=M2*MG2*A**3*B*(1+CF*s)**2*jmin
    assert kbar_min>0
    assert K_over_r2_at_s(F(0))>=kbar_min
    assert K_over_r2_at_s(s)>=kbar_min
    return {
        'interval_r': ['0',str(RMAX)],
        'eta_exact_lower':str(eta_min),'eta_exact_upper':str(eta_max),
        'J_exact_lower':str(jmin), 'K_over_r2_exact_lower':str(kbar_min),
        'eta_lower_decimal':float(eta_min),'J_lower_decimal':float(jmin),
        'K_over_r2_lower_decimal':float(kbar_min),
        'formal_origin_K':'K(r)=r^2 * positive coefficient; K(0)=0 is a spherical coordinate factor',
        'proof':'monotone eta(s), monotone J(eta), positive conformal factors',
        'status':'PROVED_FOR_FIXED_STEP37_SPATIAL_METRIC_PARAMETERS_ONLY',
    }


def read_step37_report(root: Path | None = None) -> list[dict]:
    path=(root or Path(__file__).resolve().parents[1])/'research/reports/gate2b-step37-report.json'
    raw=json.loads(path.read_text(encoding='utf-8'))
    assert raw['step']=='37' and raw['final_verdict']['GATE_2B']=='OPEN'
    return raw['independent_nonibp_discrete_bracket']


def richardson(records: list[dict], *, channel='after') -> dict:
    """Two-level Richardson assuming B(h)=B0+c2*h²+c4*h⁴+O(h⁶).

    No guaranteed error bound or proof B0=0 from only four finite values.
    Each input n must satisfy n_next-1=2*(n_prev-1).
    """
    if channel not in ('after','before'): raise ValueError('unknown bracket channel')
    n=[int(x['n']) for x in records]
    if len(n)<4 or any(n[i+1]-1!=2*(n[i]-1) for i in range(len(n)-1)):
        raise ValueError('four dyadically nested grids required')
    with localcontext() as ctx:
        ctx.prec=50
        b=[Decimal(str(x[channel])) for x in records]
        first=[(4*b[i+1]-b[i])/3 for i in range(len(b)-1)]
        second=[(16*first[i+1]-first[i])/15 for i in range(len(first)-1)]
        delta_ratio=[float((b[i]-b[i+1])/(b[i+1]-b[i+2])) for i in range(len(b)-2)]
        return {'n':n,'original':[str(v) for v in b],
                'first_Oh2':[str(v) for v in first],
                'second_Oh4':[str(v) for v in second],
                'last_estimate':str(second[-1]),
                'last_estimate_float':float(second[-1]),
                'difference_two_second_estimates':str(second[-1]-second[-2]),
                'successive_difference_ratios':delta_ratio,
                'assumption':'even-power smooth grid convergence; not independently established',
                'rigorous_bound':False}


def gate_manifest(root:Path|None=None)->dict:
    rows=read_step37_report(root)
    corrected=richardson(rows,channel='after')
    baseline=richardson(rows,channel='before')
    estimate=Decimal(corrected['last_estimate'])
    assert estimate>0
    assert Decimal(baseline['last_estimate'])>0
    assert estimate<Decimal('1e-8')
    # An extrapolated small POSITIVE bracket is evidence against silently
    # declaring the Step37 N=641 small negative sample literally zero.
    return {'step':'38','date':'2026-10-20',
            'radial_certificate':continuous_sign_certificate(),
            'original_step37_nodal_PB':{'corrected':corrected,'uncorrected':baseline},
            'caveat':'Extrapolated B0 is model-dependent, not proof that continuum Poisson bracket is strictly nonzero; no full clean Step37 provider reproduction in this audit',
            'continuous_C_local_zero':'NOT_PROVED',
            'Dirac_secondary_preservation':'NOT_DERIVED','lapse_fixing':'NOT_DERIVED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    print(json.dumps(gate_manifest(),indent=2))

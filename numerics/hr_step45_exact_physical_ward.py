"""Exact six-canonical-pair Ward and radial C identities from original HR ADM.

Uses the same ORIGINAL post-IBP Fg=N*A+N'*B, Ff=M*C+M'*D
as numerics.hr_curved_primary_mixed_kernel._compiled, but derives functional
Euler jets SYMBOLICALLY (no complex-step in r, no finite differences).

Assumptions: spherical radial chart, positive EH kinetic signs for both
metrics, two canonical moving-dust sources, algebraic relative shift z(r)
held external in the FIRST variation, compact lapse smearings. The Ward
identities hold off the lapse-primary surface as W=z*H_g/L_f; on H_g=0
W=0 exactly. The shift elimination requires F_z=0. This proves neither
secondary C=0 nor its time preservation/Dirac rank.
"""
from functools import lru_cache
import sympy as sp


@lru_cache(maxsize=1)
def exact_physical_ward():
    Q=('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')
    q=sp.symbols(' '.join(Q))
    dq=sp.symbols(' '.join(name+'r' for name in Q))
    ddq=sp.symbols(' '.join(name+'rr' for name in Q))
    names=dict(zip(Q,q))
    dnames=dict(zip(Q,dq))
    Lg,plg,Sg,psg,tg,pg,Lf,plf,Sf,psf,tf,pf=q
    Lgr,plgr,Sgr,psgr,tgr,pgr,Lfr,plfr,Sfr,psfr,tfr,pfr=dq
    z,zr,zrr=sp.symbols('z zr zrr')
    mg,mf,m2=sp.symbols('Mg2 Mf2 m2',nonzero=True)
    b0,b1,b2,b3,b4=sp.symbols('beta0:5')
    root=sp.sqrt(1-z*z)
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    Wg=m2*mg*(Lg*A0+Lf*At*root)
    Wf=m2*mg*(Lf*Af+Lg*At*root)
    dg0=psg*Sgr+pg*tgr
    kg=Lg*plg**2/(4*mg*Sg**2)-plg*psg/(2*mg*Sg)
    kf=Lf*plf**2/(4*mf*Sf**2)-plf*psf/(2*mf*Sf)
    dustg=pg*sp.sqrt(1+tgr*tgr/Lg**2)
    dustf=pf*sp.sqrt(1+tfr*tfr/Lf**2)
    # EXACT match to original numerics/hr_curved_primary_mixed_kernel.py
    Ag=kg+dustg-mg*Lg-mg*Sgr**2/Lg+Wg+z*dg0/Lg+zr*plg
    Bg=-2*mg*Sg*Sgr/Lg+z*plg
    Af_full=kf+dustf-mf*Lf-mf*Sfr**2/Lf+Wf+z*dg0/Lf
    Af_full+=plg*(zr*Lg/Lf+z*Lgr/Lf-z*Lg*Lfr/Lf**2)
    Bf=-2*mf*Sf*Sfr/Lf+z*Lg*plg/Lf

    def derivative(expr):
        # Total radial derivative treating z, z' and EACH of the 12 fields,
        # their first and second jets as independent symbolic coordinates.
        return (sum(sp.diff(expr,u)*v for u,v in zip(q,dq))
                +sum(sp.diff(expr,u)*v for u,v in zip(dq,ddq))
                +sp.diff(expr,z)*zr+sp.diff(expr,zr)*zrr)

    def euler(A,B):
        e0=[sp.diff(A,u)-derivative(sp.diff(A,v)) for u,v in zip(q,dq)]
        e1=[sp.diff(B,u)-sp.diff(A,v)-derivative(sp.diff(B,v))
            for u,v in zip(q,dq)]
        e2=[-sp.diff(B,v) for v in dq]
        return (e0,e1,e2)

    eg=euler(Ag,Bg);ef=euler(Af_full,Bf)
    def bracket(g,f):
        return sum(g[k]*f[k+1]-g[k+1]*f[k] for k in range(0,12,2))
    K={(i,j):bracket(eg[i],ef[j]) for i in range(3) for j in range(3)}
    # K00 and K01 are still explicit small expressions in field jets.
    # Evaluating C does NOT require h-step finite differentiation.
    Hg=sp.cancel(Ag-derivative(Bg))
    Hf=sp.cancel(Af_full-derivative(Bf))
    interaction=m2*mg*Lg*Lf*At
    Dg=psg*Sgr-Lg*plgr+pg*tgr
    Fz=Dg-interaction*z/root
    K20_expected=2*mg*Sg*Sgr*z/(Lg*Lf)
    W=K[0,1]-K[1,0]+derivative(K[2,0])
    C_exact=sp.cancel(sp.together(K[0,0]-derivative(K[0,1])))
    residuals={
        'high_02':sp.cancel(K[0,2]),
        'high_12':sp.cancel(K[1,2]),
        'high_21':sp.cancel(K[2,1]),
        'high_22':sp.cancel(K[2,2]),
        'K20_value':sp.cancel(K[2,0]-K20_expected),
        'K11_equal_K20':sp.cancel(K[1,1]-K[2,0]),
        'W_equals_zHg_over_Lf':sp.cancel(sp.together(W-z*Hg/Lf)),
        'shift_g_stationarity':sp.cancel(sp.together(sp.diff(Hg,z)-Fz/Lg)),
        'shift_f_stationarity':sp.cancel(sp.together(sp.diff(Hf,z)-Fz/Lf)),
    }
    return {'Q':Q,'q':q,'dq':dq,'ddq':ddq,'parameters':(mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr),
            'densities':{'Ag':Ag,'Bg':Bg,'Af':Af_full,'Bf':Bf},
            'eg':eg,'ef':ef,'K':K,'Hg':Hg,'Hf':Hf,'Fz':Fz,
            'K20_expected':K20_expected,'W':W,'C_exact':C_exact,
            'residuals':residuals, 'total_derivative':derivative}


def exact_certificate_summary():
    result=exact_physical_ward()
    fail={name:str(value) for name,value in result['residuals'].items() if value!=0}
    if fail:raise AssertionError(f'original Hamiltonian Ward identity failure: {fail}')
    # Off-shell radial C may be NONZERO! Prove no erroneous equation C=0.
    if result['C_exact']==0:
        raise AssertionError('C unexpectedly forced to zero off shell')
    all_second=set(result['ddq'])
    if result['C_exact'].free_symbols & all_second:
        raise AssertionError('Analytic C contains unresolved second canonical jets')
    return {'step':45,'exact_symbolic_residuals_all_zero':True,
            'six_canonical_pairs':6,'full_smearing_kernel_shape':[3,3],
            'high_smearing_K02_K12_K21_K22':'identically zero off shell',
            'K20_and_K11':'2*Mg2*Sg*Sg_r*z/(Lg*Lf) identically off shell',
            'W':'z*Hg/Lf exactly; thus W=0 on Hg=0',
            'shift_stationarity':'dHg/dz=Fz/Lg; dHf/dz=Fz/Lf (at fixed canonical variables)',
            'C':'exact K00-(K01) total radial derivative, nonzero off shell, no second spatial field jets',
            'scope':'symbolic original spherical positive-EH HR+two moving dust canonical action, fixed z in first variation, compact lapses',
            'secondary_exact_zero':'NOT_PROVED',
            'secondary_time_preservation':'NOT_COMPUTED',
            'lapse_fixing':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(exact_certificate_summary(),indent=2))

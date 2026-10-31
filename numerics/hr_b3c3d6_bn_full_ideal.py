"""Exact first-jet ideal reduction of Step58 B_N; provenance supplied by caller.

Uses the high-jet factor theorem and eliminates pLg_r by Fz=0 and Sg_rr
by Hg=0. A zero remainder is a universal algebraic identity on this chart,
not a physical Step55 enclosure or a positive-lapse BVP.
"""
import sympy as sp


def certify(ward, op):
    q=dict(zip(ward['Q'],ward['q']))
    dq=dict(zip(ward['Q'],ward['dq']))
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=ward['parameters']
    Lg,Lf,Sg,Sf=(q[k] for k in ('Lg','Lf','Sg','Sf'))
    Lgr,Sgr,tgr=(dq[k] for k in ('Lg','Sg','tg'))
    h=sp.sqrt(1-z*z)
    Fz,Hg=op['Fz'],ward['Hg']
    R=op['operator']['N'][1]-z*op['C']/Lg+(1-z*z)/(Lg*Lf)*op['Dt'](Hg)
    if R.has(op['zrr']) or R.has(op['zrrr']):
        raise AssertionError('uncontrolled high shift jet')
    # Import inside function to support the package used by original Step45/58.
    try:
        from numerics.hr_b3c3d6_bn_high_jet_elimination import verify_high_jet_elimination
    except ModuleNotFoundError:
        from hr_b3c3d6_bn_high_jet_elimination import verify_high_jet_elimination
    high=verify_high_jet_elimination(ward,op)
    if high['coefficient_identities_proved']!=4:
        raise AssertionError('missing high-jet factor')
    pstar=(q['pSg']*Sgr+q['pg']*tgr-op['K']*z/h)/Lg
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    kg=Lg*q['pLg']**2/(4*mg*Sg*Sg)-q['pLg']*q['pSg']/(2*mg*Sg)
    dust=q['pg']*sp.sqrt(1+tgr*tgr/Lg**2)
    sgrr=op['qpp'][2]
    rstar=Lg/(2*mg*Sg)*(-kg-dust+mg*Lg-mg*Sgr**2/Lg
          +2*mg*Sg*Sgr*Lgr/Lg**2-m2*mg*(Lg*A0+Lf*At/h))
    if sp.cancel(Fz.subs(dq['pLg'],pstar))!=0:
        raise AssertionError('Fz elimination invalid')
    if sp.cancel(Hg.subs({dq['pLg']:pstar,sgrr:rstar}))!=0:
        raise AssertionError('Hg elimination invalid')
    # Other canonical high jets are free: their coefficients are Fz multiples.
    highjets=(*op['qpp'],*op['qppp'],*op['q4'])
    sub={x:sp.S.Zero for x in highjets if x!=sgrr}
    sub.update({dq['pLg']:pstar,sgrr:rstar})
    remainder=sp.cancel(sp.together(R.subs(sub)))
    if remainder!=0:
        raise AssertionError(('first-jet ideal remainder',remainder))
    return {'four_high_jet_factors':'EXACT', 'shift_zrr_zrrr':'ABSENT',
            'Fz_and_Hg_elimination':'EXACT', 'first_jet_remainder':'ZERO',
            'identity':'Fz=Hg=0 => B_N=z*C/Lg-(1-z^2)*D_r(Hg)/(Lg*Lf)',
            'corollary':'Fz=Hg=Hg_r=C=0 => B_N=0',
            'originals_executed':'CALLER_MUST_VERIFY',
            'physical_six_A_B_E_enclosures':'NOT_CERTIFIED',
            'two_boundary_positive_BVP':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

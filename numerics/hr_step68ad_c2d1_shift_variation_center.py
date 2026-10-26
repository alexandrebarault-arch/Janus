"""JANUS 68ad-C2d1: exact Step45/58 shift-response center regularity.

Rebuild only the original Step45 Hamiltonian Euler kernels used by Step58,
with all six canonical pairs, both dusts, and the unfrozen relative shift.
This is an INDEPENDENT symbolic derivation, not execution of the original
Step58 Cdot or Step60 quotient.  The SHA-pinned sources must be checked in a
complete checkout before calling it a source-integrated reproduction.

The theorem is conditional on smooth even canonical profiles, odd S/pS/z,
regular even lapses, positive K/r^2, and the stationary shift Fz=0.
No temporal constraint signs or Dirac rank are established here.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
from hashlib import sha1
import sympy as sp

SOURCE_PINS = {
    'hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
    'hr_step60_full_constraint_prolongation.py': '9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509',
}
FIELDS = ('Lg pLg Sg pSg tg pg Lf pLf Sf pSf tf pf').split()
RELEVANT = (0, 1, 2, 3, 4, 5, 6, 8)  # all variables D or K depend on


def authenticate_originals(folder):
    folder = Path(folder)
    for filename, expected in SOURCE_PINS.items():
        raw = (folder / filename).read_bytes()
        actual = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if actual != expected:
            raise ValueError(f'Physical source drift: {filename}: {actual}')
    return SOURCE_PINS.copy()


@lru_cache(maxsize=1)
def physical_variations():
    """Return complete δD,δK coefficients for N,M and lapse jets 0..3.

    q,q' and q'' are independent symbols, as in authentic Step45/58.
    The original Euler kernels are reconstructed from the original A,B
    densities.  No shift variation is frozen; Z_D and Z_K are applied later.
    """
    q = sp.symbols(' '.join(FIELDS))
    qp = sp.symbols(' '.join(n+'r' for n in FIELDS))
    qpp = sp.symbols(' '.join(n+'rr' for n in FIELDS))
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr = sp.symbols(
        'mg mf m2 b0 b1 b2 b3 b4 z zr zrr')
    Lg,plg,Sg,psg,tg,pg,Lf,plf,Sf,psf,tf,pf = q
    Lgr,plgr,Sgr,psgr,tgr,pgr,Lfr,plfr,Sfr,psfr,tfr,pfr = qp
    root = sp.sqrt(1-z*z)
    At = b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    A0 = b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    Af = b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    Wg = m2*mg*(Lg*A0+Lf*At*root)
    Wf = m2*mg*(Lf*Af+Lg*At*root)
    dg0 = psg*Sgr+pg*tgr
    kg = Lg*plg**2/(4*mg*Sg**2)-plg*psg/(2*mg*Sg)
    kf = Lf*plf**2/(4*mf*Sf**2)-plf*psf/(2*mf*Sf)
    dustg = pg*sp.sqrt(1+tgr*tgr/Lg**2)
    dustf = pf*sp.sqrt(1+tfr*tfr/Lf**2)
    Ag = kg+dustg-mg*Lg-mg*Sgr**2/Lg+Wg+z*dg0/Lg+zr*plg
    Bg = -2*mg*Sg*Sgr/Lg+z*plg
    Am = (kf+dustf-mf*Lf-mf*Sfr**2/Lf+Wf+z*dg0/Lf
          +plg*(zr*Lg/Lf+z*Lgr/Lf-z*Lg*Lfr/Lf**2))
    Bm = -2*mf*Sf*Sfr/Lf+z*Lg*plg/Lf

    def Dt(expr):
        expr = sp.sympify(expr)
        return (sum((sp.diff(expr,u)*v for u,v in zip(q,qp) if expr.has(u)),sp.S.Zero)
                +sum((sp.diff(expr,u)*v for u,v in zip(qp,qpp) if expr.has(u)),sp.S.Zero)
                +sp.diff(expr,z)*zr+sp.diff(expr,zr)*zrr)

    def euler(A,B,i):
        return (sp.diff(A,q[i])-Dt(sp.diff(A,qp[i])),
                sp.diff(B,q[i])-sp.diff(A,qp[i])-Dt(sp.diff(B,qp[i])),
                -sp.diff(B,qp[i]))

    D = psg*Sgr-Lg*plgr+pg*tgr
    K = m2*mg*Lg*Lf*At
    Dq = [sp.diff(D,u) for u in q]
    Dqp = [sp.diff(D,u) for u in qp]
    Kq = [sp.diff(K,u) for u in q]
    out = {}
    for sector,(A,B) in {'N':(Ag,Bg),'M':(Am,Bm)}.items():
        X = {}
        for i in RELEVANT:
            j = i+1 if i%2==0 else i-1
            sign = 1 if i%2==0 else -1
            X[i] = tuple(sign*e for e in euler(A,B,j))
        rowsD,rowsK = {},{}
        for j in range(4):
            dD=dK=sp.S.Zero
            for i in RELEVANT:
                xj = X[i][j] if j<3 else sp.S.Zero
                xprev = X[i][j-1] if 0<j<=3 else sp.S.Zero
                dD += Dq[i]*xj+Dqp[i]*(Dt(xj)+xprev)
                dK += Kq[i]*xj
            rowsD[j],rowsK[j]=dD,dK
        out[sector]={'D':rowsD,'K':rowsK}
    return {'q':q,'qp':qp,'qpp':qpp,
            'parameters':(mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr),
            'D':D,'K':K,'delta':out}


@lru_cache(maxsize=1)
def center_certificate():
    """Formal leading jets for arbitrary analytic profiles to needed order.

    A,B>0; r>=0; Sg=r*Lg, Sf=r*Lf, z=r*Z. The coefficients
    a1,b1c,g1,p1,... are independent, not chosen to fit a sample.
    """
    v=physical_variations()
    r=sp.symbols('r',positive=True)
    A,B,G,P,U,V,KG,KF,Z,Rg,Rf,MG,MF,M2=sp.symbols(
        'A B G P U V KG KF Z Rg Rf MG MF M2',nonzero=True)
    b0,b1,b2,b3,b4=sp.symbols('b0v b1v b2v b3v b4v')
    a1,b1c,g1,p1,u1,v1,rg1,rf1=sp.symbols('a1 b1c g1 p1 u1 v1 rg1 rf1')
    lg=A*(1+a1*r*r);lf=B*(1+b1c*r*r)
    fields={'Lg':lg,'pLg':r*r*(G+g1*r*r),'Sg':r*lg,
            'pSg':r*(P+p1*r*r),'tg':KG*(A*r*r/2+A*a1*r**4/4),
            'pg':r*r*(Rg+rg1*r*r),'Lf':lf,'pLf':r*r*(U+u1*r*r),
            'Sf':r*lf,'pSf':r*(V+v1*r*r),
            'tf':KF*(B*r*r/2+B*b1c*r**4/4),'pf':r*r*(Rf+rf1*r*r)}
    mg,mf,m2,beta0,beta1,beta2,beta3,beta4,z,zr,zrr=v['parameters']
    sub={mg:MG,mf:MF,m2:M2,beta0:b0,beta1:b1,beta2:b2,beta3:b3,beta4:b4,
         z:Z*r,zr:Z,zrr:0}
    for i,name in enumerate(FIELDS):
        f=fields[name]
        sub[v['q'][i]]=f
        sub[v['qp'][i]]=sp.diff(f,r)
        sub[v['qpp'][i]]=sp.diff(f,r,2)
    result={}
    for sector in ('N','M'):
        d=v['delta'][sector]
        D0=sp.factor(sp.limit(d['D'][0].subs(sub)/r,r,0))
        D1=sp.factor(sp.limit(d['D'][1].subs(sub)/r**2,r,0))
        K0=sp.factor(sp.limit(d['K'][0].subs(sub)/r**2,r,0))
        K1=sp.factor(sp.limit(d['K'][1].subs(sub)/r**3,r,0))
        D0_on_shell=sp.factor(sp.limit(d['D'][0].subs(sub).subs(P,2*G)/r**3,r,0))
        result[sector]={'D0_over_r':D0,'D1_over_r2':D1,
                        'K0_over_r2':K0,'K1_over_r3':K1,
                        'D0_on_shell_over_r3':D0_on_shell}
    expectedN=Z*(P-2*G)
    expectedM=3*A*Z*(P-2*G)/B
    assert sp.factor(result['N']['D0_over_r']-expectedN)==0
    assert sp.factor(result['M']['D0_over_r']-expectedM)==0
    for sector in ('N','M'):
        for x in result[sector].values():
            assert x.is_finite is not False and not x.has(sp.oo,-sp.oo,sp.zoo,sp.nan)
    # Stationary Fz=0 implies D=O(r^3), while K*z/sqrt(1-z²)=O(r³).
    # D/r at center = A(P-2G), hence P=2G on the positive-K chart.
    return {'center_coefficients':result,
            'stationarity_center_equation':A*(P-2*G),
            'on_stationary_shift':{sector:sp.factor(result[sector]['D0_over_r'].subs(P,2*G))
                                    for sector in ('N','M')},
            'symbols':{'A':A,'B':B,'G':G,'P':P,'Z':Z}}


def theorem():
    v=physical_variations()
    high={}
    for sector in ('N','M'):
        for j in (2,3):
            for var in ('D','K'):
                residual=sp.factor(v['delta'][sector][var][j])
                if residual!=0:
                    raise AssertionError(f'Unexpected higher lapse jet: {sector}/{var}/{j}: {residual}')
                high[f'{sector}_{var}_{j}']='EXACT_ZERO_OFF_SHELL'
    c=center_certificate()
    assert all(x==0 for x in c['on_stationary_shift'].values())
    return {'step':'68ad-C2d1','scope':'ORIGINAL_STEP45_58_SHIFT_RESPONSE_CENTER_REGULARITY',
            'higher_lapse_coefficients':high,
            'center_D0_leading_N':str(c['center_coefficients']['N']['D0_over_r']),
            'center_D0_leading_M':str(c['center_coefficients']['M']['D0_over_r']),
            'Fz_implies':'P=2*G, where pSg=r*P+O(r^3), pLg=r^2*G+O(r^4)',
            'stationary_shift_deltaD':'O(r^3) for even N,M; first-lapse coefficient O(r^2)',
            'stationary_shift_deltaK':'O(r^2) for even N,M; first-lapse coefficient O(r^3)',
            'stationary_shift_deltaZ':'O(r) for smooth even N,M and K/r^2>0; no raw 1/K divergence',
            'Step58_Cdot_7_cell_signs':'NOT_EVALUATED',
            'Step60_quotient':'NOT_EVALUATED',
            'Dirac_rank':'OPEN','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(theorem(),indent=2))

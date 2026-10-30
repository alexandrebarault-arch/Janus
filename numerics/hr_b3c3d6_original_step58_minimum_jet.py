"""Exact Step58 dependency audit using byte-authentic Step45/58.

On the prescribed Step55 family only pLf,pSf,pf depend on U or U_s.
This does NOT execute the physical four-radius Step58 probe or certify a BVP.
"""
from hashlib import sha1
from pathlib import Path
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator

SOURCES = {'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
           'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f'}
FIELDS = ('pLf','pSf','pf')


def source_guard():
    for name,expected in SOURCES.items():
        data=(Path(__file__).parent/name).read_bytes()
        got=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert got==expected,(name,got,expected)
    return SOURCES.copy()


def certify():
    source_guard()
    p=exact_physical_ward();o=physical_operator()
    deps={}
    for label in ('N','M'):
        for j in (0,1,2):
            expr=o['operator'][label][j]
            used=expr.free_symbols
            assert not used.intersection(o['q4'])
            deps[f'{label}{j}']={name:[k for k,vec in enumerate((o['q'],o['qp'],o['qpp'],o['qppp']))
                                      if vec[p['Q'].index(name)] in used] for name in FIELDS}
    assert max(max(v,default=-1) for d in deps.values() for v in d.values())==1
    assert deps['M0']=={'pLf':[0,1],'pSf':[0,1],'pf':[0]}
    assert all(1 not in d['pSf'] for key,d in deps.items() if key!='M0')
    # The operator is not globally first-order in canonical radial jets:
    assert o['qppp'][p['Q'].index('Sg')] in o['operator']['N'][0].free_symbols
    assert o['qppp'][p['Q'].index('pLg')] in o['operator']['M'][0].free_symbols
    return deps


def sensitivity():
    """On Fz=0, exact dA_M/dU_ss for the prescribed Step55 field map."""
    p=exact_physical_ward();o=physical_operator()
    q=dict(zip(p['Q'],p['q']));qp=dict(zip(p['Q'],o['qp']))
    Lg,Lf,Sf=q['Lg'],q['Lf'],q['Sf']
    z,K,D=o['z'],o['K'],o['Dg'];mf=p['parameters'][1]
    slope=sp.diff(o['operator']['M'][0],qp['pSf'])
    assert sp.diff(slope,qp['pSf'])==0
    assert sp.factor(slope-z*(1-z*z)*o['Czr']/(2*Lf*mf*Sf))==0
    assert sp.factor(o['Czr']+(K*sp.sqrt(1-z*z)+z*D)/(Lg*Lf))==0
    solved=(q['pSg']*qp['Sg']+q['pg']*qp['tg']-K*z/sp.sqrt(1-z*z))/Lg
    shell=-z*sp.sqrt(1-z*z)*K/(2*Lg*Lf**2*mf*Sf)
    assert sp.factor(slope.subs(qp['pLg'],solved)-shell)==0
    r,U,Us=sp.symbols('r U Us')
    fac,beta,tfr,Sfr=sp.symbols('fac beta tfr Sfr')
    kinetic,curvature,Wf=sp.symbols('kinetic curvature Wf')
    den=beta+fac*tfr
    plfr=2*r*U+2*r**3*Us
    pf=-(kinetic-fac*(-D+Lf*plfr)+curvature+z*D/Lf+Wf)/den
    psf=(-D+Lf*plfr-pf*tfr)/Sfr
    assert sp.factor(sp.diff(psf,Us)-2*r**3*Lf*beta/(Sfr*den))==0
    # dU_s/dr=2r U_ss, and only pSf_r in A_M contains U_ss.
    result=sp.factor(shell*4*r**4*Lf*beta/(Sfr*den))
    expected=-2*r**4*z*sp.sqrt(1-z*z)*K*beta/(Lg*Lf*mf*Sf*Sfr*den)
    assert sp.factor(result-expected)==0
    return result

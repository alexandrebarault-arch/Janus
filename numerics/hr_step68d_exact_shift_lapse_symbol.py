"""Step68d: exact physical Step45/57/58 six-pair shift response and lapse cancellation.

Scope: K>0 and Fz=0; Hg=0 for N'' cancellation. Center limit uses
Hg/r² and K/r² finite, not full time preservation or Dirac rank.
"""
from functools import lru_cache
from hashlib import sha1, sha256
from pathlib import Path
import json
import sympy as sp
from .hr_step57_secondary_principal_symbol import authenticated_step45
from .hr_step58_temporal_operator import physical_operator, highest_lapse_certificate

BLOBS={
 'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'hr_step57_secondary_principal_symbol.py':'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f',
 'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f'}


def authenticate(root=None):
    root=Path(root) if root else Path(__file__).resolve().parent
    for name,expected in BLOBS.items():
        raw=(root/name).read_bytes()
        got=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if got!=expected:raise ValueError('Original Git source mismatch: '+name)
    return BLOBS.copy()


@lru_cache(1)
def physical_center_bridge():
    authenticate()
    p=authenticated_step45();o=physical_operator();h=highest_lapse_certificate()
    names=dict(zip(p['Q'],p['q']))
    Lg,Lf=names['Lg'],names['Lf'];z=o['z'];t=1-z*z
    rt=sp.sqrt(t);K=o['K']
    shell={p['dq'][p['Q'].index('pLg')]:h['shift_elimination_pLg_prime']}
    H=p['Hg'].subs(shell)
    # These are the N' and M' coefficients in delta_H(z), not in Cdot.
    n=rt**3*H/K-t/Lg;m=t/Lf
    assert sp.factor(sp.cancel(o['delta_shift']['N'][1].subs(shell)-n))==0
    assert sp.factor(sp.cancel(o['delta_shift']['M'][1].subs(shell)-m))==0
    assert all(2 not in o['delta_shift'][x] for x in ('N','M'))
    czr=-K/(Lg*Lf*rt)
    assert sp.factor(sp.cancel(o['Czr'].subs(shell)-czr))==0
    dn=-K*rt/(Lg**2*Lf);dm=K*rt/(Lg*Lf**2)
    assert sp.factor(sp.cancel(o['direct_parts']['N'][2].subs(shell)-dn))==0
    assert sp.factor(sp.cancel(o['direct_parts']['M'][2].subs(shell)-dm))==0
    sn=czr*n;sm=czr*m
    fn=sp.factor(sp.cancel(dn+sn));fm=sp.factor(sp.cancel(dm+sm))
    assert sp.factor(fn+t*H/(Lg*Lf))==0 and fm==0
    assert sp.factor(sp.cancel(o['operator']['N'][2].subs(shell)-fn))==0
    assert sp.factor(sp.cancel(o['operator']['M'][2].subs(shell)-fm))==0
    assert dm!=0 and sm!=0 and dn!=0 and sn!=0
    # Center h0=Hg/r²,k0=K/r². Treat Hg independently, not by
    # substituting inside its expanded canonical expression.
    r,a,b,h0,k0,w=sp.symbols('r a b h0 k0 w',positive=True)
    center_n=sp.limit(((1-r*r*w*w)**sp.Rational(3,2)*r*r*h0/(r*r*k0)
                       -(1-r*r*w*w)/a),r,0)
    center_m=sp.limit((1-r*r*w*w)/b,r,0)
    assert sp.simplify(center_n-(h0/k0-1/a))==0
    assert sp.simplify(center_m-1/b)==0
    return {'Nprime_shift':n,'Mprime_shift':m,
            'C_zprime_on_Fz':czr,
            'second_lapse_direct':{'N':dn,'M':dm},
            'second_lapse_from_shift':{'N':sn,'M':sm},
            'second_lapse_full':{'N':fn,'M':fm},
            'H_g_on_shift_stationarity':H,
            'center_Nprime_shift_limit':center_n,
            'center_Mprime_shift_limit':center_m,
            'center_N2_on_Hg':2*center_n.subs(h0,0),
            'center_M2_on_Hg':2*center_m}


def manifest():
    v=physical_center_bridge()
    digest=sha256(sp.srepr(v['H_g_on_shift_stationarity']).encode()).hexdigest()
    return {'step':'68d','source_sha':authenticate(),
        'delta_z_Nprime_on_Fz':'(1-z²)^(3/2)*Hg_on_Fz/K-(1-z²)/Lg',
        'delta_z_Mprime_on_Fz':'(1-z²)/Lf',
        'C_zprime_on_Fz':'-K/(Lg*Lf*sqrt(1-z²))',
        'direct_Nsecond':'-K*sqrt(1-z²)/(Lg²*Lf)',
        'direct_Msecond':'+K*sqrt(1-z²)/(Lg*Lf²)',
        'shift_Nsecond':'-(1-z²)*Hg_on_Fz/(Lg*Lf)+K*sqrt(1-z²)/(Lg²*Lf)',
        'shift_Msecond':'-K*sqrt(1-z²)/(Lg*Lf²)',
        'combined_Nsecond':'-(1-z²)*Hg_on_Fz/(Lg*Lf)',
        'combined_Msecond':'0',
        'Hg_shell_srepr_sha256':digest,
        'center_Nprime_limit':str(v['center_Nprime_shift_limit']),
        'center_Mprime_limit':str(v['center_Mprime_shift_limit']),
        'center_N2_on_Hg0':str(v['center_N2_on_Hg']),
        'center_M2_on_Hg0':str(v['center_M2_on_Hg']),
        'original_step45_57_58_executed_together':True,
        'original_step55_profile_executed':False,
        'lower_lapse_coefficients_reduced':False,
        'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN',
        'JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(manifest(),indent=2))

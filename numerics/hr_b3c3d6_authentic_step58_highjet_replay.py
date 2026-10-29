"""Replay byte-original Step45+Step58 high-lapse-jet shell identity.
NOT a Step55 six-coefficient probe or global lapse/Dirac solution.
Requires original Step45/57/58 files in the real repository; a minimal
Step57 import shim was used ONLY in the isolated 2026-10-29 execution.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from .hr_step58_temporal_operator import highest_lapse_certificate, physical_operator

EXPECTED = {
    'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
}

def source_hashes():
    out={}
    for filename, expected in EXPECTED.items():
        raw=Path(__file__).with_name(filename).read_bytes()
        digest=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if digest!=expected: raise AssertionError((filename,digest,expected))
        out[filename]=digest
    return out

def outer_geometry_factor():
    # EXACT rational constants transcribed from Step55.geometry; this
    # does NOT execute the Step55 radial ODE or its physical boundary data.
    r=F(17,20);s=r*r
    A=F(2,5); Y=F('0.5787707228025044');B=A*Y
    Lg=A*(1+F('0.0015')*s)**2
    Lf=B*(1-F('0.0012')*s)**2
    z=F('0.004')*r
    factor=-(1-z*z)/(Lg*Lf)
    assert Lg>0 and Lf>0 and 0<z<1 and factor<0
    return factor

def replay():
    blobs=source_hashes()
    original=physical_operator()
    high=highest_lapse_certificate()
    assert set(original['operator'])=={'N','M'}
    assert set(original['operator']['N'])=={0,1,2}
    assert set(original['operator']['M'])=={0,1,2}
    assert high['M2_on_Fz_shell']==0
    assert high['N2_and_M2_vanish_on_Fz_and_Hg'] is True
    Lg,Lf,z=sp.symbols('Lg Lf z')
    expected=(z*z-1)/(Lg*Lf)
    assert sp.simplify(high['N2_to_Hg_factor']-expected)==0
    outer=outer_geometry_factor()
    assert F(-11,1)<outer<F(-10,1) # coarse exact enclosure
    return {'scope':'AUTHENTIC_STEP45_STEP58_HIGH_LAPSE_JETS_ONLY',
            'source_blobs':blobs,'Step57_import':'minimal_shim_in_isolated_run_not_original_Step57',
            'original_Step58_executed':True,
            'original_Step55_executed':False,
            'original_Step58_full_six_coefficients_on_Step55_executed':False,
            'highest_jet_identity':'E_M=0 on Fz=0; E_N=-(1-z^2)*Hg/(Lg*Lf) on Fz=0',
            'outer_geometric_factor_r17_20':str(outer),
            'outer_geometric_factor_sign':'-11 < factor < -10',
            'lapse_BVP':'NOT_TESTED','Dirac':'NOT_TESTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__': print(json.dumps(replay(),indent=2))

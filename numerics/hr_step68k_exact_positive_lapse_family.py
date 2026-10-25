"""Step68k: exact flat-spatial homothetic constrained family and positive local lapse.

Two positive-energy Einstein-Hilbert sectors and two comoving positive-dust
profiles; *not* the nonhomothetic Step55 solution. A fully symbolic original
Step45/58 evaluation proves the sign theorem at EVERY r>0 of this family.
This is an exact radial constraint/time-secondary local illustration, NOT a
4D solution, global boundary-value theorem, degree-of-freedom count, or proof
of absence of a BD ghost.
"""
from functools import lru_cache
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator
from .hr_step68f_physical_pointwise import verified_sources

@lru_cache(1)
def exact_family():
    pins=verified_sources()
    p=exact_physical_ward();o=physical_operator()
    r=sp.symbols('r',positive=True)
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=p['parameters']
    T=b1+2*b2+b3
    rho_g=-(b0+3*b1+3*b2+b3)
    rho_f=-(b1+3*b2+3*b3+b4)
    # Fixed gravitational scales Mg²=Mf²=m²=1. All beta_i symbolic.
    profile={'Lg':sp.S.One,'Lf':sp.S.One,'Sg':r,'Sf':r,
             'pLg':sp.S.Zero,'pLf':sp.S.Zero,
             'pSg':sp.S.Zero,'pSf':sp.S.Zero,
             'tg':sp.S.Zero,'tf':sp.S.Zero,
             'pg':rho_g*r*r,'pf':rho_f*r*r}
    sub={mg:sp.S.One,mf:sp.S.One,m2:sp.S.One,
         z:sp.S.Zero,zr:sp.S.Zero,zrr:sp.S.Zero,o['zrrr']:sp.S.Zero}
    for i,name in enumerate(p['Q']):
        e=profile[name]
        for order,jet in enumerate((p['q'][i],p['dq'][i],p['ddq'][i],o['qppp'][i],o['q4'][i])):
            sub[jet]=sp.diff(e,r,order)
    Dg=o['Dg']
    q=dict(zip(p['Q'],p['q']));qp=dict(zip(p['Q'],p['dq']))
    Df=q['pSf']*qp['Sf']-q['Lf']*qp['pLf']+q['pf']*qp['tf']
    constraints={'Fz':p['Fz'],'Hg':p['Hg'],'Hf':p['Hf'],
                 'C':p['C_exact'],'Dg':Dg,'Df':Df}
    residuals={key:sp.factor(sp.cancel(e.subs(sub))) for key,e in constraints.items()}
    for key,e in constraints.items():
        residuals[key+'prime']=sp.factor(sp.cancel(o['Dt'](e).subs(sub)))
    if any(value!=0 for value in residuals.values()):
        raise AssertionError('Flat family violates a physical radial primary or first prolongation: '+str(residuals))
    if sp.factor(o['K'].subs(sub)-r*r*T)!=0:
        raise AssertionError('Incorrect original K sign or scaling')
    coefficients={(sector,j):sp.factor(sp.cancel(o['operator'][sector][j].subs(sub)))
                  for sector in ('N','M') for j in (0,1,2)}
    expected_N=sp.Rational(3,2)*r*r*T*(rho_g+2*T)
    expected_M=-sp.Rational(3,2)*r*r*T*(rho_f+2*T)
    if sp.factor(coefficients['N',0]-expected_N)!=0:
        raise AssertionError('Incorrect N local lapse coefficient')
    if sp.factor(coefficients['M',0]-expected_M)!=0:
        raise AssertionError('Incorrect M local lapse coefficient')
    if any(coefficients[sec,j]!=0 for sec in ('N','M') for j in (1,2)):
        raise AssertionError('Unexpected derivative-lapse terms')
    # Sign theorem given r>0, T>0, rho_g>0, rho_f>0:
    # A_N>0, A_M<0 and ratio=-A_N/A_M=(rho_g+2T)/(rho_f+2T)>0.
    return {'r':r,'T':T,'rho_g':rho_g,'rho_f':rho_f,
            'sub':sub,'profile':profile,'constraints':residuals,
            'coefficients':coefficients,'expected_N':expected_N,'expected_M':expected_M,
            'ratio':(rho_g+2*T)/(rho_f+2*T),'original_pins':pins,
            'parameter_symbols':(b0,b1,b2,b3,b4)}


def rational_witness():
    a=exact_family();b0,b1,b2,b3,b4=a['parameter_symbols']
    point={b0:-5,b1:1,b2:0,b3:0,b4:-5}
    params={name:sp.factor(a[name].subs(point)) for name in ('T','rho_g','rho_f','ratio')}
    assert params=={'T':1,'rho_g':2,'rho_f':4,'ratio':sp.Rational(2,3)}
    assert a['expected_N'].subs(point)==6*a['r']**2
    assert a['expected_M'].subs(point)==-9*a['r']**2
    assert sp.factor((3*a['expected_N']+2*a['expected_M']).subs(point))==0
    return {'parameters':{str(k):str(v) for k,v in point.items()},
            'T':'1','rho_g':'2','rho_f':'4','ratio':'2/3',
            'lapses':'N=3, M=2 positive, spatial constraint time-bracket zero',
            'A_N':'6*r**2','A_M':'-9*r**2'}


def manifest():
    a=exact_family();w=rational_witness()
    return {'step':'68k','source':'Eight authentic original 45/46/55/57/58/59/60 SHA-verified; original Step45/58 algebra',
            'original_pins':a['original_pins'],
            'profile':'Lg=Lf=1,Sg=Sf=r, gravitational canonical momenta zero, z=0, dust spatial phases constant; pg=r²*rho_g,pf=r²*rho_f',
            'canonical_positive_action':'Mg2=Mf2=m2=1',
            'parameters':{'T':str(a['T']),'rho_g':str(a['rho_g']),'rho_f':str(a['rho_f'])},
            'sufficient_positive_domain':'r>0, T>0, rho_g>0, rho_f>0',
            'all_primary_secondary_and_first_radial_residuals':{key:str(val) for key,val in a['constraints'].items()},
            'K_original':'r²*T >0 for r>0',
            'AN':'3*r²*T*(rho_g+2*T)/2 >0 on domain',
            'AM':'-3*r²*T*(rho_f+2*T)/2 <0 on domain',
            'BN_BM_second_lapse':'all exactly zero on this family',
            'positive_lapse_ratio':'(rho_g+2*T)/(rho_f+2*T) >0',
            'center_normalized_AN_AM':'AN/r², AM/r² finite and strictly nonzero; ratio extends positively to r=0',
            'rational_witness':w,
            'not_claimed':['NOT Step55 nonhomothetic branch','NOT globally evolved 4D solution','NOT conditions at spacetime boundaries','NOT general Dirac rank','NOT independent non-IBP oracle','NOT ghost freedom'],
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

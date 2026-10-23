"""Exact elimination and Frechet response of HR relative shift, Step56.

Source: original spherical six-pair Step45 Fz=Dg-K*z/sqrt(1-z*z).
This computes a necessary CHAIN-RULE component of temporal Dirac analysis;
NOT the complete {C,Htotal}, lapse ratio or constraint rank.
"""
from functools import lru_cache
from fractions import Fraction
import sympy as sp

STEP45_SHA='66aa43841dccfe4a5d586a49be9c10af3a67a10e'
STEP46_SHA='bac025c28dbe1561c0c36c56dbfda46dc326f804'

@lru_cache(None)
def physics():
 D,K,z=sp.symbols('D K z',real=True)
 R=sp.sqrt(D**2+K**2);Z=D/R
 ZD=K**2/R**3;ZK=-D*K/R**3
 assert sp.simplify(sp.diff(Z,D)-ZD)==0
 assert sp.simplify(sp.diff(Z,K)-ZK)==0
 assert sp.simplify(D-K*(D/R)/(K/R))==0  # K>0, positive sqrt branch
 Lg,Lf,Sg,Sf,pSg,pg,pLgr,Sgr,tgr,m2,mg,b1,b2,b3=sp.symbols(
  'Lg Lf Sg Sf pSg pg pLgr Sgr tgr m2 Mg2 beta1 beta2 beta3',real=True)
 At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
 Dg=pSg*Sgr-Lg*pLgr+pg*tgr
 Kphys=m2*mg*Lg*Lf*At
 names=('Lg','Lf','Sg','Sf','pSg','pg','pLgr','Sgr','tgr')
 fields=(Lg,Lf,Sg,Sf,pSg,pg,pLgr,Sgr,tgr)
 variation=sp.symbols('dLg dLf dSg dSf dpSg dpg dpLgr dSgr dtgr')
 dd=sp.expand(sum(sp.diff(Dg,f)*w for f,w in zip(fields,variation)))
 dk=sp.expand(sum(sp.diff(Kphys,f)*w for f,w in zip(fields,variation)))
 assert dd==sp.expand(Sgr*variation[4]+pSg*variation[7]-pLgr*variation[0]-Lg*variation[6]+tgr*variation[5]+pg*variation[8])
 assert sp.expand(dk-m2*mg*(Lf*At*variation[0]+Lg*At*variation[1]+
  2*Lg*Lf*((b1*Sg+b2*Sf)*variation[2]+(b2*Sg+b3*Sf)*variation[3])))==0
 N,M=sp.symbols('N M',real=True)
 Fz=D-K*z/sp.sqrt(1-z*z)
 Hz=(N/Lg+M/Lf)*(D*z+K*sp.sqrt(1-z*z))
 assert sp.simplify(sp.diff(Hz,z)-(N/Lg+M/Lf)*Fz)==0
 return dict(D=D,K=K,z=z,Z=Z,ZD=ZD,ZK=ZK,Dg=Dg,Kphys=Kphys,At=At,
   fields=dict(zip(names,fields)),variations=dict(zip(names,variation)),
   dD=dd,dK=dk,dZ=ZD*dd+ZK*dk,Fz=Fz,Hz=Hz)

def jet_commutation():
 x=physics();D,K=x['D'],x['K']
 Dr,Kr,eD,eK,eDr,eKr=sp.symbols('Dr Kr eD eK eDr eKr',real=True)
 Z=x['Z'];Zr=sp.diff(Z,D)*Dr+sp.diff(Z,K)*Kr
 delta_z=sp.diff(Z,D)*eD+sp.diff(Z,K)*eK
 delta_zr=sum(sp.diff(Zr,x)*y for x,y in ((D,eD),(K,eK),(Dr,eDr),(Kr,eKr)))
 radial_delta=sum(sp.diff(delta_z,x)*y for x,y in ((D,Dr),(K,Kr),(eD,eDr),(eK,eKr)))
 assert sp.simplify(delta_zr-radial_delta)==0
 return dict(Zr=Zr,dZr=delta_zr,commutator=sp.simplify(delta_zr-radial_delta))

def center_response():
 s,d,k,c=sp.symbols('s d k c',positive=True)
 w=d/sp.sqrt(k*k+s*d*d)
 d0=k*c/sp.sqrt(1-c*c*s)
 # Assumes k>0 and 1-c²s>0, certified on Step55 branch.
 T=sp.symbols('T',positive=True)
 subst={d:k*c/sp.sqrt(T),s:(1-T)/c**2}
 w0=sp.simplify(w.subs(subst)).subs(T,1-s*c*c)
 wd=sp.simplify(sp.diff(w,d).subs(subst)).subs(T,1-s*c*c)
 wk=sp.simplify(sp.diff(w,k).subs(subst)).subs(T,1-s*c*c)
 assert sp.simplify(w0-c)==0
 assert sp.simplify(wd-(1-s*c*c)**sp.Rational(3,2)/k)==0
 assert sp.simplify(wk+c*(1-s*c*c)/k)==0
 kmin=Fraction('0.229');z1=Fraction('0.004')
 assert 1/kmin<Fraction('4.367')
 assert z1/kmin<Fraction('0.0175')
 return dict(w=w,d0=d0,w0=w0,wd=wd,wk=wk,
   normalized_d_sensitivity_bound=1/kmin,
   normalized_k_sensitivity_bound=z1/kmin)

def stationarity_time_preservation():
 """Exact d_t Fz=0 solves for z_t, independently of the lapse equations."""
 x=physics();D,K=x['D'],x['K']
 Dt,Kt,zt=sp.symbols('Dt Kt zt',real=True)
 R=sp.sqrt(D*D+K*K)
 # Positive K branch: z=D/R and sqrt(1-z²)=K/R.
 F_t=Dt-(D/K)*Kt-(R**3/K**2)*zt
 solved=sp.solve(F_t,zt)[0]
 predicted=x['ZD']*Dt+x['ZK']*Kt
 assert sp.simplify(solved-predicted)==0
 return dict(Fz_t_on_shift_shell=F_t,z_t=solved,
             positive_K_chart=True,temporal_dirac_C_not_computed=True)


def smeared_momentum_kernel():
 """Exact Euler derivative induced by -Lg*Z_D*delta(pLg') with compact tests.

 For W[eta]=integral eta(r) z(r) dr, the pLg contribution obeys
 delta W=integral (-eta Lg Z_D) delta(pLg') dr, hence
 delta W/delta pLg = +(eta Lg Z_D)' and boundary -[eta Lg Z_D delta pLg].
 """
 r=sp.symbols('r',real=True)
 eta,Lg,zd,plgr=(sp.Function(n)(r) for n in ('eta','Lg','ZD','pLgr'))
 density=-eta*Lg*zd*plgr
 euler=-sp.diff(sp.diff(density,plgr),r)
 expected=sp.diff(eta*Lg*zd,r)
 assert sp.simplify(euler-expected)==0
 return dict(Euler=euler,boundary_coefficient=-eta*Lg*zd,
             nonzero_smearing_derivative=sp.diff(euler,sp.diff(eta,r))==Lg*zd)

def six_pair_toy():
 q=sp.symbols('q0:6',real=True);p=sp.symbols('p0:6',real=True)
 D=p[0]+2*p[1];K=2+q[0]**2;Z=D/sp.sqrt(D*D+K*K)
 ext_z=sp.Symbol('z');C=q[0]*ext_z+q[2]*p[3]
 H=p[0]+p[2]
 def bracket(f,g):
  return sp.expand(sum(sp.diff(f,a)*sp.diff(g,b)-sp.diff(f,b)*sp.diff(g,a) for a,b in zip(q,p)))
 actual=sp.simplify(bracket(C.subs(ext_z,Z),H))
 frozen=bracket(C,H).subs(ext_z,Z)
 correction=sp.simplify(actual-frozen)
 assert correction!=0
 assert sp.simplify(correction-sp.diff(C,ext_z)*bracket(Z,H))==0
 return dict(actual=actual,frozen=frozen,correction=correction)

def manifest():
 x=physics();r=jet_commutation();c=center_response();t=six_pair_toy();shift_time=stationarity_time_preservation();smear=smeared_momentum_kernel()
 return {
 'step':56,'sources':{'Step45':STEP45_SHA,'Step46':STEP46_SHA},
 'Dg':'pSg*Sgr-Lg*pLgr+pg*tgr',
 'K':'m² Mg2 Lg Lf (beta1*Sg²+2beta2*Sg*Sf+beta3*Sf²)',
 'Fz':'Dg-K*z/sqrt(1-z²)',
 'z_on_positive_K':'Dg/sqrt(Dg²+K²)',
 'delta_z':'[K² delta_Dg-Dg*K delta_K]/(Dg²+K²)^(3/2)',
 'delta_Dg':str(x['dD']), 'delta_K':str(x['dK']),
 'variation_commutes_with_spatial_derivative':r['commutator']==0,
 'smeared_pLg_frechet_kernel':'delta integral eta*z /delta pLg = +partial_r(eta*Lg*Z_D), for compact eta; boundary -[eta*Lg*Z_D*delta pLg]',
 'smeared_kernel_contains_lapse_test_derivative':smear['nonzero_smearing_derivative'],
 'shift_stationarity_t_dot':'dot_z = K²/(D²+K²)^(3/2)*dot_D - D*K/(D²+K²)^(3/2)*dot_K',
 'shift_stationarity_t_exactly_preserved':shift_time['positive_K_chart'],
 'envelope_stationarity':'delta Hred at Fz=0 uses fixed-z Hamiltonian variation, but delta Cred includes implicit delta z and delta zprime',
 'center_w':'w=z/r=d/sqrt(k²+s*d²) when Dg=r³*d and K=r²*k',
 'center_normalized_d_sensitivity_lt':str(c['normalized_d_sensitivity_bound']),
 'center_normalized_k_sensitivity_abs_lt':str(c['normalized_k_sensitivity_bound']),
 'six_canonical_pair_toy_frozen_z_omits_nonzero_term':t['correction']!=0,
 'full_temporal_Dirac_bracket':'NOT_COMPUTED',
 'lapse_fixing':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
if __name__=='__main__':
 import json
 print(json.dumps(manifest(),indent=2))

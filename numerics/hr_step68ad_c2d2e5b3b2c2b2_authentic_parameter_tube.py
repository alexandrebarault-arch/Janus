"""Authenticated Step45/46/55 G: uniform Pg parameter tube, spatial only.

Runs the original Git-blob-authenticated physical symbolic normalization and
Step55 outward-integer interval barrier. The perturbation changes Pg in ALL
Step55 g reconstructions and U0(Pg); U1/U2 remain a comparison function, not
claimed Taylor coefficients of the perturbed solution. Also reconstructs
rho_f=p_f/r**2 using the ORIGINAL Step46 f primary.

Does NOT establish physical outer boundary conditions, temporal Dirac rank,
lapse preservation, 4D stability or cosmological observables.
"""
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
from numerics import hr_step55_global_barrier as b

S_MAX = F(289,400)
ORIGINAL_BLOBS = {
 'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
 'numerics/hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
 'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}

def authenticate_sources():
 root=Path(__file__).resolve().parents[1]
 for path,expected in ORIGINAL_BLOBS.items():
  data=(root/path).read_bytes()
  actual=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
  if actual!=expected:
   raise AssertionError(f'original source mismatch: {path}: {actual} != {expected}')
 return dict(ORIGINAL_BLOBS)

def f_density_normalized(s,u,v,d):
 """Original Step46 pf formula after pLf=sU, pLf'=rV, pf=s*rho_f."""
 lf,sfr,db,wfb,rf=d['Lf0'],d['Sfr0'],d['Dbar'],d['Wfbar'],d['Rf']
 beta=(1+b.KF**2*s).sqrt()
 den=beta+b.KF*s*u/(2*b.MF*sfr)
 numer=(u**2/(4*b.MF*lf)-u/(2*b.MF*sfr)*(v-s*db/lf)
        -b.MF*lf**3*rf/2+s*b.Z1*db/lf+wfb)
 return -numer/den,den

def certificate(cells=256, radius='0.0002'):
 if not isinstance(cells,int) or not 64<=cells<=8192:
  raise ValueError('cells outside Step55 certified chart')
 rad=F(radius)
 if rad<0 or rad>F(1,5000):
  raise ValueError('radius outside independently tested proof chart [0,1/5000]')
 blobs=authenticate_sources()
 old_pg,old_u0=b.PG,b.U0
 try:
  # Single outward interval for ALL lambda in [-rad,+rad]; no point sampling.
  b.PG=old_pg+b.I.hull(-rad,rad)
  b.U0=b.MF*b.B*(b.PG/b.A-2*b.Z1)
  # This reexecutes the original Step55 barrier, now on the parameter interval.
  barrier=b.certify_global_barrier(cells=cells)
  rho_f_lo=10**80;rho_f_hi=-10**80;den_lo=10**80
  rho_g_lo=10**80;rho_g_hi=-10**80;beta_g_lo=10**80
  u_lo=10**80;u_hi=-10**80;t_lo=10**80
  for i in range(cells):
   s=b.I.hull(S_MAX*i/cells,S_MAX*(i+1)/cells)
   d=b.geometry(s)
   us,_,_=b.stars(s)
   delta=b.I.c(F(1,10000))
   u=b.I(us.lo-delta.hi,us.hi+delta.hi)
   v=b.G(s,u)
   rho_f,den=f_density_normalized(s,u,v,d)
   rho_g=d['Rhog']
   lg,sgr,g=d['Lg0'],d['Sgr0'],d['Gmom']
   beta_g=(1+b.KG**2*s).sqrt()+s*g*b.KG/(2*b.MG*sgr)
   t=b.B1*lg**2+2*b.B2*lg*d['Lf0']+b.B3*d['Lf0']**2
   rho_f_lo=min(rho_f_lo,rho_f.lo);rho_f_hi=max(rho_f_hi,rho_f.hi)
   rho_g_lo=min(rho_g_lo,rho_g.lo);rho_g_hi=max(rho_g_hi,rho_g.hi)
   den_lo=min(den_lo,den.lo);beta_g_lo=min(beta_g_lo,beta_g.lo)
   u_lo=min(u_lo,u.lo);u_hi=max(u_hi,u.hi);t_lo=min(t_lo,t.lo)
   if rho_f.lo<=0 or rho_g.lo<=0 or den.lo<=0 or t.lo<=0:
    raise ArithmeticError(f'physical chart not certified in slab {i}')
  assert rho_f_lo>b.I.c(F(1,10)).hi
  assert rho_g_lo>b.I.c(F(22,25)).hi
  assert den_lo>b.I.c(F(3,4)).hi
  assert beta_g_lo>b.I.c(F(999,1000)).hi
  assert u_lo>b.I.c(-1).hi and u_hi<b.I.c(1).lo
  def exact(x):return str(F(x,b.S))
  return {
   'step':'68ad-C2d2e5b3b2c2b2',
   'mode':'ORIGINAL_G_EXECUTED_UNIFORM_PG_PARAMETER_INTERVAL_SPATIAL',
   'source_blobs':blobs,'cells':cells,
   's_domain':['0',str(S_MAX)],'lambda_domain':[str(-rad),str(rad)],
   'original_G':'Step45/46 C exact -> Step55 normalized symbolic -> interval compiled',
   'original_step55_inward_barrier':{
    k:barrier[k] for k in ('strict_max_Fupper_rational','strict_min_Flower_rational',
      'V_minus_Vstar_lower_rational','V_minus_Vstar_upper_rational',
      'V_actual_min_enclosure','V_actual_max_enclosure')},
   'rho_f_lower':exact(rho_f_lo),'rho_f_upper':exact(rho_f_hi),
   'rho_g_lower':exact(rho_g_lo),'rho_g_upper':exact(rho_g_hi),
   'f_dust_denominator_lower':exact(den_lo),
   'g_dust_beta_lower':exact(beta_g_lo),
   'U_lower':exact(u_lo),'U_upper':exact(u_hi),
   'T_lower':exact(t_lo),
   'proven_under_original_center_analyticity':[
    'strict inward barrier on all radial and parameter cells',
    'uniform |U|<1 and positive rho_g,rho_f on original spatial reconstructed branch',
    'nonzero Pg interval for spatial radial C=0 continuation subject to Step49 center theorem'],
   'not_proven':['physical external boundary admissibility','full Dirac rank',
     'temporal tertiaries','global lapses','K=0/J=0','4D evolution','stability','observables'],
   'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
  }
 finally:
  b.PG,b.U0=old_pg,old_u0

if __name__=='__main__':
 print(json.dumps(certificate(),indent=2,sort_keys=True,ensure_ascii=False))

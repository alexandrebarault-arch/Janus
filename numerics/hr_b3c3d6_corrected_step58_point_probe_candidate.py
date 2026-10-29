"""NUMERICAL (not interval-certified) original Step58 full six-coefficient
point probe on original Step55 radial ODE at r=17/20.
Corrected candidate: cubic U(s) endpoint jet from ODE through order 3.
The four-point Step58 numerical coefficients MUST be rerun; no certification yet. Step45/46/55-normalized
and Step58 source blobs are verified. Step57 is MINIMAL import shim.
This script is NOT a global positive-lapse BVP or Dirac proof.
This corrected candidate has NOT been integration-tested against Step58 in its publication session.
"""
import json, hashlib, math, time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import mpmath as mp
import sympy as sp
from .hr_step55_normalized_secondary import normalized_symbolic, check_original_source_blobs
from .hr_step58_temporal_operator import physical_operator
from .hr_b3c3d6_ode_consistent_jet_map import endpoint_jets, cubic_U
from .hr_b3c3d6_decimal_radius_endpoint import endpoint_s

SOURCE_SHA={
 'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
 'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
 'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
 'hr_step58_temporal_operator.py':'802c23aebd41780d8c462f1aa1711707fe4ee88f',
}
def source_checks():
 check_original_source_blobs()
 for name,expected in SOURCE_SHA.items():
  b=(Path(__file__).parent/name).read_bytes()
  h=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  assert h==expected,(name,h,expected)
 return SOURCE_SHA

mp.mp.dps=45
F=lambda s:mp.mpf(str(s))
A=F('.4');Y=F('.5787707228025044');B=A*Y
MG=F(1);MF=F('.10879548725')**2;M2=F('23.3348939346')
B0,B1,B2,B3,B4=[F(x) for x in ('0','1','-4.2383993109','13.6801214252','-38.5117901844')]
CG=F('.0015');CF=F('-.0012');KG=F('.0012');KF=F('-.0016');Z1=F('.004')
H2=F('.9')/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
PG=-2*A**2*mp.sqrt(H2);U0=MF*B*(PG/A-2*Z1)
U1=F('0.0007897451667202464909325108904961683602148118201691')
U2=F('-0.00001007385348674382817573689095286393593388364194376377343')

def geometry(s):
 ug=1+CG*s;uf=1+CF*s
 Lg=A*ug**2;Lf=B*uf**2
 Sgr=A*ug*(1+5*CG*s);Sfr=B*uf*(1+5*CF*s)
 T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
 T0=B0*Lg**2+2*B1*Lg*Lf+B2*Lf**2
 Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
 root=mp.sqrt(1-Z1**2*s)
 Dbar=M2*MG*Lg*Lf*T*Z1/root
 Wgbar=M2*MG*(Lg*T0+Lf*T*root)
 Wfbar=M2*MG*(Lf*Tf+Lg*T*root)
 Rg=-48*CG/(A**2*ug**5)
 Rf=-48*CF/(B**2*uf**5)
 Gmom=PG*(1+F(5)/2*CG*s)
 Gprime=2*PG*(1+5*CG*s)
 fac=Gmom/(2*MG*Lg*Sgr)
 betag=mp.sqrt(1+KG**2*s)+s*fac*KG*Lg
 Rhog=-(Gmom**2/(4*MG*Lg)-fac*(s*Dbar+Lg*Gprime)-MG*Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag
 Psg=(s*Dbar+Lg*Gprime-Rhog*s*KG*Lg)/Sgr
 return dict(Lg0=Lg,Lf0=Lf,Sgr0=Sgr,Sfr0=Sfr,Gmom=Gmom,Psg0=Psg,Rhog=Rhog,Gprime=Gprime,tg0=KG*Lg,tf0=KF*Lf,z1=Z1,Dbar=Dbar,Wfbar=Wfbar,Rf=Rf,Lgr0=4*A*CG*ug,Lfr0=4*B*CF*uf,
 Mg2=MG,Mf2=MF,m2=M2,beta0=B0,beta1=B1,beta2=B2,beta3=B3,beta4=B4)

S_EXPR,S_SYM,U_SYM, _=normalized_symbolic()
SYMS=sorted(S_EXPR.free_symbols,key=str)
FN=sp.lambdify(SYMS,S_EXPR,modules='mpmath',cse=True)

def G(s,u):
 data=geometry(s);data['s']=s;data['U']=u
 return FN(*[data[str(v)] for v in SYMS])

def u_solution(radius):
 s0=1e-4;sf,s_exact=endpoint_s(radius)
 assert abs(F(sf)-F(radius)**2)<F('1e-40'), ('decimal-radius endpoint mismatch',radius,sf,s_exact)
 def rhs(s,y):return [float((G(F(s),F(y[0]))-2*F(y[0]))/(2*F(s)))]
 init=float(U0+U1*F(s0)+U2*F(s0)**2)
 sol=solve_ivp(rhs,(s0,sf),[init],rtol=1e-12,atol=1e-14,method='DOP853',dense_output=True)
 assert sol.success,sol.message
 ur=F(sol.y[0,-1]);gr=G(F(radius)**2,ur)
 return ur,gr,sol

def physical_fields(r,U,Gr):
 s=r*r;g=geometry(s);Lg=g['Lg0'];Lf=g['Lf0'];Sgr=g['Sgr0'];Sfr=g['Sfr0'];Gmom=g['Gmom'];Psg=g['Psg0'];Rhog=g['Rhog'];Dbar=g['Dbar']
 pLf=s*U; pLfr=r*Gr; Dg=r**3*Dbar; Wf=s*g['Wfbar']; Rf=g['Rf'];tfr=r*g['tf0'];z=Z1*r
 fac=pLf/(2*MF*(r*Lf)*Sfr)
 beta=mp.sqrt(1+tfr**2/Lf**2)
 denom=beta+fac*tfr
 kinetic=Lf*pLf**2/(4*MF*(r*Lf)**2)
 curvature=-MF*Lf*(r*Lf)**2*Rf/2
 pf=-(kinetic-fac*(-Dg+Lf*pLfr)+curvature+z*Dg/Lf+Wf)/denom
 pSf=(-Dg+Lf*pLfr-pf*tfr)/Sfr
 return dict(Lg=Lg,pLg=s*Gmom,Sg=r*Lg,pSg=r*Psg,tg=F(0),pg=s*Rhog,
             Lf=Lf,pLf=pLf,Sf=r*Lf,pSf=pSf,tf=F(0),pf=pf)

def main(radius=0.85):
 source_checks()
 ur,gr,sol=u_solution(radius)
 R=F(radius);sr=R*R
 # U_s determined by exact original normalized ODE at the endpoint.
 jets=endpoint_jets(G,sr,ur)
 us=jets['U_s']
 # Independently enclose transcribed mpmath geometry in the byte-original
 # Step55 10^-28 integer outward interval engine at this point.
 from .hr_step55_global_barrier import geometry as interval_geometry, I, S
 for key,interval in interval_geometry(I.c(str(sr))).items():
  val=geometry(sr)[key]
  assert mp.mpf(interval.lo)/S-F("1e-40") <= val <= mp.mpf(interval.hi)/S+F("1e-40"),(key,interval,val)
 def fields_at(t):
  st=t*t
  # Cubic Taylor in s matches the actual Step55 ODE jets through U_sss.
  ut=cubic_U(t,sr,ur,jets)
  return physical_fields(t,ut,G(st,ut))
 fields=fields_at(R)
 o=physical_operator(); names=o['q'];der=o['qp'];sec=o['qpp'];third=o['qppp']
 qkeys=['Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf']
 subs={}
 for k,x in zip(qkeys,names):subs[x]=fields[k]
 for k,x in zip(qkeys,der):
  if str(x) in ('tgr','tfr'):
   subs[x]=R*geometry(sr)['tg0' if k=='tg' else 'tf0']
  elif k in ('tg','tf'):
   raise AssertionError('clock derivative missing')
  else:subs[x]=mp.diff(lambda t:fields_at(t)[k],R,1)
 # Enforce the Step55 radial ODE at the same decimal radius as the jet map.
 assert abs(subs[der[qkeys.index('pLf')]]-jets['pLf_prime'])<F('1e-35')
 for k,x in zip(qkeys,sec):
  if k in ('tg','tf'):
   subs[x]=mp.diff(lambda t:t*geometry(t*t)['tg0' if k=='tg' else 'tf0'],R,1)
  else:subs[x]=mp.diff(lambda t:fields_at(t)[k],R,2)
 for k,x in zip(qkeys,third):
  if k in ('tg','tf'):
   subs[x]=mp.diff(lambda t:t*geometry(t*t)['tg0' if k=='tg' else 'tf0'],R,2)
  else:subs[x]=mp.diff(lambda t:fields_at(t)[k],R,3)
 # Independently compare pLf radial second/third derivatives with ODE chain rule.
 for order, symbols, key in ((2,sec,'pLf_second'),(3,third,'pLf_third')):
  actual=subs[symbols[qkeys.index('pLf')]]
  assert abs(actual-jets[key])<F('1e-30'),(order,actual,jets[key])
 params=o['z'],o['zr'],o['zrr'],o['zrrr'];subs.update(zip(params,[R*Z1,Z1,0,0]))
 from .hr_step45_exact_physical_ward import exact_physical_ward
 p=exact_physical_ward();subs.update(zip(p['parameters'][:8],[MG,MF,M2,B0,B1,B2,B3,B4]))
 # Critical consistency checks of prescribed primary shell and original C.
 def evalexpr(expr):
  fn=sp.lambdify(tuple(sorted(expr.free_symbols,key=str)),expr,modules='mpmath',cse=True)
  return fn(*[subs[k] for k in sorted(expr.free_symbols,key=str)])
 shell={key:evalexpr(expr) for key,expr in [('Fz',o['Fz']),('Hg',p['Hg']),('Hf',p['Hf']),('C',o['C'])]}
 print('U(R)',ur,'G(R)',gr,'ODE residual',G(sr,ur)-gr,flush=True)
 print('shell', {k:float(v) for k,v in shell.items()},flush=True)
 coeff={}
 for name,terms in o['operator'].items():
  coeff[name]={}
  for j,expr in terms.items():
   value=evalexpr(expr)
   coeff[name][str(j)]=float(value)
   print(name,j,mp.nstr(value,22),flush=True)
 # Negative controls: change physical jets after constructing the on-shell point.
 offshell={}
 for var,delta in [('pSf',F('0.01')),('pLfr',F('0.01')),('pSgr',F('0.01')),('pLf',F('0.01'))]:
  symbol=next(x for x in (*names,*der) if str(x)==var)
  old=subs[symbol];subs[symbol]=old+delta
  offshell[var]={k:float(evalexpr(o['operator'][k][1])) for k in ('N','M')}
  subs[symbol]=old
 print('offshell_B',offshell,flush=True)
 report={'scope':'NUMERICAL_POINT_PROBE_ONLY_ORIGINAL_STEP58_ON_STEP55_ODE',
         'r':str(radius),'U_at_R':str(ur),'G_at_R':str(gr),
         'source_blobs':SOURCE_SHA,'original_step58_executed':True,
         'original_step55_global_interval_barrier_executed':False,
         'original_step55_geometry_pointwise_enclosure_pass':True,
         'step57_import':'minimal_shim',
         'ode_jet_map':'CUBIC_STEP55_ODE_CONSISTENT_THROUGH_ORDER_3',
         'affine_jet_defects':{'second':mp.nstr(jets['affine_defect_second'],30),'third':mp.nstr(jets['affine_defect_third'],30)},
         'holonomic_residuals':[mp.nstr(v,15) for v in jets['holonomic_residuals']],
         'shell_residuals':{k:float(v) for k,v in shell.items()},
         'coefficients':coeff,'negative_controls':offshell,'solver_nfev':sol.nfev,
         'lapse_BVP':'NOT_TESTED','center':'NOT_TESTED','Dirac':'NOT_TESTED',
         'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
 return report
if __name__=='__main__':
 import sys
 print(json.dumps(main(float(sys.argv[1]) if len(sys.argv)>1 else 0.85),indent=2))

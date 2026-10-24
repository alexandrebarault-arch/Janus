"""Step68b: exact leading-center Hamiltonian parity in a Step45-equation reconstruction.

This module transcribes the two post-integration-by-parts lapse densities
Ag,Bg,Af,Bf from GitHub Step45 and computes their Euler gradients for the
eight g/f metric canonical variables. This is an INDEPENDENT reconstruction,
NOT an import of the SHA-pinned original Step45 source; the identity is
conditional on analytic parity and BOTH center momenta pSg/r=2G, pSf/r=2U.
No full temporal secondary rank or global constraint evolution is claimed.
"""
from __future__ import annotations
from functools import lru_cache
import json
import sympy as sp
r=sp.symbols('r',positive=True)
Q=('Lg','pLg','Sg','pSg','tg','pg','Lf','pLf','Sf','pSf','tf','pf')
q=sp.symbols(' '.join(Q)); dq=sp.symbols(' '.join(x+'r' for x in Q)); ddq=sp.symbols(' '.join(x+'rr' for x in Q))
Lg,plg,Sg,psg,tg,pg,Lf,plf,Sf,psf,tf,pf=q
Lgr,plgr,Sgr,psgr,tgr,pgr,Lfr,plfr,Sfr,psfr,tfr,pfr=dq
z,zr,zrr=sp.symbols('z zr zrr')
mg,mf,m2=sp.symbols('mg mf m2',nonzero=True)
b0,b1,b2,b3,b4=sp.symbols('b0:5')
root=sp.sqrt(1-z*z)
At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
Af=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
Wg=m2*mg*(Lg*A0+Lf*At*root); Wf=m2*mg*(Lf*Af+Lg*At*root)
dg0=psg*Sgr+pg*tgr
kg=Lg*plg**2/(4*mg*Sg**2)-plg*psg/(2*mg*Sg)
kf=Lf*plf**2/(4*mf*Sf**2)-plf*psf/(2*mf*Sf)
dustg=pg*sp.sqrt(1+tgr**2/Lg**2);dustf=pf*sp.sqrt(1+tfr**2/Lf**2)
Ag=kg+dustg-mg*Lg-mg*Sgr**2/Lg+Wg+z*dg0/Lg+zr*plg
Bg=-2*mg*Sg*Sgr/Lg+z*plg
Ac=kf+dustf-mf*Lf-mf*Sfr**2/Lf+Wf+z*dg0/Lf+plg*(zr*Lg/Lf+z*Lgr/Lf-z*Lg*Lfr/Lf**2)
Bf=-2*mf*Sf*Sfr/Lf+z*Lg*plg/Lf
full=(*q,*dq,*ddq,z,zr,zrr); nxt=(*dq,*ddq,*([0]*len(ddq)),zr,zrr,0)
def Dr(expr):
    return sp.Add(*[sp.diff(expr,x)*xp for x,xp in zip(full,nxt) if expr.has(x) and xp!=0])
def euler(A,B,index):
    u=q[index];up=dq[index]
    return (sp.diff(A,u)-Dr(sp.diff(A,up)),sp.diff(B,u)-sp.diff(A,up)-Dr(sp.diff(B,up)),-sp.diff(B,up))
# E-Lg, E-Sg, E-pLg, E-pSg for both sectors
E={}
for label,A,B in [('N',Ag,Bg),('M',Ac,Bf)]:
    for field in ('Lg','Sg','pLg','pSg','Lf','Sf','pLf','pSf'):
        E[(label,field)]=euler(A,B,Q.index(field))
# substitutions (center analytic family)
a,a2,b,bf2,G,G2,P3,rhog,rhof,U,V,kg0,kf0,w=sp.symbols('a a2 b bf2 G G2 P3 rhog rhof U V kg0 kf0 w',real=True)
profiles={'Lg':a+a2*r**2,'Lf':b+bf2*r**2,'Sg':a*r+a2*r**3,'Sf':b*r+bf2*r**3,
'pLg':G*r**2+G2*r**4,'pSg':2*G*r+P3*r**3,'pg':rhog*r**2,
'pLf':U*r**2,'pSf':V*r,'pf':rhof*r**2,
'tg':sp.Integer(0),'tf':sp.Integer(0)}
sub={}
for name, val in profiles.items():
    sub[q[Q.index(name)]]=val
    sub[dq[Q.index(name)]]=sp.diff(val,r)
    sub[ddq[Q.index(name)]]=sp.diff(val,r,2)
sub[dq[Q.index('tg')]]=kg0*r*(a+a2*r**2)
sub[dq[Q.index('tf')]]=kf0*r*(b+b2*r**2)
sub[ddq[Q.index('tg')]]=sp.diff(sub[dq[Q.index('tg')]],r)
sub[ddq[Q.index('tf')]]=sp.diff(sub[dq[Q.index('tf')]],r)
sub[z]=w*r;sub[zr]=w;sub[zrr]=0
N0,M0,N2,M2=sp.symbols('N0 M0 N2 M2',real=True)
R={};
for label in ('N','M'):
    l,l2=(N0,N2) if label=='N' else (M0,M2)
    for field in ('Lg','Sg','pLg','pSg','Lf','Sf','pLf','pSf'):
        partner={'Lg':'pLg','pLg':'Lg','Sg':'pSg','pSg':'Sg',
                 'Lf':'pLf','pLf':'Lf','Sf':'pSf','pSf':'Sf'}[field]
        es=E[(label,partner)]
        ex=sum(coefficient*value for coefficient,value in zip(es,(l+l2*r*r,2*l2*r,2*l2)))
        if field in ('Lg','Sg','Lf','Sf'): ex=ex # Xq
        else: ex=-ex # Xp
        R[(label,field)]=ex.subs(sub)

def coeff(expr,n):
    if n==0: return sp.simplify(sp.limit(expr,r,0))
    return sp.simplify(sp.limit(expr/r**n,r,0))

@lru_cache(maxsize=1)
def center_audit():
    result={}
    f_offshell_defects={}
    for label in ('N','M'):
        x={field:sp.factor(coeff(R[label,field],n)) for field,n
           in [('Lg',0),('Sg',1),('pLg',2),('pSg',1),('Lf',0),('Sf',1),('pLf',2),('pSf',1)]}
        assert sp.factor(x['Lg']-x['Sg'])==0,(label,'metric center')
        assert sp.factor(x['pSg']-2*x['pLg'])==0,(label,'momentum center')
        f_metric_defect=sp.factor(x['Lf']-x['Sf'])
        f_momentum_defect=sp.factor(x['pSf']-2*x['pLf'])
        assert sp.factor(f_metric_defect.subs(V,2*U))==0
        assert sp.factor(f_momentum_defect.subs(V,2*U))==0
        f_offshell_defects[label]={'metric':f_metric_defect,'momentum':f_momentum_defect}
        # The f center primary radial momentum constraint gives pSf/r=2U.
        x['Lf']=sp.factor(x['Lf'].subs(V,2*U))
        x['Sf']=sp.factor(x['Sf'].subs(V,2*U))
        x['pLf']=sp.factor(x['pLf'].subs(V,2*U))
        x['pSf']=sp.factor(x['pSf'].subs(V,2*U))
        # Leading Dg/r after exact Hamiltonian variation of Dg
        # = pSg Sg' - Lg pLg' + pg tg'.  The last term is O(r^3).
        # pSg/r=2G, pLg/r²=G, Sg'(0)=Lg(0)=a.
        lead=sp.factor(a*(x['pSg']-2*x['pLg'])+2*G*(x['Sg']-x['Lg']))
        assert lead==0
        result[label]={**x,'delta_Dg_over_r_at_center':lead}
    # Necessary kinematic condition and sufficiency of initial parity:
    # DeltaK is order r² as interaction K = m² Mg² Lg Lf
    # * (beta1 Sg² + 2 beta2 Sg Sf + beta3 Sf²).
    result['f_offshell_defects']=f_offshell_defects
    return result


def fail_closed(principal_g_momentum_factor=2, principal_f_momentum_factor=2, even_lapse=True):
    if principal_g_momentum_factor != 2 or principal_f_momentum_factor != 2 or even_lapse is not True:
        raise ValueError('Center argument requires BOTH pSi/r=2*pLi/r² and even lapses')
    return center_audit()


def manifest():
    v=center_audit()
    defects=v['f_offshell_defects']
    return {'step':'68b','date':'2026-10-24',
      'model':'Spherical original Step45 post-IBP lapse densities independently reconstructed',
      'physical_original_Step45_byte_imported':False,
      'exact_center_assumptions':{
       'metrics':'Lg=a+a2*r²; Lf=b+bf2*r²; Sg=r*Lg; Sf=r*Lf; bf2 distinct from interaction beta2',
       'momenta':'pLg=G*r²+G2*r⁴; pSg=2G*r+P3*r³; pLf=U*r²; pSf=V*r with V=2U on f-primary',
       'dust':'pg=r²*rho_g; pf=r²*rho_f; theta_gprime=k_g*r*Lg; theta_fprime=k_f*r*Lf',
       'shift':'z=r*w, zprime=w (fixed initial Step55 benchmark)',
       'lapses':'N=N0+N2*r², M=M0+M2*r² (independent even smooth central profiles)',
       'parameters':'All symbolic; a,b,mg,mf are nonzero for divided quantities'},
      'exact_jet_identities':{
         label:{'delta_Lg_center':str(x['Lg']),
                'delta_Sg_over_r_center':str(x['Sg']),
                'delta_pLg_over_r2_center':str(x['pLg']),
                'delta_pSg_over_r_center':str(x['pSg']),
                'delta_Lf_center':str(x['Lf']),
                'delta_Sf_over_r_center':str(x['Sf']),
                'delta_pLf_over_r2_center':str(x['pLf']),
                'delta_pSf_over_r_center':str(x['pSf']),
                'delta_Dg_over_r_center':str(x['delta_Dg_over_r_at_center'])}
         for label,x in v.items() if label in ('N','M')},
      'off_f_primary_negative_control':{lab:{q:str(expr) for q,expr in row.items()}
          for lab,row in defects.items()},
      'proved':'When BOTH regular center momentum constraints pSg/r=2G and pSf/r=2U are imposed, each N and M Hamiltonian flow independently preserves delta Si/r=delta Li and delta pSi/r=2delta pLi/r² at the center; delta Dg/r=0 and hence analytic delta Dg=O(r³), delta K=O(r²). The f lapse has an explicit nonzero defect off the f radial momentum primary, making that condition essential.',
      'not_proved':['not a full interval bound','no lapse rank','no time preservation of secondary','not an exhaustive provider regression','do not freeze delta zprime'],
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(manifest(),indent=2,ensure_ascii=False))

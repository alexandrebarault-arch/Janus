"""JANUS-005 third radial jet independent numerical replay; NOT physical certification."""
import mpmath as mp
mp.mp.dps=45
m=mp.mpf
A=m('.4'); M=m('23.3348939346'); Z=m('.004'); CG=m('.0015'); KG=m('.0012'); CF=m('-.0012')
Y=m('.5787707228025044'); b0=m(0); b1=m(1); b2=m('-4.2383993109'); b3=m('13.6801214252')
C=b0+3*b1*Y+3*b2*Y**2+b3*Y**3
PG=-2*A*A*mp.sqrt(m('.9')/(3*A**3)+M*C/3)
p0=(A,M,Z,CG,KG,CF)
def rho(s,p):
 a,m2,z,cg,kg,cf=p
 lg=a*(1+cg*s)**2; lf=a*Y*(1+cf*s)**2
 t0=b0*lg**2+2*b1*lg*lf+b2*lf**2
 t=b1*lg**2+2*b2*lg*lf+b3*lf**2
 root=mp.sqrt(1-z*z*s)
 dbar=m2*lg*lf*t*z/root
 wbar=m2*(lg*t0+lf*t*root)
 rg=-48*cg/(a*a*(1+cg*s)**5)
 gm=PG*(1+m('2.5')*cg*s); gp=2*PG*(1+5*cg*s)
 sgr=a*(1+cg*s)*(1+5*cg*s)
 fac=gm/(2*lg*sgr)
 beta=mp.sqrt(1+kg*kg*s)+s*fac*kg*lg
 return -(gm**2/(4*lg)-fac*(s*dbar+lg*gp)-lg**3*rg/2+s*z*dbar/lg+wbar)/beta
def jet(n,p):
 return mp.diff(lambda s:rho(s,p),0,n)/mp.factorial(n)
def partial(n,i):
 return mp.diff(lambda x:jet(n,p0[:i]+(x,)+p0[i+1:]),p0[i])
base=(m(1),-(4*A**3*M*C+m('.9'))/(A**4*C),-Z/A,-CG/A)
J=mp.matrix([[partial(n,i) for i in (4,5)] for n in (1,2)])
rhs=mp.matrix([-sum(partial(n,i)*base[i] for i in range(4)) for n in (1,2)])
dKG,dCF=mp.lu_solve(J,rhs); d=base+(dKG,dCF)
print('dKG',mp.nstr(dKG,35),'dCF',mp.nstr(dCF,35))
for n in (1,2,3):
 v=sum(partial(n,i)*d[i] for i in range(6))
 print('D_a%d'%n,mp.nstr(v,38))
 assert (abs(v)<m('1e-35')) if n<3 else (abs(v)>m('1e-8'))
for h in (m('1e-4'),m('1e-6')):
 pp=tuple(x+h*y for x,y in zip(p0,d)); pm=tuple(x-h*y for x,y in zip(p0,d))
 print('fd',h,mp.nstr((jet(3,pp)-jet(3,pm))/(2*h),38))

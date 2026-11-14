import sympy as S
s,A,M,Z,CG=S.symbols('s A M Z CG',real=True)
Y=S.Rational('0.5787707228025044'); CF=S.Rational('-.0012'); KG=S.Rational('.0012')
b1=S.Integer(1);b2=S.Rational('-4.2383993109');b3=S.Rational('13.6801214252')
C=3*b1*Y+3*b2*Y**2+b3*Y**3
H=S.Rational(3,10)/A**3+M*C/3;PG=-2*A**2*S.sqrt(H)
ug=1+CG*s;uf=1+CF*s;Lg=A*ug**2;Lf=A*Y*uf**2;Sgr=A*ug*(1+5*CG*s)
T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2;T0=2*b1*Lg*Lf+b2*Lf**2
root=S.sqrt(1-Z**2*s);Dbar=M*Lg*Lf*T*Z/root
Wgbar=M*(Lg*T0+Lf*T*root);Rg=-48*CG/(A**2*ug**5)
Gmom=PG*(1+S.Rational(5,2)*CG*s);Gprime=2*PG*(1+5*CG*s)
fac=Gmom/(2*Lg*Sgr)
betag=S.sqrt(1+KG**2*s)+s*fac*KG*Lg
Rhog=-(Gmom**2/(4*Lg)-fac*(s*Dbar+Lg*Gprime)-Lg**3*Rg/2+s*Z*Dbar/Lg+Wgbar)/betag
mp=-(4*A**3*M*C+S.Rational(9,10))/(A**4*C)
D=lambda f:S.diff(f,A)+mp*S.diff(f,M)-Z/A*S.diff(f,Z)-CG/A*S.diff(f,CG)
p={A:S.Rational('0.4'),M:S.Rational('23.3348939346'),Z:S.Rational('.004'),CG:S.Rational('.0015')}
center=S.simplify(D(Rhog.subs(s,0)))
jet=S.N(D(S.diff(Rhog,s).subs(s,0)).subs(p),25)
assert center==0
assert abs(float(jet)+0.08612850795005536)<1e-14
print('PASS center:',center)
print('PASS radial first jet:',jet)
print('linear at s=0.1:',S.N(jet*S.Rational(1,10),15))

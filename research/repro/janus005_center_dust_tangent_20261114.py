import sympy as s
A,Y,M,Z,F=s.symbols('A Y M Z F',positive=True)
b1,b2,b3,cg=s.symbols('b1 b2 b3 cg',real=True)
C=3*b1*Y+3*b2*Y**2+b3*Y**3
H=s.Rational(3,10)/A**3+M*C/3
PG=-2*A**2*s.sqrt(H)
U=F*A*Y*(PG/A-2*Z)
B=A*Y
A0=A*(2*b1*A*B+b2*B**2)+B*(b1*A**2+2*b2*A*B+b3*B**2)
rho=3*A**3*H-24*A*cg-M*A0
mprime=-(4*A**3*M*C+s.Rational(9,10))/(A**4*C)
zprime=-Z/A
D=lambda expr:s.factor(s.diff(expr,A)+mprime*s.diff(expr,M)+zprime*s.diff(expr,Z))
assert s.simplify(D(PG))==0 and s.simplify(D(U))==0
assert s.simplify(D(rho)+24*cg)==0
v={A:s.Rational(2,5),Y:s.Rational('0.5787707228025044'),M:s.Rational('23.3348939346'),Z:s.Rational('0.004'),F:s.Rational('0.10879548725')**2,b1:1,b2:s.Rational('-4.2383993109'),b3:s.Rational('13.6801214252'),cg:s.Rational('0.0015')}
assert D(rho).subs(v)==-s.Rational(9,250)
print('PASS: dPG=dU0=0, d(rho_g_center)/dA=-24*cg=-0.036')

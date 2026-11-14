import sympy as s
A,Y,M,Z,F,cg=s.symbols('A Y M Z F cg',positive=True)
b1,b2,b3=s.symbols('b1 b2 b3',real=True)
B=A*Y
C=3*b1*Y+3*b2*Y**2+b3*Y**3
H=s.Rational(3,10)/A**3+M*C/3
A0=A*(2*b1*A*B+b2*B**2)+B*(b1*A**2+2*b2*A*B+b3*B**2)
PG=-2*A**2*s.sqrt(H)
U0=F*A*Y*(PG/A-2*Z)
rho=3*A**3*H-24*A*cg-M*A0
assert s.simplify(rho-(s.Rational(9,10)-24*A*cg))==0
mp=-(4*A**3*M*C+s.Rational(9,10))/(A**4*C)
zp=-Z/A
cgp=-cg/A
D=lambda f:s.factor(s.diff(f,A)+mp*s.diff(f,M)+zp*s.diff(f,Z)+cgp*s.diff(f,cg))
assert all(s.simplify(D(f))==0 for f in [PG,U0,rho])
assert s.simplify(s.diff(rho,M))==0
assert s.simplify(s.diff(rho,Z))==0
assert s.simplify(s.diff(rho,cg)+24*A)==0
assert s.simplify(s.diff(rho,A)+24*cg)==0
print('PASS: rho_g=9/10-24*A*CG; d(PG,U0,rho_g)=0 with dCG/dA=-CG/A')

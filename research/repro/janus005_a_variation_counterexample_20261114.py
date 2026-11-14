import sympy as s
A,Y,M,Z,F=s.symbols('A Y M Z F',positive=True)
b1,b2,b3=s.symbols('b1 b2 b3',real=True)
C=3*b1*Y+3*b2*Y**2+b3*Y**3
H=s.Rational(3,10)/A**3+M*C/3
PG=-2*A**2*s.sqrt(H)
U=F*A*Y*(PG/A-2*Z)
J=s.Matrix([PG,U]).jacobian([M,Z])
t=s.simplify(-J.inv()*s.Matrix([s.diff(PG,A),s.diff(U,A)]))
assert all(s.simplify(x)==0 for x in J*t+s.Matrix([s.diff(PG,A),s.diff(U,A)]))
assert s.simplify(t[0]+(4*A**3*M*C+s.Rational(9,10))/(A**4*C))==0
assert s.simplify(t[1]+Z/A)==0
values={A:s.Rational(2,5),Y:s.Rational('0.5787707228025044'),F:s.Rational('0.10879548725')**2,M:s.Rational('23.3348939346'),Z:s.Rational('0.004'),b1:1,b2:s.Rational('-4.2383993109'),b3:s.Rational('13.6801214252')}
p=s.N(PG.subs(values),35);u=s.N(U.subs(values),35)
for a in (s.Rational(2,5),s.Rational(401,1000)):
 y=values[Y];f=values[F];c=C.subs(values)
 m=s.N(3/c*(p**2/(4*a**4)-s.Rational(3,10)/a**3),30)
 z=s.N((p/a-u/(f*a*y))/2,30)
 h=s.N(s.Rational(3,10)/a**3+m*c/3,30)
 assert h>0 and m>0
 assert abs(s.N(-2*a*a*s.sqrt(h)-p,25))<s.Float('1e-20')
 assert abs(s.N(f*a*y*(p/a-2*z)-u,25))<s.Float('1e-20')
 print('A',a,'M2',m,'Z1',z)
print('PASS: exact tangent and finite reconstruction')

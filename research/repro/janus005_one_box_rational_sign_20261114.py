from fractions import Fraction as F

# Independent one-box sign proof for the prescribed Step55 algebraic map.
# All decimal inputs are exact rationals. No radial subdivision or sqrt.
A=F("0.4")
B=A*F("0.5787707228025044")
smax=F("0.7225")
zmax=F("0.01")
cg=F("0.0015")
cf=F("-0.0012")
m=F("23.3348939346")
b2=F("-4.2383993109")
b3=F("13.6801214252")
b4=F("-38.5117901844")

Lg0=A
Lg1=A*(1+cg*smax)**2
Lf0=B*(1+cf*smax)**2
Lf1=B

# Outward bounds by termwise monotonicity and known coefficient signs.
Tlo=Lg0**2+2*b2*Lg1*Lf1+b3*Lf0**2
Thi=Lg1**2+2*b2*Lg0*Lf0+b3*Lf1**2
b4=F("-38.5117901844")
Tflo=b2*Lg1**2+2*b3*Lg0*Lf0+b4*Lf1**2
Tfhi=b2*Lg0**2+2*b3*Lg1*Lf1+b4*Lf0**2

# Q = Lf*Tf + Lg*T*sqrt(1-z^2*s)*(1+s*z^2).
# With Tf<0 and T>0, sqrt<=1 and 1+s*z^2<=1+smax*zmax^2.
Qhi=Lf0*Tfhi+Lg1*Thi*(1+smax*zmax**2)
assert 0<Lg0<=Lg1 and 0<Lf0<=Lf1
assert 0<Tlo<=Thi
assert Tflo<=Tfhi<0
assert Qhi<0
assert 1-smax*zmax**2>0
assert m>0
print("PASS one-box rational certificate")
for k,v in (("T_lower",Tlo),("T_upper",Thi),("Tf_upper",Tfhi),("Q_upper",Qhi)):
    print(k, str(v), float(v))
print("DOMAIN s=[0,289/400], z=[-1/100,1/100]; J<0 conditional on prescribed geometry and m>0")

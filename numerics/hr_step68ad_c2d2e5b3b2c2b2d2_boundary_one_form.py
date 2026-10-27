import sympy as s
Lg,Sg,pLg,pSg,tg,pg,Lf,Sf,pLf,pSf,tf,pf=s.symbols('Lg Sg pLg pSg tg pg Lf Sf pLf pSf tf pf', nonzero=True, real=True)
Lgr,Sgr,Sg2,pLgr,tgr,Lfr,Sfr,Sf2,pLfr,tfr=s.symbols('Lgr Sgr Sg2 pLgr tgr Lfr Sfr Sf2 pLfr tfr',real=True)
N,Nr,M,Mr,V,z,mg,mf,m2,At=s.symbols('N Nr M Mr V z mg mf m2 At',real=True)
Q=N/Lg+M/Lf
Dg=pSg*Sgr-Lg*pLgr+pg*tgr
Df=pSf*Sfr-Lf*pLfr+pf*tfr
curvg=mg*(-Lg+Sgr**2/Lg+2*Sg*Sg2/Lg-2*Sg*Sgr*Lgr/Lg**2)
curvf=mf*(-Lf+Sfr**2/Lf+2*Sf*Sf2/Lf-2*Sf*Sfr*Lfr/Lf**2)
F=N*(curvg+pg*s.sqrt(1+(tgr/Lg)**2))+M*(curvf+pf*s.sqrt(1+(tfr/Lf)**2))+z*Q*Dg+V*(Dg+Df)
# Other kinetic/potential pieces contain no radial derivatives, hence no boundary form.
# Higher derivative formula Theta_q=(dF/dq'-D_r dF/dq'')delta q+(dF/dq'')delta q'
# Total derivative of dF/dS'' uses radial derivative of N,S,L.
Dcurvg2=s.diff(F,Sg2)
Dcurvf2=s.diff(F,Sf2)
Dg2=s.diff(Dcurvg2,N)*Nr+s.diff(Dcurvg2,Sg)*Sgr+s.diff(Dcurvg2,Lg)*Lgr
Df2=s.diff(Dcurvf2,M)*Mr+s.diff(Dcurvf2,Sf)*Sfr+s.diff(Dcurvf2,Lf)*Lfr
coeff={
"Sg'":s.diff(F,Sg2),"Sf'":s.diff(F,Sf2),
'Sg':s.diff(F,Sgr)-Dg2,'Sf':s.diff(F,Sfr)-Df2,
'Lg':s.diff(F,Lgr),'Lf':s.diff(F,Lfr),
'pLg':s.diff(F,pLgr),'pLf':s.diff(F,pLfr),
'tg':s.diff(F,tgr),'tf':s.diff(F,tfr)}
expected={
'Sg\'':2*mg*N*Sg/Lg,'Sf\'':2*mf*M*Sf/Lf,
'Sg':-2*mg*Nr*Sg/Lg+(z*Q+V)*pSg,
'Sf':-2*mf*Mr*Sf/Lf+V*pSf,
'Lg':-2*mg*N*Sg*Sgr/Lg**2,'Lf':-2*mf*M*Sf*Sfr/Lf**2,
'pLg':-z*(N+M*Lg/Lf)-V*Lg,'pLf':-V*Lf,
'tg':pg*(N*tgr/(Lg**2*s.sqrt(1+(tgr/Lg)**2))+z*Q+V),
'tf':pf*(M*tfr/(Lf**2*s.sqrt(1+(tfr/Lf)**2))+V)}
assert len(expected)==10
for k in expected:
    assert s.simplify(coeff[k]-expected[k])==0,(k,s.simplify(coeff[k]-expected[k]))
print('10 symbolic boundary coefficient identities PASS')
# algebraic shift equation with HR potential derivative
K=m2*mg*Lg*Lf*At
Fz=s.simplify(Q*Dg-m2*mg*(N*Lf+M*Lg)*At*z/s.sqrt(1-z*z))
assert s.simplify(Fz-Q*(Dg-K*z/s.sqrt(1-z*z)))==0
print('shift stationarity factorization PASS')
# Full original-IBP difference B and its derivative (without sqrt dust)
B=2*mg*N*Sg*Sgr/Lg+2*mf*M*Sf*Sfr/Lf-z*pLg*(N+M*Lg/Lf)
# coefficient of delta z in delta B
assert s.diff(B,z)==-pLg*(N+M*Lg/Lf)
# this is nonzero even on Fz=0; must be cancelled by IBP bulk z-gradient contributions
print('delta B/delta z identity PASS')
# witness: independent Dirichlet-coordinate variations can have arbitrary delta Sg' and Sf'
witness={'N':s.Integer(1),'M':s.Integer(1),'V':s.Integer(0),'z':s.Rational(4,5),'Lg':s.Integer(2),'Lf':s.Integer(3),'Sg':s.Integer(5),'Sf':s.Integer(7),'mg':s.Integer(2),'mf':s.Integer(3)}
subs={eval(k):v for k,v in witness.items()}
assert expected["Sg'"].subs(subs)==10
assert expected["Sf'"].subs(subs)==14
assert expected['pLg'].subs(subs)==-s.Rational(4,3)
print('3 exact rational witness checks PASS; TOTAL 15 checks')
# Independent original/IBP radial symplectic-potential comparison, including z' boundary term.
zr=s.symbols('zr',real=True)
A=z*(N+M*Lg/Lf)
Apr=zr*(N+M*Lg/Lf)+z*(Nr+Mr*Lg/Lf+M*Lgr/Lf-M*Lg*Lfr/Lf**2)
curvibpg=mg*(-N*Lg-N*Sgr**2/Lg-2*Nr*Sg*Sgr/Lg)
curvibpf=mf*(-M*Lf-M*Sfr**2/Lf-2*Mr*Sf*Sfr/Lf)
Fibp=curvibpg+curvibpf+N*pg*s.sqrt(1+(tgr/Lg)**2)+M*pf*s.sqrt(1+(tfr/Lf)**2)+z*Q*(pSg*Sgr+pg*tgr)+Apr*pLg+V*(Dg+Df)
ibp={"Sg'":0,"Sf'":0,'Sg':s.diff(Fibp,Sgr),'Sf':s.diff(Fibp,Sfr),
     'Lg':s.diff(Fibp,Lgr),'Lf':s.diff(Fibp,Lfr),'pLg':s.diff(Fibp,pLgr),
     'pLf':s.diff(Fibp,pLfr),'tg':s.diff(Fibp,tgr),'tf':s.diff(Fibp,tfr),
     'z':s.diff(Fibp,zr)}
var={'Sg':Sg,'Sf':Sf,'Lg':Lg,'Lf':Lf,'pLg':pLg,'pLf':pLf,'tg':tg,'tf':tf,
     "Sg'":Sgr,"Sf'":Sfr,'z':z}
for key,symbol in var.items():
    assert s.simplify(coeff.get(key,0)-ibp[key]-s.diff(B,symbol))==0,key
print('11 independent original-minus-IBP boundary one-form identities PASS')
# Differentiate the genuine lapse-linear HR square-root interaction, not an assumed F_z.
A0,As=s.symbols('A0 As',real=True)
W=m2*mg*(N*(Lg*A0+Lf*At*s.sqrt(1-z*z))+M*(Lf*As+Lg*At*s.sqrt(1-z*z)))
assert s.simplify(s.diff(W+z*Q*Dg,z)-Fz)==0
print('HR interaction shift derivative identity PASS')
print('TOTAL: 27 substantive symbolic/rational assertions PASS')

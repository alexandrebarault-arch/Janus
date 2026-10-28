"""Source-faithful Step45 radial-weight audit; no complete Step58 replay.
Run: python numerics/hr_step68ad_b3c3a_diagonal_shift_covariance.py
"""
import sympy as s
Q = 'Lg pLg Sg pSg tg pg Lf pLf Sf pSf tf pf'.split()
q = s.symbols(' '.join(Q)); qp = s.symbols(' '.join(x+'r' for x in Q))
Lg,plg,Sg,psg,tg,pg,Lf,plf,Sf,psf,tf,pf = q
Lgr,plgr,Sgr,psgr,tgr,pgr,Lfr,plfr,Sfr,psfr,tfr,pfr = qp
z,zr,mg,mf,m2 = s.symbols('z zr mg mf m2')
b0,b1,b2,b3,b4 = s.symbols('b0:5')
root = s.sqrt(1-z*z)
At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
Af=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
D0=psg*Sgr+pg*tgr
Ag=Lg*plg**2/(4*mg*Sg**2)-plg*psg/(2*mg*Sg)+pg*s.sqrt(1+tgr**2/Lg**2)-mg*Lg-mg*Sgr**2/Lg+m2*mg*(Lg*A0+Lf*At*root)+z*D0/Lg+zr*plg
Bg=-2*mg*Sg*Sgr/Lg+z*plg
Am=Lf*plf**2/(4*mf*Sf**2)-plf*psf/(2*mf*Sf)+pf*s.sqrt(1+tfr**2/Lf**2)-mf*Lf-mf*Sfr**2/Lf+m2*mg*(Lf*Af+Lg*At*root)+z*D0/Lf+plg*(zr*Lg/Lf+z*Lgr/Lf-z*Lg*Lfr/Lf**2)
Bm=-2*mf*Sf*Sfr/Lf+z*Lg*plg/Lf
D=psg*Sgr-Lg*plgr+pg*tgr
K=m2*mg*Lg*Lf*At
Fz=D-K*z/root
Czr=-(K*root+D*z)/(Lg*Lf)
weights=[1,0,0,1,0,1,1,0,0,1,0,1]

def verify(expr,weight):
    # Delta q=V q'+w V' q; delta q'=V q''+(w+1)V' q'+w V'' q.
    # z is a radial scalar and z' has weight one.
    v2=sum(s.diff(expr,qp[i])*weights[i]*q[i] for i in range(12))
    v1=sum(s.diff(expr,q[i])*weights[i]*q[i]+s.diff(expr,qp[i])*(weights[i]+1)*qp[i] for i in range(12))+s.diff(expr,zr)*zr-weight*expr
    assert s.cancel(s.together(v2))==0
    assert s.cancel(s.together(v1))==0

if __name__=='__main__':
    cases=[('Ag',Ag,1),('Bg',Bg,0),('Af',Am,1),('Bf',Bm,0),('Dg',D,2),('K',K,2),('Fz',Fz,2),('C_zprime',Czr,0)]
    for name,expr,weight in cases:
        verify(expr,weight)
        print(name, 'two exact identities PASS')
    print('PASS: 16 exact SymPy equalities; 0 failures. No Dirac rank or boundary theorem.')

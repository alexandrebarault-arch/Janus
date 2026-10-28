"""b3c3d3: regular-centre pullback of all ten original non-IBP endpoint coefficients.

Source-faithful transcription of the Step37/Step45 densities, with the exact
coefficients independently checked in b3c3d2. This is a parity lemma, not a
Dirac tangency or an original Step45/55/58 engine replay.
"""
import json
import sympy as s

r=s.symbols('r',real=True)
L0,F0,H2,I2,L2,F2,N0,M0,N2,M2,mg,mf=s.symbols(
    'L0 F0 H2 I2 L2 F2 N0 M0 N2 M2 mg mf',positive=True)
z1,v1,ps1,psf1,pl2,plf2,pg2,pf2,tg2,tf2=s.symbols(
    'z1 v1 ps1 psf1 pl2 plf2 pg2 pf2 tg2 tf2',real=True)
# Independent tangent coefficients. Central metric regularity enforces
# Sg/r(0)=Lg(0), Sf/r(0)=Lf(0), including their variations.
dL0,dF0,dH2,dI2,dL2,dF2,dtg0,dtf0,dpl2,dplf2=s.symbols(
    'dL0 dF0 dH2 dI2 dL2 dF2 dtg0 dtf0 dpl2 dplf2',real=True)
Lg=L0+L2*r**2; Lf=F0+F2*r**2
Sg=r*(L0+H2*r**2); Sf=r*(F0+I2*r**2)
Sgr=s.diff(Sg,r);Sfr=s.diff(Sf,r)
N=N0+N2*r**2; M=M0+M2*r**2
Nr=s.diff(N,r);Mr=s.diff(M,r)
z=z1*r;V=v1*r
pSg=ps1*r; pSf=psf1*r
pLg=pl2*r**2;pLf=plf2*r**2
pg=pg2*r**2;pf=pf2*r**2
tgp=2*tg2*r;tfp=2*tf2*r
Q=N/Lg+M/Lf
# Original ten boundary coefficients (non-integrated by parts).
coeff={
 'Sgr':2*mg*N*Sg/Lg,
 'Sfr':2*mf*M*Sf/Lf,
 'Sg':-2*mg*Nr*Sg/Lg+(z*Q+V)*pSg,
 'Sf':-2*mf*Mr*Sf/Lf+V*pSf,
 'Lg':-2*mg*N*Sg*Sgr/Lg**2,
 'Lf':-2*mf*M*Sf*Sfr/Lf**2,
 'pLg':-z*(N+M*Lg/Lf)-V*Lg,
 'pLf':-V*Lf,
 'tg':pg*(N*tgp/(Lg**2*s.sqrt(1+(tgp/Lg)**2))+z*Q+V),
 'tf':pf*(M*tfp/(Lf**2*s.sqrt(1+(tfp/Lf)**2))+V)
}
variation={
 'Sgr':dL0+3*dH2*r**2,'Sfr':dF0+3*dI2*r**2,
 'Sg':r*(dL0+dH2*r**2),'Sf':r*(dF0+dI2*r**2),
 'Lg':dL0+dL2*r**2,'Lf':dF0+dF2*r**2,
 'pLg':dpl2*r**2,'pLf':dplf2*r**2,
 'tg':dtg0,'tf':dtf0
}
terms={k:coeff[k]*variation[k] for k in coeff}

def check():
    n=0
    # All ten contributions have odd parity; each is analytic at r=0.
    for name,term in terms.items():
        assert s.simplify(term.subs(r,-r)+term)==0,name
        n+=1
    # Only four curvature terms have an O(r) contribution.
    expected={'Sgr':2*mg*N0*dL0,'Lg':-2*mg*N0*dL0,
              'Sfr':2*mf*M0*dF0,'Lf':-2*mf*M0*dF0}
    for name,term in terms.items():
        assert s.simplify(s.limit(term/r,r,0)-expected.get(name,0))==0,name
        n+=1
    assert s.simplify(sum(expected.values()))==0;n+=1
    # A tangent perturbation of the quadratic metric coefficient shows O(r^3)
    # is sharp; it does not prove an allowed Dirac direction.
    sharp=s.limit(terms['Lg'].subs({dL0:0,dL2:1})/r**3,r,0)
    assert s.simplify(sharp+2*mg*N0)==0;n+=1
    # If the centre relation is violated by the *variation* (dSgr=dH0,
    # dSg=r*dH0 while dLg=dL0), the leading term survives.
    dH0=s.symbols('dH0',real=True)
    nonregular=s.limit((coeff['Sgr']*dH0+coeff['Lg']*dL0)/r,r,0)
    assert s.simplify(nonregular-2*mg*N0*(dH0-dL0))==0;n+=1
    # Mixed lapse/canonical leading O(r) pieces cancel on the regular centre
    # tangent plane, despite being nonzero as free ambient jet components.
    lapse_mix=s.diff(coeff['Sgr'],N0)*dL0+s.diff(coeff['Lg'],N0)*dL0
    assert s.simplify(s.limit(lapse_mix/r,r,0))==0;n+=1
    assert s.simplify(s.limit(lapse_mix/r**3,r,0)).is_finite is not False;n+=1
    return {'symbolic_assertions_passed':n,
      'theorem':'Theta_center=O(r^3) on regular parity-preserving families, including variable even lapses',
      'sharp_witness':'dL2=1, all other tangent coefficients zero: lim Theta/r^3=-2*mg*N0',
      'adversarial_nonregular':'lim Theta/r=2*mg*N0*(dH0-dL0)',
      'scope':'Original non-IBP endpoint one-form; regular center only, not outer boundary or Dirac',
      'original_step45_55_58_import_replay':False,
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(check(),indent=2))

"""Independent mathematical audit of the externally supplied 2026 JHR note.

NOT a cosmological perturbation solver. Reproduces the note's algebraic
stellar test and hand-forced 3-mode oscillator, and checks kinetic/EFT signs.
Source: 'Travaux Scientifiques - Modele Cosmologique Janus Covariant (JHR)
et Scripts Python.pdf', 14 October 2026, sections 1, 2 and 5.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp, trapezoid

MPL_REDUCED_EV=2.435e27

def tensor_kinetic_matrix(chig=1.,chif=1.,relative_f_sign=-1.):
    """Two TT polarization kinetic signature, up to an overall + prefactor."""
    if chig<=0 or chif<=0:
        raise ValueError("positive gravitational couplings required")
    return np.diag([1./chig, relative_f_sign/chif])

def eft_lambda3_eV(m_eV, reduced_planck_eV=MPL_REDUCED_EV):
    if m_eV<0 or reduced_planck_eV<=0:
        raise ValueError("invalid mass or Planck scale")
    return (m_eV*m_eV*reduced_planck_eV)**(1./3.)

def stellar_weighted_divergences(radius=None,compactness=.05):
    """Literally implement the note's combined stellar Noether test."""
    r=np.linspace(.1,5.,500) if radius is None else np.asarray(radius,dtype=float)
    phi=-compactness/np.sqrt(r*r+1.)
    dphi=compactness*r/(r*r+1.)**1.5
    phibar=-phi;dphibar=-dphi
    g0=np.exp(phibar-phi);gr=np.exp(-(phibar-phi))
    dg0=(dphibar-dphi)*g0;dgr=-(dphibar-dphi)*gr
    tr=g0+gr+2.
    V00=g0-tr+3.;Vrr=gr-tr+3.;Vtt=1.-tr+3.
    Vb00=1.-g0;Vbrr=1.-gr;Vbtt=0.
    div_g=2*r*Vrr-r*r*dg0-r*r*(dphi*(V00-Vrr)+2/r*Vtt)
    div_f=2*r*Vbrr-r*r*dgr-r*r*(dphibar*(Vb00-Vbrr)+2/r*Vbtt)
    return div_g,div_f

def toy_acoustic_peak_amplitudes(alpha=4.4,*,rtol=1e-9,atol=1e-11):
    """Reproduce the supplied toy ODE, NOT a predicted physical CMB C_l."""
    if alpha<=-1:
        raise ValueError("alpha=-1 is singular")
    eta_ini,eta_rec=1.,284.
    eta_grid=np.linspace(eta_ini,eta_rec,2000)
    ag=eta_grid/115.+.25*(eta_grid/115.)**2
    Rbg=.62*ag/ag[-1]
    rs=trapezoid(1./np.sqrt(3*(1+Rbg)),eta_grid)
    powers=[]
    for n in (1,2,3):
        k=n*np.pi/rs
        psi=.32*(np.exp(-(k/.018)**2)/(1+alpha)+
                 alpha*np.exp(-(k/.110)**2)/(1+alpha))
        def ode(eta,y):
            u,du=y
            a_rel=eta/115.+.25*(eta/115.)**2
            Rb=.62*a_rel/3.994
            dRb=.62/(115.*3.994)*(1+.5*eta/115.)
            cs2=1./(3*(1+Rb))
            return du,-dRb/(1+Rb)*du-k*k*cs2*(u-Rb*psi)
        sol=solve_ivp(ode,(eta_ini,eta_rec),(-.85,0.),rtol=rtol,atol=atol)
        powers.append(5100.*sol.y[0,-1]**2*np.exp(-2*(k/.082)**2))
    return rs,np.array(powers)

def toy_isw_ratio(omega_eff_jhr=.295):
    """Copy note's phenomenological growth-index integral; not an ISW C_l."""
    a=np.linspace(.33,1.,200)
    fl=(.315*a**-3/(.315*a**-3+.685))**.55
    f=(omega_eff_jhr*a**-3/
       (omega_eff_jhr*a**-3+(1-omega_eff_jhr)*a**(-.5)))**.56
    return trapezoid(abs(f-1)/a,a)/trapezoid(abs(fl-1)/a,a)

def main():
    print("opposite-EH TT eigenvalues:",np.linalg.eigvalsh(tensor_kinetic_matrix()))
    dg,df=stellar_weighted_divergences()
    print("Noether: max |div_g|, |div_f|, |sum| =",
          max(abs(dg)),max(abs(df)),max(abs(dg+df)))
    print("Lambda3 for m=1e-32 eV =",eft_lambda3_eV(1e-32),"eV")
    print("m for Lambda3=1meV =",np.sqrt(1e-9/MPL_REDUCED_EV),"eV")
    for alpha in (0,1,2,4.4,8,20):
        rs,p=toy_acoustic_peak_amplitudes(alpha)
        print("alpha",alpha,"rs",rs,"peak2",p[1],"peak3",p[2],
              "R32",p[2]/p[1])
    for om in (.2,.295,.35,.45):
        print("ISW toy omega_eff",om,"ratio",toy_isw_ratio(om))

if __name__=="__main__":
    main()

# JANUS-006 — maintien exact de Z pendant compensation du jet de bord (2026-11-19)

Source au HEAD 701d5aca819ae817a2e0c3c47b39b7e9bb3d3255 : numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py. Résultat ALGÉBRIQUE AMBIANT, non physique.

Le précédent rapport compensait Sgr en tenant Z fixe, sans expliciter comment préserver Z=D/sqrt(D²+K²), D=ps*Sgr-Lg*pr+pg*tgp. Poser M=rho*N, q=1+rho*Lg/Lf, Z0=D0/sqrt(D0²+K²), Sgr=h0+Z0*q*Lg*p/(2*mg*Sg), pr=(ps*Sgr+pg*tgp-D0)/Lg. À paramètres Lg,Lf,Sg,mg,K non nuls et autres variables fixées, D=D0 exactement, donc Z=Z0. Le pullback de Theta=(2mg*N*Sg/Lg)dSgr+(-Z*(N+M*Lg/Lf)-V*Lg)dp vaut exactement -V*Lg*dp ; dTheta=0. La compensation exige dpr/dp=ps*Z0*q/(2mg*Sg).

Contrôle réellement exécuté Python/SymPy : substitution de pr dans D -> D0 (PASS), substitution de Sgr dans Theta -> -V*Lg*dp (PASS), dérivée en N du coefficient -> 0 (PASS). Commandes reproductibles :
```python
import sympy as s
N,p,rho,Lg,Lf,Z,V,mg,Sg,h0,ps,pg,tgp,D0,K=s.symbols('N p rho Lg Lf Z V mg Sg h0 ps pg tgp D0 K',positive=True)
q=1+rho*Lg/Lf
h=h0+Z*q*Lg*p/(2*mg*Sg)
pr=(ps*h+pg*tgp-D0)/Lg
D=s.simplify(ps*h-Lg*pr+pg*tgp)
theta=s.simplify((2*mg*N*Sg/Lg)*s.diff(h,p)-Z*N*q-V*Lg)
assert D==D0 and theta==-V*Lg
assert s.simplify(s.diff(theta,N))==0
```
Dans ce script, Z est le symbole constant Z0 ; l'identité D=D0 rend ce choix cohérent en posant Z=D0/sqrt(D0²+K²).

LIMITES : aucune preuve de tangence Dirac, équations des lapses, stationnarité, régularité, ni deux véritables bords. Aucune cellule physique évaluée/certifiée/inconclusive (0/0/0), tests moteur/pilote SKIP. Aucun GO ou NO-GO physique.

NEXT_ACTION_EXACT : calculer le jacobien total Dirac + deux vrais bords avec dpr et dSgr, tester la tangence compensatrice. JANUS-001 BLOCKED en attente des dépendances authentifiées Step45/46/55/58. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

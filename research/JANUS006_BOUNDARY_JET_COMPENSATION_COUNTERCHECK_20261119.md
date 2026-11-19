# JANUS-006 — compensation d'un jet de bord (2026-11-19)

Source au HEAD 5ecd3adad40559a7c07531276dbb920846398eba : numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py. Résultat **algébrique ambiant seulement**.

Avec M=rho*N, Lg,Lf,Sg,mg,V,Z fixes, q=1+rho*Lg/Lf, la forme de bord sur les variables N,p,Sgr est theta=(2mg*N*Sg/Lg)dSgr+(-Z*N*q-V*Lg)dp. Contrairement au témoin antérieur à Sgr fixe, autoriser Sgr=h0+k*p avec k=Z*q*Lg/(2mg*Sg) donne exactement theta=-V*Lg*dp, donc dtheta=0 et circulation rectangulaire nulle. Plus généralement le coefficient dN wedge dp sur Sgr=h(N,p) est (2mg*Sg/Lg)*partial_p(h)-Z*q.

**Contrôle exécuté :** Python, SymPy 1.14.0 ; `python /mnt/data/janus_cycle_1919/check.py` PASS (substitution, différentiation et circulation par quatre intégrales exactes). SHA-256 script local : dd73444e163d72a8353e5666f4cad18f27de8e6f4d5cd3452686b183a0034d77. Reproduction minimale :

```python
import sympy as s
N,p,rho,Lg,Lf,Z,V,mg,Sg,h0=s.symbols('N p rho Lg Lf Z V mg Sg h0',positive=True)
q=1+rho*Lg/Lf
h=h0+Z*q*Lg*p/(2*mg*Sg)
theta_p=s.expand((2*mg*N*Sg/Lg)*s.diff(h,p)-Z*N*q-V*Lg)
assert s.simplify(theta_p+V*Lg)==0
assert s.diff(theta_p,N)==0
```

**Limites :** le graphe n'est pas prouvé compatible avec Dirac, stationnarité, maintien de Z=D/sqrt(D²+K²) lorsque Sgr varie, deux vrais bords, ou solutions globales. C'est un contre-contrôle de portée : la courbure non nulle à Sgr fixe ne s'étend pas à tous les graphes ambiants. Aucune conclusion physique. Tests moteur/pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0.

**NEXT_ACTION_EXACT :** construire le jacobien total Dirac + deux vrais bords, y compris variations compensatrices de D et Z, et vérifier si ce graphe appartient au noyau admissible. JANUS-001 : authentifier les imports historiques avant tests et pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

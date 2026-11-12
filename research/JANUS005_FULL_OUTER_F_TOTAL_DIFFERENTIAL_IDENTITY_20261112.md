# JANUS-005 — Différentielle totale algébrique des traces f au bord (2026-11-12)

**Portée :** identité exacte sur la carte algébrique du jacobien extérieur Step46, **non** dérivée le long d'une famille physique de solutions. Source des définitions : `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs` (définitions citées dans `research/JANUS005_FIXED_GEOMETRY_TANGENT_SCOPE_COUNTEREXAMPLE_20261111.md`), HEAD initial `a88efc59300ad780718b717b79efc8b62696c86a`.

Au bord extérieur fixé `R=17/20`, poser `s=R²`, `m=mf`, `L=Lf`, `T=Sfr`, `D=Dbar`, `w=Wfbar`, `rf=Rf`, `k=kf`, `z=z1`, `U=pLf/s`, `V=pLf'/R`. Définir

`den = beta + k*s*U/(2*m*T)`

`num = U²/(4*m*L) - U*(V-s*D/L)/(2*m*T) - m*L³*rf/2 + s*z*D/L + w`

`rho=-num/den; pf=s*rho; pSf=R*(L*V-s*D-s*k*L*rho)/T`.

Pour `den != 0`, la différentielle **totale** (toutes les 11 variables `m,L,T,beta,k,U,V,D,rf,z,w` autorisées à varier) est exactement

`d(rho)=-(d(num)+rho*d(den))/den`

`d(pf)=s*d(rho)`

`d(pSf)=R/T*(V*dL+L*dV-s*dD-s*(L*rho*dk+k*rho*dL+k*L*d(rho)))-pSf*dT/T`.

Ces trois identités conservent les corrélations entre coefficients et sont valides pour toute variation différentiable dans le domaine `m*L*T*den != 0`. Elles ne prouvent pas que les onze variations sont physiquement indépendantes. Elles montrent explicitement les contributions oubliées lorsqu'on extrapole le jacobien à géométrie fixée.

**Contrôle réellement exécuté :** Python/SymPy 1.14.0, deux identités symboliques `simplify(dpf - sum(diff(pf,x)*dx)) == 0` et idem pour `pSf` : PASS. Contre-vérification indépendante : substitution de onze perturbations simultanées rationnelles `x(t)=x0+t*(i+1)/100` (i=0..10), dérivation directe des deux expressions composées en `t=0`, comparaison aux formules de différentielle : 2 PASS. Au total **4 assertions PASS**, aucune donnée synthétique présentée comme cellule physique.

**Limites :** ce calcul ne fournit ni les dérivées physiques `dm/dlambda,...,dw/dlambda`, ni leurs enclosures, ni les conditions effectives aux deux bords, ni le rang Dirac. Il ne certifie aucun signe des traces. Cellules Step55/58 évaluées : **0**, certifiées : **0**. `GATE_2B=OPEN`, `JANUS_R=NOT_VALIDATED`.

**NEXT_ACTION_EXACT :** identifier dans Step45/46/49/55 les onze fonctions de la famille physique et leurs dérivées sous contraintes ; substituer ces dérivées dans les trois identités, encloser `den` sans zéro et les quatre traces au bord extérieur, puis vérifier les vraies conditions aux deux bords. En parallèle JANUS-001 : transfert authentifié des dépendances, SHA Git, neuf tests et pilote physique à une cellule.

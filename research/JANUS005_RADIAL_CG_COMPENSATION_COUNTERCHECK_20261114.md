# JANUS-005 — contrôle radial contradictoire de la compensation CG (2026-11-14)

Source fixée : main `239b1593e516a5914da641ef9f6751209b91dad3`, `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, `numerics/hr_step49_analytic_center.py` blob `d570948912885d45a625fa2db31c6a5435b6a654`.

## Question falsifiable

La tangente algébrique déjà obtenue avec `dA=1`, `dM2/dA=-(4*A**3*M2*C+9/10)/(A**4*C)`, `dZ1/dA=-Z1/A`, `dCG/dA=-CG/A` préserve exactement les trois données **centrales** PG, U0, rho_g(0). Préserve-t-elle également la densité radiale g `Rhog(s)` prescrite par Step55 ?

## Reproduction et calcul réellement exécuté

Python 3, SymPy 1.14.0. La formule `geometry(s)` du module Step55 a été retranscrite avec ses définitions exactes : `ug=1+CG*s`, `uf=1+CF*s`, `Lg=A*ug**2`, `Lf=A*Y*uf**2`, `Sgr=A*ug*(1+5*CG*s)`, `T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2`, `T0=2*b1*Lg*Lf+b2*Lf**2`, `root=sqrt(1-Z1**2*s)`, `Dbar=M2*Lg*Lf*T*Z1/root`, `Wgbar=M2*(Lg*T0+Lf*T*root)`, `Rg=-48*CG/(A**2*ug**5)`, `Gmom=PG*(1+5*CG*s/2)`, `Gprime=2*PG*(1+5*CG*s)`, `fac=Gmom/(2*Lg*Sgr)`, `betag=sqrt(1+KG**2*s)+s*fac*KG*Lg`, `Rhog=-(Gmom**2/(4*Lg)-fac*(s*Dbar+Lg*Gprime)-Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag`, avec `PG=-2*A**2*sqrt(3/(10*A**3)+M2*C/3)` et `C=3*b1*Y+3*b2*Y**2+b3*Y**3`. Calcul exact des dérivées par `sympy.diff` puis substitution rationnelle des paramètres du benchmark Step55.

La dérivée directionnelle calculée est `D(Rhog)=∂A Rhog + mp*∂M2 Rhog - (Z1/A)*∂Z1 Rhog - (CG/A)*∂CG Rhog`. Résultats (arrondis, **évaluations ponctuelles**, non certificats d'intervalle) :

| s | Rhog(s) | D(Rhog)(s) |
|---|---:|---:|
| 0 | 0.8856000000000000 | 0 exactement (simplification symbolique) |
| 0.1 | 0.8864125832393613 | -0.008611882626807962 |
| 0.5 | 0.8896568565247812 | -0.04303852860863991 |
| 0.7225 | 0.8914572232941271 | -0.06217237372402699 |

Contrôle contradictoire indépendant : différences finies `A→A+10^-7` avec `M2(A)` recalculé **exactement** par `3*((PG/(-2*A**2))**2-0.3/A**3)/C`, `Z1(A)=Z1_initial*A_initial/A`, `CG(A)=CG_initial*A_initial/A`. mpmath 60 décimales : quotients -0.008611880842241718259826 à s=0.1 et -0.04303851959914875339169 à s=0.5 ; PG préservé à ~8e-62. La différence finie converge vers la dérivée analytique quand le pas diminue.

## Verdict limité

**CONTRE-EXEMPLE à l'affirmation que la compensation centrale conserve automatiquement la densité radiale complète.** Elle conserve Rhog(0), mais pas Rhog(s) pour les points intérieurs examinés, **si** l'on maintient la forme prescrite de tous les autres coefficients Step55. Cela ne réfute pas l'existence d'une solution physique ajustant d'autres champs, ni ne démontre que Rhog(s) doive rester fixe. Les contraintes de Dirac linéarisées et les deux vrais bords ne sont pas testés. Les évaluations ponctuelles ne sont pas un certificat global.

Tests moteur b3c3d9 exécutés : 0 ; cellules physiques évaluées/certifiées/inconclusives : 0/0/0.

**NEXT_ACTION_EXACT :** dans Step45/46, identifier quelles variations de Rhog(s), de PG(s), des lapses et des deux traces aux vrais bords sont admissibles ; calculer le système linéarisé complet avant de revendiquer une direction physique. JANUS-001 : transférer les modules authentiques et les dépendances historiques puis exécuter les neuf tests et le pilote une cellule.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# JANUS-005 — M2 n'est pas une variation à géométrie fixée (2026-11-11)

## Provenance et hypothèse
Lecture du fichier authentique `numerics/hr_step55_global_barrier.py` au HEAD `0852407710e74ca7bf2e67a72a6ff92337b6ac6b`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. La tangente centrale de `JANUS005_EXPANDED_M2_FRIEDMANN_TANGENT_20261111.md` laisse varier M2, avec A,Y,MF,Z1 et B0..B4 fixes. Il faut vérifier si cela conserve les données géométriques et potentielles injectées dans l'équation radiale Step55.

## Calcul exact, contrôle contradictoire
Le code définit `Dbar=M2*MG*Lg*Lf*T*Z1/root` et `Wfbar=M2*MG*(Lf*Tf+Lg*T*root)`, où `T=B1*Lg²+2*B2*Lg*Lf+B3*Lf²`, `Tf=B2*Lg²+2*B3*Lg*Lf+B4*Lf²`, `root=sqrt(1-Z1²*s)`. Ainsi à MG=1 :
`partial_M2 Dbar=Lg*Lf*T*Z1/root` et `partial_M2 Wfbar=Lf*Tf+Lg*T*root`.

À s=0 et avec les décimales rationnelles exactes du code :
- `partial_M2 Dbar = 4.008661680144792e-5` (approximation d'un rationnel exact non nul).
- `partial_M2 Wfbar = -0.0049985348708680355` (idem).
- `K(Y)=0.04308405810889453`, et sur M2=23.3348939346, `dPG/dM2=-0.0028891577835134484`.

Le contrôle local `python /tmp/janus_m2.py` a exécuté SymPy 1.14.0 avec `Rational` construit depuis les littéraux décimaux du fichier : assertions de linéarité en M2 et non-nullité des deux dérivées centrales, plus identité de la dérivée de PG, PASS. Le script local est éphémère ; les expressions et littéraux ci-dessus suffisent à le reproduire indépendamment. Les résultats numériques affichés sont des approximations de calculs rationnels, pas des certificats d'intervalle.

## Portée scientifique
**NO-GO pour l'interprétation « M2 varie, mais la géométrie/potentiel Step55 restent fixes »** : les termes `Dbar` et `Wfbar` changent effectivement. Cela ne réfute pas la tangente du jacobien central, qui demeure une identité algébrique, ni l'existence éventuelle d'une famille physique avec M2 variable. En revanche, prolonger cette tangente vers les traces radiales exige de dériver la totalité de `geometry(s)`, de `G(s,U)`, et de résoudre la variation de l'ODE avec conditions centrales et aux deux vrais bords. Les seules variations de (PG,U0,M2) ne suffisent pas à vérifier ces contraintes.

**NEXT_ACTION_EXACT :** former le système variationnel `2*s*dU_s=(G_U-2)*dU+G_M2*dM2`, en calculant `G_M2` par différentiation totale de `geometry(s)` (y compris PG(M2), Dbar, Wfbar, données g), puis confronter sa solution régulière aux deux vrais bords et aux contraintes de Dirac. En parallèle JANUS-001 : transférer les dépendances authentifiées, vérifier les blobs, rejouer neuf tests et pilote physique. Tests Step55/58 exécutés ici : 0 ; cellules physiques évaluées/certifiées : 0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

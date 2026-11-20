# JANUS-006 — Pullback exact de la forme de bord sur Fz=0 (2026-11-20)

## Sources et hypothèses
Sources lues au HEAD 318c50778bdbcd8fb9c22983ec9973f726b50c46 : `numerics/hr_step45_exact_physical_ward.py` (blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`) et `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py` (blob `6898c88760cc0766e949f9bade4908b9bc176c58`). On considère la tranche à configuration canonique et lapses N,M fixés du module de bord, avec Lg,Lf>0, K>0, |z|<1, a=N+M Lg/Lf>0, et K constant sous les variations considérées. D=psg*Sgr-Lg*plgr+pg*tgr, Fz=D-K z/sqrt(1-z²), Z=D/sqrt(D²+K²), P=a*pLg, Theta=dC-Z dP. Aucune affirmation de réduction complète de Dirac.

## Calcul et contrôle contradictoire
Résoudre Fz=0 donne `plgr_star=(psg*Sgr+pg*tgr-K*z/sqrt(1-z²))/Lg`. Par substitution directe, Z=z (K>0, |z|<1) ; si K<0, Z=-z. Ainsi sur la sous-variété Fz=0, à configuration et lapses fixés, `i* dTheta=dP wedge dz` (K>0). Choisir les coordonnées locales indépendantes (pLg,z), en compensant plgr par la formule précédente, fournit exactement `(i* dTheta)(partial_pLg,partial_z)=a>0`. Ce sont bien des directions tangentes à **Fz seul**, car la contrainte est identiquement résolue pour plgr. Si z est en plus fixé, ce coefficient devient nul sur cette tranche restreinte. L'obstruction ambiante du rapport précédent n'est donc pas simplement effacée par Fz, mais la paire de directions construite n'est pas démontrée tangente à Hg=Hf=C_exact=0.

Contrôle indépendant : différentiation de `D=K z/sqrt(1-z²)` donne `dD/dz=K/(1-z²)^(3/2)`; `dZ/dD=K²/(D²+K²)^(3/2)`; leur produit vaut 1 pour K>0. Contrôle SymPy exécuté : résolution Fz en plgr, identité `simplify(Z²-z²)==0`, branche positive vérifiée, coefficient a de la 2-forme. **PASS algébrique, sans exécution du module Git original localement.**

## Limites et falsification suivante
Le pullback sur Fz=0 ne constitue pas le pullback sur le noyau conjoint de dHg,dHf,dFz,dC_exact, ni sur les variations holonomes respectant les deux véritables bords. La fixation dynamique de N,M et la variation de configuration peuvent modifier le diagnostic. La transcription Step45 du témoin ponctuel antérieur reste non authentifiée localement. Aucun NO-GO global.

JANUS-001 : tests/pilote SKIP ; cellules demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** calculer au témoin authentifié une base du noyau de `Jacobian([Hg,Hf,Fz,C_exact],variables)`, évaluer `dP wedge dZ` sur cette base et comparer aux variations holonomes et aux deux traces ; pour JANUS-001 transférer les sources Step45/46/55/58 et dépendances authentifiées, vérifier les SHA Git, lancer neuf tests et pilote une cellule.

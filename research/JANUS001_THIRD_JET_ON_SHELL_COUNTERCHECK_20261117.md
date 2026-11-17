# JANUS-001 — contrôle contradictoire du contre-exemple de troisième jet (2026-11-17)

## Portée
Réconciliation mathématique du rapport `JANUS001_SECOND_ORDER_JET_NONUNIQUENESS_20261117.md` avec l'ODE spatiale générique Step55 `2s U_s=G(s,U)-2U`. **Calcul formel générique, pas de replay physique Step55/58.** HEAD d'entrée `667b56d26825369560fdc01d70b9bb534bb8f0e3`.

## Résultat 1 — contre-exemple hors coquille à s0>0
Soit `delta U=epsilon*(s-s0)^3`, avec `s0>0`, et supposons `G` au moins C² en ses arguments et deux solutions de la **même** ODE. Les deux profils ont les mêmes `U,U_s,U_ss` en s0. Pour la différence des résidus `F=2sU_s-G(s,U)+2U`, la dérivée seconde en s0 vérifie exactement
`(F_B-F_A)_{ss}(s0)=12*epsilon*s0`.
En effet, la différence de `G(s,U)` est d'ordre `(s-s0)^3` et n'affecte pas le jet d'ordre 2. Pour deux solutions exactes `F_A=F_B=0`, donc `epsilon=0`. Ainsi le contre-exemple libre publié est **incompatible avec la même ODE régulière** pour `epsilon != 0` et `s0>0`. Ce n'est pas une réfutation de son identité algébrique, mais une restriction essentielle de sa portée physique.

## Résultat 2 — troisième jet fixé par l'ODE pour s>0
Deux différentiations de `2sU_s=G(s,U)-2U` donnent
`2s U_sss=G_ss+2 G_sU U_s+G_UU U_s²+(G_U-6)U_ss`, où les dérivées de G sont partielles. À s0>0, une solution C³ et G C² fixe donc U_sss dès que `s0,U,U_s,U_ss` et les dérivées de G sont connus. Cela ne fournit pas automatiquement une **enclosure** fiable des dérivées partielles de G ni de la solution. À s=0 la division par 2s est interdite : le problème de résonance centrale reste distinct.

## Résultat 3 — distinction avec le gate direct Step58
L'audit existant `numerics/hr_b3c3d7_step58_reduced_jet_order_audit.py` (blob `d5a3d214b586a238d275df281a0a03ca683ac774`) affirme et teste, sur sa carte primaire et Fz=0, `A_N` d'ordre U_s au maximum et `A_M` d'ordre U_ss au maximum. Il distingue `dA_M/dr`, qui peut requérir U_sss. **L'audit n'a pas été rejoué ici** : sa portée et ses assertions sont rapportées depuis le fichier authentique. Il faut vérifier séparément le gate qui utilise des dérivées de A_M, sans prétendre que les coefficients directs dépendent de U_sss.

## Reproduction réellement exécutée
`python` avec SymPy 1.14.0 : différentiation symbolique de `F=2sU_s-G(s,U)+2U` à l'ordre 2, résolution pour `U_sss` ; différentiation de `2s deltaU_s+2deltaU` aux ordres 0..3 en s0 : `0,0,12 epsilon s0,48 epsilon`. Contrôle indépendant : développement local `2s deltaU_s=6epsilon(s0+x)x²`, tandis que `delta G=O(x³)`, donc le coefficient de x² du résidu est `6epsilon s0`, soit dérivée seconde `12epsilon s0`.

## Limites et suite
Pas de calcul des véritables dérivées de G, pas de preuve de solution globale, de contraintes de Dirac, des deux vrais bords ou de stabilité. Tests b3c3d9 SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** sur les sources authentifiées, vérifier si le runner b3c3d9 utilise `dA_M/dr` et, dans ce cas, calculer/enclore U_sss via les dérivées secondes de G sur s>0 ; préserver le traitement singulier du centre. Reconstituer ensuite les imports Step45/46/55/58 et les blobs historiques, exécuter neuf tests puis pilote à une cellule. Si reconstruction bloquée, poursuivre JANUS-005/006 Dirac et deux vrais bords.

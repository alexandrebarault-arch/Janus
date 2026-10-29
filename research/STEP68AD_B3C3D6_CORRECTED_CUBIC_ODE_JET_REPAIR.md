# JANUS b3c3d6 — réparation des jets Step55 (29 octobre 2026)

**Verdict : avancée de méthode, PAS une conclusion physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Source de vérité et provenance

Branche unique `research/gate2b-nonhomothetic-transfer`, HEAD initial vérifié `4831ad91b2120bc0ab5dbfbcd47d4d4b8e11ba60`. Lectures directes des blobs originaux Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, et du probe précédent `643d90183367e74a28ed453d93f5489074b75b08`. Le script original du probe reste intact : la réparation est publiée séparément pour comparaison contrôlée.

## Calcul exact et correction reproductible

Pour `s=r²>0`, `pLf=r² U(s)` et `2s U_s=G(s,U)-2U` :

`U_s=(G-2U)/(2s)`

`U_ss=[G_s+(G_U-4)U_s]/(2s)`

`U_sss=[G_ss+2G_sU U_s+G_UU U_s²+(G_U-6)U_ss]/(2s)`.

Les jets radiaux exacts satisfont `pLf'=rG`, `pLf''=G+2s(G_s+G_U U_s)`, `pLf'''=6r(G_s+G_U U_s)+4rs(G_ss+2G_sU U_s+G_UU U_s²+G_U U_ss)`. Le prolongement affine historique de `U(s)` oubliait `4s²U_ss` dans `pLf''` et `36rsU_ss+8rs²U_sss` dans `pLf'''`. Le nouveau module calcule les dérivées partielles de `G` avec mpmath et construit le polynôme de Taylor cubique local ; trois identités de dérivées radiales sont contrôlées par une autre voie, et `s=0` est explicitement exclu de cette carte.

**Portée :** cette identité est exacte pour toute fonction différentiable `G` sur `s>0` ; elle ne prouve PAS que les défauts sont non nuls sur le profil physique Step55. Le solveur global DOP853 double précision et la sensibilité de Step58 aux jets restent non certifiés. Les anciennes valeurs de `B_N,B_M,E_N,E_M≈10^-44` ne doivent PAS être promues en identités exactes.

## Tests réellement exécutés

Dans le répertoire local de préparation `/mnt/data/janus_ode_repair` : `PYTHONPATH=. python -m unittest discover -s tests -v` : **6 tests PASS, 0 FAIL final**, non indépendants, sur les octets publiés du module et de son test ; `python -m compileall -q numerics tests` PASS ; contrôle séparé SymPy des **3 identités radiales** PASS. Les deux échecs initiaux de tests provenaient d'une attente erronée pour `U_s` dans le témoin jouet et d'une comparaison flottante trop stricte dans le cas affine ; ils ont été corrigés avant publication. Témoin jouet `G=s²+U², s=1/4,U=1/2` : `U_s=-11/8`, `U_ss=37/4`, défauts `37/16` et `1369/64`.

**NON EXÉCUTÉ :** le nouveau candidat `hr_b3c3d6_corrected_step58_point_probe_candidate.py` avec les moteurs Step45/46/55/58 originaux ; les **3 tests d'intégration** correspondants sont publiés, mais non comptés comme réussis. Le DNS du conteneur local ne résout pas `raw.githubusercontent.com`. La lecture et l'écriture via connecteur GitHub fonctionnent. Aucune évaluation des six coefficients corrigés aux quatre rayons n'est revendiquée.

## Fichiers

- `numerics/hr_b3c3d6_ode_consistent_jet_map.py` — blob `c66534cab7da29cf9c214f08c965def3b99b4e63`, code local réellement testé.
- `tests/test_hr_b3c3d6_ode_consistent_jet_map.py` — blob `6ed35dffb7f9c1f61d6ed0edc7106f990e912d32`, tests locaux réellement exécutés.
- `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` — blob `9eb5167bec74fc427307a262faaa6a1f785785a8`, candidat d'intégration NON exécuté.
- `tests/test_hr_b3c3d6_corrected_step58_point_probe_candidate.py` — blob `625304d17c903a7e8311c72030224a19d6f7e217`, 3 tests d'intégration NON exécutés.
- `research/reports/gate2b-b3c3d6-corrected-cubic-ode-jet-candidate.json` — rapport machine lisible.

## Prochaine étape, sans faux saut

Rejouer les **vrais** Step45/46/55/58 SHA-authentifiés à `r=1/4,1/2,7/10,17/20` avec ce candidat, mesurer `U_ss,U_sss`, les deux défauts affines, les six coefficients et leur différence avec le probe ancien, ainsi que les résidus des primaires et de `C`. Si le résultat est stable, chercher factorisation exacte et enclosures sur l'intervalle, raccord régulier au centre, lapses positifs avec **deux vrais bords**, puis analyse Dirac six couples, charges/générateurs, jauge temporelle, K=0/J=0, dynamique 4D, stabilité et observables. Pas de no-go ni de validation JANUS à ce stade.

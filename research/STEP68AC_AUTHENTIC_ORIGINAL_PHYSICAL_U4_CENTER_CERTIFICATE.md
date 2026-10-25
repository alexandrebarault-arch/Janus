# JANUS — STEP68ac : vrai coefficient central U4 du Hamiltonien physique original (six couples)

**25 octobre 2026. Branche unique de recherche : research/gate2b-nonhomothetic-transfer.**  
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Aucun fichier GitHub Actions/workflow modifié.

## 1. Résultat nouveau : coefficient analytique U4 ORIGINAL, certifié en fractions sortantes

Après la preuve d'impossibilité Step68ab de déduire des jets supérieurs des seules bornes agrégées, Step68ac utilise DIRECTEMENT le **véritable Hamiltonien sphérique HR à six couples canoniques et deux poussières mobiles** Step45, la réduction secondaire affine originale Step46, la normalisation originale Step55 et sa géométrie benchmark exacte.

Soit s=r² et pLf(r)=r² U(r²), avec la branche analytique historique Step49 :

    U(s)=U0+U1*s+U2*s²+U3*s³+U4*s⁴+O(s⁵).
    2*s*U_s=G(s,U)-2*U.

**Nouvelle borne rationnelle entière, certifiée sur le vrai U4 :**

    -3728419736053033407 / 10000000000000000000000000000
       <= U4 <=
    -3728419736052979197 / 10000000000000000000000000000
       < 0.

Soit environ **U4 ≈ -3.7284197360530 × 10^-10**. Ces fractions sont les deux bornes EXACTES extraites de l'arithmétique à arrondi sortant 10^-28 du véritable G, combinées à l'intervalle U3 précédemment certifié. L'incertitude des bornes est inférieure à 10^-21, pas une précision scientifique absolue de la cosmologie.

**Conséquence canonique**, conditionnelle à l'analyticité Step49 : dans le vrai secteur f, le coefficient de r^10 de pLf est U4 STRICTEMENT NÉGATIF et pLf^(10)(0)=10! U4 <0.

## 2. Simplification symbolique exacte, non numérique

Depuis l'expression originale G(s,U) calculée par la chaîne byte-authentic 45/46/55, SymPy prouve, SANS imposer les contraintes temporelles :

    partial_U G(s,U) |_(s=0) = -Sfr0/Lf0

où Sfr0 représente S_f'(r)/... sous la normalisation du centre et Lf0 la valeur radiale de la métrique f. Pour le centre analytique régulier historique :

    Sfr0(0)=Lf0(0)>0

donc **G_U(0,U)=-1** EXACTEMENT, indépendamment du choix de U. La dérivée seconde de G en U au centre est également symboliquement nulle.

La récurrence historique Step68ab devient alors

    U_n = [s^n]G(s,U0+...+U_(n-1)*s^(n-1)) / (2n+3),
    en particulier U4 = [s^4]G(s,U0+U1*s+U2*s²+U3*s³) / 11.

Les dénominateurs exacts pour n=1..4 sont **5, 7, 9, 11** : aucune quasi-résonance cachée au centre. L'identité G_U=-1 a également été contrôlée par une **seconde voie**, propagation automatique de Taylor dans la variable U avec la vraie expression G et l'arithmétique entière ; l'intervalle obtenu contient exactement -1.

## 3. Reproduction authentique et deux chemins d'enclosure U4

Toutes les sources historiques **reconstruites localement octet pour octet et SHA vérifiées** :

| Source historique | SHA Git blob original |
|---|---|
| numerics/hr_step45_exact_physical_ward.py | 66aa43841dccfe4a5d586a49be9c10af3a67a10e |
| numerics/hr_step46_exact_secondary_ode.py | bac025c28dbe1561c0c36c56dbfda46dc326f804 |
| numerics/hr_step55_normalized_secondary.py | a54a6acf2f7ad2f64c500faecfa1406ecbf7b862 |
| numerics/hr_step55_global_barrier.py | a6e7004120d0a166a3a8973c2fbe1487a8eb70fe |
| numerics/hr_step68l_refined_global_barrier.py | 2a1ffc026a30abf41208b44a707dc869daf0929d |
| numerics/hr_step68n_interval_ode_jets.py | 96370e0599748c6dc07faf339ab3646ae3474e7d |

Ce sont bien les ORIGINAUX importés, pas une re-saisie indépendante de leurs équations. Leur octet-identité a été vérifiée avant chaque calcul via le préflight. Le code Step68ac réutilise l'ancienne classe originale Step68n Jet. Celle-ci a un entier global K=3 fixé pour ses développements d'ordre trois ; **sans modifier son fichier source**, Step68ac le passe TEMPORAIREMENT à K=4 en mémoire sous contexte try/finally, puis restaure K=3. Un test d'exception démontre la restauration ; tout ordre initial inattendu est rejeté.

Calcul original : expression de G issue de la six-paires et de la secondaire C, 1048 opérations SymPy. Utilisation des **intervalles entiers sortants historiques de Step55 à échelle S=10^28** pour chaque opération élémentaire (y compris racines carrées, quotient et produit), et de développements de séries normalisés par les factorielles.

Deux calculs de U4 avec les MÊMES expressions G, mais des contraintes d'entrée différentes :

1. **Récurrence de zéro à quatre** : calcul U1, U2, U3, U4, en partant de la seule valeur centrale certifiée U0 ; les intervalles recalculés pour U1/U2 incluent les originaux Step55, l'intervalle U3 recoupe strictement l'intervalle publié Step67b. Cette voie donne un U4 plus large.
2. **Inputs historiques resserrés** : fixer les vrais intervalles Step55 U1/U2 et le vrai intervalle Step67b U3, ce dernier étant rechargé par le code Step68aa qui réauthentifie également Step68z et les trois rapports Step68u/v/y. Calculer [s^4]G et diviser par l'EXACT 11, puis intersecter avec la première voie. Cette voie donne la borne encadrée §1.

Les deux calculs sont corrélés (même G, même arithmétique) : **ne jamais les appeler deux oracles physiques indépendants.** Ils fournissent deux *inclusions valides* et l'intersection reste valide. Les cinq coefficients de l'EDO originale, ordres 0 à 4, ont été recalculés avec les intervalles U0..U4 retenus et leurs résidus contiennent **tous exactement zéro**. Ne jamais confondre « intervalle de résidu contient zéro » avec « l'identité est démontrée sans les hypothèses de branche ».

**Rejeu additionnel de la vraie preuve historique Step55** : le certificat global radial original à **256 cellules a réellement été réexécuté**, résultat « deux poussières/J/K positifs » confirmé (preuve spatiale).

## 4. Test, fichiers et état durable

Exécution locale dans le workspace temporaire /mnt/data/janus-step68ac (GitHub est le point permanent) :

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
      tests/test_hr_step68ac_authentic_original_U4.py \
      tests/test_hr_step68ab_derivative_data_obstruction.py \
      tests/test_hr_step68aa_canonical_center_radial_jets.py \
      tests/test_hr_step68z_invariant_center_cone.py

**44 TESTS PASSED en 5.92 secondes**, zéro échec. Soit **15 nouveaux tests Step68ac + 29 tests de régression précédents**. Ils couvrent les neuf Ward résidus originaux du vrai Hamiltonien, les cinq identités primaires Step46, la symétrie analytique G_U0, la récurrence d'ordres 1-4, le signe de U4, les résidus originaux, l'altération volontaire du blob Step68n, et le vrai certificat global historique à 256 cellules.

Fichiers publiés sur la branche recherche :

- **Code :** numerics/hr_step68ac_authentic_original_U4.py — blob **a90b2d6d4882a0ff0aa810c5a320ba247f171a13**.
- **Tests :** tests/test_hr_step68ac_authentic_original_U4.py — blob **705108773b57f4f621ac7888a63359cb19e4429b**.
- **Rapport JSON issu du VRAI PROGRAMME :** research/reports/gate2b-step68ac-authentic-U4-report.json — blob **16ae8dab3563c17134e4e20f886fb7306dc2e4ba**.
- Les trois nouveaux blobs Git ont été relus après publication et comparés aux hashes des fichiers réellement exécutés. Le rapport entier est égal octet à octet à l'output de CLI de Step68ac.

Rejouer, dans un clone complet :

    PYTHONPATH=. python -m numerics.hr_step68ac_authentic_original_U4 research/reports

## 5. Verrous encore strictement ouverts : prochaine Step68ad

Cette étude porte sur le seul COEFFICIENT CENTRAL U4 de la solution radiale. **Elle n'établit pas** l'inclusion de U_ss, U_sss ou du jet pLf''' sur un anneau de rayon positif ; ces jets exigent des bornes quantitatives des dérivées supérieures du G FIXE et un contrôle rigoureux des restes Taylor. Un seul coefficient U4 ne suffit pas pour justifier un reste uniforme, et il serait incorrect de dériver des bornes sur U ou U_s.

**NEXT STEP68ad :** reconstruire et SHA-authentifier les sources Steps57/58/60 et 68o, établir des bornes de C^k du G original sur l'intervalle petit centre s∈[0,1/1024] avec une méthode de série normalisée / divisions par s préannulées ; en déduire des tubes quantifiés pour U_ss et U_sss, puis certificats AN/r² et AM/r² sur les 7 cellules PENDING [1/64,1/32], puis r→0. Conserver tous les contrôles supplémentaires : contraintes Dirac complètes, lapses/bords/jauge, J=0/K=0, oracle NON-IBP et dynamique cosmologique 4D.

La validité globale de JANUS et l'absence de fantôme BD n'en résultent pas : **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

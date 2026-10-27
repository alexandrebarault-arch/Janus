# JANUS — 68ad-C2d2e5b3b2c2a : borne uniforme de poussière g sous variation de P_g (27 octobre 2026)

**Résultat PARTIEL, calcul indépendant exact par intervalles rationnels ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources et hypothèses
Formules recopiées indépendamment de la reconstruction g du moteur physique original `numerics/hr_step55_global_barrier.py` (blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`), avec les paramètres du benchmark, la géométrie et le shift fixés. La chaîne originale Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, normalisation Step55 `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` a été lue sur GitHub. **Les moteurs Python originaux n'ont PAS été réexécutés.** Le nouveau programme évalue une transcription indépendante de la reconstruction g, et non la vraie fonction physique `G(s,U,P_g)` de l'EDO f.

Poser `s=r²`, `0<=s<=289/400`, `P_g(lambda)=P_g(0)+lambda`, `|lambda|<=1/1000`. `P_g(0)=-2a² sqrt(H2)` avec `H2` exactement celui de Step55. Les racines carrées sont encadrées par `isqrt` sur une grille rationnelle de précision `10^-34`, avec arrondis dirigés prouvés. Tous les autres calculs emploient `fractions.Fraction` et des extensions d'intervalles contenant rigoureusement toutes les valeurs de la boîte. Le programme utilise 256 cellules radiales jointives, sans échantillonnage ponctuel.

## Résultat certifié sur la boîte complète
Les intervalles calculés donnent les **bornes rationnelles strictes** suivantes pour chaque `s` et chaque `lambda` de la boîte :
- `rho_g(s,lambda)>22/25=0.88` (borne inférieure brute ~0.8806795666522835).
- `beta_g(s,lambda)>999/1000=0.999` (borne brute ~0.9991750787755442).
- `rho_g(s,lambda)<9/10=0.9` (borne supérieure brute ~0.8963937829249305).
- `L_g>=2/5`, `S_g'>=2/5`, `sqrt(1-z²)>0`, et `P_g(lambda)<0`.

Le programme vérifie `rho_g>4/5` et `beta_g>99/100` explicitement et publie les bornes rationnelles brutes ; les seuils renforcés 22/25, 999/1000 et 9/10 ont été contrôlés indépendamment sur ces bornes rationnelles. La validité de l'enclosure repose sur l'exactitude de la transcription des formules g originales ; une relecture des formules est nécessaire pour la traçabilité de cette hypothèse. Cela établit **une marge non nulle de positivité de la poussière g sur le domaine radial entier**, pas une marge de continuation de l'EDO f.

## Exécution, reproductibilité et limites
Commande : `PYTHONPATH=. python -m unittest -v test_hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube` depuis le répertoire contenant les deux fichiers, puis `python hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube.py`. **13 tests unittest PASS, 0 FAIL** ; certificats calculés pour 64, 128, 256 et 512 cellules, tous positifs. Les 256 cellules constituent le certificat publié. Les fichiers Python publiés correspondent aux octets exécutés et le certificat JSON est celui généré localement.

**NON DÉMONTRÉ :** positivité de la poussière f sous variation, validité et sensibilité du vrai `G(s,U,P_g)`, continuation de `U` pour `lambda!=0`, compatibilité des conditions aux limites, rang Dirac/tertiaires, K=0/J=0, lapses, 4D, stabilité et observables. La borne `|lambda|<=1/1000` est **uniquement** un tube de positivité g. Elle ne doit jamais être présentée comme un voisinage physique global certifié.

## Livrables
- `numerics/hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube.py` — blob `0def484f17d991bca4b482091d4e45711ec8d1b6`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube.py` — blob `bff1e9a18a48311ba8cb90502f73ce6b822deb53`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2a-gdust-parameter-tube.json` — blob `9b775de06f6a391c6817fa2bdb184e09d887ea76`.

**Prochaine étape 68ad-C2d2e5b3b2c2b :** exécuter les modules physiques originaux et le vrai `G` paramétré, certifier un tube de continuation pour f et une sensibilité, puis étudier les bords réellement admissibles et l'oracle Dirac original à six couples.

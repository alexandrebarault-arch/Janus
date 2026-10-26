# JANUS — Step68ad-C2d2a : adaptateur temporel original et correction d'un défaut de domaine par arrondi

Date : 2026-10-26. **Résultat de méthode et de sûreté numérique, PAS une certification temporelle.** Statut : `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Découverte vérifiable : les boîtes idéales C2b ne couvrent pas nécessairement les cellules réellement évaluées

Le moteur physique original Step68o utilise `R=I.hull(rlo,rhi)`, puis `si=R**2`, où `I` est une arithmétique entière à arrondi extérieur de pas `10^-28`. Les cellules C2b, construites avec `Fraction`, bornent initialement `s∈[rlo²,rhi²]` **avant** l'élargissement du moteur. Les frontières internes (ex. `1/56`, `9/448`) ne sont pas toutes représentables exactement sur le réseau `10^-28`. Le calcul `si=R**2` couvre donc parfois un intervalle légèrement plus large que la cellule rationnelle idéale. Injecter sans correction les boîtes C2b pourrait invalider une preuve d'inclusion rigoureuse, même si l'écart est minuscule.

**Contre-exemple exact exécuté** : pour `r∈[1/56,9/448]`, avec la fonction test lisse et monotone `U(s)=s`, l'extrémité supérieure réelle de `si` après arrondi satisfait `si.hi/10^28 > (9/448)^2`. La boîte idéale `[(1/56)^2,(9/448)^2]` ne contient donc pas l'évaluation du moteur. Ce contre-exemple est **numérique/formel sur l'interface d'intervalles**, pas une réfutation de la solution physique JANUS.

## Correction nouvelle, sans toucher les sources historiques

Le module `numerics/hr_step68ad_c2d2a_temporal_replay.py` :

1. vérifie les six SHA Git originaux attendus (Step55, Step58, Step60, Step68n, Step68o, C2b) dans un clone complet, puis exige les trois rapports physiques SHA-pinnés par `load_pinned()` ;
2. reconstruit **les bornes exactes U, U_s, U_ss, U_sss sur le vrai intervalle `si=I.hull(rlo,rhi)**2`**, en réappliquant le polynôme, la barrière cubique et la monotonie originaux via `validate_reports()` et `Q` de C2b ; rejette toute sortie du domaine `s≤1/1024` ;
3. convertit avec arrondi extérieur les quatre bornes rationnelles en `Jet([U,U_s,U_ss/2,U_sss/6])`, sans jamais diviser par `s` ;
4. injecte temporairement et **uniquement** ce jet dans `_ode_coeff` de Step68o par un contexte restauré automatiquement, puis appelle `evaluate_cell` ORIGINAL (donc les douze jets canoniques originaux et le Step58 `physical_operator()` non-frozen-shift) ; le contexte vérifie l'intervalle `si` et le nombre exact d'appels ;
5. refuse de qualifier un signe si son intervalle contient zéro : `INCOMPLETE`. Écrit un JSON seulement après les sept cellules. Ne revendique ni Step60 ni rang Dirac.

**Attention** : le module a été créé et ses invariants ont été testés, mais son `run()` exige un checkout complet avec les dépendances et n'a **PAS été exécuté** dans cette session. Aucune sortie `A_N/A_M` sur les sept cellules n'a été produite ; le vrai Step60 quotient reste à exécuter. Le champ `kind=EXECUTED_ORIGINAL_STEP58_NONFROZEN_SHIFT` n'apparaît que dans une sortie générée *après* exécution réussie de `run()`, pas dans le présent rapport.

## Tests réellement exécutés

`PYTHONPATH=/mnt/data/janus_c2d2a python -m pytest -q /mnt/data/janus_c2d2a/tests/test_hr_step68ad_c2d2a_temporal_replay.py` : **20 PASS, 0 FAIL (0,07 s)**. Ces tests utilisent des doubles locaux pour `I`, `Jet` et l'appel à `evaluate_cell` : arrondis extérieurs de fractions, conversion factorielle, injection/restauration, échec sur cellule inattendue, absence de faux signes, rejet de sources absentes ou altérées, couverture des sept cellules, garde `s≤1/1024`, contre-exemple de l'ancienne conversion. **Ils ne sont pas des tests d'exécution du vrai Step58/60**.

Code publié : `numerics/hr_step68ad_c2d2a_temporal_replay.py` — Git blob `6b68c33ceac7f1f1a890e0d61a938a9ddb23ea95` (identique aux octets locaux testés).
Tests publiés : `tests/test_hr_step68ad_c2d2a_temporal_replay.py` — Git blob `3dea95d2233ea23b5cbee2583a38ca5a9be16dba` (identique aux octets locaux testés).

## Prochaine action obligatoire : 68ad-C2d2b

Dans un checkout complet, avec SymPy/pytest et rapports physiques originaux, lancer :

```bash
PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2a_temporal_replay.py
PYTHONPATH=. python -m numerics.hr_step68ad_c2d2a_temporal_replay --repo . --out research/reports/gate2b-step68ad-C2d2b-original-temporal-seven-cells.json
```

Analyser les sept `N,M` obtenus : conserver `INCOMPLETE` dès qu'un intervalle traverse zéro. Si la dépendance d'intervalles bloque les signes, subdiviser ou employer une réduction analytique prouvée, **sans modifier les sources originales**. Ensuite évaluer le véritable quotient Step60 `A_M - z/Lf*C'` sur le même shell avec le shift prolongé et ses contraintes, et seulement alors discuter du rang/lapses/bords. Les conclusions de validation cosmologique et de fantôme BD demeurent ouvertes.

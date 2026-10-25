# JANUS — Étape 68l : resserrement RIGOUREUX ×100 du tube radial global original Step55

**25 octobre 2026 — branche exclusive `research/gate2b-nonhomothetic-transfer` ; GATE_2B OPEN, JANUS-R NOT_VALIDATED.**

## 1. Question scientifique

Le calcul temporel original Step58/60 est désormais réduit, sur les contraintes, à `dot C=A_N N+A_M M` (Step68j), mais la preuve d'un signe uniforme de `A_N,A_M` exige une maîtrise rigoureuse de la VRAIE branche radiale non homothétique Step55. Au lieu d'échantillonner encore le profil `U(s)`, nous avons réexécuté, avec un maillage rationnel renforcé, **l'authentique arithmétique dirigée** du certificat global spatial de Step55. Le même polynôme central **`Ustar=U0+U1*s+U2*s²`** est conservé, **sans utiliser** la correction supplémentaire `U3` de Step67b.

**Sources physiques originales identiques octet par octet aux blobs GitHub :**

- `numerics/hr_step45_exact_physical_ward.py` : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`
- `numerics/hr_step46_exact_secondary_ode.py` : `bac025c28dbe1561c0c36c56dbfda46dc326f804`
- `numerics/hr_step55_normalized_secondary.py` : `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`
- `numerics/hr_step55_global_barrier.py` : `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`

Le nouveau programme `numerics/hr_step68l_refined_global_barrier.py` REFUSE tout changement de ces quatre originaux et appelle leurs fonctions réelles `I,compiled,geometry,G,stars,residual` avec des **intervalles entiers à arrondi extérieur, échelle `10²⁸`**. Il ne reconstruit pas un autre modèle ni un solveur flottant.

## 2. Certificat intégral sur 16 384 intervalles rationnels

Sur `s=r² in [0,289/400]`, soit `r in [0,17/20]`, la VRAIE EDO physique est

[
2sU_s=G(s,U)-2U.
]

Pour `delta=1/1000000`, on teste sur **chacune** des 16 384 cellules fermées rationnelles les deux résidus du champ différentiel à travers les courbes `Ustar±delta` :

[
F_+(s)=G(s,U_*(s)+delta)-2(U_*(s)+delta)-2sU_*'(s),
]
[
F_-(s)=G(s,U_*(s)-delta)-2(U_*(s)-delta)-2sU_*'(s).
]

**Bornes uniformes rigoureuses après arrondis extérieurs sur le continuum :**

[
oxed{
F_+(s)le-rac{52329410075807340297}{78125000000000000000000000}<0,
}
]

[
oxed{
F_-(s)gerac{5825322396515812909051}{10000000000000000000000000000}>0.
}
]

Ainsi, en réutilisant **l'existence et l'unicité analytiques centrales de Step49** et le raisonnement de premier contact/continuation déjà démontré dans l'original Step55, la solution radiale régulière associée au centre ne peut quitter ces deux barrières, pour `s>0`.

[
oxed{
orall,0le rle0,85:quad |U(r^2)-U_*(r^2)|le10^{-6}.
}
]

La borne non stricte pour l'inclusion globale est le sens logique conservateur ; les barrières ont une stricte orientation vers l'intérieur et le centre est fixé par le polynôme.

**Amélioration quantitative 100×** par rapport au tube `|U-Ustar|≤10^-4` de Step55. Aucune hypothèse cosmologique nouvelle et aucune perturbation temporelle ne sont introduites.

## 3. Encadrement de la dérivée radiale normalisée V

Définition `V(s)=G(s,U(s))=pLf'(r)/r` sur cette branche. En reprenant la vitesse de référence `Vstar=2U0+4U1*s+6U2*s²` original Step55, les mêmes 16 384 cellules fournissent une *nouvelle* borne rigoureuse :

[
oxed{
-rac{106551452922242719145541}{5000000000000000000000000000}
le V(s)-V_*(s)
le
rac{212228180149451453699149}{10000000000000000000000000000}.
}
]

Ces fractions valent approximativement `-2.13103×10^-5` et `+2.12228×10^-5`, toutes deux à l'intérieur de `±1/20000=±5×10^-5`. Le certificat initial Step55 satisfaisait seulement `±0.01` avec ses propres valeurs atteintes d'environ `±0.00204`. La nouvelle enceinte de `V` est donc beaucoup plus étroite. Les plages strictement signées pour `V` lui-même sont archivées dans le JSON machine, sans arrondir leur contenu rationnel.

Par conséquent le tube positif de poussières et les signes de `J,K` déjà prouvés par Step54 restent applicables, avec **des hypothèses spatiales nettement mieux localisées**. Il ne s'agit pas d'une preuve nouvelle de stabilité du fantôme BD.

## 4. Contrôles négatifs et robustesse

Le **même code d'arithmétique extérieure** appliqué à `delta=10^-6` mais avec seulement **8 192 cellules** *REFUSE* le certificat : sur la première cellule, l'intervalle de `F_+` comprend zéro, parce que la sur-largeur de l'arithmétique d'intervalles n'a pas diminué assez. Ceci est un **échec de résolution**, pas un contre-exemple à la solution. Le nouveau certificat avec 16 384 cellules a, lui, strictement franchi toutes les cellules.

Contrôles réellement exécutés dans la suite : fidélité aux quatre Git blobs, refus d'un blob altéré, succès historique de 256 cellules à `delta=10^-4`, succès du certificat resserré de 16 384 cellules, bornes signées rationnelles, contrôle de `V`, et rejet des paramètres de preuve invalides.

### Reproduction

```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step68l_refined_global_barrier \
  > research/reports/step68l-refined-barrier-raw.json

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step68l_refined_global_barrier.py
# RÉELLEMENT : 8 passed in 39.18s
```

- **Code nouvellement exécuté :** `numerics/hr_step68l_refined_global_barrier.py` — Git blob `2a1ffc026a30abf41208b44a707dc869daf0929d`.
- **Tests nouvellement exécutés :** `tests/test_hr_step68l_refined_global_barrier.py` — Git blob `0b117a8e13cf0bd7344da4c31d0edcb3148c957e`.
- **Rapport original des 16 384 cellules, champs rationnels exacts :** `research/reports/gate2b-step68l-refined-global-barrier.json` — Git blob `b0e698809d0f89d1bc9e618d100e22f1241daced`.
- **Sortie de tests :** `research/reports/gate2b-step68l-pytest.log` — Git blob `d4fad6d097cdb8ae87bec90511c2c0e63eba9c2a`.

Les **quatre nouvelles empreintes GitHub ont été comparées avec les fichiers locaux et sont identiques octet pour octet**, terminal LF compris. Le certificat est exécuté localement, pas par GitHub Actions.

## 5. Le vrai verrou ne doit PAS être confondu avec ce résultat

Cette amélioration réduit très fortement les incertitudes de la branche SPATIALE, ce qui aide pour certifier les coefficients temporels `A_N,A_M`. Toutefois **aucune preuve de signes `A_N>0,A_M<0` sur tout le continuum n'a encore été produite**. Les 17 évaluations numériques positives de Step68f restent des indices ponctuels, et la famille homothétique analytique Step68k n'est pas la branche non homothétique actuelle.

Prochain travail (**Step68m**) : exploiter l'enceinte `Ustar±10^-6` et la vitesse dérivée `Vstar±5×10^-5` dans une évaluation par intervalles des véritables coefficients du vrai opérateur temporel original Step58, en conservant tous les jets de poussière et les dérivées radiales jusqu'aux ordres nécessaires. Il faudra analyser `r=0` séparément pour les facteurs `r²`, puis établir ou réfuter les signes `A_N,A_M`, la positivité `M/N`, les conditions aux bords et le rang. Enfin, oracle indépendant non intégré par parties sur six couples, et examen des cartes exceptionnelles `K=0,J=0`.

**VERDICT : Tube spatial continu certifié ×100 plus étroit ; GATE_2B OPEN — JANUS-R NOT_VALIDATED.**

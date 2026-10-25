# JANUS — Étape 68m : monotonie radiale positive certifiée de la solution originale Step55

**25 octobre 2026 — branche unique : `research/gate2b-nonhomothetic-transfer`. GATE_2B OPEN, JANUS_R NOT_VALIDATED.**

## 1. Dépendance vérifiée : le nouveau tube global Step68l

Le véritable problème radial non homothétique original Step45/46/55 a pour inconnue `U(s)=p_{L_f}(r)/r²`, avec `s=r²` et véritable EDO (pas une approximation de `U_*`) :

[
2sU_s=G(s,U)-2U.
]

Le certificat exact Step68l, utilisant 16 384 cellules d'arithmétique entière dirigée et les sources physiques originales vérifiées, vient de démontrer
[
|U(s)-U_*(s)|le10^{-6},qquad0le sle289/400.
]
Le programme de la présente étape `numerics/hr_step68m_positive_radial_slope.py` **authentifie à nouveau** les quatre sources Step45/46/55 et contrôle que le fichier certifiant Step68l possède exactement le Git blob `2a1ffc026a30abf41208b44a707dc869daf0929d`. Il **réexécute complètement** le certificat Step68l avant de conclure à la monotonie.

## 2. Nouveau théorème RIGOUREUX sur un anneau compact

Pour un intervalle rationnel fermé `s in [a,b]`, de `a>0`, définir, par les opérateurs entiers originaux `I`,
[
mathcal U(s)=U_*(s)+[-10^{-6},10^{-6}],
qquad
mathcal D(s)=rac{G(s,mathcal U(s))-2mathcal U(s)}{2s}.
]

Comme le véritable `U(s)` est inclus dans `mathcal U(s)` par Step68l, **le vrai `U_s(s)` est obligatoirement inclus dans `mathcal D(s)`** via l'EDO exacte. Sur **8 192 cellules rationnelles fermées**, recouvrant sans trous
[
rac1{64}le slerac{289}{400},
quad	ext{donc}quad
rac18le rlerac{17}{20},
]
l'arithmétique extérieure fournit les bornes uniformes

[
oxed{
rac{2616650086463031354471}{1250000000000000000000000000}
le U_s(s)le
rac{30880835985796069042583}{19531250000000000000000000}.
}
]

La borne inférieure vaut environ (2{,}09332	imes10^{-6}) et est **strictement positive**, et la borne supérieure vaut environ (1{,}58110	imes10^{-3}).

**CONCLUSION EXACTE :**
[
oxed{U_s(s)>0quadorall sin[1/64,289/400].}
]

Le certificat porte sur **tous les rayons** de cet anneau, pas sur 8 192 rayons échantillonnés. Les intervalles des cellules sont fermés, y compris leurs points de jonction, et la borne est dirigée vers l'extérieur.

## 3. Limites logiques explicitement préservées

L'équation `U_s=(G-2U)/(2s)` n'est directement utilisable en arithmétique d'intervalles que pour `s>0`. La présente étape **NE PROUVE PAS** cette monotonie sur `0<s<1/64` (équivalent à `0<r<1/8`). Les coefficients Taylor du centre Step67b établissent notamment `U_s(0)=U1>0` et un voisinage positif par continuité analytique, mais ne comblent PAS rigoureusement l'intervalle intermédiaire avec une borne explicite.

Cette propriété SPATIALE de `U` sert à contrôler les jets physiques et à préparer le calcul par intervalles des coefficients temporels d'ordre zéro. Elle **n'implique PAS** `A_N>0,A_M<0` ni la positivité du rapport temporel `M/N`, le rang de Dirac, l'absence de fantôme BD ou les prédictions 4D. Les 17 rayons Step68f restent seulement exploratoires pour les lapses.

## 4. Reproductibilité

- `numerics/hr_step68m_positive_radial_slope.py` authentifie les sources historiques et le code Step68l, recalcule la barrière ×100, puis vérifie **tous** les résidus inférieurs strictement positifs.
- `tests/test_hr_step68m_positive_radial_slope.py` contrôle la provenance, le certificat positif, le refus des paramètres hors charte, la non-extension abusive au centre, et un contre-test où le maillage grossier ne certifie pas le signe.

Commande de calcul :

```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step68m_positive_radial_slope
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step68m_positive_radial_slope.py
```

Voir le résultat brut, les empreintes de code et tests, et les sorties de pytest dans les fichiers `research/reports/gate2b-step68m-*`. Les tests doivent être distingués de la preuve par intervalles elle-même : ils vérifient des invariants et des contrôles négatifs du calcul exécutable.

## 5. Prochaine étape utile

**Step68n** : construire les jets spatiaux complets de la solution U(s) avec propagation d'intervalles/AD du véritable `G(s,U)` et intégrer les cinq couples de contraintes à l'évaluation des coefficients `A_N,A_M` de l'opérateur temporel ORIGINAL Step58. Le secteur `r	o0` demande une normalisation centrale spécifique afin d'éviter la division par `s`. Il faut alors certifier ou réfuter les signes `A_N>0,A_M<0` sur le **vrai continuum non homothétique**, déterminer `M/N` et son comportement aux bords, et réaliser l'oracle non-IBP indépendant.

**VERDICT : monotonie stricte de U(s) certifiée sur [1/64,289/400] ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

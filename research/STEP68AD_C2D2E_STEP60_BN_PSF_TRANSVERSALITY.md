# JANUS — 68ad-C2d2e : transversality exacte et conditionnelle de Step60 `B_N` en `pSf`

**26 octobre 2026 — recherche limitée à `research/gate2b-nonhomothetic-transfer`.**

## Théorème algébrique exact (pas une preuve de `B_N=0`)

Soit `B_N` le représentant original `full_constraint_prolongation()['third_free_BN_on_Fz']` de Step60 (SHA original `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`), sur la coquille de stationnarité `F_z=0` où `pLg'` a été éliminé conformément à Step58/60. En gardant les autres jets canoniques indépendants et en considérant `pSf` comme variable libre, la dérivation symbolique exacte établit

`d² B_N / d(pSf)² = 0`, et `J := d B_N / d(pSf)` ne dépend pas de `pSf`.

Donc **`B_N = B_0 + J pSf`** (où `B_0` désigne ici l'ordonnée à l'origine du représentant, et non le paramètre d'interaction `beta0`). Cette identité ne suppose PAS que le profil radial est solution des équations temporelles.

## Certification continue conditionnelle

Sur la branche spatiale originale Step68o, sous les hypothèses `r>0`, `Lg>0`, `K>0`, stationnarité du shift, poussières et jets originaux contraints par les trois rapports SHA-pinnés Step68v, Step68ac, Step68ad-B2, une différentiation automatique d'intervalles (arrondi extérieur `10^-28`) donne une borne de `dJ/dr` sur chaque sous-cellule. Pour `m=(a+b)/2`, `h=(b-a)/2`, le théorème des accroissements finis certifie

`J([a,b]) ⊆ J(m)+[-h,h]·J'([a,b])`.

Les sept cellules de `[1/64,1/32]` ont été subdivisées en 32 sous-cellules rationnelles chacune : **224/224 bornes supérieures de `J` strictement négatives**. Plus grande borne supérieure exacte :

`-345763471741167637281851/312500000000000000000000000` (environ `-0.0011064431095717364`).

Plus petite borne inférieure exacte :

`-45183603720227163110391799/10000000000000000000000000000` (environ `-0.004518360372022716`).

Ainsi, **`J(r)<0` sur le continuum `[1/64,1/32]`**, sous les hypothèses indiquées. Le signe concerne la dérivée PARTIELLE du représentant Step60 par rapport à `pSf`, **pas le signe de `B_N`**, ni un lapse, ni le rang du système Dirac.

L'évaluation indépendante de l'expression originale Step60 avec une perturbation `ΔpSf=1/10000` au point `r=1/48` confirme la variation négative et son intersection avec `ΔpSf·J`. Ceci fournit un contre-exemple à l'affirmation universelle `B_N≡0` dans le voisinage canonique non contraint ; une éventuelle identité **sur la coquille physique complète** reste ouverte.

## Audit de l'hypothèse `B_N=0` sur la solution radiale

Des diagnostics numériques à précision accrue (28, 50, 80 décimales fixes, opérateur Step60 inchangé mais **précision de l'arithmétique expérimentale modifiée temporairement**) donnent des intervalles contenant zéro, de demi-largeur typique `10^-15`, `10^-37`, `10^-67` selon la précision. Ce comportement **suggère** une annulation exacte lorsque les contraintes spatiales sont imposées, mais n'en constitue pas une démonstration. Une tentative `sympy.cancel` après substitution complète a dépassé 130 secondes et a été arrêtée ; **aucune preuve exacte de `B_N=0` sur la coquille n'est revendiquée**.

Le fait que `J<0` rend au contraire pertinente la recherche de la racine unique `pSf*=-B_0/J` à jets canoniques restants fixés ; la prochaine étape devra comparer symboliquement `pSf*` au `pSf` physique Step68o, sans extrapoler les échantillons.

## Reproductibilité et non-régression

Sources et rapports physiques importés depuis GitHub à `HEAD=155be7f5f486388ca4a75a4c5032aacea99bdb9f`, puis recalcul des Git blob SHA sur **24/24 fichiers** (17 sources initiales, quatre dépendances transitives, deux tests historiques et un certificat historique). Les originaux Step45, Step58, Step60, Step68o et les trois rapports physiques sont inchangés. Leurs contrôles internes d'authenticité sont exécutés par le nouveau certificat.

Commandes effectivement exécutées depuis la racine du dépôt de calcul :

- `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e_bn_psf_transversality --repo . --out research/reports/gate2b-step68ad-C2d2e-Step60-BN-pSf-transversality.json` → 224 sous-cellules, `J<0` partout.
- `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e_bn_psf_transversality.py tests/test_hr_step68ad_c2d2d_correlated_mean_value.py tests/test_hr_step60_full_constraint_prolongation.py` → **34 PASS, 0 FAIL** (13 nouveaux tests + 21 tests historiques de non-régression).

Les premières tentatives avec de trop grandes cellules ont produit des intervalles traversant zéro ou des divisions par des intervalles contenant zéro : ce sont des **résultats INCOMPLETE**, pas des singularités physiques. Les tests ont été ajustés pour ne jamais faire passer ces domaines non certifiés pour des certificats ; la partition finale 7×32 passe. Le certificat JSON contient les 224 paires rationnelles et les SHA des sources physiques.

## Limites et décisions

- `B_N=0` sur la solution physique : **NON PROUVÉ** ; aucun signe continu de `B_N` certifié.
- Step60 `A_M<0` sur les sept cellules : résultat conditionnel antérieur préservé.
- Step58 `A_N/A_M` sur le continuum : **INCOMPLETE**.
- Rang complet des contraintes de Dirac, existence de lapses admissibles, conditions aux limites, dynamique 4D, stabilité, observables : **NON DÉMONTRÉS**.
- `GATE_2B OPEN`, `JANUS_R NOT_VALIDATED`.

**Prochaine étape : `68ad-C2d2e2`** — factoriser le représentant original `B_N` en fonction des contraintes spatiales, comparer exactement la racine `pSf*` au profil Step68o, puis traiter les coefficients Step58 par enclosures corrélées. Aucun commit de convenance ou validation cosmologique n'est justifié.

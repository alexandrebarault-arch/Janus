# JANUS — Étape 51 : sources historiques exactes, coefficient central haute précision et bilan des branches

**Date : 22 octobre 2026.** Seule branche de recherche écrite : `research/gate2b-nonhomothetic-transfer`. **État final : Gate 2B OUVERT, JANUS-R NON VALIDÉ.**

## 1. Ce qui a réellement été fait sur GitHub pour la demande « une branche »

Les pointes historiques `main` (`aead63f4...`) et `research/v2-flrw` (`dfa497cc...`, 203 commits divergents à l'origine) ont été **préservées dans l'ascendance** de la branche JANUS active par le commit à deux parents `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7`, **sans changer son arbre de fichiers**. Les comparaisons GitHub des deux anciennes branches vers l'active donnent `behind=0` : l'ancien historique est récupérable sans garder ces refs à long terme.

L'ancienne pull request de recherche V2 [#1](https://github.com/alexandrebarault-arch/Janus/pull/1) a été **fermée via le connecteur GitHub, SANS FUSION** (`state=closed`, `merged=false`). Elle ne bloque plus le ménage.

**Limite administrative effective et contrôlée :** GitHub indique toujours `default_branch=main` et la liste de **TROIS branches** `main`, `research/gate2b-nonhomothetic-transfer`, `research/v2-flrw`. Le connecteur disponible donne des actions d'écriture de fichiers/commits/refs avancées, mais **aucune action de suppression de ref ni de modification de la branche par défaut**. Il est impossible d'achever ces deux opérations par cet accès. Ne PAS prétendre « une seule branche » à ce stade.

Pour terminer sans perdre un seul commit, le propriétaire doit effectuer dans **GitHub UI** :

1. Dans **Settings > General > Default branch**, choisir `research/gate2b-nonhomothetic-transfer`.
2. Dans **Branches**, supprimer `research/v2-flrw` puis `main`. Changer le défaut AVANT de supprimer `main`.
3. Vérifier que GitHub n'affiche qu'une branche. L'historique V2 reste inclus dans le commit de préservation.

Le fichier [`research/BRANCH_CONSOLIDATION_2026-10-22.md`](BRANCH_CONSOLIDATION_2026-10-22.md) conserve les références SHA, la vérification du tree invariant, le sort de la PR et les instructions.

## 2. Progrès scientifique véritable — reprise depuis des sources originales vérifiées

L'étape 49 avait démontré conditionnellement la régularité analytique locale du problème de Cauchy normalisé (P(r)=p_{L_f}(r)=r^2 U(s)) près de (s=r^2=0) et donné une estimation numérique du premier coefficient (U_1), mais plusieurs dépendances locales étaient des adaptations mathématiques, non les fichiers historiques exacts. Étape 51 :

- `numerics/hr_step45_exact_physical_ward.py` reconstitué **octet pour octet** depuis GitHub, Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` reconstitué **octet pour octet**, blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
- Ces fichiers fournissent le **noyau Poisson original sphérique à six couples canoniques** et son élimination exacte des poussières f permettant de former le second membre `pLf_prime_rhs=-C0/C1`. Le nouveau calcul refuse un hash historique modifié (mode fail-closed). **Les autres dépendances Step45-secondary/Step47/48 ne sont pas reconstituées ici bit-identical** ; ne pas annoncer la levée des deux tests Step48 laissés en attente.

Avec la calibration décimale rationnelle de référence, les données prescrites sphériques courbes (L_g=a(1+c_g r^2)^2), (L_f=ay(1+c_f r^2)^2), (z=z_1r), deux phases non comobiles (	heta'_g=k_g rL_g), (	heta'_f=k_f rL_f), et les deux contraintes primaires g reconstruites algébriquement, le calcul original de l'étape 46 donne la quantité
[
G(s,U_0)=rac{p'_{L_f}(sqrt{s};,p_{L_f}=sU_0)}{sqrt{s}},
quad
U_0=M_f^2 bleft(rac{P_g}{M_g^2a}-2z_1ight).
]
Si (G(s,U)) est analytique dans la charte non dégénérée (hypothèse du théorème local de Step49), on a EXACTEMENT en formalisme
[
oxed{U_1=rac15partial_sG(0,U_0).}
]

Le nouveau programme évalue cette dérivée par différences de quotients à **100–120 chiffres mpmath**, pour des rayons (r=10^{-k}), avec `k=7,8,9,10,11`, et une élimination de l'erreur principale en (O(r^2)) par extrapolation à deux rayons. L'usage de `mpmath` évite l'annulation catastrophique de double précision à très petit rayon. Les valeurs à 120 chiffres sont :

| (r_1,r_2) | (U_1) extrapolé (affichage abrégé) |
|---|---|
| (10^{-7},10^{-8}) | 0.0007897451667202464909325108904961684261 |
| (10^{-8},10^{-9}) | 0.0007897451667202464909325108904961683602 |
| (10^{-9},10^{-10}) | 0.0007897451667202464909325108904961683602148125 |
| (10^{-10},10^{-11}) | 0.0007897451667202464909325108904961683602148118 |

**Nouvelle référence haute précision (non certifiée)**
[
oxed{hat U_1=0.00078974516672024649093251089049616836021481ldots}
]
L'ancienne estimation double de Step49 `0.0007897451669079507` était plus grande d'environ `1.8770420906748911e-13`, un écart minuscule en valeur absolue, mais important pour les contrôles au centre sensibles au mode (1/r).

**Portée stricte :** Les rapprochements numériques haute précision et l'extrapolation Richardson **NE SONT PAS une preuve** de la limite ni un encadrement mathématique rigoureux de (U_1). Aucune solution globale validée de l'EDO sur ([0,.85]), aucune positivité continue des deux poussières, ni aucune conservation temporelle de la contrainte ({C,H_{m tot}}) ne découlent de ces chiffres.

## 3. Sources et tests réellement exécutés

Nouveaux fichiers GitHub, empreintes de blobs **égales octet pour octet aux fichiers exécutés en local** :

- `numerics/hr_step51_highprecision_center_coefficient.py` — `97fe8f78a5daa91a8c74b14382470857c9ce29e2` ;
- `tests/test_hr_step51_highprecision_center.py` — `da85a6e4da8c7202da6d1d5e81fd1aeb8a964e3e`.

Exécuté depuis `/mnt/data/janus-step51` avec les deux vrais fichiers historiques Step45/46 :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step51_highprecision_center.py
# 7 PASSED in 1.85 seconds.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step51_highprecision_center_coefficient
```

Les tests comparent l'empreinte Git des sources historiques et refusent une modification, examinent la stabilité entre deux paires d'échelles radiales et deux précisions de 80 et 120 chiffres, protègent les domaines invalides et conservent `Gate2B=OPEN`. Une première assertion utilisait des valeurs flottantes trop voisines au niveau d'arrondi IEEE ; elle a été **corrigée pour comparer les chaînes haute précision via `Decimal`**, puis la suite de 7 tests a réussi. Pas de suite entière du dépôt, pas de CI (actions désactivées), pas de deux tests Step48 pleine provenance.

Le JSON brut a été effectivement écrit en local : `/mnt/data/janus-step51/research/reports/step51-local-raw.json`, SHA256 `5a9bcd471ed31fcc8c1ef6e05e0efc58aab8b7b450318652c263c5c08326cd3e`. Les valeurs principales et les commandes sont enregistrées dans `research/reports/gate2b-step51-report.json` sur GitHub ; le brut n'est pas un fichier GitHub autonome.

## 4. Reprise scientifique Step52 — véritables verrous

1. **Dériver un (U_1) symbolique algébrique exact ou un encadrement rationnel par série tronquée à reste rigoureux**, plutôt que d'accumuler des extrapolations de petits rayons. Garder l'expression (partial_sG(0,U_0)/5) et les sources Step45/46 byte-authentiques.
2. Rassembler **toutes** les sources historiques exactes Step45/46/47/48, relancer les deux tests Step48 précédemment désélectionnés et vérifier les hachages Git. Ce point demeure OPEN.
3. Étendre la solution initiale régulière par méthode ODE *validée* jusqu'à (.85), démontrer les deux poussières strictement positives **sans échantillonnage seulement**, et conserver toutes marges de chartes.
4. Calculer la vraie préservation temporelle ({C,H_{m tot}}) des six couples canoniques, déterminer les lapses et le rang Dirac incluant (J/K=0), le centre et les bords, sans induire une prétendue élimination du fantôme BD de la seule équation radiale.
5. L'évolution cosmologique réellement non homothétique et les tests de stabilité De Felice/Aoki ne viennent qu'après ces preuves.

**Verdict final : branche JANUS active intègre tous les commits historiques et ancienne PR est fermée ; deux suppressions/admin GitHub restent à effectuer ; coefficient (U_1) mieux déterminé NUMÉRIQUEMENT avec sources Step45/46 authentifiées ; Gate 2B OUVERT, JANUS-R NON VALIDÉ.**

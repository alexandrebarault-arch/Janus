# JANUS — Étape 50 : contrôle croisé du solveur radial et préservation des trois historiques Git

**Date : 22 octobre 2026.** Branche active : `research/gate2b-nonhomothetic-transfer`. **Statut scientifique : nouveau contrôle numérique passé, mais Gate 2B toujours ouvert ; JANUS-R non validé.**

## 1. Consolidation de l'historique demandée par l'utilisateur

Le dépôt avait réellement **trois branches** : `main` (défaut), `research/gate2b-nonhomothetic-transfer` (travail JANUS actuel) et `research/v2-flrw` (ancienne branche). Leur état a été inspecté par GitHub. `main` était déjà ancêtre de la branche active, mais `research/v2-flrw` possédait **203 commits distincts**.

Pour protéger cet historique avant suppression de branches, un commit **sans modification de l'arbre des fichiers** a été créé sur la branche active :

- **Commit à deux parents** : `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` ;
- premier parent : `9c629156c8e05d7149421404490b2d77650b45e3` (branche active) ;
- second parent : `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` (branche historique V2) ;
- arbre Git **strictement inchangé** : `e5da02813be6b378398520d9d129209fc5caf5c2`.

GitHub confirme **behind=0** pour chacune des deux anciennes pointes (`main` et `research/v2-flrw`) lorsque comparées à la branche active : leurs commits sont maintenant accessibles dans l'ascendance active. **Aucun fichier scientifique V2 n'a été réintroduit dans la version Step49.** L'ancien projet V2 n'a pas été validé simplement parce que son historique est rattaché.

**IMPORTANT :** Les trois noms de branches existent **toujours** sur GitHub, puisque le connecteur utilisé dans cette conversation ne propose ni modification de la branche par défaut ni suppression de branche. Ces actions doivent être réalisées dans les paramètres GitHub :

1. Configurer `research/gate2b-nonhomothetic-transfer` comme **branche par défaut** dans les paramètres du dépôt ;
2. Fermer l'ancienne [PR brouillon #1](https://github.com/alexandrebarault-arch/Janus/pull/1) (base `main`, tête `research/v2-flrw`) sans fusionner ses sources ;
3. Supprimer les refs `research/v2-flrw` et `main` via la page Branches, **après** modification de la branche par défaut ;
4. Vérifier qu'il ne reste qu'une seule branche.

Le plan exact et les pointes historiques sont stockés dans `research/BRANCH_CONSOLIDATION_2026-10-22.md`. Ne PAS annoncer « une seule branche » avant la suppression effective.

## 2. Contrôle numérique supplémentaire de l'équation radiale exacte

Les étapes 45–46 ont dérivé analytiquement, à partir des six couples canoniques du Hamiltonien sphérique original, l'équation (p'_{L_f}=-C_0/C_1). L'étape 49 a démontré, **conditionnellement** à l'analyticité des données imposées, l'existence et l'unicité locales d'une solution régulière en (r=0), puis réalisé un tir numérique de cette condition vers (r=0{,}85).

L'étape 50 confronte cette même construction à trois méthodes de résolution **différentes** :

- Runge–Kutta adaptatif RK45 ;
- Runge–Kutta d'ordre supérieur DOP853 ;
- méthode implicite Radau.

Toutes partent à (epsilon=0{,}00625) avec (p_{L_f}(epsilon)=U_0epsilon^2+hat U_1epsilon^4), où (hat U_1approx0{,}0007897451669079507) reste une **estimation** issue de Richardson, non un coefficient exact certifié. Paramètres : `rtol=2e-11`, `atol=1e-17`, pas maximal `0.012`, contrôle de **2 049 rayons** sur ([0{,}01;0{,}85]).

| Solveur | Évaluations RHS | (p_{L_f}(0,85)) | (min_{m échantillons} p_f/r^2) |
| --- | ---: | ---: | ---: |
| RK45 | 824 | −0.003386429356487892 | 0.11186483299522024 |
| DOP853 | 1376 | −0.0033864293564879015 | 0.11186483299522028 |
| Radau | 2647 | −0.0033864293564881253 | 0.11186483299522033 |

L'écart maximal sur **l'ensemble de la trajectoire échantillonnée**, par rapport à RK45, est (approx4{,}02	imes10^{-14}) pour DOP853 et (approx4{,}07	imes10^{-14}) pour Radau. Pour les trois solveurs, (min_{m échantillons}p_g/r^2approx0{,}8856008128827202), et le résidu secondaire substitué algébriquement est inférieur à (3{,}8	imes10^{-14}).

**Ces vérifications restent purement NUMÉRIQUES.** Les trois méthodes partagent la **même** équation reconstruite et les mêmes sources mathématiques ; leur accord ne constitue ni un oracle indépendant de l'action non intégrée (celui de Step48 était séparé), ni une estimation rigoureuse de l'erreur globale. Les minima des poussières couvrent 2 049 points, **pas tout le continuum**. Le petit (C) découle de la résolution par construction de l'équation (C=0), et ne prouve pas la préservation temporelle ({C,H_{m tot}}).

## 3. Tests exécutés et provenance

Fichiers NOUVEAUX publiés et byte-identiques à leurs fichiers exécutés :

- `numerics/hr_step50_solver_crosscheck.py` — blob `608222f9071c217d477951c8ed1ae81f5507b095` ;
- `tests/test_hr_step50_solver_crosscheck.py` — blob `c96c44c24a5b2a9293d127a77e99dadd6c629125`.

Exécutés dans `/mnt/data/janus-step50` :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step49_regular_center_shoot.py \
 tests/test_hr_step49_analytic_center.py \
 tests/test_hr_step50_solver_crosscheck.py
# 29 PASSED en 6,09 s : 21 Step49 + 8 Step50.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step50_solver_crosscheck
```

**Restriction de provenance non levée :** dans cet environnement local, plusieurs modules historiques Step45/46/47 restent des reconstitutions mathématiques/adaptateurs et ne sont pas des copies byte-identiques GitHub. Les **deux tests de Step48 dépendant de la chaîne authentique** n'ont PAS été réussis pendant cette exécution. Ceci n'est ni une régression complète du dépôt ni une exécution de GitHub Actions (désactivés).

Le JSON détaillé local `/mnt/data/janus-step50/step50-solver-crosscheck-local.json` a SHA256 `a0c76ddc29560df063ba3b83e63e57a3ef4d9becc912d4f37775cc08ed039a45`. Les principales valeurs figurent dans `research/reports/gate2b-step50-report.json`, enregistré sur GitHub. Le JSON local brut n'est pas ajouté comme fichier distinct.

## 4. Reprise sans interruption : étape 51

1. **Consolidation GitHub UI** : effectuer le changement de branche par défaut et la suppression des refs après vérification du commit de préservation, puis constater une seule branche effective.
2. **Authentification des calculs historiques** : réunir dans le même environnement toutes les sources GitHub exactes des étapes 45–49 et relancer intégralement les tests de Step48 non exécutés, sans adaptateurs.
3. **Certificat de continuation globale** : dériver un coefficient (U_1) exact ou à intervalle rigoureux, puis employer intégration d'EDO validée par intervalles ou borne spectrale a posteriori pour contrôler la continuation régulière sur (rin[0,0{,}85]), les deux densités de poussières et les dénominateurs du système.
4. **Véritable verrou théorique** : calculer la conservation temporelle de la contrainte secondaire avec tous les six couples canoniques, le rang de Dirac, la fixation des lapses et les secteurs exceptionnels (J/K). Ne pas affirmer que le fantôme de Boulware–Deser est éliminé sur la base des seuls calculs radiaux.

**Verdict : un historique Git réunifié dans une branche active et un contrôle à trois solveurs réussi, mais les refs excédentaires ne sont pas supprimées ; Gate 2B reste OUVERT et JANUS-R NON VALIDÉ.**

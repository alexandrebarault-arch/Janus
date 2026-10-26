# JANUS — 68ad-C2d2e5b2 : oracle à six couples non-IBP versus IBP, hors coquille

26 octobre 2026. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Il s'agit d'un contrôle numérique de convergence, **pas** du rang complet de Dirac.

## Provenance et méthode

Trois fichiers physiques originaux ont été relus via le connecteur GitHub sur `research/gate2b-nonhomothetic-transfer` : `hr_step37_original_nonibp_oracle.py` (blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`), `hr_spherical_mixed_hamiltonian_bracket.py` (blob `6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`) et `hr_spherical_adm_primary.py` (blob `c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`). Leurs **formules** ont été reconstruites indépendamment dans un programme Python autonome, mais les modules originaux **n'ont pas été importés ni exécutés**. Les 12 champs canoniques sont les polynômes du benchmark `default_fields` de la source IBP, sans identification des deux poussières.

Sur quatre maillages uniformes `n=41,81,161,321`, `r∈[0.1,0.9]`, calcul des deux densités ADM courbées **avant intégration par parties** avec `R_3`, `pLg'` et racine algébrique `z*=D/sqrt(K²+D²)` sur la charte `K>0`. Les douze dérivées discrètes des actions `H_g[N]`, `H_f[M]` sont obtenues par pas complexe `1e-21` sur **chaque noeud intérieur**, puis six contributions canoniques du crochet. Calcul indépendant du crochet des actions IBP avec `z'`, `N'`, `M'` et le même schéma, sans imposer la coquille. Les fonctions test `N,M` sont compactes sur `[0.2,0.7]`.

## Résultats mesurés (numériques, non certificats d'intervalles)

| n | crochet original | crochet IBP | différence |
|---:|---:|---:|---:|
| 41 | 0.04406642354880436 | 0.03544757475454052 | 0.00861884879426384 |
| 81 | 0.04382138009906760 | 0.04160021783705362 | 0.00222116226201398 |
| 161 | 0.04375925289385715 | 0.04319972683180122 | 0.00055952606205594 |
| 321 | 0.04374366606848031 | 0.04360351853125577 | 0.00014014753722454 |

La différence décroît d'environ un facteur 4 par doublement du maillage, ce qui est compatible avec une erreur de discrétisation quadratique. Les six contributions sont évaluées ; les deux paires de poussière sont conservées, même si la contribution de la paire `tf,pf` est numériquement nulle dans **ce benchmark particulier**. La stationnarité `F_z=0` est vérifiée numériquement à `≤2.8e-17`. En gelant le shift à sa racine de fond **uniquement lors des variations des actions bulk**, le crochet change de moins de `7e-15`, contrôle numérique de la règle de l'enveloppe. Cela ne permet PAS de geler `z*` dans la variation du terme de bord.

Pour `N=M=1` aux extrémités, les contributions de bord ne s'annulent pas : les sauts séparés `B_g≈2.05424226`, `B_f≈0.63793473` sur le maillage fin. Les différences d'actions non-IBP/IBP convergent vers ces sauts ; les résidus trapézoïdaux maximaux décroissent approximativement comme `2.50e-5,6.21e-6,1.54e-6,3.85e-7` (n=41,81,161,321). Cela renforce l'avertissement de C2d2e5a/b1 : ne pas effacer les flux non compacts. **Aucune obstruction physique définitive** n'en découle sans conditions aux bords.

## Tests et limites

`cd /mnt/data/janus_e5b2 && python -m unittest -v test_hr_step68ad_c2d2e5b2_six_pair_crosscheck.py` : **12 tests PASS, 0 FAIL**. Contrôles : six paires, poussières, résidu du shift, rejet explicite de la charte K≤0, flux compacts/non compacts, convergence de l'action et du crochet, contributions individuelles, enveloppe du shift, refus d'attribuer un rang Dirac fictif. `python oracle.py > report_raw.json` a calculé le tableau complet avant renommage ; le module renommé est octet-identique à celui testé hors nom de fichier.

**NON PROUVÉ :** cohérence sur la vraie solution Step55/68o, conditions aux limites globales, matrice complète des contraintes primaires/secondaires et son rang, tertiaires, chartes K=0/J=0, dynamique 4D, stabilité et observables. Le crochet mixte hors coquille non nul ne prouve ni ne réfute l'absence du mode de Boulware–Deser.

**Prochaine étape effective 68ad-C2d2e5b3 :** injecter les profils physiques Step55/68o dans l'oracle original, confronter les dérivées fonctionnelles et les termes de bord, puis construire la matrice complète de Poisson/Dirac avec contraintes tertiaires et conditions aux bords, y compris chartes singulières.

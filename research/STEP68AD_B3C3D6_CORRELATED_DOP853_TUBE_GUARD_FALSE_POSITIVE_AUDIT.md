# JANUS b3c3d6 — audit de corrélation du tube DOP853 (30 octobre 2026)

**Statut : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Audit du code réellement lu sur la branche recherche ; ce résultat est un **correctif de validité logique du contrôle d'appartenance au tube**, pas un certificat de défaut continu physique.

## Défaut identifié dans l'adaptateur précédent

Dans `numerics/hr_b3c3d6_dop853_dense_rational_defect.py`, le garde `physical_step55_dense_defect` utilisait des enveloppes séparées `P([a,b])=[p_lo,p_hi]` et `Ustar([a,b])=[u_lo,u_hi]`, puis vérifiait seulement `p_lo >= u_lo-delta` et `p_hi <= u_hi+delta`. Ces deux inégalités ne prouvent **pas** `|P(s)-Ustar(s)|<=delta` pour chaque même `s` : elles testent une inclusion dans l'enveloppe **globale** du centre mobile, sans conserver la corrélation de l'abscisse.

**Contre-exemple exact jouet :** sur `s in [0,1]`, `Ustar(s)=s`, `P(s)=1/2`, `delta=1/100`. L'ancien garde accepte `[1/2,1/2] subset [-1/100,101/100]`. Pourtant `P(0)-Ustar(0)=1/2`, et `P(1)-Ustar(1)=-1/2` : le tube est violé d'un facteur 50. Ce contre-exemple ne porte pas sur le profil physique Step55, mais **réfute la suffisance mathématique de l'ancien garde**.

## Correctif exact et intégration

Nouveau module `numerics/hr_b3c3d6_correlated_tube_guard.py` : reconstruire dans **la même variable polynomiale** `x=(s-t_old)/h` le polynôme rationnel `D(x)=P(x)-[U0+U1(t_old+h*x)+U2(t_old+h*x)^2]`. Les coefficients `U0,U1,U2` sont des **intervalles rationnels sortants**, convertis depuis les entiers `I.lo,I.hi` de Step55, sans substitution de décimaux centraux. La composition affine vers chaque vraie sous-cellule `[a,b]` et la conversion puissance→Bernstein sont effectuées par opérations exactes `Fraction` sur coefficients intervalles. Si **tous** les coefficients Bernstein sont dans `[-delta,delta]`, alors `|P(s)-Ustar(s)|<=delta` sur cette cellule, pour toute réalisation des coefficients du centre dans les intervalles fournis. L'algorithme peut rejeter un candidat pourtant valide (enclosure trop large), mais ne peut accepter le contre-exemple ci-dessus.

`physical_step55_dense_defect_correlated` vérifie **chaque** sous-cellule sur le vrai domaine binary64 `xmax=(t-t_old)/h` avant de calculer les enveloppes sortantes du défaut physique par le moteur Step55 original. L'adaptateur global `numerics/hr_b3c3d6_global_piecewise_defect_budget.py` appelle maintenant **ce garde corrélé**, et non l'ancien garde insuffisant. L'ancien helper est laissé intact pour traçabilité, mais il ne doit plus servir à valider un tube physique. Aucun assouplissement de seuil n'est appliqué.

## Exécutions, provenance et limites

Dix `unittest` rationnels **réellement exécutés** dans `/mnt/data/janus_correlated` : **10 PASS, 0 FAIL** ; `python -m compileall -q numerics tests` : **PASS** sur le nouveau module et ses tests. Le contre-exemple vérifie explicitement que l'ancien prédicat passe et que le nouveau rejette. Tests de polynôme identique, décalage constant, incertitude sur le centre, polynôme quadratique et vraie borne `xmax`, cellules multiples, erreurs d'entrée. Ce sont des tests du garde mathématique, **pas** un rejeu des cinq moteurs physiques. Les blobs Git correspondant exactement aux octets locaux testés sont :
- `numerics/hr_b3c3d6_correlated_tube_guard.py` : `3801625ac5cb0a7681ade369f4c28b761bab73eb`.
- `tests/test_hr_b3c3d6_correlated_tube_guard.py` : `1a7a2a9d38d3be79e381f4c81ead38143dbcd23d`.
- Adaptateur global modifié : `numerics/hr_b3c3d6_global_piecewise_defect_budget.py` : `5fc0572021a98d6d5fe3127293baf023c286d9f4`. **Son chemin intégré physique n'a pas été exécuté ici.**

**AUCUN** résidu continu `R_i` physique, saut `J_i` physique, erreur initiale `E0`, transport terminal, enclosure des six coefficients A/B/E, BVP de lapses strictement positifs aux deux vrais bords, ni Dirac/4D/stabilité/observables n'est certifié par ce correctif. Le lemme global précédent demeure **conditionnel**, et son utilisation physique exige désormais la nouvelle preuve corrélée sur toutes les cellules, le certificat `G_U<=0` sur le tube partagé et la fermeture de `E0`.

**Prochaine action scientifique :** matérialiser et SHA-vérifier les cinq originaux Step45/46/55/58, exécuter le Step55 DOP853 original avec `dense_output=True`, lancer l'adaptateur global corrigé, enregistrer le premier échec éventuel de cellule (sans le masquer), calculer défaut continu et sauts, puis traiter `E0` et la propagation Step58. En cas d'échec d'enclosure, raffiner rigoureusement la cellule ou changer la forme d'évaluation, sans déduire que la solution physique sort du tube. Aucune modification de `main`, `research/v2-flrw` ou des workflows.

# JANUS — b3c3d6, audit contradictoire du rang ponctuel (PARTIEL)

28 octobre 2026. **Théorème exact sur deux opérateurs jouets, NON sur l'opérateur Step58.** Le but est d'écarter une inférence illégitime : `B_N,B_M` non tous nuls et projection des jets ponctuels de rang 2 ne garantissent pas la compatibilité globale de lapses positifs avec les deux bords. `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Deux problèmes aux limites avec le même symbole principal

Sur `[0,R]`, `R=17/20`, choisir `rho=10371/20000` (strictement entre `1037/2000` et `2593/5000`), et imposer `N(0)=1`, `M(0)=rho`, `N'(0)=M'(0)=0`, `N(R)=M(R)`, `N,M>0`. La dernière égalité est **un bord jouet**, et ne remplace pas la condition d'horloge relative authentique Step55, qui dépend aussi des gradients et du shift.

Les deux opérateurs scalaires linéaires ont **exactement les mêmes coefficients** des dérivées premières `B_N=1`, `B_M=-1` en tout point, donc une projection ponctuelle de rang 2 dans les deux cas.

* `L_bad=N'-M'=0`. Alors `(N-M)'=0`, donc `N(R)-M(R)=N(0)-M(0)=1-rho>0`. Le problème aux limites est impossible, indépendamment de la positivité.
* `L_good=N'-M'+kappa*r*(N+M)=0`, avec `kappa=2*(1-rho)/((1+rho)*R²)=7703200/8777219`. Les fonctions analytiques paires `N=(S+D*(1-(r/R)²))/2`, `M=(S-D*(1-(r/R)²))/2`, où `S=1+rho`, `D=1-rho`, satisfont exactement l'opérateur, les deux conditions centrales, `N(R)=M(R)=S/2` et `N>=S/2>0`, `M>=rho>0` sur tout l'intervalle.

**Conclusion prouvée :** connaître le seul couple `(B_N,B_M)` — même exactement et en tout point — ne permet pas de conclure à l'existence ou à l'impossibilité du problème global. Les coefficients d'ordre zéro, le système complet, la régularité et les conditions aux bords comptent. Cette preuve ne dit **rien** sur l'existence des lapses Step58, la tangence Dirac, les charges, le quotient de jauge temporelle ou JANUS.

## Provenance et limites du rejeu

Le connecteur GitHub a réellement relu les sources originales `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, `numerics/hr_step68o_temporal_interval_annulus.py` blob `c99caebc17f243784450ddff94fb061767e6d8e7`, ainsi que le probe b3c3d5 blob `85469568e6df7c26920c1ebb87593dbf474deb04`. Le probe original exige les imports et sources épinglés en clone complet. `git ls-remote` a échoué avec `Could not resolve host: github.com` dans le conteneur ; **le probe original et les tests originaux Step45/55/58+b3c2 n'ont pas été exécutés**. Ne pas confondre la lecture authentifiée de fichiers avec leur exécution.

## Tests réellement exécutés

`python -m numerics.hr_step68ad_b3c3d6_bvp_counterexample` : **10 résidus SymPy exactement nuls et 6 vérifications exactes de signes**, plus deux identités de positivité, PASS. `python -m unittest -v tests.test_hr_step68ad_b3c3d6_bvp_counterexample` : **4 tests PASS, non indépendants**, 0 FAIL. Le test illustre un défaut logique potentiel, il ne certifie pas Step58.

## Suite de b3c3d6 (non terminée)

1. Exécuter `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank --probe-original` dans un clone complet et vérifier les SHA des sources, les coefficients `A_N,A_M,B_N,B_M,E_N,E_M` à `R=17/20` et les éventuelles enclosures contenant zéro.
2. Résoudre ou encadrer l'opérateur complet des lapses positifs sur `[0,R]`, avec régularité centrale et condition réelle d'horloge au bord externe ; contrôler les primaires, la secondaire et la préservation temporelle.
3. Seulement ensuite : vrai pullback Dirac, générateurs/charges, quotient temporel, six couples/rang/tertiaires, `K=0/J=0`, dynamique 4D, stabilité et observables.

**Statut : b3c3d6 PARTIEL ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

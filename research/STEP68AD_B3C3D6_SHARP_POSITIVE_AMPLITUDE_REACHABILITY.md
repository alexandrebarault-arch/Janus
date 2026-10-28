# JANUS b3c3d6 — caractérisation exacte des amplitudes terminales positives (une seule équation)

**Théorème conditionnel, non-Step55, non-Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Théorème de contrôlabilité scalaire à deux bords

Soit `[r0,R]` un anneau compact, `r0>0`. Les coefficients réels `B_N,B_M` sont `C1` et **strictement positifs** partout, `A_N,A_M` continus. On considère **uniquement**

`A_N N+A_M M+B_N N'+B_M M'=0`,

avec `E_N=E_M=0` **exactement**. Fixer **les quatre** données `N(r0),M(r0),N(R),M(R)>0`. Définir

`u_i=B_N(i)N(i)+B_M(i)M(i)`, `s_N=(B_N'-A_N)/B_N`, `s_M=(B_M'-A_M)/B_M`,

`L=int_{r0}^R min(s_N,s_M)dr`, `U=int_{r0}^R max(s_N,s_M)dr`, `T=log(u_R/u_0)`.

**Résultat nécessaire ET suffisant :**

* Si `s_N-s_M` n'est pas identiquement nul, il existe des lapses `C1` **strictement positifs** réalisant exactement les quatre données **si et seulement si** `L<T<U`. Les bornes `T=L` et `T=U` sont **impossibles** sous positivité stricte.
* Si `s_N=s_M` partout, il existe une solution positive **si et seulement si** `T=int s_N dr` (la borne se réduit à un point).

Ce théorème est indépendant des ratios initiaux et terminaux, hormis leur contribution aux valeurs `u_i` et aux poids aux deux extrémités. Il ne garantit ni une solution de la **vraie** Step58 avec autres contraintes, ni une solution avec conditions supplémentaires sur les dérivées.

## Preuve exacte

Poser `u=B_N N+B_M M>0`, `w=B_M M/u`. Alors `0<w<1` et, **en utilisant l'équation originale**,

`u'/u=(1-w)s_N+w s_M`.

Par intégration, `L<=T<=U`. Si `s_N-s_M` est non nul en un point, il l'est sur un intervalle ouvert, où `0<w<1` rend les deux inégalités **strictes**. Si les deux pentes sont égales partout, `T=int s_N`.

Inversement, les données aux bords prescrivent `w_0=B_M(r0)M(r0)/u_0` et `w_R=B_M(R)M(R)/u_R`, tous deux dans `(0,1)`. Pour chaque `C1` `w:[r0,R]->(0,1)` reliant ces valeurs, poser

`u(r)=u_0 exp(int_{r0}^r [(1-w)s_N+w s_M]dt)`,
`N=(1-w)u/B_N`, `M=w u/B_M`.

Les lapses sont positifs `C1`, satisfont l'équation et les données initiales. Des poids `C1` proches des sélecteurs ponctuels de `min(s_N,s_M)` et `max(s_N,s_M)`, avec transitions et couches de bord arbitrairement étroites, approchent respectivement `L` et `U`, tout en conservant **exactement** `w_0,w_R`. Pour tout `L<T<U`, choisir deux poids dont les intégrales encadrent `T`, puis leur combinaison convexe : l'intégrale dépend affinement du poids et atteint **exactement** `T`. La construction réalise ainsi aussi les deux valeurs finales individuelles. Cas dégénéré : si les pentes coïncident, toute interpolation positive `w` convient dès que `T=int s_N`.

## Tests exacts et témoins non physiques

Exécuté localement : `PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_sharp_amplitude_reachability` : **5 résidus SymPy génériques nuls, 11 résidus de deux familles jouets exactes nuls, 2 contrôles de bornes**, 0 FAIL. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_sharp_amplitude_reachability.py' -v` : **4 tests PASS, non indépendants**.

Famille 1 : `B_N=B_M=1,A_N=0,A_M=-1,N=M=exp(r/2)`, `r in [0,1]`, `s_N=0,s_M=1,T=1/2`. Famille 2 : `B_N=1+r,B_M=2+r,A_N=1,A_M=-1-r,u=2exp(r/2),N=u/[2(1+r)],M=u/[2(2+r)]` ; mêmes pentes et `T=1/2`. Les extrémités `T=0` ou `T=1` sont inaccessibles avec deux lapses strictement positifs dans ces deux familles. Le contrôle de la stricte inaccessibilité repose sur la preuve, pas seulement sur deux intégrales SymPy.

## Provenance, limites et suite prioritaire

Original Step58 `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; source du probe original `numerics/hr_step68ad_b3c3d5_temporal_boundary_jet_rank.py` blob `85469568e6df7c26920c1ebb87593dbf474deb04`, lus via le connecteur GitHub. **Probe Step58 à R=17/20 NON exécuté** : le clone local ne résout pas le DNS GitHub. La réduction réelle `E_N=E_M=0` sur le profil Step55, les signes et zéros de `B_N,B_M`, les coefficients centraux subdominants, la jauge temporelle, le vrai BVP Dirac et les charges restent à démontrer. La carte ne couvre pas `B_i` de signes opposés ni `Delta=0` au centre.

**Prochaine étape toujours b3c3d6 :** exécuter le probe original Step58 avec Step45/55/58, b3c2 et Step68o à `R=17/20`, vérifier les coefficients et leurs dérivées sur le vrai profil, les cartes, les deux bords et les lapses strictement positifs ; puis Dirac complet, générateurs/charges, quotient temporel, six couples, K=0/J=0, 4D, stabilité, observables. `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

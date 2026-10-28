# JANUS — b3c3d5 : projection des jets temporels et dérive centrale des horloges

28 octobre 2026. **Résultat mathématique exact mais restreint au rang ponctuel des jets de lapses ; corollaire conditionnel sur les horloges. PAS une solution de Step58 ni une obstruction Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Sources originales et authentification

Lus directement sur GitHub, branche `research/gate2b-nonhomothetic-transfer` : `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, et b3c2 `numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` blob `9a77f749a040aaec37e7c3f01368013154fdb562` avec son certificat JSON blob `4daa3b6ae9e6447eb380e512419ae4e7eaf2fedf`. Le moteur original Step45 est épinglé `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Le script nouveau épingle également l'évaluateur original Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`.

Le Step58 original construit un opérateur linéaire en `N,M` et leurs dérivées. Son certificat `highest_lapse_certificate()` établit l'annulation des coefficients de `N'',M''` sur `Fz=0` et `Hg=0` dans la carte `K>0` ; il ne prouve pas que les coefficients de `N',M'` soient nuls. Le **rejeu de cet opérateur original sur Step55 au bord R=17/20 n'a pas été effectué** : `git ls-remote` échoue par DNS `Could not resolve host: github.com` dans le conteneur. Un exécutable d'évaluation authentique est ajouté, mais ses résultats ne sont pas revendiqués.

## Théorème de projection ponctuelle — exact et exhaustif

Écrivons au bord extérieur, sous les primaires et la coquille stationnaire du shift (hypothèses de Step58), `A_N N + A_M M + B_N N' + B_M M'=0`. Les quatre coefficients sont ceux du véritable opérateur temporel, **à évaluer** sur Step55. Cette unique équation ponctuelle a les propriétés suivantes :

1. Si `(B_N,B_M) != (0,0)`, sa projection sur les deux valeurs de bord `(N,M)` est **surjective**, de rang 2 : tout couple fini peut être prolongé par au moins un choix de jets `N',M'` au point. Par exemple, si `B_M != 0`, choisir `M'=-(A_N N+A_M M+B_N N')/B_M`. Cela **ne construit pas** des lapses lisses globalement admissibles ni des données conservant les deux bords.
2. Si `B_N=B_M=0` et `(A_N,A_M)!=(0,0)`, les valeurs de bord sont contraintes à une droite, de vecteur tangent `(A_M,-A_N)` et de rang 1. Un couple **strictement positif** existe seulement si `A_N A_M<0`. Le terme de courbure mixte de b3c3d4, pour `Theta=(c_N N+c_M M)dλ`, s'annule sur cette droite **si et seulement si** `c_N A_M-c_M A_N=0`.
3. Si les quatre coefficients sont nuls, l'équation ponctuelle n'impose aucune condition sur `(N,M)` ; projection de rang 2.

Plus généralement, pour un graphe de valeurs de bord `M=m(λ,N)`, `dTheta(∂_N,∂_λ)=c_N+c_M ∂_N m`. Un graphe homogène `M=ρ(λ)N` rend ce coefficient nul ssi `c_N+ρ c_M=0`. Les coefficients `c_N,c_M` sont ceux de b3c3d4 avec `V=Vrel` et vérifient exactement `c_M-(Lg/Lf)c_N<0` sur les hypothèses positives de cette étape. **Cela ne suffit pas à déduire le signe de la courbure sur les variations globales Dirac admissibles** : celles-ci ne sont pas déterminées par l'équation ponctuelle et les lapses sont des multiplicateurs, pas des couples canoniques. Il reste aussi à contrôler les générateurs améliorés et la jauge temporelle.

## Corollaire quantitatif conditionnel reliant les deux bords

Le certificat b3c2 antérieur donne, **si** la préservation originale Step58 vaut sur la branche Step55 avec lapses positifs pairs et réguliers au centre, `1037/2000 < M(0)/N(0) < 2593/5000`. Sous shift régulier, la vitesse centrale de l'horloge relative est `w(0)=∂t(tg-tf)(0)=N(0)-M(0)`. Donc la nouvelle borne explicite est

`2407/5000 < w(0)/N(0) < 963/2000`.

Si **en outre** `w` est `C¹` sur `[0,17/20]` et le choix de shift au bord externe impose `w(17/20)=0`, le théorème des accroissements finis assure l'existence d'un `ξ∈(0,17/20)` tel que

`w'(ξ)/N(0) < -2407/4250`.

C'est une condition nécessaire de gradient radial du taux de désynchronisation des horloges, **pas** une singularité, une impossibilité de lapse positif, ni une preuve de compatibilité globale. Elle est conditionnelle au certificat central b3c2, lui-même non rejoué sur imports originaux durant cette session.

## Tests et reproduction

Exécutés localement : `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank` : **12 résidus SymPy exactement nuls**, **6 vérifications de classification exactes**, 0 échec ; `python -m unittest -v tests.test_hr_step68ad_b3c3d5_temporal_boundary_jet_rank` : **4 cas PASS**, rejouant les mêmes expressions (non indépendants), 0 échec final. Le premier essai a révélé un type `sympy.BooleanFalse` dans un contrôle utilisant `is False` ; conversion explicite `bool()` corrigée avant publication. Le script/test publiés sont identiques aux octets locaux exécutés si les SHA blobs correspondent.

Pour exécuter l'évaluation véritable du bord externe dans un **clone complet** : `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank --probe-original`. Elle vérifie les quatre SHA originaux, reconstruit les jets Step55 avec l'évaluateur Step68o, puis évalue les six coefficients `A_N,B_N,E_N,A_M,B_M,E_M` de Step58 à `R=17/20` par intervalles à arrondi sortant. **Cette commande n'a pas été exécutée** ici ; toute enclosure contenant zéro devra être classée `INCOMPLETE`, et toute exception d'évaluation devra être diagnostiquée, non convertie en preuve.

## Prochaine étape b3c3d6

Exécuter réellement le probe original Step58 au bord `17/20`, contrôler le rang des coefficients de `N',M'` sur les contraintes et les deux bords, puis résoudre/encadrer le système de lapses avec données centrales et condition d'horloge relative au bord externe. Rejouer les imports originaux Step45/55/58+b3c2. Ensuite calculer le pullback de la forme complète sur les vraies variations Dirac, les générateurs/charges améliorés, le quotient temporel et enfin six couples/rang/tertiaires, `K=0/J=0`, 4D, stabilité et observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

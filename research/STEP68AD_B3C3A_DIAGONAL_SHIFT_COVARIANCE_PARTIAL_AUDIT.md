# JANUS — b3c3a : audit exact de covariance radiale du shift diagonal (partiel)

28 octobre 2026. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et portée

Sources authentifiées sur la branche de recherche : Step45 `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step58 `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step57 blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`. Le code de cet audit est une **transcription algébrique indépendante et partielle** des densités Step45, pas un import des moteurs originaux. Le rejeu b3c2 en clone complet reste NON effectué.

## Identités vérifiées exactement

Avec les six couples canoniques dans l'ordre Step45, les poids radiaux des douze variables sont `(1,0,0,1,0,1,1,0,0,1,0,1)`. Le shift relatif `z` est scalaire et `z'` a poids 1. Pour un générateur radial diagonal `V`, la prolongation est

`delta q=V q'+w V' q` et `delta q'=V q''+(w+1)V' q'+w V'' q`.

Pour chacun des huit objets source-fidèles `Ag,Bg,Af,Bf,Dg,K,Fz,C_zprime`, les coefficients de `V''` s'annulent exactement, et ceux de `V'` valent `w X` pour les poids respectifs `1,0,1,0,2,2,2,0`. Le coefficient de `V` est `X'` par la règle de chaîne. Ainsi `delta_V X=V X'+w V' X`. **16 identités SymPy exactes PASS**, aucun échec. Un `unittest` supplémentaire PASS rejoue les mêmes identités, sans constituer une validation indépendante.

En particulier `D_g` et `K` sont tous deux des densités de poids 2, donc `z_*=D_g/sqrt(D_g²+K²)` est un scalaire sur `K>0`. L'équation algébrique `F_z=0` est covariante de poids 2. Les densités original-IBP `A_g,A_f` ont poids 1, tandis que les coefficients de dérivée des lapses `B_g,B_f` sont scalaires.

## Conséquence formelle pour la préservation temporelle

Pour un générateur radial différentiable et une secondaire réduite `C_red` effectivement covariante de poids 1, on obtient `delta_V C_red=(V C_red)'`. Sur la **coquille fonctionnelle complète** `C_red(r)=0`, son terme radial diagonal s'annule dans le volume pour tout `V` régulier. Ceci explique pourquoi l'opérateur Step58 de préservation en volume est écrit avec `N,M`, sans que `V_rel` puisse, à lui seul, lever la condition centrale b3c2.

**Restriction de preuve :** cette étape ne calcule pas directement l'identité de Lie du `C_red` complet à six couples, et ne construit pas le générateur amélioré aux frontières. La conclusion sur `C_red` est donc un **lemme de covariance conditionnel**, pas un certificat complet de Dirac ni une preuve de l'absence de charges de bord.

## Corollaire central conditionnel

Si le rapport central Step58 b3c2 est confirmé par les imports originaux, alors au centre régulier `dot(t_g-t_f)=N(0)-M(0)` et

`2407/5000 < dot(t_g-t_f)(0)/N(0) < 963/2000`.

Cette différence d'horloges avance nécessairement dans le temps pour `N(0)>0`, sous les hypothèses b3c2. Un shift radial régulier ne peut la compenser au centre où `t'_g=t'_f=0`. Cela exclut seulement une condition de stationnarité relative, **pas JANUS**.

## Tests, limites et prochaine étape

Exécutés : 16 identités exactes SymPy, 1 unittest de rejeu PASS, 7 comparaisons exactes BigInt V8 indépendantes sur le certificat central b3c2, 0 FAIL. Script local exécuté et publié octet pour octet ; tests également publiés et comparés à leurs blobs Git. Les moteurs Python originaux Step45/55/58 n'ont pas été réexécutés en clone complet, faute d'accès réseau Git depuis l'environnement Python local.

**Prochaine étape b3c3b :** exécuter le script b3c2 avec les imports authentiques dans un clone complet, comparer les quatre coefficients algébriques et les bornes, vérifier explicitement `delta_V C_red=(V C_red)'` sur la secondaire réduite, puis construire les générateurs temporels améliorés, charges et conditions de bord. Ensuite seulement : quotient de jauge, rang Dirac six couples/tertiaires, K=0/J=0, 4D, stabilité et observables.

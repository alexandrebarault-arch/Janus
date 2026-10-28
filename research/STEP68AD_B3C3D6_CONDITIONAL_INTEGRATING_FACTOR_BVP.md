# JANUS — b3c3d6 : identité globale exacte de compatibilité des lapses (conditionnelle)

28 octobre 2026. **Résultat mathématique exact sur un opérateur scalaire linéaire du premier ordre ; PAS une évaluation du Step58 original, PAS un résultat Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Réduction exacte et domaine de validité

Sur un intervalle fermé `[a,b]` où `B_M(r) ≠ 0`, considérer l'équation ponctuelle prolongée globalement

`A_N(r)N(r)+A_M(r)M(r)+B_N(r)N'(r)+B_M(r)M'(r)=0`.

Pour des coefficients suffisamment réguliers, poser `q=B_N/B_M`, `p=A_M/B_M`, `a=A_N/B_M`, `h=q'+p*q-a` et `W=M+q*N`. Une dérivation exacte donne

`W'+pW=hN`.

Avec `P(r)=∫_a^r p(s)ds`, l'intégration par facteur intégrant donne la **condition nécessaire et suffisante pour que la solution M associée à une fonction N prescrite satisfasse la condition externe M(b)=N(b)** :

`(1+q(b))N(b)=exp(-P(b))*(M(a)+q(a)N(a))+∫_a^b exp(-(P(b)-P(s)))*h(s)*N(s)ds`.

La suffisance est relative à cette équation différentielle scalaire et à la fonction `N` choisie, sous régularité et `B_M≠0`. Elle ne démontre **ni** la positivité de `M` **ni** l'existence de `N` répondant aux autres contraintes. La positivité exige en outre `W(r)-q(r)N(r)>0` sur tout l'intervalle. Si `1+q(b)=0`, le membre de gauche s'annule : le signe de l'intégrale pondérée devient un test d'obstruction. Par exemple, si `W(a)<0`, `N>0`, et `h≤0` partout, l'égalité est impossible. Il s'agit d'un **critère conditionnel de signe**, pas d'une affirmation sur Step58.

## Relecture du contre-exemple b3c3d6

Pour `R=17/20`, `rho=10371/20000`, `N(0)=1`, `M(0)=rho`, et `N(R)=M(R)`, les deux opérateurs jouets ont `B_N=1,B_M=-1`, donc `q=-1`.

- `L_bad=N'-M'` : `p=h=0`, `W=M-N` constant, `W(0)=rho-1<0` mais `W(R)=0` requis ; impossibilité globale exacte.
- `L_good=N'-M'+kappa*r*(N+M)` : `p=-kappa*r`, `h=2*kappa*r>0` pour `r>0`, et le polynôme positif pair déjà publié réalise exactement l'égalité. La distinction globale réside dans le terme source intégral et non dans le rang ponctuel.

Un contrôle symbolique additionnel à `q(r)` non constant vérifie le terme indispensable `q'` et évite une simplification fausse.

## Limite majeure : centre physique dégénéré

Le résultat central b3c2 antérieur, **non rejoué sur les imports originaux ici**, indique `B_N,B_M=O(r^4)` sur la coquille Step58/Step55. Donc `B_M(0)=0` : **la division par `B_M` et la formule de `q` ne sont PAS justifiées sur `[0,R]`**. Une application au problème physique exige d'abord un certificat de non-annulation de `B_M` sur `[epsilon,R]` ou des changements de cartes contrôlés, puis le raccordement exact au centre en `epsilon→0` avec les expansions des lapses et de Step58. Les signes des coefficients originaux `B_N,B_M` au bord `R=17/20` ne sont toujours pas connus.

La forme de bord non-IBP, les primaires, `C(r)=0`, le générateur différentiable, la jauge temporelle, les six couples et la dynamique 4D ne sont pas traités par cette identité. L'égalité externe `M(R)=N(R)` est ici une **condition jouet/illustrative**, et non la condition authentique de stationnarité des horloges Step55, laquelle dépend aussi du shift et des gradients des horloges.

## Exécution et sources

Sources originales lues via le connecteur GitHub, branche `research/gate2b-nonhomothetic-transfer` : `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, `numerics/hr_step68o_temporal_interval_annulus.py` blob `c99caebc17f243784450ddff94fb061767e6d8e7`, `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, `numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` blob `9a77f749a040aaec37e7c3f01368013154fdb562`.

Exécuté localement : `python -m numerics.hr_step68ad_b3c3d6_integrating_factor_bvp` : **13 résidus SymPy nuls, 4 contrôles de signes exacts** ; `python -m unittest -v tests.test_hr_step68ad_b3c3d6_integrating_factor_bvp` : **4 tests PASS, non indépendants**, zéro échec final. Première exécution : conversion Python implicite `0/-1→0.0` détectée puis corrigée par `sympify`, et tous les contrôles rejoués avant publication. Le probe original `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank --probe-original` et les moteurs Step45/55/58+b3c2 **NON exécutés** : `git ls-remote` échoue `Could not resolve host: github.com`.

## Suite impérative

**b3c3d6 reste PARTIEL.** Exécuter le probe original Step58 et les moteurs authentiques, certifier les coefficients `B_N,B_M` et leurs éventuels zéros sur `(0,R]`, établir le vrai problème de lapses aux deux bords et appliquer l'identité uniquement sur les cartes certifiées ; ensuite pullback Dirac réel, charges/générateurs, quotient temporel, six couples/rang/tertiaires, `K=0/J=0`, dynamique 4D, stabilité et observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

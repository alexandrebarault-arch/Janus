# JANUS b3c3d6 — atteignabilité constructive du ratio terminal sur un anneau

**Théorème conditionnel, non-Dirac, non-Step55.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Énoncé

Sur `[r0,R]` avec `r0>0`, supposons `A_N,A_M,B_N,B_M` continus, `B_N,B_M>0` partout, et l'équation **unique** `A_N N+A_M M+B_N N'+B_M M'=0` exactement (en particulier `E_N=E_M=0` dans le véritable opérateur). Pour toute paire initiale `N(r0)=N0>0`, `M(r0)=M0>0` et tout ratio final `M(R)/N(R)=kR>0`, il existe des lapses `N,M` strictement positifs `C1` sur l'anneau satisfaisant ces trois données. Si les coefficients sont analytiques, choisir une interpolation analytique positive de `k` produit une solution analytique.

## Preuve constructive

Choisir une fonction `k(r)>0` de classe `C1` avec `k(r0)=M0/N0` et `k(R)=kR`, par exemple l'interpolation affine strictement positive. Écrire `M=kN`. L'équation devient

`(B_N+B_M*k) N' + (A_N+A_M*k+B_M*k') N=0`.

Comme `B_N+B_M*k>0`, poser `H=(A_N+A_M*k+B_M*k')/(B_N+B_M*k)`, puis

`N(r)=N0 exp(-integral_{r0}^r H(s)ds)`, `M(r)=k(r)N(r)`.

La positivité, la régularité, l'équation et le ratio final sont immédiats. Cette construction **n'impose pas l'amplitude terminale** `N(R)` : une condition supplémentaire de valeur absolue peut être incompatible. L'argument s'étend si `B_N+B_M*k` reste non nul, mais sans garantie globale pour des coefficients de signes opposés ou des zéros communs. Au centre b3c2, `B_i=O(r^4)` et l'hypothèse annulaire échoue.

## Témoin exact indépendant (opérateur jouet)

`r0=1/4`, `R=17/20`, `A_N=1`, `A_M=-1`, `B_N=2`, `B_M=3`, `N0=1`, `M0=10371/20000`, `kR=1`. L'interpolation `k=k0+c(r-r0)` donne `c=9629/12000`, `D=2+3k`, `D0=71113/20000` et

`N=exp((r-r0)/3)*(D/D0)^(-48887/28887)`, `M=kN`.

Les deux fonctions sont analytiques strictement positives, vérifient l'équation exactement, et `N(R)=M(R)≈0.685968777185562552`. Ce témoin n'est **pas** le profil physique Step55.

## Contrôles exécutés et limites

`PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_ratio_reachability` : 3 résidus algébriques génériques et 5 contrôles exacts du témoin PASS. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_ratio_reachability.py' -v` : 4 tests PASS, non indépendants, 0 FAIL. L'identité de dérivée logarithmique du témoin est contrôlée symboliquement, sans recours à des valeurs flottantes pour la preuve.

Les originaux Step58 (`802c23aebd41780d8c462f1aa1711707fe4ee88f`), Step55 (`a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) et Step68o (`c99caebc17f243784450ddff94fb061767e6d8e7`) ont été **lus sur GitHub** mais pas exécutés ici. Aucun signe `B_N,B_M>0` sur le profil Step55 n'est certifié ; ni les conditions physiques aux deux bords, ni la préservation Dirac, ni les charges, ni le quotient temporel ne sont établis. Le vrai probe original Step58 à `R=17/20` reste prioritaire. Le théorème précise seulement pourquoi un **ratio terminal seul** ne peut pas constituer une obstruction dans cette carte strictement positive à une seule équation.

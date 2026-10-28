# JANUS b3c3d6 — cône de positivité et écran de croissance sans division par B_M

**Statut : théorème mathématique conditionnel sur un anneau ; pas un résultat Step55, pas une tangence Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Hypothèses et identité

Sur `[r0,R]`, coefficients `A_N,A_M,B_N,B_M` continus, `B_N,B_M` de classe C1, et lapses `N,M` C1 strictement positifs. On impose la coquille de premier ordre `A_N N+A_M M+B_N N'+B_M M'=0` (les termes en `N'',M''` doivent être exactement nuls, non simplement petits). Sur un intervalle où **`B_N>0` et `B_M>0`**, définir `u=B_N N+B_M M>0`, `v=-B_M N+B_N M`, `Delta=B_N²+B_M²`, `alpha=((B_N'-A_N)B_N+(B_M'-A_M)B_M)/Delta`, `beta=(-(B_N'-A_N)B_M+(B_M'-A_M)B_N)/Delta`. L'identité déjà établie `u'=alpha*u+beta*v` vaut sans diviser par `B_M`.

La positivité fournit exactement `v+(B_M/B_N)u=Delta*M/B_N>0` et `(B_N/B_M)u-v=Delta*N/B_M>0`. Donc `-B_M/B_N < v/u < B_N/B_M`. En posant `ell=alpha+min(-beta*B_M/B_N,beta*B_N/B_M)` et `ups=alpha+max(-beta*B_M/B_N,beta*B_N/B_M)`, on obtient `ell <= (log u)' <= ups` et par intégration la condition **nécessaire** :

`u(r0)*exp(integral ell) <= u(R) <= u(r0)*exp(integral ups)`.

Les inégalités sont strictes lorsque l'intégrale de l'écart positif est strictement positive. Un terminal hors de cet intervalle exclut toute paire de lapses positifs satisfaisant les hypothèses ; être dedans ne démontre **pas** l'existence. Si `M(R)=N(R)`, alors `u(R)=(B_N(R)+B_M(R))*N(R)` ; le test borne l'amplitude terminale, mais **ne peut pas exclure à lui seul une condition de ratio sans amplitude terminale prescrite**. Si un `B_i` s'annule, le présent cône exige une autre carte ; le cadre général `Delta>0` précédent reste valide, mais les bornes `B_N/B_M` ne le sont plus. Au centre `Delta=0`, aucun raccord n'est prouvé.

## Témoin jouet exact, exclusion et existence

Sur `[0,17/20]`, choisir `B_N=B_M=1`, `A_N=-1`, `A_M=+1`. Alors `u=N+M`, `v=M-N`, `alpha=0`, `beta=-1`, donc `u'=N-M`, et `|(log u)'|<1` pour lapses strictement positifs. Avec `N(0)=M(0)=1`, on a `u(0)=2` et `u(R)<2 exp(17/20)<2e<6` (car `e<3`). Les conditions supplémentaires `N(R)=M(R)=3` demanderaient `u(R)=6` : **impossibles**. En revanche `N=M=1` est une solution positive analytique satisfaisant le même opérateur et `N(R)=M(R)=1`. Ce sont des opérateurs **jouets**, pas les coefficients Step58 physiques.

## Reproductibilité et limites

`PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_positive_cone_growth` : 6 résidus algébriques exacts, 6 résidus jouets exacts, 0 échec. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_positive_cone_growth.py' -v` : 4 tests PASS non indépendants. Aucun probe original Step58 à `R=17/20`, aucun Step55/Step68o/b3c2 ni Dirac exécuté. L'usage physique exige les vrais coefficients, leur signe sur des sous-intervalles, le raccord des cartes et la vérification des bords.

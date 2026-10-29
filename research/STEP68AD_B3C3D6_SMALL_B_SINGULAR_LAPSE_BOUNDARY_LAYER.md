# b3c3d6 — contre-exemple exact de couche limite des lapses (29 octobre 2026)

**STATUT : résultat mathématique JOUET, non Step55, non Step58, non Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Lecture en direct de l'original Step58 blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` et du candidat cubique blob `9eb5167bec74fc427307a262faaa6a1f785785a8` ; ces moteurs n'ont PAS été exécutés durant cette session. Les valeurs historiques `B_N,B_M~1e-44` ne sont que numériques et ne démontrent PAS une annulation exacte.

## Théorème (contre-exemple de singularité de la limite B→0)

Pour tout `R>0`, `eps>0`, sur `0<r<=R`, prendre `A_N=r²`, `A_M=-2r²`, `B_N=-eps*r⁴`, `B_M=0`, `M(r)=1`, `N(r)=2-exp((1/R-1/r)/eps)`. Alors `A_N*N+A_M*M+B_N*N'+B_M*M'=0` **exactement**, `1<=N(r)<2`, `M=1`, `N(R)=M(R)=1`, `N(0)=2`, `N^(k)(0)=0` pour tout entier `k>=1` (extension C∞ plate). La borne uniforme `sup|B_N|=eps*R⁴` tend vers zéro, tandis que `N'(R)=-1/(eps*R²)` diverge. À `eps=0`, l'équation devient `r²(N-2M)=0`, incompatible avec des lapses strictement positifs et `N(R)=M(R)`. **Ainsi, remplacer un coefficient numérique extrêmement petit par zéro peut inverser le verdict d'existence du problème aux deux bords.** Le centre est C∞ mais **non analytique** ; cela ne prouve rien pour le centre analytique imposé dans JANUS Step55.

## Écran quantitatif nécessaire au bord

Pour tout opérateur du premier ordre `A_N N+A_M M+B_N N'+B_M M'=0` et `N(R)=M(R)=u>0`, si `|N'(R)|,|M'(R)|<=L*u`, alors `|A_N(R)+A_M(R)| <= L*(|B_N(R)|+|B_M(R)|)`. Un certificat `|A_N+A_M| > L*(|B_N|+|B_M|)` exclurait donc ces lapses **sous la borne de pente prouvée**. Le jouet sature exactement cette inégalité à R avec `L=1/(eps R²)` et `u=1`. Sans borne indépendante sur les pentes (ou annulation algébrique exacte des B), aucun rejet des lapses positifs ne découle de `B~1e-44`.

## Reproductibilité et limites

Commande exécutée : `PYTHONPATH=. python -m unittest discover -s tests -v` : **5 PASS, 0 FAIL**, tests SymPy non indépendants ; `python -m compileall -q numerics tests` PASS. Les dérivées jusqu'à l'ordre 6 sont testées au centre ; la platitude tous ordres suit de la propriété standard `r^-m exp(-c/r) -> 0` pour `c>0`. Aucune solution numérique Step55, aucun coefficient Step58 physique, aucun BVP JANUS exécuté ici. Prochaine action prioritaire inchangée : exécuter le candidat cubique sur les cinq originaux SHA-authentifiés aux quatre rayons, comparer les six coefficients affine/cubique, puis factoriser exactement B_N/B_M ou prouver des enclosures ET des bornes de pentes, raccord central analytique et vrais deux bords ; ensuite Dirac/4D/stabilité/observables.

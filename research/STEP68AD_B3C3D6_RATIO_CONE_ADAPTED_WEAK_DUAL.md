# JANUS b3c3d6 — dual faible adapté à un cône de ratios (29 octobre 2026)

**Théorème exact conditionnel, non physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

Pour `T=A_N N+A_M M+B_N N'+B_M M'+E_N N''+E_M M''`, `N,M>0` C², et `phi>=0` C² avec `phi=phi'=0` aux deux extrémités, poser `Q_i=phi*A_i-(phi*B_i)'+(phi*E_i)''`. Supposons des bornes de ratio **sur tout l'intervalle** `0<lo(r)<=M(r)/N(r)<=hi(r)`. Si `min(Q_N+lo*Q_M, Q_N+hi*Q_M)>=0` partout, avec stricte positivité sur un ouvert, alors `T=0` n'admet **aucun** couple de lapses strictement positifs respectant ce cône. Preuve : intégration par parties, `0=int phi*T=int N*(Q_N+(M/N)*Q_M)` ; le facteur entre parenthèses est affine en ratio, donc minoré par le minimum aux deux bornes du cône. La positivité stricte et `N>0` donnent contradiction. Cette méthode n'exige **pas** `Q_M>=0` ; elle peut donc survivre à `A_M<0` qui élimine le certificat dual composante par composante. Sans bornes globales du ratio, elle ne conclut rien.

## Témoin analytique JOUET avec B/E non nuls

Sur `[0,1]`, `phi=x²(1-x)²`, `eps=1/100`, `A_N=2`, `A_M=-3`, `B_N=eps*x³(1-x)³`, `B_M=-B_N`, `E_N=eps²*x⁴(1-x)⁴`, `E_M=-E_N`, et cône `1/4<=M/N<=1/2`. Alors `int Q_M=int phi*A_M=-1/10<0` : **dual composante par composante impossible**. Pourtant, pour tout `rho` dans le cône, `Q_N+rho Q_M >= (318401/640000)*phi>0` sur `(0,1)`.

En effet `|(phi B_N)'|/phi<=5eps/16` et `|(phi E_N)''|/phi<=33eps²/16` (avec prolongement par continuité aux bords) ; `2-3rho>=1/2` et `|1-rho|<=3/4`. D'où la marge exacte `1/2-(3/4)*(5eps/16+33eps²/16)=318401/640000`. **Contrôle négatif** : `N=1,M=2/3` est une solution positive exacte de `T=0` (les dérivées s'annulent), mais se situe **hors** du cône. Le certificat exclut uniquement les solutions à ratio borné.

## Limites physiques et priorité

Les ratios centraux Step58 b3c2 et les quatre ratios ponctuels antérieurs ne constituent **pas** un cône global certifié pour les lapses. Les coefficients Step58 cubiques et leurs signes ne sont pas rejoués ici. Ne pas confondre ce théorème de faisabilité conditionnelle avec un no-go JANUS. Il faut rejouer les cinq originaux SHA-authentifiés et le candidat cubique aux quatre rayons, certifier `A/B/E` et leurs enclosures, puis chercher ou exclure des bornes **globales** de `M/N` compatibles avec les deux bords, avant d'utiliser ce dual. Dirac six couples, charges/jauge, K=0/J=0, dynamique 4D, stabilité et observables restent ouverts.

Tests locaux : `PYTHONPATH=. python -m unittest discover -s tests -v` et `python -m compileall -q numerics tests`, SymPy rationnel exact, non indépendants ; aucune exécution physique originale Step45/46/55/58 dans cette session.

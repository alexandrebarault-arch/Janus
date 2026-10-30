# JANUS — b3c3d6 : borne d'erreur par résidu normalisé (30 octobre 2026)

**Statut : théorème conditionnel exact, pas de rejeu numérique physique.** GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

Sur l'EDO originale Step55, `2s U_s=G(s,U)-2U`, poser `rho(s)=2s v_s-G(s,v)+2v` pour un candidat continu, C1 par morceaux. Si `U` et `v` restent dans le tube physique Step55, si le certificat historique Step63 donne `G_U<=-99/100` sur les segments entre eux, et si `|rho(s)|<=R` **en tout point** de l'intervalle `[ra²,rb²]`, alors avec `e_a=|v(ra²)-U(ra²)|` :

`e_b <= (ra/rb)^(299/100)*e_a + (100*R/299)*(1-(ra/rb)^(299/100))`.

**Preuve :** pour `e=v-U`, la dérivée de Dini supérieure de `|e|` est au plus `-(299/(200s))*|e|+R/(2s)`, par accroissements finis et l'inégalité Step63. Intégration du facteur `s^(299/200)` donne la formule, avec recollement par continuité aux nœuds de l'approximation.

**Version 100 % rationnelle et directement testable :** puisque `q=ra/rb<1` et `q^(299/100)<=q²`, poser `E=100R/299`. Alors `e_b <= E + max(e_a-E,0)*q²`. La séparation du signe de `e_a-E` est indispensable : remplacer aveuglément la puissance par `q²` quand le coefficient est négatif inverserait l'inégalité. Pour `ra=1/100`, `rb=17/20`, `q²=1/7225`.

Le seuil strict de confinement historique est `R<295653233337826329055403/2000000000000000000000000000` ; sous ce seuil, `E<4.944034003e-5<1/20000`. **Ce nombre n'est PAS une erreur physique mesurée.** Il est conditionnel à la certification de la courbe numérique dans le tube, au défaut continu et à la borne initiale. Les valeurs ponctuelles aux quatre rayons ne suffisent pas : un défaut peut s'annuler aux nœuds et être non nul entre eux.

Tests locaux exécutés : `PYTHONPATH=. python -m unittest discover -s tests -v` : **11 PASS, 0 FAIL**, et `python -m compileall -q numerics tests` : **PASS**. Tests rationnels et un témoin SymPy jouet, non indépendants ; aucune intégration physique Step45/46/55/58 ou DOP853 effectuée ici.

Sources historiques épinglées : Step55 normalisé `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, barrière Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, rapport Step63 `8a6ff87fdde3efbf26fa81d20ddb2623c161c9c1`. Elles ont été lues ou reprises via le connecteur GitHub, non réexécutées. Prochaine étape inchangée : **cinq originaux SHA-authentifiés + affine/cubique Step58 aux quatre rayons, défaut continu DOP853/enclosures et erreur initiale, six coefficients A/B/E, BVP positif aux deux vrais bords, puis Dirac/4D/stabilité/observables**.

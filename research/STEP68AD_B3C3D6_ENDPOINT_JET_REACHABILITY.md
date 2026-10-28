# JANUS b3c3d6 — compatibilité exacte des jets de lapse aux deux bords (29 octobre 2026)

**Théorème conditionnel, non-Step55, non-Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Énoncé et nouveauté

Sur un anneau compact `[r0,R]`, `r0>0`, supposer `B_N,B_M` de classe C1 strictement positifs et `A_N,A_M` continus. Considérer **une seule** équation `A_N N+A_M M+B_N N'+B_M M'=0`, avec `E_N=E_M=0` exactement. Prescrire les huit nombres strictement positifs `N(r0),M(r0),N(R),M(R)` et réels `N'(r0),M'(r0),N'(R),M'(R)`. Poser `u=B_N N+B_M M`, `s_i=(B_i'-A_i)/B_i`, `L=∫min(s_N,s_M)`, `U=∫max(s_N,s_M)`, `T=log(u_R/u_0)`.

**Résultat nécessaire et suffisant** : les huit données sont réalisables par des lapses `C1` strictement positifs si et seulement si (i) l'équation scalaire initiale est satisfaite **aux deux extrémités** par les valeurs et dérivées prescrites, et (ii) `L<T<U` lorsque `s_N-s_M` n'est pas identiquement nul, ou `T=∫s_N` lorsque `s_N=s_M` partout. Aucune autre restriction sur les dérivées terminales finies n'est nécessaire **dans ce problème scalaire**. Ceci étend le théorème précédent des quatre amplitudes à **quatre dérivées terminales**.

## Preuve

Poser `w=B_M M/u`. Les données terminales de valeurs imposent `0<w_0,w_R<1`, et les dérivées prescrites imposent `w'_i=((B_M' M+B_M M')/u-w u'/u)_i`, où `u'_i=(B_N'N+B_NN'+B_M'M+B_MM')_i`. Sur la coquille scalaire, `u'/u=(1-w)s_N+w s_M`. Les contraintes locales (i) sont donc nécessaires pour que les jets de `u` coïncident aux deux bords. La condition intégrale (ii) est nécessaire par stricte positivité de `w`.

Pour la suffisance, construire deux poids `C1` strictement compris entre 0 et 1, **ayant les mêmes valeurs et dérivées prescrites aux extrémités**, et dont les intégrales `∫[(1-w)s_N+w s_M]` encadrent `T`. C'est possible en choisissant des couches de bord de largeur arbitrairement petite, avec interpolations de Hermite locales respectant les jets finies, puis des sélecteurs continus proches de `min` et `max` sur l'intérieur ; les couches de bord ont une contribution intégrale arbitrairement petite. Leur combinaison convexe conserve les quatre jets de `w` et la stricte positivité, et atteint exactement `T`. Définir `u(r)=u_0 exp(∫[(1-w)s_N+w s_M])`, `N=(1-w)u/B_N`, `M=wu/B_M`. Les deux valeurs terminales sont reproduites, et les dérivées aussi, grâce à (i). En cas de pentes identiques, toute interpolation positive de `w` avec ces jets suffit si `T=∫s_N`.

**Attention :** ce théorème n'étend PAS l'existence aux dérivées secondes imposées, aux équations supplémentaires de Dirac, aux zéros ou signes opposés de `B_i`, au centre dégénéré, ni à Step55/Step58 original.

## Certificat et contre-témoin

Code `numerics/hr_step68ad_b3c3d6_endpoint_jet_reachability.py` : 10 résidus SymPy exacts nuls (dont identités définitionnelles), 12 contrôles exacts de jouet/gardes PASS. Tests `tests/test_hr_step68ad_b3c3d6_endpoint_jet_reachability.py` : 4 unittest PASS, **non indépendants**, 0 FAIL. Exemple positif sur `[0,1]` : `B_N=B_M=1,A_N=0,A_M=-1,N=M=exp(r/2)`. Les huit jets de bord sont réalisés ; `T=1/2`, `L=0,U=1`. Gardes négatives : garder les quatre amplitudes mais imposer `N'(0)=M'(0)=0` viole l'équation locale `-1=0` ; `T=0` viole la borne intégrale stricte même si des jets locaux compatibles sont prescrits.

## Sources authentiques et limite de calcul

Step58 `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` et Step55 `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` relus via GitHub ; probe publié `numerics/hr_step68ad_b3c3d5_temporal_boundary_jet_rank.py` blob `85469568e6df7c26920c1ebb87593dbf474deb04`. Le clone Git local renvoie `Could not resolve host: github.com`. **Probe original à R=17/20 non exécuté**, pas de signes physiques de B, pas de solution globale de lapses certifiée.

**Priorité inchangée b3c3d6** : exécuter Step58 original sur Step55 R=17/20 avec Step45, Step68o et b3c2 ; certifier coefficients B_N/B_M et leurs dérivées, zéros, cartes et raccord central, vrais jets/valeurs des deux bords et lapses positifs ; puis pullback Dirac, charges/générateurs, quotient de jauge temporelle, six couples, K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

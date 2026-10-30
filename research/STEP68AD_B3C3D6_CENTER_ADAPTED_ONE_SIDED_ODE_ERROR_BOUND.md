# JANUS b3c3d6 — borne rationnelle contractante adaptée au centre (30 octobre 2026)

**Statut : théorème mathématique exact conditionnel ; aucun nouveau certificat physique.**

La source originale SHA `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` (`hr_step55_normalized_secondary.py`) pose `2s U_s=G(s,U)-2U` avec `s=r²`. Le certificat d'erreur précédent impose `Lh<1` sur chaque cellule. Ce nouveau lemme utilise **la pente unilatérale** plutôt que la constante de Lipschitz absolue et évite cette condition restrictive au voisinage du centre.

Pour `0<r_a<r_b`, si `U` est une solution exacte, `v` une approximation `C¹`, `|U(r_a²)-v(r_a²)|≤e_a`, `|v_s-(G(s,v)-2v)/(2s)|≤D` sur **tout** l'intervalle et `∂_U G(s,w)≤1` sur chaque segment entre `U(s)` et `v(s)`, alors

`e_b ≤ (r_a/r_b)e_a + (2D/3)(r_b²-r_a³/r_b)`.

**Preuve.** `f_U=(G_U-2)/(2s)≤-1/(2s)`. Pour `E=|U-v|`, la dérivée de Dini supérieure vérifie `D⁺E≤-E/(2s)+D`, y compris aux zéros par continuité. Multiplier par `sqrt(s)`, intégrer de `s_a=r_a²` à `s_b=r_b²`, puis diviser par `r_b` donne la formule. Elle est **exactement rationnelle** aux quatre rayons `1/4,1/2,7/10,17/20`, depuis `r_a=1/100`. Un défaut constant par cellule se chaîne sans extrapoler hors du tube. Le témoin jouet `G=U`, solution exacte `U=0`, approximation `v=c*s` sature exactement la borne avec `D=3c/2` et `e_a=c*r_a²`.

**Limite déterminante.** L'hypothèse physique `G_U≤1` n'est **pas** démontrée sur le tube Step55. Le défaut continu `D` de la solution dense DOP853, l'erreur initiale `e_a` et les enclosures physiques Step58 ne sont pas certifiés. Une pente négative supposée ne doit jamais être substituée à une enclosure vérifiée ; l'intégration ne constitue pas un rejeu Step58. Le centre `r=0` est exclu ; son raccord exige un traitement séparé. Aucune conclusion sur les six coefficients temporels, les lapses positifs aux deux bords, Dirac ou JANUS.

**Tests** : `PYTHONPATH=. python -m unittest discover -s tests -v` : 10 PASS ; `python -m compileall -q numerics tests` PASS. Tests rationnels jouets, non indépendants. Original Step55 **lu via connecteur GitHub et SHA contrôlé**, non exécuté ; Step45/46/55/58 et candidat cubique non rejoués dans l'environnement d'exécution (DNS direct GitHub indisponible).

**Étape suivante inchangée** : cinq originaux SHA authentifiés en environnement exécutable ; affine/cubique quatre rayons ; convergence et six coefficients A/B/E ; enclosures physiques `G_U`, défaut DOP853, erreur initiale ; centre/BVP lapses positifs aux deux bords ; Dirac, 4D, stabilité, observables. `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.

# JANUS b3c3d6 — budget d'erreur conditionnel du transport Step55→Step58 (30 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Avancée mathématique exacte mais **aucune borne physique calculée** et **aucun rejeu original Step58**.

## Résultat démontré (pour un RHS scalaire C² en y et C¹ en s)

Soit `U'=f(s,U)`, `h=s*-sf`, `y_num` la valeur numérique à `sf` et `|U(sf)-y_num|<=epsilon`.
Le transport quadratique est `T2(y)=y+h f(sf,y)+h²/2*(f_s+f_y*f)(sf,y)`.
Son dérivé exact en y est

`dT2/dy = 1+h f_y + h²/2*(f_sy+f_yy*f+f_y²)`.

Si sur le segment d'états entre `y_num` et `U(sf)` les bornes certifiées `|f_y|<=Ly`, `|f_sy|<=Lsy`, `|f_yy|<=Lyy`, `|f|<=F` tiennent, et si sur l'intervalle temporel la solution exacte est C³ avec `|U'''|<=M3`, alors

`|U(s*)-T2(y_num)| <= epsilon*[1+|h|Ly+h²/2*(Lsy+Lyy*F+Ly²)] + M3*|h|³/6`.

Preuve : théorème des accroissements finis appliqué à `T2` entre les deux états, puis Taylor-Lagrange le long de la solution exacte. Cette inégalité distingue l'erreur d'intégration déjà présente `epsilon` du reste d'extrémité. **Même à h=0, le budget reste epsilon**. Les petites valeurs de `|h|³` ne certifient donc rien sans `epsilon`.

## Spécialisation exacte à l'EDO Step55

Pour `f=(G(s,U)-2U)/(2s)`, `s>0` :

- `f_y=(G_U-2)/(2s)` ;
- `f_sy=G_sU/(2s)-(G_U-2)/(2s²)` ;
- `f_yy=G_UU/(2s)`.

Le facteur `1/s` rend **non uniforme au centre** un budget fondé uniquement sur ces bornes, sans étude de régularité et annulations propres au profil physique. La valeur initiale du candidat `U0+U1*s0+U2*s0²` à `s0=1e-4` n'a pas de borne de troncature physique démontrée ; le solveur DOP853 n'a pas de borne globale certifiée. Aucune valeur numérique des bornes `epsilon,Ly,Lsy,Lyy,F,M3` n'est proposée pour Step55.

## Tests et portée

`cd /mnt/data/janus_error_budget && PYTHONPATH=. python -m unittest discover -s tests -v` : **8 PASS, 0 FAIL**.
`python -m compileall -q numerics tests` : **PASS**. Jouets rationnels `G=2U+2s(3U+s)`, `G=2U+2s(U²+s)`, sensibilité affine atteignant la majoration, reste cubique exact, cas h=0, gardes de domaine. Tests locaux non indépendants ; originaux Step45/46/55/58 **non exécutés**.

Sources : `numerics/hr_b3c3d6_step55_transport_error_budget.py` et `tests/test_hr_b3c3d6_step55_transport_error_budget.py`. Aucun changement au candidat physique : il manque encore une enclosure de l'erreur de solveur, des dérivées du RHS et de la propagation vers les six coefficients `A_N,A_M,B_N,B_M,E_N,E_M`.

**Prochaine étape inchangée :** cinq sources SHA-authentifiées, vrai affine/cubique quatre rayons, convergence ODE et six coefficients, puis enclosures, centre/BVP lapses positifs deux bords, Dirac/4D/stabilité/observables. Ne pas confondre cette identité conditionnelle avec une validation de JANUS.

# JANUS b3c3d6 — audit de fidélité binary64 du RHS et transport d'extrémité (30 octobre 2026)

**Statut : progrès de reproductibilité numérique, PAS un résultat physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Défaut identifié dans le candidat Step58 actuellement publié

Dans `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py`, le RHS transmis à `scipy.integrate.solve_ivp` est `G(F(s),F(y[0]))` avec `F(x)=mp.mpf(str(x))`. Cela remplace les abscisses et les états binary64 effectivement fournis par SciPy par leurs représentations décimales courtes. L'intégration se déroule donc sur une grille binary64, mais l'évaluation du champ de vecteurs reçoit une valeur décimale légèrement différente. Au terme, `ur=F(sol.y[0,-1])` perd aussi l'exacte représentation binary64, et `G(F(radius)**2,ur)` mélange l'état du temps binaire `sf` avec le temps décimal `r²`. Ce défaut n'implique pas une erreur physique de taille déterminée : il manque une analyse de sensibilité et les annulations structurelles peuvent dominer.

## Correction mathématique isolée et testée

Le module `numerics/hr_b3c3d6_exact_binary_rhs_transport.py` fournit `exact_binary(float)=mp.mpf(float)`, qui préserve exactement le rationnel binary64, et un transport d'ordre 1 depuis le temps du solveur `sf` vers le carré décimal exact `s*=r²` :

`y(s*) = y(sf) + (s*-sf) f(sf,y(sf)) + O((s*-sf)^2)`.

Le décalage `s*-sf` est calculé exactement avec `Fraction`, sans passer par `str(sf)`. Cette formule est valable si le RHS est suffisamment régulier ; la constante du reste dépend des dérivées de la solution et n'est PAS majorée pour Step55. Le transport n'élimine ni les erreurs de troncature, ni l'erreur initiale, ni l'erreur de `solve_ivp`. Il n'est PAS intégré au candidat Step58 dans cette session, afin de ne pas annoncer une validation d'intégration non effectuée.

À `r=7/10`, `sf-s*=-1/112589990684262400` ; à `r=17/20`, `sf-s*=+7/225179981368524800`. À `1/4` et `1/2`, ces décalages sont nuls. Sur le jouet exact `y'=3y`, la partie de l'erreur de transport, après séparation de l'arrondi binary64 de `y(sf)`, est d'ordre quadratique en `delta`, et non linéaire.

## Reproductibilité et limites

Commande réellement exécutée : `cd /mnt/data/janus_endpoint_transport && python -m unittest discover -s tests -v` : **6 tests PASS, 0 FAIL**, plus `python -m compileall -q numerics tests` PASS. Les tests sont locaux, principalement rationnels et jouets, pas indépendants de la construction. Aucun des cinq originaux Step45/46/55/58 n'a été exécuté, aucun coefficient A/B/E physique recalculé, aucun BVP positif ni Dirac testé. DNS GitHub direct indisponible depuis le container ; connecteur GitHub opérationnel.

**Suite prioritaire :** matérialiser les cinq originaux SHA-authentifiés, intégrer puis tester `mp.mpf(float)` dans le RHS et la valeur terminale du candidat, transporter l'extrémité et comparer le candidat ancien/nouveau aux quatre rayons, avec convergence `s0`, `rtol`, `atol` et précision ; puis six coefficients A/B/E, factorisation/enclosures, centre et BVP deux bords, Dirac/4D/stabilité/observables. Aucun résultat de no-go ou validation JANUS ne découle de cet audit.

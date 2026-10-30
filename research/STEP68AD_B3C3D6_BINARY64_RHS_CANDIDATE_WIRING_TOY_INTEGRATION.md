# JANUS b3c3d6 — câblage RHS binary64 et transport du candidat cubique Step58 (30 octobre 2026)

**Statut : intégration du correctif de métrologie numérique, PAS rejeu original Step58. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Modification effectivement réalisée

Dans `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py`, le RHS SciPy utilise désormais `exact_binary(s)` et `exact_binary(float(y[0]))` plutôt que `mp.mpf(str(...))`. L'initialisation du polynôme à `s0=1e-4` utilise également le temps binary64 exact. La sortie `solve_ivp` est convertie exactement depuis son float, puis transportée au premier ordre vers `s*=Decimal(str(radius))**2` à l'aide du helper préexistant `transport_endpoint`; le jet Step55 `G(s*,U(s*))` et le calcul Step58 utilisent ainsi la même abscisse décimale cible.

Le décalage exact `s* - sf` vaut `0`, `0`, `+1/112589990684262400` et `-7/225179981368524800` aux rayons `1/4`, `1/2`, `7/10`, `17/20`. L'erreur du transport est quadratique en ce décalage **seulement sous hypothèse de régularité et avec borne des dérivées** ; aucune telle borne physique Step55 ni erreur globale de solveur n'est établie.

## Vérification exécutée et portée

Cinq tests `unittest` du **corps `u_solution` extrait par AST depuis une copie locale minimale du candidat**, et injecté dans un environnement jouet, ont passé, 0 échec final. La fonction publiée a été relue et comparée textuellement à cette copie (hors commentaires) ; les tests n'ont pas importé le candidat physique complet. Ils couvrent : extraction/compilation du corps publié, intégration SciPy DOP853 à quatre rayons de l'EDO jouet `U'=3U` (`G=2U+6sU`), fidélité des arguments binary64 du RHS, signe et valeur rationnelle du transport, conversion binary64 de l'abscisse initiale. `compileall` a passé. Cette approche évite d'importer les moteurs physiques originaux : les cinq tests sont **non indépendants et ne sont pas** une validation d'intégration de Step45/46/55/58.

Commande locale : `cd /mnt/data/janus_rhs_integration && python -m unittest discover -s tests -p 'test_hr_b3c3d6_candidate_rhs_binary_wiring.py' -v` (5 PASS, 0 FAIL), puis `python -m compileall -q numerics tests` (PASS). Environnement jouet local reproduisant exactement le corps `u_solution` candidat. Sur GitHub, le test AST pointe vers le candidat complet et peut être relancé avec le dépôt.

## Blocage restant et suite scientifique

Le conteneur n'a pas accès directement au DNS GitHub ; les cinq originaux SHA-authentifiés n'ont **pas** été matérialisés localement ni exécutés dans cette session. Le candidat physique cubique n'a pas été exécuté avec le véritable opérateur Step58 et les six coefficients A_N/A_M/B_N/B_M/E_N/E_M restent sans nouvelle mesure. Aucune factorisation/enclosure, borne de sensibilité ODE, solution de lapses positifs à deux bords, rang Dirac, dynamique 4D, stabilité ou observable n'a été établie.

**Étape suivante inchangée :** matérialiser les cinq originaux Step45/46/55/58 SHA-authentifiés, rejouer affine/cubique à 1/4,1/2,7/10,17/20 avec balayage `s0/rtol/atol`, comparer les six coefficients et tenter des enclosures. Ensuite seulement étudier le centre et le BVP positif à deux bords, puis Dirac/4D/stabilité/observables. `main`, `research/v2-flrw` et workflows restent hors périmètre.

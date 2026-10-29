# b3c3d6 — invariant exact des jets cubiques/quartiques pour Step58 (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Résultat **formel conditionnel**, pas de rejeu original Step58, pas de six coefficients physiques nouveaux.

## Sources authentifiées et portée

GitHub branche `research/gate2b-nonhomothetic-transfer`, HEAD lu à l'ouverture `8b7a0f1e0d2246eff8bcc14ea6c5d88f6dda74a6`. Sources originales lues via connecteur, blobs : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalisé `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 barrière `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step57 `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Ce sont des lectures authentifiées de blobs, **pas des imports Python originaux exécutés**.

Inspection du code Step58 : `X(q,q')`, `Xr=Dt(X)` dépend au plus de `q''`, `deltaZ` au plus de `q''`, `Dt(deltaZ)` au plus de `q'''` ; le terme direct de `C(q,q',z,z')` est d'ordre inférieur. Les symboles `q4` sont déclarés dans `Dt` mais ne sont pas atteints par les expressions renvoyées si les dépendances de Step45 sont bien celles inspectées. Ce contrat d'ordre provient d'une **lecture structurelle**, sans exécution/AST de la totalité des sources.

## Théorème exact de jet, indépendant de la solution physique

Au point `r0>0`, posons `d=r²-r0²`, `Uc=U0+U1 d+U2 d²/2+U3 d³/6`, `Uq=Uc+U4 d⁴/24`. Alors

`Uq-Uc=(U4/24)(r²-r0²)^4=O((r-r0)^4)`.

Pour toute fonction lisse `F(r,U)` et tout `k=0,1,2,3`, `∂r^k F(r,Uq)|r0=∂r^k F(r,Uc)|r0`. La première différence possible est

`∂r^4 [F(r,Uq)-F(r,Uc)]|r0=16 r0^4 U4 F_U(r0,U0)`.

En particulier `Δ pLf''''=16 r0^6 U4` pour `pLf=r²U`. Cela vaut aussi pour les champs construits avec `G(r²,U)` et leurs compositions rationnelles régulières. **Conséquence conditionnelle sur le code Step58 lu : le passage du jet cubique au jet quartique ne peut modifier aucun des six coefficients de l'opérateur original au point**, puisqu'il n'utilise que les jets radiaux d'ordre <=3. Ce n'est PAS une preuve que les coefficients cubiques sont corrects numériquement, ni qu'ils s'annulent.

## Contrôles réellement exécutés

`cd /mnt/data/janus_run11 && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 unittest PASS, 0 FAIL**, non indépendants. Cinq différences divisées SymPy exactes (U, pLf, pLfr, champ polynomial non linéaire, champ rationnel), deux calculs directs de quatrième dérivée, contrôles de non-annulation des différences d'ordre quatre. `python -m compileall -q numerics tests` : PASS. Un premier essai trop coûteux en expansion rationnelle a expiré ; l'algorithme final utilise les différences divisées et a terminé en moins d'une seconde. Aucun moteur original Step45/46/55/58 exécuté, aucun test d'intégration du candidat cubique.

## Livrables

- `numerics/hr_b3c3d6_cubic_quartic_step58_jet_invariance.py` — blob `2e6df2e83cfb25d46b48d39a6e24176ac6db346c`.
- `tests/test_hr_b3c3d6_cubic_quartic_step58_jet_invariance.py` — blob `0312ebdabeb2f0f12dc9d81f7bb13d8e9848690b`.

## Prochaine étape inchangée

**Rejouer vraiment** le candidat Step58 cubique avec les cinq sources originales SHA-authentifiées sur la solution Step55 aux quatre rayons `1/4,1/2,7/10,17/20` ; comparer les six coefficients affine/cubique et les résidus de coquille, contrôler la convergence de l'intégration depuis le centre. Puis factorisation exacte/enclosures globales, raccord central, lapses strictement positifs et **deux vrais bords**, pullback Dirac/générateurs/charges/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables. L'échec DNS local interdit ici le clone ; connecteur GitHub lecture/écriture fonctionne. Aucune modification de `main`, `research/v2-flrw` ni workflows.

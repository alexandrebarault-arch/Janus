# JANUS-005 — tangente exacte de la donnée centrale dans la famille PG-only (2026-11-11)

Source authentifiée au HEAD `6a54a388ae6e6433e6ab6b19a13a891a0cc49983` : `numerics/hr_step55_global_barrier.py`, blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Les lignes de définition donnent `A=0.4`, `Y=0.5787707228025044`, `B=A*Y`, `MF=0.10879548725**2`, `U0=MF*B*(PG/A-2*Z1)`.

En gardant les données prescrites A,Y,MF,Z1 constantes, la dérivée exacte est

`dU0/dPG=MF*Y=274023815147385251710689588080861/40000000000000000000000000000000000 > 0` (environ 0.0068505953786846315).

Commande réellement exécutée : Python standard `fractions.Fraction`, construction des quatre rationnels ci-dessus, calcul `MF*B/A`, impression de la fraction et contrôle `c>0` : PASS. Contrôle indépendant : simplification algébrique `B=A*Y` implique directement `MF*B/A=MF*Y`.

**Conséquence conditionnelle :** la variation PG-only du benchmark Step55 ne préserve PAS une condition supplémentaire imposant `U(0)=constante` lorsque PG varie et que A,Y,MF,Z1 sont prescrits. En revanche, Step55 choisit précisément `U0(PG)` : ceci n'est donc **pas** une contradiction interne ni une preuve qu'une véritable condition physique de bord fixe U0. Une condition centrale de régularité n'est pas nécessairement une condition de Dirichlet fixe. Aucune contrainte temporelle de Dirac ni condition aux deux vrais bords n'a été linéarisée ici.

**NEXT_ACTION_EXACT :** rechercher dans Step45/49/55 et les conditions de bord originales si U0 est libre, fixé, ou contraint par une relation de tir ; écrire le jacobien de ces contraintes en PG et U0, puis tester l'admissibilité du tangent. JANUS-001 : transfert authentifié des dépendances, tests puis pilote.

Nouvelles cellules physiques évaluées : 0 ; certifiées : 0. GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.

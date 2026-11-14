# JANUS-005 — identité exacte de la poussière g et direction à CG variable (2026-11-14)

Sources authentifiées au HEAD `d6663f6eb98ba0c6a2b746466120299275c41690` : `numerics/hr_step55_global_barrier.py` (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) et `numerics/hr_step49_analytic_center.py` (blob `d570948912885d45a625fa2db31c6a5435b6a654`).

Hypothèses : B=A Y, b0=0, MG=1, C=3 b1 Y+3 b2 Y²+b3 Y³, H2=3/(10 A³)+M2 C/3, A0=A³ C, A>0, H2>0. Step49 calcule `rho_g=3 A³ H2-24 A CG-M2 A0`. Simplification exacte :

`rho_g_center = 9/10 - 24 A CG`.

Il en résulte que la poussière centrale **ne dépend pas de M2 ni Z1** dans cette famille prescrite. La dérivée `-24 CG` du jalon précédent est une conséquence immédiate de la fixation de CG, et non une obstruction universelle.

Contrôle contradictoire : autoriser `dCG/dA=-CG/A` simultanément avec la tangente précédente `dM2/dA=-(4 A³ M2 C+9/10)/(A⁴ C)` et `dZ1/dA=-Z1/A` à Y, MF et b_i fixes. Alors `dPG=dU0=d(rho_g_center)=0` exactement. Cela fournit une direction **algébrique** non nulle préservant les trois données centrales. Elle ne prouve pas que CG soit libre physiquement ; modifier CG change les champs radiaux prescrits, donc les contraintes et les deux bords doivent être recalculés.

Autre vérification : au benchmark A=2/5, CG=3/2000, `rho_g=0.8856` exactement. Le seuil de test Step49 `rho_g>0.8855` impose, si CG reste 0.0015, `A<29/72≈0.4027778` (condition de cette assertion logicielle seulement, pas condition physique universelle). Si A CG est conservé, le test central reste inchangé.

Reproduction locale : `python /mnt/data/janus_audit_11/check.py`, SymPy PASS pour l'identité et quatre dérivées partielles, plus les trois dérivées totales. Le script est conservé dans `research/repro/janus005_cg_compensated_center_20261114.py`. **0 cellule physique b3c3d9 évaluée/certifiée/inconclusive**.

NEXT_ACTION_EXACT : tester la liberté de CG et la tangente compensée dans Step45/49/55, les six contraintes Dirac linéarisées et les deux véritables bords ; distinguer données initiales et paramètres de jauge. JANUS-001 : transférer les dépendances authentifiées et lancer neuf tests puis pilote physique.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

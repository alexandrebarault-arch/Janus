# JANUS-005 — La tangente PG/U0 constante modifie la poussière g centrale (2026-11-14)

**Source au HEAD initial** `53c0ac6a45ebee3a6785a17323171e1de8ab858b` : `numerics/hr_step55_global_barrier.py` (PG, U0, H2, A, Y, M2, CG) et `numerics/hr_step49_analytic_center.py` (expression `pg_center_normalized_exact`). Audit symbolique indépendant exécuté avec Python/SymPy.

Fixer Y, MF, b1,b2,b3, CG et prendre B=A Y. Poser C=3b1Y+3b2Y²+b3Y³, H2=3/(10A³)+M2 C/3, PG=-2A² sqrt(H2), U0=MF A Y(PG/A-2Z1). Le contre-exemple précédent donnait la tangente dA=1, dM2/dA=-(4A³M2C+9/10)/(A⁴C), dZ1/dA=-Z1/A, avec dPG=dU0=0.

**Nouvelle vérification :** la densité de poussière g centrale normalisée dans Step49 est `rho_g=3 A³ H2-24 A CG-M2 A0`, où `A0=A(2b1 A B+b2 B²)+B(b1 A²+2b2 A B+b3 B²)` pour b0=0. Par substitution exacte et dérivation totale le long de la tangente :

`d(rho_g)/dA = -24 CG`.

Le résultat est une identité symbolique exacte (pas une approximation). Pour CG=0.0015, `d(rho_g)/dA=-0.036`. Donc **si la densité centrale g est imposée et CG reste fixé et non nul**, cette tangente ne peut pas satisfaire simultanément dPG=dU0=d(rho_g)=0 sauf dA=0. C'est une obstruction conditionnelle de rang sur les données centrales, pas une preuve que la densité est physiquement fixée.

**Contrôle contradictoire :** la variation A précédente reste un contre-exemple valide si la densité centrale est autorisée à changer. De plus, si CG=0, cette obstruction particulière disparaît. La contrainte temporelle de Dirac, les deux vrais bords et la liberté des données de poussière n'ont pas été établis.

**Exécution locale :** `python /mnt/data/janus_audit/audit.py` : PASS (dPG=0, dU0=0, d rho=-24CG, valeur -0.036). Reproduction publiée : `python research/repro/janus005_center_dust_tangent_20261114.py` (octets GitHub non rejoués localement). **0 cellule physique b3c3d9 évaluée/certifiée/inconclusive**.

**NEXT_ACTION_EXACT :** déterminer dans Step45/49 et les vraies conditions aux bords si rho_g(0) est une donnée libre ou imposée ; calculer le rang du système de contraintes linéarisées incluant poussière et géométrie ; ne pas confondre fixation de données avec contrainte Dirac. JANUS-001 : reconstruire les sources originales, exécuter neuf tests et pilote à une cellule.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

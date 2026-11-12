# JANUS-005 — Sensibilité totale de Rhog et Psg à M2 (2026-11-12)

Source : `numerics/hr_step55_global_barrier.py` (`geometry(s)`, `H2`, `PG`) au HEAD initial `ec460cbc20746b061787f8bb19ad1c564a9fcccd`. Hypothèses : A,Y,B0..B4,CG,CF,KG,Z1,MG,MF constants, M2 variable, PG recalculé depuis Friedmann ; s=289/400. **Variation algébrique de données prescrites, non variation physique admissible démontrée.**

Poser `K=(B0+3 B1 Y+3 B2 Y²+B3 Y³)/3`, `H2=0.9/(3 A³)+M2 K`, `PG=-2 A² sqrt(H2)`. Identité exacte : `PG_M2=-A² K/sqrt(H2)`.

Avec les notations exactes de `geometry(s)`, poser `N=Gmom²/(4 MG Lg)-fac(s Dbar+Lg Gprime)-MG Lg³ Rg/2+s Z1 Dbar/Lg+Wgbar` et `beta=sqrt(1+KG²s)+s fac KG Lg`. Alors `Rhog=-N/beta`, `Psg=(s Dbar+Lg Gprime-Rhog s KG Lg)/Sgr`. Les dérivées totales exactes, incluant PG(M2), sont :
- `Rhog_M2=-(N_M2 beta-N beta_M2)/beta²`
- `Psg_M2=(s Dbar_M2+Lg Gprime_M2-s KG Lg Rhog_M2)/Sgr`.

**Exécution réelle :** script Python/SymPy construit depuis les formules originales avec `sympy.Rational`, `sympy.diff` puis substitution `M2=23.3348939346, s=289/400`. Contrôle indépendant numérique par différences centrales symétriques avec pas rationnel `1/1000000`, précision 30 chiffres. Trois assertions `abs(derivee_exacte-difference_centrale)<1e-10` : **3/3 PASS**.

| Quantité | Valeur | Dérivée totale M2 | Écart différence centrale |
|---|---:|---:|---:|
| PG | -0.763511009250883924 | -0.002889157783513448401 | 2.07e-20 |
| Rhog | 0.891457223294127148 | +0.000175463496980793729 | 4.58e-22 |
| Psg | -1.527800968806499136 | -0.005714211684519780010 | 4.14e-20 |

Le contrôle numérique ne constitue **pas** un certificat d'intervalle, et les signes sont ponctuels. Les dérivées totales diffèrent conceptuellement des dérivées partielles des sources à PG fixe. Aucune solution radiale paramétrique, aucun vrai bord, aucune contrainte Dirac ni cellule physique Step55/58 évaluée/certifiée.

**NEXT_ACTION_EXACT :** calculer `G_M2|U` et `G_U` depuis `normalized_symbolic()` authentique, puis résoudre/borner `2s (U_M2)'=(G_U-2)U_M2+G_M2|U` avec condition centrale différenciée ; tester les deux vrais bords et Dirac. JANUS-001 : transfert authentifié des modules, tests, pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

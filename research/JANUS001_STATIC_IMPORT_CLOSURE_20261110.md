# JANUS-001 — audit de fermeture des imports Python statiques (2026-11-10)

**HEAD fixé et lu :** `d685c0800d24ca0790661d14b48123d2742291ed`. **Méthode :** lecture des fichiers authentiques via connecteur GitHub `fetch_file` à ce commit ; parcours récursif des instructions textuelles `from .module import`, `from . import module` et `from numerics.module import` à partir de `numerics/hr_b3c3d9_annular_direct_enclosure.py`. Tous les chemins cités ci-dessous ont été réellement récupérés à ce SHA. Cette méthode n'est **pas** une analyse AST exhaustive des imports dynamiques ni des fichiers ouverts à l'exécution.

**Résultat vérifié :** 18 modules distincts accessibles, 37 références d'import relatives recensées, aucun chemin manquant parmi ceux recensés. Le blocage historique `hr_step55_global_barrier.py` est **résoluble par connecteur** (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) ; le fichier existe sur `main`, il manque seulement dans le checkout local historique. Les gardes d'authenticité des sources Step45/46/55/58 emploient des SHA de blobs Git calculés sur les octets locaux ; leur présence dans le code a été inspectée, mais **aucune comparaison aux octets locaux n'a été exécutée** dans ce cycle.

| Module (dans `numerics/`) | Blob GitHub |
| --- | --- |
| hr_b3c3d9_annular_direct_enclosure.py | b6fcee9e410b5702f94030ce8b0c6ec818004344 |
| hr_step55_global_barrier.py | a6e7004120d0a166a3a8973c2fbe1487a8eb70fe |
| hr_b3c3d6_monotone_physical_four_radii.py | c68eba7cf5eba4679c437b8d6c82d00455e2dbfa |
| hr_b3c3d7_step58_reduced_jet_order_audit.py | d5a3d214b586a238d275df281a0a03ca683ac774 |
| hr_b3c3d6_composed_dual_interval_jets.py | 170598ab5ceff3ba6e9fa26575b4c0fed3a36c0a |
| hr_b3c3d6_boundary_ANAM_interval_certificate.py | 7e998fbbda8f3854093d530dc5e7e07703d70624 |
| hr_step45_exact_physical_ward.py | 66aa43841dccfe4a5d586a49be9c10af3a67a10e |
| hr_step58_temporal_operator.py | 802c23aebd41780d8c462f1aa1711707fe4ee88f |
| hr_step55_normalized_secondary.py | a54a6acf2f7ad2f64c500faecfa1406ecbf7b862 |
| hr_b3c3d6_direct_first_partial_jet_enclosure.py | 7fc1a2b775e4407e2ba9f79ed8934ad588147b24 |
| hr_step46_exact_secondary_ode.py | bac025c28dbe1561c0c36c56dbfda46dc326f804 |
| hr_b3c3d6_physical_correlated_replay.py | 47a0c80cea2554daf62f3fea9ffb7f28421ae22c |
| hr_b3c3d6_authentic_bn_replay.py | fd3a76fffd78adcb585a24613b4e1357d1d00f5c |
| hr_step57_secondary_principal_symbol.py | bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f |
| hr_b3c3d6_dop853_dense_rational_defect.py | b1c8909983171b7161b28e68ca442d9a17c21cfc |
| hr_b3c3d6_correlated_tube_guard.py | 3801625ac5cb0a7681ade369f4c28b761bab73eb |
| hr_b3c3d6_bn_full_ideal.py | bc9b371c3d66f6b2491009e631fa4ed4a29a676f |
| hr_b3c3d6_bn_high_jet_elimination.py | 086b6bae543c0ee497ca9154c5a055921f018423 |

**Contrôle contradictoire / limites :** les modules récupérés contiennent des contrôles de provenance `read_bytes`, notamment `hr_step55_normalized_secondary.py`, `hr_b3c3d7_step58_reduced_jet_order_audit.py` et `hr_b3c3d6_authentic_bn_replay.py`. Un arbre d'imports complet ne garantit donc ni la présence de toutes les données externes ni le passage des gardes à l'exécution. **Tests nouveaux : 0 ; cellules physiques évaluées : 0 ; certifiées : 0 ; certificat global : aucun.** Aucun résultat physique revendiqué.

**NEXT_ACTION_EXACT :** transférer ces 18 fichiers textuels authentiques et le test `tests/test_hr_b3c3d9_annular_direct_enclosure.py` dans un checkout local ; auditer `read_bytes`/`open` et imports dynamiques ; comparer `git hash-object` aux SHA ci-dessus et aux SHA historiques requis ; exécuter `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v`, puis `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. En cas de blocage, poursuivre JANUS-005.

**Statut scientifique :** `GATE_2B = OPEN` ; `JANUS_R = NOT_VALIDATED`.

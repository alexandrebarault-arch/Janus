# JANUS-001 — audit de disponibilité des dépendances (2026-11-15)

HEAD figé : `1c1cca4cf432ce200cfcc1788cbc5103abb73d42`. Audit **statique** du dépôt par connecteur GitHub ; aucun fichier n'a été exécuté localement, aucun certificat physique obtenu.

Le moteur `numerics/hr_b3c3d9_annular_direct_enclosure.py` (blob `b6fcee9e410b5702f94030ce8b0c6ec818004344`) importe sept modules directs, tous effectivement lisibles au HEAD fixé :

| Module (dans numerics/) | SHA blob Git |
|---|---|
| hr_step55_global_barrier.py | a6e7004120d0a166a3a8973c2fbe1487a8eb70fe |
| hr_b3c3d6_monotone_physical_four_radii.py | c68eba7cf5eba4679c437b8d6c82d00455e2dbfa |
| hr_b3c3d7_step58_reduced_jet_order_audit.py | d5a3d214b586a238d275df281a0a03ca683ac774 |
| hr_b3c3d6_composed_dual_interval_jets.py | 170598ab5ceff3ba6e9fa26575b4c0fed3a36c0a |
| hr_b3c3d6_boundary_ANAM_interval_certificate.py | 7e998fbbda8f3854093d530dc5e7e07703d70624 |
| hr_step45_exact_physical_ward.py | 66aa43841dccfe4a5d586a49be9c10af3a67a10e |
| hr_step58_temporal_operator.py | 802c23aebd41780d8c462f1aa1711707fe4ee88f |

Six dépendances transitives également récupérées et inspectées :

| Module (dans numerics/) | SHA blob Git |
|---|---|
| hr_step55_normalized_secondary.py | a54a6acf2f7ad2f64c500faecfa1406ecbf7b862 |
| hr_b3c3d6_direct_first_partial_jet_enclosure.py | 7fc1a2b775e4407e2ba9f79ed8934ad588147b24 |
| hr_step46_exact_secondary_ode.py | bac025c28dbe1561c0c36c56dbfda46dc326f804 |
| hr_b3c3d6_physical_correlated_replay.py | 47a0c80cea2554daf62f3fea9ffb7f28421ae22c |
| hr_b3c3d6_authentic_bn_replay.py | fd3a76fffd78adcb585a24613b4e1357d1d00f5c |
| hr_step57_secondary_principal_symbol.py | bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f |

Trois dépendances supplémentaires ont ensuite été lues au même HEAD : `hr_b3c3d6_dop853_dense_rational_defect.py` (blob `b1c8909983171b7161b28e68ca442d9a17c21cfc`), `hr_b3c3d6_correlated_tube_guard.py` (blob `3801625ac5cb0a7681ade369f4c28b761bab73eb`) et `hr_b3c3d6_bn_full_ideal.py` (blob `bc9b371c3d66f6b2491009e631fa4ed4a29a676f`). Le dernier importe `hr_b3c3d6_bn_high_jet_elimination` : la fermeture reste ouverte. **Total : 16 modules de dépendances distincts inspectés, plus le moteur.**

La fermeture des imports **n'est pas achevée** : le module correlated_replay importe notamment `hr_b3c3d6_dop853_dense_rational_defect` et `hr_b3c3d6_correlated_tube_guard`; authentic_bn_replay importe `hr_b3c3d6_bn_full_ideal`. Les lectures de fichiers historiques par Path et leurs SHA requis n'ont pas encore été audités. Il serait erroné de conclure que 13 fichiers suffisent pour exécuter le moteur.

Environnement local contrôlé : Python avec SymPy 1.14.0, SciPy 1.17.0 et mpmath 1.3.0 importables. Commande `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` : `fatal: unable to access 'https://github.com/alexandrebarault-arch/Janus.git/': Could not resolve host: github.com`. Le connecteur GitHub fonctionne néanmoins.

**Résultat vérifié :** les 16 sources de la première partie du graphe sont présentes et lisibles au HEAD, avec blobs Git identifiés. **Non vérifié :** correspondance avec octets exécutés localement, fermeture des imports, sources historiques, tests et pilote. Cellules physiques évaluées/certifiées/inconclusives pendant ce cycle : **0/0/0**.

**NEXT_ACTION_EXACT :** poursuivre la fermeture récursive des imports et lectures Path jusqu'aux sources historiques ; transférer les octets des fichiers Git authentifiés et comparer `git hash-object` local aux SHA listés ; puis exécuter `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v` et, si l'environnement est authentique, `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. En cas de blocage persistant, reprendre JANUS-005/006 sur les contraintes de Dirac et les deux bords.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

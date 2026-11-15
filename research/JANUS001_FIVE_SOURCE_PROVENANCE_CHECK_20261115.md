# JANUS-001 — preuve de provenance des cinq sources verrouillées (2026-11-15)

HEAD de lecture : `f48183abd5a9bb2f47334e7aa7a2f818efdbca44`.

Audit statique indépendant des chemins effectivement appelés par `run_physical` dans `numerics/hr_b3c3d9_annular_direct_enclosure.py` (blob `b6fcee9e410b5702f94030ce8b0c6ec818004344`). Le runner appelle `authenticate_originals()` et `verify_sources()` **avant** la barrière Step55 et les cellules physiques. Leurs cinq SHA attendus ont été comparés individuellement aux blobs renvoyés par GitHub à ce HEAD :

| Fichier dans numerics/ | SHA attendu = SHA GitHub |
|---|---|
| hr_step45_exact_physical_ward.py | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| hr_step46_exact_secondary_ode.py | `bac025c28dbe1561c0c36c56dbfda46dc326f804` |
| hr_step55_normalized_secondary.py | `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` |
| hr_step55_global_barrier.py | `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` |
| hr_step58_temporal_operator.py | `802c23aebd41780d8c462f1aa1711707fe4ee88f` |

Résultat : **5/5 correspondances de blobs GitHub au HEAD**, donc aucun besoin démontré de récupérer une version historique différente pour ces cinq fichiers. Il reste à vérifier les octets effectivement transférés localement et la fermeture transitive.

La fonction `validate_archive` du module `hr_b3c3d6_boundary_ANAM_interval_certificate.py` est appelée par `enclose_all`, pas par `physical_jet`. Le runner invoque directement `physical_jet` ; l'archive JSON des quatre rayons n'est donc pas une dépendance directe de ce chemin, sous réserve de tout appel différé non encore découvert.

**Limites :** contrôle de provenance GitHub et de flot statique seulement ; aucune copie locale complète authentifiée, aucun test moteur nouveau, aucune cellule Step55/58 physique évaluée ou certifiée. Ce rapport ne constitue ni preuve d'exécution ni certificat de signe.

**NEXT_ACTION_EXACT :** récupérer les octets authentifiés des modules et leurs imports transitifs, vérifier chaque `git hash-object` local ; lancer `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v` puis `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. En cas de blocage de transfert, reprendre JANUS-005/006 sur Dirac et les deux vrais bords.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

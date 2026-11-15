# JANUS-001 — complément d'audit authentifié (2026-11-15)

HEAD de lecture : c12611b04582c85f98db0d1eb9003f4156a8ec95. Le module `numerics/hr_b3c3d6_bn_high_jet_elimination.py` est présent dans l'arbre Git : blob `086b6bae543c0ee497ca9154c5a055921f018423`, 3034 octets. Lecture complète : seul import top-level `sympy`. La chaîne `bn_full_ideal -> bn_high_jet_elimination` est donc fermée statiquement à ce niveau ; 17 modules de dépendance identifiés en plus du moteur, mais fermeture transitive totale NON prouvée.

Le moteur b3c3d9 appelle `physical_jet` directement ; le module boundary_ANAM possède séparément `validate_archive()` exigeant `research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json` (blob attendu `e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`). Le pilote ne déclenche pas directement `validate_archive` : ne pas imposer cet archive comme prérequis sans vérifier le chemin transitif. Le moteur commence par `certify_global_barrier(cells=256)` avant les cellules. Les neuf tests du fichier b3c3d9 ne testent que les fonctions rationnelles et restent synthétiques.

Deux tentatives réseau local : git ls-remote échoue `Could not resolve host: github.com` ; HTTPS Python raw.githubusercontent.com échoue `NameResolutionError`. Le connecteur GitHub lit les sources, mais aucun transfert local complet ni exécution physique n'a eu lieu. Tests SKIP ; cellules évaluées/certifiées/inconclusives : 0/0/0.

NEXT_ACTION_EXACT : auditer tous imports différés et Path atteints depuis run_physical ; transférer les octets authentifiés, comparer git hash-object ; lancer `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v` puis `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. Si transfert toujours impossible, poursuivre JANUS-005/006 Dirac/deux bords.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# JANUS-001 — rejeu authentifié des neuf tests b3c3d9 (2026-11-21)

## Provenance
HEAD GitHub initial : `e2255f7230d637ac5eb8c7283828bb93bbc55c8d`. Deux fichiers transférés textuellement depuis GitHub au SHA fixé dans un répertoire local temporaire, puis authentifiés par `git hash-object` :
- `numerics/hr_b3c3d9_annular_direct_enclosure.py` : `b6fcee9e410b5702f94030ce8b0c6ec818004344` (identique au blob GitHub).
- `tests/test_hr_b3c3d9_annular_direct_enclosure.py` : `13252b2bb83fe148c6aa0d04d08053f332654f1c` (identique au blob GitHub).

Python et SymPy 1.14.0 présents. Le module `numerics/__init__.py` local vide ne sert qu'à rendre importable le package pour les tests purement rationnels ; il n'est pas une dépendance physique ni une preuve Step55/58. Aucun shim de calcul physique.

## Commande et résultat
Depuis le répertoire local contenant les deux fichiers :
```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v
```
Résultat : **9 tests exécutés, 9 PASS, 0 FAIL, 0 SKIP**, durée rapportée 0.002 s. Les tests couvrent la couverture rationnelle exacte, les intervalles inversés, les signes stricts, les trous et recouvrements, et une solution analytique synthétique de `ode_jets`.

## Limites
**Aucune cellule physique Step55/58 n'a été exécutée**. Les dépendances transitives authentiques de `run_physical` ne sont pas encore transférées. Pilote SKIP, 256 cellules SKIP ; cellules physiques demandées pour une exécution effective 0, tentées 0, évaluées 0, certifiées 0, inconclusives 0. Les neuf tests sont synthétiques/rationnels et ne certifient aucun signe physique. Git CLI réseau : `Could not resolve host: github.com` ; transfert par connecteur GitHub réussi.

**NEXT_ACTION_EXACT :** récupérer au HEAD fixé les imports transitifs Step45/46/55/58 et les fichiers historiques exigés ; vérifier leurs blobs Git et les chemins de fichiers ouverts, puis lancer `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. En cas de blocage authentifié, poursuivre JANUS-005/006 (évolution Hamiltonienne, Dirac et deux vrais bords).

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

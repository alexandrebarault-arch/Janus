# JANUS-001 — Audit complémentaire des lectures de fichiers et dépendances (2026-11-11)

**HEAD des sources inspectées :** `87700c0e2b50455636e22d908d7136aed488f076`. **Nature :** audit de code source authentique via connecteur GitHub, sans exécution physique. Ce rapport complète `research/JANUS001_STATIC_IMPORT_CLOSURE_20261110.md`, qui couvrait 18 modules et 37 imports statiques, mais pas les lectures de fichiers ni les dépendances d'exécution.

## Résultats vérifiés
- `numerics/hr_b3c3d6_authentic_bn_replay.py:16-25` déclare **cinq** sources vérifiées par SHA Git, dont **`tests/test_hr_b3c3d6_bn_full_ideal.py`**, qui ne fait pas partie des 18 modules Python de l'audit précédent. Ce test existe sur `main`, blob `5862735ecc5c7c43e71ee3f6fec558fbab71a6a5`. La vérification est déclenchée par `verify_blob_provenance()`, elle-même appelée par `enclose_all()` dans le module de certificat AN/AM. Ne pas supposer que cette branche d'appel est exécutée par le pilote direct : `run_physical()` importe les types et fonctions du certificat mais ne fait pas directement appel à `enclose_all()`.
- `numerics/hr_b3c3d6_boundary_ANAM_interval_certificate.py:199-221` contient une lecture externe conditionnelle de `research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json`. Le fichier existe, blob `e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`. Cette lecture intervient dans `validate_archive()`, appelée par défaut par `enclose_all()`, **pas directement** dans le chemin `run_physical()` du pilote.
- `numerics/hr_b3c3d6_physical_correlated_replay.py` importe `scipy.integrate.solve_ivp` au chargement du module. Ce module figure dans la fermeture statique précédente : **SciPy est donc une dépendance à vérifier**, même si aucun intégrateur SciPy n'est invoqué directement par `run_physical()`.
- Les autres gardes de lecture explicite relevées parmi les 18 modules concernent les sources Step45/46/55/58 et sont documentées dans les dictionnaires `ORIGINAL_SHA`, `SOURCE_SHA` et `SOURCE_BLOBS`. Les SHA attendus ont été comparés aux métadonnées GitHub pour les fichiers inspectés ; **aucune comparaison avec les octets d'un checkout local n'a été réalisée**.
- Dans l'environnement Python du présent audit : Python `3.13.5`, SymPy `1.14.0`, SciPy `1.17.0`, mpmath `1.3.0` : imports et versions vérifiés par `python` ; cela **ne** prouve **pas** la compatibilité du moteur complet ni la reproductibilité à une version historique.

## Contrôle contradictoire
La fermeture d'imports du rapport précédent n'est **pas** une fermeture de toutes les dépendances de provenance : un fichier de test et un JSON de preuve sont lus sur certains chemins d'appel. Inversement, les déclarer indispensables au pilote serait excessif sans tracer les appels dynamiques. Les deux fichiers existent réellement sur GitHub ; aucun manque de source distante n'est démontré.

**Tests du moteur exécutés dans cette session : 0. Cellules Step55/58 évaluées : 0 ; certifiées : 0.** Aucune conclusion physique nouvelle.

## NEXT_ACTION_EXACT
1. Reconstruire dans un répertoire local les 18 modules au SHA fixé et `tests/test_hr_b3c3d9_annular_direct_enclosure.py` ; ajouter le test de provenance et le JSON d'archive si les appels authentiques l'exigent. Vérifier **les octets** par `git hash-object` contre chaque blob GitHub.
2. Exécuter `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v`.
3. Exécuter `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json` ; relever la première exception concrète, le rejeu de la barrière et le nombre de cellules réellement évaluées.
4. Si l'environnement authentique ne peut pas être reconstitué, poursuivre JANUS-005 avec un calcul mathématique falsifiable.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**

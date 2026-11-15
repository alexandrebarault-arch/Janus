# JANUS-001 — réconciliation du risque U_sss avec l'audit antérieur (2026-11-15)

HEAD source figé : `8ef3d76db868c0fca826042060b7bd9e247395db`.

## Observation contradictoire

Le rapport `JANUS001_THIRD_JET_COMPLETENESS_AUDIT_20261115.md` signalait que `pLf'''=24r U_s+36r³ U_ss+8r⁵ U_sss`, alors que `physical_jet` construit seulement le jet quadratique de U. Cette identité seule ne démontre **pas** que les coefficients de lapse sans dérivée `A_N=operator['N'][0]`, `A_M=operator['M'][0]` dépendent de `pLfrrr`.

Un audit symbolique antérieur, déjà présent au HEAD fixé, `numerics/hr_b3c3d7_step58_reduced_jet_order_audit.py` (blob `d5a3d214b586a238d275df281a0a03ca683ac774`), construit explicitement `dependency_rows()` à partir de `physical_operator()`. Il teste que `A_N` dépend de U au plus à l'ordre 1 et `A_M` au plus à l'ordre 2 ; il impose également l'absence des jets d'ordre quatre. `exact_shell_sensitivity()` donne, sur Fz=0 et la carte primaire Step46, `dA_M/dU_ss = 4*r**4*z*C1/Lf` et `dA_N/dU_ss=0`. Le code documente expressément que **la dérivée radiale de A_M**, et non A_M lui-même, requiert U_sss.

## Conclusion limitée

Le soupçon de terme U_sss omis dans les **valeurs** A_N/A_M est donc déjà contredit par l'analyse de dépendances exacte antérieure, sous réserve du rejeu de cet audit authentique. Le besoin de U_sss subsiste pour une barrière de monotonie basée sur dA_M/dr ; il ne doit pas être imposé automatiquement à la tentative directe de signe des valeurs A_N/A_M.

Contrôle effectué dans ce cycle : relecture des sources GitHub au SHA figé, dont `hr_step58_temporal_operator.py` (blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`), `hr_b3c3d6_boundary_ANAM_interval_certificate.py` (blob `7e998fbbda8f3854093d530dc5e7e07703d70624`) et le runner b3c3d9 (blob `b6fcee9e410b5702f94030ce8b0c6ec818004344`). Aucun audit symbolique complet n'a été exécuté dans ce cycle, faute de transfert local authentifié. CLI Git : `Could not resolve host: github.com`.

**NEXT_ACTION_EXACT :** transférer les sources authentiques puis exécuter `PYTHONPATH=. python -m numerics.hr_b3c3d7_step58_reduced_jet_order_audit` (ou sa fonction `audit()`) et les tests b3c3d9 ; si l'audit PASS, ne pas bloquer le pilote direct sur U_sss ; exécuter `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. Si la reconstruction reste bloquée, poursuivre JANUS-005/006 Dirac/deux vrais bords.

Tests unitaires : SKIP. Pilote : SKIP. Cellules physiques évaluées/certifiées/inconclusives : 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

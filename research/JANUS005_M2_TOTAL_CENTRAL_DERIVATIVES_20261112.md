# JANUS-005 — M2 : dérivées totales au centre (2026-11-12)

Source : `numerics/hr_step55_global_barrier.py`, HEAD initial `154ebfe99b9915e5864e9fbdee3a1f35d9d22b3b`. Retranscription indépendante des formules `geometry(s)` et `PG(M2)` ; Python/SymPy 1.14, commande `python /tmp/janus_center.py` (script local éphémère, non publié). Toutes les décimales ont été converties en rationnels exacts. Ceci n'est pas une exécution Step55/58.

Dérivées totales `d/dM2` à `s=0, M2=23.3348939346` (approximations décimales) :

| Quantité | dérivée |
|---|---:|
| PG | -0.002889157783513448 |
| U0 | -0.00001979245096002796 |
| Dbar | +0.00004008661680144791 |
| Wgbar | +0.008272139156907749 |
| Wfbar | -0.004998534870868035 |
| Rhog | **0 exactement** |
| Psg0 | -0.005778315567026897 |

Identités exactes contrôlées par SymPy : `dU0/dM2=MF*Y*dPG/dM2`, `dPsg0(0)/dM2=2*dPG/dM2`, `dRhog(0)/dM2=0` : **3 PASS**. Contrôle supplémentaire : `d_s d_M2 Rhog(0)≈+0.0002433824117500686` est non nul. Attention : `Rhog(0)` n'est pas identiquement zéro ; seule sa dérivée en M2 l'est. L'annulation résulte des contributions couplées PG et Wgbar ; geler PG ou Wgbar donne une variation erronée.

Conclusion limitée : une variation M2 affecte les données radiales et le premier jet de Rhog, malgré la stationnarité de Rhog au centre. Pas de conclusion sur les deux bords, Dirac ou la viabilité JANUS. Tests physiques rejoués : 0 ; cellules évaluées/certifiées : 0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

NEXT_ACTION_EXACT : authentifier Step45/46, former `G_M2(s,U)` par dérivation totale de `geometry(s)`, résoudre `2s δU_s=(G_U-2)δU+G_M2 δM2` avec `δU(0)=dU0/dM2 δM2`, puis vérifier deux vrais bords et Dirac. JANUS-001 : transférer les sources, vérifier les blobs, neuf tests et pilote.

# JANUS-005 — Jets radiaux cinq et six, contrôle contradictoire (2026-11-19)

**Portée : algèbre locale seulement ; aucune certification physique.** HEAD source `2b6d07802d484cf872d415e5ebd8e486630b1e44`. Source de formule : `research/repro/janus005_third_radial_jet_replay_20261115.py`, blob Git `4a83603fa13f00efc2a60f4f45ad26c55b97c797`. Un script local dérivé a recopié les constantes, `rho`, `jet`, `partial`, `base`, et la résolution linéaire `dKG,dCF` de cette source, puis prolongé la boucle à n=0..6. Ce script dérivé n'a pas été authentifié comme blob Git et ne doit pas être présenté comme un rejeu octet pour octet. Python mpmath 45 décimales.

## Résultats exécutés

`dKG/dA=0.07558748170439774118882804925531230708`; `dCF/dA=-0.0063634485820344413102374149423525733921`.

| Jet | D a_n (dA=1, compensation a1/a2) |
|---|---:|
| 0 | -7.37871222621036488908e-45 (zéro numérique) |
| 1 | -2.73691106313440834e-48 (zéro numérique) |
| 2 | 0 |
| 3 | +1.06859855966529402056407979307e-5 |
| 4 | -1.23211326921505438740229892665e-7 |
| 5 | +1.11461656290983974887106810954e-9 |
| 6 | -9.30497983377175945432032618869e-12 |

Différences finies centrées de `jet(n,p0+h*d)` et `jet(n,p0-h*d)` divisées par `2h`, avec h=1e-3 puis 1e-4 :

| n | erreur FD h=1e-3 | erreur FD h=1e-4 |
|---|---:|---:|
| 4 | -5.11131072189e-12 | -5.11057160419e-14 |
| 5 | +8.76191116318e-14 | +8.76061144028e-16 |
| 6 | -1.63871820558e-15 | -1.63854477836e-17 |

Rapport d'erreurs proche de 100 pour une réduction de h par 10, cohérent avec O(h²). Le contrôle FD réutilise la même expression `rho` : indépendant de l'opérateur de dérivation mpmath, mais pas de la formule de départ.

**Commande réellement exécutée :** `python /mnt/data/janus_cycle/jets.py`. Pour reproduire depuis le dépôt, partir du script source ci-dessus, remplacer `for n in (1,2,3)` par `for n in (0,1,2,3,4,5,6)`, retirer l'assertion qui ne convient qu'aux n<3, et calculer les différences finies centrées pour n=4,5,6 à h=1e-3 et 1e-4. Ne pas considérer ce protocole comme un script exact archivé.

**Limites :** sous-famille prescrite, paramètres KG/CF non démontrés physiquement libres, contraintes de Dirac et conditions aux deux vrais bords non testées ; les jets d'ordre 5 et 6 ne changent pas le verdict. Aucun test b3c3d9 ni pilote exécuté dans cette session ; 0 cellule physique évaluée, 0 certifiée, 0 inconclusive. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** JANUS-005/006 extraire les contraintes canoniques et les traces des deux bords, calculer la différentielle totale incluant variations géométriques/lapses, puis tester si la tangente KG/CF appartient au noyau du jacobien complet. JANUS-001 demeure BLOCKED pour le pilote tant que les sources historiques et dépendances authentiques ne sont pas reconstruites ; ne pas répéter le même échec DNS.

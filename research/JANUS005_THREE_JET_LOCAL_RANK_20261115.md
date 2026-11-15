# JANUS-005 — Rang local des trois jets radiaux (2026-11-15)

**Source figée :** `main=4cc75043fa2ed6a90c58052e1360bf0a69ddb2f5`. **Statut :** calcul algébrique local, NON certificat physique. `GATE_2B=OPEN`, `JANUS_R=NOT_VALIDATED`.

## Hypothèse et calcul

La famille de densité `rho(s,p)` et les paramètres numériques sont exactement ceux du script préexistant `research/repro/janus005_third_radial_jet_replay_20261115.py` (blob `4a83603fa13f00efc2a60f4f45ad26c55b97c797`). On définit `a_n = (d^n rho/ds^n)(0)/n!`, `s=r²`. La direction de base dans les quatre premiers paramètres est `v=(1,-(4*A**3*M2*C+0.9)/(A**4*C),-Z1/A,-CG/A)`; les deux colonnes restantes correspondent à `dKG` et `dCF`.

Le jacobien 3×3 est `D[n,:]=[sum_i (partial a_n/partial p_i)*v_i, partial_KG a_n, partial_CF a_n]`, pour `n=1,2,3`. Recalcul indépendant sous Python/mpmath 1.3.0, `mp.mp.dps=45`, à partir de la formule du script cité :

```
D =
[-0.086128507950055359946,  0.84414396724072850428, -3.5078135672202802825]
[ 0.000095289603187031398792,0.0042771372847821492474,0.065779998699050380255]
[ 0.000015284317766937654659,-0.000038996014304415650864,0.00025940677153668710621]
det(D[0:2,1:3]) = +0.070531189263328882598668903131564715
det(D) = +0.00000075369527258273493968183894735334654
```

**Contrôle indépendant :** produit du déterminant 2×2 par le résidu du troisième jet après compensation des deux premiers, publié et rejoué au cycle précédent : `0.07053118926332888 × 0.00001068598559665294020564 = 0.00000075369527258273491`, conforme au déterminant direct. Le signe et l'ordre de grandeur coïncident.

## Conclusion circonscrite

Le jacobien est de rang **3** au point prescrit : sur cette sous-famille différentiable à trois paramètres (variation de A avec M2/Z1/CG liés comme ci-dessus, et KG/CF libres), la carte vers `(a1,a2,a3)` est localement inversible. **Il n'existe pas de tangente non nulle dans cette sous-famille qui conserve simultanément les trois jets.** Ceci est une conséquence du théorème d'inversion locale, pas une obstruction universelle aux équations de JANUS.

Ce résultat ne démontre ni que les trois jets doivent être conservés physiquement, ni que cette sous-famille satisfait Dirac, les deux lapses, les deux vrais bords, la dynamique 4D ou Step55 global. Aucune cellule physique b3c3d9 évaluée, certifiée ou inconclusive durant ce calcul (0/0/0).

## Reproduction

Exécuter le script Git déjà archivé pour retrouver `rho`, `jet`, `partial`, `p0` et `base`, puis calculer :

```python
D = mp.matrix([[sum(partial(n,i)*base[i] for i in range(4)),partial(n,4),partial(n,5)] for n in (1,2,3)])
print(mp.nstr(mp.det(D),35))
```

**NEXT_ACTION_EXACT :** vérifier si les jets radiaux sont des données physiques imposées par les contraintes de Dirac et les deux vrais bords. Pour JANUS-001 : reconstruire les 18 modules authentifiés, vérifier leurs SHA, lancer les neuf tests et le pilote physique à une cellule.
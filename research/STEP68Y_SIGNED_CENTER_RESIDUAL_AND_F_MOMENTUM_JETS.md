# JANUS — STEP68y : signe strict du résidu central et jet canonique radial du secteur f

**25 octobre 2026 — branche de recherche uniquement.**  
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## 1. Résultat démontré et périmètre

Pour la **vraie branche analytique radiale** définie en Step49, et sous les certificats originaux Step67b/68u/68v, on obtient sur **0 < s=r² <= 1/1024** une nouvelle information que l'enveloppe symétrique Step68x n'utilisait pas :

`F0(s) = G(s,Ustar)-2*Ustar-2*s*Ustar_s < 0`,

où `Ustar=U0+U1*s+U2*s²` et l'EDO authentique Step45/46/55 est `2*s*U_s=G(s,U)-2*U`.

Les bornes rationnelles **globales sur le continuum**, en divisant par `s³`, sont :

```text
F0(s)/s³ ∈ [
 -104671973400629476166791119/800000000000000000000000000000000,
 -473550521560821294562534863/5000000000000000000000000000000000
] ⊂ (-∞,0)
environ [-1.30839966751e-7, -9.47101043122e-8].
```

Cela renforce la barrière déjà publiée en une **barrière SIGNÉE** :

```text
-10^-7 * s³ <= U(s)-Ustar(s) <= 0
```

Sur tout `0<s<=1/1024`, la borne supérieure est en fait strictement négative. Il s'agit d'un **résultat spatial** ; il ne dit rien, à lui seul, sur les signes temporels `A_N/r²,A_M/r²` ni sur le rang complet de Dirac.

## 2. Preuve par intersection de deux résidus indépendants déjà certifiés

Step68u a certifié, par dérivées troisièmes de la vraie EDO sur `[0,1/1024]`, les inclusions `Fplus(s)/s³∈[Plo,Phi]` et `Fminus(s)/s³∈[Mlo,Mhi]`, avec tous les jets de Taylor de degré inférieur nuls EXACTEMENT par la récurrence Step49. Les barrières sont `Ustar ± kappa*s³`, `kappa=1/10^7`.

Step68v a certifié `G_U ∈ [glo,ghi]` sur `0<=s<=1/64`, avec `glo<=ghi<0`, et a vérifié les quatre SHA originaux Step45/46/55. Les deux certificats ont été retrouvés OCTET-IDENTIQUES par leurs empreintes Git.

**Identités algébriques exactes**, avec théorème des accroissements finis :

```text
Fplus/s³ = F0/s³ + (gplus-8)*kappa
Fminus/s³ = F0/s³ + (8-gminus)*kappa

F0/s³ ∈ [Plo+(8-ghi)*kappa, Phi+(8-glo)*kappa]
F0/s³ ∈ [Mlo-(8-glo)*kappa, Mhi-(8-ghi)*kappa]
```

L'intersection rationnelle des deux dernières lignes donne l'intervalle ci-dessus, strictement négatif. Cet intervalle est lui-même inclus dans la borne plus large de `F0'''/6` publiée en 68v — contrôle supplémentaire.

Comme `U3<0` est certifié par Step67b, `U-Ustar<0` pour les petits `s>0`. Au premier contact éventuel avec `Ustar`, l'EDO impose `2*s*(U-Ustar)_s=F0(s)<0` : une remontée depuis des valeurs négatives est impossible. La borne inférieure de Step68u reste applicable. Le signe strict est donc conservé sur l'ensemble du petit centre.

## 3. Deux jets directement utilisables par le calcul physique temporel

Notons `d=U-Ustar`. Parce que `-kappa*s³<=d<=0` et `glo<=G_U<0` :

```text
2*s*d_s = F0(s) + (G_U-2)*d.
d_s/s² ∈ [
 -104671973400629476166791119/1600000000000000000000000000000000,
  4117968618087380149271638523/40000000000000000000000000000000000
]
≈ [-6.54200e-8, +1.02949e-7].
```

C'est plus serré que la borne symétrique antérieure Step68x `|d_s|/s²<=3.449385e-7`.

Pour la variable originale `V=G(s,U)=2*(U+s*U_s)` et `Vstar=2*(Ustar+s*Ustar_s)`, le signe `G_U<0` donne :

```text
(V-Vstar)/s³ ∈ [
 -104671973400629476166791119/800000000000000000000000000000000,
  117968618087380149271638523/20000000000000000000000000000000000
]
≈ [-1.308400e-7, +5.898431e-9].
```

**Jet de moment radial original** : `pLf(r)=s*U(s)`, `pLf_prime/r=V(s)`. Ainsi l'écart de `pLf` est dans `[-kappa*s⁴,0]`, et l'écart de la dérivée normalisée `pLf_prime/r` possède **l'intervalle signé précédent**. Les valeurs rationnelles de raccord en `r=1/32` et `r=1/64` sont dans le JSON machine. Ceci prépare des **données d'entrée plus fines** pour la vraie expression temporelle Step58, sans inventer des bornes de dérivées secondes/troisièmes.

## 4. Reproductibilité vérifiée

- Sources originales Git blob Step68u `aaacd0064e04cb0f5d596aa3df042a4c9a4c751d`, Step68v `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`. Ces DEUX JSON originaux ont été reconstruits en local et leur SHA Git byte-identique vérifié.
- Nouveau programme `numerics/hr_step68y_signed_center_residual.py` : **blob `6176382e73a383daa650fc007457020a3c906e05`**, vérifié après publication sur GitHub.
- Tests `tests/test_hr_step68y_signed_center_residual.py` : **blob `f7c94caff918b734a65c2e29d84d1f90f0acfb88`**, vérifié après publication.
- Rapport exact `research/reports/gate2b-step68y-signed-center-residual.json` : **blob `04271c360f2245142e171a5979db139ac4bdaf79`**, vérifié après publication.
- Exécution réelle : `8 passed in 0.09s` sous `timeout 12s` ; vérification négative des fichiers 68u/68v falsifiés ; tous les nouveaux fichiers exécutés et archivés sont octet-identiques.

Rejouer dans un clone COMPLET :
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. timeout --signal=TERM --kill-after=2s 12s python -m pytest -q tests/test_hr_step68y_signed_center_residual.py
PYTHONPATH=. python -m numerics.hr_step68y_signed_center_residual research/reports
```

## 5. Verrous qui demeurent, sans ambiguïté

Cette preuve réutilise les certificats de Step68u/68v : ce n'est PAS une seconde reconstruction indépendante du Hamiltonien non intégré par parties et ce n'est PAS une preuve de rang de Dirac.

**Étape suivante (68z)** : (1) recharger sources authentiques Step45/46/55/58 et Step68o ; (2) substituer **les enveloppes signées dépendantes de s** du vrai `U,U_s,V` ; (3) propager par la vraie ODE les jets `U_{ss},U_{sss}` avec cancellations de centre explicites — ne jamais les déduire en dérivant aveuglément une inégalité de valeur ; (4) tester l'anneau fermé `[1/64,1/32]`, puis `[1/128,1/64]`, avec preuves cellulaires rationnelles et file vide ; (5) prolonger au centre `r=0`, puis traiter les autres secondaires, lapses, bord, jauge, secteurs exceptionnels `J=0,K=0`, rang complet de Dirac et stabilité 4D.

**GATE_2B OPEN. JANUS_R NOT_VALIDATED.**

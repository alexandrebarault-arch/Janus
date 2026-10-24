# JANUS — Étape 68a : variations canoniques du shift jusqu'au deuxième jet radial

**24 octobre 2026** — branche de travail exclusive `research/gate2b-nonhomothetic-transfer`.
**GATE 2B TOUJOURS OUVERT ; JANUS-R NON VALIDÉ.**

## 1. Pourquoi cette étape est nécessaire

Les Steps66/67 ont certifié les valeurs et les dérivées du **profil de fond** du déplacement relatif sur le benchmark positif Step55 : `z=r/250, z'=1/250, z''=0`. Les Steps57/58 ont au contraire établi que la vraie secondaire physique `C(q,q',z,z')` dépend de `z'` et que son évolution de Dirac dépend de **la variation hamiltonienne** `delta_H z'`. On ne peut pas éliminer celle-ci à partir de `z''=0` sur le fond.

Le fichier authentique Step58 (`numerics/hr_step58_temporal_operator.py`, blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`) a été **lu sur GitHub**, et non exécuté dans le nouvel environnement isolé : il utilise `delta z=Z_D delta D_g+Z_K delta K`, puis dérive radialement `delta z`. L'objectif nouveau est une formulation **régulière au centre**, exploitable sans inverse apparent de `r²` et conservant cette réponse fonctionnelle.

## 2. Hypothèses exactes — ne pas généraliser

Sur la seule famille initiale Step55, le changement de variables de parité radiale est :

```text
s=r², Dg=r³ d(s), K=r² k(s), z=r*w0, w0=1/250,
0<=r<=17/20, k>229/1000, t=1-s*w0²>0.
```

Ces prémisses, y compris existence et positivité globale, proviennent des certificats antérieurs Steps49–55 ; **elles ne sont pas redémontrées** ni physiquement réimportées ici. Posons `e_d=delta d`, `e_k=delta k`, et `k1=k_s`, `k2=k_ss`. Les variations sont des variables libres lisses respectant les puissances de parité requises, pas encore les variations générées par le vrai Hamiltonien sur la surface complète des contraintes.

## 3. Résultat 68a-A : opérateur fonctionnel exact et régulier

La stationnarité normalisée de Step66, `Fhat=d-k*w/sqrt(1-sw²)=0`, impose à premier ordre :

```text
delta w = A*e_d+B*e_k
A=t^(3/2)/k
B=-w0*t/k.
```

Cette expression est aussi **l'identité algébrique** obtenue par substitution dans la formule d'origine Step58 : `Z_D=t^(3/2)/(r²k)`, `Z_K=-w0*t/(rk)`, `delta Dg=r³e_d`, `delta K=r²e_k`. Le produit simplifie `delta z=r delta w` et a une limite centrale régulière.

Les dérivées totales du fond, **avec w0 constant mais k(s) variable**, sont exactement :

```text
A_s=-3w0² sqrt(t)/(2k)-t^(3/2)*k1/k²
B_s= w0³/k+w0*t*k1/k²

A_ss=3w0⁴/(4k sqrt(t))+3w0² sqrt(t)*k1/k²
     +t^(3/2)*(2k1²/k³-k2/k²)
B_ss=-2w0³*k1/k²+w0*t*(k2/k²-2k1²/k³).
```

Il en résulte la formule opérationnelle complète :

```text
delta w_s  = A_s*e_d+B_s*e_k+A*e_d_s+B*e_k_s
delta w_ss = A_ss*e_d+B_ss*e_k+2A_s*e_d_s+2B_s*e_k_s
             +A*e_d_ss+B*e_k_ss

delta z    = r*delta w
delta z'   = delta w+2s*delta w_s
delta z''  = 2r*(3*delta w_s+2s*delta w_ss).
```

**Au centre**, si les entrées sont `C²` en `s` et `k(0)>0` :

```text
delta z'(0) = [e_d(0)-w0*e_k(0)]/k(0),
delta z''(0) = 0.
```

Le fait que `delta z''(0)=0` résulte de la parité : **cela n'autorise pas** à annuler `delta z'` ou ses dérivées ailleurs, ni à les annuler dans l'opérateur temporel six-paires de Step58.

## 4. Test négatif falsifiable

À un point central algébrique admissible (`k(0)=1/2, k_s(0)=k_ss(0)=0, e_d(0)=1, e_k(0)=0` et jets perturbés supérieurs nuls), on obtient EXACTEMENT :

```text
delta z'(0)=2 !=0,
lim_(r->0) [delta z''(r)/r]=-9/31250 !=0.
```

Ce test démontre que le **gel des variations** à cause de `z''_fond=0` serait faux. Ce point n'est PAS annoncé comme une perturbation satisfaisant tous les liens primaires/secondaires ; il contrôle l'opérateur algébrique.

## 5. Programme, contrôle de provenance et tests

- Source testée : `numerics/hr_step68a_normalized_shift_variations.py`, Git blob **`ea4376a23d7c59b353986022ed23d6d3edf8a7ad`**.
- Tests ciblés : `tests/test_hr_step68a_normalized_shift_variations.py`, Git blob **`3484e6da8bcdd3d2671e0d79042c2b85d0a8d5bd`**.
- Rapport : `research/reports/gate2b-step68a-report.json` (rapport de résultats conservant les limites).
- Manifeste brut généré localement : SHA256 **`92db7cfefefbbc6a1393834aec8d377e000d1f7359d39dd0640bd8b9aabc1bfa`**.

Les DEUX Git blobs source/test ont été relus via connecteur et correspondent octet pour octet aux fichiers réellement exécutés. Environnement reconstruit pour ce tour : `/mnt/data/janus-step68a`. Exécution réellement accomplie :

```bash
PYTHONPATH=/mnt/data/janus-step68a OPENBLAS_NUM_THREADS=1 \
python -m pytest -q /mnt/data/janus-step68a/tests/test_hr_step68a_normalized_shift_variations.py
# 20 passed in 4.46s
```

Deux premiers contrôles ont échoué par comparaison directe de deux expressions SymPy mathématiquement égales ; l'égalité a été corrigée en `simplify(lhs-rhs)==0` et les 20 tests sont ensuite passés. Les équations physiques n'ont pas été modifiées pour obtenir ce passage.

**Limitation cruciale :** le présent programme autonome reconstruit et teste les identités exactes de réponse, mais **n'importe pas** ni ne lance l'action physique originale Step45, le certificateur Step55, ou l'opérateur complet Steps57–60. Ce n'est ni un nouveau rang de Dirac, ni une preuve d'absence du fantôme BD, ni une validation cosmologique. Aucun workflow GitHub Actions n'a été réactivé.

## 6. Point de reprise technique exact — véritable Step68b

1. Reconstituer en UN SEUL environnement les sources GitHub byte-identiques Steps45/46/55/57/58/59/60/63/64/65/67b et leurs dépendances, avec le manifeste existant `research/reports/gate2b-step68-source-preflight.json`. En premier lieu, authentifier et exécuter les tests originaux pertinents avant d'appliquer cette transformation.
2. Depuis `physical_operator()['delta_Dg']` et `['delta_K']` de Step58, vérifier explicitement la parité `delta Dg=r³e_d`, `delta K=r²e_k` sur la vraie solution Step55 pour chaque coefficient `N,N',M,M'`, sans supposer cette parité hors domaine.
3. Calculer `e_d,e_k` et leurs jets en prenant le **vrai champ hamiltonien des douze variables canoniques**, puis appliquer les formules nouvelles `delta z,delta z',delta z''`. Toutes les dérivées des coefficients `k_s,k_ss` nécessitent les bornes physiques issues de la vraie géométrie.
4. Sur `Fz,Hg,Hf,Ddiag,C,C',Hg'=0`, réduire `A_N,B_N,A_M,B_M`, traiter les bords et construire un oracle Poisson temporel indépendant **non intégré par parties**, calculer rang/lapses. Ne pas perdre la variation `delta z'` sous prétexte que `z''_fond=0`.
5. Chartes `K=0`, `J=0` séparées, puis seulement questions de fantôme, évolution 4D et prédictions physiques.

**État scientifique préservé : GATE_2B OPEN — JANUS-R NOT_VALIDATED.**

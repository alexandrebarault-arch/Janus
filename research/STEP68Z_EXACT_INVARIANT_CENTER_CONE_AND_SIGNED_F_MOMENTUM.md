# JANUS — STEP68z : cône invariant rationnel au petit centre (profil radial f)

**2026-10-25 — recherche, branche `research/gate2b-nonhomothetic-transfer` uniquement.**  
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## 1. Vrai problème et dépendances authentifiées

Il s'agit EXCLUSIVEMENT de la branche spatiale analytique Step49, paramétrée par `s=r²`, avec la vraie EDO réduite de Step45/46/55 :

```
2*s*U_s = G(s,U) - 2*U,
Ustar = U0 + U1*s + U2*s²,
F0(s) = G(s,Ustar) - 2*Ustar - 2*s*Ustar_s.
```

Les trois rapports **octet-identiques à GitHub et vérifiés par SHA** sont :

- Step68u : `aaacd0064e04cb0f5d596aa3df042a4c9a4c751d` (U3 exact encadré, récurrence analytique et barrière).
- Step68v : `d83a3b80862a2e990a4c4879ec8745a4e91c8b34` (borne signée `G_U` sur la vraie bande).
- Step68y : `04271c360f2245142e171a5979db139ac4bdaf79` (résidu `F0/s³<0`, domaine `0<s<=1/1024`).

Ce calcul N'EST PAS une réexécution de Step58, ni une validation indépendante de tous les certificats d'amont.

## 2. Cône invariant mathématique

Poser `d=U-Ustar=s³*h`, `f(s)=F0(s)/s³`, et `g(s)` la pente sécante `[G(s,U)-G(s,Ustar)]/[U-Ustar]`, dont les bornes sont celles de `G_U` sur la bande. Par passage continu au centre, ces quantités ont des valeurs régulières. L'EDO VRAIE donne exactement

```
2*s*h_s = f(s)+(g(s)-8)*h.
```

Avec les bornes CERTIFIÉES `flo<=f<=fhi<0`, `glo<=g<=ghi<0`, on pose

```
h_lower = flo/(8-ghi) ; h_upper=fhi/(8-glo).
```

Pour tout `f,g` dans le rectangle, `f+(g-8)*h_lower >= 0`, et `f+(g-8)*h_upper <= 0`. Vérification des quatre coins en fractions exactes. Le coefficient analytique initial `U3` de Step67b/68u satisfait `h_lower<=U3<=h_upper` EXACTEMENT. La comparaison sur `s>0`, avec continuité et existence analytique Step49 au centre, préserve ce cône fermé jusqu'à `s=1/1024`. Ce n'est PAS une simple différentiation d'une inégalité.

**Bornes exactes certifiées :**

```
(U-Ustar)/s³ in [
 -104671973400629476166791119/7195089541176515764100055780800000,
 -473550521560821294562534863/45030426760826663318804444937500000
]
~[-1.454770e-8,-1.051623e-8]  (contre [-1e-7,0] en Step68y).
```

## 3. Dérivées et signe du moment CANONIQUE

De l'EDO, avec `h` enfermé dans le cône, on tire SANS différencier une borne d'erreur :

```
(U_s-Ustar_s)/s² = [f+(g-2)*h]/2
 in [-4.967791e-8,-2.548924e-8]   STRICTEMENT NÉGATIF.

[G(s,U)-G(s,Ustar)]/s³ = g*h
 in [+1.045168e-8,+1.463623e-8]   STRICTEMENT POSITIF.
```

**POINT D'AUDIT ESSENTIEL :** `Vstar=2*(Ustar+s*Ustar_s)`, donc **`G(s,Ustar) != Vstar`** puisque `F0(s)=G(s,Ustar)-Vstar` est STRICTEMENT négatif. Pour le **vrai moment physique `pLf_prime/r=G(s,U)`**, l'écart au polynôme référent `Vstar` est

```
G(s,U)-Vstar = F0(s) + g*(U-Ustar).
[G(s,U)-Vstar]/s³ in [-1.203883e-7,-8.007388e-8]  STRICTEMENT NÉGATIF.
```

Cette dernière borne est strictement comprise dans la borne plus large du Step68y, qui croisait zéro. Confondre `G(s,U)-G(s,Ustar)` avec `G(s,U)-Vstar` inverserait le signe : **les distinguer partout dans les jets Step68o**. L'exact contenu rationnel à conserver pour chacune des quatre inclusions figure dans le JSON machine.

## 4. Reproductibilité ET incident corrigé avant clôture

- Source `numerics/hr_step68z_invariant_center_cone.py`, Git blob **`8c3a46b44e5c55c7b8f464668f9e8dc7d17eae8b`**.
- Tests `tests/test_hr_step68z_invariant_center_cone.py`, Git blob **`33d20c7e109d1066372292558c17c1a4862346cc`**.
- Certificat `research/reports/gate2b-step68z-invariant-center-cone.json`, Git blob **`38f55aabf7a7c47c812f32db684f50ffbaf16374`**.
- **8 tests réellement exécutés et réussis en 0.05 s**, à partir des TROIS JSON d'amont reconstitués en local octet-identiques à GitHub (SHA vérifiés).
- Un PREMIER essai a échoué au test authentique parce que la différence auxiliaire `G(U)-G(Ustar)` avait été prise à tort pour la différence physique `G(U)-Vstar` ; cette tentative et sa correction sont documentées ici. Code et tests publiés ont été corrigés ; les blobs finaux ont été vérifiés comme identiques au code réellement testé. Ce contrôle est précisément ce qui empêche une conclusion non justifiée.
- Reproduction dans le dépôt complet :

```bash
PYTHONPATH=. python -m pytest -q tests/test_hr_step68z_invariant_center_cone.py
PYTHONPATH=. python -m numerics.hr_step68z_invariant_center_cone research/reports
```

## 5. Suite prioritaire : HARD RED STEP68aa

1. Recharger les véritables sources Steps45/46/55/57/58/60 et **Step68o** avec vérification des SHA et provenance, sans confondre les deux références `G(Ustar)` et `Vstar`.
2. Construire le jet réel de `U_{ss},U_{sss}` en différentiant l'EDO **symbolique/analytique**, avec quotient et annulations réorganisées à `s=0`; INTERDIT de dériver directement les intervalles des écarts.
3. Substituer les nouvelles bornes **signées dépendantes de `s`** dans les douze jets canoniques du Hamiltonien original non figé. Normaliser les puissances de `r` avant de faire les calculs d'intervalles de `A_N/r²`, `A_M/r²`.
4. Certifier **exhaustivement et sans trous** les anneaux `[1/64,1/32]` et `[1/128,1/64]`, puis le centre ; ne pas recycler comme preuve complète les 7 cellules PENDING du Step68u.
5. Enfin les autres secondaires, le rang de Dirac COMPLET, les lapses, bords/jauge et chartes exceptionnelles `J=0,K=0`, stabilité 4D et confrontation observationnelle.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Aucun résultat de rang Dirac temporel nouveau n'est revendiqué dans Step68z.

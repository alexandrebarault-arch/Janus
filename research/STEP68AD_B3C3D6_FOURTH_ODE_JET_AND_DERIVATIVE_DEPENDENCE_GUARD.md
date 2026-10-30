# b3c3d6 — quatrième jet exact de Step55 et garde sur les champs dérivés (30/10/2026)

**Statut : résultat FORMEL exact, non physique ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Lecture en direct du HEAD de reprise `7f3c885e612881f047e738549d55306b210dbadb`, du checkpoint et de l'état. Sources originales inspectées par le connecteur : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55-normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; leurs moteurs physiques n'ont PAS été exécutés.

## Résultat mathématique

Pour `2s U_s=G(s,U)-2U` avec `s0>0`, les dérivées `u1,u2,u3` sont celles du module existant `hr_b3c3d6_ode_consistent_jet_map.py`. Le quatrième jet exact est

```
2s*u4 = G_sss + 3 G_ssU*u1 + 3 G_sUU*u1^2 + G_UUU*u1^3
       + 3 (G_sU+G_UU*u1)*u2 + (G_U-8)*u3 .
```

Pour `h=s-s0`, le cubique `Uc=u0+u1*h+u2*h²/2+u3*h³/6` et le quartique `Uq=Uc+u4*h⁴/24` ont les mêmes jets radiaux d'ordres 0 à 3 **pour tout champ lisse F(r,U)**. Ce constat ne s'étend PAS automatiquement à un champ dépendant de `U_s` : `pLf'=d(r²U)/dr=2rU+2r³U_s` vérifie exactement

```
(d³/dr³)[pLf'_quartique-pLf'_cubique] à r0 = 16*r0^6*u4 .
```

Le résidu normalisé `H=2U+2sU_s-G(s,U)` du cubique a `H=H'=H''=0` au point et `H'''_r=-16*r0^5*u4` ; le quartique a les quatre jets `H,H',H'',H'''_r` nuls. La distinction est importante car le candidat Step58 utilise `pLf'` pour construire les champs secondaires `pSf,pf` et leurs dérivées, tandis que l'opérateur original manipule des jets canoniques jusqu'à l'ordre 3. **Il faut examiner les dépendances et annulations exactes des coefficients Step58 avant d'affirmer que le cubique suffit ou que le quartique change les six coefficients physiques.** Aucune de ces deux affirmations n'est ici démontrée.

## Tests et témoin

11 tests SymPy rationnels réellement exécutés, 0 FAIL final ; `python -m compileall -q numerics tests` PASS. Témoin non physique `G=s²+u²+s*u`, `s0=1/4,u0=1/2` : `(u1,u2,u3,u4)=(-9/8,131/16,-2343/32,59331/64)`. Vérifications indépendantes dans la mesure du possible : récurrence par dérivation totale, résidu aux ordres 0–3, champ dérivé négatif et solution polynomiale exacte. Tests jouets, pas de calcul des coefficients Step58 ni de borne de résidu continu DOP853.

Fichiers : `numerics/hr_b3c3d6_fourth_jet_holonomic_guard.py`, `tests/test_hr_b3c3d6_fourth_jet_holonomic_guard.py`. SHA blobs Git attendus respectivement `de8a44e698386edc17eabc28ec9339160fcad58f` et `59a6632c7d838f5acca30ba4d3bf3b38d696b8a0` (à confirmer par relecture).

**Prochaine étape inchangée :** exécuter les cinq originaux SHA-authentifiés et le vrai Step58 affine/cubique aux quatre rayons 1/4, 1/2, 7/10, 17/20 ; ajouter un contrôle quartique si la dépendance aux troisièmes jets de champs dérivés est réelle ; certifier défaut continu, erreur initiale, six coefficients A/B/E, puis BVP positif deux bords, Dirac, 4D, stabilité et observables.

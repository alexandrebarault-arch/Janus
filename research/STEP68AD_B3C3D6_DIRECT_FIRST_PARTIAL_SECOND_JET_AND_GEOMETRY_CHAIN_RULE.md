# b3c3d6 — alternative exacte : enclosure directe du second jet avec dérivées premières (31 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED. Résultat mathématique conditionnel, NON certificat physique Step58.**

## Théorème exact

Sur un rayon exact `s=r²>0`, l'EDO Step55 `2s U_s=G(s,U)-2U` donne, en posant `F=(G-2U)/(2s)` :

```
U_s  = F
U_ss = [G_s+(G_U-4)F]/(2s)
pLf''(r) = G+2s G_s+G_U(G-2U)
pLf(r)=s U ; pLf'(r)/r=G.
```

Supposons que, **au même s exact**, des intervalles sortants physiquement certifiés enferment `U`, `G(s,U)`, la dérivée partielle **physique** `G_s(s,U)` à U fixe, et `G_U(s,U)`. Leur évaluation en arithmétique d'intervalles rationnels des trois expressions ci-dessus enferme rigoureusement `U_s`, `U_ss` et `pLf''`. **Aucune borne de `G_sU` ni `G_UU` n'est nécessaire pour cette voie directe.** En contrepartie les boîtes peuvent être larges, notamment si le tube `U` est large ou les dépendances corrélées sont perdues. Les bornes mixtes de la session précédente restent utiles pour une **borne d'erreur fine relative au candidat** ; elles ne sont pas nécessaires pour obtenir une première enclosure absolue.

## Précaution déterminante : dériver la géométrie prescrite

Le fichier original `numerics/hr_step55_normalized_secondary.py` expose une expression `E(s,U,v_1,...,v_k)` où les `v_i` sont des symboles auxiliaires (Lg0, Lf0, Sgr0, etc.). Le vrai champ physique est `G(s,U)=E(s,U,v_1(s),...,v_k(s))`. Donc

```
G_s = E_s + sum_i E_{v_i} v_i'(s)      [U maintenu fixe]
G_U = E_U
G_sU = E_sU + sum_i E_{v_i U} v_i'(s).
```

**Ne pas** confondre `E_s` en tenant la géométrie fixe et `G_s` du Step55 physique. Par exemple, `E=a U²+b s`, `a=1+s²`, `b=1/(1+s)` donnent `G_s=2sU²+1/(1+s)²` tandis que `E_s=b` : l'écart est non nul. Ceci est un test de chaîne **JOUET**, pas un défaut constaté dans un ancien certificat physique : les sessions précédentes n'avaient précisément pas certifié `G_s`.

## Provenance et vérifications

Sources originales relues via le connecteur GitHub sur la seule branche de recherche :
- Step45 `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ;
- Step46 `numerics/hr_step46_exact_secondary_ode.py` blob `bac025c28dbe1561c0c36c56dbfda46dc326f804` ;
- Step55 `numerics/hr_step55_normalized_secondary.py` blob `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` ;
- Step55 barrière `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

Exécuté localement : `PYTHONPATH=/mnt/data/janus_b3c3d6_direct python -m unittest discover -s /mnt/data/janus_b3c3d6_direct/tests -v` : **10 PASS, 0 FAIL** (deux résidus SymPy généraux, tests chaîne géométrique, 101 points rationnels jouets inclus dans un test, erreurs de domaine). `python -m compileall -q` des nouveaux modules/tests : **PASS**. Code et tests GitHub relus et leurs SHA blobs **identiques aux octets exécutés** :
- `numerics/hr_b3c3d6_direct_first_partial_jet_enclosure.py` : `7fc1a2b775e4407e2ba9f79ed8934ad588147b24` ;
- `tests/test_hr_b3c3d6_direct_first_partial_jet_enclosure.py` : `2ab052e40d03678074a947e959f1ac11ce47b755`.

**NON EXÉCUTÉ CETTE SESSION :** le moteur original Step45/46/55/58, le rejeu physique DOP853, les quatre extractions P(s), les intervalles physiques G_s/G_U/G/F, les six enclosures Step58 et le BVP de lapses positifs. Aucune valeur de `G_s`, `U_ss` ou `pLf''` physique n'est certifiée par ce travail.

## Prochaine expérience prioritaire

Rejouer les originaux SHA-authentifiés et DOP853 aux quatre rayons exacts `1/4,1/2,7/10,17/20`. Construire **la dérivée totale composée** `G_s` de la géométrie Step55 ; l'encloser avec `G,G_U,U` sur les tubes communs, puis calculer d'abord les enclosures directes `U_ss,pLf''`. Comparer ensuite avec les budgets fins utilisant `G_sU,G_UU` si nécessaire. Propager vers les six coefficients Step58, factoriser les éventuels zéros et traiter le BVP strictement positif à deux vrais bords, puis Dirac/4D/stabilité/observables. **Ne jamais inférer un coefficient physique d'une seule identité conditionnelle.**

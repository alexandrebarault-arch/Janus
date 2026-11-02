# JANUS — b3c3d7 : ordre exact des jets Step58 sur la carte Step55 (02/11/2026)

**Statut : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Résultat exact de structure, **pas** une certification des signes physiques sur un continuum. Les sources originales Step45, Step46 et Step58 ont été relues sur `main`, copiées octet pour octet dans un mini-arbre local et authentifiées par leurs SHA Git : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `bac025c28dbe1561c0c36c56dbfda46dc326f804`, `802c23aebd41780d8c462f1aa1711707fe4ee88f`. L'import Step57 a été remplacé **uniquement** par un shim local `authenticated_step45() -> exact_physical_ward()` ; l'algèbre originale Step45/46/58, elle, a été exécutée. Ce n'est pas un rejeu de toute la suite Step57.

## Résultat démontré

Dans les coefficients de lapse **sans dérivée de lapse** `A_N=operator['N'][0]` et `A_M=operator['M'][0]` du vrai opérateur Step58, le balayage exact des symboles des jets `q,q',q'',q''',q''''` montre :

- `A_N` ne dépend, parmi les champs variables de la carte Step55, que de `pLf` et `pSf` à l'ordre radial zéro. Or `pLf=r²U(r²)` et `pSf` dépend algébriquement de `pLf` et `pLf'` par Step46. Donc **`A_N=A_N(r,U,U_s)`** ; aucune dépendance à `U_ss` ni `U_sss`.
- `A_M` dépend de `pLf,pSf,pf` et des jets `pLf',pSf'` ; il ne dépend d'aucun jet radial d'ordre deux ou plus des trois champs variables. Donc **`A_M=A_M(r,U,U_s,U_ss)`** ; aucune dépendance à `U_sss` ou au-delà.
- Les jets radiaux d'ordre trois présents dans `A_N,A_M` concernent seulement des champs **prescrits** sur la carte Step55 (`Sg,tg,pLg`), pas `pLf,pSf,pf`. Cela explique pourquoi l'absence de `U_sss` n'est pas contradictoire avec la présence de certains `q'''`.

Une identité supplémentaire est vérifiée symboliquement, sans substitution numérique. En notant `C1=dC/d(pLf')` le coefficient original Step46 et en imposant **Fz=0** :

```text
d A_N / d U_ss = 0
d A_M / d(pSf') = (z/Lf) * dC/d(pSf)
d(pSf')/d U_ss = 4*r^4 * d(pSf)/d(pLf')
d A_M / d U_ss = 4*r^4 * z * C1 / Lf.
```

L'opérateur original `A_M` est exactement affine en `pSf'`. L'identité `C1=(dC/dpSf)*(dpSf/d(pLf'))` et la formule de Step46 pour `dpSf/d(pLf')` ont été contrôlées. La formule de sensibilité n'exige ni hypothèse de signe supplémentaire, ni valeurs numériques ; son application physique exige les conditions régulières de la carte (`Lf,Sf,Sf',K>0`, `|z|<1`, dénominateur de poussière non nul, `r>0`).

## Conséquence opérationnelle

**Il existe une voie plus courte que la dérivation de `A/s`** pour prouver le signe continu de `A_N` et `A_M` : sur chaque cellule rationnelle `s=r²>0` du tube Step55, borner directement `U`, puis `U_s=(G-2U)/(2s)`, `U_ss=(G_s+(G_U-4)U_s)/(2s)`, et évaluer les coefficients originaux Step58 par intervalles sortants. Cette **voie de signe direct** ne nécessite que `G,G_s,G_U` sur la cellule, **pas** `G_ss,G_sU,G_UU`. Elle est un algorithme proposé, **non exécuté sur toutes les cellules physiques**. Des subdivisions adaptatives ou des formes centrées pourront être nécessaires pour éviter les surestimations de dépendance.

La **voie alternative par bornes de dérivées** de `A_M/s` reste plus coûteuse : elle requiert `U_sss` et donc les dérivées secondes de `G`, comme démontré au checkpoint précédent. Le présent résultat ne valide ni les signes continus, ni les zéros éventuels de `A_M`, ni le centre, ni les deux bords temporels, ni Dirac complet.

## Reproduction, limites et prochaine priorité

Nouveaux fichiers : `numerics/hr_b3c3d7_step58_reduced_jet_order_audit.py` et `tests/test_hr_b3c3d7_step58_reduced_jet_order_audit.py`. Sur les octets identiques à ceux publiés, `PYTHONPATH=<mini-arbre> python -m unittest discover -s <mini-arbre>/tests -p 'test_hr_b3c3d7_step58_reduced_jet_order_audit.py' -v` : **13 PASS, 0 FAIL, 0 SKIP** ; exécution du module : PASS ; `compileall` des deux nouveaux fichiers : PASS. Un test initial de substitution SymPy des jets a échoué pour une raison de forme syntaxique ; corrigé par un polynôme de Taylor explicite, puis la suite entière a été rejouée avec succès. Les originaux physiques Step45/46/58 ont été exécutés, mais **ni** la barrière physique complète Step55 **ni** les 256 cellules Step58 **ni** la suite complète du dépôt n'ont été rejouées.

**Prochaine priorité :** brancher l'évaluateur de coefficients originaux Step58 sur les intervalles rationnels des cellules Step55 ; calculer `G,G_s,G_U` sur **tout** l'anneau `1/16<=s<=289/400`, en respectant les dépendances corrélées et en subdivisant au besoin ; certifier `A_N>0,A_M<0` ou identifier un verrou/contre-exemple physique. Puis traiter `0<=r<=1/4`, les éventuels zéros, les deux vrais bords, les contraintes Dirac, charges, dynamique 4D, stabilité et observables. Les boîtes ponctuelles antérieures ne constituent pas un certificat continu.

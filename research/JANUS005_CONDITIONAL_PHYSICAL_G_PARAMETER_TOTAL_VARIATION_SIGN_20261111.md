# JANUS-005 — Signe conditionnel de la variation paramétrique totale de G (2026-11-11)

**HEAD de départ vérifié :** `2a6358e546a00bd7951d7ccdc25d016839bbc70b`. **Portée :** conséquence algébrique rigoureuse d'intervalles déjà publiés, **pas** un nouveau rejeu des opérateurs physiques, ni une certification des bords ou du modèle cosmologique.

## Proposition

Sur la famille analytique Step49 / tube spatial Step55 et pour `s in [0,289/400]`, `|lambda|<=1/5000`, noter `v=partial_lambda U(s,lambda)` et `V(s,lambda)=G(s,U(s,lambda),Pg+lambda)`. Le rapport antérieur `research/STEP68AD_C2D2E5B3B2C2B3C2B2B_AUTHENTIC_PHYSICAL_G_VARIATIONAL_BARRIER.md` fournit les **bornes décimales arrondies vers l'extérieur** :

- `-1.001099494671 < G_U < -0.993939366018` ;
- `0.020435412499 < G_Pg < 0.020578225856` ;
- `0.00681 < v < 0.00689`.

Par la règle de chaîne, à `s` fixé, `partial_lambda V = G_U v + G_Pg`. Comme `G_U<0` et `v>0`, le produit le plus négatif combine la borne inférieure de `G_U` avec la borne supérieure de `v`, tandis que le produit le moins négatif combine les bornes opposées. D'où les inégalités strictes :

```
0.020435412499 - 1.001099494671 * 0.00689
  = 0.01353783698071681
  < partial_lambda V
  < 0.020578225856 - 0.993939366018 * 0.00681
  = 0.01380949877341742.
```

**Conclusion conditionnelle :** `partial_lambda V > 0` uniformément sur le tube cité. En particulier, `lambda -> V(s,lambda)` est strictement croissante tant que la famille régulière et les hypothèses publiées restent valables. Ceci n'est **pas** une affirmation sur `G_s`, les lapses, le rang de Dirac ou les quatre traces f aux deux vrais bords.

## Vérification contradictoire arithmétique

Les deux bornes sont obtenues par calcul entier décimal exact (échelle `10^12` pour chaque facteur) et la sélection des coins extrêmes du rectangle d'intervalles. Les numérateurs à dénominateur commun `10^24` sont respectivement `13537836980716810000000` et `13809498773417420000000`, tous deux positifs, dans l'ordre attendu. Aucune hypothèse d'indépendance probabiliste n'est utilisée : l'arithmétique par intervalles reste une majoration valide même lorsque les variables sont corrélées. Le résultat repose sur la validité des certificats antérieurs et n'en constitue pas une réexécution indépendante.

**Exécution réelle de ce jalon :** calcul BigInt exact en JavaScript de ces deux extrêmes et contrôle `lower>0` : PASS. **Nouveaux tests authentiques Step55/58 : 0 ; nouvelles cellules physiques : 0 ; certifiées : 0.**

## Prochaine action

Calculer, avec les sources physiques authentifiées, les dérivées des **quatre traces f au vrai bord extérieur**, en tenant compte de `delta V` et des termes géométriques/paramétriques complets. Ne pas inférer le signe d'une trace f de celui de `delta V` seul. En parallèle, JANUS-001 demeure bloqué pour le pilote tant que les dépendances ne sont pas reconstruites localement.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**

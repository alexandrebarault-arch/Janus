# JANUS — Step68ad-B1 : polarisation exacte des jets de G, calcul physique à exécuter

**26 octobre 2026.** Branche `research/gate2b-nonhomothetic-transfer`. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED**.

## Résultat nouveau, réellement démontré

La difficulté de Step68ad-B est d'encadrer les dérivées partielles mixtes du **G physique fixe** de l'EDO `2s U_s=G(s,U)-2U` sur `0<=s<=1/1024`. Il est possible de le faire **sans réécrire ni différencier symboliquement** les ~1048 opérations de G, en réutilisant l'opérateur Taylor d'intervalles originel Step68n à l'ordre K=3.

Pour chaque rectangle continu `s∈S, U∈B`, évaluer quatre jets directionnels de la MÊME fonction `G` : `A(t)=G(s+t,U)`, `B(t)=G(s,U+t)`, `C(t)=G(s+t,U+t)`, `D(t)=G(s+t,U-t)`. Les coefficients `A_k,B_k,C_k,D_k` sont ceux de `t^k` (factorielles déjà normalisées).

**Identités exactes** :

```
G_s=A1; G_U=B1
G_ss=2 A2; G_UU=2 B2; G_sU=C2-A2-B2
G_sss=6 A3; G_UUU=6 B3
G_ssU=C3-D3-2 B3
G_sUU=C3+D3-2 A3
```

Les quatre jets suffisent donc pour toutes les dix dérivées mixtes d'ordre total ≤3. La preuve est l'identité polynomiale du développement de `G(s+t,U+c t)` en puissances de `c`, avec `c=0,+1,-1`. Les soustractions d'intervalles peuvent **élargir** les bornes mais ne peuvent pas en exclure la vraie valeur si les quatre jets entrants sont des extensions d'intervalles correctes.

Le module publie également les véritables formules de chaîne

```
R2 = G_ss + 2 G_sU U_s + G_UU U_s²
R3 = G_sss + 3 G_ssU U_s + 3 G_sUU U_s² + G_UUU U_s³
     + 3 G_sU U_ss + 3 G_UU U_s U_ss .
```

Ceci est une **preuve algébrique et un harnais calculatoire**, PAS encore une enclosure physique de R2/R3 : les quatre jets de G original doivent être réellement évalués sur toutes les cellules.

## Intégration au G original et fail-closed

`numerics/hr_step68ad_b_directional_polarization.py` utilise `hr_step68n_interval_ode_jets.jet_G`, **pas un G de substitution**, et refuse l'exécution si le blob Step68n ne vaut pas `96370e0599748c6dc07faf339ab3646ae3474e7d`, si ses sources originales Step45/46/55/68l ne sont pas authentiques, si K≠3 ou si le rectangle dépasse `s=1/1024`. Il ne modifie aucun de ces fichiers.

La fonction `physical_R2_global(folder,cells=32)` est un **programme d'essai non encore exécuté sur G physique** : elle importe les rapports 68v/68ac avec vérification SHA via Step68ad-A, forme pour chaque cellule l'enclosure cubique originale `|U-Ustar|<=10^-7 s³` et l'enclosure de `U_s` publiée par 68v, évalue `R2` par les quatre jets, puis applique le théorème de moyenne positive Step68ad-A avec `a2=6-G_U>0`. Une sortie réussie établirait un tube continu pour `U_ss`, éventuellement large, **conditionnel aux certificats Step49/68v et à la validité de l'arithmétique d'intervalles Step68n**. Aucun tel résultat numérique n'est revendiqué ici.

La procédure n'effectue aucune division par s ; elle couvre des cellules rationnelles fermées de `s=0` à `1/1024`. Les signes temporels Step58 et les sept cellules en attente ne sont pas abordés.

## Vérification réellement effectuée dans cette session

**18 tests PASS, 0 FAIL, en 1,88 s** via `PYTHONPATH=/mnt/data/janus68adB python -m pytest -q /mnt/data/janus68adB/tests/test_hr_step68ad_b_directional_polarization.py`. Les tests ont réellement été exécutés en Python/SymPy : dix monômes couvrant toutes les dérivées, polynôme mixte non linéaire, R2/R3 comparés indépendamment à SymPy, contrôle du signe de la direction négative, absence d'hypothèse d'affinité en U, contrôle des entrées invalides, et oracle indépendant d'intervalles exacts `Fraction` vérifiant les inclusions. Un premier test d'entrée invalide a échoué parce que l'import physique était effectué avant la validation ; le code a été corrigé et la suite entière relancée à **18 PASS**.

**N'ont PAS été exécutés :** le compilateur physique original Step45/46/55, `physical_G_partials`, `physical_R2_global`, les tests historiques Step68ad-A et le véritable opérateur temporel Step58. Le runtime local de cette session n'avait pas de clone GitHub (résolution DNS impossible) ; les sources originales ont été lues par connecteur GitHub, mais ne sont pas matérialisées dans le workspace Python. **Ne pas annoncer de certificat physique de U_ss ou U_sss.**

Les deux fichiers réellement testés ont été publiés puis relus via GitHub, avec comparaison stricte des blobs Git :

- `numerics/hr_step68ad_b_directional_polarization.py` : **3d075699fb8266ddce2ee9b370afa85cb17f2c73**.
- `tests/test_hr_step68ad_b_directional_polarization.py` : **6e1b4b81fe1e5b8588c6c9639829727da6eb4d21**.

## Prochaine action exacte : Step68ad-B2

1. Dans un environnement Python contenant les originaux authentiques, lancer `physical_R2_global('research/reports',cells=32)` et contrôler ses SHA, puis augmenter le nombre de cellules si les dépendances élargissent trop les bornes. Écrire un rapport JSON de la sortie réelle, avec vérification des intervalles `R2`, `a2` et `U_ss`.
2. Utiliser les **mêmes quatre jets** pour R3, en injectant le tube prouvé U_ss. Certifier U_sss sur le même domaine par Step68ad-A, puis construire les 12 jets canoniques.
3. Évaluer ensuite **le véritable Step58/60 temporel** sur les sept cellules encore PENDING et l'anneau central. Ne jamais substituer un résultat spatial à une preuve Dirac/4D.
4. Conserver les branches `main`, `research/v2-flrw` et les workflows désactivés absolument inchangés.

**État honnête : Step68ad-B1 (outil algébrique) TERMINÉ ; Step68ad-B2 (calcul physique continu) EN ATTENTE ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

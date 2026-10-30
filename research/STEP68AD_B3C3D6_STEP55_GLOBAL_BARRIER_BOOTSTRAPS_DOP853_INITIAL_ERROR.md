# JANUS b3c3d6 — fermeture conditionnelle de E0 par la barrière Step55

**Date : 2026-10-30. Statut : THÉORÈME RATIONNEL EXACT CONDITIONNEL ; aucun nouveau rejeu physique.**
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Résultat exact, sans résidu central cubique C

La preuve originale Step55 `hr_step55_global_barrier.py` établit pour la solution analytique régulière `U` :
`|U(s)-Ustar(s)| <= delta` pour `0<=s<=289/400`, `delta=1/10000`.
Au véritable temps initial binary64 `s0` du DOP853, si le polynôme dense
rationnalisé `P` vérifie `P(s0)-Ustar(s0) in [lo,hi]`, alors

`|U(s0)-P(s0)| <= E0 := delta + max(|lo|,|hi|)`.

Preuve : `U-P=(U-Ustar)-(P-Ustar)`, inégalité triangulaire.
Si la garde corrélée prouve `[lo,hi] subset [-delta,delta]`, on obtient
**`E0<=2*delta=1/5000`**. La borne est optimale sous ces seules hypothèses :
`Ustar=0, U=+delta, P=-delta` la sature. Ce résultat ne suppose **aucune**
borne `C` du résidu de Taylor central. Le décalage de l'initialisation
binary64 est **déjà inclus** dans `P(s0)-Ustar(s0)` si `P` est reconstruit
à partir des véritables octets DOP853 ; il ne faut pas le compter deux fois.

## Contribution au bord externe

Sous les hypothèses du registre existant `G_U<=0` sur le tube commun,
défauts continus certifiés `R_i` et sauts exacts `J_i`, la contribution
de cette borne initiale à `|U(sR)-P(sR)|` est
`(s0/sR)*E0 <= (s0/sR)/5000`.
Sur les **temps idéaux rationnels** `s0=1/10000, sR=289/400`,
elle vaut au plus `1/36125000` (environ `2.76816609e-8`).
Sur les **vrais temps binary64** du candidat `float(1e-4)` et
`float(Decimal('0.85')**2)`, le majorant rationnel exact est
`819855292164869/29617272429455892480000`
(environ `2.76816609e-8`).
Ceci n'est **pas** une borne finale totale : il faut ajouter les défauts
continus, les sauts, et certifier la même hypothèse `G_U<=0`.

## Conditions de validité et garde anti-fausse-certification

1. Réexécuter et vérifier la barrière Step55 authentique sur la même famille
   `Ustar`. Le résultat historique existe, mais n'a PAS été rejoué ici.
2. Reconstituer les octets binary64 du **premier** polynôme dense DOP853,
   puis évaluer l'intervalle corrélé `P(s0)-Ustar(s0)` à `x=0`.
3. Refuser `[lo,hi]` hors `[-delta,delta]` pour l'intégration dans
   le tube commun ; le lemme triangulaire isolé reste vrai sans cette garde.
4. Le registre global doit encore encloser **chaque défaut continu** et
   **chaque saut**, puis rattacher la borne `G_U<=0` Step63 au même tube.
5. Une borne `E0` finie, même optimale, ne prouve ni les six enclosures
   Step58 A/B/E, ni l'existence de lapses positifs aux deux bords, ni Dirac,
   dynamique 4D, stabilité ou observables.

## Livrables et vérification

- `numerics/hr_b3c3d6_barrier_initial_bootstrap.py` : calcul rationnel
  de `E0`, extraction du premier DOP853 dense et raccord au registre.
  Git blob `924082d7ff32c623357988210c6b0967111b30c5`.
- `tests/test_hr_b3c3d6_barrier_initial_bootstrap.py` : 11 tests rationnels
  dont saturation, refus hors tube, abscisses idéales/binary64 et puissance.
  Git blob `8103f06993aaac12817aefa1b649f27216b0271c`.
- Tests réellement exécutés sur les mêmes octets locaux :
  `PYTHONPATH=. python -m unittest discover -s tests -q` :
  **11 PASS, 0 FAIL** ; `python -m compileall -q numerics tests` : **PASS**.
- Source original Step55 barrière lue via GitHub :
  `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ;
  source normalisation `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
  **Aucune exécution physique DOP853 ou Step58 dans cette session.**

**Étape suivante :** exécuter le vrai DOP853 Step55 et la barrière,
certifier la garde corrélée sur tous les pas et le `E0` effectif,
puis les `R_i/J_i`, `G_U` et le registre global ; propager ensuite
vers six enclosures Step58 et le BVP positif à deux vrais bords.

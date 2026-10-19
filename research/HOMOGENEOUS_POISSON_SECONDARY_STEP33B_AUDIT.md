# JANUS Gate 2B — Étape 33b : crochet de Poisson homogène et condition secondaire (avec deux poussières)

**Date :** 19 octobre 2026  
**Branche GitHub :** `research/gate2b-nonhomothetic-transfer`  
**Statut :** homogène `MINISUPERSPACE_SECONDARY=GREEN`; contraintes secondaires radiales/locales HR et physiques `NOT_DERIVED`; **`GATE_2B=OPEN`**.

## 1. Question précise

À l’étape 33a, la représentation ADM sphérique avec deux lapses et deux poussières canoniques a été écrite sous forme linéaire en lapses après redéfinition du décalage relatif. Cette propriété est nécessaire, mais elle ne démontre PAS l’existence et la préservation de la contrainte secondaire Boulware–Deser en théorie des champs. La présente étape calcule exactement un **modèle réduit homogène FLRW**, puis établit en quoi ce résultat doit et ne doit pas être interprété.

## 2. Action canonique réduite — variables, signes et poussières

La réduction homogène à géométrie spatialement plate utilise deux facteurs d’échelle positifs `a,b`, leurs moments `pa,pb`, et **deux paires canoniques indépendantes** `(theta_g,pg)` et `(theta_f,pf)` avec `pg,pf>0`. Les phases de poussière sont cycliques sur ce fond, donc `pg` et `pf` sont deux constantes séparées, non fusionnées.

L’Hamiltonien réduit est `H=N_g H_g+N_f H_f` avec

```text
H_g = -pa²/(12 Mg² a) + m² Mg² a³ [β0+3β1 y+3β2 y²+β3 y³] + pg
H_f = -pb²/(12 Mf² b) + m² Mg² a³ [β1+3β2 y+3β3 y²+β4 y³] + pf
y=b/a.
```

Les quatre paires canoniques ont les crochets standards : `{a,pa}=1`, `{b,pb}=1`, `{theta_g,pg}=1`, `{theta_f,pf}=1`. On fixe ici l’unité de cellule homogène (normalisation des densités radiales traitée par le test d’immersion sphérique, §5). Le calcul NE suppose PAS `H_g=H_f=0` avant de calculer les crochets.

## 3. Crochet exact et branche dynamique

La dérivation sympy est indépendante de la fonction numérique :

```text
{H_g,H_f} = (m² Mg²/2) a² J(y) χ,
J(y) = β1 + 2 β2 y + β3 y²,
χ = pa/(Mg² a) - pb/(Mf² b).
```

La conservation des contraintes primaires homogènes en présence de lapses non nuls donne **`J(y) χ=0`** si `m²>0`. Sur la branche dynamique régulière `J(y)≠0`, on obtient la **condition secondaire homogène** `χ=0`, équivalente à l’égalité des taux de Hubble normalisés par les lapses. Cette contrainte est un analogue homogène de la condition Bianchi, PAS une preuve du rang/fermeture de la contrainte Boulware–Deser locale en géométrie sphérique non homogène.

Sur la branche `J(y)=0`, le crochet s’annule sans imposer `χ=0`. Un contrôle négatif teste explicitement ce cas, ainsi que le découplage `m²=0`; la formule de la branche dynamique ne leur est PAS extrapolée.

## 4. Conservation temporelle de la condition secondaire et lapses

Notons `V=β0+3β1 y+3β2 y²+β3 y³`, `W=β1+3β2 y+3β3 y²+β4 y³`, `A=β0+2β1 y+β2 y²`, `K=β2+2β3 y+β4 y²`, `k=m² Mg²`, `M=Mg²`, `F=Mf²`. Le calcul canonique direct donne :

```text
B_g = {χ,H_g}
    = pa²/(12 M² a³) - 3 k a A/M + 3 k a² J/(F b)

B_f = {χ,H_f}
    = -pb²/(12 F² b³) - 3 k a J/M + 3 k a² K/(F b).
```

La préservation de `χ=0` requiert `N_g B_g+N_f B_f=0`, donc, lorsque `B_f≠0`, `N_f/N_g=-B_g/B_f`. Le code refuse explicitement de calculer un rapport de lapses « physique » loin de `H_g=H_f=χ=0` ou au dénominateur dégénéré. Aucune condition de jauge supplémentaire n’est déduite.

La matrice antisymétrique des trois contraintes **homogènes** `(H_g,H_f,χ)` sur la branche régulière et sur solution est

```text
D = [[0,   0,  -B_g],
     [0,   0,  -B_f],
     [B_g,B_f,     0]].
```

Les tests la trouvent de **rang 2** pour plusieurs époques de Candidate-C et montrent que `(1,N_f/N_g,0)` est son vecteur nul, ce qui confirme l’existence de l’unique combinaison de lapse restant libre dans le **système réduit homogène**. **Ne pas transformer ce rang en comptage du degré de liberté BD de la théorie inhomogène.**

## 5. Immersion indépendamment vérifiée dans les contraintes sphériques ADM

La solution plate homogène `L=a`, `S=a r` s’immerge dans l’action sphérique de l’étape 33a par

```text
pL=(pa/3) r²,       pS=(2pa/3) r,       ∂r pL=(2pa/3) r
(analogue en f : a→b, pa→pb),
p_dust_g=pg r²,  p_dust_f=pf r²,  ∂r theta_g=∂r theta_f=0.
```

Ces densités reproduisent `H_g^{spherical}/r²=H_g^{mini}` et `H_f^{spherical}/r²=H_f^{mini}`, ainsi que la contrainte de moment radial diagonale nulle. Un test négatif montre que supprimer artificiellement `∂r pL` détruit cette dernière identité. Cette immersion confirme la **normalisation homogène**, mais le crochet calculé est toujours un crochet **après réduction homogène**, et non le crochet fonctionnel complet avant restriction. Ces deux opérations ne sont pas automatiquement interchangeables.

## 6. Valeurs de contrôle sur Candidate-C (deux poussières, sans rayonnement)

Le prolongement de racines d’un polynôme quartique et le calcul indépendant `N_f=y+d y/d ln a` produisent, aux points représentatifs :

| a | y=b/a | Nf/Ng attendu | Nf/Ng issu des crochets |
|---|---:|---:|---:|
| 1 | 0.5568825591873 | 0.5515457786483 | 0.5515457786483 |
| 0.4 | 0.5787707228025 | 0.5185264338279 | 0.5185264338279 |
| 0.09 | 0.9399775251263 | 0.4169220933391 | 0.4169220933391 |
| 0.03 | 1.9795452448545 | 0.4618315649332 | 0.4618315649332 |

Sur ces quatre points, les deux contraintes homogènes, le crochet primaire et `χ` s’annulent à des résidus numériques `~1e-13` ou moins; le rapport issu de la préservation de `χ` concorde à `~2e-14` ou mieux. Le modèle présenté est explicitement **la variante Candidate-C sans rayonnement**, pas l’histoire cosmologique complète.

## 7. Tests et honnêteté de provenance

Nouveaux fichiers :

- `numerics/hr_homogeneous_poisson_secondary.py` : analytique, crochet numérique indépendant à quatre paires canoniques et immersion sphérique.
- `tests/test_hr_homogeneous_poisson_secondary.py` : tests symboliques SymPy, différences finies, branche `J=0`, découplage `m²=0`, conservation des deux poussières, Candidate-C, et matrice de Dirac homogène.
- `scripts/verify_gate2b_step33b.py` : relance ciblée, empreintes SHA-256/Git, contrôle des fichiers sources exacts de 33a, rapport d’acceptation strict.

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests
# 57 passed in one standalone focused workspace
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33b.py gate2b-step33b-report.json
```

Le résultat de **57 tests** comprend **les 21 tests exacts de l’étape 33a et 36 nouveaux tests paramétrés de l’étape 33b**, dans **le même** environnement local `/mnt/data/janus33b`. Les anciens 93 tests de l’étape 32e ne sont PAS réexécutés ici. Aucun clonage intégral, CI ou revue indépendante n’est revendiqué. Les fichiers 33a ont été contrôlés à leurs empreintes GitHub; les nouveaux fichiers 33b devront être comparés à leurs empreintes GitHub après publication.

## 8. Verrous restants — prochain point d’attaque exact

1. **NON RÉSOLU :** crochets de Poisson **fonctionnels** des véritables contraintes sphériques `C_g(r), C_f(r), D(r)` de l’étape 33a, avec dérivées spatiales, distributions/smearings, interactions HR, courbure et LES DEUX paires de poussière. La condition secondaire locale dépend des contraintes primaires et des conditions de bord; aucune factorisation homogène ne remplace sa démonstration.
2. **NON RÉSOLU :** préservation temporelle, stabilité/rang du primaire-secondaire de BD, et élimination canonique en géométrie sphérique pleinement radiale; garder les dust `p,theta` distincts.
3. **NON RÉSOLU :** connexion du résultat ADM sphérique à l’action scalaire temps-intégrable de l’étape 32e, sur un fond réellement non homothétique sur solution et non une simple reparamétrisation homogène.
4. **NON RÉSOLU :** les références physiques **De Felice** à H fini et limite `mu→0`, **Aoki** homothétique `K_S,c_S²` stables et instables sur la **même action contrainte**, puis seulement la première transition relative de Candidate-C autour de `a≈0.0301646`.

**Verdict final de cette étape :** `HOMOGENEOUS_SECONDARY_CHI=GREEN`, `TWO_DUST_CANONICAL_PAIRS=GREEN`, `LOCAL_SPHERICAL_BD_SECONDARY=OPEN`, `GATE_2B=OPEN`, `JANUS_R_NOT_VALIDATED`.

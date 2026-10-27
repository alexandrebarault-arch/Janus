# JANUS — 68ad-C2d2e5b3b2b1 : compatibilité exacte des premiers jets centraux

27 octobre 2026. **Étape partielle**, pas un oracle fonctionnel de Dirac. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et contrôle

Sources originales relues par connecteur GitHub, blobs authentifiés : Step45 `numerics/hr_step45_exact_physical_ward.py` = `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; Step46 `numerics/hr_step46_exact_secondary_ode.py` = `bac025c28dbe1561c0c36c56dbfda46dc326f804` ; Step49 `numerics/hr_step49_analytic_center.py` = `d570948912885d45a625fa2db31c6a5435b6a654` ; Step55 `numerics/hr_step55_global_barrier.py` = `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Les moteurs originaux **n'ont pas été réexécutés**. Les calculs ci-dessous reconstruisent les densités originales Step45 et composent le résultat historique exact Step49 pour la secondaire.

## Théorème de compatibilité des jets d'ordre minimal

Sur une classe analytique centrale à géométrie `Lg=a(1+cg r²)², Sg=r Lg, Lf=b(1+cf r²)², Sf=r Lf`, avec `a,b,mg,mf>0`, prendre `pLg=r²(Pg+Pg1 r²)`, `pLf=r²(U+U1 r²)`, `pSg=r(2Pg+Psg1 r²)`, `pSf=r(2U+Psf1 r²)`, `pg=r² rhog`, `pf=r² rhof`, `tg'=r kg Lg`, `tf'=r kf Lf`, `z=r z1+O(r³)`. Les champs de poussière peuvent être intégrés en primitives radiales, comme dans Step68o. Les paramètres `Pg1,U1,kg,kf,z1` sont libres à ce niveau de troncature.

Définir `At=b1 a²+2 b2 ab+b3 b²`, `k0=m2 mg a b At>0`, `Vg=a(b0 a²+2 b1 ab+b2 b²)+b At`, `Vf=b(b2 a²+2 b3 ab+b4 b²)+a At`. L'expansion directe des deux contraintes originales donne :

```text
Hg/r² -> -3 Pg²/(4 mg a) + rhog + 24 mg a cg + m2 mg Vg
Hf/r² -> -3 U²/(4 mf b) + rhof + 24 mf b cf + m2 mg Vf
Dg/r³ -> a(Psg1 + 8 cg Pg - 4 Pg1 + kg rhog)
Df/r³ -> b(Psf1 + 8 cf U  - 4 U1  + kf rhof)
```

Les termes `Dg/r` et `Df/r` sont nuls grâce aux coefficients `pSg/r=2Pg`, `pSf/r=2U`. Pour `z=r z1`, `Fz/r³ -> Dg3-k0 z1`. La secondaire originale, **après élimination de la primaire poussière f suivant Step46 et avec W=pLf'/r=2U au centre**, a pour terme dominant historique Step49 :

```text
C/r² -> -m2 At [6 a b mf mg z1 + 3 a mg U - 3 b mf Pg]/(2 a b mf).
```

La solution algébrique explicite de ces contraintes au premier ordre non trivial est :

```text
U     = mf b (Pg/(mg a) - 2 z1)
rhog  = 3 Pg²/(4 mg a) - 24 mg a cg - m2 mg Vg
rhof  = 3 U²/(4 mf b) - 24 mf b cf - m2 mg Vf
Psg1  = k0 z1/a - 8 cg Pg + 4 Pg1 - kg rhog
Psf1  = -k0 z1/b - 8 cf U + 4 U1 - kf rhof
```

Substitution exacte : `Hg2=Hf2=C2=Fz3=Ddiag3=0`, avec `Dg3=k0 z1`, `Df3=-k0 z1`. **Cela n'impose aucune contrainte sur les coefficients radiaux d'ordre supérieur, ni sur les conditions aux bords, ni sur les équations temporelles.** La solution `z=r z1` n'est garantie ici qu'à l'ordre dominant, pas comme identité radiale exacte.

## Tangence non triviale et contrôles négatifs

En fixant la géométrie et `z1,Pg1,U1,kg,kf`, la variation `Pg -> Pg+epsilon` et la résolution **non linéaire exacte** des cinq coefficients ci-dessus préservent ces cinq contraintes centrales pour tout `epsilon` suffisamment petit pour conserver les signes et la charte. Ainsi `delta U=mf b/(mg a) delta Pg`, `delta rhog=3 Pg/(2 mg a) delta Pg`, `delta rhof=3 U/(2 mf b) delta U`. Il existe donc une direction tangentielle non nulle aux **contraintes centrales tronquées** : l'annulation de `delta Hg2,delta Hf2,delta C2` n'impose pas `delta Pg=0`. Ne pas extrapoler à l'espace tangent aux contraintes fonctionnelles sur tout `r`.

Le témoin **synthétique**, non une solution physique Step55, utilise `a=2/5,b=1/4,mg=1,mf=1/16,m2=5,cg=1/1000,cf=-1/1000,z1=1/250,Pg=-3/5,beta=(-10,1,0,1,-10)`. Il donne `k0=89/800>0`, `rhog=127491/40000>0`, `rhof=1812387/16000000>0`, `U=-377/16000`. Les tests adversariaux perturbent isolément `U,rhog,rhof,Psg0,Psf0,Psg1,Psf1` et constatent des résidus non nuls.

## Vérifications réellement exécutées

Programme V8 publié `scripts/hr_step68ad_c2d2e5b3b2b1_center_constraint_jets.cjs` : **25 assertions exactes BigInt PASS** ; wrapper publié `tests/test_hr_step68ad_c2d2e5b3b2b1_center_constraint_jets.cjs` : **12 assertions PASS**, total **37 assertions V8**, zéro échec. Contrôle indépendant SymPy en session : **15 identités symboliques PASS**, dont courbures g/f originales, limites `Hg/r²,Hf/r²`, `Dg3,Df3`, substitutions exactes, famille `Pg+epsilon` et tangence `C2`. **Total 52 vérifications exactes PASS, 0 FAIL**, mais les 15 identités SymPy sont un contrôle de session non publié sous forme de script autonome. Aucun moteur original Step45/46/49/55 n'a été réexécuté.

## Limites et prochaine étape

**Prochaine étape effective : 68ad-C2d2e5b3b2b2** — imposer les contraintes linéarisées comme fonctions de `r` sur la solution réelle Step55/68o, et non seulement leurs jets au centre ; construire l'oracle Poisson/Dirac original non-IBP sur les six couples, avec variations de shift et termes de bord, rang/tertiaires, chartes `K=0/J=0`, lapses globaux, puis dynamique 4D/stabilité/observables. Les résultats locaux ne constituent ni preuve de liberté du fantôme BD, ni obstruction physique, ni validation de JANUS.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

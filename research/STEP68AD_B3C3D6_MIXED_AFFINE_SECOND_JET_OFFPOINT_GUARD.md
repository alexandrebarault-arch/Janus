# JANUS b3c3d6 — second jet hors point de l'affine mixte historique (30/10/2026)

**Statut : théorème local formel exact, non physique et non Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Résultat et portée

L'ancien probe `numerics/hr_b3c3d6_full_original_step58_point_probe.py` (blob `643d90183367e74a28ed453d93f5489074b75b08`) impose `pLfr=rG(s,Ua)` hors point ; le candidat cubique `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` (blob `43a140cacfca81aaf41073facea3da4e47e64f5e`) impose `pLfr=d[r²Uc]/dr`. Poser `s=r²`, `h=s-s0`, `2sU_s=G(s,U)-2U`, `u2=U_ss(s0)`, `u3=U_sss(s0)`, `Ua=u0+u1h` et `Uc=Ua+u2h²/2+u3h³/6`.

Pour `G` de classe C³ dans la carte considérée, le développement de Taylor exact au sens des jets donne

```text
pLfr_mixed/r - pLfr_cubic/r = -(G_U(s0,u0) u2 / 2) h² + O(h³).
pLf_mixed - pLf_cubic = -(s0 u2 / 2) h² + O(h³).
[pLfr_mixed-pLfr_cubic]''(r0) = -4 r0³ G_U(s0,u0) u2.
[pLf_mixed-pLf_cubic]''(r0) = -4 r0⁴ u2.
```

Les jets radiaux 0 et 1 coïncident. Le deuxième jet de `pLfr` peut donc différer, même si l'ancien affine mixte et le cubique sont **ponctuellement indiscernables pour les six coefficients Step58** selon l'audit original des dépendances `numerics/hr_b3c3d6_original_step58_minimum_jet.py` (blob `8d81fc1bc7823774e6304e25a52653d32e36c4ee`). Cette identité n'est PAS un résultat de différence des six coefficients : ceux-ci ne dépendent que des jets 0/1 des champs dépendant de U.

La comparaison numérique correcte exige **un seul et même état terminal U(r0)**, le même rayon décimal exact et les mêmes paramètres : appeler séparément les deux `main()` peut comparer des intégrations ou transports d'extrémité distincts et ne teste pas cette invariance. Un contrôle négatif utile est l'affine strictement holonome, dont le premier jet de pLfr diffère déjà de celui du cubique de `-4r0⁴u2`.

## Reproductibilité

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_mixed_affine_second_jet.py' -v` : **9 PASS, 0 FAIL** ; `python -m compileall -q numerics/hr_b3c3d6_mixed_affine_second_jet.py tests/test_hr_b3c3d6_mixed_affine_second_jet.py` : **PASS**. Tests SymPy rationnels et différentiation radiale directe, non indépendants du formalisme. Témoin JOUET : `r0=1/2`, `U_ss=-5/21`, `G_U=-3/2` : écart de deuxième jet `pLfr=-5/28`, `pLf=5/84`. Aucun calcul de coefficients physiques Step58 aux quatre rayons effectué cette session.

Fichiers : `numerics/hr_b3c3d6_mixed_affine_second_jet.py` blob `b615d1996b4fbcd9e5d641b84b42ce6a5befc7f1` ; `tests/test_hr_b3c3d6_mixed_affine_second_jet.py` blob `c4e7529c9c1d2f90c15db5c9d569b496be1a7551`. Sources originales Step45/46/55-normalized/55-barrier/58 lues par connecteur avec SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `bac025c28dbe1561c0c36c56dbfda46dc326f804`, `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, `802c23aebd41780d8c462f1aa1711707fe4ee88f`. **Originaux non exécutés**, car non matérialisés localement ; réseau GitHub direct du conteneur en échec DNS, connecteur fonctionnel.

## Prochaine étape inchangée

Rejeu physique authentique et apparié aux rayons `1/4,1/2,7/10,17/20` des six coefficients ancien mixte/quadratique/cubique, contrôle négatif affine holonome ; défaut continu DOP853 et erreur initiale, enclosures A/B/E, BVP lapses positifs aux deux bords, Dirac six couples, dynamique 4D, stabilité et observables. Aucune validation JANUS.

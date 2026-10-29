# JANUS b3c3d6 — audit exact des jets de l'EDO dans le probe Step58 (29/10/2026)

**Verdict : défaut de construction des jets supérieurs identifié dans le script numérique précédent ; impact sur les six coefficients Step58 encore INCONNU.** GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

## Source et portée

Audit du code authentique `numerics/hr_b3c3d6_full_original_step58_point_probe.py`, Git blob `643d90183367e74a28ed453d93f5489074b75b08`, lu sur la branche de recherche. Dans `main()`, `fields_at(t)` utilise `Ulin(s)=U_R+U_s(s-s_R)`, tandis que `physical_fields` utilise `pLf'=r*G(s,Ulin)` pour construire les autres champs. L'égalité `pLf'=r G` n'est imposée qu'au rayon d'évaluation, et le script calcule les jets suivants par `mp.diff(fields_at)`. Il n'utilise pas `U_{ss}` et `U_{sss}` de l'EDO.

Pour l'EDO Step55 originale `2s U_s=G(s,U)-2U` (`s=r²>0`), la différentiation exacte donne :

```text
U_s   = (G-2U)/(2s)
U_ss  = [G_s+(G_U-4)U_s]/(2s)
U_sss = [G_ss+2 G_sU U_s+G_UU U_s²+(G_U-6)U_ss]/(2s)
```

Avec `pLf(r)=r²U(r²)`, les jets véritables sont
`pLf''=2U+10s U_s+4s² U_ss` et
`pLf'''=24r U_s+36rs U_ss+8rs² U_sss`.
Le prolongement affine du script supprime donc exactement
`ΔpLf''=4s² U_ss` et
`ΔpLf'''=36rs U_ss+8rs² U_sss`.
Un contrôle équivalent montre que la dérivée de `r G(s,Ulin)` et celle de `r²Ulin` divergent à l'ordre 2 de `4s² U_ss`, sauf si `U_ss=0` au point.

**Ce qui est prouvé :** identité algébrique générale et insuffisance de la méthode affine pour certifier les jets supérieurs d'une EDO non affine. **Ce qui n'est PAS prouvé :** `U_ss≠0` aux quatre points Step55, ou dépendance effective de `A_N,A_M,B_N,B_M,E_N,E_M` à ces jets manquants. Les valeurs antérieures compatibles avec `B_N=B_M=E_N=E_M=0` ne sont ni réfutées ni confirmées par cet audit. Le test à 70 décimales ne corrige pas un éventuel défaut de jets.

## Contrôles exécutés

`PYTHONPATH=/mnt/data/janus_jet_audit python -m unittest discover -s /mnt/data/janus_jet_audit/tests -v` : **5 unittest PASS, 0 FAIL**, non indépendants ; `python -m numerics.hr_b3c3d6_step55_jet_holonomicity` PASS. Témoin rationnel **JOUET, NON Step55** : `G=s²+U²`, `s=1/4`, `U=1/2` ; `U_s=-11/8`, `U_ss=37/4`, `U_sss=-1295/16` ; `ΔpLf''=37/16`, `ΔpLf'''=1369/64`. Un témoin affine exact annule les deux défauts. Aucune exécution des moteurs Step45/55/58 originaux pendant cet audit.

## Action scientifique prioritaire

Corriger le constructeur de jets du probe original : construire un Taylor cubique de `U(s)` à partir de `G,G_s,G_U,G_ss,G_sU,G_UU` et de l'EDO ; vérifier explicitement `pLf',pLf'',pLf'''` par deux voies indépendantes ; réévaluer les six coefficients Step58 aux quatre rayons, avec tests de perturbation des jets supérieurs. Puis seulement chercher une factorisation exacte de `B_N,B_M` et une certification uniforme sur `0<r≤17/20`. L'erreur DOP853 globale reste non certifiée. Lapses positifs, deux vrais bords, Dirac/charges/jauge/six couples/K=0/J=0/4D/stabilité/observables demeurent ouverts.

**Sources et livrables :** code `numerics/hr_b3c3d6_step55_jet_holonomicity.py` (Git blob `22fea2970d22027e2a8a8531f22bb87a4f7af2e5`) ; tests `tests/test_hr_b3c3d6_step55_jet_holonomicity.py` (Git blob `d607c1fcc4954982ffd30b47f088c461220ec351`). Aucune branche protégée ni workflow modifié.

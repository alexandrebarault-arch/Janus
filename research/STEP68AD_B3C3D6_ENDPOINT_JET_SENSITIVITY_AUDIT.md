# b3c3d6 — Sensibilité exacte des jets au prolongement cubique (29 octobre 2026)

**Statut : résultat algébrique limité ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

Audit des octets authentifiés du candidat `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` (blob `9eb5167bec74fc427307a262faaa6a1f785785a8`), de la carte `hr_b3c3d6_ode_consistent_jet_map.py` (blob `c66534cab7da29cf9c214f08c965def3b99b4e63`) et de l'original Step58 `hr_step58_temporal_operator.py` (blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`). Il s'agit d'une lecture des sources et d'un calcul SymPy local, **pas** d'un rejeu des moteurs originaux.

Posons `s=r²`, `U_a(s)=u0+u1(s-s0)` et `U_c(s)=U_a+u2(s-s0)²/2+u3(s-s0)³/6`, `s0=r0²>0`. Dans les deux prolongements, `pLf=r²U` et `pLfr=r G(s,U)`. Les valeurs et premières dérivées radiales de ces deux champs coïncident au point. Les différences **cubique moins affine** valent exactement :

```
Delta pLf''  = 4 r^4 u2
Delta pLf''' = 36 r^3 u2 + 8 r^5 u3
Delta pLfr'' = 4 r^3 G_U u2
Delta pLfr'''= 24 r^2 G_U u2
               + 24 r^4 (G_sU + G_UU u1) u2 + 8 r^4 G_U u3
```

Les dérivées de G sont évaluées en `(s0,u0)`. Pour toute fonction composée `H(r)=F(r²,U(r²))`, `Delta H''=4r² F_U u2` ; cela montre que les champs secondaires algébriques dépendant de U et de G peuvent aussi être affectés. Les formules sont des identités de chaîne indépendantes de la valeur physique de U2/U3. L'original Step58 construit son opérateur par `Dt(X)` et `Dt(deltaZ)` : ses coefficients d'ordre inférieur ne peuvent **pas** être réputés invariants par simple coïncidence des jets 0/1. Une invariance éventuelle sur la coquille Step55 nécessite une vérification effective, non un argument d'ordre.

**Contrôles exécutés** dans un environnement local SymPy : 9 résidus algébriques nuls (8 pour pLf/pLfr, 1 pour F générique), 5 unittest PASS (non indépendants), `compileall` PASS. Témoin **jouet hors coquille** `r=1/2,u0=1/3,u1=1/5,u2=2/7,u3=-1/11,G=s²+2sU+3U²+4s+5U` : `Delta pLf''=1/14`, `Delta pLf'''=389/308`, `Delta pLfr''=15/14`, `Delta pLfr'''=21387/1540`. Il ne s'agit d'aucune valeur Step55 physique.

**Limites et prochain test obligatoire :** le candidat original corrigé n'a pas été exécuté ici (DNS du conteneur local bloqué vers GitHub ; connecteur GitHub fonctionnel). Les quatre rayons, six coefficients et leurs variations **restent inconnus** pour les vrais jets Step55 ; aucun BVP, zéro, raccord centre ou résultat Dirac n'est prouvé. Prochaine étape : exécuter les cinq sources originales SHA-authentifiées avec le candidat corrigé aux quatre rayons, comparer six coefficients affine/cubique et les résidus de coquille, puis factorisation exacte/enclosures, lapses positifs et deux bords, Dirac/4D/stabilité/observables.

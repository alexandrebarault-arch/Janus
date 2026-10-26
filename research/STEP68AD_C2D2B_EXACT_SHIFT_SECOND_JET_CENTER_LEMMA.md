# JANUS — 68ad-C2d2b : régularisation exacte du second jet du shift (2026-10-26)

**Nature : lemme algébrique CONDITIONNEL sur la branche stationnaire positive-K ; PAS une exécution physique des sept cellules Step58, PAS le quotient complet Step60.** Le verrou 68ad-C2d2b reste ouvert. Statut : `GATE_2B OPEN`, `JANUS_R NOT_VALIDATED`.

## Sources originales consultées directement sur GitHub

- `numerics/hr_step58_temporal_operator.py` : blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
- `numerics/hr_step60_full_constraint_prolongation.py` : blob `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`.
- `numerics/hr_step68o_temporal_interval_annulus.py` : blob `c99caebc17f243784450ddff94fb061767e6d8e7`.
- `numerics/hr_step68ad_c2d2a_temporal_replay.py` : blob `e5a6c34ba95548527bc26d946f1e210d77355ee6`.

## Lemme exact et domaine de validité

L'équation de stationnarité originale est `Fz=D-K*z/sqrt(1-z²)=0`. Pour `K>0`, sa branche régulière est `z=D/sqrt(D²+K²)`. Avec `R=sqrt(D²+K²)` et `W=K*D'-D*K'` :

```text
z'  = K*W/R³
z'' = [K'*W+K*(K*D''-D*K'')]/R³
      - 3*K*W*(D*D'+K*K')/R⁵
```

Les expressions originales de Step60 pour `ZD=(1-z²)^(3/2)/K`, `ZK=-z*(1-z²)/K`, et `z''=ZD*D''+ZK*K''+D_r(ZD)*D'+D_r(ZK)*K'` reproduisent exactement cette dérivée **si et seulement si les jets externes sont mis sur la même coquille** `z=D/R, z'=K*W/R³`. Le test établit l'égalité dans ce cas, sans affirmer la nécessité logique de ces substitutions dans toute formulation équivalente.

Si, en outre, `D=r³*d(s)`, `K=r²*k(s)`, `s=r²`, `k(s)>0` et `d,k` sont `C³`, alors

```text
z=r*A(s),  A(s)=d(s)/sqrt(k(s)²+s*d(s)²)
z'   = A+2s*A_s
z''  = r*(6*A_s+4s*A_ss)
z''' = 6*A_s+24s*A_ss+8s²*A_sss
```

D'où `z'(0)=d0/k0`, `z''(0)=0`, `z'''(0)=6*(d1/k0-d0*k1/k0²-d0³/(2*k0³))` pour `k0>0`. Ce sont des identités de dérivation exactes, sans division par `r` dans les expressions finales. Elles sont utiles pour une future évaluation cohérente du second jet du shift Step60 au centre. L'hypothèse `D=O(r³)` n'est pas déduite ici de toute la dynamique : elle doit être vérifiée sur le profil physique.

## Exécutions locales et contre-exemples

`PYTHONPATH=. python -m numerics.hr_step68ad_c2d2b_shift_second_jet` : **10 identités symboliques exactes**. `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2b_shift_second_jet.py` : **10 tests PASS, 0 FAIL** (1,42 s), dont six profils rationnels indépendants, le contrôle de la branche `K<0` et un contre-exemple `D=r,K=r²` donnant `lim z=1` au lieu de `z=O(r)`. Ces exemples ne sont pas des solutions physiques de JANUS.

Code : `numerics/hr_step68ad_c2d2b_shift_second_jet.py` (blob `b10085e6c8cbfc562f3b2cc1a120eb6448535a57`). Tests : `tests/test_hr_step68ad_c2d2b_shift_second_jet.py` (blob `c3fb478715587c02bad49f95093e9d4b06a0cae1`). Les deux blobs ont été relus sur GitHub et comparés aux octets locaux exécutés.

## Verrou inchangé / prochaine action effective

**0/14 coefficients temporels physiques nouveaux certifiés.** Le vrai Step58 sur les sept cellules et le quotient physique complet Step60 n'ont pas été exécutés : le conteneur de calcul ne possède pas les dépendances originales et les trois rapports pinés sous un même checkout, et son accès réseau GitHub direct échoue. Prochaine étape : réunir un checkout byte-authentique, rejouer les tests C2d2a/C2d2b, exécuter `numerics.hr_step68ad_c2d2a_temporal_replay.run()` sur les sept cellules, contrôler les 14 intervalles avec le garde exact, puis calculer le quotient Step60 avec `z,z',z''` prolongés sur la coquille. Si un intervalle contient zéro, verdict `INCOMPLETE`. Rang Dirac, lapses, bords, BD, 4D et observables restent OPEN.

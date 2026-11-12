# JANUS-005 — Courbure exacte de la branche centrale M2 (2026-11-12)

Source authentique lue : `numerics/hr_step55_global_barrier.py`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, HEAD initial `a344724f40bfba0709a1394b375cdc3a2f50c352`.

## Question falsifiable
La tangente centrale élargie à M2 du rapport `JANUS005_EXPANDED_M2_FRIEDMANN_TANGENT_20261111.md` est-elle seulement infinitésimale, ou s'intègre-t-elle exactement en une courbe algébrique locale ? Cela ne teste ni les équations radiales ni Dirac.

Fixons A,Y,MF,Z1 et les coefficients du potentiel, et posons `K=(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3`, `Hbase=0.9/(3*A**3)`. La source impose `H2=Hbase+M2*K`, `PG=-2*A**2*sqrt(H2)` et `U0=MF*Y*(PG-2*A*Z1)`.

Pour `K>0`, `H2>0`, la branche négative est une courbe exacte :
`M2(PG)=(PG**2/(4*A**4)-Hbase)/K`,
`U0(PG)=MF*Y*(PG-2*A*Z1)`.
Ainsi `dM2/dPG=PG/(2*A**4*K)` (la tangente du rapport antérieur) et `d²M2/dPG²=1/(2*A**4*K)>0`. Inversement,
`dPG/dM2=-A**2*K/sqrt(H2)`,
`d²PG/dM2²=A**2*K**2/(2*H2**(3/2))>0`,
`d²U0/dM2²=MF*Y*d²PG/dM2²`.

## Exécution et contre-contrôle
Commande réellement exécutée dans le conteneur : Python/SymPy (symboles positifs A,K,M,MF,Y,Z,H), définition `P=-2*A**2*sqrt(H+K*M)`, `U=MF*Y*(P-2*A*Z)`, `Minv=(p**2/(4*A**4)-H)/K`, puis cinq assertions `sympy.simplify` : dérivées première/seconde de P, dérivée seconde de U, dérivées première/seconde de Minv. **5 PASS, 0 FAIL**. Contrôle indépendant : substitution directe de Minv dans `PG²-4*A⁴*(Hbase+M2*K)` donne zéro identique ; branche physique négative seulement si PG<0 et H2>0.

**Portée :** la tangente centrale s'intègre exactement dans ces deux seules relations ; une extrapolation *linéaire* de M2(PG) n'est pas une famille exacte au second ordre. Cela ne prouve aucune famille de solutions radiales, aux deux vrais bords ou de Dirac. Il faut recalculer la géométrie et la source à chaque M2. Zéro cellule physique Step55/58 évaluée ou certifiée.

NEXT_ACTION_EXACT : calculer `G_M2(s,U)` total depuis `geometry(s)` et `normalized_symbolic()`, en incluant PG(M2), puis résoudre la variation radiale et tester les deux vrais bords/Dirac ; en parallèle JANUS-001 transférer les modules originaux et lancer les neuf tests puis pilote. `GATE_2B=OPEN`, `JANUS_R=NOT_VALIDATED`.

# JANUS-005 — Rang de la relation centrale Step55 (2026-11-11)

Source examinée à main 10895b06d9d7bb8e3b2ea1ec8e57d8fd06fd77b0 : `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Il définit `B=A*Y` et `U0=MF*B*(PG/A-2*Z1)` avec A,Y,MF,Z1 prescrits. Le rapport antérieur `JANUS005_PG_ONLY_CENTRAL_TANGENT_CONDITIONAL_20261111.md` avait calculé `dU0/dPG=MF*Y`.

## Proposition et vérification indépendante

Dans l'espace formel (PG,U0) avec A,Y,MF,Z1 constants et A non nul, définir la relation centrale prescrite `C(PG,U0)=U0-MF*A*Y*(PG/A-2*Z1)=0`. Son jacobien est exactement `J_C=(-MF*Y,1)`, de rang 1. Son noyau est engendré par `t=(1,MF*Y)`, et `J_C*t=0`. En revanche, la variation artificielle `(1,0)` (PG varie, U0 fixé) donne `J_C*(1,0)=-MF*Y != 0` pour MF,Y non nuls.

Commande réellement exécutée dans Python/SymPy : construction symbolique de C, `J=s.Matrix([[s.diff(C,P),s.diff(C,U)]])`, `J.rank()`, `J*s.Matrix([1,M*Y])`, `J*s.Matrix([1,0])`, puis assertion `J.rank()==1 and J*t==s.zeros(1,1)`. Résultat : PASS, rang 1, tangent dans le noyau, variation U0 fixe hors noyau. Contrôle manuel indépendant : `C=U0-MF*Y*PG+2*A*MF*Y*Z1` rend les deux dérivées immédiates.

## Portée et falsification

**La relation centrale déjà imposée par Step55 n'exclut PAS la tangente PG-only accompagnée de sa variation U0.** Ajouter arbitrairement `U0=const` crée une deuxième contrainte indépendante et élimine cette tangente, mais rien dans ce calcul n'établit qu'une telle condition physique existe. Le rang 1 est celui de cette unique relation algébrique, PAS le rang de Dirac ni celui du problème aux deux vrais bords. Aucune solution globale ni admissibilité physique prouvée. Le résultat écarte la piste consistant à traiter `dU0/dPG !=0` comme contradiction de la relation centrale elle-même.

## NEXT_ACTION_EXACT

Lire les conditions de bord et les contraintes originales Step45/49/55 ; extraire une contrainte supplémentaire authentique `F(PG,U0,...)=0`, calculer son gradient **avec toutes les autres variables autorisées à varier**, puis vérifier si `dF(t)=0`. Ne pas supposer de condition `U0=const` sans source. Pour JANUS-001, transférer les 18 modules et tests authentiques, contrôler les blobs Git, rejouer la suite et le pilote.

Tests physiques Step55/58 rejoués : 0 ; nouvelles cellules évaluées : 0 ; certifiées : 0. GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.

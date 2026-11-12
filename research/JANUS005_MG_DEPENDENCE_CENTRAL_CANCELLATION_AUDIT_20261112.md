# JANUS-005 — Dépendance de l'annulation centrale à MG (2026-11-12)

Source : `numerics/hr_step55_global_barrier.py` au HEAD `337abe692c72bee04fecf8eb952c8801a2a85dc8`. Audit contradictoire du résultat précédent `d Rhog(0)/d M2=0`.

Posons `K=B0+3*B1*Y+3*B2*Y**2+B3*Y**3`, `H2=0.9/(3*A**3)+M2*K/3`, `PG=-2*A**2*sqrt(H2)`. À `s=0`, la source donne `Lg=A, Gmom=PG, Gprime=2*PG, fac=PG/(2*MG*A**2), Rg=-48*CG/A**2, Wgbar=M2*MG*A**3*K, betag=1`. En les substituant dans la formule originale de Rhog, la dérivée totale à A,Y,CG,MG et coefficients B constants est exactement :

`d Rhog(0)/d M2 = -A**3*(MG**2-1)*K/MG`.

À `MG=1` (valeur fixée par Step55), la dérivée est identiquement nulle : le résultat précédent est confirmé. Elle n'est **pas universellement nulle** à MG fixé mais différent de 1. Contre-exemple algébrique : `MG=2,A=Y=B0=1,B1=B2=B3=0,M2>0` donne `-3/2`, avec H2>0. Ce n'est pas une réfutation physique de JANUS : ce choix sort de la carte MG=1 du benchmark.

Rejeu réel en Python/SymPy : construction des expressions ci-dessus, `sympy.factor(sympy.diff(rho,M2))`, contrôle `simplify(der-expected)==0`, contrôle MG=1, contrôle du contre-exemple : **3 PASS, 0 FAIL**. La formule Rhog utilisée est `-(PG**2/(4*MG*A)-(PG/(2*MG*A**2))*(A*2*PG)-MG*A**3*(-48*CG/A**2)/2+M2*MG*A**3*K)`. Les commandes et formules permettent le rejeu sans dépendance au script éphémère.

Limites : audit algébrique central, sans Step55/58 exécuté, aucune cellule physique calculée ou certifiée, aucun vrai bord ni Dirac. `GATE_2B=OPEN`, `JANUS_R=NOT_VALIDATED`.

NEXT_ACTION_EXACT : dériver `G_M2(s,U)` total à MG=1 depuis Step45/46 et geometry(s), résoudre la variation radiale, tester les deux vrais bords et Dirac ; JANUS-001 : transférer les sources originales, vérifier les empreintes, rejouer neuf tests et pilote une cellule.

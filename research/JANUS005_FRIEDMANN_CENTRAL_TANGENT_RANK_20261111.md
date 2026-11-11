# JANUS-005 — contrainte de Friedmann centrale, 11 novembre 2026

Source authentique : `numerics/hr_step55_global_barrier.py` au HEAD `12ad814b66a218091e0109923e0f288498794436`. Le fichier prescrit `H2=.9/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3`, `PG=-2*A**2*sqrt(H2)` et `U0=MF*Y*(PG-2*A*Z1)`. Pour A,Y,M2,B0..B3,MF,Z1 fixés, H2 est constant, PG<0.

Définissons C=U0-MF*Y*(PG-2*A*Z1), F=PG²-4*A⁴*H2. Le jacobien de (C,F) en (PG,U0) est [[-MF*Y,1],[2*PG,0]], de déterminant **-2*PG**, non nul sur la branche prescrite PG<0. La tangente t=(1,MF*Y), auparavant dans le noyau de dC, donne dF(t)=2*PG !=0. **NO-GO circonscrit** : PG-only avec paramètres de Friedmann fixés n'est pas une famille de solutions des deux relations centrales prescrites. Le précédent rang 1 ne concernait que C.

Contrôle exécuté avec Python/SymPy 1.14.0 : `J=Matrix([C,F]).jacobian([PG,U0]); J.det(); J*Matrix([1,MF*Y]); diff(F,H2)`. Trois assertions exactes PASS : déterminant -2PG, Jt=(0,2PG), dérivée de F en H2 = -4A⁴. Une première assertion avec le signe erroné +2PG a FAIL ; corrigée puis trois assertions PASS. Vérification manuelle indépendante par expansion de C et F.

Limite : si A ou H2 varient, `2PG*dPG-4A**4*dH2-16*A**3*H2*dA=0` peut permettre dPG non nul. Il faut alors dériver H2 par rapport aux paramètres autorisés et contrôler les deux vrais bords. Aucune réfutation de JANUS général, de la solution radiale fixe, ni preuve sur le rang de Dirac.

NEXT_ACTION_EXACT : construire le jacobien de (C,F,conditions aux deux vrais bords) avec toutes les variables physiquement libres et tester son noyau. JANUS-001 : transfert authentifié des dépendances, tests puis pilote.

Tests Step55/58 rejoués : 0. Cellules physiques évaluées : 0 ; certifiées : 0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

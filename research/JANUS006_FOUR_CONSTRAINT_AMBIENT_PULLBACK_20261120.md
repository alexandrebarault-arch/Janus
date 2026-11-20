# JANUS-006 — Pullback sur les quatre contraintes ambiantes (2026-11-20)

## Provenance et hypothèse
Au HEAD ad9f06f4a172ce47d9882dffefef74ce2c5909ed, Step45 Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, rapport du témoin `research/JANUS006_ON_SHELL_ALTERNATIVE_MINOR_WITNESS_20261120.md` (blob `d7b87caeb3d0989eef142e0ca5980cbbd47da476`), et rapport du pullback Fz `research/JANUS006_FZ_PULLBACK_BOUNDARY_TWO_FORM_20261120.md` (blob `e20ce762345b652227fc9123855d49150be0b341`). **La matrice du témoin vient d'une transcription locale de Step45 non authentifiée octet à octet ; la présente conclusion est conditionnelle à sa fidélité.**

Hypothèse à tester : la non-fermeture de la forme de bord pourrait disparaître dès qu'on impose simultanément les quatre contraintes algébriques Hg,Hf,Fz,C_exact, même si elle persiste sur Fz seul.

## Argument exact — théorème des fonctions implicites
Au témoin du rapport précédent, Hg=Hf=Fz=C_exact=0, K=16>0, Lg=Lf=N=M=1 et le jacobien des contraintes par rapport à y=(Sgrr,Sfrr,pLgr,pSf) est diag(2,6,-1,-8/3), de déterminant **32**. Fixons tous les autres jets et paramètres sauf les deux variables libres u=pLg et v=z. Par le théorème des fonctions implicites, il existe localement une application y=y(u,v) conservant exactement les quatre contraintes, pour |z|<1 et dans le domaine régulier. Ses directions tangentes satisfont les quatre différentielles des contraintes (sans imposer d'holonomie).

Sur Fz=0 et K>0, Z=z exactement ; avec lapses et Lg/Lf fixes, P=(N+M Lg/Lf)pLg=a u, a=2. La restriction de dTheta=dP∧dZ au graphe des quatre contraintes vaut donc **a du∧dv=2 du∧dv**, strictement non nulle au témoin. Ce n'est pas une simple non-fermeture sur Fz : elle persiste sur la sous-variété algébrique locale définie par les quatre contraintes. Le résultat est local et conditionnel à la fidélité de la transcription du jacobien ; il ne suppose pas que y(u,v) est le jet d'une solution radiale.

## Calcul réellement exécuté et contre-contrôles
Commande : `python - <<'PY'` (SymPy 1.14.0), matrice J=diag(2,6,-1,-8/3), `J.det()` retourne 32 et `J.inv()` retourne diag(1/2,1/6,-1,-3/8). Le déterminant de la matrice des dérivées (P,Z) par rapport à (u,v) est `det([[a,0],[0,1]])=a`. Pour K=16, substitution D=16z/sqrt(1-z²) dans Z=D/sqrt(D²+256) donne Z=z sur |z|<1 ; dérivée au témoin z=0 égale 1. PASS. Contrôle indépendant : la résolution successive des quatre contraintes est permise par les pivots diagonaux 2,6,-1,-8/3 ; le produit extérieur d(2u)∧dv est 2du∧dv. PASS.

## Portée, limites, falsification
**Non-fermeture sur la variété des quatre contraintes algébriques dans l'espace ambiant des jets**, conditionnelle à la transcription Step45 ; **pas** de NO-GO physique : les variations y(u,v) peuvent violer l'holonomie Sgr=Sg', Sgrr=Sg'', plgr=pLg', etc., la fixation de N,M par Dirac, et les deux vraies conditions de bord. L'espace de jets ambiant contient davantage de directions que l'espace des solutions physiques. Aucune certification d'intervalle ou cellule physique.

Tests b3c3d9 : SKIP ; pilote : SKIP ; cellules demandées/tentées/évaluées/certifiées/inconclusives : 0/0/0/0/0.

**NEXT_ACTION_EXACT :** (1) transférer les octets exacts de Step45, vérifier `git hash-object` = `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, rejouer le témoin et J ; (2) imposer holonomie, Dirac/lapses et les deux vraies traces au graphe y(u,v) et recalculer le pullback ; (3) JANUS-001 authentifier les dépendances Step45/46/55/58, exécuter neuf tests et pilote à une cellule. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# JANUS-006 — coefficient non dégénéré du jet radial supérieur (2026-11-21)

## Provenance et portée
HEAD de lecture `4b7b8810e06b1e1fcab150ff1fac42489e68e44c`. Suite algébrique du rapport `research/JANUS006_DOUBLE_RADIAL_JET_INTEGRABILITY_20261121.md` (formules transcrites, NON authentifiées par exécution locale de Step45). Le module Step45 a été relu sur GitHub, blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Aucun test physique Step55/58 ni réduction Dirac.

## Résultat exact conditionnel
Poser `L=Lg, m=mg, S=Sg, h=Sgr, p=pLg, u=pSg, q=1+rho*Lg/Lf, z=z, v=Lg', w=c'`, et `c=z*q*L/(2*m*S)`. Avec A et B du rapport antérieur, la branche non triviale forcée se simplifie en

`T=-2*(L**2*p + 2*L*S*h*m*q*z + L*S*u*q**2*z**2 - L*S*u - 2*v*S**2*m*q*z + 4*S**3*w*m**2)/(L**2*(1+q**2*z**2))`.

Vérification SymPy : `factor((w-A+c*c*u/L)/B-T)==0` PASS. En particulier, `partial(T)/partial(p)=-2/(1+q**2*z**2)` et `partial(T)/partial(w)=-8*S**3*m**2/(L**2*(1+q**2*z**2))`, non nuls sur le domaine réel régulier `L,m,S>0`. Ces deux dérivées ont été obtenues par différentiation symbolique de la forme factorisée ; contrôle manuel du coefficient linéaire PASS.

## Conséquence falsifiable et limites
Dans `R=T'-(u*c/L)*T`, la contribution de `c''` est exactement `-8*S**3*m**2/(L**2*(1+q**2*z**2))*c''`. Sous réserve que les autres jets radiaux soient fixés indépendamment, la compatibilité `R=0` détermine donc une valeur unique de `c''` ; elle n'est pas une identité automatique des seules deux holonomies précédentes. ATTENTION : `c''` dépend des jets de z,q,L,S, et ceux-ci peuvent être contraints par les équations complètes ; ce constat ne prouve ni liberté de choisir c'', ni contradiction physique. Aucun NO-GO JANUS, aucune existence globale, aucune condition aux deux bords vérifiée.

Commande de contrôle (Python 3, SymPy) : définir les symboles `L,m,S,h,p,u,q,z,v,w`, `c=z*q*L/(2*m*S)`, `A=-(L**2*p+2*L*S*h*m*q*z-L*S*u-2*v*S**2*m*q*z)/(4*S**3*m**2)`, `B=-L**2*(1+q**2*z**2)/(8*S**3*m**2)`, puis `T=factor((w-A+c*c*u/L)/B)`, `factor(diff(T,w))` et `factor(diff(T,p))`. Cette vérification a été exécutée en Python/SymPy, mais pas depuis les modules originaux reconstruits.

JANUS-001 : tests SKIP ; pilote SKIP ; cellules demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0.

**NEXT_ACTION_EXACT :** reconstituer et authentifier Step45 en Python, exprimer `c''` par les jets radiaux de z,q,L,S, réduire R sous Hg=Hf=Fz=C_exact et les équations de Dirac ; tester les deux vraies traces. Pour JANUS-001, reconstituer les dépendances historiques et exécuter neuf tests puis pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

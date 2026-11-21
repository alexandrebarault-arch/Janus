# JANUS-006 — Compatibilité simultanée des deux jets radiaux (2026-11-21)

## Sources et portée
HEAD de lecture `8344afd79a7d4e6d816fff60ef479abcc58dc989`. Dérivation nouvelle à partir de la tranche compensatrice explicitée dans `research/JANUS006_RADIAL_RICCATI_INTEGRABILITY_20261120.md` (blob `b900f49116150fd5dec39be4021a21c64eebde36`). Les formules de départ sont une transcription de Step45 et ne constituent pas une exécution authentifiée du moteur original. **Résultat nécessaire conditionnel sur cette tranche, non NO-GO JANUS.**

## Hypothèses et deux équations nécessaires
Sur un intervalle régulier, supposer `c=z*q*Lg/(2*mg*Sg) != 0`, avec `Lg,mg,Sg>0`, `q=1+rho*Lg/Lf`, et une solution de référence holonome. La famille du rapport antérieur est
`pLg=p0+t`, `Sgr=h0+c*t`, `Sgrr=u0+A*t+B*t²`, `plgr=plgr0+(psg*c/Lg)*t`.
Elle préserve ponctuellement D et Hg. L'holonomie de Sg impose
`c*t'=(A-c')*t+B*t²`.
**L'holonomie supplémentaire de pLg**, `plgr=(pLg)'` et `plgr0=p0'`, impose indépendamment
`t'=(psg*c/Lg)*t`.
Par élimination de t', nécessairement
`t*[B*t + A-c'-(psg*c²/Lg)]=0`.
Ainsi, lorsque `B!=0`, toute branche non nulle doit satisfaire point par point
`t=(c'-A+psg*c²/Lg)/B` **ET** l'équation différentielle `t'=(psg*c/Lg)t`. Cette seconde exigence est cruciale : substituer la valeur algébrique dans l'ODE fournit un test différentiel supplémentaire sur les données de référence. Une égalité algébrique en un rayon ne suffit pas à construire une famille radiale.

Pour les coefficients du rapport précédent,
`B=-Lg²*(1+q²*z²)/(8*Sg³*mg²)`, donc `B<0` sur le domaine réel régulier avec `Lg,mg,Sg>0`. La branche non nulle est donc au plus unique **à chaque rayon**, sans preuve d'existence sur un intervalle. Si `t=0` en un rayon, l'ODE linéaire de l'holonomie de pLg donne `t≡0` sur la composante régulière (pour coefficients continus), indépendamment de la Riccati.

## Contrôle exact exécuté
Python 3 + SymPy 1.14.0 : symboles non nuls réels `L,mg,S,h,p,psg,q,z,Lr,cprime`, `c=z*q*L/(2*mg*S)`, `A=-(L**2*p+2*L*S*h*mg*q*z-L*S*psg-2*Lr*S**2*mg*q*z)/(4*S**3*mg**2)`, `B=-L**2*(1+q**2*z**2)/(8*S**3*mg**2)`, `T=(cprime-A+c*c*psg/L)/B`. Vérifications `factor((c*(psg*c*t/L)-(A-cprime)*t-B*t*t).subs(t,T)) == 0` et même expression à `t=0` : PASS. Factorisation de B : PASS. Contrôle indépendant par soustraction directe des deux équations différentielles : PASS.

## Limites et prochaine falsification
Il faut maintenant calculer la dérivée totale radiale de `T(r)` avec les vrais jets de la solution de référence et vérifier l'identité `T'-(psg*c/Lg)*T=0`, puis imposer Hf, Fz, C_exact, Dirac/lapses et les deux véritables bords. Aucun de ces tests physiques n'a été effectué. La branche `t=0` n'est pas imposée par la seule condition Dirichlet canonique, qui ne fixe pas les moments aux bords. Aucun certificat d'intervalle, aucune cellule physique évaluée.

JANUS-001 : tests b3c3d9 SKIP ; pilote SKIP ; cellules demandées/tentées/évaluées/certifiées/inconclusives : 0/0/0/0/0.

**NEXT_ACTION_EXACT :** sur Step45 authentifié, reconstituer c,A,B et calculer symboliquement la dérivée totale de T le long de la solution de référence ; tester si `T'-(psg*c/Lg)*T` peut s'annuler avec les quatre contraintes et les deux vraies traces. En parallèle, JANUS-001 reconstruire les dépendances authentifiées puis exécuter neuf tests et pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

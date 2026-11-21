# JANUS-006 — coefficient du jet de shift z'' dans la double holonomie (2026-11-21)

## Domaine et provenance
Lecture GitHub de main au SHA `e91568a2f4cb7b72992d6ec82ad1882f0f3d3f09`, module Step45 blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Suite **conditionnelle** de `JANUS006_HIGHER_RADIAL_JET_COMPATIBILITY_20261121.md` : les expressions de T sont transcrites dans les rapports et n'ont pas été rejouées par import local authentifié de Step45. Aucun résultat physique Step55/58.

Poser `c=L*q*z/(2*m*S)`, `q=1+rho*L/Lf`, `L=Lg`, `S=Sg`, `m=Mg2` et la branche compensatrice non nulle `t=T` du rapport antérieur. Son coefficient en `w=c'` vaut `T_w=-8*S**3*m**2/(L**2*(1+q**2*z**2))`. La compatibilité radiale est `R=dT/dr-(pSg*c/L)*T=0`.

## Nouveau calcul exact
Le terme en `z''` provient de `T_w*c''` puisque `T` dépend des autres champs et de `w=c'`, mais pas explicitement de `z'` ailleurs que par w (à jets indépendants). Avec `partial(c'')/partial(z'')=partial(c)/partial(z)=L*q/(2*m*S)`, on obtient

`partial(R)/partial(z'') = -4*S**2*m*q/(L*(1+q**2*z**2))`.

Ce coefficient est strictement négatif si `L,S,m,q>0` et `z` réel ; il ne s'annule pas sur ce domaine. En particulier, la condition R=0 fixe **conditionnellement** le jet z'' lorsque tous les autres jets d'ordre 2 pertinents sont prescrits. Cela n'établit pas que z'' soit une variable libre après différentiation de Fz, Hg, Hf, C_exact ou application de Dirac. Les équations peuvent déterminer le même jet ou engendrer une contradiction ; aucune des deux issues n'est démontrée ici.

## Contrôles reproductibles
Python 3 / SymPy 1.14.0, script de contrôle effectivement exécuté en session (`/tmp/janus_check.py`, non persistant) : définir `L,m,S,h,p,u,q,z,v,w=s.symbols(...)`; `c=z*q*L/(2*m*S)`; `T=-2*(L**2*p+2*L*S*h*m*q*z+L*S*u*q**2*z**2-L*S*u-2*v*S**2*m*q*z+4*S**3*w*m**2)/(L**2*(1+q**2*z**2))`; `factor(diff(T,w)*diff(c,z))`. Résultat exact : `-4*S**2*m*q/(L*(q**2*z**2+1))`; soustraction de la formule attendue = 0. Contrôle indépendant : développer `c''` par deux dérivations totales avec jets `L',m',S',q',z'` et `L'',m'',S'',q'',z''`, puis `factor(diff(c2,zrr)) = L*q/(2*S*m)`, et `diff(c2,zrr)-diff(c,z)=0`. PASS.

Autres coefficients directs de R via c'' (jets considérés indépendants) : `q'' : -4*S**2*m*z/(L*(1+q**2*z**2))`, `L'' : -4*S**2*m*q*z/(L**2*(1+q**2*z**2))`, `S'' : +4*S*m*q*z/(L*(1+q**2*z**2))`. Attention : `q=1+rho*L/Lf` implique que q'' n'est pas indépendant en dynamique réelle. Ces coefficients sont **partiels** et ne remplacent pas le coefficient total après cette substitution.

## Limites et prochaine falsification
Aucune source Step45 importée localement, aucune réduction des quatre contraintes, aucune matrice de Dirac, aucun lapse fixé, aucune condition aux deux vrais bords ; ce n'est ni une solution ni un NO-GO physique. Tests b3c3d9/pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0.

**NEXT_ACTION_EXACT :** authentifier Step45 et rejouer T depuis les expressions originales ; substituer `q=1+rho*Lg/Lf`, calculer `D_r(Fz)=0` et `D_r^2(Fz)=0` avec jets holonomes, puis comparer leur coefficient de z'' à celui de R et tester le rang du système conjoint sous Hg=Hf=C_exact=0 ; ensuite Dirac et les deux vrais bords. Pour JANUS-001, reconstruire les imports historiques et exécuter neuf tests puis pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

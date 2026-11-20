# JANUS-006 — Intégrabilité radiale de la levée par Sg'' : équation de Riccati et obstruction à donnée nulle (2026-11-20)

## Provenance
HEAD fixé : `bc83e8bd095a560b6196c07a93f7a0f6e0b47aee`. Source immédiate : `research/JANUS006_HG_SECOND_JET_EXACT_LIFT_20261120.md`, qui transcrit les termes pertinents de Step45. Ce travail est une **analyse conditionnelle de la tranche algébrique**, non un calcul de solution physique complète.

## Question et hypothèses
La compensation finie de `Hg` par `u=Sg''` peut-elle être le jet d'une fonction radiale `Sg(r)` ? On suppose un intervalle radial régulier, une famille de données de référence différentiables satisfaisant `h0=Sg0'`, `u0=Sg0''=h0'`, et des coefficients radiaux lisses, `Lg,mg,Sg>0`, `c(r)=z*q*Lg/(2*mg*Sg) != 0`. Ici `q=1+rho*Lg/Lf` et `z=Z0` sont ceux de la tranche. On laisse `t=t(r)` plutôt qu'un paramètre constant, avec `p=p0+t`, `h=h0+c*t`, `plgr=plgr0+(psg*c/Lg)*t`, de sorte que `D` reste constant **ponctuellement en r** par rapport à la référence.

## Calcul exact
En reprenant le Hamiltonien polynomial du rapport antérieur, l'unique compensation algébrique par `u` s'écrit
```
u = u0 + A(r)*t + B(r)*t**2
A = -(Lg**2*p0 + 2*Lg*Sg*h0*mg*q*z - Lg*Sg*psg
      - 2*Lgr*Sg**2*mg*q*z)/(4*Sg**3*mg**2)
B = -Lg**2*(1+q**2*z**2)/(8*Sg**3*mg**2)
```
Le contrôle SymPy 1.14.0 de `H(p0+t,h0+c*t,u)-H(p0,h0,u0)==0` donne PASS. L'intégrabilité nécessaire `u=dh/dr` impose
```
c*t' = (A-c')*t + B*t**2.
```
C'est une équation de Riccati homogène (sans terme constant). Si `c` ne s'annule pas et les coefficients sont continus, le second membre est localement lipschitzien en `t`. Par unicité du problème de Cauchy, **t(r*)=0 en un point de l'intervalle impose t identiquement nul sur toute la composante régulière**. Une famille non triviale de ce graphe qui doit fixer `pLg` à un bord (même un seul) ne peut donc satisfaire simultanément cette intégrabilité et cette condition de bord homogène, sous ces hypothèses. Il existe au contraire des solutions locales non nulles pour des données initiales non nulles ; la compensation n'est pas universellement impossible.

## Contrôle indépendant et limites
La conclusion d'unicité suit directement du théorème standard d'unicité ODE : `t'=f(r)t+g(r)t²`, `f=(A-c')/c`, `g=B/c`, et `t=0` est une solution. C'est indépendant du contrôle symbolique de conservation de Hg. Une vérification SymPy des coefficients `A,B` et de l'identité polynomiale a été exécutée localement, PASS, avec Python/SymPy 1.14.0. Reproduction minimale : définir `H=Lg*p**2/(4*mg*Sg**2)-p*psg/(2*mg*Sg)+mg*h**2/Lg+2*mg*Sg*u/Lg-2*mg*Sg*h*Lgr/Lg**2`, `c=z*q*Lg/(2*mg*Sg)`, puis `Delta=expand(H(p+t,h+c*t,u)-H(p,h,u))`, `A=-Lg/(2*mg*Sg)*diff(Delta,t).subs(t,0)`, `B=-Lg/(4*mg*Sg)*diff(Delta,t,2)`; vérifier `simplify(H(p+t,h+c*t,u+A*t+B*t*t)-H(p,h,u))==0`.

**Ne pas confondre :** le véritable problème à deux bords ne fixe pas nécessairement `pLg` ; la condition `t(r*)=0` est une hypothèse supplémentaire, non établie par les traces physiques. La constance radiale de `D` n'est pas affirmée : seulement sa préservation relativement à la référence à chaque r. L'intégrabilité de `plgr`, les variations des autres champs, `Hf,Fz,C_exact`, les deux véritables traces et le rang Dirac ne sont pas testés. Si `c=0` ou est singulier, le théorème d'unicité ci-dessus ne s'applique pas. Aucun NO-GO global pour JANUS.

Tests moteur b3c3d9 SKIP ; pilote SKIP ; cellules physiques demandées/tentées/évaluées/certifiées/inconclusives : 0/0/0/0/0.

**NEXT_ACTION_EXACT :** lire les définitions canoniques des deux vraies traces de bord et déterminer si elles imposent effectivement une donnée homogène sur `t` ; imposer aussi l'intégrabilité de `plgr` et construire le jacobien conjoint `Hg,Hf,Fz,C_exact`. JANUS-001 : reconstruire les imports historiques authentifiés Step45/46/55/58, puis neuf tests et pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

## Contrôle de portée sur la vraie convention Dirichlet du dépôt
Lecture authentifiée au même cycle de `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py` (blob `6898c88760cc0766e949f9bade4908b9bc176c58`) : commentaire explicite `Fixed canonical configuration q=(Lg,Sg,tg,Lf,Sf,tf), fixed N,M,V` et `Other endpoint momenta and first jets are independent ambient variables`. Donc **cette convention Dirichlet ne fixe pas pLg aux bords**. Le corollaire `t(r*)=0 => t≡0` est mathématiquement correct mais **n'est pas applicable à la seule condition Dirichlet canonique telle qu'écrite dans cette source**. L'audit des conditions physiques complètes reste nécessaire ; ne pas interpréter ce corollaire comme une obstruction au problème Dirichlet du dépôt.

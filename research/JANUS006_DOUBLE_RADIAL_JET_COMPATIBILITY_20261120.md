# JANUS-006 — Compatibilité simultanée des deux jets radiaux (2026-11-20)

## Provenance et hypothèses
HEAD source fixé : `6c1cc46519c7e95f99a1ae2c80bde9f2fe8078c6`. Sources : `numerics/hr_step45_exact_physical_ward.py` (identification de `plgr=d(pLg)/dr` et `Sg2=d(Sgr)/dr`), `research/JANUS006_HG_SECOND_JET_EXACT_LIFT_20261120.md` et `research/JANUS006_RADIAL_RICCATI_INTEGRABILITY_20261120.md`. Résultat **conditionnel à la même tranche** : tous les champs de fond et leurs profils radiaux restent fixés, `p=p0+t(r)`, `h=h0+c(r)t`, `plgr=plgr0+(psg*c/Lg)t`, `u=u0+A(r)t+B(r)t²`, avec `p0'=plgr0`, `h0'=u0`, `Lg,mg,Sg>0`, `c≠0`, coefficients C1 et `B=-Lg²(1+q²z²)/(8*Sg³*mg²)<0`. Ne pas supposer ces variations admissibles sur la coquille Dirac.

## Deux équations nécessaires, et leur intersection
L'intégrabilité de `plgr` **en plus** de celle de `Sg2` donne :
```
t' = k*t,                         k=psg*c/Lg
c*t' = (A-c')*t+B*t**2
=> t*[A-c'-c*k+B*t]=0.
```
Sur une composante connexe régulière, toute solution non nulle de `t'=k*t` ne s'annule jamais. Elle doit donc satisfaire **partout**
```
t=T(r)=(c*k-A+c')/B,
T'(r)-k(r)*T(r)=0.
```
Ainsi, si le résidu différentiel `R=T'-k*T` n'est pas identiquement nul sur un intervalle, **aucune solution non triviale de cette tranche à deux jets intégrables n'existe sur cet intervalle**. Si `R=0` et `T` est non nul, `t=T` est une solution de ces deux relations nécessaires ; cela ne suffit pas à satisfaire Hf, Fz, C_exact, les conditions aux bords ou la dynamique. Si `T=0` identiquement, seule la solution triviale subsiste. L'argument est un critère de compatibilité, non un NO-GO physique universel.

## Contrôle reproductible et contradictoire
Python/SymPy (exécuté dans cette session) :
```python
import sympy as s
A,B,c,cp,k,t=s.symbols('A B c cp k t',nonzero=True)
ric=(A-cp)*t+B*t*t-c*k*t
T=(c*k-A+cp)/B
assert s.simplify(ric.subs(t,T))==0
assert s.simplify(ric-t*B*(t-T))==0
print("PASS")
```
Contrôle indépendant : l'équation linéaire `t'=kt` a la solution `t(r)=t(r0)*exp(integral(k))`; toute solution non triviale est partout non nulle. Substituer dans la Riccati impose alors `t=T` et la condition `T'=kT`. Un choix de coefficients permettant `T'=kT` montre que l'obstruction n'est pas universelle. Le calcul ne prétend pas que ces coefficients proviennent d'une solution physique.

## Limites et prochaine étape
Le résidu R n'a **pas** été évalué pour les profils physiques Step55 : les fonctions de fond et leurs dérivées authentifiées sont nécessaires. Les conditions aux deux vrais bords ne fixent pas directement pLg dans la convention Dirichlet citée dans le rapport Riccati. Les relations de préservation ponctuelle de D, Z et Hg restent algébriques. Aucun test moteur b3c3d9 ni pilote : cellules demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0.

**NEXT_ACTION_EXACT :** substituer les profils radiaux authentiques Step45/55 dans `c,A,B,k`, calculer `R=d[(c*k-A+c')/B]/dr-k*(c*k-A+c')/B` sur une solution de fond vérifiée ; tester sa non-nullité ou son annulation avec contrôle indépendant. Ensuite confronter la direction au jacobien `Hg,Hf,Fz,C_exact` et aux deux vraies traces. JANUS-001 : reconstruction octet-authentifiée, neuf tests puis pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

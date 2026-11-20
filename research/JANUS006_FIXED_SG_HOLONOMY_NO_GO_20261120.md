# JANUS-006 — Audit de holonomie du premier jet sur fond fixé (2026-11-20)

## Sources et hypothèses
HEAD lu : `57058a64bb5b1cb06c369cbab0c09bbbf6f106ee`. Sources authentifiées : `numerics/hr_step45_exact_physical_ward.py` (blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`), `research/JANUS006_HG_SECOND_JET_EXACT_LIFT_20261120.md` (blob `7600ad81a06262fc584aad3fd53308ae22f3c282`), `research/JANUS006_DOUBLE_RADIAL_JET_COMPATIBILITY_20261120.md` (blob `ae342e298da1a66ec06f05817da23d244c75507c`). Aucun nouveau profil physique n'est supposé.

## Test de cohérence supplémentaire : h=Sg' ET Sg fixé
La famille compensatrice écrit `h=h0+c*t`, avec `h0=Sg0'` et `c=z*q*Lg/(2*mg*Sg)`. Dans la tranche annoncée, `Sg(r)=Sg0(r)` est maintenu comme **profil** sur un intervalle. Toute famille de champs radiaux différentiables vérifiant la relation holonome `h=Sg'` doit donc satisfaire

`0=(Sg-Sg0)'=h-h0=c*t`.

Sur tout intervalle où `c != 0`, il suit **t=0 identiquement**. C'est un NO-GO exact pour toute compensation non triviale à **profil Sg fixé**, avant même les deux équations d'intégrabilité de jets dérivées précédemment. Si c s'annule ponctuellement, cette implication est seulement locale sur les ouverts où c est non nul ; aucune conclusion globale aux zéros sans régularité supplémentaire.

Contrôle Python/SymPy réellement exécuté :
```python
import sympy as s
r=s.symbols('r',real=True)
c=s.Function('c')(r); t=s.Function('t')(r)
print(s.simplify(s.diff(s.Integer(0),r)-c*t))  # -c(r)*t(r)
print(s.solve(c*t,t))                            # [0], sous c non nul
```
PASS. Contre-contrôle indépendant : théorème fondamental du calcul, `Sg-Sg0=0` sur un intervalle entraîne `Sg'-Sg0'=0` partout ; donc la variation `c*t` doit s'annuler. Aucun appel au Hamiltonien ni aux autres contraintes n'est requis.

## Portée et correction de lecture
Les résultats antérieurs de conservation algébrique de `D,Z,Hg` restent valables sur **l'espace des jets indépendants**, et le critère `R=T'-kT` reste une condition nécessaire dans son système formel. En revanche, la famille non triviale ne peut être un jet holonome de profils radiaux avec `Sg` strictement fixé. Le calcul du résidu R sur cette tranche ne constitue donc pas la prochaine expérience physique prioritaire : il faut d'abord libérer `delta Sg` et imposer `delta Sg'=c*t`, puis reconstruire toutes les équations de contraintes et les deux bords. Cela ne réfute pas JANUS ni les familles où Sg et les autres configurations varient.

Tests b3c3d9 et pilote : SKIP ; cellules demandées/tentées/évaluées/certifiées/inconclusives : 0/0/0/0/0. Aucune solution physique certifiée.

**NEXT_ACTION_EXACT :** introduire une variation radiale `sigma=delta Sg`, imposer `sigma'=c*t` et recalculer `delta D,delta Z,delta Hg` avec la dépendance explicite de c,A,B aux champs variables ; ensuite construire le jacobien conjoint `Hg,Hf,Fz,C_exact` et les deux traces. JANUS-001 : transférer les dépendances historiques authentifiées et exécuter les neuf tests puis pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

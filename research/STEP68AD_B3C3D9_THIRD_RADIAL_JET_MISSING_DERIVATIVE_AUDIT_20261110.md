# JANUS-004 — Audit contradictoire du jet radial d'ordre 3 (2026-11-10)

**Base examinée :** main `645fd8b0e8af845fbaeed558717ae6438a30da58`. Sources originales lues via GitHub : `numerics/hr_b3c3d9_annular_direct_enclosure.py` blob `b6fcee9e410b5702f94030ce8b0c6ec818004344`, `numerics/hr_b3c3d6_boundary_ANAM_interval_certificate.py` blob `7e998fbbda8f3854093d530dc5e7e07703d70624`, `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

## Problème vérifiable

Le runner fournit `physical_jet(rb, Jet.c(u), Jet.c(us), Jet.c(uss))`. Dans `physical_jet`, la fonction de fond est représentée par `uc=u+us*h+uss*h*h/2`, où `h=s-s0`. Il en résulte un jet radial d'ordre 3 construit à partir d'un Taylor **quadratique** en `s`. Le runner affecte ensuite `fields[name].val(3)` aux variables `qppp` du Step58. Sans une borne supplémentaire sur `U_{sss}`, ces valeurs ne sont pas, en général, des enclosures garanties des vraies dérivées radiales d'ordre 3. Une largeur d'intervalle sur `u,us,uss` ne remplace pas une borne sur la dérivée manquante.

## Contre-exemple exact, exécuté avec SymPy 1.14.0

Prendre `U(s)=s^3`, `s=r^2`, `s0=r0^2`, `pLf=s U(s)=r^8`. Le Taylor quadratique utilisant les jets exacts au centre est `Ut(s)=s0^3+3*s0^2*(s-s0)+3*s0*(s-s0)^2`. Alors

```python
import sympy as sp
r,r0=sp.symbols('r r0',positive=True)
s0=r0**2
U=(r*r)**3
Ut=s0**3+3*s0**2*(r*r-s0)+3*s0*(r*r-s0)**2
delta=sp.factor(sp.diff(r*r*(U-Ut),r,3).subs(r,r0))
assert delta == 48*r0**5
assert delta.subs(r0,sp.Rational(1,2)) == sp.Rational(3,2)
print('PASS:',delta)
```

**Exécution locale réelle : PASS**, `delta=48*r0**5`, `delta(1/2)=3/2`. Les valeurs de `U,U_s,U_{ss}` au centre sont **exactes**, et pourtant le jet radial d'ordre 3 de `pLf` manque `3/2` à `r0=1/2`. Ce contre-exemple est synthétique, non un calcul Step55 physique.

## Portée et contrôle contradictoire

Ceci démontre une insuffisance **générique** de la reconstruction des jets d'ordre 3, pas encore une fausse certification `A_N,A_M` pour les paramètres physiques. Le Step58 définit explicitement `qppp`, mais il reste à vérifier si les expressions finales `op['operator']['N'][0]` et `['M'][0]` dépendent effectivement des jets d'ordre 3 concernés après simplification/shell. Si leur dépendance est nulle, le défaut est inoffensif pour ce calcul précis ; sinon une borne authentique sur `U_{sss}` ou une élimination algébrique rigoureuse est requise avant toute certification. Ne pas remplacer la dérivée manquante par zéro sans preuve.

**Tests du dépôt : NON EXÉCUTÉS dans cette session** ; **cellules Step55/58 : 0 évaluée, 0 certifiée**. Git CLI : `fatal: unable to access 'https://github.com/alexandrebarault-arch/Janus.git/': Could not resolve host: github.com`. Le connecteur GitHub est opérationnel.

**NEXT_ACTION_EXACT :** authentifier/reconstruire les imports Step55/58 ; calculer pour chaque coefficient final `sp.diff(op['operator'][label][0], qppp[i])` (et les autres jets potentiellement manquants), tester leur nullité sur la coquille physique ; si non nuls, obtenir une enclosure de `U_{sss}` (via dérivation de l'ODE et secondes partielles de G) et réviser le runner avant de traiter les résultats comme des certificats. En parallèle reprendre JANUS-001 et son pilote physique.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**

# JANUS-006 — contre-exemple exact au mineur sur la strate z non nul (2026-11-20)

## Hypothèse testée
L'annulation du facteur conditionnel du mineur 4×4 rapporté dans JANUS006_C_EXACT_MOMENT_DERIVATIVE_20261120 serait limitée au plan z=0.

## Provenance et domaine
Formule P issue du rapport JANUS006_C_EXACT_MOMENT_DERIVATIVE_20261120, lui-même fondé sur une transcription locale de Step45 **non rejouée octet pour octet**. Ce résultat est donc **conditionnel à l'authenticité de cette formule** et ne porte pas sur la surface des quatre contraintes ni sur les deux bords.

P = 2 Lf Sg (Sf beta3 + Sg beta2) + Lg sqrt(1-z²)(Sg² beta1 - Sf² beta3).

Prendre Lg=Lf=Sg=beta1=beta2=beta3=m2=Mg2=Mf2=1, z=3/5, Sf=7/2. Alors sqrt(1-z²)=4/5 et

P = 2(7/2+1)+(4/5)(1-49/4) = 9-9 = 0.

At = Sg² beta1+2 Sg Sf beta2+Sf² beta3 = 1+7+49/4 = 81/4 > 0, donc K=m2 Mg2 Lg Lf At=81/4 >0, et z≠0. La contrainte Fz=0 peut être résolue algébriquement en pLg_r lorsque Lg=1, sans garantir les autres contraintes.

La dérivée de P par rapport à Sf vaut 2-(8/5) Sf = -18/5 au point choisi, non nulle. Par le théorème des fonctions implicites, l'hypersurface P=0 traverse localement une famille régulière à z non nul, tant que les autres paramètres sont maintenus.

## Reproduction
Commande réellement exécutée sous Python/SymPy 1.14.0 :

```python
import sympy as s
x=s.Rational(7,2); z=s.Rational(3,5)
r=s.sqrt(1-z*z)
P=s.factor(2*(x+1)+r*(1-x*x))
At=1+2*x+x*x
assert (P,At,r)==(0,s.Rational(81,4),s.Rational(4,5))
X=s.Symbol('x')
assert s.diff(2*(X+1)+r*(1-X*X),X).subs(X,x)==-s.Rational(18,5)
```

Contrôle arithmétique indépendant : 2(9/2)=9, (4/5)(-45/4)=-9 ; At=(1+7/2)²=81/4 ; dérivée 2-(8/5)(7/2)=-18/5.

## Verdict et limites
PASS : P=0 avec z≠0, K>0, paramètres positifs et transversalité locale dans l'espace ambiant. Cela réfute uniquement l'affirmation que P=0 serait confiné à z=0. **Ne prouve pas** la perte de rang du jacobien complet, l'existence d'une solution des quatre contraintes, l'intégrabilité radiale, ni les deux vraies conditions de bord. Source Step45 originale non exécutée ; tests b3c3d9 SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0.

**NEXT_ACTION_EXACT :** authentifier les octets Step45, rejouer la formule de P depuis exact_physical_ward(), puis substituer P=0 dans Hg=Hf=Fz=C_exact=0 et rechercher des mineurs alternatifs ; ensuite imposer intégrabilité et les deux bords. JANUS-001 : reconstruire dépendances historiques authentiques et lancer tests puis pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

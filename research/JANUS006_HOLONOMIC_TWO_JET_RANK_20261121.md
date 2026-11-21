# JANUS-006 — rang holonome à deux jets (2026-11-21)

## Source et hypothèses
HEAD source `356eadebb61bc68eb3b69f0375e8cb511d24d71f`. Lecture authentique via connecteur GitHub de `numerics/hr_step45_exact_physical_ward.py` : `Dg=psg*Sgr-Lg*plgr+pg*tgr` et `Fz=Dg-K*z/sqrt(1-z²)`, avec `K=m2*Mg2*Lg*Lf*At`. Le rapport précédent établit `R=a*z''+Q` où `a=-4*Sg²*Mg2*q/(Lg*(1+q²*z²))`. Ici Q est supposé indépendant de `pLg'''` et de `z''`, hypothèse à revérifier après réduction dynamique. K ne dépend d'aucun moment canonique dans Step45.

## Résultat vérifié
Par la règle de Leibniz, `∂D''/∂pLg'''=-Lg`. Donc, dans l'espace de jets **holonomes non réduits par Dirac**, le jacobien des deux prolongements `(R,Fz'')` par rapport à `(z'',pLg''')` vaut

```
[[a, 0],
 [-K/(1-z²)^(3/2), -Lg]]
```

et son déterminant exact est `-Lg*a = 4*Sg²*Mg2*q/(1+q²*z²)`, non nul lorsque `Lg,Sg,Mg2,q>0`, `|z|<1`. Le rang deux persiste **après substitution de la définition holonome de D**, tant que le troisième jet `pLg'''` est libre. Ce résultat ne suppose pas K non nul ; il couvre la strate K=0 sans division par K.

Contrôle exécuté : `python` / SymPy 1.14.0 avec `J=Matrix([[a,0],[-K/(1-z*z)**Rational(3,2),-L]])`; `factor(J.det())=-L*a` PASS et `simplify(J*J.inv()-eye(2))=zeros(2)` PASS. Contrôle indépendant : expansion diagonale `a*(-Lg)`.

## Limites et tentative de réfutation
Il s'agit d'un résultat de rang **cinématique**, pas d'un rang physique. Les équations hamiltoniennes, la fermeture Dirac, les deux lapses, les quatre contraintes complètes et les deux traces de bord peuvent retirer la liberté de `pLg'''` et annuler le rang réduit. La source Step45 ne fournit pas à elle seule une évolution temporelle complète des jets radiaux. Aucun NO-GO ni validation globale n'en découle.

JANUS-001 : tentative réelle `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` : FAIL `Could not resolve host: github.com` ; SymPy 1.14.0 disponible ; tests b3c3d9 SKIP, pilote SKIP, cellules physiques évaluées/certifiées/inconclusives 0/0/0. Aucun faux module ou résultat physique simulé.

**NEXT_ACTION_EXACT :** extraire les équations d'évolution et la chaîne de Dirac authentiques (au-delà du seul module Step45), prolonger ces relations jusqu'aux jets d'ordre trois, calculer le noyau tangent conjoint et son rang sur les deux vrais bords. En parallèle, pour JANUS-001, transférer les dépendances originales authentifiées Step45/46/55/58 et exécuter neuf tests puis pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# JANUS b3c3d6 — écran nécessaire exact d'admissibilité des lapses sur un anneau

28 octobre 2026. **Résultat mathématique conditionnel, non évalué sur Step58.**

Sur un anneau `[epsilon,R]` où `B_M != 0`, l'identité antérieure `W=M+qN`, `W'+pW=hN` (avec `q=B_N/B_M`, `p=A_M/B_M`, `h=q'+pq-A_N/B_M`) donne, avec `P(r)=int_epsilon^r p(s)ds` :

`(1+q(R))N(R) = exp(-P(R))W(epsilon) + int_epsilon^R exp(P(s)-P(R))h(s)N(s)ds`

si `M(R)=N(R)`. La formule est une **égalité nécessaire** sur toute solution ; elle ne garantit ni la positivité de `M`, ni la tangence Dirac.

Si `0<nlo(s)<=N(s)<=nhi(s)` est certifié et `hplus=max(h,0)`, `hminus=min(h,0)`, le membre de droite est compris entre

`L=exp(-P(R))W(epsilon)+int K(s)[hplus*nlo+hminus*nhi]ds`

et

`U=exp(-P(R))W(epsilon)+int K(s)[hplus*nhi+hminus*nlo]ds`, avec `K(s)=exp(P(s)-P(R))>0`.

Donc `T=(1+q(R))N(R)` **hors de `[L,U]` exclut** toute solution à lapses positifs respectant ces bornes. `T` dans `[L,U]` n'est PAS une preuve d'existence. Si `W(epsilon)` est seulement borné, remplacer sa valeur par ses bornes correspondantes dans `L,U`. Les intégrales exigent des bornes dirigées et des certificats de signe sur chaque cellule ; aucun milieu flottant n'est admissible.

## Témoins rationnels exacts (jouets)

Pour `epsilon=1/4`, `R=17/20`, `p=0`, `q=-1`, `W(epsilon)=-1/2`, `1/2<=N<=2`, `N(R)>0` :

- `h=-1` donne `L=-17/10`, `U=-4/5`, `T=0` : **exclusion exacte**.
- `h=+1` donne `L=-1/5`, `U=7/10`, `T=0` : **pas d'exclusion**. La solution explicite `N=5/6`, `M(r)=1/3+(5/6)(r-1/4)` est positive et satisfait `M(R)=N(R)` ainsi que `W'=hN`.
- Pour `h=r-1/2` sur `[1/4,3/4]`, les aires signées exactes sont `-1/32,+1/32` ; les bornes intégrales avec `1<=N<=2` sont `-1/32,+1/32` (sans terme initial). Ceci contrôle la partition par signes.

## Portée et verrou

Le programme joint ne traite **que** le cas `p=0`, `q,h` constants et les paramètres rationnels, pour obtenir des tests exacts sans exponentielles. Le théorème général couvre des coefficients variables, sous réserve de leur certification. **Aucun** coefficient original `A_N,A_M,B_N,B_M` de Step58 n'a été calculé ici. `B_M(0)=0` est compatible avec les asymptotiques b3c2 : l'anneau commence strictement après zéro et le raccord central reste à construire. `M(R)=N(R)` est une condition illustrative, non la condition d'horloge Step55. Les sources originales Step45/55/58 et le probe R=17/20 ne sont pas rejoués, DNS Git toujours indisponible. Ne pas convertir cet écran en obstruction physique.

## Exécution locale

`PYTHONPATH=/mnt/data/janus_b3c3d6 python -m numerics.hr_step68ad_b3c3d6_annular_interval_screen` : 10 assertions exactes PASS après correction d'un témoin initial incorrect (pente de M : 1 remplacé par 5/6). `PYTHONPATH=/mnt/data/janus_b3c3d6 python -m unittest discover -s /mnt/data/janus_b3c3d6/tests -p 'test_hr_step68ad_b3c3d6_annular_interval_screen.py' -v` : 4 tests PASS, non indépendants, 0 FAIL final.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Prochaine étape : exécuter le probe Step58 original, certifier `B_N/B_M`, puis écran annulaire sur vrais coefficients et raccord centre ; vraies conditions de bord, générateurs/charges/quotient temporel, Dirac complet, K=0/J=0, 4D/stabilité/observables restent ouverts.

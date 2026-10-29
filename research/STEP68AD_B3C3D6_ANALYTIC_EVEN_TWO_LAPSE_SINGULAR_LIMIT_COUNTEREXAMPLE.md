# JANUS b3c3d6 — contre-exemple analytique pair à DEUX lapses (29/10/2026)

**Statut : théorème exact sur un opérateur JOUET, NON PHYSIQUE. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** L'opérateur temporel original Step58, les cinq sources SHA-authentifiées et le candidat cubique ne sont PAS rejoués dans cette session. Ce résultat ne prouve aucune solution JANUS ni aucune obstruction Dirac.

## Énoncé exact

Fixons `R=17/20`, `k=10371/20000` (strictement dans la bande centrale conditionnelle `1037/2000 < k < 2593/5000` rapportée par b3c2), et tout `epsilon>0`. Considérons l'opérateur scalaire de type Step58, mais **inventé pour ce contre-exemple** :

`T = A_N N + A_M M + B_N N' + B_M M' + E_N N'' + E_M M''`,

avec `A_N=[k/(1-k)] r²`, `A_M=-r²/(1-k)`, `B_N=-epsilon*r^5`, et `B_M=E_N=E_M=0`. Définissons

`N(r)=exp((R²-r²)/(2 epsilon R⁴))`,

`M(r)=N(r)*[k+(1-k)*(r/R)^4]`.

Alors **exactement** `T=0` pour tout `r`, `N,M` sont strictement positifs et analytiques pairs en `r` sur tout l'axe réel, `N'(0)=M'(0)=0`, `M(0)/N(0)=k`, et **les deux vrais bords du jouet** satisfont `N(R)=M(R)=1`. En effet, `N'=-r N/(epsilon R⁴)` et

`A_N N+A_M M=-(r^6/R^4)N`, `B_N N'=(r^6/R^4)N`.

Au bord, `A_N(R)+A_M(R)=-R²=-289/400`, `B_N(R)N'(R)=R²`, `N'(R)=-1/(epsilon R³)=-8000/(4913 epsilon)`. Ainsi `B_N(R)→0` quand `epsilon→0+`, tandis que la pente terminale diverge. Pour `epsilon=0` exactement, l'équation réduite impose `M=kN`, incompatible avec `N(R)=M(R)=u>0` puisque `k<1`.

**Point crucial par rapport au précédent jouet analytique central :** l'analyticité paire des DEUX lapses, même accompagnée du ratio central b3c2 et de l'égalité positive au bord, ne suffit PAS à exclure une couche limite lorsque l'on ne contrôle pas les amplitudes/pentes. La construction précédente à lapse M constant devenait non analytique au centre ; celle-ci est analytique, car M varie. Cela ne contredit pas le résultat précédent : les opérateurs et hypothèses sont différents.

## Budget manquant et limites

L'amplitude centrale nécessaire vaut `N(0)=exp(1/(2 epsilon R²))=exp(200/(289 epsilon))`, donc explose pour `epsilon→0+` sous la normalisation `N(R)=1`. Une borne uniforme `N(0)≤C` avec `C>1` imposerait `epsilon≥200/(289 log C)` **dans ce jouet**. La parité et l'analyticité seules ne fournissent pas cette borne. `B_N=-epsilon*r^5` est impair, donc compatible avec la parité du terme `B_N N'`; les coefficients `A` sont pairs et `E` nuls. Les coefficients Step58 physiques ne sont PAS ceux-ci, et les deux conditions de bord de ce jouet ne sont pas certifiées admissibles pour JANUS.

Le verdict de b3c3d6 reste **PARTIEL**. Avant toute conclusion physique, rejouer les cinq originaux Step45/46/55/58 avec jets cubiques aux rayons `1/4,1/2,7/10,17/20`, comparer six coefficients affine/cubique, factoriser/enclore `B/E` et `A`, puis traiter l'analyticité réelle et les bornes de lapses **sur l'opérateur physique**, les deux vrais bords et enfin Dirac/charges/jauge/six couples/K=0/J=0/4D/stabilité/observables.

## Reproductibilité

`PYTHONPATH=. python -m unittest discover -s tests -v` : **6 unittest SymPy exacts PASS, 0 FAIL**, non indépendants (code et tests dérivent du même témoin). `python -m compileall -q numerics tests` : PASS. Aucune source originale Step45/46/55/58 exécutée dans cette session. Fichiers : `numerics/hr_b3c3d6_analytic_even_two_lapse_boundary_layer.py`, `tests/test_hr_b3c3d6_analytic_even_two_lapse_boundary_layer.py`, cette note. Aucun changement hors branche `research/gate2b-nonhomothetic-transfer`.

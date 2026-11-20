# JANUS-006 — Levée algébrique exacte de l'obstruction Hg par le second jet Sg'' (2026-11-20)

## Provenance et question
HEAD initial `eb2abcb4f6bae7d9fa2ead30750d721df7567432`. Sources lues au HEAD fixé : `numerics/hr_step45_exact_physical_ward.py`, `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py`, `research/JANUS006_HG_QUADRATIC_FIXED_Z_GRAPH_NO_GO_20261120.md`. Le NO-GO précédent imposait Sg'' fixe. Test contradictoire : une variation de ce jet lève-t-elle l'obstruction quadratique de Hg, tout en préservant D et Z ?

## Identité exacte sur la tranche explicitement définie
Posons `p=pLg`, `h=Sgr`, `r=plgr`, `u=Sg2`, `D=psg*h-Lg*r+pg*tgr`, et `q=1+rho*Lg/Lf`. Les paramètres `Lg,Sg,mg,psg,pg,tgr,Lgr,z,q` sont fixés et non singuliers ; `Lg,Sg,mg>0`. On fixe `D=D0` et `z=Z0` en imposant l'équation algébrique de stationnarité correspondante. Les termes de Hg variables sur cette tranche, transcrits de Step45, sont :

```
H = Lg*p**2/(4*mg*Sg**2) - p*psg/(2*mg*Sg)
    + mg*h**2/Lg + 2*mg*Sg*u/Lg
    - 2*mg*Sg*h*Lgr/Lg**2 + z*D/Lg + constant
```

La compensation de bord précédente fixe `c=z*q*Lg/(2*mg*Sg)`. Pour un paramètre t, poser `p(t)=p0+t`, `h(t)=h0+c*t`, `r(t)=r0+(psg*c/Lg)*t`. Alors `D(t)=D(0)` exactement. Définir
```
u(t) = u0 - Lg/(2*mg*Sg) * ( H(p(t),h(t),r(t),u0) - H(p0,h0,r0,u0) )
```
où la différence H exclut les constantes. Par linéarité de H en u, **H(t)=H(0)** pour tout t, exactement, et donc si le point de départ satisfait Hg=0, la famille le satisfait sur cette tranche. Les coefficients de bord ne dépendent pas de Sg2 ; le pullback de la forme de bord sur le graphe reste celui du calcul fixe-Z antérieur, soit `Theta=-V*Lg*dp` sous ses hypothèses (N,M,V et autres jets de bord fixés).

## Jacobien et rang
Dans les coordonnées (p,h,r,u), le jacobien de (D,H) a un mineur sur (r,u) égal à `-2*mg*Sg`, non nul. Il a donc rang 2 pour mg,Sg>0. La direction tangentielle (1,c,psg*c/Lg,du/dt|0) est dans son noyau, avec
```
du/dt|0 = -(Lg**2*p + 2*Lg*Sg*h*mg*q*z - Lg*Sg*psg
            - 2*Lgr*Sg**2*mg*q*z)/(4*Sg**3*mg**2).
```
Ce résultat est plus fort qu'une tangence ponctuelle : il construit un graphe algébrique fini qui maintient Hg et D.

## Reproduction et contrôle indépendant
Exécution Python/SymPy locale : définition de D et H comme ci-dessus, calcul du jacobien, vérification des deux résidus `J*w=0`, déterminant mineur `-2*mg*Sg`, puis substitution de la courbe finie et vérification `simplify(D(t)-D(0))=0`, `simplify(H(t)-H(0))=0`, `simplify(diff(u(t),t).subs(t,0)-du)=0` : tous PASS. La preuve indépendante est la résolution linéaire explicite de Hg=const en Sg2 ; elle ne repose pas sur une approximation numérique. SymPy disponible dans l'environnement d'exécution ; commande conceptuellement reproductible en recopiant les expressions du présent rapport. Aucun moteur physique complet n'a été exécuté.

## Portée critique
Le NO-GO quadratique précédent reste vrai **à Sg2 fixé**, mais ne s'étend pas aux familles où Sg2 peut varier. Cette levée algébrique **ne prouve pas** que Sg2 est libre sur les solutions de l'ODE Step55, ni que Hf=0, C_red=0, Fz=0 et les deux vraies traces de bord sont préservés ; la stationnarité de z exige aussi que D0 soit compatible avec les paramètres d'interaction. La courbe ne constitue donc pas une famille de solutions physiques, ni une preuve de fermeture sur l'espace de Dirac. Il faut maintenant calculer le jacobien conjoint réel et vérifier l'intégrabilité radiale de Sg2.

Tests b3c3d9 SKIP, pilote SKIP, cellules physiques demandées/tentées/évaluées/certifiées/inconclusives durant ce cycle : 0/0/0/0/0.

**NEXT_ACTION_EXACT :** sur Step45, former et réduire `Jacobian([Hg,Hf,Fz,C_exact], [pLg,Sgr,plgr,Sg2, ...])` sur une solution physique candidate, ajouter les deux traces de bord et les conditions d'intégrabilité radiale, puis calculer noyau et rang ; JANUS-001 reste BLOCKED jusqu'à reconstruction authentifiée Step45/46/55/58 et tests/pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

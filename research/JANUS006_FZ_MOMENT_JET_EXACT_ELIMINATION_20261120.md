# JANUS-006 — Élimination exacte de Fz par le jet du moment (2026-11-20)

HEAD source : e7c8842f575dd7730732cfb76ec691dd94cd41e9. Source canonique : numerics/hr_step45_exact_physical_ward.py, exact_physical_ward(). Hypothèses Lg≠0, |z|<1, champs réguliers.

La contrainte exacte Step45 est Fz=psg*Sgr-Lg*plgr+pg*tgr-m2*mg*Lg*Lf*At*z/sqrt(1-z²), At=b1*Sg²+2*b2*Sg*Sf+b3*Sf².

Elle admet **exactement** la résolution :

`plgr=(psg*Sgr+pg*tgr)/Lg-m2*mg*Lf*At*z/sqrt(1-z²)`.

En imposant l'holonomie Sgr=Sg'(r), plgr=pLg'(r), on obtient pour Fz seul une solution par quadrature, pLg(r)=pLg(r0)+int(r0,r) [(psg*Sg'+pg*tgr)/Lg-m2*mg*Lf*At*z/sqrt(1-z²)] dr. Ceci est local et ne démontre aucune autre contrainte ni les bords.

Sur la tranche où z,Lg,Lf,Sf,psg,pg,tgr sont fixés, sigma=delta Sg entraîne exactement au premier ordre :

`delta plgr=(psg/Lg)*sigma' -2*m2*mg*Lf*z*(b1*Sg+b2*Sf)*sigma/sqrt(1-z²)`.

Cela lève **uniquement** l'obstruction Fz obtenue précédemment en fixant simultanément D,z,plgr ; le prix est une variation du moment compatible avec sa dérivée. Si les deux valeurs du moment sont imposées, une contrainte intégrale supplémentaire apparaît ; ce n'est pas une condition Dirichlet physique déjà établie.

## Contrôle réellement exécuté
Python/SymPy : définition de At et de plgr ci-dessus, substitution dans Fz, `assert simplify(Fz)==0` : PASS. `diff(plgr,Sg)` a retourné le coefficient attendu en sigma. Contrôle indépendant : Fz est affine en plgr de coefficient -Lg, et le théorème fondamental du calcul vérifie la quadrature.

## Limites
Pas de test b3c3d9 ni pilote ; cellules demandées/tentées/évaluées/certifiées/inconclusives 0/0/0/0/0. Pas de certification Dirac, Hg,Hf,C_exact, bords ou stabilité. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

NEXT_ACTION_EXACT : substituer plgr éliminé dans Hg,Hf,C_exact canoniques, calculer le jacobien tangent holonome et les deux vraies traces ; en parallèle JANUS-001 reconstruire sources Step45/46/55/58 authentifiées, neuf tests et pilote.

# JANUS-005 — Correction de portée du tangent extérieur : géométrie variable (2026-11-11)

Source authentifiée au HEAD `cc698c3abad3605a88a212e00ec869d251cb94b7` : `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs`, lignes 27–47. Ce code teste explicitement une différentielle **à géométrie fixée** (voir son champ `scope`). Ce rapport n'affirme pas que la géométrie physique varie effectivement dans la famille Step49/55.

## Proposition exacte et contre-contrôle

À rayon R fixé, s=R², den=beta+k*s*U/(2*m*T), numer=U²/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L³*rf/2+s*z*D/L+w, rho=-numer/den, pf=s*rho et pSf=(R*L*V-R*s*D-R*s*k*L*rho)/T. Ici w=Wfbar, D=Dbar, T=Sfr.

Lorsque U,V et tous les coefficients sauf w restent fixés et que den≠0 :

`partial_w pf = -s/den`

`partial_w pSf = R*s*k*L/(T*den)`.

Par conséquent la formule `dpf=H*d(pLf)+chi*d(pLf')` publiée pour la carte **à géométrie fixe** n'est **pas** la dérivée totale d'une famille où w varie indépendamment. La dérivée totale doit ajouter `(-s/den)*dw/dlambda` et, en général, toutes les autres contributions des coefficients géométriques et sources. De même la formule publiée pour `dpSf` ne couvre pas ces variations.

Contrôle contradictoire purement algébrique, **non solution JANUS** : R=1/2, s=1/4, m=L=T=beta=1, k=1/10, U=V=D=rf=z=w=0, et dw/dlambda=1 avec dU=dV=0. Alors d(pLf)=d(pLf')=0, tandis que dpf=-1/4 et dpSf=1/80. L'interprétation de la différentielle à géométrie fixe comme dérivée totale donnerait incorrectement zéro.

## Reproduction exacte

Python 3.13 / SymPy 1.14 : construire les expressions ci-dessus avec `sympy.symbols`; vérifier par `sympy.simplify` les deux identités en w, `diff(pf,U)=s*H`, `diff(pf,V)=s*U/(2*m*T*den)`, puis les deux valeurs rationnelles du contre-exemple. Exécution locale : **5 assertions PASS** (deux identités w, deux identités U/V, un contrôle rationnel double), après correction d'une erreur initiale de facteur s dans le contrôle de pSf. Cette erreur de brouillon a été corrigée avant la conclusion.

**Portée :** ce résultat précise une condition de validité, ne réfute ni la carte Step46 à géométrie fixe ni JANUS. Il n'établit pas que w soit indépendant sur la vraie famille de solutions ; les contraintes peuvent imposer dw/dlambda=0 ou des compensations. Les bornes conditionnelles de H et des traces ne doivent être utilisées comme dérivées totales qu'après preuve des hypothèses de géométrie fixée ou incorporation des termes manquants.

**NEXT_ACTION_EXACT :** inspecter Step45/46/55 pour déterminer quelles variables géométriques sont fixes sous lambda ; établir la chaîne complète d(pf)/dlambda et d(pSf)/dlambda sous contraintes, puis seulement encloser H, den et les quatre traces. JANUS-001 : transfert des sources authentifiées et pilote 1 cellule. Cellules physiques nouvelles évaluées/certifiées : 0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# JANUS-005 — Troisième jet radial après compensation KG+CF (2026-11-15)

HEAD source figé : `68ec334c833618967dc62e652e8cabec03f7b50e`. Provenance : `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, fonction `geometry(s)`, et rapport `research/JANUS005_KG_CF_TWO_RADIAL_JETS_20261115.md` blob `5b867d89055df28e997a2bf610f9f12d109b603c`.

## Question falsifiable
La tangente `dA=1`, `dM2/dA=-(4*A**3*M2*C+0.9)/(A**4*C)`, `dZ1/dA=-Z1/A`, `dCG/dA=-CG/A`, compensée par `dKG/dA` et `dCF/dA` pour annuler les jets `a1,a2`, annule-t-elle aussi `a3=(d³rho_g/ds³)(0)/6` ?

## Exécution et contrôle
Calcul réellement exécuté dans Python 3, mpmath 1.3.0, `mp.dps=45`, par transcription littérale de `geometry(s)` : `Lg=A*(1+CG*s)**2`, `Lf=A*Y*(1+CF*s)**2`, `T0=b0*Lg**2+2*b1*Lg*Lf+b2*Lf**2`, `T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2`, `Dbar=M2*Lg*Lf*T*Z1/sqrt(1-Z1**2*s)`, `Wgbar=M2*(Lg*T0+Lf*T*sqrt(1-Z1**2*s))`, `Rg=-48*CG/(A**2*(1+CG*s)**5)`, `Gmom=PG*(1+2.5*CG*s)`, `Gprime=2*PG*(1+5*CG*s)`, `Sgr=A*(1+CG*s)*(1+5*CG*s)`, `fac=Gmom/(2*Lg*Sgr)`, `betag=sqrt(1+KG**2*s)+s*fac*KG*Lg`, `rho_g=-(Gmom**2/(4*Lg)-fac*(s*Dbar+Lg*Gprime)-Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag`. `PG=-2*A**2*sqrt(0.9/(3*A**3)+M2*C/3)` **est évalué au point de base et maintenu constant dans les variations**, conformément à la tangente centrale.

Paramètres : `A=.4, M2=23.3348939346, Z1=.004, CG=.0015, KG=.0012, CF=-.0012, Y=.5787707228025044, MF=.10879548725**2, (b0,b1,b2,b3,b4)=(0,1,-4.2383993109,13.6801214252,-38.5117901844)`. `C=b0+3*b1*Y+3*b2*Y**2+b3*Y**3`.

Procédure exacte : `jet(n,p)=mp.diff(lambda s:rho_g(s,*p),0,n)/mp.factorial(n)`. Former le jacobien 3x6 de `jet(n,p)` (`n=1,2,3`) par `mp.diff` selon `p=(A,M2,Z1,CG,KG,CF)`. Résoudre le sous-système 2x2 pour `(dKG,dCF)` en annulant les deux premières lignes, puis évaluer la troisième. Contrôle indépendant par différence finie centrée de `jet(3,p+h*d)`.

## Résultats
- `dKG/dA=+0.0755874817043977411888280492553`
- `dCF/dA=-0.00636344858203444131023741494235`
- Résidus directionnels a1 et a2 : respectivement `-1.3246e-48` et `2.4451e-51` (zéros numériques, pas des identités symboliques).
- **Résidu du troisième jet : `D a3=+0.000010685985596652940205640797930702548` (non nul).**
- Différence finie centrée h=1e-4 : `+0.000010685994447768693859909036270931253`.
- Différence finie centrée h=1e-6 : `+0.000010685985597538051474329497895878079`.
- La convergence en O(h²) confirme la valeur analytique au niveau numérique.

## Verdict et portée
**NO-GO circonscrit** : la tangente à six paramètres qui conserve les données centrales et les deux premiers jets ne conserve PAS le troisième jet de densité. Cela ne prouve ni que le troisième jet est une donnée physique imposée, ni qu'aucun autre paramètre/champ ne peut compenser, ni l'échec de JANUS. Calcul ponctuel différentiel, **aucune cellule physique Step55/58 évaluée ou certifiée (0/0/0)**. Tests moteur b3c3d9 : SKIP. Script temporaire exécuté dans l'environnement de session mais pas archivé ; ce rapport donne les formules et la procédure de reconstruction, pas une reproduction octet pour octet.

**NEXT_ACTION_EXACT :** (1) reconstruire et archiver un script de reproduction complet à partir des formules ci-dessus ; (2) examiner si le troisième jet est contraint par Step45/46, Dirac et les deux vrais bords ; (3) JANUS-001 transférer les dépendances authentifiées et lancer neuf tests et pilote physique.

**GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

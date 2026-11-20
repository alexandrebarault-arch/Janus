# JANUS-006 — Non-fermeture ambiante de la forme de bord au témoin algébrique (20 novembre 2026)

Source GitHub au HEAD `60f91c634b77c8724350a6e80514821f1daaf103` : `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py`, plus le témoin conditionnel `research/JANUS006_ON_SHELL_ALTERNATIVE_MINOR_WITNESS_20261120.md`. Le module original n'a pas été exécuté localement : vérification indépendante de ses expressions par SymPy 1.14.0.

À configuration canonique et lapses fixés, `Theta=dC-Z*dP`, `P=a*pLg`, `a=N+M*Lg/Lf`, `Z=D/sqrt(D**2+K**2)`, `D=psg*Sgr-Lg*plgr+pg*tgr`. Dans les deux directions **ambiantes** indépendantes (pLg,plgr), le coefficient de `dTheta=dP wedge dZ` est exactement

`W=-a*Lg*K**2/(D**2+K**2)**(3/2)`.

Au témoin algébrique précédent satisfaisant conditionnellement `Hg=Hf=Fz=C_exact=0`, avec `Lg=Lf=1, Sf=3, z=0, K=16, D=0`, choisir `N=M=1` donne `a=2` et `W=-1/8 != 0`. Les lapses positifs choisis ne sont pas certifiés par leur préservation temporelle.

**Contrôles exécutés** : Python/SymPy 1.14.0, dérivation symbolique `diff(P,p)*diff(Z,pr)-diff(P,pr)*diff(Z,p)`, assertion d'identité symbolique PASS, substitution rationnelle `-1/8` PASS. Contrôle indépendant : `partial_pr D=-Lg`, `partial_D Z=K²/(D²+K²)^(3/2)`, `partial_p P=a`.

**Portée critique** : les deux directions utilisées ne sont pas démontrées tangentes à la surface des quatre contraintes ; `Fz=0` relie D et z. La non-fermeture **ambiante** au point ne prouve aucune non-fermeture après réduction de Dirac ou application des deux véritables conditions de bord. Le témoin sur quatre contraintes reste conditionnel à la transcription non authentifiée de Step45. Aucun NO-GO physique.

JANUS-001 tests et pilote SKIP ; cellules demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0.

**NEXT_ACTION_EXACT** : calculer le pullback de `dTheta` sur le noyau conjoint de `dHg,dHf,dFz,dC_exact`, puis imposer l'intégrabilité radiale et les deux traces de bord. En parallèle transférer les octets authentifiés Step45/46/55/58, vérifier les SHA Git, exécuter les neuf tests et le pilote. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

# JANUS-006 — courbe exacte d'annulation du mineur conditionnel (20 novembre 2026)

## Provenance et portée

HEAD de départ `97a30fbe0331bfe5e446b3cbb02bd252dcd003bd`. Le facteur `P` est celui du rapport JANUS006_C_EXACT_MOMENT_DERIVATIVE_20261120.md, dérivé d'une transcription locale Step45 **non rejouée depuis les octets originaux**. Ce travail est une identité algébrique **conditionnelle**, pas une solution des contraintes physiques ni un certificat de rang Dirac.

## Hypothèses et démonstration

Sur la famille positive `Lg=Lf=Sg=beta1=beta2=beta3=m2=Mg2=Mf2=1`, `Sf=x>0`, `|z|<1`, poser `r=sqrt(1-z²)>0`. Alors

`P=2(x+1)+r(1-x²)=(x+1)[2+r(1-x)]`.

Puisque `x+1>0`, l'annulation équivaut **exactement** à

`x=1+2/sqrt(1-z²)`.

Elle est donc possible pour tout `|z|<1`, avec `x>=3`, et impossible sur cette famille lorsque `0<x<3`. La courbe est lisse à l'intérieur du domaine ; `dP/dx=-r(x+1)<0` sur la courbe. L'interaction `At=1+2x+x²=(x+1)²>0` et `K=At>0` partout. Pour `z=0`, `x=3`; pour `z=3/5`, `x=7/2`. Lorsque `|z|→1`, `x→+infinity`, ce qui n'autorise pas une solution finie au bord `|z|=1`.

## Contrôle indépendant

Développement direct : `(x+1)(2+r-r*x)=2x+2+r-r*x²`, égal au P initial. En substituant `x=1+2/r`, `2+r(1-x)=0` exactement. La dérivée `2-2rx` devient `-2(r+1)`, égale à `-r(x+1)`. SymPy 1.14.0 : factorisation et résolution symbolique PASS ; contrôle manuel indépendant PASS.

## Limites et action suivante

Le résultat établit une **famille continue d'annulations d'un mineur choisi**, pas une perte de rang complet. Ni `Hg=Hf=Fz=C_exact=0`, ni l'intégrabilité des jets, ni les deux vrais bords ne sont imposés. Le Step45 source est lisible sur GitHub au blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, mais la transcription utilisée pour P n'a pas été authentifiée octet pour octet. Aucun test du moteur b3c3d9 ni cellule physique exécutée ici.

**NEXT_ACTION_EXACT :** rejouer `python -c "from numerics.hr_step45_exact_physical_ward import exact_physical_ward; import sympy as s; p=exact_physical_ward(); print(s.factor(s.diff(p['C_exact'],p['q'][1])))"` depuis un module Step45 aux octets vérifiés ; confronter la courbe aux quatre contraintes et aux autres mineurs, puis imposer l'intégrabilité et les deux vrais bords. JANUS-001 : reconstruire Step45/46/55/58 authentiques, exécuter neuf tests et pilote.

**GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

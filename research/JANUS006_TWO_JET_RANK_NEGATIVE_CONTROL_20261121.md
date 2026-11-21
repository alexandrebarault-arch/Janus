# JANUS-006 — contre-contrôle de rang du prolongement shift (2026-11-21)

## Objet et provenance
HEAD de départ `a4f3c5f98c8cef886b0ed4b3dc0357c9b6a47364`. À partir des identités déjà publiées dans `JANUS006_SHIFT_CONSTRAINT_PROLONGATION_20261121.md` et `JANUS006_SHIFT_SECOND_JET_COMPATIBILITY_20261121.md`, examiner si les deux coefficients non nuls devant z'' impliquent à eux seuls une contradiction. Ceci est une **analyse algébrique de rang conditionnelle**, non un calcul de Dirac.

Écrire `R=a*z''+Q`, avec `a=-4*Sg²*Mg2*q/(Lg*(1+q²*z²))`, et `Fz''=D''-K''f-2K'z'f'-Kf''(z')²-Kf'z''`, `f=z/sqrt(1-z²)`. Dans ce contrôle seulement, `Q` est indépendant de `z''` et de `D''` ; il faut **vérifier cette dernière indépendance après transcription complète des jets Step45**. Les coefficients `K,K',K''` sont ici traités comme données indépendantes de `D''` et de `z''`.

## Résultat exact
Le jacobien des deux équations `(R,Fz'')` par rapport à `(z'',D'')` est `[[a,0],[-K/(1-z²)^(3/2),1]]`, donc son déterminant vaut exactement `a`. Sur le domaine régulier `a!=0`, ce système est localement résoluble, **y compris pour K=0** :

`z''=-Q/a`

`D''=K''f+2K'z'f'+Kf''(z')²-Kf'Q/a`.

Ainsi, si `D''` demeure un jet libre, **les deux prolongements ne produisent aucune obstruction algébrique**. L'élimination de z'' produit une condition sur D'', pas une contradiction. Cela corrige la tentation d'interpréter deux prescriptions non nulles de z'' comme incompatibles sans réduction de l'espace des jets. Sur K=0, la première équation fixe encore z'' et la seconde peut fixer D'' ; ne pas diviser par K.

## Contrôle indépendant
Le déterminant se vérifie directement par expansion `a*1-0*(-K f')=a`. La substitution des deux expressions dans les deux équations donne zéro par distributivité. Le contrôle de dérivation symbolique de f et de Fz'' figure dans le rapport antérieur ; **aucun test moteur physique ni vérification de dépendance effective de Q et D'' sur Step45 complet n'a été réalisé ici**.

## Limites et prochaine expérience falsifiable
Ce rang 2 est celui d'un système **élargi** en deux jets formellement indépendants, non le rang sur l'espace holonome/Dirac. Si `D''` est lié à z'' ou fixé par les contraintes dynamiques, le déterminant ci-dessus ne s'applique pas après réduction. Prochaine action : développer D'' depuis `D=pSg*Sgr-Lg*pLgr+pg*tgr`, identifier tous les jets d'ordre supérieur, substituer les relations d'évolution/Dirac et calculer le rang réduit ; imposer ensuite les deux vraies traces de bord. Ne pas annoncer de NO-GO.

JANUS-001 : tests SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# JANUS-006 — audit holonome du jet D'' (2026-11-21)

HEAD source fixé : `98659896420c566b550ac5117b648ce83872d136`. Source originale `numerics/hr_step45_exact_physical_ward.py` lue via GitHub : `Dg=psg*Sgr-Lg*plgr+pg*tgr`. Calcul local SymPy de dérivée radiale seconde, sans import du module original ; **contrôle cinématique uniquement**.

En notant prime la dérivée totale radiale et D=pSg Sg'−Lg pLg'+pg tg', la règle de Leibniz donne exactement :

```
D'' = pSg*Sg''' + 2*pSg'*Sg'' + pSg''*Sg'
    - Lg*pLg''' - 2*Lg'*pLg'' - Lg''*pLg'
    + pg*tg''' + 2*pg'*tg'' + pg''*tg'.
```

Le coefficient de `pLg'''` vaut `-Lg`, non nul si Lg>0. **Ainsi le jet formel D'' n'est pas une coordonnée canonique indépendante après imposition de la définition holonome : il contient un troisième jet de pLg.** Toutefois, à jets restants prescrits et Lg>0, cette relation permet encore de résoudre pour pLg''' ; elle ne crée donc aucune contradiction algébrique avec R=0 et Fz''=0 sans équations supplémentaires de dynamique/Dirac ou traces de bord.

Contrôles : `python` + SymPy, construction de six fonctions symboliques u,S,L,v,w,t et commande `expand(diff(u(r)*diff(S(r),r)-L(r)*diff(v(r),r)+w(r)*diff(t(r),r),r,2))` : PASS ; coefficient `diff(diff(D,r,2),diff(v(r),r,3))=-L(r)` : PASS. Contrôle indépendant : application manuelle de (fg')''=f''g'+2f'g''+fg'''. Aucun module physique Step45 importé, aucune évolution canonique résolue, aucune donnée aux deux bords testée.

**Prochaine falsification :** extraire les équations Hamiltoniennes des six paires depuis la source authentique et déterminer si elles fixent pLg''' ou relient ce jet à z'' ; réduire alors le rang de (R,Fz'') sur l'espace des solutions de Dirac, puis tester les deux véritables traces. Ne pas traiter le rang artificiellement libre de (z'',D'') comme un rang physique.

JANUS-001 : neuf tests SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

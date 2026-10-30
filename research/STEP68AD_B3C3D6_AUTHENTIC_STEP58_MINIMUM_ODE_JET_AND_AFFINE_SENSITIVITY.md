# b3c3d6 — ordre minimal des jets Step55 dans les six coefficients Step58 originaux (30/10/2026)

**Résultat structurel EXACT sur l'opérateur Step58 ORIGINAL ; pas de rejeu numérique physique aux quatre rayons. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources authentifiées et exécution

À la reprise, HEAD de recherche `8f034d6dd01cab94bdcb24634115eb864a11fa27`, `00_CURRENT_RESTART.md` et `research/AUTOMATION_STATE.json` lus directement via le connecteur GitHub. Les octets des modules **originaux exécutés localement** ont été comparés aux SHA de blobs Git : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. L'import Step57 a été remplacé localement par un **shim minimal** ne faisant que retourner `exact_physical_ward()` ; le Step57 complet n'a pas été exécuté. Le moteur Step58 ORIGINAL a réellement construit `physical_operator()` et les six expressions `operator['N'/'M'][0/1/2]`.

**6 tests unittest exécutés PASS, 0 FAIL**, `python -m compileall -q numerics tests` PASS dans l'environnement local minimal. Ils ne sont pas indépendants des deux moteurs symboliques et ne prouvent aucun coefficient numérique physique.

## Résultat 1 — dépendance exacte des six coefficients

Pour les trois champs canoniques dépendant de `U` ou `U_s` sur la famille Step55 prescrite, les indices ci-dessous sont les **ordres de dérivation radiale présents réellement** dans chaque expression originale :

| Coefficient | pLf | pSf | pf |
|---|---|---|---|
| A_N = N0 | 0 | 0 | aucun |
| B_N = N1 | 0 | 0 | aucun |
| E_N = N2 | aucun | aucun | aucun |
| A_M = M0 | 0,1 | 0,1 | 0 |
| B_M = M1 | 0 | 0 | aucun |
| E_M = M2 | aucun | aucun | aucun |

Aucun des six coefficients ne dépend d'un **jet radial d'ordre 2 ou 3** de `pLf,pSf,pf`, ni d'un jet canonique d'ordre 4. L'opérateur original dépend néanmoins réellement des jets d'ordre 3 d'autres champs **indépendants de U** sur cette famille, notamment `Sg'''` dans A_N et `pLg'''` dans A_M. Il serait faux d'affirmer que Step58 est globalement du premier ordre.

## Résultat 2 — la courbure U_ss compte, mais pas U_sss ni U_ssss

Dans la construction prescrite Step55, `pLf=r²U`, `pLf'=2rU+2r³U_s` ; `pf` et `pSf` dépendent algébriquement de `U,U_s` et des champs géométriques prescrits. Ainsi `pSf'` dépend de `U_ss`, et c'est **le seul** jet dépendant de U d'ordre supérieur à 1 en s susceptible d'entrer dans les six coefficients. Un prolongement **quadratique en s** ayant les mêmes `U,U_s,U_ss` suffit donc pour les valeurs ponctuelles des six coefficients Step58 originaux ; cubique et quartique donnent les **mêmes six coefficients exacts** au même point et sur la même coquille, sous le contrat de champs du candidat. Le quatrième jet, utile au défaut holonome hors point, n'est pas requis pour cette évaluation ponctuelle.

L'opérateur original donne, avec `Czr=∂C/∂zr` et `K` l'interaction positive,
`∂A_M/∂pSf' = z(1-z²) Czr/(2 Lf Mf2 Sf)`.
Identité exacte `Czr=-(K sqrt(1-z²)+z Dg)/(Lg Lf)`. Sur `Fz=0`, `Dg=K z/sqrt(1-z²)`, donc
`∂A_M/∂pSf' = -z sqrt(1-z²) K/(2 Lg Lf² Mf2 Sf)`.
Pour `beta=sqrt(1+tfr²/Lf²)`, `den=beta+fac*tfr` et `Sfr=dSf/dr`, le champ `pSf` du candidat vérifie
`∂pSf'/∂U_ss=4r⁴ Lf beta/(Sfr den)`.
D'où l'identité **exacte conditionnelle sur cette famille** :

```
∂A_M/∂U_ss = -2 r⁴ z sqrt(1-z²) K beta /
              (Lg Lf Mf2 Sf Sfr (beta+fac*tfr)).
```

Pour `0<z<1`, `K>0` et dénominateurs strictement positifs, ce coefficient est strictement négatif. La différence `A_M(quadratique)-A_M(affine)` est ce facteur multiplié par `U_ss` si les prolongements ont les mêmes `U,U_s` au point. Les cinq autres coefficients restent égaux. Ce résultat **réfute la justification générique de l'affine** et **écarte le besoin d'un quartique pour les six valeurs ponctuelles**, sans calculer leur amplitude physique.

## Limites et priorité

Aucune intégration DOP853 originale Step55 ni aucun rejeu affine/quadratique/cubique Step58 aux rayons `1/4,1/2,7/10,17/20` pendant cette session ; aucun défaut continu, erreur initiale, six coefficients numériques, factorisation/enclosure uniforme, BVP positif à deux bords, Dirac, 4D, stabilité ou observables certifiés. Les originaux Step46/55 ne sont pas exécutés ici. Le prochain vrai test doit comparer **affine vs quadratique vs cubique** aux quatre rayons, et vérifier numériquement que seul `A_M` change entre affine et quadratique ; ce contrôle est plus ciblé qu'un quartique de routine. Une divergence serait un signal d'erreur dans la substitution des champs, des jets ou des sources.

Livrables : `numerics/hr_b3c3d6_original_step58_minimum_jet.py` ; `tests/test_hr_b3c3d6_original_step58_minimum_jet.py`. Résultat scientifique **partiel**, aucune validation de JANUS.

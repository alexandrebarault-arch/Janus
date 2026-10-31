# JANUS b3c3d6 — audit exact des deux branches secondaires locales Step58 (31 octobre 2026)

**Verdict : progrès algébrique ponctuel, non physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et exécution

Les octets originaux Git Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f` ont été reconstruits, SHA-authentifiés et exécutés avec un shim **minimal** de Step57 (le moteur Step57 complet n'a pas été exécuté). L'exécution locale utilise SymPy et des fractions exactes ; aucun DOP853 physique ni Step55 n'a été rejoué.

## Famille exacte à deux paramètres, coefficients temporels complets

On reprend la tranche de jets locaux du certificat précédent : `Lg=Lf=Sg=Sf=Mg2=Mf2=m2=1`, `K=1`, `z=3/5`, `pg=7/4>0`, `pf=1>0`, potentiels `beta0=-5,beta1=1,beta2=beta3=0,beta4=-2`, et jets gelés selon le module exécutable. Deux paramètres libres : `a=z_r`, `b=Sf_r`. Après résolution de `Fz=Hg=Fz_r=Hg_r=0` :

- `C=-(25a+24b+12)/20`, `Hf=b²-1`, `B_N=3C/5` et `B_M=E_N=E_M=0` ;
- `A_N=(1200ab-3775a-2048b²+2952b+4408)/1000` ;
- `A_M=(625a²-9600ab+3600a+2400b²-4704b-22336)/4000`.

Les deux équations supplémentaires `Hf=C=0` fixent **exactement deux points** de cette tranche :

| `(a,b)` | `A_N` | `A_M` | `-A_N/A_M` | Lapses `N,M>0` dans l'équation ponctuelle `A_N N+A_M M=0` |
| --- | ---: | ---: | ---: | --- |
| `(-36/25,1)` | `451/50` | `-919/250` | `2255/919` | **Compatibles ponctuellement** avec `M/N=2255/919` |
| `(12/25,-1)` | `-149/50` | `-547/250` | `-745/547` | **Incompatibles ponctuellement** : deux coefficients négatifs |

La distinction est rigoureuse **uniquement pour les jets gelés de cette tranche**. Elle n'est ni un rang Dirac ni un BVP.

## Contrôle négatif décisif : la tranche n'est pas holonome

Les dérivées radiales supplémentaires, calculées avec le **même opérateur original** et les jets d'ordre supérieur gelés du certificat, ne s'annulent **sur aucune des deux branches** :

| `(a,b)` | `Fz_{rr}` | `Hf_r` | `C_r` |
| --- | ---: | ---: | ---: |
| `(-36/25,1)` | `65/64` | `-51/16` | `349/100` |
| `(12/25,-1)` | `-191/64` | `113/16` | `-59/100` |

**Conclusion négative essentielle :** les deux témoins ne sont PAS des profils radiaux satisfaisant toutes les contraintes fonctionnelles. Le gel des jets supérieurs viole déjà les conséquences différentielles de `Fz=Hf=C=0`. Il serait scientifiquement incorrect de transférer leurs signes de lapses au vrai Step55, ou de les présenter comme un contre-exemple à JANUS. Des jets supérieurs réajustés pourraient changer les coefficients ; cette possibilité n'est pas examinée ici.

## Tests et artefacts

Commande exécutée : `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_two_branch_secondary_lapse.py' -v` : **10 PASS, 0 FAIL, 0 SKIP** après correction d'un premier échec de comparaison structurelle `(b-1)(b+1)` versus `b²-1`. `python -m compileall -q numerics tests` : **PASS**. CLI `python -m numerics.hr_b3c3d6_step58_two_branch_secondary_lapse` : **PASS**.

Fichiers : `numerics/hr_b3c3d6_step58_two_branch_secondary_lapse.py`, `tests/test_hr_b3c3d6_step58_two_branch_secondary_lapse.py`, `research/reports/gate2b-b3c3d6-Step58-two-branch-secondary-lapse.json`. SHA Git blobs des octets exécutés : source `5779c731313055f34a9b70a02f1767f24cd703bb`, tests `197f050d3ae93d4f92aba12c044ee2c343330295`, rapport `64b392d64167d6db95644764bb0497848924af6b`. Ces blobs doivent être relus après publication.

## Verrous inchangés et prochaine étape

Prouver ou réfuter universellement le résidu inférieur `B_N-zC/Lg-beta*Hg_r` sur la coquille **complète** `Fz=Fz_r=Hg=Hg_r=0`, en conservant les conséquences radiales nécessaires ; certifier les six coefficients `A_N,A_M,B_N,B_M,E_N,E_M` du vrai Step55 aux rayons `1/4,1/2,7/10,17/20` (DOP853 rigoureux si nécessaire), puis le BVP de deux lapses strictement positifs aux vrais bords, Dirac, 4D, stabilité et observables. **Aucune de ces étapes n'est close.**

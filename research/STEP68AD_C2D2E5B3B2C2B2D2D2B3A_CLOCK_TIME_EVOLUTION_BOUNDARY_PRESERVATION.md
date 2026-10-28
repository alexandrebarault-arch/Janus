# JANUS — 68ad-C2d2e5b3b2c2b2d2d2b3a : évolution temporelle des horloges et préservation des bords

28 octobre 2026. **Théorème exact conditionnel sur les signes Step55 ; générateurs temporels améliorés et quotient Dirac NON calculés. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Dérivation physique

Depuis les termes de poussière originaux Step37 et le shift diagonal ADM, avec `Q=N/Lg+M/Lf`, `sg=sqrt(1+(tg'/Lg)^2)`, `sf=sqrt(1+(tf'/Lf)^2)`, la stationnarité du shift relatif `F_z=0` autorise le théorème de l'enveloppe :

```
dot(tg)=ug=N*sg+(z*Q+V)*tg'
dot(tf)=uf=M*sf+V*tf'
Jg=pg*[N*tg'/(Lg^2*sg)+z*Q+V]
Jf=pf*[M*tf'/(Lf^2*sf)+V].
```

Les équations canoniques à support compact donnent `dot(pg)=d_r(Jg)` et `dot(pf)=d_r(Jf)`. Sur un domaine où les traces et l'évolution sont définies, l'intégration formelle donne `dot(Qi)=Ji(R)-Ji(0)`, `Qi=integral pi dr`. **Cela ne prouve ni différentiabilité du générateur complet, ni conservation des charges.** La translation constante laisse la densité inchangée mais les arguments canoniques exigent les contributions de bord appropriées.

## Deux conditions Dirichlet temporellement constantes sont incompatibles

Sur Step55, à `R=17/20`, `tg'>0`, `tf'<0`, `z>0`, `Lg,Lf,N,M>0`. Si `uf=0`, `V=-M*sf/tf'>0` et `ug>0`. Si `ug=0`, `V=-zQ-N*sg/tg'<0` et `uf>0`. Donc **aucun shift diagonal fini ne peut maintenir les deux horloges immobiles au bord extérieur**, dans ce secteur et avec ces lapses. Cela complète, sans s'y substituer, le théorème de flux nus b2.

Au centre régulier Step55, `tg'(0)=tf'(0)=0` ; pour multiplicateurs finis, `dot(tg)(0)=N(0)` et `dot(tf)(0)=M(0)`. Des valeurs individuelles fixées **constantes dans le temps** au centre imposent donc un lapse nul, incompatibles avec des lapses strictement positifs au centre. Des données de bord évoluant dans le temps restent possibles. Le rang cinématique des translations calculé en b2 ne certifiait pas la préservation temporelle.

## Condition relative et séparation d'avec le flux nu

Une condition `tg(R)-tf(R)=constante dans le temps` impose `ug=uf`. Puisque `tg'-tf'>0`, elle fixe instantanément un shift unique :

```
Vrel=(M*sf-N*sg-z*Q*tg')/(tg'-tf')
ucommon=[(-tf')*(N*sg+z*Q*tg')+tg'*M*sf]/(tg'-tf')>0.
```

La compatibilité avec les équations de lapses et les contraintes temporelles reste à vérifier. **Préserver la différence des horloges n'implique pas annuler le flux nu sur la variation diagonale.**

Témoin rationnel exact **non Step55** : `Lg=Lf=N=M=1`, `tg'=3/4`, `tf'=-5/12`, `z=1/5`, `pg=2`, `pf=3`, `sg=5/4`, `sf=13/12`. Alors `Vrel=-2/5`, `ucommon=5/4`, tandis que le shift annulant `Jg+Jf` est `Vflux=-11/65` et `(Jg+Jf)|Vrel=-15/13`. C'est un contre-exemple algébrique, pas une solution physique.

## Provenance, tests et limites

Sources originales SHA-authentifiées : Step37 `005449ade6e3582e3b9a5c3374a881a77e73e3f6`, Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, forme non-IBP d2a `94bd7e089ebb0978569361c03a4f3ab950b950df`. Moteurs physiques Python originaux **non réexécutés**. Les assertions BigInt testent les données rationnelles et le témoin ; les inégalités générales sont démontrées par signes dans le présent audit, et non par échantillonnage.

**Non prouvé :** Hamiltonien amélioré fonctionnellement différentiable, statut physique des charges, quotient de jauge temporelle, préservation globale des conditions relatives, lapses temporels, rang/tertiaires Dirac six couples, K=0/J=0, 4D, stabilité, observables.

**Prochaine étape : 68ad-C2d2e5b3b2c2b2d2d2b3b** — confronter le shift `Vrel` au véritable opérateur temporel Step58 et aux conditions de régularité, puis construire les générateurs améliorés et leurs charges sur un domaine différentiable.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

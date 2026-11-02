# JANUS — b3c3d6 : compatibilité exacte des deux bords pour les lapses après réduction Step58 (02/11/2026)

**Statut scientifique : progrès exact conditionnel + contre-modèle construit ; AUCUNE validation physique globale. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Source de vérité et données héritées

HEAD GitHub vérifié à l'entrée : `f3d7422eb6ba36c47a9dc161b6f7c0861e2fffbd`, branche `research/gate2b-nonhomothetic-transfer`.

Les **quatre boîtes Step58 physiques précédemment certifiées** de `A_N,A_M` sont reprises du rapport `research/reports/gate2b-b3c3d6-step58-physical-ANAM-four-radii-sign.json`, objet Git `c502b9779056e8a493c43d330696515a661128c4`. Elles sont **des hypothèses archivée de cette déduction**, et **n'ont pas été recalculées avec Step45/55/58 durant la présente session**.

À chaque rayon, si `0<a_lo<A_N<a_hi` et `m_lo<A_M<m_hi<0`, alors la condition algebraïque sur coquille impose le rapport
```
 rho=M/N=-A_N/A_M ;  a_lo/(-m_lo) < rho < a_hi/(-m_hi).
```

Les quatre encadrements rationnels **stricts et exacts**, issus d'une simple opération monotone sur les boîtes antérieures, sont :

| Rayon exact | Borne basse strictement franchie | Borne haute stricte |
| --- | --- | --- |
| 1/4 | 107/215 | 223/413 |
| 1/2 | 847/1697 | 883/1634 |
| 7/10 | 1639/3279 | 1709/3157 |
| 17/20 | 2385/4768 | 2489/4588 |

En particulier, au **vrai bord extérieur** `R=17/20` :
```
1/2 < 2385/4768 < M(R)/N(R) < 2489/4588 < 11/20.
```
Cela est plus informatif que l'incompatibilité précédemment montrée avec `M(R)=N(R)>0`. Aucune de ces bornes n'est un intervalle démontré sur le *continuum* entre les quatre points.

## Lemme nécessaire/suffisant pour UNE équation de préservation algébrique

Supposons `0<=r<=R` et des coefficients temporels sur la coquille complète `B_N=B_M=E_N=E_M=0`, de sorte que l'unique équation étudiée soit
```
A_N(r) N(r) + A_M(r) M(r) = 0.
```
Si `A_M != 0` pour `r>0` et si `rho(r)=-A_N(r)/A_M(r)` admet un prolongement **strictement positif et C^k** sur l'intervalle fermé, alors, pour quatre amplitudes Dirichlet **positives** `N(0),M(0),N(R),M(R)`, il existe un couple de lapses strictement positifs `C^k` satisfaisant CETTE SEULE équation et ces deux bords **si et seulement si**
```
M(0)/N(0)=rho(0)  et  M(R)/N(R)=rho(R).
```
**Preuve :** la nécessité résulte de la division par `A_M` pour `r>0` puis par continuité au centre. Pour la suffisance, prendre `N>0` comme interpolation `C^k` des deux valeurs et `M=rho N`. Si `rho` est fonction analytique paire de `r`, prendre `N(r)=N(0)+(N(R)-N(0))(r/R)^2`, qui reste strictement positif et analytique pair. Il s'agit de la **seule équation algébrique**, NON de toutes les secondaires Dirac, des équations d'évolution, des charges/flux ou des conditions temporelles de bord.

Conséquence méthodologique : une fois les quatre coefficients de jets de lapses annulés **exactement** sur la coquille, l'équation seule n'est plus une EDO de shooting à deux lapses : elle fixe `M/N` là où `A_M != 0`. Les autres contraintes peuvent bien sûr rétablir des restrictions fonctionnelles.

## Contre-modèle analytique exact, EXPLICITEMENT NON PHYSIQUE

Pour exclure toute inférence abusive « quatre boîtes + ratio central ⇒ impossibilité de tous les lapses positifs », définir avec `s=r²`
```
A_N^toy(r)=s(3500-175s),   A_M^toy(r)=-s(6750-375s),
N^toy(r)=1,  M^toy(r)=(3500-175s)/(6750-375s),  B_i^toy=E_i^toy=0.
```
Tous ces champs sont analytiques et pairs au centre, `N,M>0` sur `[0,17/20]`. L'égalité `A_N^toy N^toy + A_M^toy M^toy=0` est **exacte pour tout r**. Son rapport central `14/27` vérifie la borne centrale historique `1037/2000<M(0)/N(0)<2593/5000`. **À chacun des quatre rayons, les coefficients toy entrent strictement dans LES VRAIES BOÎTES PUBLIÉES de Step58**. On a `d(M/N)/ds=131250/(6750-375s)^2>0` ; les deux bords, avec amplitudes positives `N(0)=N(R)=1`, `M(0)=14/27` et `M(R)=rho(R)>0`, sont satisfaits.

Cet exemple montre UNIQUEMENT que ces informations ponctuelles ne peuvent, **à elles seules**, exclure tous les cas de lapses positifs avec ratio extérieur libre. Les coefficients toy NE SONT PAS ceux de Step58 physique entre les points, et aucune condition Dirac, de poussière, de flux, de charge, ni aucune dynamique 4D ne leur est attribuée.

## Reproductibilité exacte

- `numerics/hr_b3c3d6_lapse_boundary_compatibility.py`, objet Git `b41cbadc7d5a144d4f98b09da57ffa6d99c188da`.
- `tests/test_hr_b3c3d6_lapse_boundary_compatibility.py`, objet Git `9c7ef57a26258b70126223c2bca61f9a10301b14`.
- Commande `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_lapse_boundary_compatibility.py' -v` : **8 PASS, 0 FAIL**.
- Commande `PYTHONPATH=. python -m numerics.hr_b3c3d6_lapse_boundary_compatibility` : **PASS** avec quatre bornes rationnelles exactes.
- `python -m compileall -q numerics tests` : **PASS**.
- Les octets envoyés par GitHub `create_blob` ont été contrôlés contre leur **empreinte d'objet Git** calculée localement, pas contre un SHA1 de fichier nu.
- Les moteurs physiques originaux et la barrière Step55 256 cellules : **NON REJOUÉS DANS CETTE SESSION**.

## Reste à faire

Étudier la **vraie fonction** `rho_physical(r)=-A_N(r)/A_M(r)` avec des bornes continues, y compris `r→0` et les possibles zéros de `A_M`, puis vérifier l'admissibilité **physique** des deux véritables bords temporels et les équations Dirac restantes. Renforcer si nécessaire les 24 boîtes `A/B/E` indépendantes aux quatre rayons. Ensuite : six couples, rang, charges et jauges, `K=0`, `J=0`, 4D, stabilité et observables.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

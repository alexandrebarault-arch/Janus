# JANUS — Étape 68s : certificat temporel original continu jusqu'à r = 1/32

**25 octobre 2026 — branche unique : `research/gate2b-nonhomothetic-transfer`. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Nouveau résultat rigoureux

Les deux certificats précédents ont prouvé (A_N>0,A_M<0) sur `r∈[1/16,17/20]`. Le même moteur **original six-pair Step58**, avec les huit fournisseurs physiques historiques byte-authentifiés, arithmétique orientée originale Step55, et le tube certifié `|U-Ustar|<=1e-6`, a maintenant été exécuté sur **toute la bande fermée** `r∈[1/32,1/16]`.

**Certificat complet de 1 006 cellules finales fermées, jointives, exactes :**
- **2 011 nœuds de subdivision traités**, 1 006 feuilles certifiées, aucune cellule non certifiée, aucune cellule en attente.
- Couverture des extrémités et des 1005 jonctions vérifiée de manière indépendante par `fractions.Fraction`.
- Bornes globales dirigées exactes :

[
oxed{
A_N(r)gerac{23763242565712321121633107}{10000000000000000000000000000}>0,
}
]

[
oxed{
A_M(r)le-rac{21235779180155817648396567047}{5000000000000000000000000000}<0
}
]

pour tout (rac1{32}le rlerac1{16}), à la précision extérieure `S=10^28` du certificat d'intervalles historique et sans échantillonnage non certifié.

La jonction exacte en `r=1/16` avec l'étape 68q, puis en `r=1/8` avec l'étape 68p, donne :
[
oxed{A_N(r)>0,quad A_M(r)<0
quadorall rin[1/32,17/20].}
]

Ces signes sont ceux des coefficients temporels `[dot C]_N,[dot C]_M` de l'ORIGINAL sphérique six-couples Step58, sur la branche spatiale non homothétique Step55 et ses contraintes. Le quotient `M/N=-A_N/A_M>0` est formellement positif sur ce domaine dès que les identities exactes d'élimination des dérivées de lapses Steps68h/j et les autres contraintes sont bien appliquées. **Rang Dirac complet et conditions aux bords ne sont PAS démontrés.**

### Données de la preuve

Certificat brut **390 326 octets** `research/reports/gate2b-step68s-inner-1over32-to-1over16-cover.json`, Git blob `e890998a2f925f881ab85b60a9027e5828e35ed5`, SHA256 des octets locaux `7491e166286279f8ac6423677fec069f7fc9d6bca7bfda4271cedd1c0addedd4`. Le statut de sortie est `CERTIFIED`, le champ `processed` vaut `2011`, les 1 006 lignes de certificats contiennent les véritables bornes rationnelles inférieures/supérieures de chaque coefficient et leurs deux bornes de rayon.

Neuf jobs exécutés sous le **lanceur à timeout** `scripts/janus_bounded_job.py --timeout-seconds 24 --grace-seconds 2` :
- lots 1..8 : chaque lot 240 nœuds de subdivision ;
- lot 9 : 91 derniers nœuds ;
- tous les neuf ont fini `PASSED`, en 9 à 19 secondes chacun ;
- chaque nœud donne lieu à une sauvegarde atomique de l'état; les premières sorties ont correctement indiqué `INCOMPLETE` et le dernier `CERTIFIED`.
- États et logs locaux `research/reports/step68s-inner-band-run1..9.state.json`, `...log`.

**Limitations et travaux suivants** : zone `0≤r<1/32` **NON ENCORE TRAITÉE** ; l'intervalle de perturbation `Ustar±1e-6` conduit à la division par `s` et à une inflation d'intervalles près du centre, qui imposera probablement une normalisation par séries centrales et résidus divisibles (Step67b). Le replay complet des 1006 nouvelles feuilles avec un second processus borné reste à faire ; les 579 feuilles Steps68p/q ont été rejouées exactement au Step68r. Les équations de préservation temporelle globale, la jauge, les bords, le rang Dirac et le calcul indépendant non-IBP restent ouverts.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

# JANUS — Step68ad-B2 : vrai G physique, U_ss et U_sss certifiés sur un continuum

**26 octobre 2026 — uniquement \`research/gate2b-nonhomothetic-transfer\`.**  
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Résultat nouveau réellement exécuté : disparition du blocage « original G absent »

Les six sources physiques originales du Hamiltonien sphérique HR à six couples canoniques (Steps45/46/55norm/55barrier/68l/68n), les deux programmes Step68ad-A/B1 et les deux rapports historiques 68v/68ac ont été **reconstitués localement octet pour octet depuis GitHub et vérifiés par SHA Git blob**. La reconstruction a été effectuée dans \`/mnt/data/janus68adB2\`, puis le véritable \`physical_R2_global\` Step68ad-B1 a été **exécuté**, et un nouveau programme Step68ad-B2 a été écrit et exécuté sur les mêmes originaux. Contrairement à B1, ce travail n'est PAS limité à des polynômes jouets.

La branche radiale historique satisfait \`2s U_s=G(s,U)-2U\`, \`s=r²\`. L'original Step68v fournit les tubes rigoureux \`|U-Ustar|<=10^-7 s³\`, \`U_s>0\` et \`G_U<0\` sur \`0<=s<=1/64\`. Les quatre jets directionnels Step68n authentiques évaluent les dérivées de ce même G, avec arithmétique d'intervalles entière à arrondi sortant \`S=10^28\`. Les 32 cellules rationnelles fermées couvrent **tous** les \`s∈[0,1/1024]\` (donc \`r∈[0,1/32]\`), y compris \`s=0\`. Aucun échantillonnage ni division par s.

**NOUVEAUX INTERVALLES PHYSIQUES CONTINUS CERTIFIÉS, conditionnels aux preuves historiques Step49/68v :**

| Objet | Borne inférieure approx. | Borne supérieure approx. | Signe strict |
|---|---:|---:|---|
| \`R2\` | -1.414170375015186e-4 | -1.406541559177554e-4 | négatif |
| \`U_ss\` | **-2.022016433671329e-5** | **-2.007599805707252e-5** | **négatif** |
| \`R3\` | -7.320689826385639e-7 | -6.226026282646365e-7 | négatif |
| \`U_sss\` | **-8.139651115656399e-8** | **-6.913132664403898e-8** | **négatif** |

Les bornes faisant foi sont les **fractions rationnelles exactes** de \`research/reports/gate2b-step68ad-B2-original-G-Uss-Usss.json\` (32 lignes R2 et 32 lignes R3). Ces intervalles sont prouvés sur le **continuum**, pas uniquement aux 32 centres de cellules. La règle de transport Step68ad-A \`2s y'+(2n+2-G_U)y=R_n\`, \`a_n>0\`, transforme les bornes \`R2\` en \`U_ss\`, puis les bornes \`R3\` (utilisant le tube \`U_ss\` déjà certifié) en \`U_sss\`, sans singularité en \`s=0\`. Les intervalles contiennent les valeurs centrales historiques \`U_ss(0)=2U2\` et \`U_sss(0)=6U3\`. Ainsi **U est strictement croissante, concave, avec U_ss strictement décroissante** sur ce centre, sous les hypothèses historiques.

### Théorème exact supplémentaire sur la structure du véritable G

SymPy appliqué à \`normalized_symbolic()\` du **vrai** Hamiltonien 45/46/55 démontre **globalement sur le chart régulier** :

\`\`\`
degree_U G(s,U) = 2
G_UUU(s,U) = 0 identiquement
G_UU(s,U) = s * C(s)

C(s) = -tf0 * [
  3 Lf0² beta3 sqrt(1-s z1²)
  + 2 Lf0 Lg0 beta2 sqrt(1-s z1²)
  + 4 Lf0 Lg0 beta2
  - Lg0² beta1 sqrt(1-s z1²)
  + 4 Lg0² beta1
] / [
  2 Lf0 Mf2 sqrt(Lf0²+s tf0²) sqrt(1-s z1²)
  (Lf0² beta3+2 Lf0 Lg0 beta2+Lg0² beta1)
]
\`\`\`

L'égalité exacte \`G_UU=s C(s)\` a été **vérifiée par soustraction symbolique identiquement nulle** ; \`G_UUU=0\` est exact. En injectant les fonctions géométriques originales Step55, l'arithmétique d'intervalles entière sur le rectangle **entier** \`s∈[0,1/1024]\` prouve :

\`\`\`
C(s) ∈ [
  273675860491573585434851043 / 312500000000000000000000000,
  8759118527135013881867641213 / 10000000000000000000000000000
] ⊂ (0.87576, 0.87592).
\`\`\`

\`At>0\`, le crochet du numérateur \`>0\`, \`tf0<0\` et les dénominateurs restent positifs sur le chart. Par conséquent \`G_UU(0,U)=0\` et \`G_UU(s,U)>0\` pour \`0<s<=1/1024\`. Ce résultat est un **théorème de structure original** utile pour réduire les dépendances d'intervalles dans les prochaines étapes ; ne pas le confondre avec une preuve de stabilité cosmologique.

## Vérifications effectivement effectuées

- **16 tests nouveaux PASS, 0 FAIL final** : \`PYTHONPATH=/mnt/data/janus68adB2 OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_step68ad_b2_physical_center_higher_jets.py\` (16,26 s). Un premier run avait **1 FAIL de test mal spécifié** : il exigeait qu'un intervalle de R3 calculé par une voie indépendante CONTIENNE tout l'intervalle historique de 54 U3. La condition correcte est leur **intersection non vide** ; corrigée, suite entière relancée 16 PASS. Ce n'était pas une contradiction physique.
- **32 cellules originales** exécutées, 64 cellules exécutées et incluses dans les bornes 32 ; **128 cellules** supplémentaires exécutées (15,08 s), donnant \`U_ss∈[-2.017944995e-5,-2.011665476e-5]\` et \`U_sss∈[-7.690428106e-8,-7.360653894e-8]\` : signes stables et bornes resserrées. Les 128 ne sont PAS la source du JSON canonique 32 cellules.
- **Step55 original 256 cellules réellement rejoué**, \`Step54_positive_two_dust_and_JK_signs_apply=True\` (4,5 s).
- Les 9 résidus symboliques Step45 et 5 identités Step46 ont été recalculés, avec 0 échec.
- Le JSON complet est issu de l'exécution du VRAI programme, puis publié sur GitHub. SHA blob **exactement identique** à la sortie locale Python : \`ac961b5b83667a83497497d22a701c24584cb561\`. Les codes et tests publiés ont aussi les **mêmes SHA** que les fichiers Python effectivement exécutés.

**Fichiers GitHub :**
- \`numerics/hr_step68ad_b2_physical_center_higher_jets.py\` — blob \`89ce02af12145eb8ab6bdcc354649571dd5da179\`.
- \`tests/test_hr_step68ad_b2_physical_center_higher_jets.py\` — blob \`5e2b5f297fbef78e38f05c76aebd05f8f4b2ee02\`.
- \`research/reports/gate2b-step68ad-B2-original-G-Uss-Usss.json\` — blob \`ac961b5b83667a83497497d22a701c24584cb561\`.

Pour reproduire depuis un checkout complet : \`PYTHONPATH=. python -m numerics.hr_step68ad_b2_physical_center_higher_jets research/reports 32\`, puis la commande pytest ci-dessus.

## Limites et action suivante : Step68ad-C

**Ne PAS revendiquer la fermeture de GATE_2B.** Cette preuve concerne les dérivées SPATIALES \`U_ss,U_sss\` de la branche radiale historique, sous ses hypothèses d'existence et de positivité. **AUCUN coefficient temporel original Step58/60 n'a été évalué dans cette session**, aucune preuve de rang de Dirac complet, lapses/bords/jauge, exceptions J/K, oracle NON-IBP, stabilité BD ni cosmologie 4D.

**NEXT EXACT ACTION : Step68ad-C** : reconstruire/authentifier les sources temporelles Steps57/58/60 et 68o, remplacer dans le calcul des **12 jets canoniques** les dérivées \`U_ss,U_sss\` issues d'une division par \`s\` (instables près du centre) par les enclosures **prouvées ici**, tout en conservant le vrai G et les tubes U/Us Step68v. Calculer \`A_N/r²,A_M/r²\` sur les **7 cellules PENDING [1/64,1/32]**, puis sur l'anneau plus intérieur et \`r→0\`. Si les intervalles sont trop larges, utiliser la structure quadratique exacte de G pour raffiner les enclosures avant toute revendication de signe. Le rang Dirac et les conditions aux bords restent ouverts indépendamment de ces signes.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

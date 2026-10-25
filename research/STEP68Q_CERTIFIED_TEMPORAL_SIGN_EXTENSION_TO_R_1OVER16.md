# JANUS — Étape 68q : extension exacte du certificat temporel à r=1/16

**25 octobre 2026 — branche de recherche unique `research/gate2b-nonhomothetic-transfer`. GATE_2B OPEN, JANUS-R NOT_VALIDATED.**

## Avancée physique

Le certificat de signes de la vraie branche non homothétique Step55, du vrai opérateur temporel local Step58 et de leurs six couples canoniques incluant deux poussières a été prolongé vers le centre.

Le certificat original Step68p couvre `r∈[1/8,17/20]`. Pour le nouveau sous-domaine contigu `[1/16,1/8]`, l'algorithme INCHANGÉ `numerics/hr_step68p_adaptive_temporal_sign.py` utilise encore :
1. les huit sources historiques physiques originales vérifiées par Git blob SHA ;
2. le tube continu `|U-Ustar|<=10^-6` certifié Step68l depuis `r=0` jusqu'à `r=17/20` ;
3. les jets ODE `U_s,U_ss,U_sss` via le vrai `2sU_s=G(s,U)-2U`, et tous les jets spatiaux canoniques nécessaires à `A_N,A_M` ;
4. les intervalles entiers à arrondis externes originaux Step55, échelle `10^28` ;
5. le vrai six-pair `physical_operator()` Step58, y compris la variation dynamique du déplacement.

**Résultat exact sur les 314 cellules FERMÉES, JOINTIVES couvrant `[1/16,1/8]` :**

[
oxed{
A_N(r)gerac{13992170999239591409209901}{500000000000000000000000000}>0,
}
qquad
oxed{
A_M(r)le-rac{17646463958239652791556564517}{1250000000000000000000000000}<0
}
]

sur chaque rayon de ce domaine, pas uniquement sur des points testés. La lecture conservatrice du rapport local (-A_N/A_M) (sur le shell des contraintes Steps68h/j) est
[
rac{55968683996958365636839604}{79184386692553776136944653495}
le -A_N/A_M le
rac{79689385241469629236974176738}{33850878182454791881349054917}.
]
Ces bornes sur le rapport sont larges et **ne doivent pas être confondues** avec le ratio numérique ponctuel ~0,519 de Step68f.

**Statistique auditée :** 627 nœuds traités, 314 cellules certifiées, 0 rejet, 0 attente. Une vérification indépendante par `fractions.Fraction` a trié les feuilles et confirmé les 313 jonctions exactement, le début `r=1/16`, la fin `r=1/8` et les 314 signes stricts.

Le certificat complet contient les quatre bornes rationnelles par cellule, la provenance git/source et la file finale vide :

`research/reports/gate2b-step68q-inner-1over16-to-1over8-cover.json` — Git blob `82f5d046cd0ca0c342adabe8b8f13cfc3f99308d`, SHA256 des octets réellement exécutés `296e83528f9675fd42521b7cfffa2ec0f6057cce1d930a97a323aa007009e2c2`.

## Timeouts réels, travaux segmentés et état d'interruption

Quatre lots bornés par `scripts/janus_bounded_job.py` (chacun `--timeout-seconds 24 --grace-seconds 2`) ont enregistré atomiquement après CHAQUE cellule les résultats et la file de subdivision dans `research/reports/step68q-inner-band-1over16-to-1over8.json` avant les étapes suivantes.

| Lot | Total nœuds au terme | Feuilles certifiées | Cellules en attente |
|---|---:|---:|---:|
| 1 | 160 | 77 | 7 |
| 2 | 320 | 158 | 5 |
| 3 | 576 | 286 | 5 |
| 4 | 627 | 314 | 0 |

Les quatre commandes se sont terminées avant les 24 secondes allouées, **sans timeout**. Elles ont conservé leurs propres états et journaux bruts `research/reports/step68q-inner-band-run{1..4}.state.json` / `.log` dans le workspace local. Le certificat central est publié sur GitHub ; les journaux individuels peuvent être publiés en annexe.

## Portée et limitation scientifique

En joignant **exactement** la borne supérieure précédente `r=1/8`, la zone continue actuellement certifiée est :

[
oxed{A_N(r)>0,quad A_M(r)<0qquad
orall,rin[1/16,17/20]}
]

sur la vraie branche radiale SPATIALE certifiée, **conditionnellement au modèle sphérique d'origine, à l'évaluation des contraintes et au choix de charte régulière**.

**TOUJOURS OUVERT :** `0<=r<1/16` (y compris centre `K(0)=0`), preuve locale régulière du rapport de lapses au centre, compatibilité temporelle complète, bords/jauge, oracle six-couples Poisson NON-IBP, rang Dirac, absence fantôme BD, pertinence 4D. Le résultat n'a pas été étendu à ces domaines.

**Prochaine étape :** relecture arithmétique de TOUTES les cellules enregistrées par nouvelle évaluation bornée indépendante, puis adapter la largeur près de `r=0`. Si la méthode d'intervalles divergente en `1/s` ne permet plus de conclure, normaliser les coefficients et utiliser les séries centrales Step67b, sans fabriquer une extension de validité.

**VERDICT : certificat temporel extérieur et nouvelle bande intérieure rigoureux ; GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

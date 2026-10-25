# JANUS — Étapes 68n–68p : certificat temporel par intervalles sur l'anneau extérieur

**25 octobre 2026 — branche exclusive `research/gate2b-nonhomothetic-transfer`. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Résultat rigoureux conditionnel à la chaîne physique originale

Les huit modules physiques originaux Step45/46/55-normalisé/55-barrière/57/58/59/60 sont authentifiés octet pour octet et exécutés ensemble. La nouvelle arithmétique des jets Taylor d'ordre 3 part de la véritable EDO Step55

[
2sU_s=G(s,U)-2U,qquad s=r^2,
]

et du **tube global continu certifié** de Step68l, (|U-U_*(s)|le10^{-6}). Elle propage les intervalles des jets nécessaires de **douze variables canoniques**, dont les deux poussières, puis évalue les expressions **originales du crochet temporel complet Step58**, sans figer les variations du déplacement relatif. Les opérations d'intervalle sont celles de l'original Step55, à entiers orientés avec échelle (10^{28}). Une anomalie initiale d'interprétation des exposants demi-entiers a été corrigée avant la certification.

La routine `numerics/hr_step68p_adaptive_temporal_sign.py` subdivise automatiquement les cellules dont les intervalles ne permettent pas de conclure. Elle conserve après **chaque** cellule une file d'attente, les cellules certifiées, les échecs et l'identité SHA de ses fournisseurs. Une cellule incertaine est **subdivisée**, jamais déclarée positive par approximation. Elle ne délivre `CERTIFIED` que lorsque l'ensemble du domaine est couvert sans trou par des cellules aux bornes strictement signées.

**Certificat fini archivé :**
- Domaine exact des rayons : (oxed{1/8le rle17/20}), soit (0{,}125le rle0{,}85).
- **529 nœuds examinés, 265 cellules fermées certifiées**, 0 cellule échouée, 0 cellule en attente ; limites rationalisées exactes et vérification de jonction.
- Borne globale inférieure rigoureuse de (A_N) :

[
oxed{A_Ngerac{74947205335628168039413183}{1250000000000000000000000000}>0}
]

- Borne globale supérieure rigoureuse de (A_M) :

[
oxed{A_Mle-rac{237882690187249002934304118023}{5000000000000000000000000000}<0.}
]

Ces fractions sont lues en forme exacte dans `research/reports/gate2b-step68p-adaptive-outer-cover.json`, avec tous les intervalles locaux vérifiables. **Le quotient local** (-A_N/A_M) est donc strictement positif sur cet anneau sur la branche radiale déterminée par les contraintes précédemment certifiées.

Les estimations globales très prudentes sur ce quotient sont incluses dans le rapport machine, mais elles sont **beaucoup plus larges** que les variations numériques ponctuelles de Step68f (~0,519) et ne prouvent pas une précision uniforme au millième.

## Reproductibilité, timeout et provenance

**Nouveaux modules archivés :**
- `numerics/hr_step68n_interval_ode_jets.py` — Git blob `96370e0599748c6dc07faf339ab3646ae3474e7d`
- `numerics/hr_step68n_temporal_interval_point.py` — Git blob `33e2ab71738baaea104e686c427bd8c52109343d`
- `numerics/hr_step68o_temporal_interval_annulus.py` — Git blob `c99caebc17f243784450ddff94fb061767e6d8e7`
- `numerics/hr_step68p_adaptive_temporal_sign.py` — Git blob `10f62bacafa25827de747707dd3f45c7c96458a6`
- `tests/test_hr_step68o_68p_temporal_annulus.py` — Git blob `381f44035d638fab153373ac5a2e76c830b46c5d`

Le **certificat des 265 cellules** est publié intégralement dans `research/reports/gate2b-step68p-adaptive-outer-cover.json`, SHA Git blob `978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6`, SHA256 local `179b967cc21160dcfef5eb98e1142c5ca17b83ee182d17162a2ec64708e48e4f`.

Le rapport synthétique `research/reports/gate2b-step68p-certification-machine-summary.json` conserve les marges, les limitations et les traces d'exécution. La suite spécifique donne **10 tests réussis en 4,75s**, exécutés sous `scripts/janus_bounded_job.py` avec **27s de délai maximal** et journal/état `research/reports/gate2b-step68p-final-test.*`. Les lots du balayage ont été terminés sous trois échéances de 28s/27s/27s ; un arrêt déclenche la sauvegarde atomique, et la relance conserve les cellules déjà prouvées.

Commande reproductible depuis le workspace :
```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/janus_bounded_job.py \
  --timeout-seconds 27 --grace-seconds 2 \
  --state research/reports/gate2b-step68p-final-test.state.json \
  --log research/reports/gate2b-step68p-final-test.log \
  --label step68p-final-test -- \
  python -m pytest -q tests/test_hr_step68o_68p_temporal_annulus.py
```

Des tests négatifs conservent explicitement l'échec de certification d'une cellule trop large, le rejet de rayons hors domaine et d'une preuve altérée, et la comparaison à un calcul flottant indépendant de l'original Step58 à (r=2/5). Le certificat des signes de lapses n'est pas dérivé d'une interpolation sur des rayons isolés.

## Frontières de la preuve — URGENT pour la reprise

Cette étape **NE TRAITE PAS** (0le r<1/8), où l'EDO (U_s=(G-2U)/(2s)) exige une normalisation spécifique au centre. Elle ne démontre pas non plus la conservation globale dans le temps de toutes les contraintes, la résolution de jauge ou des conditions aux bords, le rang complet de Dirac, l'oracle Poisson NON-IBP six-couples, les chartes (K=0,J=0), l'absence du fantôme BD, ni la cosmologie 4D.

**Prochaine étape 68q :** rejouer les 265 cellules par lots bornés indépendants et conserver des témoins de replay, puis prolonger l'analyse de signes vers l'intérieur ((0,1/8)) à l'aide des séries certifiées au centre (U_0,ldots,U_3) et/ou d'une continuation par segments adaptatifs. Il faut garantir que l'erreur temporelle en chaque cellule contient effectivement la VRAIE solution centrale. Enfin analyser compatibilité et fixation des lapses, conditions aux bords et rang.

**VERDICT : certificat de signes temporels sur anneau extérieur ACQUIS dans les hypothèses du modèle sphérique Step55 ; GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

# b3c3d6 — audit rationnel indépendant des jets U_ss Step55 (31 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Cette session ne rejoue **aucun** moteur physique Step45/46/55/58 et ne prétend pas avoir certifié les six coefficients Step58.

## Entrées authentifiées et portée

Le certificat Step55 physique antérieur, `research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json` (Git blob SHA `e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`), fournit les boîtes rationnelles sortantes `G,G_s,G_U` aux quatre rayons exacts. La transcription de `U0,U1,U2` reprend les constantes originales de `numerics/hr_step55_global_barrier.py` (SHA `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`). Le `sqrt(H2)` de `U0` est enclos par `isqrt` avec deux rationnels consécutifs de dénominateur `10^40` et contrôle exact des carrés. Aucune approximation flottante n'intervient dans les inégalités.

À chaque `s=r²>0`, `U` est enclos par `Ustar(s)±1/10000`, puis `F=U_s=(G-2U)/(2s)` et
`U_ss=[G_s+(G_U-4)F]/(2s)`.
Toutes les opérations et comparaisons finales utilisent `fractions.Fraction`. Les quatre boîtes sont **ponctuelles** ; aucune interpolation radiale ni certification BVP n'en découle.

## Nouveaux budgets physiques conditionnés aux enclosures antérieures

| r exact | borne rationnelle stricte | intervalle U_ss indicatif |
|---|---|---|
| 1/4 | `|U_ss|<1/10` | [-0,096825718 ; +0,096784173] |
| 1/2 | `|U_ss|<1/160` | [-0,006223061 ; +0,006181852] |
| 7/10 | `|U_ss|<1/590` | [-0,001686533 ; +0,001645747] |
| 17/20 | `|U_ss|<1/1200` | [-0,000810101 ; +0,000769446] |

Ces bornes sont vérifiées **exactement**, non sur les nombres décimaux affichés. Le signe de `U_ss` reste indéterminé aux quatre points. Recomposition indépendante de `pLf''=G+2sG_s+G_U(G-2U)` : les quatre boîtes calculées sont incluses dans celles du certificat archivé, avec borne supérieure strictement négative. Ce contrôle vérifie la cohérence du transfert de jets ; il ne vérifie pas à nouveau les calculs physiques initiaux de `G_s` et `G_U`.

## Exécution, tests, limites

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_independent_uss_archive.py' -v` : **7 PASS, 0 FAIL, 0 SKIP** après reconstruction locale de l'archive à l'identique, Git blob SHA vérifié. `python -m compileall -q numerics/hr_b3c3d6_independent_uss_archive.py tests/test_hr_b3c3d6_independent_uss_archive.py` : **PASS**. Quatre contrôles négatifs : signe de `G_U`, rayon incorrect, borne `pLf''` altérée et enregistrement manquant. Une première exécution locale sur une **fixture partielle** avait produit 6 PASS/1 SKIP ; après restitution exacte des 4 640 octets et SHA de l'archive, les sept tests ont été rejoués PASS.

Fichiers : `numerics/hr_b3c3d6_independent_uss_archive.py`, `tests/test_hr_b3c3d6_independent_uss_archive.py`, `research/reports/gate2b-b3c3d6-Uss-pointwise-independent-audit.json`, présente note. Le code peut imprimer les fractions complètes des quatre boîtes `U_ss` à partir de l'archive authentifiée.

**Étape suivante inchangée :** exécuter le moteur original Step58 SHA `802c23aebd41780d8c462f1aa1711707fe4ee88f` sur les vrais jets Step55 aux quatre rayons, encloser les six `A_N,A_M,B_N,B_M,E_N,E_M` et rechercher les annulations exactes ; raffiner le tube par DOP853 au rayon exact si nécessaire. Puis résoudre/exclure le BVP des lapses strictement positifs aux deux vrais bords ; enfin Dirac six couples, jauge temporelle, 4D, stabilité et observables. Aucun résultat ponctuel ne vaut no-go ni validation globale.

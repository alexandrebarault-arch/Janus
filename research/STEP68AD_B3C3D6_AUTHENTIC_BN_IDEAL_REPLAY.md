# JANUS — b3c3d6 : rejeu original authentifié de l'identité B_N (2 novembre 2026)

**Résultat nouveau : original Step45 + original Step58 exécutés ; facteur du premier jet B_N vérifié par SymPy exactement sur la carte K>0.** Il ne s'agit plus seulement d'une transcription indépendante.

## Provenance et tests
Départ HEAD `4f7037cb40093558a3f2878c741cf0d1ed8acb62`. Copie depuis le contenu GitHub via connecteur et contrôle des blobs Git : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; module de réduction des hauts jets `086b6bae543c0ee497ca9154c5a055921f018423` ; réduction de l'idéal `bc9b371c3d66f6b2491009e631fa4ed4a29a676f` ; ancien test `5862735ecc5c7c43e71ee3f6fec558fbab71a6a5`. Le shim d'import de Step57 redirige uniquement `authenticated_step45()` vers la fonction originale `exact_physical_ward()` ; ce n'est **pas** le Step57 intégral.

Commandes réellement lancées : `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_*bn*.py' -v` : **12 PASS, 0 FAIL, 0 SKIP** (7 tests existants originaux et 5 nouvelles gardes) ; `PYTHONPATH=. python -m numerics.hr_b3c3d6_authentic_bn_replay` : PASS ; `python -m compileall -q numerics tests` : PASS. Source et test de nouvelle garde exécutés localement, avec SHA Git `fd3a76fffd78adcb585a24613b4e1357d1d00f5c` et `348cc8c0d5f5585473f3a81e9e009ed8e335217a`.

## Théorème exact vérifié sur les sources originales
Poser R = B_N - z C / Lg + (1-z²) D_r(Hg)/(Lg Lf). Pour K>0 et les expressions Step45/58, les quatre hauts jets Sg_rrr, pLg_rr, Lg_rr, tg_rr sont des multiples exacts de Fz ; les jets zrr, zrrr sont absents ; les jets restant sont éliminés par Fz=0 et Hg=0. **SymPy renvoie zéro identiquement pour le résidu sur toute cette carte**, sans figer les autres premiers jets. Donc sur Fz=Hg=0 :

`B_N = z*C/Lg - (1-z²)*D_r(Hg)/(Lg*Lf)`.

Si aussi C=D_r(Hg)=0, B_N=0. Le test négatif de la source originale vérifie hors Hg=0 : Fz=0, Hg=2 et R=244/125, non nul. Les coefficients d'ordre deux E_N,E_M sont également annulés sur Fz=Hg=0 par le certificat original Step58.

## Limites indispensables
Résultat **formel local** sur la coquille de jets du modèle à six couples en carte K>0 ; aucun BVP positif entre deux vrais bords n'est construit ou exclu. L'identité ne certifie pas les boîtes de A_N,A_M,B_N,B_M,E_N,E_M sur la solution physique Step55 ; en particulier A_N+A_M à r=17/20 reste à encloser rigoureusement. La conservation globale des contraintes, le secteur K=0, le Dirac complet, la dynamique 4D, la stabilité et les observables restent ouverts.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Prochaine priorité : coefficient A_N+A_M au bord via l'opérateur original sur les enclosures physiques, puis les 24 boîtes A/B/E aux 4 rayons, enfin résoudre/écarter le BVP des deux lapses positifs.

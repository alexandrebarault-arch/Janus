# JANUS b3c3d6 — REJEU PHYSIQUE APPARIÉ Step55/Step58, quatre rayons (30 octobre 2026)

**Résultat numérique authentique et reproductible, non certifié par intervalles. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Ce qui a été réellement exécuté

Les **cinq originaux** ont été récupérés via le connecteur GitHub, matérialisés localement et vérifiés par le SHA-1 **Git blob** des octets exécutés : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalisé `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 barrière `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Le probe historique `643d90183367e74a28ed453d93f5489074b75b08`, le candidat cubique `43a140cacfca81aaf41073facea3da4e47e64f5e`, le runner apparié `bfb428de15d0d093d626f9b0f86fb42fa1f9442f` et les quatre helpers originaux ont également été matérialisés avec leurs SHA Git exacts. **Step57 n'a été utilisé que sous la forme d'un shim minimal d'import**, pas comme exécution du module complet.

La commande `PYTHONPATH=. python -m numerics.hr_b3c3d6_paired_original_step58_four_radii` a exécuté **une intégration DOP853 par rayon** et **quatre modes sur le même état terminal** (affine historique mixte, affine holonome strict, quadratique holonome, cubique holonome), aux rayons `1/4,1/2,7/10,17/20`. Le runner a été exécuté **deux fois**, dont une fois au sein du test d'intégration. Le probe historique seul a également été exécuté à `17/20`. La barrière Step55 originale à **256 cellules** a été réellement rejouée et a passé ses inégalités rationnelles sortantes.

## Résultats numériques ponctuels, PAS enclosures

| r | A_N | A_M | -A_N/A_M | max des quatre B/E en valeur absolue | ΔA_M affine holonome − historique |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1/4 | 218.48557629596342 | -421.15710622765034 | 0.51877452158640349 | 7.56e-45 | -1.564875423398e-7 |
| 1/2 | 865.16660342386560 | -1665.51343945579381 | 0.51945939487979071 | 1.18e-44 | -9.984903325433e-6 |
| 7/10 | 1673.86063913027884 | -3217.01554590731466 | 0.52031474988044848 | 1.91e-44 | -7.4891916105297e-5 |
| 17/20 | 2437.09399636764373 | -4676.64723416818403 | 0.52111991226576225 | 1.93e-44 | -2.39189973170046e-4 |

Les **six coefficients** de l'affine historique mixte, du quadratique et du cubique sont identiques à la précision **22 chiffres significatifs imprimés** par le vrai probe original. Le contrôle négatif affine **réellement holonome** ne modifie que `A_M`, aux quatre rayons. Ce contrôle est non trivial : l'ancienne « affine » historique était un prolongement **mixte non holonome** de `pLfr=rG(s,Ua)`. Le vrai Step58 original a donc confirmé les prédictions algébriques précédentes sur la famille physique testée. Les B/E affichés à ~10^-44 sont **des résidus numériques, pas une preuve de zéro exact**. Les résidus ponctuels `Fz,Hg,Hf,C` restent inférieurs à `9e-45` en valeur absolue dans ce rejeu ; ils ne constituent pas un contrôle continu.

**Contrôle croisé analytique supplémentaire sur les vraies données physiques :** la sensibilité exacte déjà dérivée sur `Fz=0`,
`dA_M/dU_ss=-2r^4 z sqrt(1-z²) K beta/(Lg Lf Mf2 Sf Sfr (beta+fac*tfr))`,
multipliée par `-U_ss`, reproduit la différence du contrôle affine holonome aux quatre rayons. Rapports observé/prédit : `1.0000000000005551`, `1.0000000000000265`, `1.0000000000000053`, `1.0000000000000009`. Le test vérifie une erreur relative <`2e-10` ; ce n'est pas un contrôle indépendant de la théorie physique.

## Convergence numérique et barrière

Affinage DOP853 `rtol=1e-10,1e-12,1e-13`, `atol=rtol/100`, avec RHS binary64 fidèle et transport terminal d'ordre 2 : les quatre différences `U(1e-13)-U(1e-12)` valent environ `±8.67361737988e-19` (une unité de quantification binary64 du solveur). Les `nfev` du runner principal sont `242,332,392,437`. **Une stabilisation sous raffinement n'est pas une borne rigoureuse d'erreur**, et le défaut DOP853 continu, l'erreur initiale de la série centrale et les enclosures A/B/E restent ouverts.

La barrière originale Step55 sur 256 cellules donne `max F_upper=-1480966474499367232302129/10000000000000000000000000000<0` et `min F_lower=295653233337826329055403/2000000000000000000000000000>0`. Elle concerne le profil spatial et repose sur les hypothèses centrales Step49 ; elle ne certifie ni les lapses ni Dirac.

## Tests, fichiers et reproduction

**6 unittest effectivement exécutés, 6 PASS, 0 FAIL**, dont **1 test d'intégration physique complet** activé par `JANUS_RUN_PHYSICAL_STEP58=1` ; `python -m compileall -q numerics tests` PASS. Cinq tests sont des gardes de parsing/état/signe, non indépendants ; le sixième rejoue les cinq originaux et les quatre modes. L'exécution de la barrière 256 cellules et les 12 solveurs de raffinement sont des commandes distinctes, **non comptées** comme unittest.

Fichiers : `numerics/hr_b3c3d6_physical_paired_replay_validation.py` (parse les six valeurs 22 chiffres et vérifie sensibilité/état), `tests/test_hr_b3c3d6_physical_paired_replay_validation.py` (test opt-in), `research/reports/b3c3d6_original_step58_four_radius_physical_replay_summary.json` (six A/B/E via résumés, quatre rayons, raffinement et barrière). Les blobs code/tests/rapport doivent être relus après publication. Le rapport complet brut local (incluant stdout par mode) n'est **pas** déposé dans GitHub ; le runner permet de le régénérer.

Reproduction : `JANUS_RUN_PHYSICAL_STEP58=1 PYTHONPATH=. python -m unittest tests.test_hr_b3c3d6_physical_paired_replay_validation -v`, ou `PYTHONPATH=. python -m numerics.hr_b3c3d6_paired_original_step58_four_radii > research/reports/b3c3d6_paired_full_raw.json`.

## Prochaine difficulté scientifique, inchangée

**b3c3d6 reste PARTIELLE.** Le comparateur physique est désormais rejoué ; priorité à un **certificat continu** du défaut DOP853, à l'erreur initiale et aux enclosures des six coefficients (en particulier B/E), puis à une factorisation exacte des éventuels zéros, au centre et au **vrai BVP avec N,M>0 et deux conditions de bord**. Ensuite seulement : contraintes Dirac six couples/rang/tertiaires, jauge temporelle et charges, K=0/J=0, dynamique 4D, stabilité et observables. Les petites valeurs de B/E ne doivent jamais être remplacées par zéro sans preuve.

Aucun changement de `main`, `research/v2-flrw` ni des workflows désactivés.

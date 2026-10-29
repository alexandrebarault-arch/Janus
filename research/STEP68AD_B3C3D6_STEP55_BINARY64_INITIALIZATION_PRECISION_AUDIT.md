# JANUS b3c3d6 — audit de l'arrondi binary64 de la condition initiale Step55 (30/10/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Audit numérique spécifique au candidat physique Step55→Step58 ; **aucun** moteur original Step45/46/55/58 n'a été exécuté dans cette session. Le code audité est `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py`, blob Git `8162e35deed964a5ec2cbca53bc32cc5c875e420`, lu via connecteur GitHub. Les paramètres sont recopiés de ce fichier, sans prétendre reproduire son intégration.

## Observation quantifiée

Le candidat fixe `s0=1e-4`, calcule `U0+U1*F(s0)+U2*F(s0)**2` avec mpmath puis **convertit le résultat en `float`** avant de le transmettre à `scipy.integrate.solve_ivp`. En reproduisant exactement les constantes décimales du candidat à 100 chiffres, la valeur **tronquée à l'ordre quadratique** est

`-0.005252347922344801514364923472998400505989718191313428996077244359492678…`.

Le binary64 effectivement transmis s'affiche `-0.005252347922344801`. Son erreur d'arrondi absolue relativement à cette valeur tronquée haute précision est `1.92639229918244511758…e-19`, erreur relative `3.667678393860944635…e-17`. La conversion ultérieure `mp.mpf(str(y_float))` utilisée dans le RHS n'est pas identique au binary64 exact : elle diffère de celui-ci de `3.217256935547538887…e-19`, et de la valeur tronquée de `5.143649234729984005…e-19`.

La seule erreur d'arrondi initiale est donc **plus de 10^25 fois l'échelle 10^-44** précédemment affichée pour certains coefficients B/E. **Attention : il ne s'agit PAS d'une borne d'erreur sur ces coefficients** ; leur sensibilité à U n'a pas été calculée et une annulation structurelle exacte reste possible. L'observation prouve seulement que **45 chiffres mpmath à l'évaluation finale n'impliquent pas 45 chiffres de précision pour la solution ODE produite par solve_ivp en binary64**. L'erreur inconnue du Taylor initial (terme cubique et suivants), l'erreur de solve_ivp et l'amplification dynamique restent non bornées.

## Contrôles reproductibles

`PYTHONPATH=. python -m unittest discover -s tests -v` : **6 tests PASS, 0 FAIL**, dont contrôle de la constante centrale, encadrement de l'erreur d'arrondi, distinction binary64/chaîne décimale, stabilité 90→120 chiffres, recomputation des diagnostics et contrôle négatif à 10^-40. `python -m compileall -q numerics tests` : PASS. Tests locaux isolés, non indépendants des formules transcrites. L'audit ne remplace pas le rejeu des sources SHA-authentifiées.

## Conséquence opérationnelle

Pour le vrai rejeu b3c3d6, séparer les sorties `NUMERICAL_DOUBLE_PRECISION` de toute prétention `EXACT_ZERO` ; mesurer la convergence en `rtol/atol`, en `s0` et en précision, puis fournir une preuve symbolique ou une enclosure validée des six coefficients A/B/E et de la solution Step55 avant toute inférence sur les lapses. Prochaine étape prioritaire inchangée : cinq originaux SHA-authentifiés, candidat cubique et ancien affine aux quatre rayons 1/4,1/2,7/10,17/20, puis centre/BVP positif deux bords, Dirac/4D/stabilité/observables. `main`, `research/v2-flrw`, workflows non modifiés.

Code : `numerics/hr_b3c3d6_step55_float_initialization_audit.py` ; tests : `tests/test_hr_b3c3d6_step55_float_initialization_audit.py`.

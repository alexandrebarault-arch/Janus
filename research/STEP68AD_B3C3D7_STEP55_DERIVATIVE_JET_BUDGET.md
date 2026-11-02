# JANUS — b3c3d7 : fermeture des jets Step55 nécessaire à une certification continue (02/11/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Le HEAD main authentifié à la reprise était `88bbe8e78a736180e84ee9e8d3ae04333a230598`. Les sources originales Step55 `numerics/hr_step55_normalized_secondary.py` (blob a54a6acf2f7ad2f64c500faecfa1406ecbf7b862) et Step58 `numerics/hr_step58_temporal_operator.py` (blob 802c23aebd41780d8c462f1aa1711707fe4ee88f) ont été lues sur main ; les moteurs physiques ne sont PAS rejoués dans cette session.

## Calcul exact : fermeture holonome de l'EDO normalisée

Avec `s=r²>0`, `2s U_s=G(s,U)-2U`, on dérive le long de la vraie solution :
```
U_s   = (G-2U)/(2s)
U_ss  = (G_s+(G_U-4)*U_s)/(2s)
U_sss = (G_ss+2*G_sU*U_s+G_UU*U_s²+(G_U-6)*U_ss)/(2s).
```
Si un coefficient Step58 réduit s'exprime comme `A=A(s,U,U_s,U_ss)`, la dérivée requise par le gate b3c3d7 est exactement
`d(A/s)/ds = (s*(A_s+A_U*U_s+A_(U_s)*U_ss+A_(U_ss)*U_sss)-A)/s²`.
La condition « si » doit être revérifiée sur les expressions physiques originales : ce script ne certifie pas leur dépendance réelle et n'évalue pas leurs dérivées.

**Donnée manquante identifiée :** les archives ponctuelles `G,G_s,G_U` utilisées pour `U_s,U_ss` ne bornent pas, à elles seules, `U_sss` ; il faut également des enclosures de `G_ss,G_sU,G_UU` sur le tube Step55 et un contrôle de dépendance du Step58 réduit. Contre-exemple analytique exact non physique : `G_1=G_0+epsilon*(s-s0)²` conserve `G,G_s,G_U` à `s0>0` mais change `U_sss` de `epsilon/s0`; à `s0=1/4,epsilon=1`, différence **4**. Cela ne constitue pas une perturbation admissible du vrai `G` physique, qui est fixé.

## Centre

Pour `U=U0+U1*s+U2*s²+...` analytique, la compatibilité impose `G(0,U0)=2U0`, puis `(4-G_U(0,U0))*U1=G_s(0,U0)` et `(6-G_U(0,U0))*U2=(G_ss+2G_sU*U1+G_UU*U1²)/2` au centre. Les cas résonants `G_U=4` ou `6` nécessitent une analyse séparée. Aucune borne physique du reste de Taylor ni des coefficients `A_N,A_M` sur `0<=r<=1/4` n'est obtenue.

## Reproduction et prochain travail

Fichiers : `numerics/hr_b3c3d7_step55_derivative_jet_budget.py` et `tests/test_hr_b3c3d7_step55_derivative_jet_budget.py`. Test local sur les octets préparés : `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d7_step55_derivative_jet_budget.py' -v` : **9 PASS, 0 FAIL, 0 SKIP** ; `PYTHONPATH=. python -m numerics.hr_b3c3d7_step55_derivative_jet_budget` : PASS ; `python -m compileall -q numerics tests` : PASS (sur les deux nouveaux fichiers). Contrôler les blobs Git après publication.

**Prochaine priorité réelle :** dériver et borner par intervalles rationnels les trois dérivées secondes `G_ss,G_sU,G_UU` sur les cellules du tube original Step55 ; authentifier la dépendance de `A_N,A_M` réduits et leurs dérivées par les jets physiques, puis comparer aux seuils suffisants `4123900/147` et `378550/7`. Traiter séparément le centre et les deux vrais bords temporels ; poursuivre Dirac/charges/4D/stabilité/observables. Aucun certificat continu physique ni BVP JANUS obtenu.

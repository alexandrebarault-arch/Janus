# JANUS b3c3d6 — marge uniforme exacte de non-fermeture sur la tranche de jets gelés (31 octobre 2026)

**Verdict : théorème algébrique exact, STRICTEMENT RESTREINT ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et portée

Branche `research/gate2b-nonhomothetic-transfer`. HEAD authentifié au démarrage `2cc4e429391ada2fd11ab67cb1b512fd137c8736`. Sources originales Step45 et Step58 lues via GitHub, blobs `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `802c23aebd41780d8c462f1aa1711707fe4ee88f`. **Ces moteurs originaux n'ont pas été exécutés cette session** : le conteneur ne résout pas raw.githubusercontent.com. Ce certificat est une conséquence algébrique indépendante des polynômes du précédent audit de la tranche à trois paramètres, et non une vérification physique indépendante de leur provenance.

Sous `Fz=Fz_r=Hg=Hg_r=C=Hf=0` et les jets restants GELÉS comme dans `hr_b3c3d6_three_parameter_radial_no_go.py`, avec `b=Sf_r≠0`, `a=-(24b+12)/25`, `c=(b²−1)/(2b)`, on a :

```text
P(b)=204b³−72b²−141b−56
T(b)=144b³+224b²+b−20
Fz_rr=−P(b)/(64b)
C_r=T(b)/(100b)
```

**Théorème plus fort que le simple résultant non nul : pour tout b réel non nul de cette tranche,**

```text
max(|Fz_rr|, |C_r|) > 7/8.
```

Il n'existe donc même pas de fermeture radiale *approchée* avec les deux résidus simultanément de module ≤7/8 dans cette normalisation précise. Cela ne s'étend ni aux jets libres ni aux profils Step55.

## Preuve rationnelle, trois domaines exhaustifs

Pour `0<b≤1/2`, `204b³≤102b²` et `30b²≤15b` donnent `P(b)≤30b²−141b−56<−56` ; ainsi `|Fz_rr|>56/(64b)≥7/4`.

Pour `b≥1/2`, `C_r=(144b²+224b+1−20/b)/100` est strictement croissant (dérivée `(288b+224+20/b²)/100>0`) ; donc `C_r≥C_r(1/2)=109/100>7/8`.

Pour `b<0`, poser `x=−b>0`. L'identité exacte est `Fz_rr=−7/8−h(x)/(64x)`, où `h(x)=204x³+72x²−197x+56`. Sur `[0,2]`, six cellules rationnelles `[0,1/4]`, `[1/4,3/8]`, `[3/8,7/16]`, `[7/16,1/2]`, `[1/2,1]`, `[1,2]` ont leurs **quatre coefficients de Bernstein strictement positifs**, consignés intégralement dans le rapport JSON. Pour `x≥2`, `h=x(204x²+72x−197)+56>0`. Donc `Fz_rr<−7/8` sur tout `b<0`.

La borne est **stricte**, démontrée en fractions exactes ; les échantillons des tests ne servent pas de preuve.

## Tests, limitations, prochaine priorité

**8 unittest PASS, 0 FAIL, 0 SKIP au rejeu final**, `python -m compileall -q` PASS et CLI JSON PASS. Un premier lancement a eu deux FAIL de comparaison SymPy structurelle/coefficient de dérivée dans les tests, corrigés avant le rejeu final ; aucune erreur résiduelle. Les fichiers source/test publiés sont vérifiés par comparaison des SHA Git avec les octets effectivement testés.

AUCUNE factorisation universelle du résidu inférieur `B_N-z*C/Lg-beta*Hg_r` sur la coquille holonome complète ; AUCUNE des six enclosures physiques Step55/58 aux quatre rayons ; AUCUN BVP de deux lapses positifs ni résultat Dirac/4D/stabilité/observables. **Prochaine priorité inchangée :** réexécuter les originaux Step45/58 authentifiés ; calculer le résidu universel B_N avec jets libres, puis les six enclosures physiques et le BVP strictement positif aux deux vrais bords. Le gain de cette session est un **écart uniforme** pour la seule tranche gelée, pas un no-go physique.

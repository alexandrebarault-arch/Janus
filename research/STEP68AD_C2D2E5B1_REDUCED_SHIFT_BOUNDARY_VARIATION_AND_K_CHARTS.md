# JANUS — 68ad-C2d2e5b1 : variation du shift réduit dans le terme de bord

26 octobre 2026. Branche exclusive `research/gate2b-nonhomothetic-transfer`. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Source et problème
Sources originales relues sur GitHub (blobs) : `numerics/hr_step37_original_nonibp_oracle.py` (`005449ade6e3582e3b9a5c3374a881a77e73e3f6`), `numerics/hr_spherical_mixed_hamiltonian_bracket.py` (`6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`), `numerics/hr_spherical_adm_primary.py` (`c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`). Leurs moteurs physiques ne sont **pas** réexécutés ici. La formule de bord à shift fixé de C2d2e5a ne doit pas être variée comme si `z` était indépendant une fois la réduction `F_z=0` effectuée.

## Identité exacte sur charte régulière
Poser `D=pSg*Sg' - Lg*pLg' + pg*tg'`, `K=m2*mg2*Lg*Lf*(b1*Sg²+2*b2*Sg*Sf+b3*Sf²)`, `Q=N+M*Lg/Lf`, `P=pLg`, `F_z=D-K*z/sqrt(1-z²)`. Sur **K>0** et `|z|<1`, la racine unique est `z*=D/sqrt(K²+D²)`. Par dérivation exacte :

```
dz*/dD = K²/(K²+D²)^(3/2)
dz*/dK = -D K/(K²+D²)^(3/2)
dz*/d(pLg') = -Lg K²/(K²+D²)^(3/2)
B_shift = -Q P z*
dB_shift/d(pLg') = Q P Lg K²/(K²+D²)^(3/2).
```

Ce dernier terme est **absent** si l'on varie à shift fixé. Il s'agit de la variation du terme de bord qui relie les densités originale et IBP, **pas** encore du flux symplectique complet de l'action originale. Dans le bulk, la règle de l'enveloppe élimine les contributions proportionnelles à `F_z` lorsque l'équation du shift est satisfaite ; elle ne justifie pas de supprimer les variations de bord.

## Témoin rationnel hors coquille
`K=3,D=4,Lg=2,Lf=3,N=M=1,P=7` donne `z*=4/5`, `F_z=0`, `dz*/d(pLg')=-18/125` et **`dB_shift/d(pLg')=42/25`**. Le terme est non nul. Ces nombres sont un contre-exemple à l'hypothèse de **variation de bord à shift fixé après élimination** ; ce ne sont pas des données initiales physiques Step68o ni une obstruction définitive.

## Chartes singulières et changement de signe
Sur `K<0`, la racine correcte est `z*=sign(K)*D/sqrt(K²+D²)`, pas la formule K>0 prolongée naïvement. Témoin `K=-3,D=4` : `z*=-4/5` satisfait `F_z=0` ; la racine incorrecte `+4/5` donne `F_z=8`. À `K=0,D≠0`, `F_z=D` interdit toute racine intérieure. À `K=D=0`, `F_z=0` pour tout `|z|<1` : l'élimination implicite n'est pas unique. La charte `J=0` n'est **pas** traitée.

## Exécution, provenance, portée
`cd /mnt/data/janus_e5b && python -m unittest -v test_hr_step68ad_c2d2e5b_shift_boundary.py` : **9 tests unittest PASS, 0 FAIL**, dont 4 sous-identités exactes SymPy ; `python hr_step68ad_c2d2e5b_shift_boundary.py` : PASS. Empreintes Git des octets réellement testés : programme `1996748565b7f587eaf46be3b740167e9bd1adbc`, tests `d771a62f9a0806ed39f3eeeea54233258e2f5978`. Les résultats rationnels sont synthétiques hors coquille. **Aucun crochet de Poisson complet à six couples ni rang Dirac n'a été calculé.**

**Prochaine étape effective : 68ad-C2d2e5b2** : construire et comparer les variations fonctionnelles non-IBP originales et IBP après réduction `z*`, en conservant tous les termes de bord et les six couples, puis examiner les conditions aux limites, contraintes tertiaires et chartes `K=0/J=0`. Ne pas considérer la variation du seul `B_shift` comme une matrice de Dirac.

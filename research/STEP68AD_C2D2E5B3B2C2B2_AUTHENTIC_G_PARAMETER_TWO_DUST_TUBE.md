# JANUS — 68ad-C2d2e5b3b2c2b2 : vrai moteur Step45/46/55, tube paramétrique spatial et deux poussières

**27 octobre 2026. Résultat certifié dans la charte spatiale sphérique prescrite, sous le théorème local analytique Step49. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources originales effectivement réexécutées

Quatre fichiers originaux ont été recopiés dans une arborescence Python isolée et vérifiés octet pour octet par leur SHA Git :
- `numerics/hr_step45_exact_physical_ward.py` : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` : `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
- `numerics/hr_step55_normalized_secondary.py` : `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
- `numerics/hr_step55_global_barrier.py` : `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

**Contrairement aux étapes précédentes, le véritable `G(s,U,P_g)` a été compilé depuis la contrainte secondaire originale à six couples et exécuté.** Le calcul emploie `normalized_symbolic()`, `G()`, `geometry()` et `certify_global_barrier()` originaux, avec `P_g` remplacé par l'intervalle `P_g+[-1/5000,1/5000]` dans toutes les reconstructions g. Le centre `U_0` est simultanément remplacé par `M_f^2 b[(P_g+lambda)/a-2z_1]`. Les coefficients `U_1,U_2` du benchmark initial restent une **fonction de comparaison**, et ne sont pas prétendus coefficients de Taylor de la famille perturbée.

## Certificat uniforme, non échantillonné

Sur `s=r² in [0,289/400]`, `|lambda|<=1/5000=0.0002`, 256 cellules radiales jointives et une seule enclosure extérieure de lambda, l'arithmétique entière dirigée `10^-28` donne :

- résidu de barrière supérieure `F_plus < -0.00003592609862704619` et résidu inférieur `F_minus > +0.00003557401204494962` (fractions exactes dans le JSON) ;
- `-0.005354 < U < -0.004585` ; donc l'hypothèse `|U|<=1` de l'audit précédent est satisfaite sur ce tube spatial ;
- `rho_f > 0.1094480192129855 > 1/10`, `rho_g > 0.8844952279164069 > 22/25` ;
- dénominateur poussière f `>=1>3/4`, beta poussière g `>0.9991759495061955>999/1000`, et `T>0.1060297323982008>0` ;
- `|G(s,U)-V_star(s)|<0.01` sur toute l'enclosure.

La positivité de `rho_f` utilise la **reconstruction primaire originale Step46**, après substitution exacte `pLf=sU`, `pLf'=rG`, `pf=s rho_f` :

`rho_f= -[U²/(4Mf2 Lf) - U*(G-s Dbar/Lf)/(2Mf2 Sfr) - Mf2*Lf³*Rf/2 + s*z1*Dbar/Lf + Wfbar] / [sqrt(1+kf²*s)+kf*s*U/(2Mf2*Sfr)]`.

Cette identité a été contrôlée indépendamment avec SymPy : résidu exact zéro. Le centre du **véritable** `G` a aussi été contrôlé symboliquement pour `P_g` variable : `G(0,U,P_g)=3Mf2*b*(P_g/a-2z1)-U` avec résidu exact zéro. Sous l'existence analytique locale Step49, les inégalités de barrière empêchent une sortie du tube et fournissent une continuation spatiale régulière sur le domaine radial considéré.

**Portée exacte :** une famille de données initiales sphériques contraintes, avec les deux poussières positives, dans la charte de reconstruction Step45/46/55. Les paramètres de référence et la géométrie prescrite sont ceux du benchmark ; ceci ne certifie pas les conditions physiques aux bords externes.

## Reproductibilité

Dans un clone complet du dépôt contenant les quatre sources ci-dessus :

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py' -v`

**13 tests unittest PASS, 0 FAIL** ; ils incluent deux identités SymPy exactes, la réexécution des identités originales Step45 et Step46, les SHA de quatre blobs, les bornes sur 256 cellules, la contre-vérification 512 cellules, et la détection de source altérée. `PYTHONPATH=. python numerics/hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py` régénère le JSON. Un essai exploratoire à 128 cellules ne certifie pas la barrière (surestimation d'intervalle au premier slab), tandis que 256 et 512 cellules la certifient : **échec de résolution d'enclosure, pas contre-exemple physique**. Les 13 tests finaux incluent un test qui vérifie que cet échec attendu est correctement détecté.

Fichiers scientifiques de cette étape :
- `numerics/hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py` — blob `180307509ad7992880b99319dbeb6f8662752127`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py` — blob `ec8e3145b65f902a95648872bfc3e5b554c25046`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2-authentic-Pg-fdust-tube.json` — blob `012e70e49b41cc3180da423c3962d279e3909a26`.

## Ce qui n'est toujours PAS démontré

Les conditions aux limites physiques à `r=17/20` n'ont pas été définies et la variation de `P_g` modifie les traces. Les résultats ne certifient ni une famille de solutions au problème aux limites final, ni les contraintes temporelles complètes. Le `J` temporel, le rang de Dirac et les tertiaires ne sont **pas** calculés ici ; ne pas réutiliser les indicateurs Step54 de la configuration fixe comme une preuve de rang paramétrique. Les chartes `K=0/J=0`, les lapses globaux, la dynamique 4D, la stabilité et les observables restent ouverts.

**Prochaine étape : 68ad-C2d2e5b3b2c2b3** — définir les conditions aux limites physiques et calculer la carte des traces paramétriques sur le tube certifié ; confronter la famille aux bords admissibles, puis engager l'oracle fonctionnel Poisson/Dirac original non-IBP à six couples, rang/tertiaires/lapses. Conserver `GATE_2B OPEN` et `JANUS_R NOT_VALIDATED`.

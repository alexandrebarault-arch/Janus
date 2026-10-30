# JANUS b3c3d6 — transfert exact des jets Step55 au bord DOP853 (31 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED. Étape b3c3d6 PARTIELLE.** Cette note complète, sans remplacer, le certificat physique Step55 du 30 octobre (28 pas, 7 168 sous-cellules corrélées, borne terminale rationnelle). Aucun nouveau rejeu physique Step55/58 n'a été exécuté dans cette session : le calcul présent réutilise les fractions **authentifiées et publiées** du certificat antérieur.

## Résultat exact, avec conditions explicites

Pour l'EDO originale `2s U_s=G(s,U)-2U`, soit `P(s_b)` la valeur du polynôme dense DOP853 au **temps terminal binary64** `s_b=6507701461550367/9007199254740992`. Le certificat Step55 précédent fournit `|U(s_b)-P(s_b)|<=epsilon`, où `epsilon` est la fraction exacte publiée dans le rapport du 30 octobre et vaut environ `4.849547003502489e-6`. La même garde corrélée assure que les deux valeurs et le segment qui les joint appartiennent au tube original. Sur ce tube, `G_U` est rigoureusement enclos dans `[-1.0010994328099383,-0.9939716062572771]` (les fractions exactes sont dans le code).

Par le théorème des accroissements finis, **sans différencier le polynôme dense**, avec `F(s,u)=(G(s,u)-2u)/(2s)` :

`|U_s(s_b)-F(s_b,P(s_b))| <= max(|G_U-2|)*epsilon/(2s_b) = 1.0071953468232841e-5` (borne rationnelle exacte, affichage décimal indicatif).

Les champs Step58 `pLf=sU` et `pLf'/r=G(s,U)` satisfont au **même s_b** :

- `|pLf(s_b)-s_b P(s_b)| <= s_b epsilon = 3.503797710030549e-6` ;
- `|pLf'(s_b)/sqrt(s_b)-G(s_b,P(s_b))| <= max(|G_U|) epsilon = 4.854878754591478e-6`.

Les comparaisons rationnelles strictes `|U_s-F|<11/1000000` et `|pLf'/r-G|<51/10000000` sont exécutées par les tests. **Attention :** ce ne sont ni des erreurs sur `P_s`, ni une enclosure des six coefficients Step58, ni une évaluation au rayon décimal exact `r=17/20`. Le décalage `s_b-289/400` est exactement positif et vaut environ `3.1086244689504386e-17`; son transport doit encore être enclos avant d'attribuer ces bornes au bord Step58 original.

## Deuxième jet : formule exacte, borne physique non disponible

En posant `F=(G-2u)/(2s)` et `Q=(G_s+(G_U-4)F)/(2s)`, la solution vraie vérifie `U_{ss}=Q(s,U)`. La dérivée de sensibilité exacte est

`Q_U = [G_{sU}+G_{UU}F+(G_U-4)(G_U-2)/(2s)]/(2s)`.

Ainsi `|U_{ss}-Q(s,P)|<=epsilon sup|Q_U|` si un intervalle **physique sortant** de `G_{sU}`, `G_{UU}` et `F` est établi sur le segment et le même domaine. Le seul certificat `G_U` ne suffit **pas**. Contre-exemple algébrique jouet : `G(s,u)=k(s-1)u` donne `G_U(1,u)=0` pour tout `k`, tandis que `Q_U(1,u)=k/2+2` est non borné quand `k` croît. Cela identifie un verrou concret avant la propagation des six coefficients Step58.

Un second contre-exemple jouet, `U(s)=1` et `P(s)=1+10^9(s-1)`, montre que `U(1)=P(1)` n'impose aucune proximité de `U_s(1)` et `P_s(1)`. **La dérivation directe du polynôme DOP853 depuis la seule erreur terminale aurait été une fausse preuve.** Le transfert ci-dessus utilise exclusivement des jets cohérents avec l'EDO.

## Provenance, exécution et suite

Sources originales Step45/46/55 utilisées par le certificat antérieur, Git blob SHA : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `bac025c28dbe1561c0c36c56dbfda46dc326f804`, `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Rapport physique réutilisé : `research/reports/gate2b-b3c3d6-Step55-physical-correlated-DOP853-7168-cell.json` blob `e2e210e4ebe5a3b34a2c533e2c1cd705f7deb2dc`. Aucune nouvelle authentification d'exécution des moteurs originaux n'est revendiquée.

Code `numerics/hr_b3c3d6_endpoint_ode_jet_transfer.py` blob `06bc2eaf9bce60e70f0e05b85cce3b8f385e04ea` ; tests `tests/test_hr_b3c3d6_endpoint_ode_jet_transfer.py` blob `5476716f4abd8e9a86681a3812177668a739a345`. **5 unittest PASS, 0 FAIL** par `PYTHONPATH=. python -m unittest discover -s tests -v` dans le répertoire minimal de ces deux nouveaux fichiers ; `python -m compileall -q numerics tests` **PASS** ; `python -m numerics.hr_b3c3d6_endpoint_ode_jet_transfer` exécuté. Les deux SHA Git blob des fichiers publiés sont identiques aux octets réellement testés localement.

**Prochaine étape prioritaire :** calculer les enclosures sortantes physiques `G_{sU},G_{UU},F` sur le tube Step55, certifier `U_{ss}` au même point, puis transporter au rayon exact `r=17/20` et aux quatre rayons Step58 ; propager ces intervalles dans **A_N,A_M,B_N,B_M,E_N,E_M**, tester factorisation exacte et BVP `N,M>0` aux deux vrais bords. Ensuite seulement : Dirac six couples, rang, tertiaires, charges/jauge temporelle, 4D, stabilité et observables. Les valeurs numériques `B/E~10^-44` ne sont pas des zéros exacts.

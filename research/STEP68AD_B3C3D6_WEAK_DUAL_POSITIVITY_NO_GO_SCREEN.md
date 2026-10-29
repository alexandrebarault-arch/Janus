# JANUS b3c3d6 — certificat dual faible pour les lapses (29/10/2026)

**Résultat exact CONDITIONNEL et témoin JOUET, non physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Aucune exécution du candidat Step58 cubique sur les cinq originaux pendant cette session.

## Théorème global

Pour l'opérateur scalaire `T=A_N N+A_M M+B_N N'+B_M M'+E_N N''+E_M M''`, soient les coefficients suffisamment réguliers et `N,M∈C²([a,b])` strictement positifs. Pour une fonction test non négative `φ∈C²`, non nulle, avec `φ=φ'=0` aux deux bords, deux intégrations par parties donnent exactement

`∫ φ T dr = ∫ (Q_N N+Q_M M) dr`, où `Q_i=φ A_i-(φ B_i)'+(φ E_i)''`.

Si `Q_N,Q_M≥0` partout et `Q_N+Q_M>0` sur un intervalle ouvert, alors `T=0` n'admet **aucune** paire `N,M>0`. Ce critère n'exige **aucune borne de pente ou courbure** des lapses ; il inclut les coefficients `E_i` non nuls et évite les divisions par `B_i`. L'échec du test ne démontre pas l'existence.

## Témoin polynomial exact à deux lapses et E non nul

Fixer `R=17/20`, `x=r/R∈[0,1]`, `ε=1/100`, `φ=x²(1-x)²`. En coordonnées r, choisir `A_N=A_M=x²`, `B_N=R ε x³(1-x)³`, `B_M=-B_N`, `E_N=R² ε² x⁴(1-x)⁴`, `E_M=-E_N`. Les facteurs R garantissent la bonne transformation des dérivées vers x.

Avec `P=x⁴(1-x)²`, le calcul exact donne `Q_N=P-ε c1+ε² c2` et `Q_M=P+ε c1-ε² c2`, où `c1=5x⁴(1-x)⁴(1-2x)`, `c2=6x⁴(1-x)⁴[5(1-2x)²-2x(1-x)]`.

Pour `0≤x≤1`, `|1-2x|≤1`, `x(1-x)≤1/4`, `(1-x)²≤1` impliquent `|c1|≤5P`, `|c2|≤33P`. Donc **sur tout l'intérieur** `Q_N,Q_M≥(9467/10000)P>0`. L'opérateur JOUET n'admet aucune paire de lapses C² strictement positifs, même sans imposer les amplitudes aux bords, et malgré `B=O(ε)`, `E=O(ε²)` non nuls. Contrôle négatif : remplacer `A_M` par `-A_N` laisse `N=M=1` solution exacte ; la seule petitesse des B/E n'est donc pas suffisante.

## Reproductibilité et limites

Code et tests exacts SymPy publiés : `numerics/hr_b3c3d6_weak_dual_lapse_certificate.py` et `tests/test_hr_b3c3d6_weak_dual_lapse_certificate.py`. Localement, **5 unittest PASS, 0 FAIL**, `compileall` PASS. Contre-vérification SymPy séparée : **9 identités/conditions de bord et 6 inégalités rationnelles ponctuelles PASS** ; la borne uniforme repose sur les inégalités analytiques, non sur ces points. Tests non indépendants de l'énoncé.

Les anciens sondages numériques physiques Step58 sur Step55 suggéraient `A_N>0,A_M<0`, situation différente de ce témoin. **Aucun certificat dual physique n'a été construit.** Il faut d'abord exécuter les originaux SHA-authentifiés Step45/46/55/58 avec le candidat cubique aux rayons `1/4,1/2,7/10,17/20`, comparer les six coefficients affine/cubique, puis factoriser/enclore les coefficients et leurs dérivées sur l'intervalle, et seulement ensuite rechercher un φ admissible. Centre, vrai BVP positif à deux bords, Dirac six couples, charges/jauge temporelle, K=0/J=0, 4D/stabilité/observables : **NON PROUVÉS**. Branches main/v2-flrw et workflows intacts.

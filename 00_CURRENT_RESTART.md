# JANUS — REPRISE PRIORITAIRE : STEP68ad-C2c TERMINÉE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main`, ni `research/v2-flrw`, ni GitHub Actions/workflows désactivés.
**DERNIÈRE ÉTAPE TERMINÉE : 68ad-C2c (carte positive du shift, PAS encore opérateur temporel). NEXT : 68ad-C2d.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68AD_C2C_POSITIVE_SHIFT_CHART_AND_DENOMINATORS.md`, `numerics/hr_step68ad_c2c_shift_chart.py`, `research/reports/gate2b-step68ad-C2c-shift-chart.json`, `research/AUTOMATION_STATE.json`. Le checkpoint 68ad-C2b et TOUT l'historique antérieur sont conservés intégralement CI-DESSOUS.

## RÉSULTAT ORIGINAL : K/r² > 0, SHIFT RESCALÉ ET DÉNOMINATEUR f-DUST

**SIX SOURCES PHYSIQUES COMPLÈTES POSITIVEMENT AUTHENTIFIÉES PAR SHA-1 GIT RECALCULÉ SUR LE CONTENU LU VIA LE CONNECTEUR :** Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`, rapports Step68v `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`, Step68ac `16ae8dab3563c17134e4e20f886fb7306dc2e4ba`, Step68ad-B2 `ac961b5b83667a83497497d22a701c24584cb561`. Le conteneur n'a toujours pas de clone GitHub ; ce contrôle a été exécuté via le connecteur, avec SHA-1 JavaScript indépendant.

**IDENTITÉ EXACTE DU VRAI Step58/68o :**
```
s=r² ; y=Lf/Lg ; q(y)=b1+2*b2*y+b3*y²
K/r²=m2*mg*Lg³*Lf*q(y), r>0 (prolongement régulier en 0)
0.23384592478391242 < K/r² < 0.23385629318172435
|z|<=1/8000 ; 4.276130247104033 < r² Z_D < 4.27631997831076
|r² Z_K| < 0.000534539997289
rho_f denominator=beta_f+s*Ffac*KF*Lf >=1
```
Bornes **rationnelles exactes** dans le certificat JSON ; les décimales affichées sont indicatives. La preuve du continuum utilise la monotonie rationnelle de `q(y)` sur `y>=1/2` et les signes authentifiés `U<0, KF<0`. **ATTENTION : K(0)=0 et le Z_D NON rescalé diverge comme 1/r² au centre** ; il faut factoriser les variations avant la limite, sans conclure à une singularité physique. Sur les 7 cellules positives, K>0.

**12 TESTS LOCAUX RÉELLEMENT EXÉCUTÉS : 12 PASS, 0 FAIL**, `cd /mnt/data/janus_c2c && PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2c_shift_chart.py` (0,07 s). Il s'agit d'un certificat algébrique rationnel autonome, **PAS d'une exécution des opérateurs Step58/60** ; la CLI qui vérifie les fichiers originaux dans un clone complet n'a pas été exécutée localement.

**QUATRE FICHIERS PUBLIÉS, RELUS ET OCTET-IDENTIQUES AUX FICHIERS LOCAUX TESTÉS :**
- `numerics/hr_step68ad_c2c_shift_chart.py` — blob `7318b33d7bb1a982e9dc8d1c2780470887c919ed`
- `tests/test_hr_step68ad_c2c_shift_chart.py` — blob `719bda24064315094e1a86142f3637a46f591809`
- `research/reports/gate2b-step68ad-C2c-shift-chart.json` — blob `723e98fd5b490f92c3781d87477c7d8c24a3918c`
- `research/STEP68AD_C2C_POSITIVE_SHIFT_CHART_AND_DENOMINATORS.md` — blob `3781f6b76a791e7e7fd2e352f3c179cf2f080f5f`

**NEXT 68ad-C2d :** utiliser les sept boîtes C2b `Jet([U,U_s,U_ss/2,U_sss/6])` avec conversion outward `old.I.hull`, injecter dans l'original Step68o sans le modifier, exécuter le vrai Step58 non-frozen-shift et le quotient Step60 ; si les bornes contiennent zéro, garder INCOMPLETE et traiter explicitement les corrélations et la factorisation r². Les 7 signes temporels restent PENDING ; rang Dirac, lapses/bords, J/K, NON-IBP, BD, dynamique 4D et observables restent ouverts.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE COMPLET CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-C2b TERMINÉE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main`, ni `research/v2-flrw`, ni les workflows/Actions GitHub désactivés.
**ÉTAPE TERMINÉE : 68ad-C2b (boîtes d'entrée rationnelles, PAS évaluation temporelle). NEXT : 68ad-C2c.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68AD_C2B_SEVEN_CENTER_SAFE_INPUT_BOXES.md`, `numerics/hr_step68ad_c2b_center_boxes.py`, `research/reports/gate2b-step68ad-C2b-center-safe-input-summary.json`, `research/AUTOMATION_STATE.json`. Tous les checkpoints antérieurs sont conservés intégralement CI-DESSOUS.

## RÉSULTAT NOUVEAU — 7 CELLULES D'ENTRÉE PHYSIQUES RIGOUREUSES, SANS DIVISION PAR s

Les trois rapports physiques originaux sont identifiés et lus via GitHub : Step68v `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`, Step68ac `16ae8dab3563c17134e4e20f886fb7306dc2e4ba`, Step68ad-B2 `ac961b5b83667a83497497d22a701c24584cb561`. Leur contenu établit, conditionnellement à la branche analytique Step49, le tube `|U-Ustar|<=s³/10^7` et les bornes des dérivées U_s, U_ss, U_sss sur `0<=s<=1/1024`.

**NOUVELLE APPLICATION EXACTE FRACTION :** 7 cellules fermées couvrant sans lacune `r∈[1/64,1/32]`, extrémités `1/64,1/56,9/448,5/224,11/448,3/112,13/448,1/32`. Intersecter la barrière cubique avec le tube de monotonie U_s>0 donne :
- largeur MAX des boîtes U `5349668327184482945967454922219/50352619520000000000000000000000000000` ≈ `1.0624409173110848e-7`;
- erreur MAX de la seule barrière cubique `1/10737418240000000` ≈ `9.313225746154785e-17`;
- sur chacune des 7 cellules : `U<0, U_s>0, U_ss<0, U_sss<0`, les dérivées sont des bornes historiques IMPORTÉES, PAS différentiées de l'intervalle U;
- `r=0` également supporté par les formules, sans `1/s`.

Les dix profils canoniques non-horloges de l'original Step68o sont des compositions algébriques de `s,U,G(s,U)` et de `jet_geometry(s)` : le troisième jet de chacun n'exige pas `U_ssss`, sous réserve de dénominateurs non nuls. Le prochain calcul doit utiliser `Jet([U,U_s,U_ss/2,U_sss/6])` puis le vrai Step58/60, sans changer le Step68o original.

**16 TESTS RÉELLEMENT EXÉCUTÉS : 16 PASS, 0 FAIL, 2.18s** dans `/mnt/data/janus_c2b`, `PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2b_center_boxes.py`. Tests de fractions exactes, partition, centre, signes, provenance négative (tamper), règles de chaîne symboliques, dépendance d'ordre 3. **LIMITATION** : ces tests utilisent des champs rationnels recopiés des rapports lus via le connecteur GitHub ; le conteneur n'a pas DNS GitHub, donc pas de relecture LOCALE positive des trois rapports complets. `load_pinned()` exige néanmoins leurs octets SHA exacts en clone complet et doit être rejoué. Aucune exécution du vrai Step58/60 ; les sept signes temporels restent PENDING.

**FICHIERS PUBLIÉS ET RELUS SHA OCTET IDENTIQUES :**
- `numerics/hr_step68ad_c2b_center_boxes.py` — `94928e285f7e04deaf546abbeb9d3f05db33b213`.
- `tests/test_hr_step68ad_c2b_center_boxes.py` — `ae95668d5401df63c74fe22380b00fdc561fb426`.
- `research/reports/gate2b-step68ad-C2b-center-safe-input-summary.json` — `a131c60c221a9f54f9437b932dd44e04eddd2398`.
- `research/STEP68AD_C2B_SEVEN_CENTER_SAFE_INPUT_BOXES.md` — `6c4fed04e581ef7fc984f6f6d348b74be00a5bab`.

**NEXT 68ad-C2c :** (1) reconstituer les 3 rapports complets et vérifier leurs blobs localement ; (2) convertir les boîtes rationnelles en `old.I` sortants, les injecter dans le vrai Step68o via un nouveau module sans `_ode_coeff=(G-2U)/(2s)` ; (3) exécuter `jet_geometry`, `jet_G`, f-dust, les 12 jets, puis le vrai Step58 et quotient Step60 non-frozen-shift sur les 7 cellules ; (4) si signe non séparé de zéro, conserver INCOMPLETE et raffiner sans faux certificat ; (5) poursuivre vers r=0, rang Dirac, lapses, bords, jauge, J/K, NON-IBP, BD, cosmologie 4D.

**POINT DE REPRISE PRÉFIXÉ, HISTORIQUE COMPLET CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-C2a TERMINÉE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main`, ni `research/v2-flrw`, ni les workflows/Actions GitHub désactivés.
**ÉTAPE VALIDÉE : 68ad-C2a. PROCHAINE ÉTAPE EXACTE : 68ad-C2b.**
**STATUT SCIENTIFIQUE INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE D'ABORD** `research/STEP68AD_C2A_ALL_TWELVE_CANONICAL_PARITY_LEMMA.md`, `numerics/hr_step68ad_c2a_all_canonical_parity.py`, `research/reports/gate2b-step68ad-C2a-canonical-parity.json`, puis `research/AUTOMATION_STATE.json`. Tous les checkpoints antérieurs restent intégralement CI-DESSOUS.

## NOUVEAU RÉSULTAT RÉEL — LEMME EXACT POUR LES 12 JETS CANONIQUES, PAS ENCORE TEMPOREL

La source originale Step68o, blob `c99caebc17f243784450ddff94fb061767e6d8e7`, a été lue, ainsi que le Step58 temporel complet non-frozen-shift (`802c23aebd41780d8c462f1aa1711707fe4ee88f`) et Step60 quotient des contraintes (`9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`). L'ancien `_ode_coeff` de Step68o utilise `(G-2U)/(2s)` et souffre d'un élargissement d'intervalles près du centre.

**DÉMONSTRATION SYMBOLIQUE EXACTE (SymPy) DES 12 PROFILS DE PARITÉ :**
- `Lg,Lf` : F(s) ; `Sg,Sf,pSg,pSf` : rF(s) ; `pLg,pLf,pg,pf` : r²F(s) ; `tg,tf` : horloges dont t'=r k L(s), avec t(r0) valeur de jauge ponctuelle.
- Pour `F(s)` : `X'=2rF_s ; X''=2F_s+4sF_ss ; X'''=r(12F_ss+8sF_sss)`.
- Pour `rF(s)` : `X'=F+2sF_s ; X''=r(6F_s+4sF_ss) ; X'''=6F_s+24sF_ss+8s²F_sss`.
- Pour `r²F(s)` : `X'=2r(F+sF_s) ; X''=2F+10sF_s+4s²F_ss ; X'''=r(24F_s+36sF_ss+8s²F_sss)`.
- Horloges : `t''=k(L+2sL_s)`, `t'''=rk(6L_s+4sL_ss)`.
- **AUCUNE DIVISION PAR r OU s** ; 12/12 champs et leurs dérivées 0..3 ont un prolongement régulier au centre, SOUS RÉSERVE que leurs profils F possèdent les dérivées nécessaires. L'identité pLf'''/r de Step68ad-C1 est retrouvée exactement.

**15 NOUVEAUX TESTS RÉELLEMENT EXÉCUTÉS : 15 PASSED EN 0,74 s ; 0 FAIL**, `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2a_all_canonical_parity.py` dans `/mnt/data/janus68adC2a`. Tests de chaîne symbolique indépendante, polynômes rationnels, r=0, horloges, complétude des 12 champs et entrées altérées. Ce ne sont PAS des tests numériques du Step58 original.

**FICHIERS PUBLIÉS ET BLOBS GitHub RELUS, IDENTIQUES AUX OCTETS TESTÉS LOCALEMENT :**
- `numerics/hr_step68ad_c2a_all_canonical_parity.py` — `bf673187d6b923193c846749b15c3e291ef3ac9f`
- `tests/test_hr_step68ad_c2a_all_canonical_parity.py` — `e465fcb265a76998d6db662836b500e3b8ba9d10`
- `research/reports/gate2b-step68ad-C2a-canonical-parity.json` — `1f0ecef8fa1a8dbf9d8f38c2a9a5609dc0bdf5f7`
- `research/STEP68AD_C2A_ALL_TWELVE_CANONICAL_PARITY_LEMMA.md` — `66614703349b8a50483b0aec94c9ff0feaf5ed71`

**LIMITES :** aucune certification de F_s,F_ss,F_sss pour les NEUF autres profils, aucun A_N/r² ou A_M/r² évalué, aucun des sept intervalles temporels en attente certifié. La vérification positive locale des sources originales n'a pas eu lieu : le conteneur n'a pas de DNS GitHub (`git ls-remote` échoue), mais le connecteur GitHub permet les lectures et les écritures. Ne pas confondre le lemme cinématique avec un théorème de rang Dirac.

**NEXT 68ad-C2b :** reconstruire octet-identiques les vrais Steps68n/68o/58/60 via GitHub ; former dans la variable s les dix profils F,F_s,F_ss,F_sss par l'original `Jet` Step68n à partir des tubes prouvés Step68v/B2, en particulier `rhof` et `psf` ; injecter dans les 12 jets réguliers ; évaluer le vrai opérateur Step58/60 non-frozen-shift sur les sept cellules PENDING [1/64,1/32], puis r→0. Si dépendances d'intervalles trop larges, garder le statut INCOMPLETE. Les contraintes temporelles, rang complet, lapses/bords/jauge, J/K, oracle NON-IBP et cosmologie 4D restent ouverts.

**CHECKPOINT PRÉFIXÉ, HISTORIQUE COMPLET CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-C1 TERMINÉE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE EN ÉCRITURE :** research/gate2b-nonhomothetic-transfer. **NE JAMAIS MODIFIER** main, research/v2-flrw, ni GitHub Actions/workflows désactivés.
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
**DERNIÈRE ÉTAPE TERMINÉE : 68ad-C1. PROCHAINE ÉTAPE EXACTE : 68ad-C2.** Ne pas recommencer 68ad-B2.

**LIRE EN PREMIER :** research/STEP68AD_C1_ORIGINAL_CANONICAL_MOMENTUM_THIRD_JET.md, numerics/hr_step68ad_c1_center_momentum_jet.py, research/reports/gate2b-step68ad-C1-original-canonical-pLf-third-jet.json et research/AUTOMATION_STATE.json. L'historique complet reste CI-DESSOUS.

## NOUVELLE CONSÉQUENCE MATHÉMATIQUE ORIGINALE — TROISIÈME JET CANONIQUE f AU CENTRE

À partir des TROIS rapports originaux GitHub authentifiés (Step68v U_s, Step68ac U0, Step68ad-B2 U_ss/U_sss), sur TOUT r∈[0,1/32] : le véritable moment canonique radial f satisfait pLf(r)=r² U(r²). Dérivation symbolique EXACTE :

    pLf'/r   = 2(U+s U_s)
    pLf''    = 2U+10s U_s+4s² U_ss
    pLf'''/r = 24U_s+36s U_ss+8s² U_sss
    U(r²)'''/r = 12U_ss+8s U_sss,  s=r².

**NOUVEAUX INTERVALLES RATIONNELS CERTIFIÉS CONDITIONNELS À LA BRANCHE PHYSIQUE HISTORIQUE :**

    pLf'/r   ∈ [-0.010504853794,-0.010501768851] <0
    pLf''    ∈ [-0.010504853794,-0.010495598966] <0
    pLf'''/r ∈ [ 0.018945615724, 0.018953886023] >0
    U(r²)'''/r∈[-0.000242642608,-0.000240911976] <0

**Fractions exactes** dans le rapport JSON. Les quotients par r sont prolongés analytiquement jusqu'au centre, SANS division d'intervalles contenant zéro. pLf'''(0)=0, pLf''(0)=2U0<0, et pLf'' croît strictement pour r>0. C'est une avancée sur **UN SEUL DES DOUZE JETS CANONIQUES**, PAS encore sur le temps.

**Rapports GitHub vérifiés :** 68v d83a3b80862a2e990a4c4879ec8745a4e91c8b34 ; 68ac 16ae8dab3563c17134e4e20f886fb7306dc2e4ba ; B2 ac961b5b83667a83497497d22a701c24584cb561. Les sources temporelles Step57/58/60/68o ont été lues via GitHub, SHA respectifs bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f, 802c23aebd41780d8c462f1aa1711707fe4ee88f, 9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509, c99caebc17f243784450ddff94fb061767e6d8e7 ; **NON EXÉCUTÉES LOCALEMENT** (pas de clone, pas de réseau externe container).

**15 TESTS RÉELLEMENT PASSÉS EN 0,61s** (Python Fraction et SymPy, sur champs rationnels des trois rapports lus via connecteur), 0 FAIL. Il s'agit des tests du NOUVEAU POST-TRAITEMENT ALGÉBRIQUE, PAS de la réexécution B2 ni d'un certificat temporel. Test de rejet de rapports altérés exécuté ; lecture complète des trois rapports avec vérification SHA dans un clone reste à rejouer.

**FICHIERS NOUVEAUX PUBLIÉS, GIT BLOBS VÉRIFIÉS IDENTIQUES AUX OCTETS LOCAUX EXÉCUTÉS :**
- numerics/hr_step68ad_c1_center_momentum_jet.py — 08f6d13b2f799705328f10f12d80433617f16ef8
- tests/test_hr_step68ad_c1_center_momentum_jet.py — a367c80566a6bec9119201a23136f597619ee3a7
- research/reports/gate2b-step68ad-C1-original-canonical-pLf-third-jet.json — 62f98abd0fe18004b2a6654e1d422d02cfe025aa
- research/STEP68AD_C1_ORIGINAL_CANONICAL_MOMENTUM_THIRD_JET.md — 87925fee61f7236fa8e4616aadb61f23f983606f

**NEXT STEP68ad-C2 :** reconstruire/authentifier le vrai Step58/60/68o et les 12 jets canoniques ; remplacer dans le Step68o la division par s de _ode_coeff par le jet régulier issu des tubes B2 (U,Us,Uss,Usss) et la formule C1 ; évaluer A_N/r² et A_M/r² sur les sept cellules PENDING [1/64,1/32], puis r→0. Préserver Fz=0, réponse du shift NON GELÉ, quotient complet Step60 ; arrêter honnêtement sur toute dépendance d'intervalle excessive. Aucun signe temporel original nouveau ni rang de Dirac n'a été calculé en C1.

**POINT DE REPRISE DURABLE AJOUTÉ ; TOUS LES CHECKPOINTS ANTÉRIEURS CONSERVÉS INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-B2 VRAIE PHYSIQUE CERTIFIÉE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. NE JAMAIS modifier `main`, `research/v2-flrw`, ni GitHub Actions/workflows désactivés.
**STATUT SCIENTIFIQUE INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
**DERNIÈRE ÉTAPE TERMINÉE : 68ad-B2 ; PROCHAINE ÉTAPE EXACTE : 68ad-C.** NE PAS recommencer 68ad-B1 ou 68ad-B2.

**LIRE D'ABORD :** `research/STEP68AD_B2_ORIGINAL_PHYSICAL_CONTINUUM_HIGHER_JETS.md`, `numerics/hr_step68ad_b2_physical_center_higher_jets.py`, `research/reports/gate2b-step68ad-B2-original-G-Uss-Usss.json`, `research/AUTOMATION_STATE.json`. TOUS les checkpoints historiques sont conservés intégralement CI-DESSOUS.

## RÉSULTAT SCIENTIFIQUE NOUVEAU ET RÉELLEMENT EXÉCUTÉ — ORIGINAL G PHYSIQUE

Les **six originaux** du Hamiltonien six couples canoniques Steps45/46/55norm/55barrier/68l/68n ont été reconstitués depuis GitHub **OCTET POUR OCTET** et SHA-authentifiés ; les deux programmes originaux 68ad-A/B1 et rapports historiques 68v/68ac également. Contrairement au dernier run B1, le vrai `physical_R2_global` et les quatre jets Step68n du vrai G ont **RÉELLEMENT TOURNÉ** sur le continuum `s∈[0,1/1024]` (`r∈[0,1/32]`), avec 32 cellules rationnelles fermées et arithmétique entière sortante 10^-28.

**NOUVELLE PREUVE PHYSIQUE SPATIALE (conditionnelle aux hypothèses historiques Step49/68v) :**

```
R2(s)    ∈ [-1.414170375015186e-4, -1.406541559177554e-4] < 0
U_ss(s)  ∈ [-2.022016433671329e-5, -2.007599805707252e-5] < 0
R3(s)    ∈ [-7.320689826385639e-7, -6.226026282646365e-7] < 0
U_sss(s) ∈ [-8.139651115656399e-8, -6.913132664403898e-8] < 0
pour TOUT s∈[0,1/1024], sans trou, incluant s=0.
```

Les **FRACTIONS RATIONNELLES EXACTES** et les 32 lignes de R2 + 32 lignes de R3 figurent dans le JSON machine authentifié, pas dans ces seules approximations. Step68ad-A transport positif `2s y'+a_n y=R_n` (`a_n=2n+2-G_U>0`) transforme R2→U_ss puis R3→U_sss sans division par s. Le certificat contient les valeurs centrales `2U2` et `6U3`. Avec `U_s>0` historique, U est **croissante et strictement concave** et U_ss **strictement décroissante** sur ce domaine.

**THÉORÈME EXACT SUPPLÉMENTAIRE :** sur le vrai G symbolique original `degree_U(G)=2`, `G_UUU=0` IDENTIQUEMENT et `G_UU=s*C(s)` EXACTEMENT. SymPy vérifie l'identité en soustrayant la factorisation fermée. L'intervalle entier original sur tout `s∈[0,1/1024]` prouve `0.87576275<C(s)<0.87591186` ; donc `G_UU>0` pour tout `s>0`. Voir la formule exacte et les fractions dans l'audit/JSON.

**TESTS RÉELLEMENT EXÉCUTÉS :** 16 nouveaux tests Step68ad-B2 **PASS** (16,26 s, 0 FAIL final), dont le vrai Hamiltonien original, les identités exactes Step45/46, factorisation G, signes continus U_ss/U_sss, contrôle des valeurs centrales, cellules 32 et 64, altération SHA, comparaison au JSON machine. Un premier run avait 1 échec de TEST mal formulé (il demandait la contenance d'un intervalle indépendant au lieu de leur intersection non vide) ; corrigé, suite complète relancée 16 PASS. **Original Step55 256 cellules rejoué PASS** ; tests de raffinement physique B2 à 64 et **128 cellules** également exécutés, signes négatifs stables, intervalles plus serrés (128 : U_ss ~[-2.017945e-5,-2.011665e-5], U_sss ~[-7.690428e-8,-7.360654e-8]). Ne PAS additionner les anciens tests 18 B1 ou 19 A comme s'ils avaient été rejoués.

**FICHIERS RÉELLEMENT PUBLIÉS ET SHA Git blob identiques aux octets locaux exécutés :**

- `numerics/hr_step68ad_b2_physical_center_higher_jets.py` blob **89ce02af12145eb8ab6bdcc354649571dd5da179**
- `tests/test_hr_step68ad_b2_physical_center_higher_jets.py` blob **5e2b5f297fbef78e38f05c76aebd05f8f4b2ee02**
- `research/reports/gate2b-step68ad-B2-original-G-Uss-Usss.json` blob **ac961b5b83667a83497497d22a701c24584cb561**
- `research/STEP68AD_B2_ORIGINAL_PHYSICAL_CONTINUUM_HIGHER_JETS.md` blob **d49e30ce7093927480dcac6e8f962556eebe963c**
- `research/AUTOMATION_STATE.json` blob **a5cbe90cdd891f2eb44230de5460262c62bf6b6f**

## NEXT EXACT ACTION : STEP68ad-C — TEMPORAL ORIGINAL, PAS UN NOUVEAU POLYNÔME JOUET

1. **AUTHENTIFIER** les sources originales Steps57/58/60/68o et le vrai opérateur temporel non-frozen-shift Step58, à leurs Git blob SHA ; préserver les huit sources physiques et les deux rapports originaux déjà certifiés. Reprendre sur GitHub le dernier HEAD, jamais un ancien checkpoint.
2. Dans les 12 vrais jets canoniques, substituer **les tubes rigoureux U_ss/U_sss** de B2 (ou des tubes locaux resserrés par sous-cellule), sans diviser naïvement par `s` ni différencier les bornes de U/Us. Exploiter `G_UUU=0` et `G_UU=s*C(s)` pour améliorer les bornes si nécessaire.
3. Évaluer `A_N/r²,A_M/r²` du VRAI Step58/60 sur les **sept cellules PENDING r∈[1/64,1/32]**, puis anneau plus intérieur et centre r→0. Vérifier toutes les hypothèses, signes et collisions d'intervalles ; si les signes ne sont pas certifiés, déclarer précisément le blocage.
4. Même en cas de signes temporels favorables, **NE PAS FERMER** le GATE sans rang Dirac complet, lapses/bords/jauge, exceptions J/K, oracle indépendant NON-IBP, stabilité BD et validation 4D. Documenter et publier chaque vraie avancée.
5. PRÉFIXER CE fichier après l'avancée suivante SANS SUPPRIMER aucun ancien texte ; actualiser l'index machine, SHA, tests et HEAD. Ne jamais faire de commit artificiel.

**POINT DE REPRISE PERMANENT MIS À JOUR ; HISTORIQUE COMPLET CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-B1 OUTIL ALGÉBRIQUE TERMINÉ (2026-10-26)

**BRANCHE UNIQUE EN ÉCRITURE** `research/gate2b-nonhomothetic-transfer`. Ne jamais modifier `main`, `research/v2-flrw` ni les workflows GitHub Actions désactivés.
**ÉTAT SCIENTIFIQUE INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
**DERNIÈRE SOUS-ÉTAPE TERMINÉE : 68ad-B1. PROCHAINE SOUS-ÉTAPE : 68ad-B2.**

**LIRE EN PREMIER** `research/STEP68AD_B1_DIRECTIONAL_POLARIZATION_HARNESS.md`, puis `numerics/hr_step68ad_b_directional_polarization.py`, `tests/test_hr_step68ad_b_directional_polarization.py` et `research/AUTOMATION_STATE.json`. TOUS les anciens checkpoints 68ad-A/68ac/... sont intégralement conservés CI-DESSOUS.

## NOUVELLE PREUVE EXACTE, SANS NOUVELLE CERTIFICATION PHYSIQUE

Pour le VRAI G fixe Step45/46/55, le code nouvellement publié permet de calculer TOUTES les dérivées partielles mixtes de degré total ≤3 par quatre appels au moteur original de Taylor intervalle Step68n `jet_G` : `A(t)=G(s+t,U)`, `B(t)=G(s,U+t)`, `C(t)=G(s+t,U+t)`, `D(t)=G(s+t,U-t)`. En notant `X_k=[t^k]X(t)` :

```
G_s=A1, G_U=B1, G_ss=2A2, G_sU=C2-A2-B2, G_UU=2B2,
G_sss=6A3, G_ssU=C3-D3-2B3, G_sUU=C3+D3-2A3, G_UUU=6B3.
R2=G_ss+2 G_sU U_s+G_UU U_s².
R3=G_sss+3 G_ssU U_s+3 G_sUU U_s²+G_UUU U_s³
   +3 G_sU U_ss+3 G_UU U_s U_ss.
```

Identités EXACTES démontrées par polarisation et testées indépendamment en SymPy sur dix monômes et des polynômes mixtes, plus oracle Fraction d'intervalles vérifiant les inclusions. **18 TESTS RÉELLEMENT PASSÉS EN 1,88s, zéro échec final.** Un premier run avait 1 FAIL dû à un import avant validation des entrées ; corrigé, suite complète relancée à 18 PASS.

**Code réellement testé ET PUBLIÉ SHA IDENTIQUE** `numerics/hr_step68ad_b_directional_polarization.py` blob `3d075699fb8266ddce2ee9b370afa85cb17f2c73`.
**Tests réellement testés ET PUBLIÉS SHA IDENTIQUE** `tests/test_hr_step68ad_b_directional_polarization.py` blob `6e1b4b81fe1e5b8588c6c9639829727da6eb4d21`.
**Audit** `research/STEP68AD_B1_DIRECTIONAL_POLARIZATION_HARNESS.md` blob `09f56801dd01b78c8213d70aa505acb034c4840b`.
**État machine** `research/AUTOMATION_STATE.json` mis à jour et relu, blob `c5e779869f80c5a67de3e7abc216ef12298558b3`.

**ATTENTION CRITIQUE :** le runtime de cette session ne possédait pas le clone Python du dépôt (DNS `github.com` impossible dans container) ; GitHub a été consulté ET écrit via son connecteur, mais `physical_G_partials`, `physical_R2_global` et les originales Steps45/46/55/68n n'ont PAS été exécutés localement. Les 18 tests valident les IDENTITÉS et l'inclusion d'intervalles sur polynômes génériques, **PAS les bornes physiques de R2/U_ss/U_sss**. Le harnais original fail-closed vérifie Step68n blob `96370e0599748c6dc07faf339ab3646ae3474e7d`, sources Step45/46/55/68l et rapports Step68v/68ac ; son exécution sur tout `s∈[0,1/1024]` reste PENDING.

## NEXT EXACT ACTION : STEP68ad-B2 (NE PAS RÉPÉTER B1)

1. Dans un workspace avec les six sources Python physiques originelles et rapports SHA authentiques, exécuter `physical_R2_global('research/reports',cells=32)`. Il parcourt tout le centre `0<=s<=1/1024` avec les tubes U et U_s prouvés Step68v, appelle 4 jets de G original par cellule, calcule R2 puis U_ss via théorème positif Step68ad-A. Mesurer les bornes et ajuster le nombre de cellules en cas d'effet de dépendance ; produire et TESTER le JSON réel, sans inventer de résultat.
2. Avec U_ss réellement certifié, calculer R3 et U_sss, puis le vrai opérateur temporel Step58/60, les sept cellules PENDING [1/64,1/32], et la zone centrale ; préserver les hypothèses des 12 jets canoniques.
3. Maintenir le rang de Dirac, lapses/bords/jauge, exceptions K/J, NON-IBP et 4D OUVERTS. Aucun verdict cosmologique validé.
4. Préfixer de nouveau CE fichier après toute avancée, conserver l'historique, mettre à jour l'index `research/AUTOMATION_STATE.json`, relire les blobs et HEAD GitHub. Si exécution physique impossible, rapporter explicitement le blocage sans faux certificat.

**CHECKPOINT NOUVEAU PRÉFIXÉ ; HISTORIQUE INTÉGRAL CI-DESSOUS SANS SUPPRESSION.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-A TERMINÉE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE EN ÉCRITURE** `research/gate2b-nonhomothetic-transfer`. NE PAS modifier `main`, `research/v2-flrw` ni les workflows/Actions GitHub désactivés.
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED**. **PROCHAINE SOUS-ÉTAPE EXACTE : 68ad-B** (ne PAS relancer 68ac ni 68ad-A).

## RÉSULTAT NOUVEAU : TRANSPORT DÉRIVÉ ORIGINAL SANS SINGULARITÉ ARTIFICIELLE

**LIRE EN PREMIER** `research/STEP68AD_A_DESINGULARIZED_PHYSICAL_DERIVATIVE_TRANSPORT.md` et `research/reports/gate2b-step68ad-A-derivative-transport.json` ; puis le checkpoint 68ac intégralement conservé CI-DESSOUS. Les deux rapports historiques Step68v et Step68ac ont été reconstruits localement **octet pour octet** et vérifiés à leur SHA Git respectifs `d83a3b80862a2e990a4c4879ec8745a4e91c8b34` et `16ae8dab3563c17134e4e20f886fb7306dc2e4ba`. La chaîne originale Steps45/46/55 est ainsi traçable. Les codes Step57/58/60/68o ont été **relus sur GitHub mais NON exécutés** dans cette session.

Pour la VRAIE EDO physique `2s U_s=G(s,U)-2U`, les identités symboliques EXACTES (SymPy, n=1,2,3,4) donnent :

```
2s*(U^(n))_s + a_n(s)*U^(n) = R_n(s),
a_n(s)=2n+2-G_U(s,U(s)),
R_n=d^n[G(s,U(s))]/ds^n-G_U(s,U(s))*U^(n),
R_n ne contient PAS U^(n) (plus haute dérivée recherchée).
R1=G_s;
R2=G_ss+2 G_sU U_s+G_UU U_s²;
R3=G_sss+3G_ssU U_s+3G_sUU U_s²+G_UUU U_s³+3G_sU U_ss+3G_UU U_s U_ss.
```

**THÉORÈME EXACT DE COMPARAISON (démontré)** : pour `2s y'+a(s)y=R(s)` avec a(s) strictement positif sur [0,S] et y bornée au centre, y(s) est une **moyenne positive de R(t)/a(t)**, poids normalisé à 1. Donc un intervalle rigoureux [Rlo,Rhi] sur le DOMAINE ENTIER et un intervalle 0<amin<=a<=amax donnent `y(s) ∈ range([Rlo,Rhi]/[amin,amax])` pour TOUT s∈[0,S]. **AUCUNE division par s=0, aucun échantillonnage.**

**CERTIFICATION PHYSIQUE ORIGINALE RÉELLE** : Step68v fournit G_U sur le continuum s∈[0,1/64] dans [-1.00608535216533...,-0.99386192647064...], et donc a1∈(4.99386,5.00609), a2∈(6.99386,7.00609), a3∈(8.99386,9.00609), a4∈(10.99386,11.00609). Bornes rationnelles EXACTES dans JSON. Le transport ne peut pas résonner sur ce chart aux quatre premiers ordres. Les signes EXACTS au CENTRE de R_n(0)=(2n+3)n!U_n sont +,−,−,− pour n=1,2,3,4 ; valeurs en fractions dans JSON.

**VERROU MAJEUR TOUJOURS OUVERT** : il MANQUE des enclosures CONTINUES de `R2(s),R3(s),R4(s)` calculées sur le G physique fixe. Le théorème ne constitue PAS un certificat de U_ss/U_sss à rayon positif ; il ne prouve PAS les signes des coefficients temporels Step58 ni le rang Dirac. **NE JAMAIS EXTRAPOLER** les signes de Rn(0) au voisinage sans une preuve uniforme.

**CODE PUBLIÉ ET TESTÉ** `numerics/hr_step68ad_center_derivative_transport.py` blob Git `3768d309f008391813c5fd70302ff487141afe1b`.
**TESTS PUBLIÉS ET TESTÉS** `tests/test_hr_step68ad_center_derivative_transport.py` blob `79946d5f7220f7445676f27b68a92c0be30bf98e`.
**RAPPORT MACHINE CLI PUBLIÉ ET TESTÉ** `research/reports/gate2b-step68ad-A-derivative-transport.json` blob `6be5cc1e9cb61479cf4b9dd897aa28105195d4f5`.
**AUDIT SCIENTIFIQUE** `research/STEP68AD_A_DESINGULARIZED_PHYSICAL_DERIVATIVE_TRANSPORT.md` blob `4e39bf191ce858ef647f731945cd4c2abb19cfe0`.
**19 TESTS NOUVEAUX RÉELLEMENT PASSED EN 1.21s**, zéro échec, avec reports Step68v/ac reconstitués à SHA identique. Les TROIS nouveaux fichiers source/test/JSON publiés ont été relus GitHub et leurs blob SHA comparés OCTET IDENTIQUES aux fichiers locaux exécutés. Les tests historiques Step68ac (44) ne sont PAS rejoués dans cette session, ne pas additionner comme si exécutés.

## NEXT EXACT ACTION : STEP68ad-B

1. Authentifier originaux 45/46/55/68n et les reports 68v/68ac ; utiliser l'AD MULTIVARIÉE sur le G original pour borner `G_ss,G_sU,G_UU` et R2 sur s∈[0,1/1024] avec les vrais tubes U,Us (68v/x/z). Appliquer le théorème positif pour U_ss.
2. Borner `G_sss,G_ssU,G_sUU,G_UUU` et R3 avec U_ss prouvé, puis U_sss ; si besoin quatrième ordre et R4. Utiliser des cellules rationnelles sortantes, sans différencier des enveloppes ni diviser des intervalles par s.
3. Reconstruire les 12 jets canoniques et tester le VRAI Step58/60 temporel, normalisé A_N/r² et A_M/r² sur les 7 cellules PENDING [1/64,1/32], puis [1/128,1/64], puis le centre. Garder le rang Dirac et 4D ouverts.
4. Sauvegarder chaque résultat dans code/tests/JSON/audit et PRÉFIXER CE JOURNAL, conserver intégralement tout historique ; actualiser `research/AUTOMATION_STATE.json`, vérifier SHA GitHub et HEAD.

**TOUS LES ANCIENS CHECKPOINTS 68ac, 68ab, 68aa, ... SONT CONSERVÉS SANS SUPPRESSION CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ac TERMINÉE (2026-10-25)

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer` ; **NE JAMAIS TOUCHER** `main`, `research/v2-flrw`, ni GitHub Actions/workflows que l'utilisateur a désactivés.
**STATUT SCIENTIFIQUE INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE IMMÉDIATEMENT** `research/STEP68AC_AUTHENTIC_ORIGINAL_PHYSICAL_U4_CENTER_CERTIFICATE.md`, puis l'audit Step68ab intégralement conservé CI-DESSOUS. **REPRENDRE À STEP68ad**. GitHub est le journal permanent, le workspace local `/mnt/data/janus-step68ac` est TRANSITOIRE.

## NOUVEAU RÉSULTAT PHYSIQUE ORIGINAL — VRAI U4 CERTIFIÉ

**SIX SOURCES PHYSIQUES ORIGINALES RECONSTITUÉES, GIT HASH BYTE-IDENTIQUE ET EXÉCUTÉES :** Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 global barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step68l `2a1ffc026a30abf41208b44a707dc869daf0929d`, Step68n `96370e0599748c6dc07faf339ab3646ae3474e7d`. Les reports Steps68u/v/y, le code/report Step68z et la source Step68aa sont également réauthentifiés via `authenticated_inputs()`, y compris l'intervalle U3 originel Step67b.

La **VRAIE fonction G physique** issue du Hamiltonien sphérique original Step45/46/55 est dérivée symboliquement, ~1048 opérations, **PAS un G alternatif du contre-modèle Step68ab**. Son identité centrale EXACTE, démontrée SymPy avant intervalle :

```
partial_U G(s,U)|_(s=0) = -Sfr0/Lf0 .
Sur le centre régulier Sfr0(0)=Lf0(0)>0 => G_U(0,U)=-1 EXACT.
U_n = [s^n]G(s,Σ_{k<n} U_k s^k)/(2n+3).
Dénominateurs pour n=1,2,3,4 : 5, 7, 9, 11.
```

**NOUVELLE BORNES RATIONNELLES CERTIFIÉES EXACTES POUR LA SOLUTION ORIGINALE :**

```
U4 ∈ [
 -3728419736053033407/10000000000000000000000000000,
 -3728419736052979197/10000000000000000000000000000
] ⊂ (-∞,0)
U4 ≈ -3.728419736053e-10
pLf(r)=r²[U0+U1r²+U2r⁴+U3r⁶+U4r⁸+O(r^10)]
pLf^(10)(0)=3628800*U4 ≈ -0.001352968953819 <0.
```

Méthode RIGOUREUSE : original Step68n `Jet` temporairement K=4 en MÉMOIRE, source inchangée, try/finally restaure K=3 ; arithmétique exacte d'intervalles entiers sortants Step55 à S=10^28, racines/quotients inclus ; d'abord récurrence U1..U4 depuis U0, puis calcul U4 avec intervalles hist. U1,U2 et intervalle prouvé Step67b U3, intersection; **ces deux usages du MÊME G sont deux inclusions compatibles, PAS des oracles indépendants**. Résidus de l'ODE originale sur cinq coefficients n=0..4 contiennent zéro. U1/U2 recouvrent les sources historiques, U3 recouvre Step67b. Original Step55 barrière spatiale **256 cellules effectivement RERUN** et POSITIF.

**SOURCE FINALE PUBLIÉE TESTÉE** `numerics/hr_step68ac_authentic_original_U4.py`, blob `a90b2d6d4882a0ff0aa810c5a320ba247f171a13`.
**TESTS FINAUX PUBLIÉS TESTÉS** `tests/test_hr_step68ac_authentic_original_U4.py`, blob `705108773b57f4f621ac7888a63359cb19e4429b`.
**RAPPORT MACHINE ORIGINAL** `research/reports/gate2b-step68ac-authentic-U4-report.json`, blob `16ae8dab3563c17134e4e20f886fb7306dc2e4ba`.
**AUDIT DÉTAILLÉ** `research/STEP68AC_AUTHENTIC_ORIGINAL_PHYSICAL_U4_CENTER_CERTIFICATE.md`.
**TESTS RÉELLEMENT EXÉCUTÉS ENSEMBLE : 44 PASSED EN 5.92s, zéro skip** : 15 Step68ac authentiques +29 régressions Step68ab/aa/z. Six fichiers originaux ET TROIS nouveaux fichiers source/test/JSON recontrôlés OCTET IDENTIQUES GitHub/local. AUCUNE assertion de l'exécution Steps57/58/60 ou d'un vrai coefficient temporel nouveau.

**NON RÉSOLU :** il s'agit du SEUL COEFFICIENT CENTRAL U4 (s=0) et de la barrière spatiale historique, PAS d'un reste Taylor C³ certifié sur 0<s<=1/1024, PAS d'encadrements temporels AN/r², AM/r² au-dessous de r=1/32, PAS d'un rang de Dirac complet ni d'une preuve de stabilité BD/4D.

## NEXT HARD RED : STEP68ad

1. Reconstruire/AUTHENTIFIER Steps57/58/60 et 68o originaux à leur SHA historiques depuis GitHub. Conserver l'exact G physique ci-dessus et ses 6 fichiers originaux inchangés.
2. Calculer rigoureusement les dérivées G_s,G_U,G_ss,G_sU,G_UU,... et des restes de U(s) à partir de CETTE fonction fixe pour `s ∈ [0,1/1024]`. Utiliser les séries renormalisées `h=(U-Ustar)/s³` et U4 signé ; **interdit** de différencier naïvement des bornes sur U,Us ou de diviser des intervalles non factorisés par s.
3. Obtenir inclusion entière de U_ss,U_sss et des 12 vrais jets canoniques; tester l'opérateur temporel original Step58 normalisé A_N/r²,A_M/r². Certifier les 7 cellules PENDING [1/64,1/32] et anneau [1/128,1/64], puis centre, ENTIÈREMENT sans trou.
4. Ensuite certificat complet lapses/bords/jauge et rang Dirac, exceptions K=0,J=0, vrai oracle NON-IBP, stabilité cosmologique 4D / observables. Maintenir GATE ouvert / JANUS-R non validé.

**CHECKPOINT NOUVEAU PRÉFIXÉ ; TOUS LES CHECKPOINTS ANTÉRIEURS RESTENT INTÉGRALEMENT CI-DESSOUS, SANS AMPUTATION.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ab TERMINÉE (2026-10-25)

**BRANCHE UNIQUE EN ÉCRITURE** `research/gate2b-nonhomothetic-transfer`. Ne jamais écrire dans `main`, `research/v2-flrw`, ni réactiver GitHub Actions/workflows OFF.
**ÉTAT DURABLE : GATE_2B OPEN ; JANUS_R NOT_VALIDATED**.

**LIRE D'ABORD** `research/STEP68AB_PROOF_HARNESS_HIGHER_JETS_NOT_FROM_SIGNED_BARRIERS.md`, puis la preuve Step68aa immédiatement ci-dessous. L'historique entier 68aa/68z/... est conservé SANS suppression. **REPRENDRE À STEP68ac.**

## STEP68ab — RÉSULTAT RIGOUREUX, NON-PHYSIQUE MAIS BLOQUANT UN FAUX RACCOURCI

Les certificats SHA-originaux Step68u (Fplus/Fminus'''/6), Step68v (F0'''/6 et G_U), Step68y (F0 signé), Step68z (cône h et U_s, G−Vstar), Step68aa (U3<0 et jets au point r=0) ne permettent **PAS, à eux seuls**, de borner U_sss au rayon fixé `smax=1/1024`.

Contre-modèle EXACT analytique qui conserve ces inclusions (mais NE REMPLACE PAS le G physique original) : c=milieu rationnel de U3 authentique, kappa=10^-7, eps=10^-11, `h_n=c+eps*(s/smax)^6*sin(n*s)/n`, `U_n=Ustar+s³*h_n`. Définir G_n(s,u) par interpolation cubique et exacte de ses trois courbes Ustar, Ustar±kappa*s³, et par l'EDO sur la courbe U_n ; G_n analytique et G_n,U~-1 sur tout le tube. Toutes les inégalités de sources originales ont été calculées exactement en Fraction et vérifiées strictement, les résidus F0/Fplus/Fminus sont même des constantes fois s³. Pourtant pour `n=2πk/smax`, `U_n'''(smax)−6c = eps*smax*(216−4π²k²)→−∞`. Ceci prouve la **non-déductibilité des jets à partir des certificats agrégés**, ABSOLUMENT PAS un problème avéré de la fonction physique G originale, qui est FIXE.

**RÉCURRENCE U4 EXACTE**, à évaluer sur VRAI G : `U4=[s^4]G(s,U0+U1*s+U2*s²+U3*s³)/(10-G_U(0,U0))`. Le développement polynomial de g_ij, avec dépendance vraie en U et facteur (10−g01), a été validé indépendamment par SymPy. Aucun g_ij ORIGINAL ni U4 numérique physiquement certifié dans cette session. L'opérateur temporel Step58, ses bornes AN/AM pour r<1/32 et le rang Dirac COMPLET restent NON CALCULÉS.

**CODE PUBLIÉ TESTÉ** `numerics/hr_step68ab_derivative_data_obstruction.py` blob `32c3a2172155bad361bc6c3d73bdec63fc27423d`.
**TESTS PUBLIÉS TESTÉS** `tests/test_hr_step68ab_derivative_data_obstruction.py` blob `5a790953779c81db7eb729948f078c9d3b682956`.
**RAPPORT MACHINE PUBLIÉ** `research/reports/gate2b-step68ab-derivative-data-obstruction.json` blob `fcef873c8d565bc9c326043906fb4efaa613d395`.
**AUDIT COMPLET** `research/STEP68AB_PROOF_HARNESS_HIGHER_JETS_NOT_FROM_SIGNED_BARRIERS.md`.
**29 TESTS RÉELLEMENT PASSED en 3.21s**, 12 Step68ab +17 regressions 68aa/68z, zéro skip ; origine 68u/v/y et sources 68aa/68z revérifiées par SHA, 3 NOUVEAUX blobs Git égaux aux fichiers locaux effectivement exécutés et au JSON CLI. Une faute symbolique intermédiaire (`k` doit être entier pour sin(2πk)=0) a été détectée et corrigée avant publication.

## NEXT HARD RED : STEP68ac

1. SHA-authentifier et charger dans un espace Python **la vraie fonction G originale** Steps45,46,55-normalized,55-global, Step68n Jet, Step68o, Steps57/58/60. Ce nouvel audit Step68ab est mathématique et ne ré-exécute PAS encore le véritable opérateur temporel Step58.
2. Extraire les coefficients g_ij du Taylor de G original i+j≤4, bornés en fractions, puis calculer le VRAI U4 par la récurrence. Utiliser les limites centre Step68aa comme oracle et établir bornes de reste des jets 2/3 par une majoration des dérivées réelles du G FIXE ; **interdit** de seulement différencier les enveloppes U ou U_s publiées.
3. Avec les douze vrais jets canoniques, calculer les coefficients du Step58 A_N/r²,A_M/r² et certifier sans trou `[1/64,1/32]` dont sept cellules sont PENDING, puis `[1/128,1/64]`, puis r=0. Ne pas transformer des échantillons en preuve.
4. Ensuite traiter lapses/bords/jauge, contraintes secondaires, rang Dirac COMPLET, exceptions J=0/K=0, oracle indépendant NON-IBP, cosmologie 4D/stabilité/observations. Le statut reste OPEN et NOT_VALIDATED.

**CHECKPOINT NOUVEAU PRÉFIXÉ ; TOUS LES CHECKPOINTS HISTORIQUES SONT CI-DESSOUS INTÉGRALEMENT.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68aa TERMINÉE (2026-10-25)

**SEULE BRANCHE AUTORISÉE À L'ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. **NE JAMAIS MODIFIER** `main`, `research/v2-flrw`, GitHub Actions/workflows OFF (désactivés par utilisateur).
**GATE_2B OPEN — JANUS_R NOT_VALIDATED**.

**LIRE D'ABORD** `research/STEP68AA_AUTHENTIC_F_CANONICAL_CENTER_THIRD_RADIAL_JETS.md` ; ensuite `research/STEP68Z_EXACT_INVARIANT_CENTER_CONE_AND_SIGNED_F_MOMENTUM.md`. Tous les checkpoints antérieurs Steps68z/y/x/... demeurent CI-DESSOUS intégralement, sans amputation. Commencer le calcul suivant à **Step68ab** et ne pas refaire Step68aa.

## NOUVEAUX RÉSULTATS CANONIQUES ORIGINAUX — POINT CENTRE UNIQUEMENT

Partant de la vraie branche analytique Step49 / ODE original Steps45/46/55, `s=r²`, `pLf(r)=r² U(s)`, `U=U0+U1*s+U2*s²+U3*s³+O(s⁴)`, coefficient `U3<0` historiquement borné exactement par Step67b (publié dans le véritable rapport 68u), **neuf relations de limite analytiques** ont été certifiées. En particulier :

```
lim(r->0) ((pLf''-(2U0+12U1*r²+30U2*r⁴))/r^6) = 56*U3 <0
lim(r->0) ((pLf'''/r-(24U1+120U2*r²))/r^4) = 336*U3 <0
lim(r->0) ((pLf'/r-(2U0+4U1*r²+6U2*r⁴))/r^6) = 8*U3 <0
pLf^(8)(0)=40320*U3 <0.
U_sss(0)=6U3<0.
```

TOUTES ces égalités valent au CENTRE seulement ; aucune borne `pLf'''(r)` exhaustive pour `0<r<=1/32` n'en découle. Les fractions bornées EXACTES et les neuf multiplications se trouvent dans le rapport machine.

**SOURCES EXÉCUTÉES/PUBLIÉES, SHA GIT OCTET-IDENTIQUE VÉRIFIÉS** :

- `numerics/hr_step68aa_canonical_center_radial_jets.py` blob `924192725dc20597df96451e7f211eba91861b50`.
- `tests/test_hr_step68aa_canonical_center_radial_jets.py` blob `f83d6f72570646e2cc04cb4a73f3213373425301`.
- `research/reports/gate2b-step68aa-canonical-center-radial-jets.json` blob `1a536bd0ff9e7b2a95254b3b7cd883d6fd9c524c`.
- Audit `research/STEP68AA_AUTHENTIC_F_CANONICAL_CENTER_THIRD_RADIAL_JETS.md` (lire d'abord).

**TESTS RÉELLEMENT EXÉCUTÉS EN LOCAL : 9 nouveaux tests Step68aa + 8 tests Step68z = 17 PASSED en 0,65s, sans skip**. Le vrai Step68z code blob `8c3a46b44e5c55c7b8f464668f9e8dc7d17eae8b`, certificat blob `38f55aabf7a7c47c812f32db684f50ffbaf16374`, vrais reports Step68u/v/y blobs `aaacd0064e04cb0f5d596aa3df042a4c9a4c751d`/`d83a3b80862a2e990a4c4879ec8745a4e91c8b34`/`04271c360f2245142e171a5979db139ac4bdaf79` sont **byte-authentifiés** par le nouvel outil. Un oracle SymPy indépendant avec U4 libre a recomputé les 9 multiplicateurs en dérivant réellement pLf en r. Deux omissions initiales `U2*s` au lieu de `U2*s²` dans des expressions tests ont été REJETÉES par l'oracle et CORRIGÉES avant la publication finale. Les originaux Step45/46/55/58 n'ont PAS été importés/rejoués dans cette session ; ils sont seulement sous-jacents à l'authenticité de la chaîne amont.

**IDENTITÉS ANALYTIQUES SUR s>0, PAS ENCORE ENCLOSURES** :

```
2s Uss = G_s+(G_U-4)*Us
2s Usss = G_ss+2 G_sU Us+G_UU Us²+(G_U-6) Uss
(2n+2-G_U(0,U0))*U_n=[s^n]G(s,Σ_{k<n} U_k s^k), n>=1
```

`G_U<0` (Step68v) implique absence de résonance des dénominateurs de récurrence au centre. Ne PAS utiliser naïvement `1/s` en intervalles, ni différencier des inégalités `|U-Ustar|`.

## NEXT HARD RED STEP68ab

1. Reconstituer byte-authentiquement les sources originales Steps45/46/55/57/58/60 et `hr_step68n_interval_ode_jets.py`, `hr_step68o_temporal_interval_annulus.py` et dépendances. Étape 68aa n'a PAS fait la relecture complète du Hamiltonien original cette fois.
2. Calculer explicitement `U4` via la vraie fonction G originale et obtenir des bornes de ses dérivées/reste continu, afin de certifier les 2e et 3e jets pour un intervalle entier `0<s<=1/1024`, avec cancellations exactes de centre. Les limites Step68aa sont **tests limites obligatoires**, non remplaçantes.
3. Propager les jets authentiques dans les 12 variables, calculer les coefficients temporels originaux Step58 `A_N/r²,A_M/r²`, certifier EXHAUSTIVEMENT et sans trou `r∈[1/64,1/32]` (ancienne file 7 PENDING), puis `[1/128,1/64]` et centre. Vérifier cellules et limites sans surinterprétation.
4. Enfin contraintes supplémentaires, lapses/bords/jauge, J=0,K=0, rang Dirac COMPLET, nonIBP indépendance, dynamique 4D, stabilité et observables. Conserver GATE ouvert jusqu'à preuve.

**CHECKPOINT PRÉFIXÉ. HISTORIQUE PRÉCÉDENT INTACT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68z TERMINÉE (2026-10-25)

**ÉCRITURE UNIQUEMENT** sur `research/gate2b-nonhomothetic-transfer`. **INTERDIT** de toucher `main`, `research/v2-flrw`, GitHub Actions/workflows OFF.
**ÉTAT SCIENTIFIQUE : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE EN PRIORITÉ** `research/STEP68Z_EXACT_INVARIANT_CENTER_CONE_AND_SIGNED_F_MOMENTUM.md`. Les anciens checkpoints Steps68y/x/w/etc. demeurent intégralement CI-DESSOUS. REPRISE doit partir de **Step68aa**, pas Step68d. Branche initialement retrouvée au commit `ba933be17f52ff7aa0337a45c31f5802e676faf5` avec Step68y, puis cette session a enregistré Step68z.

## PREUVE NOUVELLE ET DÉLIMITATION

Pour `s=r², 0<s<=1/1024` et solution analytique Step49/EDO Step45/46/55, en utilisant les vrais rapports d'origine Steps68u/v/y :

```
d=U-Ustar=s³*h
f=F0/s³, F0=G(s,Ustar)-2*(Ustar+s*Ustar_s)
g=(G(s,U)-G(s,Ustar))/(U-Ustar) in [glo,ghi] <0
2*s*h_s=f+(g-8)*h
h ∈ [ flo/(8-ghi), fhi/(8-glo) ]
  ≈ [-1.4547695730763e-8,-1.0516234369175e-8]  (strict negative)
(U_s-Ustar_s)/s² ∈ [-4.9677906532e-8,-2.5489244634e-8]  (strict negative)
[G(s,U)-G(s,Ustar)]/s³ ∈ [+1.0451684949e-8,+1.4636223583e-8]  (strict positive)
[G(s,U)-Vstar]/s³ ∈ [-1.2038828180e-7,-8.0073880730e-8]  (strict negative)
Vstar=2*(Ustar+s*Ustar_s).
```

**ATTENTION — ERREUR DÉTECTÉE AU TEST ORIGINAL ET CORRIGÉE :** `G(s,Ustar) != Vstar` car `F0<0`. Dans la quantité physique `pLf_prime/r=G(s,U)`, l'écart à `Vstar` est `F0+g*d`, NON `g*d`. Une version intermédiaire erronée de Step68z a été commitée, mais les commits finaux source/tests ont été **CORRIGÉS**, testés et leurs SHA identiques au local. Voir audit Step68z §4.

**CODE FINAL GITHUB** `numerics/hr_step68z_invariant_center_cone.py` SHA `8c3a46b44e5c55c7b8f464668f9e8dc7d17eae8b`. **TESTS FINAUX** `tests/test_hr_step68z_invariant_center_cone.py` SHA `33d20c7e109d1066372292558c17c1a4862346cc`. **MACHINE JSON** `research/reports/gate2b-step68z-invariant-center-cone.json` SHA `38f55aabf7a7c47c812f32db684f50ffbaf16374`. **AUDIT COMPLET** `research/STEP68Z_EXACT_INVARIANT_CENTER_CONE_AND_SIGNED_F_MOMENTUM.md`.

**8 tests réellement PASSED en 0.05s, zéro skip** avec les trois rapports originaux 68u SHA `aaacd0064e04cb0f5d596aa3df042a4c9a4c751d`, 68v SHA `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`, 68y SHA `04271c360f2245142e171a5979db139ac4bdaf79`, tous reconstitués localement OCTET IDENTIQUES et vérifiés Git hash-object. Le JSON final a été généré par l'exécutable avec sources authentiques, son blob GitHub a été comparé à celui du local. L'oracle indépendant BigInt JavaScript sur les trois sources authentiques a validé le cône et les signes, AVANT le correctif distinguant les deux écarts G.

**NON PROUVÉ** : les coefficients temporels Step58 `A_N/r², A_M/r²` jusqu'à r=0, les 7 cellules PENDING sur `[1/64,1/32]`, l'équation complète de stabilité temporelle, rang Dirac, lapses et bords, stabilité nonlinéaire/cosmologie 4D.

## NEXT HARD RED : STEP68aa

1. Authentifier Step45/46/55/57/58/60 et Step68o, reconstructeurs `Jet` et intervalles `I`. Reprendre du précédent Step68z.
2. Insérer les bornes signées des 4 écarts, en distinguant expressément **G(Ustar) vs Vstar**. Calculer `U_{ss},U_{sss}` par différentiation de l'EDO et annulations analytiques au centre, **jamais** par différentiation d'une inégalité sur U ou Us.
3. Evaluer le vrai opérateur temporel six-paires, et recertifier les 7 cellules antérieurement PENDING du trou `[1/64,1/32]`, puis descendre `[1/128,1/64]` et r=0. Exhaustivité, budget, queue vide, 2 contrôles.
4. Vérifier contraintes Dirac complètes/bords/lapses, secteurs J=0,K=0, jauge et 4D. Pas de validation JANUS sans ces vérifications.

**CHECKPOINT AJOUTÉ PAR PRÉFIXE ; HISTORIQUE CONSERVÉ ENTIÈREMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68y TERMINÉE (2026-10-25)

**BRANCHE UNIQUE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. **NE PAS TOUCHER** `main` ou `research/v2-flrw`, ni GitHub Actions/workflows désactivés.
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED**.

**LIRE IMMÉDIATEMENT** `research/STEP68Y_SIGNED_CENTER_RESIDUAL_AND_F_MOMENTUM_JETS.md` puis l'audit Step68x ci-dessous, CONSERVÉ INTÉGRALEMENT.
**SOURCE EXACTE PUBLIÉE** `numerics/hr_step68y_signed_center_residual.py`, blob `6176382e73a383daa650fc007457020a3c906e05`.
**TESTS PUBLIÉS** `tests/test_hr_step68y_signed_center_residual.py`, blob `f7c94caff918b734a65c2e29d84d1f90f0acfb88`.
**CERTIFICAT MACHINE JSON** `research/reports/gate2b-step68y-signed-center-residual.json`, blob `04271c360f2245142e171a5979db139ac4bdaf79`.
**SOURCES ORIGINALES RECONSTITUÉES ET AUTHENTIFIÉES en local** : Step68u rapport blob `aaacd0064e04cb0f5d596aa3df042a4c9a4c751d`, Step68v rapport blob `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`. Tests réellement exécutés **8 PASSED en 0.09s**, deuxième reprise locale **8 PASSED en 0.05s** ; fichiers code/test/JSON publiés OCTET-IDENTIQUES à leurs versions testées, SHA Git relus.

## RÉSULTAT MATHÉMATIQUE NOUVEAU — PETIT CENTRE À SIGNE CONTRÔLÉ

Pour `s=r²`, `0<s<=1/1024` (`0<r<=1/32`), dans le modèle sphérique et conditionnel aux preuves source Steps49/67b/68u/68v, avec `Ustar=U0+U1*s+U2*s²`, `kappa=10^-7`, `2sU_s=G(s,U)-2U` :

- Les deux résidus *authentiques* et leur `G_U<0` donnent par intersection EXACTE, sans flottants, **`F0(s)/s³ ∈ [-104671973400629476166791119/800000000000000000000000000000000, -473550521560821294562534863/5000000000000000000000000000000000] <0`**, où `F0=G(s,Ustar)-2Ustar-2sUstar_s`.
- Step67b donne le coefficient vrai `U3<0`. La comparaison avec `F0<0` interdit une remontée de `U` au-dessus de `Ustar` : **`-kappa*s³<=U-Ustar<=0`**, avec borne supérieure stricte pour tout `s>0`.
- Par la véritable EDO et `G_U<0`, l'intervalle SIGNÉ de `(U_s-Ustar_s)/s²` est **`[-104671973400629476166791119/1600000000000000000000000000000000, 4117968618087380149271638523/40000000000000000000000000000000000]`** (environ `[-6.54e-8,+1.03e-7]`), plus serré que Step68x `±3.449e-7`.
- Le même calcul donne `(G(s,U)-Vstar)/s³ ∈ [-104671973400629476166791119/800000000000000000000000000000000, 117968618087380149271638523/20000000000000000000000000000000000]`, environ `[-1.3084e-7,+5.8984e-9]`, `Vstar=2(Ustar+sUstar_s)`.
- **Lien au secteur canonique original f :** `pLf=sU`, `pLf_prime/r=G(s,U)`. En conséquence le jet de valeur `pLf-sUstar` appartient à `[-kappa*s⁴,0]` et le jet de dérivée normalisée possède la borne signée précédente. Le certificat conserve tous les rationnels aux points `r=1/32` et `r=1/64`.

**NE PAS EXAGÉRER** : 68y ne recalcule PAS les coefficients temporels du Step58 `A_N/r²`, `A_M/r²` pour `r<1/32`, ne borne PAS `U_{ss},U_{sss}`, n'exécute PAS le vrai Hamiltonien six-couples non-IBP, et ne traite PAS le rang Dirac complet ni la cosmologie 4D. L'annulus `[1/64,1/32]` antérieurement INCOMPLET reste NON CERTIFIÉ : Step68u antérieur avait 500 nœuds, 247 cellules signées, **7 PENDING**. Les 1585 cellules Step68w couvrent UNIQUEMENT `[1/32,17/20]`, sans changer.

## NEXT HARD RED STEP68z

1. Depuis le connecteur GitHub, recharger et SHA-authentifier sources originelles Step45/46/55/57/58/60 et moteur `numerics/hr_step68o_temporal_interval_annulus.py`. Le répertoire local `/mnt/data/janus-step68y` est TRANSITOIRE, il ne contient que Step68y, tests et JSON 68u/68v ; **GitHub est le point de reprise fiable**.
2. Injecter la **barrière signée** `-kappa*s³<=U-Ustar<=0`, et bornes signées de `U_s`, `V=G(s,U)`, dans les douze jets canoniques originaux avant d'évaluer le coefficient temporel complet et non le seul moment radial.
3. Obtenir `U_{ss}`, `U_{sss}` par différentiation de la VRAIE ODE avec jet analytique/annulation des facteurs `s`, et non en dérivant les inégalités de `U` ou `U_s` (mathématiquement interdit). Normaliser d'abord les annulations `r²` avant intervalles sur `A_N/r²,A_M/r²`.
4. Certifier de façon **exhaustive** les anneaux `[1/64,1/32]` puis `[1/128,1/64]` et le centre `r=0` avec budgets bornés, reprise atomique, queue vide et double vérification ; enregistrer SANS PRETENDRE des portions incomplètes signées.
5. Puis autres contraintes temporelles, jauge et bords, indépendance des deux lapses, rang de Dirac COMPLET, oracle six-paires NON-IBP, chartes `J=0,K=0`, BD/4D ; conserver Gate ouvert et JANUS non validé.

**CHECKPOINT PRÉFIXÉ, HISTORIQUE PRÉCÉDENT CI-DESSOUS CONSERVÉ SANS AMPUTATION.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68x, APRÈS AUDIT STEP68w (2026-10-25)

**BRANCHE UNIQUE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. Garder `main` et `research/v2-flrw` intouchées ; GitHub Actions/workflows OFF. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**À LIRE D'ABORD :** `research/STEP68X_EXACT_SHRINKING_CENTER_U_AND_US_ENCLOSURES.md`, puis `research/STEP68W_INDEPENDENT_RATIONAL_LAPSE_RATIO_AND_ROW_RANK_AUDIT.md`. La précédente preuve Step68v du profil spatial jusqu'au centre est immédiatement ci-dessous, conservée intégralement.

## STEP68w NOUVEAU AUDIT RATIONNEL INDÉPENDANT — 1585 CELLULES

**SOURCE EXÉCUTÉE ET SHA GIT RELU :** `scripts/hr_step68w_archived_lapse_ratio_audit.py`, blob `93109dd8da5e524876a19340382d88ff4c077629`.
**TESTS PUBLIÉS ET EXÉCUTÉS, SHA RELU :** `tests/test_hr_step68w_archived_lapse_ratio_audit.py`, blob `6cd0be37ef7a8ac5dac734b518f794216d4d250b`.
**RAPPORT MACHINE SHA RELU :** `research/reports/gate2b-step68w-rational-ratio-audit.json`, blob `d644f0f02df36987ffb4d2d11c567509ffcdeca8`.
**ANCIENNES PREUVES AUTHENTIFIÉES** : 68s 1006 cellules (blob `e890998a2f925f881ab85b60a9027e5828e35ed5`), 68q 314 (blob `82f5d046cd0ca0c342adabe8b8f13cfc3f99308d`), 68p 265 (blob `978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6`). Les TROIS JSON ENTIERS ont été lus depuis GitHub et leurs 1585 cellules contrôlées dans un vérificateur JavaScript indépendant en `BigInt` rationnel : statut, 0 failures/queue, endpoints exacts, intervalles signés et JOINTIFS sans trou. Les cellules extrêmes de quotient ont été trouvées en divisions/produits d'entiers exacts, PAS par flottants.

```
Ensemble r in [1/32,17/20]:
1/50000 < M/N=-A_N/A_M < 14
A_N/r² > 7/20
A_M/r² < -546
```
Ces inégalités sont déduites CELLULE PAR CELLULE (pas ratio des bornes globales). Le rapport borné prouve le NON-ANNULLEMENT POINT PAR POINT et la compatibilité positive DE LA SEULE LIGNE ALGÉBRIQUE `dot C=A_N N+A_M M` sous contraintes historiques Steps68h/j. **Rang 1 de cette UNIQUE équation sur ce domaine ≠ rang de Dirac complet, et bords/gauge/évolution 4D NON vérifiés.**

**Reproductibilité** : vrai contrôle complet BigInt sur 1585 cellules effectivement exécuté via les archives GitHub connectées. Vérificateur Python autonome publié, **7 tests SYNTHÉTIQUES 68w localement PASSED en 0.04s**, MAIS la relecture Python du TRIO de JSON complets n'a PAS été relancée localement parce que la session container a été réinitialisée et les gros fichiers GitHub ne sont pas montés. Ne PAS prétendre le contraire. Le vérificateur Python accepte `python scripts/hr_step68w_archived_lapse_ratio_audit.py research/reports` dans un clone complet.

## STEP68x NOUVEAU COROLLAIRE SPATIAL CENTRE : U ET U_s À ERREUR VARIABLE

**SOURCE PUBLIÉE, VRAIMENT EXÉCUTÉE ET SHA RELU :** `numerics/hr_step68x_normalized_center_ode_envelope.py`, blob `720a893ed8e0321fdf2b84aaff881b904c08e9fd`.
**TESTS PUBLIÉS, EXÉCUTÉS ET SHA RELU :** `tests/test_hr_step68x_center_corollary.py`, blob `a98fefbf13e391a3ea11dfcbb9b27997e6eb38f8`. **5 tests spécifiques PASSED.**
**RAPPORT MACHINE CALCULÉ AVEC VRAI RAPPORT ORIGINAL STEP68v** `research/reports/gate2b-step68x-center-normalized-envelope.json`, SHA `22a9c0014c717e8422b575f0ebd731069af29850`.
**ORIGINAL 68v EXACTEMENT RECONSTITUÉ dans ce workspace depuis Github** : `research/reports/gate2b-step68v-global-monotone-radial-U.json`, blob `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`. Re-exécuté le calcul d'intervalle des deux bornes F0'''/6 et G_U depuis ce rapport, sous réserve des certificats amont originaux Step49/67b/68v. Cette étape NE REJOUE PAS 68v lui-même dans cette session, seulement son corollaire exact.

À partir `|U-Ustar|<=kappa*s³` avec `kappa=1/10^7`, `F0(s)=G(s,Ustar)-2Ustar-2sUstar'`, `|F0|<=R0*s³`, `|G_U|<=L`, déduire EXACTEMENT de la vraie ODE :
```
pour 0<=s<=1/64 :
|U_s-Ustar'| <= C*s²
C = 551901551914723209073991119/1600000000000000000000000000000000
  ≈ 3.44938469946702e-7
à r=1/32 (s=1/1024) :
|U-Ustar| <= 1/10737418240000000 ≈9.313225746e-17
|U_s-Ustar'| <= C/1024² ≈3.289589595e-13 .
```
Ceci remplace le tube constant 1e-6 par une borne de U **10 737 418 240 fois plus étroite à r=1/32**, et de dérivée O(s²) jusqu'à s=0. Le signe de U_s avait déjà été certifié par Step68v ; il s'agit ici de précision quantitative nouvelle, non de signe temporal.

**12 TESTS COMBINÉS DES VERSIONS PUBLIÉES Step68w+68x PASSED en 0.04s sous timeout 8s** ; log SHA vérifié `research/reports/gate2b-step68wx-published-tests.log` blob `101f7703ff8a1006ec74a54d6ea42ab9f2e924b1`.

**LIMITATION** : Step68x n'évalue PAS `A_N,A_M` sur `r<1/32`, et ne reconstitue pas le Hamiltonien Step58 complet dans cet environnement container RÉINITIALISÉ. Une tentative de publier un premier jeu de tests plus long a été bloquée par un filtre du connecteur ; elle a été remplacée par **5 tests effectivement exécutés et publiés octet-identiques**, voir SHA ci-dessus. Ne pas présenter les tests non publiés comme test Git du projet.

## NEXT HARD RED STEP68y

1. Retrouver/réunir les 8 modules physiques originaux Step45/46/55/57/58/59/60 via GitHub et SHA de `research/reports/gate2b-step68-source-preflight.json`. Sans clone direct autorisé dans le container, utiliser le connecteur ; le workspace local `/mnt/data/janus-step68w` est TRANSITOIRE et peut disparaître à la prochaine session.
2. Injecter **le tube cubique variable `kappa*s³`** à la place du tube constant `1e-6` dans le moteur `hr_step68o_temporal_interval_annulus.py`, en conservant tous 12 jets et la vraie variation du shift, et propager les coefficients normalisés `A_N/r²,A_M/r²` avec simplifications analytiques des facteurs r pour éviter une explosion d'intervalles.
3. Certifier le vrai anneau `[1/64,1/32]` COMPLET sous budgets bornés `scripts/janus_bounded_job.py`, puis zone `(0,1/64]` et limite centrale r=0, avec développement central original U0..U3. L'ancien essai Step68u sur [1/64,1/32] est INCOMPLET : 500 nœuds, 247 cellules prouvées, 7 pending. **Ne PAS le déclarer certifié.**
4. Enfin autres contraintes temporelles, bords/jauge, vrai oracle six-paires NON-IBP, rang complet Dirac, K=0/J=0 et BD/4D. Maintenir `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.
5. Après toute preuve créer GitHub code/tests/rapport sur SEULE branche, garder Actions OFF et PRÉFIXER checkpoint historique sans supprimer ~270k caractères.

---

# JANUS — REPRISE PRIORITAIRE : STEP68v (APRÈS 68u) TERMINÉE (2026-10-25)

**SEULE BRANCHE MODIFIABLE** `research/gate2b-nonhomothetic-transfer`. `main` et `research/v2-flrw` INTACTES. GitHub Actions/workflows OFF. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68V_CERTIFIED_GLOBAL_RADIAL_U_MONOTONICITY.md`, puis `research/STEP68U_CERTIFIED_SHRINKING_CUBIC_CENTER_BARRIER.md`; conserver preuves temporelles précédentes `research/STEP68S_CERTIFIED_TEMPORAL_SIGNS_TO_R_1OVER32.md`.

**NOUVELLE SOURCE 68v VRAIMENT EXÉCUTÉE, GIT SHA BYTE-MATCH :** `numerics/hr_step68v_global_monotone_U.py`, blob `9b6a2f93271a96af97d62648201c163282758c08`. **6 TESTS RÉUSSIS** (2.27s, lanceur timeout 22s) : `tests/test_hr_step68v_global_monotone_U.py`, blob `6bdff3937051dd40719eb1d0f1441065eecb4b54`. **RAPPORT RATIONNEL** `research/reports/gate2b-step68v-global-monotone-radial-U.json`, blob `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`. États/logs `research/reports/gate2b-step68v-pytest-state.json` et `...pytest.log`.

## THÉORÈME SPATIAL NOUVEAU : U_s>0 JUSQU'AU CENTRE ET SUR TOUT LE RAYON

Sur `0<=s<=1/64` (`0<=r<=1/8`), prendre la VRAIE branche analytique centrale Step49/67b et ses coefficients EXACTS `U0,U1,U2`, et le coefficient `U3` encadré rigoureusement Step67b. Définir `Ustar=U0+U1*s+U2*s²` ; `kappa=1/10^7`, barrières `Ustar±kappa*s³`. Les dérivées 3 des vrais résidus `Fplus,Fminus` de la véritable EDO 45/46/55 satisfont STRICTEMENT :
```
Fplus'''/6 <= -3664994635715032685663/5000000000000000000000000000 <0
Fminus'''/6 >= 1270413128798157440287/2500000000000000000000000000 >0
```
par jets I entiers dirigés original `S=10^28` sur le continuum. La vraie récurrence analytique centrale donne exactement F±(0)=F±'(0)=F±''(0)=0 (NE PAS affirmer que la seule appartenance numérique de zéro à l'intervalle suffit). Taylor-Lagrange + |U3|<kappa + comparaison donne `|U-Ustar|<=10^-7*s³` sur le centre ENTIER r<=1/8. L'ancien Step68u (`numerics/hr_step68u_cubic_center_barrier.py`, Git blob `4249c1a8c1f60071612c52d756d9f4ff753f22e3`, **6 tests PASSED**, rapport `research/reports/gate2b-step68u-center-cubic-barrier.json`) n'avait certifié que r<=1/32 ; il reste un sous-théorème valide et est conservé.

**NOUVEAU CONTRÔLE DE DERIVÉE DE LA VRAIE EDO :** G_U bornée exactement sur tout le nouveau tube par une différentiation automatique originale. Si `F0=G(s,Ustar)-2Ustar-2sUstar'`, alors `|U_s-Ustar'|<=s²*(R0+(L_G+2)*kappa)/2`, où R0 borne `|F0'''/6|` et L_G borne `|G_U|`, toutes deux obtenues par intervalles. La borne inférieure strictement positive de la VRAIE solution normalisée est
```
U_s(s)>=3947151372926460534852373/5000000000000000000000000000 >0
pour TOUT s in [0,1/64], inclut U_s(0)=U1.
```
Step68m original a déjà CERTIFIÉ `U_s>0` par 8192 cellules sur `s in [1/64,289/400]` soit `r in [1/8,17/20]` ; leurs intervalles joints prouvent donc **U_s>0 pour CHAQUE s∈[0,289/400]**, c'est-à-dire **TOUT r∈[0,0.85]** (SPATIAL SEULEMENT), conditionnel aux preuves anciennes Step49/67b. Tous fournisseurs physiques Step45/46/55 originales byte-identiques et sources 68u/m pin SHA.

## TEMPORAL ENCORE OUVERT

Le VRAI opérateur temporel six-pair Step58 a son signe `A_N>0, A_M<0` continu sur `r∈[1/32,17/20]` certifié Steps68p/q/s et **1585 cellules EXACTEMENT rejouées** Steps68r/t. Pas de preuve `A_N,A_M` sur `0<=r<1/32`. Step68u essai brut `r in [1/64,1/32]` **INCOMPLETE : 500 nœuds, 247 cellules certifiées, 7 en attente**, SHA authentifié GitHub `research/reports/gate2b-step68u-incomplete-1over64-to-1over32-checkpoint.json` blob `fbbeeb09fb397abf14d77fb0bce22d8a44172b79`. Relance possible depuis workspace local `research/reports/step68u-band-1over64-to-1over32.json` avec `--start 1/64 --end 1/32 --max-depth 25` dans lanceur jobs TIMEOUT 24s, mais sub-division brut inefficace. La nouvelle barrière cubique élimine l'incertitude U dominante, cependant pour des cellules LARGES les autres dépendances d'intervalles du Step58 restent inflationnistes.

**PRIORITÉ UNIQUE SUIVANTE :** construire un module de jets canoniques/réponse du shift NORMALISÉ PAR r,s au centre, réduire `A_N/r²` et `A_M/r²` sur les contraintes complètes avec les séries centrales `U0..U3` et l'encadrement cubique `|U-Ustar|<=10^-7*s³`, puis certifier signes jusque r=0. NE PAS simplement prolonger les résultats extérieurs sans calcul. Les limites/signes de A_N/r²,A_M/r² au centre NON PROUVÉS. Ensuite : jauge/bords/lapses temporels, rang Dirac, vrai oracle Poisson NON-IBP indépendant, charts K0/J0, fantôme BD, cosmologie 4D.

**RAPPEL OPERATOIRE :** chaque calcul >quelques secondes doit être lancé sous `python scripts/janus_bounded_job.py --timeout-seconds 20..25 --grace-seconds 2 --state <state> --log <log> --label <name> -- <cmd>` ; état JSON atomique et interrompt les enfants. Après chaque vraie avancée préfixer ce fichier en conservant les anciennes ~260K lignes/chars et publier code/test/rapport SHA-vérifiés. **GATE_2B OPEN — JANUS_R NOT_VALIDATED**.

---

# JANUS — REPRISE PRIORITAIRE : STEP68t TERMINÉE (2026-10-25)

**SEULE BRANCHE D'ÉCRITURE** `research/gate2b-nonhomothetic-transfer`, main et v2-flrw intouchées, GitHub Actions OFF. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AUDIT :** `research/STEP68T_EXACT_REPLAY_1006_INNER_TEMPORAL_CELLS.md`.
**CODE SOURCE :** `numerics/hr_step68t_replay_near_center.py` SHA `4cf195f22ec2218de7453797bccaf5f151a4d2cd`.
**TESTS :** `tests/test_hr_step68t_replay_near_center.py` SHA `2f9929f1433d00d2026478d48606a46a790dd2b7`, trois tests PASSED 4.19s, sous timeout 16s.
**REPLAY COMPLET :** `research/reports/gate2b-step68t-replay-1006-cells-report.json` Git blob `b5c5a52a0b3960ae630ef2d3521e0d4d9689f4d3` ; état `research/reports/gate2b-step68t-replay-state.json` Git blob `1ac99ccbbd5413f67ffa140d28bf091c8c6eb5f2` : 1006/1006, PASSED, zéro discrepancy. SIX jobs séparés sous timeout 24s chaque. L'état est atomique par cellule et refuse toute dérive SHA du certificat/moteur.
**AVERTISSEMENT :** il s'agit du MEME évaluateur arithmétique Step58 relancé exactement, PAS un oracle non-IBP indépendant.

**STATUT CALCUL :** 3 certificats continus joints **r∈[1/32,17/20]** pour vrai profil Step55 de l'EDO originale : Step68p 265 feuilles ([1/8,17/20]), Step68q 314 feuilles ([1/16,1/8]), Step68s 1006 feuilles ([1/32,1/16]). Total **1585 cellules certifiées et effectivement re-évaluées une par une, strictement (A_N>0,A_M<0)**. Les fractions et sources exactes se trouvent dans les 3 archives GitHub.
**RESTE SCIENTIFIQUE** : centre `[0,1/32)` NON CERTIFIÉ, limites A_N/r² A_M/r², bords/jauge, rang Dirac, oracle Poisson NON-IBP, charts exceptionnelles, BD et cosmologie JANUS-R encore OUVERTS. Le théorème ne constitue pas une validation de 4D JANUS.

## NEXT STEP68u (HARD RED)

1. Tenter `[1/64,1/32]` en lots bornés avec le moteur inchangé (`--start 1/64 --end 1/32 --max-depth 24`) et états enregistrés à chaque feuille ; si la quantité de cellules explose, NE PAS ignorer l'inefficacité, écrire explicitement le blocage et la file de reprise.
2. Prioriser la méthode normale du centre en traitant l'ODE singulière (2sU_s=G-2U) via la récurrence U0..U3 certifiée originale Step67b. Obtenir des bornes de A_N/r² et A_M/r² sur [0,epsilon], avec un calcul exact dans les variables normalisées. Ne PAS déduire les signes au centre par extrapolation.
3. Ensuite bords + gauge, vrai oracle non-IBP six couples, rang global Dirac, K0/J0. Maintenir état durable et timeout sur toute exécution.

---

# JANUS — REPRISE PRIORITAIRE : STEP68s CERTIFIÉE (2026-10-25)

**BRANCHE EXCLUSIVE MODIFIABLE :** `research/gate2b-nonhomothetic-transfer`. MAIN/V2 intouchées ; GITHUB ACTIONS OFF ; **GATE_2B OPEN, JANUS-R NOT_VALIDATED**.

**LIRE D'ABORD :** `research/STEP68S_CERTIFIED_TEMPORAL_SIGNS_TO_R_1OVER32.md` ; puis `research/STEP68R_EXHAUSTIVE_REPLAY_579_TEMPORAL_INTERVAL_CELLS.md`.
**NOUVEAU GROS CERTIFICAT 390326 OCTETS :** `research/reports/gate2b-step68s-inner-1over32-to-1over16-cover.json`, Git blob `e890998a2f925f881ab85b60a9027e5828e35ed5`, SHA256 local `7491e166286279f8ac6423677fec069f7fc9d6bca7bfda4271cedd1c0addedd4`. Certifié par SAME byte-original original Step58/Jets/adaptive SHA-pin 68n/68o/68p. 2011 nœuds (1006 FEUILLES fermées), 0 pending et 0 failed. Fractions exactes pour TOUTES les 1005 jonctions et deux bornes terminales [1/32,1/16]. `A_N >=23763242565712321121633107/10^28 >0` ; `A_M <= -21235779180155817648396567047/(5*10^27)<0`.
**NOUVELLE ZONE SIGNÉE CONTINUE TOTALE**, jointe aux certificats précédents 68q/68p : `A_N(r)>0,A_M(r)<0 POUR CHAQUE r in [1/32,17/20]` sur vraie branche radiale Step55 sous le tube global certifié Step68l et contraintes locales originales Steps68h/j. Rapport de lapses local `-A_N/A_M>0` sous shell. NE PAS INFÉRER rang global Dirac, bords ou fantôme BD.

**JOBS BORNÉS :** neuf lots `scripts/janus_bounded_job.py --timeout-seconds 24 --grace-seconds 2`, tous PASSED et chacun 9..19 secondes, avec états atomiques `research/reports/step68s-inner-band-run1..9.state.json` et logs `...log`. Un état `INCOMPLETE` a été conservé à chaque coupure, puis `CERTIFIED` seulement quand file vide.
**AUDIT REPLAY PRECEDENT STEP68r :** 579/579 cellules historiques p/q recalculées EXACTEMENT, 4 lots <=25 secondes PASSED; source `numerics/hr_step68r_cell_replay.py` SHA `60214f32d16ea2aa1f04ff63ce76338e28457034` et tests 6 PASSED, états et rapport archivés GitHub. IL S'AGIT DU MÊME MOTEUR PHYSIQUE, pas d'un oracle Poisson indépendant.

## NEXT STEP68t

1. Prolonger le script de REPLAY `numerics/hr_step68r_cell_replay.py` à la nouvelle preuve `[1/32,1/16]` (1006 cellules) avec SHA256 pin, vérifier toutes les cellules par lots <=25s et états persistants, puis publier preuve de relecture et tests GitHub.
2. **CENTRE non couvert r∈[0,1/32) :** tenter calcul par intervalles à `[1/64,1/32]` sous jobs bornés, mais le coût croit rapidement. Passer ensuite à normalisation centrale des moments (Taylor réel U0...U3 certifiés Step67b) et calcul des limites `A_N/r²,A_M/r²` sans division impropre par s. Ne PAS proclamer centre par continuité non chiffrée.
3. Bords, choix de jauge, lapses positifs globaux, rang six-pair Poisson indépendant NON-IBP, charts K=0/J=0 ; Gate2B reste OPEN.
4. Après chaque vraie avancée récrire en PRÉFIXE ce restart, conserver tous les anciens contenus et ne jamais réactiver Actions.

---

# JANUS — REPRISE PRIORITAIRE : STEP68r TERMINÉE (2026-10-25)

**BRANCHE EXCLUSIVE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. MAIN/V2 intouchées, GitHub Actions/workflows OFF. **GATE_2B OPEN — JANUS-R NOT_VALIDATED.**

**AUDIT IMMÉDIAT :** `research/STEP68R_EXHAUSTIVE_REPLAY_579_TEMPORAL_INTERVAL_CELLS.md`.
**RÉEXÉCUTION EXHAUSTIVE DES CELLULES PAR LE MÊME MOTEUR :** source `numerics/hr_step68r_cell_replay.py` SHA `60214f32d16ea2aa1f04ff63ce76338e28457034`; tests `tests/test_hr_step68r_cell_replay.py` SHA `b0ddcd8d8504d8bb090148764a06824f86d1c978`.
**RAPPORT COMBINÉ :** `research/reports/gate2b-step68r-replay-summary.json`; états `.../gate2b-step68r-inner-replay-state.json` et `.../gate2b-step68r-outer-replay-state.json`.
**ÉVÉNEMENT VÉRIFIÉ :** ALL 579 CELLS STRICTLY MATCHED EXACTLY : 265/265 annulus extérieur [1/8,17/20] et 314/314 bande intérieure [1/16,1/8]. Chaque intervalle de A_N et A_M a été recalculé et DOIT ÊTRE égal à la valeur exacte du JSON source ; SHA256 archives pin, Git originaux pin et source jet/interval pin, jet/constraint physical originals. Quatre jobs PASSÉS, chacun timeout dur 25s, après chaque cellule checkpoint atomique.
**6 TESTS CIBLÉS PASSED 4.40s** sous launcher borné 22s. PREMIER essai 3 failed et 3 passed UNIQUEMENT faute d'avoir fait copie du JSON intérieur sous son nom définitif local, second essai 6 passed complet. Log conservé `research/reports/gate2b-step68r-pytest.log`. IL NE S'AGIT PAS D'UN ORACLE THÉORIQUE NON-IBP INDÉPENDANT : moteur d'intervalles identique. Ne pas revendiquer rang Dirac ou validité JANUS.

**SITUATION ACTUELLE CERTIFIÉE :** vrais coefficients temporels six-pair `A_N>0,A_M<0` sur **tout r ∈ [1/16,17/20]** conditionnellement aux vrais profils spatiaux originaux et Step68l Ustar±1e-6. Steps68h/j prouvent exactement B_N=B_M=0 on-shell. Sur r<1/16, statut OUVERT.

## NEXT STEP68s

(1) tenter par lots <=25s l'annulus `r∈[1/32,1/16]` avec `python scripts/janus_bounded_job.py --timeout-seconds 24 --grace-seconds 2 ... -- python -m numerics.hr_step68p_adaptive_temporal_sign --state <state> --start 1/32 --end 1/16 --max-cells N --max-depth 22`, données JSON atomiques avec status INCOMPLETE tant que queue non vide. SI ÉCHEC, conserver le blocage et privilégier normalization régulière du centre via série U0..U3 Step67b.
(2) republier vrais tests, code, rapports, SHA vérifiés, préfixer le journal sans effacer.
(3) conditions bords/gauge, oracle Poisson non IBP, rang Dirac, K=0/J=0, fantôme BD restent NON PROUVÉS.

---

# JANUS — REPRISE PRIORITAIRE : STEP68q CERTIFIÉE (2026-10-25)

**BRANCHE EXCLUSIVE EN ÉCRITURE** `research/gate2b-nonhomothetic-transfer`, `main`/`research/v2-flrw` intouchées. GitHub Actions/workflows OFF. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AUDIT DE PREMIER NIVEAU :** `research/STEP68Q_CERTIFIED_TEMPORAL_SIGN_EXTENSION_TO_R_1OVER16.md` ; puis `research/STEP68N_68P_CERTIFIED_OUTER_TEMPORAL_LAPSE_SIGNS.md`.
**CERTIFICAT COMPLET 314 CELLULES :** `research/reports/gate2b-step68q-inner-1over16-to-1over8-cover.json`, GIT SHA `82f5d046cd0ca0c342adabe8b8f13cfc3f99308d` égal fichier LOCAL vérifié, SHA256 `296e83528f9675fd42521b7cfffa2ec0f6057cce1d930a97a323aa007009e2c2`, 122536 octets.
**PREUVE SOURCE :** `numerics/hr_step68p_adaptive_temporal_sign.py` Git SHA `10f62bacafa25827de747707dd3f45c7c96458a6`; `numerics/hr_step68o_temporal_interval_annulus.py` Git SHA `c99caebc17f243784450ddff94fb061767e6d8e7`; `numerics/hr_step68n_interval_ode_jets.py` Git SHA `96370e0599748c6dc07faf339ab3646ae3474e7d`. Ces fichiers et les 8 modules physiques originaux SHA-pin sont authentifiés dans le certificat.

**THÉORÈME NOUVEAU, PROLONGEMENT INTÉRIEUR :** sur l'ENSEMBLE du sous-anneau `r∈[1/16,1/8]` de la VRAIE BRANCHE Step55 sous enveloppe globale Step68l `Ustar±1e-6` :
```
A_N(r) >= 13992170999239591409209901/500000000000000000000000000 >0,
A_M(r) <= -17646463958239652791556564517/1250000000000000000000000000 <0.
```
Ceci repose sur 627 nœuds de subdivision, 314 feuilles rationnelles fermées et jointives, état `CERTIFIED`, 0 pending/failed. **Joint à Step68p** `[1/8,17/20]`, établit `A_N>0,A_M<0` continûment sur `[1/16,17/20]`, pas le centre.
**TIMEOUTS** quatre lots terminés sous 24s chacun, avec état local atomique `research/reports/step68q-inner-band-1over16-to-1over8.json` et logs `research/reports/step68q-inner-band-run{1..4}.[state.json|log]`. Lots : 160/77/7 ; 320/158/5 ; 576/286/5 ; 627/314/0 (nœuds/feuilles/attente). Après chaque cellule sauvegarde durable.

**RÉCENTE INTERRUPTION CORRIGÉE :** L'étape 68p précédente a été publiée jusqu'au bout après coupure : 4 sources physiques nouvelles, tests, 265 cellules sur annulus extérieur, Git blob du gros JSON `978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6` byte-identique local ; rapport, logs et audit archivés. 10 tests déjà PASSED 4.75s sous timeout 27s. Les premières parties du nouveau calcul 68q n'ont PAS encore été relancées dans un test de relecture du contenu physique cellule par cellule (mais test indépendant de jonction et signes exacts effectué).

**NEXT** (1) ajouter un replayer physique rigoureux de TOUTES cellules 68p+68q par lots sous timeout, comparant chaque intervalle enregistré à un nouveau calcul `evaluate_cell` et refusant changements SHA/provenance ; publier état/log/resultats. (2) tenter `r∈[1/32,1/16]` sous jobs bornés et éventuellement aller plus près du centre ; si cela échoue, combiner avec normalisation Taylor centrale. (3) reprendre vérifications bords/lapses/gauge et oracle NON-IBP, rang Dirac 4D. **Ne PAS déclarer JANUS validé**.

---

# JANUS — REPRISE PRIORITAIRE : STEP68p CERTIFIÉE ET ARCHIVÉE (2026-10-25)

**SEULE BRANCHE MODIFIABLE** `research/gate2b-nonhomothetic-transfer`. `main`, `research/v2-flrw` intouchées ; GitHub Actions/workflows désactivés. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**RÉSULTAT IMMÉDIAT :** `research/STEP68N_68P_CERTIFIED_OUTER_TEMPORAL_LAPSE_SIGNS.md`.
**ORIGINAL CANONICAL SOURCES :** huit véritables modules Step45/46/55/57/58/59/60 byte-SHA authentifiés ; Step68l certificat global `|U-Ustar|≤10^-6` disponible et Step68m preuve `U_s>0` sur anneau.
**NOUVEAU CALCUL EXACT TEMPOREL :** `numerics/hr_step68n_interval_ode_jets.py` (`96370e0599748c6dc07faf339ab3646ae3474e7d`), `numerics/hr_step68n_temporal_interval_point.py` (`33e2ab71738baaea104e686c427bd8c52109343d`), `numerics/hr_step68o_temporal_interval_annulus.py` (`c99caebc17f243784450ddff94fb061767e6d8e7`), `numerics/hr_step68p_adaptive_temporal_sign.py` (`10f62bacafa25827de747707dd3f45c7c96458a6`), tests `tests/test_hr_step68o_68p_temporal_annulus.py` (`381f44035d638fab153373ac5a2e76c830b46c5d`). TOUS les blobs ont été comparés aux exécutables locaux.
**CERTIFICAT COMPLET DES 265 CELLULES** (105268 bytes !) `research/reports/gate2b-step68p-adaptive-outer-cover.json`, Git blob `978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6`, SHA256 local `179b967cc21160dcfef5eb98e1142c5ca17b83ee182d17162a2ec64708e48e4f` **VERSION VRAIMENT RELUE GITHUB : MATCH SHA Git exact**.
**RAPPORT SYNTHÈSE** `research/reports/gate2b-step68p-certification-machine-summary.json`, ET état/test logs `research/reports/gate2b-step68p-final-test.state.json` / `...-test.log`. Nouveau test 10 PASSED 4.75s sous lanceur timeout 27s.

## THÉORÈME TEMPOREL NOUVEAU, CONDITIONNEL AU VRAI PROFIL GLOBAL STEP55

Sur TOUT `r∈[1/8,17/20]=[0.125,0.85]`, avec les intervalles outward originaux de tous 12 jets canoniques (poussières incluses), générés depuis l'EDO EXACTE `2sU_s=G-2U` et le tube Step68l 10^-6 :
```
A_N(r) = [dot C_original_step58]_N > 0
  (borne rationnelle globale) A_N >= 74947205335628168039413183/1250000000000000000000000000 >0;
A_M(r) = [dot C_original_step58]_M < 0
  (borne rationnelle globale) A_M <= -237882690187249002934304118023/5000000000000000000000000000 <0.
```
**Algorithme :** 529 cellules adaptatives examinées, 265 cellules fermées certifiées couvrent TOUT cet anneau SANS TROUS ni cell pending. Calcul original six-pair Step58 (full shift non figé). A chaque cellule source-sha vérifié + checkpoints atomiques, jamais affirmer CERTIFIED avec file non vide. Premier large slab non-certifiant correctement subdivisé. Ratio local `M/N=-A_N/A_M>0` sur cet anneau si l'algèbre Steps68h/j réduit les lapses dérivés sur shell. La borne globale du ratio est TRÈS PRUDENTE (voir JSON), NE PAS affirmer ratio=0.519 avec erreur globale faible.

**TOUS LES CALCULS LONGS AVEC DEADLINE :** `scripts/janus_bounded_job.py --timeout-seconds 27 --grace-seconds 2 --state <state.json> --log <job.log> --label <name> -- <cmd>`. Trois lots de preuve sous 28s/27s/27s ; test final terminé avant 27s, 10 PASSED. En cas SIGTERM/SIGKILL arrêt du groupe enfant et état JSON, reprise cellule par cellule depuis disque.

## ENCORE OUVERT (PRIORITÉ STEP68q)

1. **REJOUER INDÉPENDAMMENT LES 265 CELLULES** de la preuve Step68p avec l'évaluateur original, vérifier chaque enclosure recomputé contenue ou respectée dans sauvegarde et publier certificat de relecture; le test existant ne rejoue pas automatiquement toutes les cellules.
2. ATTENTION : `r in [0,1/8)` TOUJOURS NON CERTIFIÉ pour signes A_N,A_M. Faire un prolongement par bornes de série Taylor centrées `U0..U3` ou continuation adaptative s>0 rapprochant progressivement le centre, sous JOBS bornés. Dans tous les cas normaliser A_N/r², A_M/r² et assurer extension r=0. Ne pas injecter arbitrairement des jets / geler z.
3. Fixation globale et compatibilité conditions de jauge/bords, oracle Poisson indépendant NON-IBP six-paires, rang Dirac complet, charts exceptionnelles K=0,J=0 ; BD et 4D encore OUVERTS.
4. Après chaque résultat créer code + tests + JSON + audit GitHub sur seule branche, et préfixer ce fichier sans perdre les centaines de kilooctets d'historique.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68m TERMINÉE APRÈS STEP68l (2026-10-25)

**SEULE BRANCHE D'ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. Préserver `main` et `research/v2-flrw` et NE PAS RÉACTIVER GitHub Actions/workflows. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**LIRE D'ABORD :** `research/STEP68M_CERTIFIED_POSITIVE_RADIAL_U_SLOPE_ANNULUS.md`, puis `research/STEP68L_CERTIFIED_100X_REFINED_GLOBAL_RADIAL_BARRIER.md`.
**CODE STEP68m EXÉCUTÉ, GIT BLOB IDENTIQUE :** `numerics/hr_step68m_positive_radial_slope.py`, SHA `639c88563411ad6d69298f36cf878f46c0e7be79`.
**5 TESTS STEP68m VRAIMENT PASSÉS (46.07s), BLOB IDENTIQUE :** `tests/test_hr_step68m_positive_radial_slope.py`, SHA `bbba6eee09b81c7932a81b55d3c03739a11ef71b`.
**RAPPORT RATIONNEL BRUT :** `research/reports/gate2b-step68m-certified-positive-radial-slope.json`, Git blob `b3ef2cdc0b187df12a671c1bd276e4142eb73495`.
**PYTEST BRUT :** `research/reports/gate2b-step68m-pytest.log`, Git blob `9517377423e1e99b4cdf66fb17af73ea18b837f4`.

## NOUVELLE CERTIFICATION DE MONOTONIE SUR LA VRAIE BRANCHE ORIGINALE STEP55

En s'appuyant sur le certificat Step68l global `|U(s)-Ustar(s)|<=1e-6`, **le programme Step68m REEXECUTE ENCORE CE CERTIFICAT EXACT** depuis les quatre sources originales physiques Step45/46/55normal/55global, SHA octet-identiques. Puis il utilise la vraie EDO `2*s*U_s=G(s,U)-2U` et l'arithmétique entière orientée historique `I, S=10^28` pour évaluer les dérivées de U sur **8192 cellules rationnelles** couvrant **TOUT** le sous-domaine fermé `s in [1/64,289/400]` (`r in [1/8,17/20]`).

```
STRICT exact lower U_s >=
2616650086463031354471/1250000000000000000000000000
≈ 2.093320069170425e-6 >0

STRICT exact upper U_s <=
30880835985796069042583/19531250000000000000000000
≈ 0.0015810988024727588
```

Donc sur **TOUTE LA VRAIE BRANCHE RADIALE** : `U_s>0` pour **CHAQUE** r de `[0.125,0.85]`, pas des points isolés. Les tests de provenance, mutation de la preuve, refus de résolution grossière et refus de paramètres non couverts ont PASSÉ ; les 4 nouveaux blobs source/test/rapport/log sur GitHub ont été relus et sont strictement identiques aux fichiers exécutés.

**LIMITES :** Ce certificat NE COUVRE PAS r in [0,0.125) par cette méthode divisant par s ; même si `U_s(0)=U1>0` par Taylor et qu'un voisinage existe, PAS de borne explicite réconciliant les deux domaines. NE prouve A_N,A_M temporels, M/N positif global, rang de Dirac, fantôme BD ou théorie 4D.

## STEP68l A LIRE CI-DESSOUS : TUBE 100× PLUS PRÉCIS

Step68l a VRAIMENT prouvé à 16 384 cellules fermées : `|U-Ustar|<=1e-6` pour TOUT 0<=r<=0.85 et encadré exactement `V=G(s,U)=pLf'/r` avec `|V-Vstar|<1/20000`, en resserrant l'original Step55 de 100× (ancien deltaU 1e-4). Huit tests Step68l PASSÉS (39.18s) et blobs GitHub authentifiés. Les résultats d'origine Step68k et la suppression algébrique des lapses dérivés Step68j/h ne sont PAS remaniés.

## NEXT STEP68n — VERROU TEMPORAL DÉCISIF

1. Utiliser le tube continu amélioré `Ustar±1e-6`, la borne exacte `V=G(s,U)` et `U_s>0` pour r>=1/8 afin de construire les dérivées complètes q'', q''' etc avec AD d'intervalles, en conservant les deux poussières, la variation de z,z' et le vrai Step58.
2. CERTIFIER ou RÉFUTER `A_N>0,A_M<0` du VRAI crochet temporel sur la solution NON HOMOTHÉTIQUE Step55 pour TOUT 0<r<=0.85, en séparant les zones r<1/8 et r=0 à l'aide des séries certifiées centrales U0..U3. L'ancien M/N ~0.519 est numériquement favorable mais NON CERTIFIÉ.
3. Ensuite étudier globalement la jauge et les lapses positifs, les conditions aux bords, le rang de Dirac et l'oracle Poisson NON-IBP à six couples, ainsi que les charts exceptionnelles K=0,J=0. Si l'intervalle de A_N ou A_M inclut 0, NE PAS conclure : raffiner la preuve / publier l'obstruction exacte.
4. A CHAQUE nouvelle avancée préfixer ce checkpoint et préserver l'historique entier ; n'écrire que sur branche active, GitHub Actions OFF. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED**.

---

# JANUS — REPRISE PRIORITAIRE : STEP68l CERTIFIÉE (2026-10-25)

**BRANCHE EXCLUSIVE EN ÉCRITURE** `research/gate2b-nonhomothetic-transfer`. NE PAS TOUCHER `main` ni `research/v2-flrw`. GitHub Actions/workflows utilisateur restent DÉSACTIVÉS. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**DÉBUTER PAR :** `research/STEP68L_CERTIFIED_100X_REFINED_GLOBAL_RADIAL_BARRIER.md`.
**CODE EXÉCUTÉ, GIT BLOB IDENTIQUE :** `numerics/hr_step68l_refined_global_barrier.py` SHA `2a1ffc026a30abf41208b44a707dc869daf0929d`.
**8 TESTS EXÉCUTÉS ET RÉUSSIS (39.18s), GIT BLOB IDENTIQUE :** `tests/test_hr_step68l_refined_global_barrier.py` SHA `0b117a8e13cf0bd7344da4c31d0edcb3148c957e`.
**RAPPORT MACHINE D'INTERVALLES EXACTS ORIGINAL LOCAL, GIT BLOB IDENTIQUE :** `research/reports/gate2b-step68l-refined-global-barrier.json` SHA `b0e698809d0f89d1bc9e618d100e22f1241daced`. **TRACE PYTEST EXACTE :** `research/reports/gate2b-step68l-pytest.log` SHA `d4fad6d097cdb8ae87bec90511c2c0e63eba9c2a`.

## NOUVELLE PREUVE CERTIFIÉE : TUBE SPATIAL GLOBAL 100× PLUS ÉTROIT SUR BRANCHE STEP55

**QUATRE ORIGINAUX PHYSIQUES RECONSTITUÉS À L'OCTET IDENTIQUE :** Step45 `66aa438...`, Step46 `bac025c...`, Step55-normalisé `a54a6ac...`, Step55-global `a6e7004...`. Le certificat NOUVEAU utilise les opérateurs originaux d'arithmétique entière à arrondi externe `I` (`S=10^28`), la vraie source `G(s,U)`, la même géométrie, les mêmes coefficients centraux `U0,U1,U2` et le même argument de comparaison/continuation de Step49–55. **Pas d'échantillonnage**, 16 384 cellules EXACTES fermées couvrant le continuum `s=r² in [0,289/400]`.

```
Ustar(s)=U0+U1*s+U2*s² (IDENTIQUE au polynôme ancien)
delta=1/1_000_000 = 1e-6 (ANCIEN Step55: delta=1e-4)
strict upper Fplus <= -52329410075807340297/78125000000000000000000000 <0
strict lower Fminus >= 5825322396515812909051/10000000000000000000000000000 >0
=> POUR LA VRAIE SOLUTION ANALYTIQUE CENTRALE GLOBALE: |U-Ustar| <= 1e-6
   sur tout 0<=r<=17/20=0.85 ; amélioration certifiée ×100.
```

Nouvelle enceinte exacte de vitesse `V=G(s,U)=pLf'(r)/r`, `Vstar=2U0+4U1*s+6U2*s²` :
```
-106551452922242719145541/5000000000000000000000000000
  <= V-Vstar <=
 212228180149451453699149/10000000000000000000000000000.
```
Donc `|V-Vstar|<1/20000=5e-5` sur tout le continuum, contre hypothèse de 0.01 historique. Source et tests GitHub relus strictement identiques octet pour octet aux fichiers locaux réellement exécutés.

**CONTROLE NEGATIF :** `delta=1e-6` sur l'ancien maillage de 8192 cellules échoue EXACTEMENT au slab 0 avec intervalle recouvrant zéro : insuffisance de résolution INTERVALLE, pas une obstruction de l'EDO. 16384 cellules strictement réussies. Le polynôme Ustar n'a PAS été modifié avec U3 ; ce gain provient seulement de l'augmentation du nombre de cellules et de l'ancienne preuve physique.

**CE QUI RESTE NON PROUVÉ :** Ni `A_N>0`, ni `A_M<0` sur la vraie branche non homothétique, ni le rang Dirac complet, ni la fixation des lapses ni la dynamique 4D n'ont été établis par cette étape. Les identités STRUCTURELLES `B_N=B_M=0` sur les contraintes (Steps68h/68j) et le témoin HOMOTHÉTIQUE à lapses positifs Step68k sont conservés et ne suffisent PAS à la branche Step55.

## PROCHAINE STEP68m, VERROU RÉEL

1. Brancher le nouveau tube GLOBAL `Ustar±1e-6`, `Vstar±5e-5` dans l'opérateur temporel ORIGINAL Step58 avec les champs radiaux et jets ENTIERS de Step55, puis CONSTRUIRE arithmétique d'intervalles/AD valide pour `A_N,A_M`. Commencer par des cellules STRICTEMENT éloignées de r=0 ; séparer la limite centrale r→0 et ses facteurs r².
2. Chercher certification stricte des signes `A_N>0,A_M<0` **SUR LE CONTINUUM UNIQUE**, puis `M/N=-A_N/A_M>0`, contrôle de stabilité sous la variation de `U` et conditions aux bords ; si les bornes se recouvrent, affiner le calcul AD/les cellules plutôt que proclamer le signe.
3. Oracle Poisson temporel INDEPENDANT non-IBP sur six couples, rang Dirac global, chartes K=0/J=0 et absence BD. NE PAS confondre la nouvelle preuve SPATIALE avec la fermeture temporelle.
4. Vérifier sources Git et préserver en PRÉFIXE les ~250k caractères d'historique. GitHub Actions OFF, branches main/v2-flrw intouchées.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68k, PUIS STEP68j (2026-10-25)

**SEULE BRANCHE AUTORISÉE À L'ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. Les branches `main`, `research/v2-flrw` et GitHub Actions DÉSACTIVÉES demeurent intouchées. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**LIRE EN PRIORITÉ :** `research/STEP68K_EXACT_POSITIVE_LAPSE_FLAT_FAMILY_AUDIT.md` pour le résultat nouveau, puis `research/STEP68J_EXACT_FULL_CDOT_BN_SECONDARY_IDENTITY_AUDIT.md` pour la preuve structurelle générale des annulations de N',M'.
**CODE STEP68k :** `numerics/hr_step68k_exact_positive_lapse_family.py`, Git blob `5e8783eec4f342cc29b7208ad6cdeb1d7df9cbd2`.
**18 TESTS STEP68k :** `tests/test_hr_step68k_exact_positive_lapse_family.py`, Git blob `c9c53a6123c84e2310f3fcb52c4b185d18d92410`. VRAIMENT **18 passed in 11.14s** après correction d'une comparaison syntaxique SymPy d'expressions mathématiquement égales.
**RAPPORT MACHINE :** `research/reports/gate2b-step68k-exact-positive-flat-family.json`, Git blob `7beda486cd587303df8b376c946b7f8a82f94d8a`.
**SOURCE DES RÉSULTATS STRUCTURELS STEP68j :** `numerics/hr_step68j_BN_exact_secondary_identity.py` SHA `a500cdb1a09c853d46848719e26be9bbec55fb64` ; `tests/test_hr_step68j_BN_exact_secondary_identity.py` SHA `44a84c5b5aa234ae719fa2e6f818456985c2dad9` ; rapport `research/reports/gate2b-step68j-original-BN-C-identity.json` SHA `25a47c7eeed9dec111ecd3f5da891a02d84184d9`. TOUS les blobs ci-dessus relus sur GitHub et byte-identiques aux fichiers exécutés.

## NOUVEAU THÉORÈME STEP68k : LAPSUS POSITIFS SUR UNE FAMILLE SPATIALE PLATE HOMOTHÉTIQUE EXACTEMENT CONTRAINTE

Les HUIT sources ORIGINALES Step45/46/55normal/55global/57/58/59/60 sont authentifiées SHA Git avant calcul, et les vrais opérateurs Step45/58 sont exécutés dans le même runtime. Sur la famille spatiale CANONIQUE HOMOTHÉTIQUE plate, qui N'EST PAS la solution non homothétique Step55 :
```
Mg²=Mf²=m²=1 ; Lg=Lf=1 ; Sg=Sf=r ;
pLg=pLf=pSg=pSf=0 ; z=0 ; theta_g=theta_f=const ;
p_g=r²*rho_g, p_f=r²*rho_f ;
T=beta1+2 beta2+beta3 ;
rho_g= -(beta0+3 beta1+3 beta2+beta3) ;
rho_f= -(beta1+3 beta2+3 beta3+beta4).
```
La contrainte de shift K=r² T>0 dès r>0,T>0. Le vrai ORIGINAL vérifie EXACTEMENT à TOUT rayon r>0 : `Fz=Hg=Hf=C=Dg=Df=0` et les SIX dérivées premières radiales égales à zéro ; tous jets canoniques jusqu'à 4 calculés analytiquement à partir du profil. Le vrai Cdot Step58 donne
```
A_N = +3/2*r²*T*(rho_g+2T) > 0
A_M = -3/2*r²*T*(rho_f+2T) < 0
B_N=B_M=coeff_N''=coeff_M''=0
=> dot C = 3/2*r²*T * [(rho_g+2T)*N-(rho_f+2T)*M].
=> M/N = (rho_g+2T)/(rho_f+2T)>0,
```
si `r>0,T>0,rho_g>0,rho_f>0`. Le rapport est constant en r et a limite régulière comme quotient r²/r² au centre (attention chart K(0)=0 non résolu en variables canoniques).

TÉMOIN RATiONNEL EXACT : `(beta0,beta1,beta2,beta3,beta4)=(-5,1,0,0,-5)`, `T=1,rho_g=2,rho_f=4`, `dot C=r²(6N-9M)`, positif `N=3,M=2`, ratio `M/N=2/3` pour TOUT r>0 sur cette famille spatiale. Régularité 4D et évolution complète/non-IBP non démontrées. Cette famille est HOMOTHÉTIQUE ET LE CHOIX DE beta DIFFÈRE DU BENCHMARK Step55 ; ne PAS en déduire les signes de la branche Janus non homothétique cible.

**PREUVE STRUCTURELLE STEP68j RETENUE :** sur `Fz=0,K>0`, le vrai coefficient temporel `B_N=-(1-z²)/(Lg Lf)*Hgprime+beta*Hg+(z/Lg)*C`, certifié par 25 dérivées symboliques indépendantes et référence `C=-53/40 !=0`. Donc `B_N=0` sur `Hg=Hgprime=C=0`. Step68h certifie `B_M=3z(z²-1)/(Lg Lf²)*Fzprime` et `B_M=0` sur `Fzprime=0`. Step58 certifie coefficients de N'',M'' nuls sur Hg,Fz. Donc TEMPORAL Cdot sur shell se réduit EXACTEMENT à `A_N N + A_M M`. Les coefficients A_N,A_M du Step55 global n'ont ENCORE AUCUN certificat par intervalles.

## NEXT HARD RED STEP68l — VOIE VERS CONCLUSION

1. Sur le VRAI profil non homothétique positif Step55 (pas la famille homothétique de contrôle), prouver/certifier par intervalles l'évaluation complète des coefficients `A_N,A_M` sur les 256 cellules rationnelles, avec AD de `U(s)` solution ODE et bornes sur tous ses jets ainsi que paramètres. Isoler le centre r=0 avec la régularité normalisée, calculer rang local et signe `M/N=-A_N/A_M` **sur toute la branche**.
2. Vérifier les équations de préservation des autres contraintes, conditions aux bords, choix de jauge, et existence de lapses globaux positifs. Les 17 rayons Step68f et leur ratio ~0.519 positif restent des évaluations numériques exploratoires, NON des intervalles.
3. Oracle ORIGINAL temporel Poisson NON-IBP indépendant sur 6 couples, rang Dirac complet, chartes `K=0,J=0`, fantôme BD, cosmologie 4D. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.
4. Continuer à PRÉFIXER ce journal de reprise en conservant l'historique existant ci-dessous. Aucune exécution asynchrone une fois la réponse terminée.

---

# JANUS — REPRISE PRIORITAIRE : STEP68j CERTIFICAT ORIGINAL COMPLET (2026-10-25)

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. `main` et `research/v2-flrw` restent intouchées. Ne réactiver AUCUN GitHub Actions/workflow. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68J_EXACT_FULL_CDOT_BN_SECONDARY_IDENTITY_AUDIT.md`.
**SOURCE PROUVANT LA NOUVELLE IDENTITÉ :** `numerics/hr_step68j_BN_exact_secondary_identity.py`, Git blob `a500cdb1a09c853d46848719e26be9bbec55fb64` VERIFIÉ identique au fichier exécuté.
**TESTS RÉELS :** `tests/test_hr_step68j_BN_exact_secondary_identity.py`, Git blob `44a84c5b5aa234ae719fa2e6f818456985c2dad9` VERIFIÉ identique au fichier exécuté.
**CERTIFICAT DES 25 DÉRIVÉES :** `research/reports/gate2b-step68j-original-BN-C-identity.json`, SHA blob `25a47c7eeed9dec111ecd3f5da891a02d84184d9`. Contient les noms des 25 variables, chaque dérivée EXACTEMENT NULLE, ancrage `C=-53/40` et test du mauvais signe.

## VERROU B_N LEVÉ EXACTEMENT AU NIVEAU DE LA CHARTE PHYSIQUE ET DES CONTRAINTES

Les VRAIES sources originales Step45/57/58/59/60 sont toutes importées et SHA authentifiées dans `/mnt/data/janus-step68f` avec les modules précédents. Leur vrai coefficient du crochet temporel à six couples `B_N=[dot C]_(N')` vérifie, sur `Fz=0` (charte `K>0,|z|<1,Lg Lf Sg Mg² nonzero`) l'IDENTITÉ EXACTE :
```
alpha=(1-z²)/(Lg Lf)
beta= [partial_(Sg'') (B_N + alpha Hgprime)]/[2 Mg² Sg/Lg]
B_N = -alpha*Hgprime + beta*Hg + (z/Lg)*C .
```
PREUVE : Step60 élimine jets q''' avec Hgprime ; Step68i élimine les 12 jets q'' avec beta Hg. Step68j construit `T=(B_N+alpha Hgprime-beta Hg)-(z/Lg)*C` sur Fz=0 et prouve EXACTEMENT toutes les 25 dérivées indépendantes `dT/dx=0` (numérateur symbolique expansé ZÉRO), plus référence rationnelle régulière `T=0` et **C=-53/40 NON NUL**, excluant toute annulation fabriquée en posant C=0. Mauvais signe devant `zC/Lg` explicitement réfuté. D'où **B_N=0** sur `Fz=Hg=Hgprime=C=0`. À Step68h, `B_M=3z(z²-1)/(Lg Lf²)*Fzprime`, donc **B_M=0** sur `Fz=Fzprime=0`. Étape 58 avait annulé `N''`,`M''` sur `Fz=Hg=0`. Ainsi, sur ces contraintes du système SPHÉRIQUE à six paires, le crochet temporel local se réduit EXACTEMENT à `dot C=A_N N+A_M M` ; **les coefficients A_N,A_M et leur rang/compatibilité globale ne sont PAS encore certifiés**.

**EXÉCUTION RÉELLE DES VÉRIFICATIONS PAR GROUPES :** 4 tests Pytest réussis (13 jets + ancrage/sanity), 1 test métriques A (2 variables) réussi, 1 test métriques B (2 variables) réussi. Le groupe des 8 couplages/z a été vérifié à terminaison normale directement par `group_certificate('couplings_and_z')`. Une tentative Pytest de ce groupe a affiché `1 passed` MAIS dépassé ensuite la limite de sortie ; elle n'est PAS comptée comme succès Pytest terminé. Ces groupes couvrent précisément 13+2+2+8=25 dérivées EXACTES ; aucune suite Pytest combinée n'est revendiquée. Voir détails et commandes dans l'audit Step68j.

## PROCHAINE PRIORITÉ STEP68k — SIGNES ET LAPSES (DÉCISIF)

1. Sur la **vraie branche intégrée et certifiée depuis r=0** Step55 (PAS seulement `U(s0)=Ustar(s0)+offset` de Step68f), démontrer ou certifier par intervalles les signes exacts `A_N>0,A_M<0` pour `0<r<=0.85`, et limites centrales `A_N/r²,A_M/r²` non nulles et régulières ; traiter les garanties d'erreur de troncature et paramètres rationnels, poussières.
2. Alors `M/N=-A_N/A_M>0` deviendrait une conclusion compatible LOCALEMENT, mais reste à traiter toutes les primaires de temps, conditions de bord/gauge, existence de lapses positifs et normalisation globale. Sur 17 rayons Step68f : ratio positif NUMÉRIQUE ~0.51855..0.52112 ; ce n'est PAS un certificat continuum.
3. Construire oracle Poisson ORIGINAL six-couples NON intégré par parties, analyser rang complet de Dirac, chartes K=0/J=0, fantôme BD et théorie 4D. **TOUJOURS OUVERTS — JANUS_R NOT_VALIDATED**.
4. Conserver les anciens 230k caractères ci-dessous, les SHA et les fichiers de reprise ; après chaque étape préfixer ce fichier. Aucun travail en arrière-plan en dehors des sessions explicites.

---

# JANUS — REPRISE PRIORITAIRE : STEP68i ACHEVÉE (2026-10-25)

**BRANCHE EXCLUSIVE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. Laisser `main` et `research/v2-flrw` INTACTES. GitHub Actions/workflows utilisateur restent DÉSACTIVÉS. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE D'ABORD :** `research/STEP68I_EXACT_FULL_CDOT_BN_LOWER_JET_QUOTIENT_AUDIT.md`.
**SOURCE NOUVELLE EXÉCUTÉE ET GIT BYTE IDENTIQUE :** `numerics/hr_step68i_BN_lower_jet_quotient.py` SHA `2ffc0f4bb65615836c25c5af83d905bd8b94783a`.
**NOUVEAUX TESTS :** `tests/test_hr_step68i_BN_lower_jet_quotient.py` SHA `94253af441672db15387f7dc6d6c049c5c4c8e4d`.
**RAPPORT MACHINE :** `research/reports/gate2b-step68i-BN-lower-jet-quotient.json` SHA `49f1158cd1e9583a29cc583c30c8d96fe1dcd3b6`.
**RÉSULTAT ANTÉRIEUR IMMEDIAT CRUCIAL :** Step68h a démontré EXACTEMENT pour le vrai six-pair Cdot `B_M = 3z(z²-1)/(Lg Lf²)*Fz'` sur `Fz=0,K>0` ; **B_M=0** sur `Fz=Fz'=0` SANS imposer Hg,Hf,C. Le rapport scientifique `research/STEP68H_EXACT_ORIGINAL_FULL_CDOT_BM_IDENTITY.md` et ses 24 dérivées symboliques sont conservés ci-dessous.

## AVANCÉE STEP68i : VRAI COEFFICIENT DE N' SANS AUCUN JET CANONIQUE D'ORDRE 2/3

L'ORIGINAL physique Step60 donne sur Fz=0 le coefficient complet après élimination exacte des 12 jets q''' avec la dérivée COMPLETE Hg' :
```
tilde_B_N = B_N + (1-z²)/(Lg Lf) * Hgprime
```
Ce représentant contient APPAREMMENT `Lg'',pLg'',Sg'',theta_g''`. Leurs dérivées EXACTES satisfont `partial_Lgrr=partial_pLgrr=partial_tgrr=0` ; une seule reste, celle de `Sg''`. Depuis l'original Step45, `partial Hg / partial Sg'' = 2 Mg² Sg/Lg`, non nul sur la charte `r>0,Sg>0`.

Définir **exactement** :
```
beta = [partial_(Sg'') tilde_B_N] / [2 Mg² Sg/Lg]
R_BN = B_N + (1-z²)/(Lg Lf)*Hgprime - beta*Hg .
```
Le calcul EXÉCUTÉ prouve **partial_(q_i'') R_BN=0 pour les 12 canoniques ET absence des 12 jets q_i'''**, sur Fz=0 ; un vrai représentant ne contenant que q,q',z,z' est construit et testé. Le mauvais signe de beta restitue une dépendance non nulle à Sg''. La source calcule beta (725 opérations) et conserve le hash SHA256 de son `srepr` `dfdc84fd8cf3b29ede2f2c320a901abd8239325bf0dc8ca6893d394f2824c095`.

**CE QUI RESTE OUVERT :** contrairement à B_M, `R_BN` est NON NUL génériquement HORS des autres contraintes : le test négatif sur variables canoniques libres le prouve. Sur le jet physique radial Step55 à r=0.4, il tend numériquement à zéro, MAIS `R_BN=0` sur le système complet n'est PAS démontré. Le coefficient beta contient 1/Sg, sa normalisation régulière au centre r=0 est aussi non prouvée. Aucun verdict sur rang de Dirac ou fantôme BD.

**TESTS RÉELLEMENT PASSED :** Step68i 9 PASSED en 13.51s ; Steps68e/f/g/h 49 PASSED dans un processus séparé en 31.86s. Une tentative de les concaténer en une suite de 58 tests a EXPIRÉ à 180s et NE DOIT PAS ÊTRE PRÉSENTÉE COMME PASSÉE. HUIT originaux physiques historiques Step45/46/55normal/55global/57/58/59/60 déjà réunis byte-identiques et leurs certificats conjointement rejoués. Aucun CI activé.

## NEXT STEP68j HARD RED

1. Eliminer algébriquement les DERNIÈRES dépendances q,q',z,z' du R_BN modulo `Hg,Hf,Ddiag,Fz,C` et leurs prolongations. Etablir, ou réfuter via contre-exemple physique, `B_N=0` sur tout le secteur initial positif Step55 ; privilégier éliminations variables linéaires/coefficients séparés, car substitution globale naïve SymPy a time-out.
2. Certifier par INTERVALLES sur la VRAIE trajectoire globale du centre les signes `A_N>0`, `A_M<0`, la régularité centrale du rapport `M/N` et les conditions aux bords. Les 17 rayons Step68f et leur ratio positif ~0.51855..0.52112 sont NUMÉRIQUES, PAS une preuve.
3. Calcul indépendant original Poisson NON intégré par parties, toutes six paires, puis rang Dirac, lapse fixing, charts exceptionnels K=0,J=0 et BD. **GATE_2B OPEN — JANUS_R NOT_VALIDATED**.
4. CONTINUER À PRÉFIXER ce fichier avec chaque nouvelle avancée, tout en préservant intégralement son historique.

---

# JANUS — REPRISE PRIORITAIRE : STEP68h CERTIFICAT ANALYTIQUE ACHEVÉ (2026-10-25)

**BRANCHE D'ÉCRITURE EXCLUSIVE** `research/gate2b-nonhomothetic-transfer`. `main` et `research/v2-flrw` intouchées, Actions/workflows utilisateur restent DÉSACTIVÉS. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**LIRE D'ABORD :** `research/STEP68H_EXACT_ORIGINAL_FULL_CDOT_BM_IDENTITY.md`.
**CODE EXÉCUTÉ ET GIT BLOB VÉRIFIÉ :** `numerics/hr_step68h_BM_global_identity.py`, SHA `991eeb0e1b557a65964ca0157c0577ce7524dcfc`.
**8 TESTS SPÉCIFIQUES :** `tests/test_hr_step68h_BM_global_identity.py`, SHA `4cdd3fce5b385e77894cac4e29e58386dbf1995b`.
**CERTIFICATS BRUTS :** `research/reports/gate2b-step68h-original-BM-identity.json`, `research/reports/gate2b-step68h-24-derivative-certificate.json`. Tous fichiers publiés relus byte-identiques à l'exécution locale.

## NOUVEAU THÉORÈME EXACT : UN COEFFICIENT DE DERIVÉE PREMIÈRE DU LAPSE DISPARAÎT

Dans l'ORIGINAL complet Step58 six-couples avec deux poussières, coefficient `B_M=[dot C_red]_(M')`. Dans la charte `K>0,|z|<1,Lg Lf nonzero`, avec `Fz=Dg-Kz/sqrt(1-z²)` :

```
lambda = 3*z*(z²-1)/(Lg*Lf²) = -3*z*(1-z²)/(Lg*Lf²)
EXACTEMENT SUR Fz=0 : B_M = lambda * Fz'
=> EXACTEMENT SUR Fz=Fz'=0 : B_M=0 .
```

Ceci est un résultat ANALYTIQUE nouveau, PAS une observation numérique Step68f. Il NE requiert PAS `Hg=Hf=C=0`. Preuve dans code : partir du quotient Step68g `R_BM=B_M-lambda Fz'`, dont les 12 dépendances q'' avaient été éliminées exactement. Les 24 symboles INDEPENDANTS restants du représentant sont TOUS dérivés ; chaque numérateur rationnel de chaque dérivée s'expanse EXACTEMENT à ZÉRO. Valeur en point rationnel régulier (z=3/5, sqrt=4/5, autres paramètres simples) EXACTEMENT 0. Donc le représentant est nul sur la branche analytique régulière physique. Oracle indépendant : on résout `Fz=0` pour `pLg'`, `Fz'=0` pour `pLg''`, et le vrai `B_M` vaut EXACTEMENT ZÉRO tout en conservant `Hg=357/80`, `Hf=33/10+11sqrt(2)/10`, `C=-247/200` **NON NULS**. Test négatif mauvais signe nonzero.

**SUITE INTÉGRÉE VRAIMENT EXÉCUTÉE : 49 passed in 31.86s** avec ordre de tests
```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q \
 tests/test_hr_step68e_exact_shift_full_lapse_response.py \
 tests/test_hr_step68f_joint_profile.py \
 tests/test_hr_step68g_full_Cdot_Mprime_quotient.py \
 tests/test_hr_step68h_BM_global_identity.py
```
(18+13+10+8 tests). L'ordre inverse a atteint un timeout avant conclusion ; seul le passage COMPLET de 49 tests est retenu. Les HUIT sources historiques originales Step45/46/55normal/55barrier/57/58/59/60 sont déjà reconstituées, SHA vérifiées et exécutées ENSEMBLE avec le certificat spatial global Step55 256 cellules. Reprise de leurs preuves/nombres et des indicateurs de ratio M/N numérique dans `research/STEP68F_68G_ORIGINAL_JOINT_TEMPORAL_LAPSE_AND_EXACT_MPRIME_QUOTIENT.md`.

## PROCHAINE STEP68i — TEST DE RANG TOUJOURS CRUCIAL

1. Réduire analytiquement le coefficient TEMPOREL `B_N=[dot C]_(N')`, après élimination des jets q''' par `Hg'` comme dans original Step60, puis des jets q'' par les dérivées COMPLETES `Fz',Hg',C',Hf',Ddiag'`. NE PAS fixer les jets arbitrairement. Chercher un certificat du type Step68h : dérivées symboliques nulles et point rationnel exact.
2. Sur la VRAIE solution globale unique du centre Step55, et pas uniquement les jets LOCAUX de Ustar du Step68f, certifier par calcul rationnel/intervalle `A_N>0`, `A_M<0` et existence d'une limite régulière `M/N=-A_N/A_M` vers r=0. Les 17 points numériques favorables précédents NE VALENT PAS une preuve globale.
3. Etudier compatibilité avec contraintes primaires de temps, gauge, conditions aux bords ; construire oracle Poisson NON-IBP indépendant original six-couples, analyser rang de Dirac et secteur K=0/J=0. **JUSQU'ALORS : JANUS_R NOT_VALIDATED**.
4. Continuer à préfixer ce fichier à chaque accomplissement et conserver l'historique précédent sans le supprimer.

---

# JANUS — REPRISE PRIORITAIRE : STEP68g ACHEVÉE APRÈS STEP68f (2026-10-25)

**SEULE BRANCHE MODIFIABLE :** `research/gate2b-nonhomothetic-transfer`. Ne toucher ni `main` ni `research/v2-flrw`. GitHub Actions/workflows demeurent DÉSACTIVÉS. **GATE 2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE ABSOLUMENT :** `research/STEP68F_68G_ORIGINAL_JOINT_TEMPORAL_LAPSE_AND_EXACT_MPRIME_QUOTIENT.md`.
**SYNTHÈSE MACHINE :** `research/reports/gate2b-step68f-68g-integrated-status.json`.
**NOUVELLE SOURCE PHYSIQUE EXÉCUTÉE :** `numerics/hr_step68f_physical_pointwise.py` SHA Git blob `82e1ebb3a290f54a0d3b5069df67504044381626`.
**NOUVEAUX TESTS DE RACCORDEMENT :** `tests/test_hr_step68f_joint_profile.py` SHA Git blob `5d423b4d646c6c3ac4d28884e3116bf56a35bde0`.
**NOUVEAU THÉORÈME SYMBOLIQUE EXACT :** `numerics/hr_step68g_full_Cdot_Mprime_quotient.py` SHA Git blob `2245403862795569d3d6215aeb5e6227ee1148d6`.
**TESTS DE CE THÉORÈME :** `tests/test_hr_step68g_full_Cdot_Mprime_quotient.py` SHA Git blob `5afc5b52e260532eb94e8ecec940354eb3f12d9d`.

**IMPORTANT : HUIT MODULES PHYSIQUES ORIGINAUX TESTÉS ENSEMBLE OCTET IDENTIQUES À GITHUB** dans `/mnt/data/janus-step68f/numerics` : Step45, Step46, Step55normal, Step55global, Step57, Step58, Step59, Step60. Voir source hashes exacts dans `research/reports/gate2b-step68f-68g-integrated-status.json`. Les certificats physiques 45/46/55/57/58/59/60 ont RÉELLEMENT PASSÉ dans le même process, incluant certificat spatial global Step55 256 cellules et ses marges rationnelles strictes d'origine. Trace GitHub : `research/reports/gate2b-step68f-original-eight-module-joint.json`.

## AVANCÉE SÉRIEUSE : PREMIER COEFFICIENT TEMPORAL NUMÉRIQUE ÉVALUÉ SOUS LES CONTRAINTES

À rayon `r>0`, choisir un point `U(s0)=Ustar(s0)+offset` dans la barrière certifiée Step55 ; déterminer `U_s,U_ss,U_sss` depuis le vrai second membre original `G(s,U)` et ses dérivées, pas par différentiation arbitraire de Ustar. Tous les champs canoniques à six couples, les moments poussière, `z,z',z''` et jets radiaux jusqu'à l'ordre 4 sont construits selon les sources physiques originales. L'original Step58 calcule le VRAI crochet temporel `Cdot` avec la réponse du shift non figée.

```
r=0.4 ; précision mpmath 55 chiffres :
contraintes Fz,Hg,Hf,C,Hg',C' : |résidu| < 2e-54
coefficient N0 de Cdot : +556.3983109239983805209505844...
coefficient M0 de Cdot : -1071.784882043146390125740547...
coefficients N',M',N'',M'' : ~1e-54
rapport local candidat M/N = +0.519132449287150599440043197596...
```

À 17 rayons DISTINCTS observés sur `0.05≤r≤0.85`, les signes `A_N>0,A_M<0` et `M/N>0` persistent numériquement ; valeurs observées `M/N ≈ 0.518552348... à 0.521119909...`. À `r=0.4`, décalages `Ustar±1e-5` préservent le signe positif. Contrôle négatif : ajout volontaire `pSf+=0.001` rompt Hf,C et crée `B_N ≈ -0.000733887` ; les annulations ne sont pas constantes hors contraintes. Données BRUTES ET BYTE-COPIÉES sur GitHub :

- `research/reports/gate2b-step68f-physical-highprecision-scan.json` ;
- `research/reports/gate2b-step68f-extended-radius-scan.json` ;
- `research/reports/gate2b-step68f-negative-off-primary.json`.

**LIMITATION MAJEURE :** ces jets sont des SOLUTIONS LOCALES de l'EDO à un rayon choisi, initialisées à `Ustar+offset`, mais pas une preuve qu'ils appartiennent à la trajectoire UNIQUE exactement prolongée du centre. Les signes/ratios de l'opérateur temporel ne sont PAS encadrés uniformément par intervalles. Les dizaines de décimales décrivent seulement la stabilité arithmétique de l'évaluation à ce point, PAS une précision certifiée du véritable profil global. Il manque rang et bords.

## DEUXIÈME AVANCÉE — STEP68g : QUOTIENT COMPLET DU COEFFICIENT TEMPOREL M'

En utilisant le VRAI six-pair Step58, sur la stationnarité `Fz=0,K>0`, définir `B_M=[Cdot]_{M'}` et
```
lambda=3*z*(z²-1)/(Lg*Lf²)=-3*z*(1-z²)/(Lg*Lf²)
R_BM = B_M - lambda * Fz'
```
avec `Fz'` obtenu en dérivant la CONTRAINTE COMPLÈTE. Le calcul exact SymPy démontre **toutes les 12 dérivées `partial(R_BM)/partial(q_i'')=0` sur `Fz=0`**. Avant quotient, B_M dépend NON TRIVIALEMENT de `pLg'', Sg'', theta_g''` seulement. Mauvais signe ou omission de Fz' donne un résidu non nul. Sur `Fz=Fz'=0`, `R_BM=B_M`. Le produit `lambda Fz'` vaut `-3r³w(1-sw²)(3f+2sf_s)/(Lg Lf²)` avec `Fz=r³f(s)`, régulier au centre sous les parités. **ATTENTION : B_M=0 SUR TOUTE LA BRANCHE N'EST PAS ENCORE DÉMONTRÉ** ; ce quotient enlève uniquement les jets seconds.

**TESTS RÉELLEMENT EXÉCUTÉS ENSEMBLE : 41 PASSED en 16.48s** (13 nouveaux 68f, 10 nouveaux 68g, 18 précédents 68e) par `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68f_joint_profile.py tests/test_hr_step68g_full_Cdot_Mprime_quotient.py tests/test_hr_step68e_exact_shift_full_lapse_response.py`. Les 4 NOUVEAUX Git blobs source/test ont été relus identiques octet pour octet aux fichiers VRAIMENT exécutés.

## PRIORITÉ UNIQUE À LA REPRISE — STEP68h (HARD RED)

1. **NE PAS PERDRE LES 8 SOURCES ORIGINALes** : recharger leur liste/SHA depuis le rapport Step68f et vérifier hashes avant chaque nouveau calcul. Les modules original 63–65 peuvent être ajoutés en fonction des dérivées requises, mais ne bloquent plus le calcul conjoint de base.
2. **PROUVER AU LIEU D'ÉCHANTILLONNER** : réduire exactement `B_N,B_M` modulo `Fz,Hg,Hf,Ddiag,C,Fz',Hg',C'`, en partant du nouveau `R_BM` sans jets seconds. Déterminer s'ils sont identiquement nuls sur la branche admissible ou si une obstruction réelle survit.
3. Certifier uniformément les signes `A_N>0,A_M<0` et la limite `r→0` de leur quotient sur la VRAIE solution régulière globale Step55 (et non seulement des jets locaux `Ustar`). Employer intervalles/outward AD et rapports aux Steps62–65, avec tests de signe négatifs. Essayer le ratio `M/N` positif, mais NE PAS LE TENIR POUR ACQUIS.
4. Tester l'existence de lapses positifs avec conditions aux limites et gauge temporelle, oracle Poisson indépendant NON IBP à six couples, rang de Dirac complet, secteur exceptionnel K=0/J=0. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED**.
5. Après CHAQUE vraie avancée, publier code/tests/rapport dans GitHub sur la branche active, et PRÉFIXER ce fichier en conservant tous ses ~215K caractères historiques.

---

# JANUS — REPRISE ACTIVE : STEP68f — RÉSULTAT EXPÉRIMENTAL RÉEL (2026-10-25)

**ONLY WRITABLE BRANCH** `research/gate2b-nonhomothetic-transfer` ; preserve main, v2-flrw and disabled GitHub Actions. **GATE_2B OPEN, JANUS-R NOT_VALIDATED.**

**NOUVEAU RÉSULTAT PRIORITAIRE:** HUIT modules historiques ORIGINAUX Step45/46/55normal/55barrier/57/58/59/60 réunis byte-identiques au dépôt dans `/mnt/data/janus-step68f/numerics`, avec hashes authentifiés via `research/reports/gate2b-step68-source-preflight.json`. Leurs 7 certificats physiques originaux 45,46,57,58,59,60,55 ont TOUS été exécutés successivement dans le MEME processus local, **PASSED**, dont le certificat global Step55 256 cellules avec les deux marges exactes originelles et vérification des dérivées troisièmes Step60. Exécution totale environ 8.84s. Trace locale `/mnt/data/janus-step68f/research/reports/step68f-8module-original-joint.json` SHA256 `4c20479ef8a6fd448f34c432eeeadf70315f80bc668c577777682a832b3e74c8`.

**NOUVEAU TEST DU VRAI CROCHET TEMPOREL SUR DONNEES PHYSiQUES:** `/mnt/data/janus-step68f/numerics/hr_step68f_physical_pointwise.py`, SHA256 `fcfca8eaf2f6cede8ffa3e996b0bf700d4030f731df6fa37fc2acee1df78e403`; 8 SHA source originaux vérifiés avant chaque calcul. A rayons r=.2,.4,.6,.8, sur un jet local de l'EDO physique exacte Step55 initialisé à Ustar(s), primaires Fz,Hg,Hf,C et prolongations Hg',C' résidu ~1e-54 à mp.dps=55 ; B_N,B_M et coeff N'',M'' ~1e-54 ; MAIS A_N>0, A_M<0, non nuls. Exemple r=.4: A_N=556.39831092399838..., A_M=-1071.78488204314639..., M/N=0.519132449287150599..., avec B_N/B_M ~1e-54. Sur 17 rayons r=.05...0.85 (4 également high precision), ratio positif augmente de .518552348 (r=.05) à .521119910 (r=.85). Deux offsets Ustar±1e-5 à r=.4 conservent cette conclusion. Perturbation NON PHYSIQUE pSf+=.001 laisse C=-.18355984, Hf=.0003743 et B_N=-.0007339 (test négatif). **13 nouveaux tests intégrés PASSED en 14.97s**.

**AVERTISSEMENT CRUCIAL :** Les U(s0)=Ustar(s0)+offset sont des valeurs LOCALes dans la barrière Step55. Leurs dérivées U'(s0), U''(s0), U'''(s0) proviennent du véritable G(s,U) de Step55, mais ce ne sont PAS une trajectoire exactement intégrée sur tout [0,.85], ni des bornes par intervalles pour A_N,A_M, ni une preuve de rang de Dirac. Ratios numériques d'ordre inférieur prometteurs, besoins de preuve analytique et d'oracle indépendant. Les calculs interpolent des constantes Step55 `I` à leurs milieux rationnels; l'évaluation de `Cdot` utilise le symbole ORIG original Step58 lambdifié à 55 chiffres puis double dans test quadrillage. Les chiffres à 40 décimales ne sont PAS certifiés à ce nombre de décimales pour la branche originale (incertitudes du benchmark et du tube).

**ACTION IMMÉDIATE SI INTERRUPTION :** (1) lire présent en-tête et reprendre dossier local si toujours monté ; (2) publier/code complet `hr_step68f_physical_pointwise.py`, tests `test_hr_step68f_joint_profile.py` et rapports sur GitHub, vérifier blobs ; (3) démontrer que B_N=B_M=0 modulo contraintes, et encadrer A_N>0,A_M<0 sur la vraie branche Step55 (arithmétique d'intervalles/AD), puis étudier bords et lapses ; (4) oracle non-IBP six-paires indépendant, rang complet. **GATE_2B OPEN**.

---

# JANUS — REPRISE PRIORITAIRE : STEP68e TERMINÉE (2026-10-25)

**BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer` UNIQUEMENT. Ne modifier ni `main` ni `research/v2-flrw`. GitHub Actions/workflows DÉSACTIVÉS, à maintenir ainsi. **GATE_2B OPEN — JANUS-R NOT_VALIDATED.**

**LIRE D'ABORD** : `research/STEP68E_EXACT_SHIFT_FZPRIME_QUOTIENT_AUDIT.md`.
**CODE SCIENTIFIQUE RÉELLEMENT EXÉCUTÉ** : `numerics/hr_step68e_exact_shift_full_lapse_response.py`, Git blob `8f4e82bcec2b5c179f5c2d4e21ccb70f2828b206`.
**18 TESTS CIBLÉS** : `tests/test_hr_step68e_exact_shift_full_lapse_response.py`, Git blob `0f9aef7510d4e6d035405cf87820d28f032d0db0`.
**RAPPORT STRUCTURÉ** : `research/reports/gate2b-step68e-shift-Fzprime-quotient.json`.
**VRAI FOURNISSEUR PHYSIQUE ORIGINEL IMPORTÉ ET VÉRIFIÉ OCTET PAR OCTET** : `numerics/hr_step45_exact_physical_ward.py`, blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Les 9 résidus Ward physiques s'annulent exactement ; six couples originaux et deux poussières intégrés. SEUL Step45 original réellement réimporté dans ce workspace du tour ; anciens tests originaux 55/57/58/59/60 non rejoués ensemble.

## AVANCÉE DU TOUR : VRAI SHIFT COMPLET N,N',M,M' ET QUOTIENT Fz'

Depuis les vrais gradients d'Euler Step45, la variation du déplacement est reconstruite sur les SIX couples :
```
delta_H z = Z_N0*N + Z_N1*N' + Z_M0*M + Z_M1*M'.
```
Les coefficients en dérivées secondes et troisièmes des lapses dans CETTE VARIATION DE SHIFT s'annulent par le calcul (ne pas confondre avec le crochet Cdot complet). Sur la charte `Fz=0,K>0,|z|<1` on retrouve indépendamment l'étape 68d :
```
Z_N1=(1-z²)^(3/2)*Hg/K - (1-z²)/Lg
Z_M1=(1-z²)/Lf.
```
**NOUVEAU résultat exact :** `Z_N0` ne dépend d'aucun jet canonique radial d'ordre 2. `Z_M0` dépend EXACTEMENT des trois jets `pLg'', Sg'', theta_g''`, non nuls en général. Le quotient par la DERIVÉE SPATIALE COMPLETE de la stationnarité les élimine TOUS :
```
Fz = Dg - K*z/sqrt(1-z²)=0, et Fz'=0,
alpha = -z*(1-z²)^(3/2)/(Lf*K)
R_M0 = Z_M0 + alpha*Fz'
partial(R_M0)/partial(q_i'') = 0 pour les 12 canoniques.
```
Ce certificat a été exécuté exactement sur les fonctions originales, avec tests négatifs : omettre Fz' ou inverser le signe de alpha laisse un jet d'ordre 2 non nul. Sur Fz=Fz'=0, `R_M0=Z_M0`. Il ne s'agit pas de poser les dérivées secondes à zéro.

**REGULARITÉ CENTRALE :** si `s=r²,z=rw(s),K=r²k(s), Fz=r³f(s)`, alors `alpha=O(1/r)` isolément mais
```
alpha*Fz'=-r*w*(1-s*w²)^(3/2)*(3*f+2*s*f_s)/(Lf*k) = O(r).
```
C'est le PRODUIT du quotient qui est régulier, si `k,Lf` positifs et fonctions normalisées C¹ ; ne PAS attribuer une régularité séparée à alpha.

**RÉELLEMENT EXÉCUTÉ** en local dans `/mnt/data/janus-step68e` :
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68e_exact_shift_full_lapse_response.py
# 18 passed in 2.37s
python -m numerics.hr_step68e_exact_shift_full_lapse_response
```
Les DEUX nouveaux blobs source/test publiés sur GitHub correspondent byte-identically aux vrais fichiers exécutés. SHA256 du manifeste brut `024c4dc81ec76fc2076d683ac42154b43ada352f5aaa9812bd962d5c0695eda1`. Une première erreur de syntaxe du test et une factorisation manifest trop coûteuse ont été corrigées AVANT la suite réussie ; ne pas revendiquer de test complet GitHub Actions.

## PROCHAINE STEP68f : HARD RED SCIENTIFIQUE

1. Reconstituer les originaux historiques physiquement COHERENTS Step45/46/55/57/58/59/60 (+ Steps63–65) dans UN seul runtime, SHA authentifiés ; relancer leurs tests séparés/ensemble et certificat global Step55. Les empreintes des 15 sources sont déjà archivées dans `research/reports/gate2b-step68-source-preflight.json`.
2. Substituer le nouveau `R_M0` (quotient Fz') dans le VRAI calcul temporal Step58/60 `Cdot=A_NN+B_NN'+A_MM+B_MM'` sur l'exact profil radial Step55, avec contraintes ET PROLONGATIONS `Hg,Hf,Ddiag,Fz,C,Hg',C',Fz'`. NE PAS ANNULER `delta_Hz'` ni ses jets : les annulations de Step68d s'appuient sur sa présence.
3. Construire et tester l'oracle six-couples indépendant **non intégré par parties**, poser des bords explicites, analyser rang de Dirac, existence de lapses compatibles, secteurs `K=0,J=0`. TOUT EST ENCORE OUVERT.
4. Sauvegarder chaque nouvelle avancée dans `00_CURRENT_RESTART.md` en PRÉFIXE, conserver l'historique, garder les deux autres branches et GitHub Actions intouchés.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68d TERMINÉE (2026-10-25)

**BRANCHE EXCLUSIVE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. Ne jamais modifier `main` ni `research/v2-flrw`. GitHub Actions/workflows restent désactivés. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68D_AUTHENTIC_SHIFT_LAPSE_SYMBOL_COMPENSATION_AUDIT.md`.
**SOURCE NOUVELLE TESTÉE :** `numerics/hr_step68d_exact_shift_lapse_symbol.py`, Git blob `6af0322b0ba5c39ab014874455d4f380f6ea66fa`.
**16 TESTS CIBLÉS :** `tests/test_hr_step68d_exact_shift_lapse_symbol.py`, Git blob `9f1b9bfef4c573fa8fa365a37bf83e4d6307684b`.
**RAPPORT MACHINE :** `research/reports/gate2b-step68d-exact-shift-lapse-bridge.json`.
**MODULES PHYSIQUES ORIGINAUX RÉELLEMENT RECONSTITUÉS OCTET-PAR-OCTET ET EXÉCUTÉS ENSEMBLE :**
```
numerics/hr_step45_exact_physical_ward.py             66aa43841dccfe4a5d586a49be9c10af3a67a10e
numerics/hr_step57_secondary_principal_symbol.py      bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f
numerics/hr_step58_temporal_operator.py                802c23aebd41780d8c462f1aa1711707fe4ee88f
```
*ATTENTION : Step46/55/59/60 non réimportés dans le workspace DE CE TOUR ; ne PAS prétendre avoir calculé la réduction temporelle totale ou la branche Step55 physiquement.*

## RÉSULTAT NOUVEAU : FORMULE COURTE EXACTE DU VRAI OPÉRATEUR DE SHIFT

Sur `F_z=D_g-Kz/sqrt(1-z²)=0,K>0`, avec `H_g` **pas encore imposé nul**, le vrai six-pair Step58 `physical_operator()['delta_shift']` satisfait EXACTEMENT :
```
coefficient_(N') [delta_H z] = (1-z²)^(3/2) * Hg_on_Fz/K - (1-z²)/Lg
coefficient_(M') [delta_H z] = (1-z²)/Lf
C_zprime_on_Fz = -K/(Lg Lf sqrt(1-z²)).
```
Preuve SymPy sur les expressions CANONIQUES ORIGINALES, sans noyau reconstruit. Elle révèle deux termes compensateurs non nuls dans le crochet temporel `Cdot` :
```
direct_Ndoubleprime = -K sqrt(1-z²)/(Lg² Lf)
shift_Ndoubleprime  = -(1-z²)Hg/(Lg Lf) + K sqrt(1-z²)/(Lg² Lf)
TOTAL_Ndoubleprime  = -(1-z²)Hg/(Lg Lf).
direct_Mdoubleprime = +K sqrt(1-z²)/(Lg Lf²)
shift_Mdoubleprime  = -K sqrt(1-z²)/(Lg Lf²)
TOTAL_Mdoubleprime  = 0.
```
Sur `Fz=Hg=0`, les deux **coefficients de lapses doubles dans le CROCHET COMPLET** sont exactement nuls. Si on FIGE `delta_H z`, le terme `direct_Mdoubleprime` persiste FAUSSEMENT : un contrôle négatif protège ce point. Ce calcul simplifie et explique le Step58 existant, il ne fixe PAS les lapses.

## NOUVEAU PONT AVEC STEP68c AU CENTRE

Sous `Lg(0)=a>0,Lf(0)=b>0,z=rw,K=r²k0+...,Hg=r²h0+...`, les coefficients `N',M'` de `delta_Hz` admettent les limites
```
center Delta_z_Nprime = h0/k0 - 1/a
center Delta_z_Mprime = 1/b.
```
Pour `N=N0+N2r²+...`, `M=M0+M2r²+...`, les contributions PAR LA VOIE `N',M'` à `delta_H z'(0)` sont `2h0/k0-2/a` et `2/b`. Sur `Hg0=0` cela retrouve les coefficients `-2/a` et `2/b` du calcul indépendant du VRAI Step45 à l'étape 68c. Ne pas confondre cette contribution du SHIFT avec les coefficients du crochet complet Cdot. Le test rationnel isolé des constantes Step55 donne `k0>229/1000`.

**EXÉCUTION RÉELLE** `cd /mnt/data/janus-step68d && OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68d_exact_shift_lapse_symbol.py` ⇒ **16 passed in 11.01s**. Le calcul d'authenticité refuse chacun des trois fichiers si un octet est modifié. Code et tests GitHub relus SHA identiques à l'exécution. Manifeste brut local SHA256 `866746017010c856db29e0f3c77ef40fabdff30070939913fd69955dd0d95625`.

## PROCHAINE STEP68e — VERROU RÉEL

1. Reconstituer les sources originales Step45/46/55/57/58/59/60/63–65 ainsi que leurs tests, **TOUTES OCTET IDENTIQUES**, dans un seul environnement et exécuter ensemble leurs vérifications. En ce tour 45/57/58 faits, mais PAS 55/59/60.
2. Calculer et réduire les QUATRE coefficients d'ordre inférieur `A_N,B_N,A_M,B_M` de `Cdot` sur la **vraie** solution radiale Step55 et toutes les contraintes `Hg,Hf,Ddiag,Fz,C,Hg',C'` avec jets `U0..U3`, `z,z',z''`, **sans figer la réponse du shift**.
3. Oracle temporel Poisson NON-IBP indépendant sur SIX couples, conditions aux bords et chartes exceptionnelles `J=0,K=0`.
4. Déterminer rang de Dirac, fixation du rapport des lapses, puis examiner fantôme BD et validation 4D. **TOUT cela est encore OUVERT**. Conserver historique GitHub intégral.

**STATUT : Gate2B OPEN ; JANUS-R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68c TERMINÉE (2026-10-24)

**BRANCHE UNIQUE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. `main` et `research/v2-flrw` **intouchées**. GitHub Actions restent désactivés. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE D'ABORD :** `research/STEP68C_AUTHENTIC_STEP45_CENTER_SHIFT_LAPSE_JETS_AUDIT.md`.
**SCRIPT PHYSIQUE TESTÉ :** `numerics/hr_step68c_authentic_center_hamiltonian.py`, Git SHA `8d91d69cd1712f09cbc2f6fe8217f73ee52bede5`.
**29 TESTS PASSÉS :** `tests/test_hr_step68c_authentic_center_hamiltonian.py`, Git SHA `4d4cdab8e3a56691a5d60ced8bbc4f49efe85265`.
**RAPPORT MACHINE :** `research/reports/gate2b-step68c-authentic-center-report.json` (conserve expressions exactes de e_d/e_k et Hg0).
**SOURCE ORIGINALE VRAIMENT IMPORTÉE :** `numerics/hr_step45_exact_physical_ward.py`, SHA octet-identique `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. 9 identités Ward EXACTEMENT NULLES lors de cette exécution, six couples canoniques et poussières inclus. Ce tour est une réelle amélioration de provenance sur la transcription autonome Step68b.

## Résultat nouveau : le vrai champ hamiltonien ne fige PAS les dérivées du shift

Sur le centre analytique du benchmark Step55, `a=Lg(0), b=Lf(0), s=r², w=z/r=1/250`, avec `Sg=rLg,Sf=rLf,pLg=r²G,pSg=2rG,pLf=r²U,pSf=2rU` (la dernière relation exige la primaire f) et indépendamment `N=N0+N2r²+N4r⁴`, `M=M0+M2r²+M4r⁴` :

- La stationnarité `Fz=0` fixe le jet `P3` de `pSg=2Gr+P3r³` par `Dg/r³=k0*w`, où `k0=Mg²*m²*a*b*(beta1*a²+2 beta2*a*b+beta3*b²)\neq0`.
- Les SIX termes de `delta_H Dg`, incluant dust `delta pg` et `delta theta_g`, ont été calculés avec les vrais gradients d'Euler 12 variables Step45. Leur terme `r` s'annule EXACTEMENT séparément pour N et M ; leur coefficient `e_d(0)=lim deltaDg/r³` est calculé NON NUL en général. `e_k(0)=lim deltaK/r²` est calculé depuis la vraie interaction K. Les quatre expressions complètes sont dans le rapport machine.
- La règle physique de l'étape 68a donne `delta_H z'(0)=[e_d(0)-w*e_k(0)]/k0`. Le coefficient de `N4` ou `M4` en ce point est exactement nul, MAIS ceux de `N2`, `M2` NE LE SONT PAS.
- **CERTIFICAT EXACT :** `∂_(N2) delta_H z'(0) = 2*Hg0/k0 - 2/a`, `∂_(M2) delta_H z'(0)=2/b`. Sur la primaire `Hg0=lim Hg/r²=0`, ces deux coefficients valent **-2/a** et **+2/b**. Comme `N''(0)=2N2`, `M''(0)=2M2`, les sensibilités aux doubles dérivées des lapses de **delta z'** valent **-1/a**, **+1/b**. ATTENTION : ceci N'EST PAS le coefficient de N'' ou M'' du crochet complet Cdot ; les annulations de Step58 y subsistent.
- Contrôle négatif : sans la primaire f `pSf/r=2U` les relations de parité f échouent par `M0(2U-V)/(2b Mf²)`. La variation du shift est donc contrôlée seulement sur ce secteur de contraintes.

**VRAIMENT EXÉCUTÉ** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=/mnt/data/janus-step68c pytest -q /mnt/data/janus-step68c/tests/test_hr_step68c_authentic_center_hamiltonian.py` => **29 passed in 8.79s**. Un test modifie les octets du noyau original et vérifie que la source drift est rejetée. Les Git SHA finaux du script et des tests sont identiques aux exécutables locaux. Manifeste brut local SHA256 `81aae685a21c00f02860d5fe5600f0af9bf51bbebea1b2899ba97fa9ae8e3e3f`.

**CORRECTION ANCIENNE STEP68b :** `numerics/hr_step68b_center_hamiltonian_parity.py` avait encore `kf0*r*(b+b2*r²)` au lieu de `kf0*r*(b+bf2*r²)` dans `tf'`, malgré le renommage `bf2` précédent. CETTE ERREUR EST CORRIGÉE SUR GITHUB (commit `234e16b`). Ne pas présenter les anciens 23 tests Step68b comme rejoués APRÈS ce correctif : le nouveau contrôle authentique Step68c avec la bonne géométrie a 29 tests passés.

## PROCHAINE HARD RED — STEP68d

1. Reconstituer EN UN SEUL ENVIRONNEMENT les VRAIS modules original Step45/46/55/57/58/59/60 (également 63–65) plus tests avec Git hashes vérifiés, suivre manifeste préflight `research/reports/gate2b-step68-source-preflight.json`. Step45 VRAIMENT réexécuté ici ; Step55 et Step57–60 **pas** ensemble en ce tour.
2. Substituer les nouveaux `e_d(0),e_k(0)` et jets prolongés dans le vrai Step58/60 de `Cdot=A_N N+B_N N'+A_M M+B_M M'`. Respecter TOUTES les contraintes originales `Hg,Hf,Ddiag,Fz,C,C',Hg'`, le profil SPATIAL EXACT Step55 et le Taylor certifié `U0..U3`.
3. Produire l'oracle temporel indépendant NON-IBP six-couples, traiter bords et secteurs exceptionnels `K=0,J=0`. Calculer rang et existence de lapses compatibles. **Rien de tout cela n'est encore établi**.
4. Continuer à préfixer ce fichier sans écraser l'historique. **Gate 2B OPEN, JANUS-R NOT_VALIDATED**.

---

# JANUS — REPRISE PRIORITAIRE : STEP68b TERMINEE (2026-10-24)

**BRANCHE EXCLUSIVE :** `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main` ni `research/v2-flrw`. GitHub Actions restent désactivées. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68B_CENTER_HAMILTONIAN_PARITY_AND_F_PRIMARY_GATE_AUDIT.md`.
**SCRIPT EXACT TESTÉ :** `numerics/hr_step68b_center_hamiltonian_parity.py`, Git blob `e8c7e932994f340933521ac6f48b46f8a53d1bf6`.
**23 TESTS CIBLÉS :** `tests/test_hr_step68b_center_hamiltonian_parity.py`, Git blob `c35fef4551fc68c860147e51cccf5b8069bc4fb1`.
**RAPPORT MACHINE :** `research/reports/gate2b-step68b-center-parity-report.json`.
**PRECEDENT :** Step68a et Step67b intégralement conservés ci-dessous.

## NOUVELLE AVANCÉE : VRAI TEST DE PARITÉ CENTRALE DU FLUX HAMILTONIEN

Les densités post-IBP de l'ORIGINAL Step45 ont été TRANSCRITES dans une reconstruction indépendante ; le module original GitHub Step45, quoique LU et comparé, N'A PAS ÉTÉ RÉIMPORTÉ par le code. On utilise la charte radiale analytique du benchmark Step55 : `Sg=r Lg,Sf=r Lf,pLg=r²G,pSg=2rG,pLf=r²U,pSf=2rU`, avec lapses INDEPENDANTS `N=N0+N2r²` et `M=M0+M2r²`. Les deux relations de moments au centre sont des conséquences de la stationnarité du shift (g) et de la contrainte primaire de moment f de Step46 ; il est FAUX de les omettre.

**CALCUL EXACT SYMPY (pour N et M SÉPARÉMENT) :**
```
lim delta Sg/r = lim delta Lg; lim delta pSg/r = 2 lim delta pLg/r²
lim delta Sf/r = lim delta Lf; lim delta pSf/r = 2 lim delta pLf/r²
=> lim delta Dg/r = 0.
```
Ainsi, sur cette famille analytique et ses contraintes centrales, `delta Dg=O(r³)` et `delta K=O(r²)` pour chacun des deux flots de lapses. C'est le premier contrôle d'APPLICABILITÉ CENTRALE des formules de shift Step68a au champ Hamiltonien ; PAS une preuve globale de Dirac.

**CONTROLE NEGATIF MAJEUR :** sans la primaire f et en écrivant `pSf=V*r`, le lapse M donne
```
lim(delta Lf - delta Sf/r) = M0 (2U-V)/(2b Mf²)
lim(delta pSf/r - 2delta pLf/r²) = M0 U(2U-V)/(2b² Mf²).
```
Ces termes ne s'annulent PAS génériquement hors de `V=2U`. La primaire f est donc ESSENTIELLE. Les jets des lapses `N2,M2` restent présents : ce travail NE FIXE PAS leur rapport ni le rang.

**RÉSULTATS RÉELLEMENT EXÉCUTÉS :** 23 tests Step68b PASS en 7.22s ; Step68a + Step68b ensemble **44 PASSED en 12.85s**, local `/mnt/data/janus-step68a`. Un risque de confusion entre le coefficient radial métrique f `bf2` et le beta d'interaction `b2` a été détecté, corrigé et les tests REJOUÉS. Les DEUX blobs SHA code/tests GitHub ont été relus et vérifiés byte-identiques à l'exécuté. Manifeste local final SHA256 `c556154cc6b72266df7143c94f5cce2ba5cb5e2ac4a370ef5df79be37f46c19b`. Aucun workflow activé, aucun test complet du repo.

## HARD RED — PROCHAINE STEP68c

1. REIMPORTER et authentifier OCTET PAR OCTET dans UN workspace vrai Step45+46+55+57–60+63–65, plus les jeux de tests, et COMPARER les vrais gradients d'Euler à la reconstruction de Step68b.
2. Calculer les TERMES FINIS non triviaux `e_d=delta Dg/r³`, `e_k=delta K/r²` et leurs jets sur la solution Step55 authentique, y compris les poussières et séries `U0..U3` de Step67b.
3. Réduire les vrais quatre coefficients temporels `A_N,B_N,A_M,B_M` du Step58/60 en respectant `delta z,delta z'` de Step68a, les contraintes complètes et leurs prolongations.
4. Oracle Poisson non-IBP indépendant six-couples, bords, rang de Dirac, lapses et chartes exceptionnelles. **TOUT OUVERT**.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Conserver la suite historique complète ci-dessous.

---

# JANUS — REPRISE PRIORITAIRE : STEP68a TERMINÉE (2026-10-24)

**ÉCRITURE AUTORISÉE UNIQUEMENT** sur `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main` ou `research/v2-flrw` ; GitHub Actions/workflows restent désactivés. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE D'ABORD** `research/STEP68A_CENTER_SHIFT_FUNCTIONAL_VARIATION_AUDIT.md`.
**SOURCE LOCALE ET GITHUB IDENTIQUES** : `numerics/hr_step68a_normalized_shift_variations.py`, Git blob `31840c495175d01d275661e3553436983e3dc43c`.
**TESTS LOCAUX ET GITHUB IDENTIQUES** : `tests/test_hr_step68a_normalized_shift_variations.py`, Git blob `7c9ec9569bec35e98d78e540a9e7fe8096c120e6`.
**RAPPORT ARCHIVÉ** : `research/reports/gate2b-step68a-report.json`, Git blob `41a7be90bff5324ebad01ef4d04f6f85bcd61982`.
**PREPARATION Step68** : `research/reports/gate2b-step68-source-preflight.json` (15 hashes originaux consultés) reste inchangée.
**PRÉCÉDENT IMPORTANT** : Step67b (vraie source physique historique 45/46/55 relancée, coefficient U3 certifié) est maintenu INTÉGRALEMENT ci-dessous.

## Résultat nouveau vérifié maintenant : variation spatiale du SHIFT jusqu'à z'' au centre

Sur la SEULE famille analytique de données initiales Step55, `s=r²`, `D_g=r³d(s)`, `K=r²k(s)`, `k>229/1000`, `z=r*w0`, `w0=1/250`, et pour les variations conservant la parité `delta D_g=r³e_d(s)`, `delta K=r²e_k(s)`, définir `t=1-s*w0²` :

```text
A=t^(3/2)/k, B=-w0*t/k
delta w=A*e_d+B*e_k
A_s=-3*w0²*sqrt(t)/(2k)-t^(3/2)*k_s/k²
B_s= w0³/k+w0*t*k_s/k²
A_ss=3*w0⁴/(4k*sqrt(t))+3*w0²*sqrt(t)*k_s/k²
       +t^(3/2)*(2k_s²/k³-k_ss/k²)
B_ss=-2w0³*k_s/k²+w0*t*(k_ss/k²-2k_s²/k³)
delta w_s=A_s e_d+B_s e_k+A e_d_s+B e_k_s
delta w_ss=A_ss e_d+B_ss e_k+2A_s e_d_s+2B_s e_k_s+A e_d_ss+B e_k_ss
delta z=r*delta w
delta z'=delta w+2s*delta w_s
delta z''=2r*(3delta w_s+2s delta w_ss)
```

Ces égalités ont été vérifiées symboliquement, y compris l'identité de pullback de l'ancienne équation physique Step58 `delta z=Z_D delta D_g+Z_K delta K`. Au centre `delta z'(0)=[e_d(0)-w0 e_k(0)]/k(0)`, généralement NON NUL. Exemple négatif exact : `k=1/2,e_d=1,e_k=0,k_s=k_ss=e_d_s=...=0` => `delta z'(0)=2`, `lim_{r→0}delta z''/r=-9/31250`. Interdire de figer `delta z'` simplement parce que `z''` du FOND vaut zéro.

**RÉELLEMENT EXÉCUTÉ** : `PYTHONPATH=/mnt/data/janus-step68a OPENBLAS_NUM_THREADS=1 python -m pytest -q /mnt/data/janus-step68a/tests/test_hr_step68a_normalized_shift_variations.py` => **21 passed in 6.01s**. Deux égalités algébriques SymPy initialement comparées structurellement ont été réparées par `simplify(a-b)==0` AVANT l'exécution réussie. Source et tests uploadés, Git blobs relus identiques aux fichiers vraiment exécutés. Une autre correction de rigueur a supprimé l'hypothèse non justifiée de positivité sur k_s,k_ss : deux symboles réels de signe libre, validés par un 21e test avec k_s négatif. Le manifeste brut local SHA256 est `92db7cfefefbbc6a1393834aec8d377e000d1f7359d39dd0640bd8b9aabc1bfa`.

**PROVENANCE LIMITÉE** : le véritable Step58 a été LU sur GitHub, mais Steps45/55/57/58/59/60 n'ont PAS été exécutés ensemble dans le nouveau workspace. Les variations e_d,e_k ne proviennent PAS encore du Hamiltonien six-couples ; leurs parités doivent être vérifiées dans la vraie solution physique. Ceci est un théorème d'algèbre sur la charte benchmark, pas une preuve de rang Dirac / absence du fantôme BD / cosmologie.

## PROCHAIN VRAI VERROU — STEP68b

1. Recréer un workspace octet-authentique GitHub Step45/46/55/57/58/59/60/63–65/67b ; vérifier les SHA, clôturer toutes dépendances et exécuter tests pertinents ENSEMBLE (clone direct impossible ici : erreur DNS, donc utiliser le connecteur GitHub).
2. Identifier les variations `delta D_g,delta K` générées par `physical_operator()['delta_Dg'],['delta_K']` sur la vraie solution positive Step55 pour chaque coefficient `N,N',M,M'`. PROUVER ou réfuter leur parité normalisée `r³,r²` avant d'utiliser Step68a sur ces perturbations.
3. Substituer les vrais `k_s,k_ss` et la vraie géométrie (dont le U3 physique Step67b), reconstruire `delta z,delta z'` dans les vrais coefficients `A_N,B_N,A_M,B_M`; imposer les contraintes originales `Fz,Hg,Hf,Ddiag,C` et leurs dérivées complètes.
4. Exécuter oracle Poisson temporel indépendant NON IBP sur SIX couples et les bords ; calculer le rang, la fixation des lapses et les chartes exceptionnelles `K=0,J=0`. Jusqu'alors `GATE_2B=OPEN`, `JANUS_R=NOT_VALIDATED`.

**TOUT L'HISTORIQUE DES ÉTAPES 67b, 67, 66, 65... EST PRÉSERVÉ CI-DESSOUS.**

---

# JANUS — POINT DE REPRISE PRIORITAIRE : STEP67b TERMINÉE (2026-10-24)

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. NE PAS modifier `main`, `research/v2-flrw`. GitHub Actions/workflows restent DÉSACTIVÉS. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED**.

**LIRE EN PREMIER :** `research/STEP67B_AUTHENTIC_ORIGINAL_G_U3_CENTER_INTERVAL_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step67b-original-center-u3-report.json`.
**NOUVELLE SOURCE TESTÉE :** `numerics/hr_step67_true_center_taylor_certificate.py`, Git blob `d73e74089b9a2437aa6ba9cd011e5b4819dcb339`.
**16 NOUVEAUX TESTS :** `tests/test_hr_step67_true_center_taylor_certificate.py`, Git blob `681f667b3d1f3a066471efc89c43133dcc78ac12`.
**AUTRE STEP67 DÉJÀ EXISTANT :** `research/STEP67_CENTER_RADIAL_SHIFT_JETS_AUDIT.md`, `research/reports/gate2b-step67-report.json`, `numerics/hr_step67_radial_shift_jets.py`. Ils sont PRÉSERVÉS INTACTS dans l'historique ci-dessous. Le présent travail « 67b » sur U3 est COMPLÉMENTAIRE et NON un remplacement.

## AVANCÉE DU TOUR : ORIGINAUX PHYSIQUES DÉSORMAIS RÉELLEMENT EXÉCUTABLES

Les QUATRE sources historiques ont été **reconstituées OCTET PAR OCTET et GIT HASH VÉRIFIÉES**, simultanément dans `/mnt/data/janus-step67` :

```text
numerics/hr_step45_exact_physical_ward.py      66aa43841dccfe4a5d586a49be9c10af3a67a10e
numerics/hr_step46_exact_secondary_ode.py      bac025c28dbe1561c0c36c56dbfda46dc326f804
numerics/hr_step55_normalized_secondary.py     a54a6acf2f7ad2f64c500faecfa1406ecbf7b862
numerics/hr_step55_global_barrier.py           a6e7004120d0a166a3a8973c2fbe1487a8eb70fe
```

Ce ne sont PAS des copies modifiées, des noyaux manufacturés ou des transcriptions approximatives : les blobs Git calculés localement par `git hash-object` sont égaux aux vrais SHA du connecteur GitHub. Les fichiers Step57/58/59/60 du **Dirac temporel** ne sont PAS encore tous réunis dans CE workspace ; ne pas prétendre au calcul temporel complet.

**LA VRAIE PHYSIQUE G(s,U) A ÉTÉ EXÉCUTÉE :** `numerics.hr_step55_normalized_secondary.normalized_symbolic()`, dérivée de l'action originale Step45 sur les six couples, via la primaire-réduite Step46, retourne un polynôme exactement QUADRATIQUE en U avec 22 paramètres indépendants avant restriction à l'initial-data benchmark.

**LE VRAI CERTIFICAT GLOBAL Step55 A ÉTÉ RÉEXÉCUTÉ** dans le même environnement, `certify_global_barrier(cells=256)`, avec les marges rationnelles originales IDENTIQUES :

```text
strict_max_Fupper = -1480966474499367232302129/10000000000000000000000000000 <0
strict_min_Flower = +295653233337826329055403/2000000000000000000000000000 >0
```

Le certificat concerne le PROFIL SPATIAL initial sur r∈[0,17/20], avec les signes poussières/J/K de Step54 en tant que résultats antérieurs ; il ne démontre pas la fermeture en temps.

## NOUVELLE PREUVE : QUATRIÈME COEFFICIENT REGULIER DU MOMENTUM pLf

Avec `s=r²`, `P(r)=pLf=r² U(s)`, et la véritable EDO `2s U_s=G(s,U)-2U`, écrire `U=U0+U1*s+U2*s²+U3*s³+...`. Les U0,U1,U2 proviennent des vrais INTERVALLES entiers à arrondis extérieurs de l'original `hr_step55_global_barrier.py`. Les fonctions et paramètres géométriques du benchmark sont repris dans l'algèbre de Taylor de degré 3 **en entiers à échelle 10^28 et arrondis extérieurs à chaque opération**, puis réinjectés dans le vrai `G` compilé par Step55. Les 3 résidus des ordres s^0,s^1,s^2 contiennent zéro.

La récurrence non résonante formelle donne `U3=[s³] G(s,U0+U1s+U2s²)/9`. NOUVEL ENCAdREMENT RATIONNEL RIGOUREUX :

```text
-31325163121998456229/2500000000000000000000000000
 <= U3 <=
-62650326243996887233/5000000000000000000000000000 .
U3 environ -1.253006524879938e-8, STRICTEMENT NÉGATIF.
Largeur en fraction environ 5.045e-24.
```

Il s'agit du terme nouveau `U3*r^8` dans la série régulière physique `pLf(r)`. De même `pLf'''/r=24U1+120U2*r²+336U3*r^4+...`, avec `336U3 ~ -4.210101923596592e-6`. L'interprétation suppose l'existence de la branche analytique centrale certifiée Step49 et les bornes U0/U1/U2 Steps52/53. **Ce nouveau coefficient est une propriété SPATIALE, pas une équation de lapses ou une preuve d'absence de fantôme.**

## TESTS VRAIMENT EXÉCUTÉS ET REPRISE

```bash
cd /mnt/data/janus-step67
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step67_true_center_taylor_certificate.py
# VRAIMENT : 16 passed in 3.20s.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step67_true_center_taylor_certificate > research/reports/gate2b-step67-local-manifest.json
# SHA256 local : aada56f82452eb67a5fc43c4808df0731cad6c8cfae3915c6ee6d77504b55cf3
```

Les DEUX NOUVEAUX fichiers ont été comparés au dépôt GitHub et sont byte-identiques aux fichiers réellement exécutés. Les tests incluent vérification SHA de 4 originaux, mutation négative fail-closed, Ward physique Step45, restauration secondaire Step46, preuve entière ORIGINALE Step55 sur 256 cellules, séries Taylor avec racines/inverses à enveloppement exact, coefficient U3 de signe strict, et test indépendant du facteur 9. Le manifeste brut local n'est pas uploadé séparément ; ses bornes exactes et le code reproductible sont dans le nouveau rapport 67b sur GitHub. Pas de CI ou de suite complète du dépôt.

## NEXT STEP68 — HARD RED

1. **RÉUNIR DANS CE WORKTREE ORIGINAL** les sources authentiques Step57/58/59/60 du calcul TEMPOREL, plus les bornes originales sur G de Steps63/64/65 et la normalisation Step66. Valider TOUS les SHA et rejouer leurs tests ensemble.
2. Appliquer les véritables contraintes et leurs jets prolongés `Fz,Hg,Hf,Ddiag,C,C',Hg'`, les dérivées cohérentes `z,z',z''` (correction Step61) et le nouveau développement central `U0..U3`, pour réduire les quatre coefficients du lapse `A_N,B_N,A_M,B_M` sur la solution radiale EXACTE et positive.
3. Construire/vérifier l'oracle TEMPOREL indépendant des six couples depuis l'action originale NON IBP, puis le rang/lapse ratio avec des conditions de bord compatibles ; examiner les charts K=0/J=0 séparément.
4. Continuer à préfixer `00_CURRENT_RESTART.md` sans écraser les étapes antérieures. Laisser `main`, V2 et Actions inchangés.

**BILAN : réelle action physique 45/46/55 + vrai invariant Step55 256 cellules exécutés ; nouvelle borne U3 prouvée ; Dirac temporel complet, rang des lapses et santé BD du modèle TOUJOURS OPEN. GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE STEP67 TERMINÉE (2026-10-24)

**SEULE BRANCHE MODIFIABLE :** research/gate2b-nonhomothetic-transfer. Ne toucher ni main ni research/v2-flrw. GitHub Actions/workflows restent désactivés selon la demande utilisateur.

**LIRE EN PREMIER :** research/STEP67_CENTER_RADIAL_SHIFT_JETS_AUDIT.md.
**CODE :** numerics/hr_step67_radial_shift_jets.py, SHA blob 9368df2289756feb2e47a86917e5466c2a90ab75.
**TESTS :** tests/test_hr_step67_radial_shift_jets.py, SHA blob 92dcdbc0cebbab2f5fccf98c5a62ff1c7d7da592.
**RAPPORT :** research/reports/gate2b-step67-report.json, SHA blob 7dfdccf13f549b51e12b90d18ec584c5d2a9aa2c.
**PREUVE LOCALE EXÉCUTÉE :** 20 nouveaux tests PASSED en 1.21s dans /mnt/data/janus-step67; fichiers exécutés et 3 blobs Git comparés byte-identical. Ni CI ni suite complète. Le script neuf n'importe PAS les originaux physiques Steps45/55 ; il assume leur benchmark publié.

## Résultat nouveau, strictement sur le profil radial Step55 certifié

Dans la charte normalisée s=r², Dg=r³d(s), K=r²k(s), z=rw(s), k>229/1000, w=1/250 et s<=289/400 :
- Racine physique Fhat=d-k*w/sqrt(1-sw²)=0 => W(s,d,k)=d/sqrt(k²+s*d²).
- À d,k fixés, W_s=-w³/2, W_ss=3w⁵/4, W_sd=-3w²*t^(3/2)/(2k), W_sk=3w³*t/(2k), t=1-sw².
- Dérivée totale w_s=W_s+W_d*d_s+W_k*k_s, et w_ss=W_ss+2W_sd*d_s+2W_sk*k_s+W_dd*d_s²+2W_dk*d_s*k_s+W_kk*k_s²+W_d*d_ss+W_k*k_ss.
- Stationnarité et w=constant imposent d=k*w/sqrt(t), d_s=w*k_s/sqrt(t)+k*w³/(2*t^(3/2)), d_ss=w*k_ss/sqrt(t)+w³*k_s/t^(3/2)+3k*w⁵/(4t^(5/2)).
- SUBSTITUTION SYMBOLIQUE EXACTE : w_s=w_ss=0, donc z=r/250, z'=1/250, z''=0 jusqu'au centre.
- CONTRÔLE NÉGATIF : omettre W_s créerait un résidu artificiel +w³/2.
- Caps Fraction exacts (coefficients PARTIELS de référence seulement) : |W_s|=1/31250000; |W_ss|=3/3906250000000; |W_sd|<3/28625; |W_sk|<3/7156250. Aucun bound sur d_s,k_s,d_ss,k_ss hors du profil.

**CRITICAL Step58 WARNING:** z'=1/250, z''=0 are BACKGROUND-ONLY identities. The Hamiltonian first variations delta z, delta z' (and radial derivatives thereof) are generically NONZERO and must be kept in the original six-pair temporal Dirac operator. delta w = W_d delta d + W_k delta k; delta z'=delta w+2s (delta w)_s. NEVER set delta z' to zero merely because the baseline shift is linear. See Step57/58 and the amended Step67 audit.

**STEP68 PRÉPARATION RÉALISÉE :** research/reports/gate2b-step68-source-preflight.json (Git blob 902dad4052df5304453bb09c00b7f4b6428b8412), qui gèle 15 empreintes authentifiées GitHub et les imports relatifs directs repérés pour reconstituer le vrai noyau physique. Ce manifeste de préparation n'établit PAS la clôture exhaustive des dépendances ni l'exécution du vrai système temporel. Revalider localement chacun de ces blobs avant le calcul de Dirac.

## PROCHAIN VRAI VERROU — STEP68, PAS UNE VALIDATION DE JANUS

1. Reconstituer dans UN vrai workspace l'ensemble original GitHub exact Steps45/46/55/57/58/59/60/63/64/65, ainsi que dépendances transitives et tests. Ne jamais prétendre que Step67 seul a rejoué le cœur physique.
2. Injecter les jets vrais P',P'',P''' et les jets stationnaires z,z',z'' ci-dessus dans l'opérateur de temps sur la famille positive Step55 (contraintes/prolongations complètes).
3. Calculer A_N,B_N,A_M,B_M des quatre lapses/gradients de lapses ; tester indépendamment l'oracle Poisson ORIGINAL non-IBP sur SIX couples, les conditions de bord, le rang et la fixation des lapses.
4. Chartes K=0/J=0 à traiter séparément ; physique 4D / fantôme BD / cosmologie restent NON PROUVÉS.

**GATE_2B OPEN. JANUS_R NOT_VALIDATED.**
**HISTORIQUE Step66 et toutes les anciennes étapes conservés CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP66 TERMINÉ — 2026-10-24

**ÉCRITURE AUTORISÉE SEULEMENT :** `research/gate2b-nonhomothetic-transfer`. Ne toucher NI `main` NI `research/v2-flrw`. Garder GitHub Actions/workflows DÉSACTIVÉS. **GATE 2B OPEN ; JANUS-R NOT VALIDATED.**

**LIRE EN PREMIER :** `research/STEP66_CENTER_NORMALIZED_SHIFT_C2_IMPLICIT_CERTIFICATE.md`.
**RAPPORT MACHINE ARCHIVÉ :** `research/reports/gate2b-step66-report.json`.
**CODE NOUVEAU TESTÉ :** `numerics/hr_step66_center_shift_implicit_condition.py`, Git blob `47231c568a7a08954dc3894c82552552da58fde5`.
**20 NOUVEAUX TESTS EXÉCUTÉS :** `tests/test_hr_step66_center_shift_implicit_condition.py`, Git blob `274837f216d3399540a3eb96e5836cb9d721add4`.
**PRÉCÉDENT :** `research/STEP65_MONOTONE_PHYSICAL_GUU_SHARPER_RATIONAL_BOUND_AUDIT.md`, point de reprise Step65 conservé CI-DESSOUS, avec toutes les étapes 62–65 préservées.

## AVANCÉE ANALYTIQUE EXACTE — DÉPLACEMENT RELATIF C² NORMALISÉ JUSQU'AU CENTRE

Cette étape N'EST PAS l'exécution du vrai calcul temporel Step60. Elle démontre un théorème de conditionnement de l'équation algébrique ORIGINALE du shift relatif de l'action positive-EH HR sphérique à deux poussières / six couples :
```text
Fz=Dg-K*z/sqrt(1-z²)=0
sur la branche radiale initiale Step55 STRICTEMENT POSITIVE :
s=r², 0<=r<=17/20, Dg=r³ d(s), K=r² k(s), k>229/1000,
z=r*w(s), w=1/250 (=0.004, pente préscrite du vrai benchmark).
```

Pour r>0, diviser Fz par r³ et poser w=z/r. La fonction stationnaire normalisée se prolonge EXACTEMENT au centre :
```text
Fhat(s,d,k,w)=d - k*w/sqrt(1-s*w²)
w(d,k;s)=d/sqrt(k²+s*d²)  sur k>0
∂Fhat/∂w = -k/(1-s*w²)^(3/2)
t=1-s*w² >=24999711/25000000>9999/10000.
DONC |∂Fhat/∂w|>229/1000 sur TOUT r∈[0,17/20], centre INCLUS.
```

**THÉORÈME NOUVEAU** : dérivées premières et SECONDES de cette véritable racine (à s fixé), toutes EXACTES :
```text
w_d = t^(3/2)/k
w_k = -w*t/k
w_dd = -3*s*w*t²/k²
w_dk = (3*s*w²-1)*t^(3/2)/k²
w_kk = w*(2-3*s*w²)*t/k²
```

Les bornes **Fraction rationnelles strictes CONTINUES** sur le vrai benchmark sont
```text
|w_d|<22/5 ; |w_k|<1/50 ;
|w_dd|<1/5 ; |w_dk|<20 ; |w_kk|<1/5.
```
Les caps rationnels plus précis qui impliquent ces bornes sont respectivement `1000/229,4/229,8670/52441,1000000/52441,8000/52441`. Au CENTRE `s=0`, les cinq dérivées valent `1/k,-w/k,0,-1/k²,2w/k²` : **finies** sur k>229/1000. Tous les nombres sont calculés en `fractions.Fraction`, AUCUN flottant dans la preuve.

Pour une variation qui PRÉSERVE la parité radiale de la famille (`delta Dg=r³ delta d`, `delta K=r² delta k`), on obtient EXACTEMENT
```text
delta(z/r) = t^(3/2)/k *delta d -w*t/k*delta k
delta z = r*delta(z/r).
|delta(z/r)| <= 1000/229*(|delta d|+|delta k|/250).
```
**Attention** : <= est indispensable pour le cas de perturbation NULLE, 0<=0. Une version strictement `<` fausse a été **corrigée avant la clôture du Step66** ; un contrôle explicite protège l'inégalité correcte. La normalisation compense l'apparent inverse divergent en `1/r²` des variations du Fz BRUT. Ceci rend l'argument de fonction implicite robuste **dans la charte/parité initiale prescrite**, et NON pour toutes les variations canonique off-shell. Le secteur `K=0` n'est PAS couvert ; à k=0, `∂Fhat/∂w=0`.

## PROVENANCE ET TESTS VRAIMENT EFFECTUÉS

IMPORTANT : le fichier Step66 est un module AUTONOME. Il se fonde sur l'identité physique Fz de l'original Step45 et sur les bornes `K/r²>0.229` et `z/r=0.004` issues des rapports précédents Step54/55 **consultés sur GitHub**. Les sources originales Step45/55, les certifications Step63/64 et le vrai Dirac Step58/60 N'ONT PAS été réimportées dans ce nouvel environnement local ni rejouées. Ne PAS prétendre autrement. La preuve nouvelle symbolique/rationnelle est exacte SOUS CES HYPOTHÈSES certifiées précédemment ; aucun rang temporel n'a été calculé.

Workspace `/mnt/data/janus-step66` ; version FINALE du code et du test byte-identiques à GitHub :

```bash
cd /mnt/data/janus-step66
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step66_center_shift_implicit_condition.py
# RÉEL : 20 PASSED en 2.80s (après correction de l'inégalité zéro).
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step66_center_shift_implicit_condition > research/reports/gate2b-step66-local-manifest.json
# SHA256 brut local 08ec605aea6ad09e9aa55b03c8ebcc832c970b80b702d47123d5885380b8bf19
```

Manifeste brut local NON téléversé séparément ; module, tests, audit, rapport machine de résultats conservés sur GitHub. Les 20 tests contrôlent symboliquement la racine/Fhat, dérivées et Hessienne, branche positive, parité et centre, bornes en fractions continues, mauvais paramètres/k=0, et refus de prétendre au rang temporel.

## NEXT STEP67 — GROS VERROU TOUJOURS À LEVER

1. **RECONSTITUTION AUTHENTIQUE COHÉRENTE** : importer, avec validation SHA des octets, les originaux Step45/46/55/57/58/59/60 et l'AD physique Steps63/64/65 dans UN même worktree. Le shell local reste non connecté DNS GitHub ; jusqu'ici les modules d'origine n'ont pas été reconstitués dans le nouveau workspace Step66. Ne pas annoncer de faux tests physiques.
2. Sur la vraie branche positive exacte Step55, reprendre les BORNES `P',P'',P'''` Step64 et la dérivée de G Step65, imposer les vrais `z=Z(Dg,K), z'=Z1, z''=Z2` (correction Step61), et employer les variables **normalisées** `d,k,w` et leurs dérivées Step66 pour éviter les erreurs apparentes au centre.
3. **CALCULER ET RÉDUIRE** les quatre vrais coefficients du crochet temporel `A_N,B_N,A_M,B_M`, en imposant TOUTES les contraintes et leurs dérivées (`Fz,Hg,Hf,Ddiag,C`), puis leurs rangs et bords, chartes K/J exceptionnelles.
4. Valider par le crochet temporel **indépendant NON-IBP** sur les 6 couples et des fonctions tests compactes, avant d'affirmer une fixation des lapses ou l'absence du fantôme BD. Aucun théorème d'évolution 4D JANUS n'est encore démontré.
5. Préfixer le fichier `00_CURRENT_RESTART.md` à chaque étape, préserver tout l'historique et les deux autres branches, Actions OFF.

**VERDICT : Step66 uniform C² condition number of normalized HR algebraic shift, exact center-inclusive rational inequalities and 20 verified tests. FULL TEMPORAL DIRAC RANK, LAPSE FIXING, BD GHOST ABSENCE AND JANUS-R VALIDATION: STILL OPEN.**

---

# JANUS — REPRISE PRIORITAIRE : STEP65 TERMINÉ — 2026-10-23

**SEULE BRANCHE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`; `main`, `research/v2-flrw` NON MODIFIÉS. GitHub Actions/workflows restent désactivés. **GATE_2B OPEN — JANUS-R NOT VALIDATED.**

**LIRE D'ABORD :** `research/STEP65_MONOTONE_PHYSICAL_GUU_SHARPER_RATIONAL_BOUND_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step65-report.json`.
**NOUVEAU CODE :** `numerics/hr_step65_monotone_physical_curvature.py`, Git blob `046a58e5c118ac269fc68d4020e1d192349dc28f`.
**15 NOUVEAUX TESTS :** `tests/test_hr_step65_monotone_physical_curvature.py`, Git blob `e4d1d002f8d5176cda1057dc194e744a6518bd6d`.
**ORIGINALS 45/46/55 AUTHENTIFIÉS dans vrai worktree :**
`numerics/hr_step45_exact_physical_ward.py` `66aa43841dccfe4a5d586a49be9c10af3a67a10e`;
`numerics/hr_step46_exact_secondary_ode.py` `bac025c28dbe1561c0c36c56dbfda46dc326f804`;
`numerics/hr_step55_normalized_secondary.py` `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
**SOURCE ANALYTIQUE Step62 REJOUÉE :** `numerics/hr_step62_physical_G_curvature.py` Git `d2040a4bde9672933eac9bbab91b792005227f40`.
**PRÉCÉDENT :** `research/STEP64_FULL_CENTER_PHYSICAL_PTHIRD_INTERVAL_AUDIT.md` — sa preuve du vrai P''' global y compris centre est préservée. Ne PAS confondre avec d'autres étapes Step62/63 parallèles.

## AVANCÉE RÉELLE ET EXACTE : STRICTION MONOTONE DE G_UU SUR LA VRAIE FONCTION G

Sur la véritable équation secondaire sphérique positive-EH HR avec 2 poussières et 6 couples Step45/46/55, la fonction physique `G(s,U)` a degré 2 EXACTEMENT en U (`G_UUU=0`). Step62 avait obtenu `0<=G_UU<337/500=0.674` pour le benchmark sur `s=r²∈[0,289/400]`.

Nouveau Step65 : avec les constantes RATIONNELLES EXACTES du benchmark radial Step55 (géométrie décrite dans `numerics/hr_step55_global_barrier.py` CONSULTÉ mais NON importé comme source authentique ici), montrer

```text
G_UU(s,U)=s*F(s);
F= -kf*T/(2 Lf Mf2 sqrt(1-z1²*s) sqrt(1+kf²*s) At),
At = beta3 Lf² + 2 beta2 Lf Lg + beta1 Lg²,
T  = (3 beta3 Lf² + 2 beta2 Lf Lg - beta1 Lg²)*sqrt(1-z1²*s)
     +4 beta2 Lf Lg +4 beta1 Lg².
Lf=b(1+cf*s)²>0, Lg=a(1+cg*s)²>0, At>0, T>0, kf<0.
F'/F=T'/T-Lf'/Lf-R1'/R1-R2'/R2-At'/At.
```

L'arithmétique d'intervalles **fractions exactes sur TOUT L'INTERVALLE CONTINU en UNE SEULE cellule** (pas des points numériques) prouve `F'/F>0` et surtout

```text
4/5 < G_sUU(s,U)=F(s)*(1+s F'/F) < 1
sur tous s ∈ [0,289/400], tous U. G_UU(0)=0.
ENCADREMENTS PLUS PRÉCIS (indicatifs décimaux, vraies fractions dans manifeste) :
0.8239432487687015 < G_sUU < 0.9353760451877611.
```

**Théorème : G_UU est strictement croissant en s**, indépendamment de U. On calcule donc sa valeur MAX à UNE SEULE EXTRÉMITÉ `s=289/400`, avec encadrement des radicaux en fractions décimales 14 chiffres via `isqrt` entier et vérification des carrés :

```text
0.6338791317425377 < G_UU(289/400,U) < 0.6338791317425752.
NOUVEAU CERTIFICAT UNIFORME EXACT:
0 <= G_UU(s,U) < 317/500 = 0.634   SUR TOUT [0,289/400], tous U.
(AMÉLIORATION de 337/500 du Step62.)
```

Le vrai tube Step55 `|U-Ustar|<=1/10000` implique par l'IDENTITÉ quadratique en U :

```text
|G_U(s,U)-G_U(s,Ustar)| < 317/5000000 = 0.0000634,
|G(s,U)-G(s,Ustar)-G_U(s,Ustar)*(U-Ustar)|
    < 317/100000000000 = 3.17e-9.
Ancien Step62 Taylor remainder: 3.37e-9.
```

C'est un progrès GÉOMÉTRIQUE et de conditionnement de l'EDO spatiale, PAS un calcul des lapses temporels ni du rang de Dirac. Une inversion du signe de la pente de la poussière f inverse le signe de G_UU : résultat BENCHMARK-dépendant, PAS universel pour HR.

## TESTS RÉELLEMENT EXÉCUTÉS ET REPRISE AUTOMATIQUE

```bash
cd /mnt/data/janus-step62
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step62_physical_G_curvature.py \
  tests/test_hr_step65_monotone_physical_curvature.py
# RÉEL : 32 PASSED en 2.88s ; 17 originaux Step62 + 15 nouveaux Step65.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step65_monotone_physical_curvature \
 > research/reports/gate2b-step65-local-manifest.json
```

Code/test Step65 sont BYTE IDENTIQUES GitHub aux exécutés, Git blobs ci-dessus. Le manifeste local complet contient toutes les FRACTIONS EXACTES `/mnt/data/janus-step62/research/reports/gate2b-step65-local-manifest.json` SHA256 `a9969377a56936b960a987c8b3d8e6958d9ef64e2c528c486ed650e009e6b7d3`; il N'EST PAS uploadé comme fichier distinct, l'essentiel est consigné dans `research/reports/gate2b-step65-report.json`. Ce tour n'a PAS rejoué les tests Step63–64, Step57–61 ni full CI. Les Actions restent OFF.

## NEXT STEP66 — VÉRITABLE VERROU TEMPOREL SIX COUPLES

1. Reconstituer et Git-hash vérifier les **vrais modules Steps57,58,59,60** dans le même worktree que Steps45/46/55 et Steps63/64 ; les calculs Step65 ne les importaient PAS. Avec la vraie branche Step55 strictement positive, réinjecter les jets `P',P'',P'''` certifiés jusque r=0 par Step64.
2. Imposer **la stationnarité complète du déplacement** `z=Z(D_g,K),zr=Z1,zrr=Z2` sans oublier la correction du défaut d'évaluation Step61 ; annuler les primaires Hg,Hf,Ddiag, la secondaire Cred et leurs dérivées spatiales cohérentes. Réduire les vrais 4 coefficients `A_N,B_N,A_M,B_M` de Step60 sur la donnée RADIALE exactement contrainte, pas sur un témoin manufacturé.
3. Alors seulement étudier rang du système des lapses, existence de lapses positifs compatibles, centre/bords et chartes K=0/J=0 ; valider avec un ORIGINAL oracle temporel non-IBP à six couples. Sans ces calculs, ABSENCE de fantôme BD et évolution 4D NON ÉTABLIES.
4. Préfixer encore `00_CURRENT_RESTART.md` à l'étape suivante ; conserver tout l'historique, main et V2 inchangés, Actions désactivées.

**BILAN : Step65 vraie fonction physique G : monotonie radiale STRICTE prouvée, borne G_UU améliorée, Taylor sensible resserré et 32 tests ciblés PASS. GATE2B OPEN ; JANUS-R NOT VALIDATED ; DIRAC TEMPOREL RANK NOT COMPUTED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP64 TERMINÉ — 2026-10-23

**SEULE BRANCHE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. NE PAS MODIFIER `main`, `research/v2-flrw`, GitHub Actions/workflows (désactivés). **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LECTURE PRIORITAIRE :** `research/STEP64_FULL_CENTER_PHYSICAL_PTHIRD_INTERVAL_AUDIT.md`.
**RAPPORT MACHINE, BORNES EN FRACTIONS EXACTES :** `research/reports/gate2b-step64-center-full-third-report.json`.
**CODE EXÉCUTÉ :** `numerics/hr_step64_center_third_jet.py` Git blob `07d80d70636952bcabf61bd8eb7da88cc8bc6c72`.
**TESTS 12 NOUVEAUX :** `tests/test_hr_step64_center_third_jet.py` Git blob `1db2c2c9cb7bad57cf2ffbb895b198ec61432d28`.
Les deux fichiers Step64 sont BYTE-IDENTICAL au code/test localement exécuté et ont été lus-vérifiés sur GitHub.
**PRÉCÉDENT :** `research/STEP63_REAL_G_GEOMETRY_INTERVAL_AD_RADIAL_HIGH_JETS_AUDIT.md`. Son `numerics/hr_step62_original_interval_ad.py` Git `a93bcd10cd54eec3b478ab0e02ff24fe592e4b8c` et `tests/test_hr_step62_original_interval_ad.py` Git `ce270b88c8731e61ed71bf4949ba1686b7a5b69b` sont des ressources créées en parallèle de l'autre Step62, mais affectées à STEP63. L'**AUTRE** véritable `research/STEP62_AUTHENTIC_G_QUADRATIC_CURVATURE_CERTIFICATE.md` et `research/reports/gate2b-step62-report.json` sont PRÉSERVÉS sans changement : ce travail avait prouvé analytiquement `0<=G_UU<337/500` pour le benchmark. Ne PAS écraser le Step62 existant ou confondre les rapports.

## NOUVELLE AVANCÉE EXACTE — PREMIÈRE CERTIFICATION GLOBALE DU VRAI P''' AU CENTRE

Vraie EDO radiale Step55: `s=r², P=pLf=r²U(s), 2s U_s=G(s,U)-2U`, branche originale positive régulière analytique issue du Step49, `U(0)=U0`. La source originale authentique donne au centre `G(0,U)=3U0-U`. Les **QUATRE** fichiers originaux physiques importés/testés BYTES EXACTS :

```text
numerics/hr_step45_exact_physical_ward.py  66aa43841dccfe4a5d586a49be9c10af3a67a10e
numerics/hr_step46_exact_secondary_ode.py bac025c28dbe1561c0c36c56dbfda46dc326f804
numerics/hr_step55_normalized_secondary.py a54a6acf2f7ad2f64c500faecfa1406ecbf7b862
numerics/hr_step55_global_barrier.py a6e7004120d0a166a3a8973c2fbe1487a8eb70fe
```

Step63 avait réellement REJOUÉ le certificat Step55 global 256-cellules et ses deux inégalités de barrières strictes, puis certifié par AD à géométrie complète et arrondi entier extérieur 10^-28 `P''` sur **TOUT** r∈[0,.85], mais `P'''` seulement sur 255 cellules intérieures, faute de borne directe du quotient `(G-2U)/s` au centre.

**Solution STEP64 : facteur intégrant et enveloppe uniforme de U.** Poser `W=U-U0`, `A(s,U)=[G(s,U)-(3U0-U)]/s=∫_0^1 G_s(ts,U)dt`. De l'EDO EXACTE :

```text
2s W_s +3W = s A(s,U(s)).
W(s)= s^(-3/2)/2 * integral_0^s t^(3/2) A(t,U(t)) dt.
Si |A|<=B, alors |W/s|<=B/5, et |U_s|<=4B/5, s>0,
avec prolongement régulier par continuité au centre.
```

IMPORTANT : pour borner `G_s(t,U(s))` à U(s) FIXE lors de l'intégration sur t≤s, utiliser une BOÎTE UNIFORME en U contenant **tous** les `Ustar(s)±1e-4` Step55 pour tout s∈[0,289/400]. Le seul tube mobile `Ustar(t)±delta` ne suffit pas ! Le nouveau code calcule donc le MAX ABS GLOBAL de G_s(t,U) dans les 256 cellules continues en t × boîte uniforme U, via `hr_step62_original_interval_ad.py` et le réel module historique `hr_step55_global_barrier.py`.

```text
B = 21885092944341379217378943/5000000000000000000000000000
  ≈0.004377018588868276.
|U_s|<=4B/5 ≈0.003501614871094621 sur TOUT [0,289/400].
P'''(r)=2r[H_s+H_U U_s], H=G+2s G_s+(G-2U)G_U.
```

**CERTIFICAT NOUVEAU EN FRACTIONS EXACTES, `0<=r<=17/20=0.85`, sur TOUS les 256 intervalles incluant r=0 :**

```text
-157117705762868039310811/625000000000000000000000000
 <= P'''(r) <=
  128641166369078726897489771/5000000000000000000000000000

Décimal strict volontairement élargi : -0.000252 < P'''(r) < 0.025729.
La cellule centrale r=0 incluse : 0<=P'''<=
16458628607489610074397529/10000000000000000000000000000.
```

La borne est **conditionnée à la branche physique RADIALE initiale exacte positive et analytiquement régulière de Step49/55** ; le calcul ne re-prouve PAS son existence au centre indépendamment. Il ne prouve pas d'évolution en temps 4D, ni rang de Dirac ni absence de fantôme BD.

## EXÉCUTIONS, TESTS ET VRAIE PROVENANCE

```bash
cd /mnt/data/janus-step62
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step64_center_third_jet.py tests/test_hr_step62_original_interval_ad.py
# VRAIMENT EXÉCUTÉ : 27 passed in 23.56s
# =12 NOUVEAUX Step64 +15 vrais tests Step63 originaux.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step64_center_third_jet 256 > research/reports/gate2b-step64-center-full-Pthird.json
# Local brut généré SHA256: 19bc8c6633714e99582e0f41a3e3a88782d0edccd479e537f7a3ee27554cc7f3
```

Les deux nouveaux fichiers + quatre historiques ont été Git-hash vérifiés exactement. Le brut de sortie a été généré LOCALLEMENT, NON uploadé comme artefact indépendant ; ses fractions et métadonnées sont sur GitHub dans `research/reports/gate2b-step64-center-full-third-report.json`. **27 nouveaux+anciens tests ciblés Step63–64 passés ensemble**, mais ne pas prétendre avoir rejoué les 17 tests de l'autre Step62, les Steps57–61 ou toute la suite du dépôt/CI. Actions OFF.

## NEXT STEP65 — VÉRITABLE VERROU DIRAC TEMPOREL, TOUJOURS OPEN

1. Reconstituer et SHA-verifier les vrais modules physiques `hr_step57_secondary_principal_symbol.py`, `hr_step58_temporal_operator.py`, `hr_step59_third_jet_gate.py`, `hr_step60_full_constraint_prolongation.py`, et profil original Step55 dans un worktree cohérent. Ces quatre modules temporels N'ONT PAS été importés/rejoués pendant Steps63–64.
2. Évaluer les **4 vrais coefficients d'ordre inférieur des lapses** `A_N,B_N,A_M,B_M` sur les données radiales EXACTEMENT contraintes, en utilisant maintenant nos jets P'',P''' certifiés sur tout le rayon ; `z=Z(Dg,K),zr=Z1,zrr=Z2` à imposer **cohérents** (correction Step61), toutes contraintes et prolongations Step60. Puis, seulement ensuite, calcul du vrai rang, existence de lapses positifs, conditions de bord et exception K=0/J=0.
3. Oracle physique original non-IBP TEMPOREL indépendant, six couples et deux poussières, pour valider une éventuelle conclusion de ghost-freedom ; comparer Step62 courbure exacte et Step63 dérivées totales sans mélanger les hypothèses.
4. **Préfixer à nouveau `00_CURRENT_RESTART.md` avec état, Git SHA, tests, hypothèses et étapes. Ne jamais réécrire l'historique ni main/V2.**

**BILAN : Étape64 certifie P''' sur TOUT [0,0.85], y compris centre, depuis la VRAIE équation originale Step55. Rang DIRAC/lapse fixing/JANUS-R encore OPEN.**

---

# JANUS — REPRISE PRIORITAIRE : STEP63 TERMINÉ — 2026-10-23

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. NE PAS MODIFIER `main` ni `research/v2-flrw`. Ne PAS réactiver GitHub Actions/workflows. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LECTURE PRIORITAIRE :** `research/STEP63_REAL_G_GEOMETRY_INTERVAL_AD_RADIAL_HIGH_JETS_AUDIT.md`.
**RAPPORT MACHINE (fractions EXACTES) :** `research/reports/gate2b-step63-original-interval-report.json`.
**CODE :** `numerics/hr_step62_original_interval_ad.py` Git blob `a93bcd10cd54eec3b478ab0e02ff24fe592e4b8c`.
**TESTS :** `tests/test_hr_step62_original_interval_ad.py` Git blob `ce270b88c8731e61ed71bf4949ba1686b7a5b69b`.
Ces noms Step62 correspondent au module élaboré parallèlement à l'autre Step62, conservé tel quel pour éviter une réécriture inutile; le rapport et la progression scientifique sont **STEP63**. Les DEUX nouveaux fichiers sont byte-identiques aux originaux exécutés et SHA-vérifiés dans le GitHub actuel.

**L'AUTRE STEP62 PRÉSERVÉ ET NON ÉCRASÉ :** `research/STEP62_AUTHENTIC_G_QUADRATIC_CURVATURE_CERTIFICATE.md`, `research/reports/gate2b-step62-report.json`, `numerics/hr_step62_physical_G_curvature.py`. Il démontre EXACTEMENT deg_U G=2, G_UUU=0, et strictement `0<=G_UU<337/500` sur le benchmark, avec 17 tests Step62. Il n'avait PAS réimporté les octets originaux du quatrième module de barrière globale. NOTRE étape 63 le fait et ajoute les dérivées **géométriques TOTALES** avec un AD bivarié 256-cellules. Ne pas fusionner naïvement les deux preuves ni prétendre que Step62 était absent !

## VRAIES SOURCES PHYSIQUES IMPORTÉES ET EXÉCUTÉES

Les QUATRE modules originaux GitHub sont **BYTE-IDENTIQUES**, testés `git hash-object` et authentifiés à chaque appel :

```text
numerics/hr_step45_exact_physical_ward.py  66aa43841dccfe4a5d586a49be9c10af3a67a10e
numerics/hr_step46_exact_secondary_ode.py bac025c28dbe1561c0c36c56dbfda46dc326f804
numerics/hr_step55_normalized_secondary.py a54a6acf2f7ad2f64c500faecfa1406ecbf7b862
numerics/hr_step55_global_barrier.py a6e7004120d0a166a3a8973c2fbe1487a8eb70fe
```

La VRAIE équation sphérique positive-EH Hassan–Rosen à deux poussières et SIX couples donne `s=r²`, `P=pLf=r²U(s)`, `2s U_s=G(s,U)-2U`, `G=P'/r`. G comporte 1048 opérations SymPy dans original Step55 et des paramètres `Lg0(s),Lf0(s),Sgr0(s),...` qui dépendent de s. Ne JAMAIS prendre simplement `∂_s G` en laissant cette géométrie physique figée ! Un test original compare la dérivée avec géométrie figée et la vraie dérivée totale, résultat strictement différent. Le nouveau moteur a un JET TAYLOR bivarié d'ordre 2 avec des coefficients `I` du vrai Step55, arrondi entier extérieur à **10^-28**, racines/inverses et tous les produits exacts; recouvre les **256 cellules continues** s∈[0,289/400] × tube Ustar±1e-4.

**CERTIFICAT STEP55 REJOUÉ DE BOUT EN BOUT :** `original.certify_global_barrier(256)` retourne exactement `max Fplus=-1480966474499367232302129/10^28<0` et `min Fminus=295653233337826329055403/(2*10^27)>0`; signatures de poussières positives et J/K restent issues du certificat historique.

## NOUVEAUX RÉSULTATS DE DÉRIVATION ORIGINALE CERTIFIÉS SUR LE CONTINUUM

```text
0 <= s=r² <=289/400, 0<=r<=17/20 et U dans tube Step55 exact :
0.003704 < G_s < 0.004085          (DERIVEE TOTALE géométrie incluse)
-1.003   < G_U < -0.992
-0.000161< G_ss < -0.000138
0.00318  < G_sU < 0.00705
-0.020   < G_UU < 0.655            (encadrement AD, pas preuve de signe).
NOTE : l'AUTRE audit Step62 analytique prouve plus fortement 0<=G_UU<0.674.
P'' = G+2s*G_s+(G-2U)*G_U :
     -0.014708 < P'' < 0.000685 sur TOUT [0,0.85].
P''' = 2r[H_s+H_U*(G-2U)/(2s)], H=P'' :
     -0.117 < P''' < 0.120 sur les 255 cellules s>289/(400*256).
!!! Première cellule avec s=0 : P''' NON CERTIFIÉ par cette méthode
    à cause du quotient (G-2U)/s avec tube Ustar±1e-4 de largeur constante.
```

Les bornes de rapport sont également sauvegardées sous forme de fractions rationnelles EXACTES dans `gate2b-step63-original-interval-report.json`. La vraie technique est continûment valide sur chaque cellule, PAS de simple échantillonnage ponctuel ou différence finie. L'intervalle AD G_UU peut croiser zéro bien que l'identité analytique Step62 prouve le signe : ceci reflète seulement la dépendance pessimiste des intervalles, pas une contradiction.

## EXÉCUTIONS ET LIMITES

```bash
cd /mnt/data/janus-step62
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step62_original_interval_ad.py
# RÉELLEMENT REJOUÉ : 15 PASSED IN 11.42s
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step62_original_interval_ad 256 > research/reports/gate2b-step62-raw-intervals.json
# Fichier local brut produit, sha256 4b5dbf232cea21cb92a59b095da2026eedbbdfdf379db180d6c3e3b080930e88
```

Le fichier brut n'a PAS été uploadé séparément comme fichier GitHub ; les FRACTIONS et SHA sont sauvegardées dans le rapport GitHub Step63. 15 tests nouveaux Step63 sont exécutés avec vrais 4 imports, ainsi qu'un contrôle complet 256-cellules de l'original Step55 ; NE PAS affirmer que les 17 tests de l'autre Step62 ou les Steps57–61 ont été rejoués conjointement. Le véritable crochet TEMPORAL Step60 et son rang de Dirac n'ont PAS été évalués.

## PROCHAIN VERROU — STEP64 / RED

1. **CENTRE :** prolonger le certificat de `P'''` à s=0 par l'EDO régulière `G(0,U)=3U0-U` et une estimation intégrale exacte sur `W=U-U0` : `2sW_s+3W=s A(s,U)`, `A(s,U)=(G(s,U)-G(0,U))/s`. Pour garantir `|A|`, construire un intervalle **uniforme en U pour toutes les abscisses intermédiaires** t≤s (la seule bande Ustar(t)±delta ne suffit pas pour G_s(t,U(s))). Puis `|W|/s<=max|A|/5`, `|U_s|<=4/5 max|A|`, et majorer `P'''=2r(H_s+H_U U_s)` avec les intervalles Step63. Prouver numériquement avec arithmétique extérieure sur les 256 cellules, pas extrapoler un jet lisse sans borne.
2. Reconstituer la chaîne physique Step57–60 et substituer ses véritables six-couples temporels avec `z=Z(Dg,K), zr=Z1,zrr=Z2` COHERENT (Step61), y compris tous les jets du profil original Step55. Évaluer les quatre coefficients `N,N',M,M'` et RANK sur une branche exacte; pas de ghost freedom avant.
3. Oracle original NON IBP TEMPOREL indépendant et bords ; chartes K=0 et J=0 hors du positif actuel.
4. Préfixer `00_CURRENT_RESTART.md` dès que nouveau résultat, conserver son historique, n'écrire que cette branche.

**BILAN : STEP63 original complet 4 sources et AD d'intervalles global, P'' certifié sur tout le rayon et P''' certifié sur les 255 cellules intérieures. DIRAC TEMPORAL ET LAPSE FIXING TOUJOURS OUVERTS. GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP62 TERMINÉ — 2026-10-23

**SEULE BRANCHE À MODIFIER :** `research/gate2b-nonhomothetic-transfer`. NE PAS modifier `main` ou `research/v2-flrw`. GitHub Actions/workflows doivent RESTER désactivés. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE IMMÉDIATEMENT :** `research/STEP62_AUTHENTIC_G_QUADRATIC_CURVATURE_CERTIFICATE.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step62-report.json`.
**NOUVEAU CODE :** `numerics/hr_step62_physical_G_curvature.py`, vrai blob Git `d2040a4bde9672933eac9bbab91b792005227f40`.
**17 NOUVEAUX TESTS :** `tests/test_hr_step62_physical_G_curvature.py`, vrai blob Git `b8e432ff4afe4a53b7d54150f174706a5b65460b`. Ces deux nouveaux fichiers sont **byte-identical GitHub vs versions localement exécutées**.
**3 SOURCES PHYSIQUES HISTORIQUES RECONSTITUÉES, IMPORTÉES ET VERIFIÉES BYTE-IDENTICAL :** `numerics/hr_step45_exact_physical_ward.py` Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; `numerics/hr_step46_exact_secondary_ode.py` Git `bac025c28dbe1561c0c36c56dbfda46dc326f804` ; `numerics/hr_step55_normalized_secondary.py` Git `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
**PRECEDENT :** `research/STEP61_NORMALIZED_RADIAL_ODE_JETS_AND_SHIFT_CONSISTENCY_AUDIT.md`, 15 tests standalone.

## RÉSULTAT SCIENTIFIQUE PHYSIQUE INÉDIT STEP62 : VRAIE FONCTION G ET COURBURE CERTIFIÉE

Contrairement à Step61, nous avons exécuté le VRAI `G(s,U)` calculé par `hr_step55_normalized_secondary.normalized_symbolic()` depuis l'action positive-EH HR originale à SIX couples et deux poussières (étapes 45,46,55). L'expression originale possède 1048 opérations SymPy. Résultat EXACT à partir de cette source originale, et NON d'un exemple artificiel :

```text
s=r², P=pLf=r²U(s), 2s U_s=G(s,U)-2U.
degree_U(G)=2; d³G/dU³=0 identiquement; d²G/dU²(s=0)=0.
l=Lf0, g=Lg0, t=tf0, mf=Mf2, h=sqrt(1-s*z1²).
At=l² beta3+2*l*g beta2+g² beta1.
T=(3*l² beta3+2*l*g beta2-g² beta1)*h+4*l*g beta2+4*g² beta1.
G_UU= -s*t*T / [2*l*mf*sqrt(l²+s*t²)*h*At].
G_U(0,U)=-Sfr0/Lf0 ; at benchmark center = -1.
```

La factorisation G_UU ci-dessus est vérifiée exactement par SymPy : résidu ZÉRO après comparaison avec la véritable expression de l'original Step55. Elle est indépendante de U. Changement de signe de la pente de la poussière f, à géométrie fixe, inverse le signe de cette courbure.

**VRAI CERTIFICAT D'INTERVALLE RATIONNEL :** sur tout s∈[0,289/400]=[0,0.7225], pour la géométrie benchmark exacte de Step55 (Lg0=.4*(1+.0015s)² ; Lf0=.4*.5787707228025044*(1-.0012s)² ; tf0=-.0016 Lf0 ; z1=.004 ; Mf2=.10879548725² ; beta1=1,beta2=-4.2383993109,beta3=13.6801214252), les produits et divisions d'intervalles sont effectués EN FRACTIONS EXACTES, avec les racines délimitées rationnellement et vérifiées par carré. Preuve stricte `At>0`, `T>0` et dénominateur non nul, conduisant à :

```text
POUR TOUT 0<=s<=289/400, pour TOUT U:
       0 <= G_UU(s,U) < 337/500 = 0.674
et G_UU>0 pour s>0.
(Borne Fraction calculée ≈ 0.6736978758144369, décimal informatif seulement.)
```

**RÉSULTAT IMMEDIAT D'ERREUR QUADRATIQUE** : sur l'EXACTE solution radiale positive Step55, ancien certificat `|U-Ustar|<=1/10000`. Puisque G est exactement quadratique :

```text
G(s,U)-G(s,Ustar)-G_U(s,Ustar)*(U-Ustar)
                  = G_UU(s)/2*(U-Ustar)^2 EXACTEMENT.
|G_U(s,U)-G_U(s,Ustar)| < 337/5000000 = 6.74e-5.
|G(s,U)-G(s,Ustar)-G_U(s,Ustar)*(U-Ustar)|
                                  < 337/100000000000 = 3.37e-9.
```

Ces bornes s'étendent à TOUT le benchmark radial certifié sans échantillonnage. Ce sont des **bornes sur les variations en U**, PAS sur les dérivées totales par s ; elles ne prouvent PAS encore P''/P''' global, ni les 4 coefficients de lapses du Step60 ou le rang de Dirac.

**NUANCE DE PROVENANCE:** les TROIS modules originaux Step45/46/55 sont vraiment byte-authenticated et importés localement. La géométrie benchmark est une transcription littérale en `Fraction` du vrai fichier historique `hr_step55_global_barrier.py` consulté sur GitHub, mais ce QUATRIÈME fichier n'a PAS été importé ni byte-vérifié dans le nouveau workspace Step62. La prochaine étape doit corriger cette dernière limite avant les dérivées totales.

## VRAIE EXÉCUTION, OCTETS ET TESTS

```bash
cd /mnt/data/janus-step62
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step62_physical_G_curvature.py
# RÉELLEMENT EXÉCUTÉ FINAL : 17 PASSED en 2.57 secondes.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step62_physical_G_curvature
```

Les tests comprennent vrai G original et source-pin fail-closed, G_UUU=0, identité G_UU, centre et pente poussière f, certificat arithmétique d'intervalle sur tout s, tests négatifs pour arithmétique et signe, deux bornes du tube Taylor. Nouveau code + nouveaux tests byte-identical au HEAD GitHub vérifié. Le manifeste brut local existe `/mnt/data/janus-step62/research/reports/gate2b-step62-local-manifest.json`, SHA256 `2e99f43bda32edbbf47380d1806f913a99fca2203de21da8de63174bd0ccb814`, mais n'a PAS été téléversé comme artefact indépendant ; le rapport `research/reports/gate2b-step62-report.json` stocke toute la preuve et les fractions. Aucune CI ni anciens tests Steps57–61 réexécutés dans ce workspace ciblé ; ne pas prétendre 73/73 tests cumulés comme une exécution commune.

## STEP63 — PROCHAIN VERROU PHYSIQUE

1. Reconstituer et PINNER aussi `numerics/hr_step55_global_barrier.py` en octets EXACTS depuis GitHub. Employer son VRAI `geometry(s)` et le G original ici vérifié, pour les dérivées TOTALES en s des champs métriques/dust et de `G(s,U)`, pas simplement les dérivées PARTIELLES à géométrie fixée.
2. Certifier sur la vraie solution positive du Step55, avec arithmétique d'intervalles, les grandeurs `G_s,G_U,G_ss,G_sU` et notamment les limites régulières au centre s=0 ; appliquer le bridge Step61 pour obtenir P'',P''' bornés.
3. Importer ensuite l'opérateur six-pair temporel original Step60 et imposer `z=Z(Dg,K),zr=Z1,zrr=Z2` avec toutes primaires, secondaire et prolongations radiales sur le profil EXACT Step55, puis tenter le rang/multiplicateurs/rapport des lapses. NE PAS DÉDUIRE rang ni absence BD du seul certificat G_UU.
4. Comparaison indépendante non-IBP du VRAI crochet temporel, bords et secteurs exceptionnels K=0/J=0.
5. Préfixer cette même reprise après chaque progrès sans écraser l'historique, conserver main/V2 et Actions intacts.

**VERDICT : propriété exacte du G physique originale démontrée + courbure G_UU uniformément bornée et reste Taylor global rigoureux sur Step55. PRÉSERVATION TEMPORELLE, RANG DIRAC, FIXATION DES LAPSES, ABSENCE DU FANTÔME BD, ÉVOLUTION 4D NON ÉTABLIS ; Gate2B OPEN, JANUS-R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP61 TERMINÉ — 2026-10-23

**SEULE BRANCHE DE RECHERCHE AUTORISÉE AUX ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`. NE PAS modifier `main` ni `research/v2-flrw`. Ne pas réactiver GitHub Actions/workflows. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP61_NORMALIZED_RADIAL_ODE_JETS_AND_SHIFT_CONSISTENCY_AUDIT.md`.
**RAPPORT MACHINE ARCHIVÉ :** `research/reports/gate2b-step61-report.json`.
**NOUVEAU CODE :** `numerics/hr_step61_normalized_jet_lift.py`, Git blob `b345169d8806ce524527229c794ace71cf5d540e`.
**15 TESTS NOUVEAUX :** `tests/test_hr_step61_normalized_jet_lift.py`, Git blob `08da0dba3aac34a5cd631a48ba6258d3ecfd01c2`. Deux empreintes vérifiées sur GitHub identiques aux OCTETS VRAIMENT exécutés.
**SOURCES HISTORIQUES SEULEMENT CONSULTÉES** pour cette étape autonome : Step55 `numerics/hr_step55_normalized_secondary.py` Git `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step60 `numerics/hr_step60_full_constraint_prolongation.py` Git `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`. Elles n'ont PAS été importées ni entièrement rejouées dans le workspace nouveau. Ne pas prétendre « full historical suite ».
**PRÉCÉDENT :** `research/STEP60_FULL_CONSTRAINT_RADIAL_PROLONGATION_AUDIT.md`, avec 56 tests Step57–60 passés dans leur propre environnement de la session précédente.

## NOUVELLES IDENTITÉS EXACTES STEP61 — JETS COHÉRENTS DE L'EDO CERTIFIÉE STEP55

Les données exactes spatiales Step55 : `s=r², P=pLf=r²U(s)`; `V=P'/r=G(s,U)` ; `2s U_s=G(s,U)-2U`. Cette EDO normalisée est fondée sur la vraie secondaire physique originale dans Steps45/46/55, mais Step61 vérifie la règle de dérivation comme une ALGÈBRE AUTONOME et non encore en substituant la fonction G physique originale.

```text
P' = r G(s,U)
H(s,U) = G + 2s*G_s + (G-2U)*G_U
P'' = H(s,U)
P''' = 2r[H_s + H_U*(G-2U)/(2s)], pour s>0.
```

Ces dérivées sont exactes SUR l'EDO. Les deux variables partielles de G sont `s` et `U` prises indépendamment avant restriction à la solution. Pour le vrai Dirac Step60, les jets d'ordre 2/3 de pLf DOIVENT respecter ces relations. Au centre `s=0`, n'évaluez PAS naïvement le `0/0` : employer la série régularisée.

**Centre :** Step55 possède `G(0,U)=3U0-U`; écrire `G=3U0-U+s A(s,U)`. Alors pour `U(s)=U0+Σ_{n>=1} U_n s^n` :

```text
(2n+3)*U_n = coefficient de s^(n-1) dans A(s,U(s)),
n >=1 ; denominators 5,7,9,... NONZERO.
U1=G_s(0,U0)/5,
U2=[G_sU(0,U0)*U1 + G_ss(0,U0)/2]/7.
P''(0)=2 U0 ; P'''(0)=0 ; limit (P'''/r) =24 U1.
```

La règle générale est une RÉCURRENCE FORMELLE exacte, pas le calcul des vraies valeurs U_n du modèle sans la fonction G physique.

**NOUVELLES BORNES RATIONNELLES IMMÉDIATES (et réellement dérivées du vrai certificat Step55) :**

```text
0<=r<=17/20 ; s<=289/400.
Step55 : |U-Ustar|<=1/10000 ; |V-Vstar|<41/20000.
Donc |P-Pstar|<=289/4000000 = 0.00007225.
Et  |P'-Pstar'|<697/400000 = 0.0017425.
Mais AUCUNE BORNE P''/P''' ne découle de ces deux seules inégalités ;
il faut compiler les vraies dérivées G_s,G_U,G_ss,G_sU,G_UU
avec leurs bornes d'intervalles sur le tube physique Step55.
```

**CONTRÔLE NOUVEAU DE COHÉRENCE STEP60 :** la vraie racine du shift requiert `zr=Z1` aussi DANS l'expression de `z''` construite avec `Dt(ZD)`, `Dt(ZK)`. Si `zr` reste un symbole libre, le défaut exact vaut :

```text
ZD=(1-z²)^(3/2)/K, ZK=-z(1-z²)/K,
Z1=ZD*Dg' + ZK*K',
Delta_Z2 = (zr-Z1)/K * [-3*z*sqrt(1-z²)*Dg' + (3*z²-1)*K'].
```

Ce défaut s'annule EXACTEMENT pour `zr=Z1`, mais est GÉNÉRIQUEMENT NON NUL si `zr=0` ou reste indépendant. **Les identités d'annulation des jets TROISIÈMES de Step60 ne sont pas réfutées** : le défaut porte sur les jets inférieurs, dont l'évaluation physique reste justement ouverte. Ne pas conclure au rang physique avant substitution de `z,z',z''` cohérente.

## EXÉCUTION VÉRIFIÉE, TESTS ET PORTÉE RÉELLE

```bash
cd /mnt/data/janus-step61
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step61_normalized_jet_lift.py
# RÉELLEMENT EXÉCUTÉ : 15 passed in 1.13 s.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step61_normalized_jet_lift
```

Les 15 tests incluent formules de chaîne jusqu'à P''', solution analytique manufacturée, dénominateurs sans résonance (10 premiers ordres formels), premières valeurs centrales, comportement pair, bornes de fractions exactes, CONTRE-EXEMPLE montrant qu'un tube (U,U_s) seul ne contrôle pas U_ss, et défaut exact de z'' pour z' indépendant, avec contrôle négatif z'=0. **Le contre-exemple manufacturé n'est PAS une autre solution de la même EDO JANUS.**

Le manifeste brut existe LOCALLEMENT : `/mnt/data/janus-step61/research/reports/gate2b-step61-local-manifest.json` SHA256 `6ae2f7f56ebb790f7be501ea72a528e216d5798fae6212ec7483d5584d88ef94`. PAS téléversé séparément sur GitHub ; rapport machine `research/reports/gate2b-step61-report.json` et module complet y sont commités. Les 56 tests Step57–60 ne furent PAS réexécutés dans ce workspace partiel ; pas de full CI ni de full physical Step60 temporal rank.

## STEP62 — LES ACTIONS CRITIQUES À REPRENDRE APRÈS INTERRUPTION

1. Reconstituer le VRAI dépôt ou un environnement cohérent octet-authentique Steps45,46,55,57,58,59,60. Importer le véritable `G(s,U)` par `numerics.hr_step55_normalized_secondary.normalized_symbolic()`, y compris paramètres physiques rationnels exacts.
2. Différentier G, calculer/valider des bornes d'intervalles `G_s,G_U,G_ss,G_sU,G_UU` sur le tube Step55, y compris normalisation `s=0`. Les formules Step61 donnent alors les jets P',P'',P''' certifiables sur l'EXACTE solution radiale.
3. Réduire l'opérateur temporel Step60 en substituant **z=Z(Dg,K), zr=Z1, zrr=Z2**, puis toutes les primaires/secondaire et leurs dérivées spatiales compatibles et les jets de P physiques. Évaluer les quatre coefficients N,N',M,M' et traiter rang et conditions de bord. Séparer chartes K/J exceptionnelles.
4. Valider contre le CROCHET TEMPOREL ORIGINAL NON IBP à six couples indépendant (non calculé jusqu'ici) ; ne pas déduire absence du fantôme BD sans clôture de Dirac.
5. Après toute avancée, préfixer `00_CURRENT_RESTART.md` et vérifier les véritables HEADs ; laisser `main`, V2 et Actions intacts.

**VERDICT : Step61 exact ODE-to-jet bridge + coherent stationary shift z'' audit, 15 standalone tests ; full physical temporal Dirac rank/lapse fixing OPEN ; Gate2B OPEN ; JANUS-R NOT_VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP60 TERMINÉ — 2026-10-23

**SEULE BRANCHE AUTORISÉE AUX ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`. Ne PAS modifier `main` ou `research/v2-flrw`, ne PAS réactiver Actions/workflows. **Gate2B OPEN, JANUS-R NOT_VALIDATED**.

**LIRE D'ABORD :** `research/STEP60_FULL_CONSTRAINT_RADIAL_PROLONGATION_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step60-report.json`.
**NOUVEAU MODULE PHYSIQUE EXACT :** `numerics/hr_step60_full_constraint_prolongation.py` Git blob `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`.
**NOUVEAUX 12 TESTS :** `tests/test_hr_step60_full_constraint_prolongation.py` Git blob `1e9a0f227af3795297de882964b53337225db9ce`.
**QUATRE DÉPENDANCES AUTHENTIFIÉES OCTET-PAR-OCTET :** original six-pair `numerics/hr_step45_exact_physical_ward.py` `66aa43841dccfe4a5d586a49be9c10af3a67a10e`; `hr_step57_secondary_principal_symbol.py` `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`; `hr_step58_temporal_operator.py` `802c23aebd41780d8c462f1aa1711707fe4ee88f`; `hr_step59_third_jet_gate.py` `ae26a79cbfa7bb50fbb398d7d6c18478adf7627e`. NOUVEAU code fail-closed si l'une de ces quatre sources diverge de sa vraie empreinte GitHub.

## RÉSULTAT SCIENTIFIQUE EXACT, PLUS FORT QUE L'ÉTAPE 59

On part du VRAI `C_exact(q,q',z,z')=K00-(K01)'` et des deux Hamiltoniens originaux `H_g,H_f`, six couples (deux poussières), EH positif. Étape58 : sur `Fz=Hg=0`, les jets `N''`,`M''` s'annulent IDENTIQUEMENT ; reste `dot C_red=A_N*N+B_N*N'+A_M*M+B_M*M'`.

Étape59 : les *parties principales* q''' des coefficients B_N,A_M étaient reliées aux contraintes Hg',C'_red. Étape60 : on a enfin construit les **DÉRIVÉES RADIALES COMPLÈTES**, sans jeter les termes de bas ordre, avec `z''` correct :

```text
Fz=Dg-K*z/sqrt(1-z²)=0, K>0, z=Dg/sqrt(Dg²+K²).
Z_D=(1-z²)^(3/2)/K ; Z_K=-z*(1-z²)/K.
z'=Z_D*Dg' + Z_K*K'
z''=Z_D*Dg''+Z_K*K''+(D_r Z_D)*Dg'+(D_r Z_K)*K'
Hg'=D_r[Hg_original] (total).
C'_red=D_r[C_original(q,q',z,z')], with z''=TRUE second prolonged root.
R_N=B_N + (1-z²)/(Lg Lf)*Hg'
R_M=A_M - (z/Lf)*C'_red
```

**THÉORÈME VÉRIFIÉ EXACTEMENT DANS SYMPY :** après élimination du véritable pLg' par Fz=0, **toutes les dérivées de R_N et R_M par rapport à chacun des DOUZE jets canoniques troisièmes sont IDENTIQUEMENT ZÉRO**. 4 dérivées q''' non triviales s'annulent : `∂R_N/∂Sg'''=0`, `∂R_M/∂pLg'''=∂R_M/∂Sg'''=∂R_M/∂tg'''=0`. Les autres q''' n'apparaissaient déjà pas. Les expressions sont AFFINES en ces jets ; cette propriété a été contrôlée avant d'extraire leurs représentants sans q'''.

**NOUVELLES EXPRESSIONS RÉUTILISABLES PAR LA REPRISE :** `full_constraint_prolongation()['third_free_BN_on_Fz']` et `['third_free_AM_on_Fz']` contiennent LES VRAIS RÉSIDUS DE BAS ORDRE, conservés exactement, sans q'''. Ils ne sont PAS prouvés nuls, et n'ont pas été évalués sur la solution exacte Step55. Ne PAS perdre ces expressions ou remplacer les dérivées de contraintes par leurs seuls termes dominants.

**DEUX CONTRÔLES NÉGATIFS EXACTS :** (a) mauvais signe de soustraction Hg' -> dérivée Sg''' = `-4 Mg² Sg(1-z²)/(Lf Lg²)` NON NULLE ; (b) figer z''=0 -> dérivée pLg''' = `z(1-z²)/Lf²` NON NULLE. Les tests échoueraient donc si l'on oubliait un terme critique du déplacement relatif ou la vraie contrainte.

## PROVENANCE ET TESTS RÉELLEMENT EXÉCUTÉS

Workspace isolé `/mnt/data/janus-step58`, avec les quatre originaux scientifiques pinés SHA Git, importés et exécutés ; ce n'est pas un clone complet du dépôt.

```bash
cd /mnt/data/janus-step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step57_secondary_principal_symbol.py \
 tests/test_hr_step58_temporal_operator.py \
 tests/test_hr_step59_third_jet_gate.py \
 tests/test_hr_step60_full_constraint_prolongation.py
# RÉEL : 56 PASSED in 9.23 seconds = 12 Step57 + 15 Step58 + 17 Step59 + 12 nouveaux Step60.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step60_full_constraint_prolongation
```

NOUVEAU CODE SHA `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509` et NOUVEAU TEST SHA `1e9a0f227af3795297de882964b53337225db9ce` sont vérifiés BYTE-IDENTICAL sur GitHub et dans les octets exécutés. Tests négatifs et garde-fou sur les quatre sources inclus. Pas de CI, Actions OFF. Pas de preuve complète des lapses.

## STEP61 — PREMIÈRE ACTION À REPRENDRE

1. Réduire les vrais résidus inférieurs `R_N`,`R_M` plus `A_N,B_M` via les **contraintes complètes et leurs prolongations radiales**, notamment `Fz,Fz',Fz'',Hg,Hg',Hf,Ddiag,C_red,C'_red`, sans confondre ce quotient q''' avec l'annulation des expressions. Utiliser les représentations sans q''' du module Step60. Imposer `z'=Z_DDg'+Z_KK'`, puis `z''` de la même racine, avec l'équation de secondaire exacte.
2. Sur la branche positive et régulière EXACTE de Step55 (pLf=r²U(s), U solution de l'EDO certifiée sur 0<=r<=.85), obtenir les jets cohérents par AD/ODE et mesurer/borner les 4 coefficients réduits. Attention aux normalisations r près du centre. Seulement alors étudier la matrice de multiplicateurs/lapses et son rang.
3. Valider avec une seconde méthode indépendante NON IBP du véritable CROCHET TEMPOREL de Dirac à six couples (l'original Step44 testait seulement le crochet mixte des primaires). Régularité des bords, chartes K=0/J=0 hors de la charte actuelle.
4. Préfixer une nouvelle section à `00_CURRENT_RESTART.md` après progrès, sans modifier l'historique. Conserver `main`/V2 et Actions inchangés.

**BILAN : annulation des q''' du véritable Dirac temporel prouvée après soustraction des CONTRAINTES RADIALES COMPLÈTES. RANG DIRAC, FIXATION DES LAPSES, SANTÉ GHOST et ÉVOLUTION 4D TOUJOURS OPEN. GATE 2B OPEN ; JANUS-R NON VALIDÉ.**

---

# JANUS — REPRISE PRIORITAIRE : STEP59 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne PAS modifier `main`, `research/v2-flrw` ni réactiver GitHub Actions/workflows. **GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

**LIRE EN PREMIER :** `research/STEP59_THIRD_RADIAL_JETS_CONSTRAINT_PROLONGATION_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step59-report.json`.
**NOUVEAU CODE EXÉCUTÉ :** `numerics/hr_step59_third_jet_gate.py`, Git SHA `ae26a79cbfa7bb50fbb398d7d6c18478adf7627e`.
**17 NOUVEAUX TESTS :** `tests/test_hr_step59_third_jet_gate.py`, Git SHA `ee6dd8f99e963c60a78c3b4f5a52000273b929c4`.
**SOURCES PHYSIQUES ORIGINALES BYTE-IDENTIQUES :** `numerics/hr_step45_exact_physical_ward.py` Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`; `numerics/hr_step57_secondary_principal_symbol.py` Git `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`; `numerics/hr_step58_temporal_operator.py` Git `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
**PRÉCÉDENT :** `research/STEP58_EXACT_PHYSICAL_TEMPORAL_OPERATOR_HIGH_LAPSE_CANCELLATION.md`.

## NOUVELLE AVANCÉE EXACTE : JETS CANONIQUES TROISIÈMES ET CONTRAINTES DIFFÉRENTIÉES

Le Step58 a démontré que sur Fz=Hg=0 les jets SECONDS de lapse disparaissent exactement et que l'opérateur temporel de la vraie secondaire réduite sur SIX couples a la forme
```text
dot C_red = A_N*N + B_N*N' + A_M*M + B_M*M' .
```
Step59 différentie EXACTEMENT les véritables coefficients `A_N,B_N,A_M,B_M` (original Step45 + total Dirac Step58) par rapport aux 12 jets de TROISIÈME dérivée canonique, après élimination Fz=0. TOUS les coefficients d'ordre 3 s'annulent sauf :

```text
d(B_N)/d(Sg''') = -2 Mg² Sg (1-z²)/(Lf Lg²)
d(A_M)/d(pLg''') = +z(1-z²)/Lf²
d(A_M)/d(Sg''')  = -pSg z(1-z²)/(Lg Lf²)
d(A_M)/d(tg''')  = -pg  z(1-z²)/(Lg Lf²)
A_N, B_M : aucune dépendance à des jets canoniques 3e ordre sur Fz=0.
```

**THÉORÈME DE PARTIE PRINCIPALE** : le vrai primaire Hg ne comporte qu'un seul jet canonique d'ordre 2 `dHg/dSg''=2Mg²Sg/Lg`, et la vraie secondaire réduite Step57 possède `dC_red/dpLg''=(1-z²)/Lf`, `dC_red/dSg''=-pSg(1-z²)/(LgLf)`, `dC_red/dtg''=-pg(1-z²)/(LgLf)`. Donc les parties principales d'ordre 3 sont EXACTEMENT

```text
(B_N)_(q''') = -(1-z²)/(Lg Lf) * (Hg')_(q''')
(A_M)_(q''') = +z/Lf * (C_red')_(q''')
                = -z(1-z²)/(Lg Lf²) * (Dg'')_(q''') .
```

Ceci identifie les bonnes contraintes RADIALEMENT PROLONGÉES à soustraire dans l'étape suivante. **IL NE S'AGIT PAS** d'une identité des COEFFICIENTS COMPLETS `B_N` ou `A_M` : leur partie de plus bas ordre reste à calculer. Il serait incorrect de fixer simplement les jets troisièmes à zéro ou de conclure au rang de Dirac par ce seul calcul.

**Stationnarité du déplacement prolongée 2 FOIS** sur `K>0`, `R=sqrt(Dg²+K²)`, `z=Dg/R` :

```text
z'=(K² Dg' - Dg K K')/R³
z''=(K² Dg'' + K K' Dg' - Dg (K')² - Dg K K'')/R³
    -3 (K² Dg' - Dg K K') (Dg Dg' + K K')/R⁵
Fz=Fz'=Fz''=0, exact on positive K root.
```

Au centre, si `Dg=r³ d(s),K=r² k(s)>0,s=r²`, alors `z=r*w(s)`, `z'=w+2s*w_s`, `z''=r(6w_s+4s*w_ss)`; z''=O(r) pour d,k réguliers C² en s. Cette parité n'est PAS une preuve 4D d'évolution régulière.

## EXÉCUTION RÉELLE ET PROVENANCE

Workspace local isolé `/mnt/data/janus-step58` avec sources 45/57/58 exactes GitHub. Nouveaux code+test byte-identiques à leurs octets réellement exécutés et vérifiés directement par les SHA GitHub.

```bash
cd /mnt/data/janus-step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step57_secondary_principal_symbol.py tests/test_hr_step58_temporal_operator.py tests/test_hr_step59_third_jet_gate.py
# 44 PASSED en 5.12s : 12 historiques Step57, 15 Step58, 17 NOUVEAUX Step59.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step59_third_jet_gate
```

Manifeste brut `/mnt/data/janus-step58/research/reports/gate2b-step59-local-manifest.json`, SHA256 `c2bbd8c3829c2333f61f586170502b0dbd0b0a1b7e8e4d71e0d38be12fe70012`, généré localement mais PAS uploadé ; formules/versions/tests dans `research/reports/gate2b-step59-report.json`. Pas de full suite originale ni CI, Actions toujours OFF.

## STEP60 — PROCHAINE ACTION INDISPENSABLE

1. Construire les dérivées radiales COMPLETES `Hg'` et `C_red'` de l'ACTION PHYSIQUE avec `z,z',z''` cohérents; puis former **exactement** les résidus `B_N+(1-z²)/(LgLf)*Hg'` et `A_M-(z/Lf)*C_red'`. Prouver qu'ils ne contiennent plus AUCUN q''' (pas seulement égalité de coefficients principaux), sans ignorer les autres termes de plus bas ordre.
2. Réduire les quatre coefficients complets `A_N,B_N,A_M,B_M` modulo `Fz,Fz',Fz'',Hg,Hg',Hf,Ddiag,C_red,C'_red` et les jets du profil global Step55 strictement positif. Déterminer le véritable opérateur des deux lapses et son rang, avec borne de stabilité/régularité au centre. Ne PAS déduire automatiquement la fixation des lapses.
3. Comparer avec une VARIATION TEMPORALE INDÉPENDANTE de la véritable action non-IBP originale à six couples, et vérifier bords et K/J exceptionnels. **RANG DIRAC / FIXATION DES LAPSUS / ABSENCE DE FANTÔME BD TOUJOURS NON ÉTABLIS**.
4. Préfixer de nouveau CE FICHIER sur la seule branche active ; conserver le contenu des étapes précédentes, main/V2 intacts et Actions désactivées.

**VERDICT : Step59 parties principales d'ordre 3 exactes, contraintes prolongées identifiées, shift z,z',z'' certifié algébriquement ; aucun rang de Dirac complet ni dynamique 4D validée. Gate2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP58 TERMINÉ — 2026-10-23

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`; ni `main` ni `research/v2-flrw`. Ne pas réactiver GitHub Actions/workflows. **GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

**LIRE EN PREMIER :** `research/STEP58_EXACT_PHYSICAL_TEMPORAL_OPERATOR_HIGH_LAPSE_CANCELLATION.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step58-report.json`.
**CODE :** `numerics/hr_step58_temporal_operator.py`, Git blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
**15 TESTS NOUVEAUX :** `tests/test_hr_step58_temporal_operator.py`, Git blob `0f9f91de0f607e811dc168e1ead0c3e9296574d0`.
**ORIGINAUX PHYSIQUES BYTE-AUTHENTIQUES :** `numerics/hr_step45_exact_physical_ward.py` Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `numerics/hr_step57_secondary_principal_symbol.py` Git `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`.
**PRÉCÉDENT :** `research/STEP57_SECONDARY_REDUCED_SECOND_JETS_AND_TEMPORAL_SYMBOL_AUDIT.md`.

## AVANCÉE RÉELLE STEP58

Pour la PREMIÈRE FOIS ici, l'évolution temporelle locale de la secondaire REDUITE de la véritable formulation positive-EH HR sphérique avec 2 poussières et SIX couples a été **assemblée exactement dans SymPy, sous forme de coefficients factorisés des jets des lapses**. `H_g,H_f,C` et les six gradients d'Euler de l'action originale Step45 sont importés en octets authentifiés GitHub. L'équation stationnaire positive `F_z=D_g-K z/sqrt(1-z²)=0` impose `z=D_g/sqrt(D_g²+K²)`. L'évolution est obtenue via les douze flux symplectiques originaux, y compris la dérivée de chaîne de `z,z'` :

```text
X_(q_i) = + Euler_(p_i) H[N,M]
X_(p_i) = - Euler_(q_i) H[N,M]
delta_H z = ((1-z²)^(3/2)/K)*delta_H Dg - z*(1-z²)/K*delta_H K
dot C_red = sum_i(C_qi X_i + C_qiprime D_r X_i)
          + C_z delta_H z + C_zprime D_r(delta_H z)
```

Cette écriture LOCALE est l'adjoint du crochet avec test compact eta : `integral eta dot C_red = {integral eta C_red, H_tot}` modulo bords contrôlés ; la construction garde toutes les dérivées implicites de z. En jet lapse symbolique, les SEULS ordres non nuls AVANT contraintes sont `N,N',N'',M,M',M''` ; pas de jets troisième/quatrième (constat de structure exacte, pas troncature).

**THÉORÈME ANALYTIQUE NOUVEAU ET TESTÉ :** sur `F_z=0`, éliminer exactement le jet `pLg'` original :

```text
pLg'=(pSg*Sg' + pg*tg' - K*z/sqrt(1-z²))/Lg.
coefficient [M''] | Fz=0 = 0  IDENTIQUEMENT
coefficient [N''] | Fz=0 = (z²-1)*Hg/(Lg*Lf) IDENTIQUEMENT
```

Donc les DEUX dérivées secondes des lapses s'annulent EXACTEMENT lorsque **Fz=0 et Hg=0**. L'opérateur TEMPOREL restant est de premier ordre :
```text
dot C_red | Fz=Hg=0 = A_N*N + B_N*N' + A_M*M + B_M*M'
```
Les 4 coefficients résiduels sont CALCULÉS et disponibles comme expressions SymPy FACTORISÉES dans `physical_operator()['operator']`, mais ne sont pas simplifiés/évalués sur les données EXACTEMENT contraintes Step55. **NE PAS CONFONDRE** les annulations des seconds jets avec une fixation de lapses ni avec un rang de Dirac calculé.

## TESTS RÉELLEMENT EXÉCUTÉS, OCTETS ET PORTÉE

```bash
cd /mnt/data/janus-step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step57_secondary_principal_symbol.py tests/test_hr_step58_temporal_operator.py
# 27 PASSED in 3.75 s = 12 Step57 + 15 NOUVEAUX Step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step58_temporal_operator
```

LES DEUX NOUVEAUX fichiers ont été comparés à leur vrai Git SHA sur GitHub et sont byte-identical aux octets locaux exécutés. La vraie source Step45 importée a été vérifiée par SHA à l'exécution. Inclut un banc d'essai exact IBP intégré, avec 2 paires actives d'une théorie à 6 paires manufacturée, NE PAS LE QUALIFIER d'oracle JANUS original non-IBP. Ce n'est PAS une suite complète de tests historiques, ni CI ; les workflows restent désactivés.

## NEXT STEP59 — HARD RED

1. Substituer la véritable branche radiale contrainte positive **Step55** (`Fz=Hg=Hf=Ddiag=C=0`), les jets compatibles de `z`, dans les **quatre** coefficients physiques factorisés `A_N,B_N,A_M,B_M`. Simplifier exactement si possible, sinon par AD certifiée et arithmétique d'intervalles ; comparer centre et intérieur. Ne pas confondre les coefficients d'ordre 1 avec la fixation des lapses.
2. Calculer la vraie matrice de Dirac/multiplicateurs, ses modes de jauge, le ratio relatif des lapses s'il existe et ses bords, en traitant `K=0/J=0` hors charte à part.
3. Oracle indépendant non-IBP TEMPORAL depuis l'action ADM originale avec toutes les variables canoniques (l'oracle Step44 ne testait que les primaires mixtes, pas le présent crochet temporel). Préserver les contraintes et le centre; ne pas annoncer absence du fantôme BD ni une 4D nonhomothetic on-shell tant que non démontrés.
4. PRÉFIXER à nouveau `00_CURRENT_RESTART.md` avec Git HEAD, fichiers, SHA, tests et limites, sans écraser l'historique ; branch main/V2 et Actions restent inchangées.

**CONCLUSION : véritable opérateur temporel local à six couples formellement reconstruit, et annulation EXACTE des seconds jets lapses sur primaires ; RANG DIRAC / LAPSE FIXING / ON-SHELL EVOLUTION NON ÉTABLIS. GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP57 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main` ni `research/v2-flrw` ; ne PAS réactiver GitHub Actions/workflows. **GATE_2B OPEN, JANUS-R NOT VALIDATED**.

**LIRE D'ABORD :** `research/STEP57_SECONDARY_REDUCED_SECOND_JETS_AND_TEMPORAL_SYMBOL_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step57-report.json`.
**NOUVEAU CODE :** `numerics/hr_step57_secondary_principal_symbol.py`, Git blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`.
**12 TESTS :** `tests/test_hr_step57_secondary_principal_symbol.py`, Git blob `1c97b1764ef4180deec48da8c68e138ed59b254a`.
**ORIGINAL PHYSIQUE IMPORTÉ BYTE-EXACT :** `numerics/hr_step45_exact_physical_ward.py`, Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` (vérification explicite à l'exécution). Précédent : `research/STEP56_SHIFT_RESPONSE_AND_TEMPORAL_DIRAC_JETS_AUDIT.md`.

## AVANCÉE EXACTE — SECONDE DÉRIVÉE CANONIQUE APPARAÎT APRÈS ÉLIMINATION DE Z

À partir du VRAI `C_exact=K00-(K01)'` Step45 à SIX couples (positif-EH HR+deux poussières), `C_exact(q,q',z,z')` dépend AFFINEMENT de z' (vérifié symboliquement) :

```text
Dg = pSg*Sg' - Lg*pLg' + pg*tg'
K  = m² Mg² Lg Lf (beta1 Sg² + 2 beta2 Sg Sf + beta3 Sf²)
Fz = Dg - K z/sqrt(1-z²) = 0
dC_exact/dz' = -(K sqrt(1-z²) + Dg z)/(Lg Lf)
             = -K/(Lg Lf sqrt(1-z²)) - z*Fz/(Lg Lf)
on the chart K>0, R=sqrt(Dg²+K²), Fz=0:
z=Dg/R ; dC_exact/dz'=-R/(Lg Lf).
```

Alors `C_red(q,q',q'')=C_exact(q,q',Z(Dg,K),dZ/dr)` possède EXACTEMENT les 3 dérivées secondes NON NULLES :

```text
d C_red / d pLg'' = + K²/(Lf R²)                = (1-z²)/Lf
d C_red / d Sg''  = - pSg K²/(Lg Lf R²)
d C_red / d tg''  = - pg  K²/(Lg Lf R²)
all OTHER nine second canonical radial jets = 0.
```

La variation fonctionnelle de `int eta C_red` DOIT donc inclure eta'' ; ne JAMAIS figer z dans la variation de la contrainte secondaire. Formule exacte du pullback pour chaque champ u (`D=d/dr` total ; C-partials à z,z' externes AVANT substitution) :

```text
T = eta*C_z - D(eta*C_zprime)
E_u(eta C_red) = eta*C_u - D(eta*C_uprime)
                + Z_u*T - D(Z_uprime*T)
```

La formule COMPLETE abstraite pour ses coefficients eta,eta',eta'' est implémentée et comparée à l'Euler direct d'ordre 2 d'un exemple symbolique de deux champs, avec égalité EXACTE.

## VÉRITABLE CONTRACTION HAMILTONIENNE SUR SIX COUPLES : PREMIER SYMBOLE DE DIRAC TEMPOREL

En employant les six vrais couples et gradients d'Euler `eg,ef` de Step45, le coefficient dans `{int eta C_red,H[N,M]}` devant `eta''` multiplié par chaque jet de lapse est calculé EXACTEMENT. Sur Fz=0, K,Lg,Lf,R>0 :

```text
coefficient [eta'' * M]  = - K²/(Lg Lf² R)                   NONZERO
coefficient [eta'' * N'] = - 2 Mg² Sg Sg' K²/(Lg² Lf R²)
coefficient [eta'' * N''] = 0
coefficient [eta'' * M']  = 0
coefficient [eta'' * M''] = 0
coefficient [eta'' * N]  = computed symbolic, not simplified.
```

**POINT SCIENTIFIQUE CRUCIAL :** ces termes appartiennent à l'INTÉGRANDE AVANT intégration par parties du paramètre-test eta. Les contributions de eta' et eta, non encore contractées complètement sur les 12 variables originales, peuvent annuler ou déplacer des termes de lapse. **NE PAS DÉDUIRE DE RANG DE DIRAC NI FIXATION DE LAPSES** de ce seul coefficient.

## EXÉCUTION ET PROVENANCE

Environnement isolé : `/mnt/data/janus-step57`, contenant le véritable fichier Step45 ORIGINAL Git blob identique `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, importé directement.

```bash
cd /mnt/data/janus-step57
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step57_secondary_principal_symbol.py
# RÉELLEMENT EXÉCUTÉ : 12 passed in 1.62s.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step57_secondary_principal_symbol
```

NOUVEAU CODE ET NOUVEAUX TESTS byte-identiques aux octets réellement exécutés ET vérifiés sur GitHub : blobs ci-dessus. Un contrôle purement numérique du test contenait d'abord une erreur de facteur 2, CORRIGÉE avant son upload ; 12/12 passent sur la version publiée. Le manifeste local `/mnt/data/janus-step57/research/reports/gate2b-step57-local-manifest.json`, SHA256 `d69b2245e37eb5057dd96bebe325cc6f3869166d16d83a88b0607a6c66198af3`, n'a PAS été déposé séparément ; l'essentiel est sauvegardé dans le rapport machine GitHub. Pas de réexécution de tout l'historique du dépôt, ni CI/Actions.

## STEP58 — LA SUITE EXACTE À EXÉCUTER APRÈS INTERRUPTION

1. **CALCULER TOUTES LES VARIATIONS TEMPORELLES :** depuis `abstract_pullback_coefficients`, calculer les gradients physiques eta0 et eta1 pour CHAQUE champ de la vraie secondaire Step45 éliminant z(Dg,K), y compris dépendances z' et dérivées des jets jusqu'à l'ordre nécessaire. Les contracter au Hamiltonien total Step45, LES SIX COUPLES et les deux lapses N,M.
2. **ADJOINT EXACT DES FONCTIONS TEST :** réunir eta0+eta1+eta2, intégrer par parties les dérivées de eta en retenant les BORDS. Identifier ensuite, et seulement ensuite, l'opérateur différentiel final en N,M sur la branche stationnaire positive.
3. **DIRAC :** calculer rang, contraintes de préservation, fixation ou non du rapport des lapses sur vraies données radiales exactement contraintes Step55. Traiter séparément K=0/J=0. Vérifier par oracle Poisson de l'action non-IBP originale et ne PAS annoncer absence de fantôme BD sans fermeture temporelle.
4. Toujours PRÉFIXER ce `00_CURRENT_RESTART.md` avec état, SHA, données réelles et limitations. Actions restent désactivées.

**BILAN : Step57 symbole de Dirac temporel PARTIEL mais PHYSIQUE ET EXACT dérivé des vrais six couples ; {C,Htotal} COMPLET ET RANG NON CALCULÉS. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP56 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main` ni `research/v2-flrw`. Ne PAS réactiver GitHub Actions/workflows. **GATE_2B=OPEN, JANUS-R=NOT_VALIDATED**.

**LIRE EN PREMIER :** `research/STEP56_SHIFT_RESPONSE_AND_TEMPORAL_DIRAC_JETS_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step56-report.json`.
**NOUVEAU CODE :** `numerics/hr_step56_shift_response.py` SHA Git `71bc56d3433e146c5671351e6ea21468ee5149ca`.
**14 TESTS :** `tests/test_hr_step56_shift_response.py` SHA `75efdc7b99af067f3f7c2b1bc4947cb5a7c9e48f`.
**PROVENANCE FORMULES ORIGINALES :** GitHub `numerics/hr_step45_exact_physical_ward.py` SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`; `numerics/hr_step46_exact_secondary_ode.py` SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804`. Ces fichiers furent lus depuis GitHub pour construire ce **module algébrique autonome**, mais n'ont PAS été importés en octets originaux dans le test local Step56. Ne pas prétendre entière chaîne historiquement réexécutée.

## NOUVELLE AVANCÉE MATHÉMATIQUE EXACTE — OPÉRATEUR DE DÉPLACEMENT RELATIF POUR LE DIRAC TEMPOREL

Le Step55 a certifié le profil radial initial contraint et positif sur r∈[0,.85] dans les données prescrites, mais n'a PAS traité l'évolution en TEMPS. L'étape 56 repart de la VRAIE équation de stationnarité algébrique de l'action positive-EH sphérique à SIX couples canoniques :

```text
Dg = pSg*Sg' - Lg*pLg' + pg*theta_g'
K  = m² Mg² Lg Lf (beta1*Sg²+2 beta2*Sg Sf+beta3*Sf²)
Fz = Dg - K*z/sqrt(1-z²)=0
sur la branche K>0 :
z = Dg/sqrt(Dg²+K²)
delta_z = (K² delta_Dg - Dg*K delta_K)/(Dg²+K²)^(3/2)
dot_z   = (K² dot_Dg - Dg*K dot_K)/(Dg²+K²)^(3/2)
```

La variation `delta_Dg` comprend ABSOLUMENT `-Lg delta(pLg')`. Pour un test radial compact `eta(r)`, il en résulte le noyau Poisson fonctionnel DISTRIBUTIONNEL exact :

```text
Z_D = K²/(Dg²+K²)^(3/2)
delta z(r)/delta pLg(x) = -Lg(r)*Z_D(r)*partial_r delta(r-x)
delta/delta pLg(x) [ integral eta(r)*z(r) dr ]
    = +partial_x[eta(x)*Lg(x)*Z_D(x)]
```

Pour des variations non compactes, garder EXPLICITEMENT le bord `-[eta Lg Z_D delta pLg]`. Cette dérivée de fonction test est une contribution importante au véritable crochet secondaire temporel et peut introduire dérivées des lapses. L'identité exacte `delta(z')=(delta z)'` a également été vérifiée avec les jets radiaux. Le Hamiltonien réduit satisfait l'enveloppe stationnaire `partial_z(N Hg+M Hf)=(N/Lg+M/Lf)Fz=0` sur Fz=0, MAIS la variation de `C_red` **DOIT** inclure ses dépendances implicites à `z,z',...` ; figer z dans les deux variations est incorrect. Un exemple symbolique à SIX couples indépendants prouve que cette omission donne un crochet différent, mais cet EXEMPLE n'est PAS le Dirac physique JANUS.

**CENTRE NORMALISÉ :** `Dg=r³ d(s), K=r² k(s)>0, w=z/r=d/sqrt(k²+s d²)`. Sur le benchmark stationnaire `z=.004r`, `partial_d w=(1-s*.004²)^(3/2)/k` et `partial_k w=-.004*(1-s*.004²)/k`. La borne certifiée Step55 `k>0.229` donne les nouvelles marges rationnelles EXACTES `0<partial_d w<1000/229<4.367` et `|partial_k w|<4/229<.0175` sur s∈[0,.7225]. Ceci est une sensibilité de shift, PAS une preuve dynamique 4D.

## EXÉCUTION RÉELLE ET LIMITES

```bash
cd /mnt/data/janus-step56
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step56_shift_response.py
# 14 PASSED in 2.00s.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step56_shift_response
```

Les DEUX nouveaux fichiers CODE/TEST sont Git blob BYTE-IDENTICAL aux octets exécutés (vérifiés DIRECTEMENT dans GitHub). Le test local est AUTONOME et ne contient PAS tout l'ancien dépôt : pas de full-suite/CI, pas de vrai `{C,Htotal}` calculé. JSON brut local `/mnt/data/janus-step56/research/reports/step56_shift_local.json` SHA256 `7541d626330d4cc8589bbc264ede472b8b81b1a92efdf054bf97fbcf29f3341e`, NOT uploaded as standalone GitHub file ; éléments essentiels et tests dans `research/reports/gate2b-step56-report.json`.

## STEP57 — LE VÉRITABLE VERROU PHYSIQUE RESTE OUVERT

1. Reconstituer l'ORIGINAL COMPLET `Hg,Hf,C_exact` à six couples depuis les vrais sources GitHub, avec `z[Dg,K]`, `z'` et jets, et calculer réellement `{C_red,H_total,red}` par équations canoniques et variations fonctionnelles. Utiliser les dérivées de shift, dérivées des fonctions test et bords démontrés ici. Ne pas doubler les termes de chaîne dans H grâce au théorème d'enveloppe.
2. Résoudre/simplifier l'OPÉRATEUR SUR LES LAPSUS et déterminer le rang de Dirac, la conservation secondaire, la fixation du rapport des lapses, les branches exceptionnelles K/J, tous sur le profil initial positif Step55. Ne pas supposer d'avance une élimination du fantôme BD.
3. Vérifier le résultat avec un oracle Poisson indépendant sur l'action d'origine non intégrée par parties, et la régularité tensorielle du centre.
4. Continuer à PREPENDRE ce fichier GitHub après chaque étape. Actions toujours désactivées.

**STATUT SCIENTIFIQUE : opérateur de réponse du déplacement relatif établi EXACTEMENT ; VRAI CROCHET TEMPORAL ET RANG DIRAC NON CALCULÉS. GATE 2B OPEN ; JANUS-R NOT VALIDATED.**

**ADMIN GITHUB :** historiques des anciennes branches main/V2 préservés en ascendance active via commit `4f7a3a1`; PR V2 #1 fermée sans fusion ; mais GitHub garde TROIS références et le défaut `main`. Le connecteur ne possède toujours pas les actions de changement du défaut/suppression de ref ; propriétaire doit effectuer Settings > Default branch -> active, puis supprimer V2/main dans Branches. Ne jamais annoncer « une branche » avant contrôle.

---

# JANUS — REPRISE PRIORITAIRE : STEP55 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE AUX ÉCRITURES : research/gate2b-nonhomothetic-transfer. NE PAS RÉACTIVER GITHUB ACTIONS. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**

**LIRE D'ABORD :** research/STEP55_GLOBAL_RADIAL_BARRIER_AND_POSITIVE_TWODUST_AUDIT.md
**RAPPORT MACHINE EXACT :** research/reports/gate2b-step55-report.json.
**NOUVEAU CODE NORMALISÉ :** numerics/hr_step55_normalized_secondary.py, Git blob a54a6acf2f7ad2f64c500faecfa1406ecbf7b862.
**NOUVEAU CODE D'INTERVALLES :** numerics/hr_step55_global_barrier.py, Git blob a6e7004120d0a166a3a8973c2fbe1487a8eb70fe.
**12 TESTS :** tests/test_hr_step55_global_barrier.py, Git blob 5dfb8036c66c9b2774847b0989be15ea41c65408.
**ORIGINAL PHYSIQUE BYTE-IDENTIQUE :** numerics/hr_step45_exact_physical_ward.py Git 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; numerics/hr_step46_exact_secondary_ode.py Git bac025c28dbe1561c0c36c56dbfda46dc326f804.
**TOUR PRÉCÉDENT :** research/STEP54_CONDITIONAL_CONTINUUM_TWODUST_INTERVAL_TUBE_AUDIT.md, certificat rationnel conditionnel à |U-Ustar|,|V-Vstar|<=.01.

## GRANDE AVANCÉE : TUBE STEP54 DÉSORMAIS PROUVÉ POUR LA VRAIE SOLUTION RADIALE CONTRAINTE

Au centre sphérique la branche analytique locale unique satisfaisant C=0 était garantie conditionnellement par le théorème Step49. Étapes52/53 fournissent U1/U2 algébriques exacts pour paramètres rationnels décimaux. Step55 part de l'équation de la secondaire physique construite depuis les SIX couples canoniques originales Steps45/46 et élimine symboliquement les facteurs factices en r :

    s=r², U(s)=pLf(r)/r², V(s)=pLf'(r)/r
    Ustar(s)=U0+U1*s+U2*s²
    Vstar(s)=2*U0+4*U1*s+6*U2*s²
    V=G(s,U) ; 2s U_s = G(s,U)-2U ; G(0,U)=3U0-U

**NOUVEAU THÉORÈME DE BARRIÈRES INVARIANTES CONTINUES.** Sur EXACTEMENT tout s∈[0,.7225], recouvert par 256 cellules rationnelles et arithmétique d'intervalles entière arrondie vers l'extérieur à l'échelle 10^-28, on démontre pour les murs Ustar±delta, delta=1/10000 :

    Fplus(s)=G(s,Ustar+delta)-2(Ustar+delta)-2s Ustar'(s)
           <= -1480966474499367232302129/10000000000000000000000000000 <0
    Fminus(s)=G(s,Ustar-delta)-2(Ustar-delta)-2s Ustar'(s)
           >= 295653233337826329055403/2000000000000000000000000000 >0.

La solution analytique centrale commence strictement entre les murs, le théorème de premier-contact empêche toute sortie à s>0 et l'EDO lisse sur la charte compacte non dégénérée s'étend jusqu'à .7225. Donc **SUR LA VRAIE BRANCHE RADIALE EXACTE** :

    |U-Ustar| <= .0001   sur r∈[0,.85].

La dérivée V doit être bornée distinctement ; la même évaluation d'intervalles sur toutes les valeurs U du tube donne EXACTEMENT :

    -10209601928354599272595789/5000000000000000000000000000
       <= V-Vstar <=
     20404447710211286903383733/10000000000000000000000000000.

Donc **-0.00205<V-Vstar<0.00205<0.01** partout. Les deux hypothèses du CERTIFICAT CONTINU Step54 sont désormais démontrées pour la solution radiale RÉELLE, pas simplement une famille hypothétique.

**CONSÉQUENCE (SUR DONNÉES SPHÉRIQUES RADIALES PRESCRITES SEULEMENT) :**
    pg/r² > .8854 ; pf/r² > .063 ; J > .659 ; K/r² > .229,
avec les deux dénominateurs de poussière, Sf', sqrt(1-z²) strictement positifs sur tout [0,.85], centre normalisé compris. **Le verrou radial d'existence/positivité de CES DONNÉES INITIALES est désormais clos sur le benchmark explicite.**

**INTERDICTION ABSOLUE D'EN DÉDUIRE ABSENCE FANTÔME BD.** Il ne s'agit ni de véritable évolution en temps 4D, ni de rang de Dirac, ni de fixation des lapses, ni de preuve de régularité tensorielle complète au centre. Gate2B reste OPEN ; JANUS-R non validé.

## PROVENANCE, COMMANDES, TESTS RÉELLEMENT EXÉCUTÉS

    cd /mnt/data/janus-step55
    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step55_global_barrier.py
    # 12 PASSED in 3.85 s, EFFECTIVEMENT EXECUTED.
    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step55_global_barrier

Les 3 nouveaux fichiers CODE/TEST et les 2 véritables sources historique Steps45/46 sont **OCTET POUR OCTET IDENTIQUES** aux blobs GitHub ci-dessus et ont été relus de GitHub. Tests : SHA originals fail-closed, intervalle exact négatif/positif/radical, centres, couverture 256 cellules, barrières strictes, bornes V, raffinement 512, cas large delta_U=.001 REFUSÉ car V non certifié, RHS physique ORIGINAL NON-SIMPLIFIÉ évalué indépendamment à r=.05,.35,.85 contient les bornes normalisées, garde faux positif Dirac. Il n'y a PAS de suite historique GitHub TOTALE, ni CI/workflows, ni Dirac temporel.

Résultat brut local /mnt/data/janus-step55/research/reports/step55-global-barrier-local.json SHA256 4f22328452d36ee252f966fbe6a1fa476e7aaba8daee43ec9d555b11619f0cfd ; PAS uploadé séparément. Résultats exacts sauvegardés dans rapport GitHub machine.

## NEXT STEP56 — PRIORITÉ MAINTENANT DIRAC TEMPOREL, PLUS LE RADIAL

1. Décomposer précisément l'action sphérique ORIGINAL non intégrée par parties pour calculer la **VRAIE PRÉSERVATION TEMPORELLE {C,Htot}**, six couples canoniques, deux lapses et déplacement relatif éliminé en respectant ses variations. Évaluer rang de Dirac et fixation des lapses pour la branche positive maintenant certifiée ; étudier J/K branches exceptionnelles/bords.
2. Vérifier indépendamment le crochet Poisson complet original non-IBP sur le profil exact radial construit avec barrières, sans confondre le résidu algébrique C=0 par construction avec une vraie vérification fonctionnelle.
3. Analyser la régularité sphérique CARTÉSIENNE/TENSORIELLE complète du centre et des évolutions 4D. Aucun résultat Step55 ne vaut absence de fantôme ni validité cosmologique.
4. Continuer à committer code/tests/rapport et PREPENDRE ce point de reprise après chaque avancée. Ne réactiver aucune GitHub Action.
5. ADMINISTRATIF : historique main/V2 déjà préservé dans branche active grâce au commit à double-parent 4f7a3a1, PR V2 #1 fermée non-fusionnée, mais Github a encore **3 branches NOMMÉES / défaut main**. Le connecteur ne donne pas changer défaut/supprimer des branches ; seul le propriétaire peut dans Github UI désigner active comme défaut puis supprimer V2/main. Ne jamais prétendre que l'unification des noms est faite.

**VERDICT : Step55 solution C=0 radiale du benchmark analytique régulier étendue jusque .85 avec deux poussières positives SUR LE CONTINUUM ; mais FULL DIRAC/TEMPORAL GATE2B OPEN et JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP54 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE POUR LES ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`. Ne PAS réactiver GitHub Actions/workflows. Ne PAS modifier le `main` historique ni `research/v2-flrw`. **GATE 2B OUVERT ; JANUS-R NON VALIDÉ.**

**À LIRE ABSOLUMENT EN PREMIER :** `research/STEP54_CONDITIONAL_CONTINUUM_TWODUST_INTERVAL_TUBE_AUDIT.md`.
**RAPPORT MACHINE / FRACTIONS EXACTES :** `research/reports/gate2b-step54-report.json`.
**CODE D'INTERVALLES :** `numerics/hr_step54_interval_tube.py`, Git blob `c2db1e6a4888194fc6f79aaee866efdad479dbfb`.
**9 TESTS :** `tests/test_hr_step54_interval_tube.py`, Git blob `d1dc7407ae1781aa742cab09cff0fc5a24bce66e`.
**FOURNISSEURS ORIGINAUX OCTET-IDENTIQUES GITHUB :** `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `numerics/hr_step46_exact_secondary_ode.py` blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`. Ces deux copies originales ont été effectivement vérifiées par le programme de Step54 en local.
**PRÉCÉDENT CENTRE :** `research/STEP53_EXACT_CENTER_U2_AND_SHOOTING_AUDIT.md` et `research/reports/gate2b-step53-report.json` (U0,U1,U2 exacts dans corps quadratique rationnel du benchmark).

## AVANCÉE STEP54 : POSITIVITÉ *CONTINUE* POUR UNE CLASSE CONDITIONNELLE DE PROFILS

Nouvelle preuve de **signes continus sur TOUT `r∈[0,.85]`** grâce à 256 cellules d'intervalles exacts en `s=r²∈[0,.7225]`, chacune couvrant tous les réels de sa cellule (AUCUN échantillonnage flottant pour les signes). Arithmétique par entiers à grille `1e-30`, arrondis sortants sur TOUS `+,-,*,/,sqrt`, `math.isqrt`, bornes RATIONNELLES certifiées pour U1/U2 des étapes52/53. Le centre r=0 est compris par normalisation analytique.

Pour le benchmark sphérique prescrit, posons `P(r)=pLf(r)`, `U=P/r²`, `V=P'/r`, `Ustar(s)=U0+U1*s+U2*s²` et `Vstar(s)=2U0+4U1*s+6U2*s²`.

**THÉORÈME DE SIGNES CONDITIONNEL :**
```text
SI POUR TOUT r in [0,.85], (par prolongement régulier en r=0) :
   |U(r²)-Ustar(r²)| <= 0.01
   |V(r²)-Vstar(r²)| <= 0.01
ALORS SUR TOUT CE CONTINUUM :
   pg/r² > 0.8854
   pf/r² > 0.063
   J > 0.659
   K/r² > 0.229
   both dust lapse coefficients >0.998
   Sf' >0.230
   sqrt(1-z²)>0.9999
```

Les fractions inférieures EXACTES sont sauvegardées in extenso dans rapport machine. Tube plus fin `delta=0.0001` permet `pf/r²>0.1111`. Source de poussière f vérifiée indépendamment en mpmath 75 chiffres sur quatre rayons contre l'expression symbolique ORIGINALE `hr_step46_exact_secondary_ode.py:p_f`.

**TRÈS IMPORTANT : NOUS N'AVONS PAS PROUVÉ QUE LA SOLUTION RADIALE EXACTE DE `pLf'=-C0/C1` APPARTIENT À CE TUBE.** Donc encore AUCUNE preuve d'existence globale exacte ou de positivité positive de la vraie trajectoire, malgré la preuve continue CONDITIONNELLE. Le prochain verrou est désormais **UNE INÉGALITÉ DE PROXIMITÉ SUR LA SOLUTION ET SA DÉRIVÉE NORMALISÉE**, pas un nouveau simple tableau d'échantillons.

## TESTS RÉELLEMENT PASSÉS ET REPRODUCTION

```bash
# Depuis checkout contenant scripts Github authentiques
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step54_interval_tube.py
# EFFECTIVEMENT EXÉCUTÉ EN LOCAL /mnt/data/janus-step54 : 9 PASSED en 2.03s.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -c 'import json;from numerics.hr_step54_interval_tube import certify;print(json.dumps(certify(256,"0.01"),indent=2))'
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step54_interval_tube
```

Les deux nouveaux blobs GitHub CODE/TEST = EXACTEMENT OCTETS EXÉCUTÉS. Deux vrais sources physiques historiques Step45/46 aussi byte-identical aux blobs GitHub. Ne pas affirmer une exécution complète des historiques Step33g→53 : tests ciblés 9, pas suite entière, pas CI. Une première version a échoué sur une garde de `profiles(s<0)` : bug CORRIGÉ puis les neuf tests RÉUSSIS.

JSON des 256 cellules locales : `/mnt/data/janus-step54/research/reports/gate2b-step54-tube_001.json`, SHA256 `708fad17c8e88520a0eb0122a49c60caaa22daeb09be543a0e513ef08dc2c378` ; `gate2b-step54-tube_0001.json`, SHA256 `c60f48da3569ec40e7e8a1c024af061eb35e2e8d5234f5dce130fc9b36b24212`. Les traces n'ont PAS été uploadées séparément mais leurs minima rationnels, le code régénérateur et toutes données essentielles figurent dans `research/reports/gate2b-step54-report.json`.

## NEXT STEP55 : DERNIER VERROU RADIAL FORMALISÉ

1. **CERTIFIER L'APPARTENANCE DE LA VRAIE SOLUTION AU TUBE** : à partir de `2s U_s=G(s,U)-2U`, `G(0,U)=3U0-U`, et des U1/U2 algébriques exacts, construire des bornes d'EDO a posteriori à intervalles (barrières haute/basse, contraction Picard ou Chebyshev). Prouver `|U-Ustar|<=0.01` ET `|V-Vstar|<=0.01` de s=0 à .7225. La preuve de signes Step54 s'appliquera alors AUTOMATIQUEMENT à la véritable solution. Chercher des seuils plus fins si utile.
2. Après cela relancer un oracle Poisson NON-IBP original pour la trajectoire enveloppée ; ne pas compter le résidu C par construction comme contrôle indépendant.
3. **TOUJOURS MAJEUR :** calculer le vrai crochet de PRÉSERVATION TEMPORELLE `{C,H_total}` de l'action originale avec SIX couples canoniques, bords, fixation des lapses, rang de Dirac, chartes J/K exceptionnelles. Rien de cela n'est établi par Step54.
4. Enfin éventuelle évolution cosmologique non homothétique on shell et stabilité même action ; manuscrit externe JHR de signe f-EH opposé reste voie d'audit distincte.
5. **ADMIN GITHUB** : les anciens commits main/V2 sont déjà ancêtres de la branche active par `4f7a3a1`, la PR brouillon historique #1 est fermée sans fusion. GitHub affiche encore TROIS branches avec défaut `main`. Le connecteur ne sait toujours PAS modifier le défaut ni supprimer refs. Propriétaire via Settings > Default branch choisir active, puis supprimer V2/main dans Branches. Ne pas prétendre suppression faite avant vérification.

**STATUT FINAL : PROPOSITION DE POSITIVITÉ RIGOUREUSE SUR TOUT LE CONTINUUM SOUS HYPOTHÈSE DE TUBE, HYPOTHÈSE NON ENCORE PROUVÉE POUR LA VRAIE EDO ; CONSERVATION TEMPORELLE DIRAC NON CALCULÉE ; GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP53 TERMINÉ — 2026-10-22

**LIRE CETTE SECTION EN PREMIER.** Branche scientifique ACTIVE UNIQUEMENT : `research/gate2b-nonhomothetic-transfer`. Ne PAS réactiver GitHub Actions/workflows ni modifier `main`/V2. **Gate 2B OUVERT, JANUS-R NON VALIDÉ.**

**AUDIT SCIENTIFIQUE :** `research/STEP53_EXACT_CENTER_U2_AND_SHOOTING_AUDIT.md`.
**RAPPORT MACHINE AVEC FRACTIONS EXACTES :** `research/reports/gate2b-step53-report.json`.
**CODE U2 :** `numerics/hr_step53_exact_center_u2.py`, Git blob `ee4515190e5b1733fb94641e6344e4ee96cdef6c`.
**CODE TIR DOP853 :** `numerics/hr_step53_outward_compare.py`, Git blob `7a445614167a4cb7304aec7d19f38295d32a8890`.
**TESTS :** `tests/test_hr_step53_exact_center_u2.py`, Git blob `4e1848157c6ec95c7a0d6e73c0921573605f7117`.
**BASE :** Step52 `research/STEP52_EXACT_CENTER_U1_RATIONAL_TAYLOR_AUDIT.md`, vraies équations physiques de Step45/46.

## NOUVELLE AVANCÉE ANALYTIQUE DÉMONTRÉE : SECOND COEFFICIENT CENTRAL U2

Pour la même famille de données canoniques sphériques primaires-réduites et les paramètres du benchmark traités comme rationnels décimaux EXACTS,

```text
pLf(r)=r² [U0+U1 r²+U2 r⁴+O(r⁶)],
s=r², G(s,U)=pLf'(sqrt(s),pLf=sU)/sqrt(s), G(0,U)=3U0-U
5U1 = partial_s G(0,U0)
7U2 = (1/2)partial_ss G(0,U0) + partial_sU G(0,U0)*U1
     + (1/2)partial_UU G(0,U0)*U1².
U2=A2+B2*sqrt(H²), H²,A2,B2 EXACTEMENT RATIONNELS,
U2≈-0.000010073853486743828175736890952863935933883641943763773429699704274
```

**EXACT U2 EST CERTIFIÉ NÉGATIF** dans le modèle rationnel : `rational_interval(...,digits=100)` sur la racine positive `sqrt(H²)` utilise `isqrt` et des fractions exactes, donne largeur < `1e-100`. Le rapport machine conserve IN EXTENSO les trois fractions A2, B2, H² ; aucune perte de précision dans le dépôt.

Le programme évalue deux fois le SECOND MEMBRE de `C=0` construit depuis les VRAIES FORMULES sphériques Step45/46 : au premier passage `pLf=r²U0` il retrouve exactement les fractions de U1 du Step52 ; au second `pLf=r²(U0+U1r²)`, le terme r³ est EXACTEMENT `4U1`, r⁵ est `7U2`. Jets de Laurent quadratiques `Q(sqrt(H²))` avec inverses/racines par récurrences EXACTES et propagation conservative des premières puissances inconnues. Les ordres tronqués **12,14,18,22 donnent A2 et B2 IDENTIQUES bit-à-bit**, et les premiers termes inconnus ne peuvent entrer qu'en r^7,r^9,r^13,r^17 > r⁵. Ce certificat est LOCAL, il n'établit aucune existence globale.

## CONTRÔLE NUMÉRIQUE DU GAIN SUR LE TIR DEPUIS LE CENTRE

Même équation physique `pLf'=-C0/C1` évaluée sur les données de fond courbes/DEUX poussières/non-comobiles du benchmark ; solveur `scipy solve_ivp DOP853`, `rtol=2e-12`, `atol=1e-18`, pas max `.012`. Référence interne depuis `eps=.001` avec les trois coefficients : `pLf(.85)=-.0033864293564879076`.

```text
eps     |fin avec U0+U1 - référence|    |fin avec U0+U1+U2 - référence|
.05          9.270795936489051e-15             4.336808689942018e-19
.025         8.109832250191573e-17             3.0357660829594124e-18
.0125        1.0842021724855044e-17            8.239936510889834e-18
.00625       2.168404344971009e-18            9.974659986866641e-18
```

**Ces écarts sont des COMPARAISONS à une référence NUMÉRIQUE, PAS bornes d'erreur certifiées.** Les chiffres se saturent au plancher binaire pour les petits rayons. Les poussières positives sur tout le CONTINUUM et une solution exacte prolongée jusqu'à .85 restent NON démontrées. Le C calculé de l'EDO est petit PAR CONSTRUCTION, distinct des contrôles du Poisson original Step48.

## TESTS EFFECTIVEMENT EXÉCUTÉS ET PROVENANCE

```bash
cd /mnt/data/janus-step53
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step53_exact_center_u2.py
# 9 PASSED IN 12.62s.

for j in 12 14 18 22; do
  JANUS_JET_ORDER=$j OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step53_exact_center_u2
done
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step53_outward_compare
```

**Les TROIS nouveaux fichiers sont BYTE-IDENTICAL aux fichiers locaux qui ont été réellement exécutés**, blobs GitSHA ci-dessus. Les sources historiques Step45/46 du PETIT ENVIRONNEMENT LOCAL ont été reconstituées fidèlement par leurs équations, **MAIS ne sont PAS octet pour octet les fichiers originaux GitHub dans ce tour**. Le dépôt GitHub importe les véritables sources historiques et la réexécution intégrale U2 avec les octets originaux reste **PENDING**. Il serait FAUX de compter cette session comme full original-provider regression. La suite complète et CI non exécutées ; Actions désactivées.

JSON détaillés générés localement, NON uploadés séparément : `research/reports/step53-u2-raw.json` SHA256 `44244e855f6f0cd8b7fdbe53c145fdab6e9c7aa872e61a6dd72232177ffd445c`, `research/reports/step53-shoot-raw.json` SHA256 `d7d7b1c68e28b36859322b7efc19ddbce01b5279717829d729013fa368e6b573`. A2/B2/H² et tous les chiffres principaux sont dans rapport GitHub.

## STEP54 — VERROUS À TRAITER APRÈS INTERRUPTION

1. **REPRODUCTIBILITÉ** : constituer un checkout original entier Step33g→53 sans adaptateurs et re-exécuter le module U2 + tests ainsi que les deux contrôles historiques Step48 complets.
2. **RIGUEUR GLOBALE** : à partir du vrai U0,U1,U2, construire une continuation EDO VALIDÉE par intervalles depuis r=0 jusqu'à r=.85, avec preuve de `pg/r²,pf/r²,J,K/r²>0` sur TOUT L'INTERVALLE du nouveau profil et bords sphériques réguliers. Pas seulement des échantillons ni des écarts entre solveurs.
3. **THÉORIE DYNAMIQUE** : dériver/calculer `{C,H_total}` temporel avec TOUS les 6 couples canoniques, régler fixation lapses/rapport lapses, matrice de Dirac, J/K exceptionnels et bords. C'est le verrou physique fondamental ; Ward et EDO spatiale seuls n'éliminent PAS un fantôme.
4. Ensuite seulement évolution non homothétique on-shell, stabilité même action De Felice/Aoki et confrontations empiriques.
5. **ADMIN GITHUB** : histoire `main`+V2 déjà préservée dans l'ascendance active par `4f7a3a1`, ancienne PR#1 fermée sans fusion. Mais GitHub affiche encore TROIS refs ; défaut `main`. Aucune fonction disponible pour supprimer ces refs/changer défaut ; propriétaire doit via UI changer défaut vers active, PUIS supprimer V2 et main. Ne pas prétendre 1 branche avant vérification réelle.

**VERDICT : U2 EXACT ALGÉBRIQUE CERTIFIÉ LOCAL SUR BENCHMARK RATIONNEL, TIR AMÉLIORÉ ; GATE_2B OPEN, JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP52 TERMINÉ — 2026-10-22

**BRANCHE SCIENTIFIQUE AUTORISÉE UNIQUEMENT :** `research/gate2b-nonhomothetic-transfer`. Ne pas écrire dans `main`, `research/v2-flrw`, ne pas réactiver Actions/workflows. **NE PAS AFFIRMER JANUS-R VALIDÉ**.

**LIRE D'ABORD :** `research/STEP52_EXACT_CENTER_U1_RATIONAL_TAYLOR_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step52-report.json` contient les fractions EXACTES A,B,H² et les bornes.
**NOUVEAU CODE :** `numerics/hr_step52_exact_center_taylor.py`, Git blob `b7da7e5272e08819fc89053fdf15852fcf4cc536`.
**NOUVEAUX TESTS :** `tests/test_hr_step52_exact_center_taylor.py`, Git blob `cf9416641583de47ab0d60f4527bca7ce60d2806`.
**DÉPENDANCES PINNÉES EXACTES :** `numerics/hr_step45_exact_physical_ward.py` SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `numerics/hr_step46_exact_secondary_ode.py` SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
**PRÉCÉDENT :** `research/STEP51_AUTHENTIC_CENTER_U1_AND_BRANCH_ADMIN_AUDIT.md`.

## AVANCÉE PRINCIPALE : COEFFICIENT U1 EXACTEMENT ALGÉBRIQUE ET BORNÉ

Au lieu de l'estimation non rigoureuse de Step51, calcul par jets de LAURENT avec coefficients `A+B*sqrt(H²)` dans le corps quadratique rationnel de la calibration sphérique Step41, à partir du SECOND MEMBRE PHYSIQUE de l'EDO `pLf'=-C0/C1` dérivée du vrai noyau de Poisson sphérique à six couples canoniques.

```text
pLf(r) = r² (U0 + U1*r² + ...)
U0 = Mf²*b*(Pg/(Mg²*a)-2*z1)
G(s,U) = pLf'(sqrt(s), pLf=s*U)/sqrt(s) ; G(0,U)=3U0-U
U1 = (partial_s G)(0,U0)/5
U1 = A + B*sqrt(H²)   ;   A,B,H² EXACTEMENT RATIONNELS
0.0007897451667202464909325108904961683602148118201690
   < U1 <
0.0007897451667202464909325108904961683602148118201692
```

Le programme calcule les deux fractions A,B exactement avec `Fraction` (et H²). Radicaux et dénominateurs développés en jets formels avec propagation conservatrice de la première puissance inconnue. Les TRONCATURES 14,20,26 donnent EXACTEMENT les mêmes A,B ; les termes omis ne peuvent atteindre les puissances r^0..r³ (leurs ordres d'inconnu : r^9,r^15,r^21). La racine positive sqrt(H²) est encadrée par `isqrt` sur grille 10^-90, puis A+B sqrt(H²) par EXACTES fractions. Largeur réelle de l'encadrement ≈8.30667e-96, donc <1e-80. AUCUNE extrapolation numérique utilisée pour la preuve de cette valeur centrale.

**Limite** : le certificat vaut pour les paramètres de l'étalonnage imprimé traités comme fractions décimales exactes, et pour l'action sphérique primaire-réduite. Pas une borne sur les arrondis binary64 du logiciel historique, ni une solution radiale complète.

## TESTS ET PROVENANCE — RÉELLEMENT EXÉCUTÉS

```bash
cd /mnt/data/janus-step52
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step52_exact_center_taylor.py
# ACTUELLEMENT EXÉCUTÉ : 8 PASSED in 11.01s

JANUS_JET_ORDER=14 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step52_exact_center_taylor
JANUS_JET_ORDER=20 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step52_exact_center_taylor
JANUS_JET_ORDER=26 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step52_exact_center_taylor
```

Les deux nouveaux fichiers code/tests ont des Git blobs EXACTEMENT IDENTIQUES aux octets locaux exécutés ; les deux fournisseurs historiques Step45/46 sont eux aussi bit-identiques GitHub. Contrôles : SHA fail-closed, corps quadratique, coefficients centraux/termes absents, reste jet >r³, même A,B à 3 ordres, bornes fractions strictes et oracle haute précision Step51 indépendant. C'est une suite ciblée, pas le dépôt entier.

Le JSON brut local réellement généré `/mnt/data/janus-step52/research/reports/step52-u1-jet-20.json` a SHA256 `069191a6e92c7474677c3b5a004de0affba94c1ede63f1debfe253d09d3fca6f` mais n'a PAS été uploadé séparément ; les fractions exactes A,B,H² et les bornes sont enregistrées dans le rapport GitHub `research/reports/gate2b-step52-report.json`.

## BRANCHES — RÉDUCTION NOMINALE ENCORE NON RÉALISÉE

Commits des 3 branches déjà préservés sans changement de tree dans l'ascendance active grâce au commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7`. PR brouillon historique #1 **FERMÉE SANS FUSION**. Mais GitHub a TOUJOURS `default=main`, trois refs `main`, `research/v2-flrw`, `research/gate2b-nonhomothetic-transfer`. Le connecteur n'offre pas modifier branche par défaut ni supprimer des refs. Propriétaire : changer Default branch à `research/gate2b-nonhomothetic-transfer` dans Settings, PUIS supprimer V2 et main dans Branches, puis vérifier liste réelle. Ne pas mentir sur cette opération.

## NEXT STEP53 : PRIORITÉ SCIENTIFIQUE

1. Utiliser CE VRAI U1 (exact) dans le tir régulier depuis r≈0 ; développer éventuellement U2 avec jets à reste contrôlé. Évaluer les différences de raccordement sans les présenter comme borne d'erreur globale.
2. Réunir en un SEUL checkout tous les imports upstream historiques Step33g/37/45/46/47/48 strictement byte-identiques ; relancer sans filtre la suite Step48 puis tests Step49/51/52. Deux imports antérieurs encore adaptateurs sont à remplacer.
3. Construire un vrai certificat continu de prolongement régulier U(s) sur [0,.85], densités poussières `pg/r²,pf/r²>0`, chartes J,K/r², et bornes de résidu/EDO.
4. Calculer la VRAIE préservation temporelle `{C,Htot}` des six couples canoniques avec bords, rang de Dirac et fixation des lapses. Ne pas déduire ghost-free du calcul du coefficient central.
5. Veiller à tenir `00_CURRENT_RESTART.md` et GitHub à jour à chaque interruption.

**VERDICT : U1 ANALYTIQUE EXACT POUR BENCHMARK RATIONNEL = CERTIFIÉ ; SOLUTION RADIALE GLOBALE ET DIRAC TEMPOREL NON ÉTABLIS ; GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

---

# CORRECTION D'AUTORISATIONS GITHUB — VÉRIFIÉ 2026-10-22

**Fait établi :** le compte GitHub authentifié `alexandrebarault-arch` possède `permission=admin` sur `alexandrebarault-arch/Janus` (outil GitHub `get_repo_collaborator_permission`). Les affirmations antérieures laissant entendre que l'UTILISATEUR n'avait pas les droits sont ERRONÉES. Il possède bien l'administration du dépôt.

**Limite DISTINCTE :** la connexion disponible dans CETTE conversation est une installation GitHub App aux permissions restreintes et aux fonctions explicitement limitées : elle peut créer/mettre à jour fichiers, commits et pointer une ref vers un commit, **mais NE FOURNIT NI modification de `default_branch` NI `DELETE git/refs/heads/...`**. La fonction de lecture générique GitHub `fetch` n'autorise que `GET` et sa documentation indique que les installations d'app n'ont pas l'accès `administration`. Le terminal local possède `git` mais ne dispose ni de `gh`, ni de credential GitHub configuré, ni de résolution DNS valide vers `api.github.com`. Ne pas confondre cette impossibilité *du connecteur* avec un manque de droits du compte.

**État distant vérifié :** branche par défaut = `main`; 3 refs toujours présentes (`main`, `research/gate2b-nonhomothetic-transfer`, `research/v2-flrw`). Les anciennes pointes sont préservées dans l'ascendance active via commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7`, sans changement d'arbre scientifique. PR historique #1 fermée non fusionnée. **Suppression NON FAITE** et aucune promesse d'avoir ramené effectivement le dépôt à une branche.

**Action admin restante quand un vrai client GitHub avec autorisation d'administration est disponible :** PATCH default_branch vers `research/gate2b-nonhomothetic-transfer`, puis DELETE ref `heads/research/v2-flrw` et DELETE ref `heads/main`; vérifier qu'une seule ref reste. Ne pas tenter de simuler la suppression en effaçant les fichiers ou en forçant `update_ref` vers un autre SHA. Via interface GitHub : Settings > General > Default branch, puis page Branches pour suppression.

**Reprise scientifique :** inchangée, étape 52 selon le bloc d'étape 51 ci-dessous. Gate2B OPEN, JANUS-R NOT VALIDATED.

---

# JANUS — REPRISE STEP51 : ADDENDUM SOURCE-AUTHENTIC (2026-10-22)

**REPRENDRE ICI AVANT LE TEXTE PRÉCÉDENT.** Dernier audit : `research/STEP51_AUTHENTIC_CENTER_U1_AND_BRANCH_ADMIN_AUDIT.md` section 5. Rapport : `research/reports/gate2b-step51-report.json`.

## NOUVELLE AVANCÉE DEPUIS LE PREMIER CHECKPOINT STEP51

La chaîne Step48 à CINQ providers historiques strictement byte-identiques est effectivement reconstituée et vérifiée `check_git=True` : `hr_step37_original_nonibp_oracle.py` `005449ade6`, `hr_step45_exact_physical_ward.py` `66aa43841`, `hr_step45_secondary_point_certificate.py` `6ab94dacb`, `hr_step46_exact_secondary_ode.py` `bac025c28`, `hr_step47_interior_ivp.py` `c558a827`. Le programme Step48 original `hr_step48_original_ivp_oracle.py` `dc5101d4` est LUI AUSSI identique octet pour octet. L'ancienne obstruction de vérification des 5 hash est donc levée.

Crochet Poisson ORIGINAL NON-IBP à 12 champs / 6 couples sur nouvel IVP et DEUX lapses : `N=161 A=-5.909466451194632e-7 B=-9.466192080859973e-7` ; `N=321 A=-1.4770852485167414e-7 B=-2.3664938826562995e-7` ; `N=641 A=-3.6925374684076886e-8 B=-5.916200850443823e-8`. Ces crochets FINIS ne sont PAS nuls exactement, mais diminuent comme ~h². Cette session utilise encore 2 **adaptateurs d'IMPORT SEULEMENT** dans les sources upstream `hr_curved_moving_dust_primary.py` (constantes/R) et `hr_curved_primary_mixed_kernel.py` (ordre Q) ; **pas de régression totale intégralement authentifiée**. Les anciens tests du fichier Step48 complet ne sont pas relancés, mais leurs deux fonctionnalités en attente ont été exercées par des tests NEW.

**TESTS RÉELLEMENT EXÉCUTÉS :**
```bash
cd /mnt/data/janus-step51
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step51_highprecision_center.py tests/test_hr_step51_original_chain.py
# 13 PASSED, 14.54s (7 Step51 centre haute précision + 6 véritable chaîne Step48)
```
NOUVEAU TEST GITHUB : `tests/test_hr_step51_original_chain.py` Git blob `2687e7279ddda3c1b0bc8ea2ba340cab0ce3499d`, identique à l'exécuté.

## BRANCHES — DEMANDE UTILISATEUR ENCORE PARTIELLEMENT ADMINISTRATIVE

Préservation des commits des 3 branches dans une SEULE ascendance active : commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` arbre inchangé. PR historique #1 FERMÉE et NON fusionnée. **MAIS default=main, 3 refs demeurent** : `main`, `research/v2-flrw`, `research/gate2b-nonhomothetic-transfer`. Connector GitHub ne fournit pas la modification de branche par défaut ni la suppression de refs. Pour terminer : utilisateur via GitHub Settings > General > Default branch sélectionner `research/gate2b-nonhomothetic-transfer`, puis Branches supprimer `research/v2-flrw` et `main`. Vérifier réel affichage une seule branche. Ne PAS prétendre suppression faite.

## NEXT STEP52

1. Reconstituer les DEUX sources upstream `hr_curved_moving_dust_primary.py` et `hr_curved_primary_mixed_kernel.py` exactement ; relancer la suite complète Step48 originelle sans filtre et tests Step49/51.
2. U1 actuellement NUMÉRIQUE 120 chiffres `0.00078974516672024649093251089049616836021481...`, original Step45/46 strict byte-identical ; DERIVER / CERTIFIER U1 algébriquement par jets Taylor et intervalle.
3. Certifier l'EDO régulière du centre jusque r=.85 et densités poussières positives EN CONTINU ; les échantillons restent insuffisants.
4. VRAIE PRÉSERVATION TEMPORELLE de C, rang de Dirac, fixation des lapses et chartes exceptions J/K sont TOUJOURS NON ÉTABLIS. **Gate2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP51 TERMINÉ — 2026-10-22

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE AUX ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`. **NE PAS RÉACTIVER GitHub Actions/workflows.** Ancien `main` et V2 ne doivent plus recevoir de commits scientifiques.

**DOCUMENT PRINCIPAL :** `research/STEP51_AUTHENTIC_CENTER_U1_AND_BRANCH_ADMIN_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step51-report.json`.
**NOUVEAU CALCULATEUR :** `numerics/hr_step51_highprecision_center_coefficient.py` SHA Git blob `97fe8f78a5daa91a8c74b14382470857c9ce29e2`.
**NOUVEAUX TESTS :** `tests/test_hr_step51_highprecision_center.py` SHA `da85a6e4da8c7202da6d1d5e81fd1aeb8a964e3e`.
**SOURCE HISTORIQUE STEP45 :** `numerics/hr_step45_exact_physical_ward.py` SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
**SOURCE HISTORIQUE STEP46 :** `numerics/hr_step46_exact_secondary_ode.py` SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
**BRANCHES/PR :** `research/BRANCH_CONSOLIDATION_2026-10-22.md`.

## LE POINT DEMANDÉ : UNE SEULE BRANCHE — HISTORIQUES PRÉSERVÉS, DEUX RÉFÉRENCES ENCORE À SUPPRIMER

- Avant : `main` HEAD `aead63f4`, `research/v2-flrw` HEAD `dfa497cc` avec 203 commits divergents, actif `research/gate2b-nonhomothetic-transfer`. Le commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` a fusionné leur ASCENDANCE (deux parents) en laissant l'arbre de fichiers actifs **STRICTEMENT IDENTIQUE**. Vérification GitHub : `behind=0` pour les deux anciennes pointes par rapport à l'actif. AUCUN commit perdu, AUCUN fichier ancien V2 écrasant les nouveaux.
- La **pull request brouillon historique #1 est FERMÉE sans fusion** via le connecteur, état GitHub `closed/merged=false`.
- **TOUJOURS 3 BRANCHES NOMMÉES SUR GITHUB** : défaut actuel `main`, plus `research/gate2b-nonhomothetic-transfer`, plus `research/v2-flrw`. Ne PAS déclarer avoir réellement réduit à une branche.
- **L'OUTIL GITHUB DISPONIBLE NE PERMET PAS** changer `default_branch` ou supprimer une ref. **OPÉRATION RESTANTE POUR LE PROPRIÉTAIRE VIA UI** : dans repo Settings > General > Default branch, choisir `research/gate2b-nonhomothetic-transfer` ; puis dans Branches supprimer `research/v2-flrw`, ensuite `main`, APRES avoir changé la branche par défaut ; contrôler que liste = 1. Ancienne PR n'a plus besoin d'être traitée.
- Ne pas tenter une destruction artificielle du contenu des anciennes branches : cela ne supprimerait pas les refs et risquerait de corrompre l'historique.

## PROGRÈS SCIENTIFIQUE STEP51 — VRAIES SOURCES GITHUB, U1 PLUS PRÉCIS

Cette session a reconstitué en local les VRAIS fichiers historiques STEP45 et STEP46 octet par octet (empreintes ci-dessus, confirmées par `git hash-object`). Le nouveau programme refuse une modification de leur SHA. Dans le modèle sphérique Hamiltonien positif-EH HR à DEUX poussières et calibration décimale rationnelle, avec les g primaires reconstruites et `pLf=r² U0`, il calcule le second membre exact de la contrainte secondaire `pLf'=-C0/C1` à précision `mpmath` **100–120 chiffres**, pour extraire numériquement

```text
s = r², pLf=r² U(s)
G(s,U0) = pLf'(sqrt(s), pLf=s U0)/sqrt(s)
U1 = partial_s G(0,U0)/5   [FORMULE EXACTE si G analytique dans la charte]
U1 ≈ 0.0007897451667202464909325108904961683602148118202349246798
U1 de Step49 en double : 0.0007897451669079507
écart ancien - nouveau ≈ +1.877042090674891095e-13.
```

Quatre paires de rayons décroissants `(10^-7,10^-8)` jusqu'à `(10^-10,10^-11)` et extrapolation principale `O(r²)` donnent les mêmes 35 premiers chiffres environ ; stabilité vérifiée à 80 et 120 chiffres. **N'EST PAS UN ENCADREMENT RIGOUREUX DE U1**, car le reste d'extrapolation en rayon n'est pas mathématiquement borné.

## TESTS RÉELLEMENT EXÉCUTÉS — PAS ENTIÈRE SUITE

```bash
cd /mnt/data/janus-step51
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step51_highprecision_center.py
# ACTUELLEMENT : 7 PASSED en 1.85 s ; fichiers NEW et vrais providers45/46 byte-exacts.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step51_highprecision_center_coefficient
```

Deux nouveaux blobs GitHub vérifiés égal aux OCTETS exécutés; sources Step45/46 strictement égales à GitHub. Les historiques complémentaires `hr_step45_secondary_point_certificate.py`, Step47/Step48 sont toujours à reconstituer ensemble pour débloquer les DEUX tests Step48 authentiques encore en attente. Aucun contrôle sur la vraie évolution Dirac, aucune borne global ODE, aucun CI/workflow.

## NEXT — STEP52

1. Dériver **EXACTEMENT** `U1=∂_s G(0,U0)/5` comme expression algébrique, ou une borne rationnelle certifiée par jets/Taylor, sans extrapolation non contrôlée.
2. Reconstituer la CHAÎNE AUTHENTIQUE COMPLÈTE Step45/46/47/48 et relancer les 2 tests Step48 longtemps désélectionnés, en plus des nouveaux tests ; ne pas appeler ce résultat complet avant exécution.
3. Construire une continuation par EDO à intervalles ou barrière analytique jusqu'à `.85`, certifier en continu `pg/r²>0,pf/r²>0,J>0,K/r²>0` pour les nouvelles données initiales régulières au centre.
4. Ensuite le VERROU MAJEUR : calculer `{C,Htot}` temps avec TOUS six couples canoniques et bords, rang Dirac et fixation des lapses. Ni Ward ni intégration radiale ne démontrent absence du fantôme BD.
5. Quand le propriétaire a exécuté changement défaut et deux suppressions des refs, vérifier sur GitHub qu'il ne reste vraiment qu'UNE branche ; ne pas modifier `main` tant qu'elle existe.

**STATUT : HISTORIQUES GIT CONSOLIDÉS ET PR BROUILLON FERMÉE ; MAIS 3 REFS GITHUB ENCORE EXISTANTES. STEP51 U1 120 CHIFFRES TRÈS STABLE NUMÉRIQUEMENT AVEC SOURCES 45/46 ORIGINALES ; GATE2B OPEN, JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP50 TERMINÉ — 2026-10-22

**BRANCHE SCIENTIFIQUE ACTIVE UNIQUE POUR TOUTES LES ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`.

**ATTENTION : LE DÉPÔT GITHUB A ENCORE TROIS NOMS DE BRANCHES !** Le travail de préservation est effectif, mais leur suppression et le changement de défaut doivent se faire dans l'interface GitHub (le connecteur ne possède pas les actions d'administration). NE PAS AFFIRMER QU'IL NE RESTE QU'UNE BRANCHE AVANT LE CONTRÔLE DISTANT.

**LIRE EN PREMIER :** `research/STEP50_BRANCH_CONSOLIDATION_AND_SOLVER_CROSSCHECK_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step50-report.json`.
**CONSOLIDATION GIT DÉTAILLÉE :** `research/BRANCH_CONSOLIDATION_2026-10-22.md`.
**NOUVEAU PROGRAMME :** `numerics/hr_step50_solver_crosscheck.py`, Git blob `608222f9071c217d477951c8ed1ae81f5507b095`.
**NOUVEAUX TESTS :** `tests/test_hr_step50_solver_crosscheck.py`, Git blob `c96c44c24a5b2a9293d127a77e99dadd6c629125`.
**ANCIEN CONTRÔLE CENTRE :** `research/STEP49_ANALYTIC_CENTER_AND_OUTWARD_SHOOTING_AUDIT.md`.

## CONSOLIDATION SANS PERTE D'HISTORIQUE EFFECTIVEMENT FAITE

- Ancien `main` SHA `aead63f4098f0d15a849e579105af034b6317b30` était déjà ancêtre de la branche active.
- Ancien `research/v2-flrw` SHA `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` avait 203 commits divergents.
- Commit de préservation `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` à DEUX PARENTS, ajouté sur la branche active, avec Git TREE EXACTEMENT IDENTIQUE `e5da02813be6b378398520d9d129209fc5caf5c2` : aucun fichier ancien V2 importé/écrasé.
- Contrôle GitHub après opération : `behind=0` pour `main` ET `research/v2-flrw` par rapport à la branche active. Leurs commits sont préservés dans l'ascendance ; PR historique brouillon [#1](https://github.com/alexandrebarault-arch/Janus/pull/1) **FERMÉE le 22 octobre sans fusion** via le connecteur ; ancien code V2 NON fusionné.
- **PENDING INTERVENTION UI GITHUB** : (1) changer branche par défaut `main` → `research/gate2b-nonhomothetic-transfer`, (2) PR brouillon #1 déjà FERMÉE sans fusion, (3) supprimer refs `research/v2-flrw` et `main`, (4) vérifier que GitHub affiche réellement **une seule branche**. Changer le défaut AVANT de supprimer `main`. NE PAS réactiver Actions/workflows.

## AVANCÉE SCIENTIFIQUE STEP50 — TROIS SOLVEURS INDÉPENDANTS, PAS TROIS THÉORIES

Les programmes RK45, DOP853 et Radau intègrent depuis `eps=.00625` vers `r=.85` la même équation d'EDO analytique `pLf'=-C0/C1` déduite des primaires f aux étapes 45/46, avec l'initialisation régulière de Step49 `pLf(eps)=U0 eps² + U1_est eps⁴`. `U1_est≈0.0007897451669079507` est NUMÉRIQUE NON CERTIFIÉ. Pour `rtol=2e-11`, `atol=1e-17`, pas max `.012` et **2049 rayons** sur `[.01,.85]` :

```text
méthode    RHS       pLf(.85)                 min_pf/r² (2049 échantillons)
RK45       824       -0.003386429356487892   0.11186483299522024
DOP853     1376      -0.0033864293564879015  0.11186483299522028
Radau      2647      -0.0033864293564881253  0.11186483299522033
```

Max écart pLf sur la TRAJECTOIRE ÉCHANTILLONNÉE par rapport RK45 : DOP853 `4.020178287489351e-14`, Radau `4.0734668242670136e-14`. Les deux poussières positives SUR CES POINTS ; g normalisée min `0.8856008128827202`. `C` par substitution algébrique max `3.8e-14` est faible **PAR CONSTRUCTION**, pas un contrôle indépendant de l'action originale non intégrée (déjà mené séparément au Step48).

**AUCUNE borne d'erreur CONTINUE/INTERVALLE**, ni positivité continue sur [0,.85], ni préservation temporelle du Dirac n'ont été établies en Step50.

## TESTS ET PROVENANCE HONNÊTES

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step49_regular_center_shoot.py tests/test_hr_step49_analytic_center.py tests/test_hr_step50_solver_crosscheck.py
# EFFECTIVEMENT EXÉCUTÉ : 29 PASSED en 6.09 s ; 21 anciens Step49 et 8 nouveaux Step50.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step50_solver_crosscheck
```

Les DEUX nouveaux fichiers source/test sont Git blob BYTE-IDENTICAL aux fichiers réellement testés ; les sources antérieures Step45/46/47 dans l'environnement local `/mnt/data/janus-step50` sont encore des adaptateurs mathématiques NON OCTET-IDENTIQUES à GitHub. Les deux tests originaux Step48 nécessitant 5 providers authentiques n'ont donc PAS été vérifiés ; pas de suite entière ni de CI. Le JSON local complet a SHA256 `a0c76ddc29560df063ba3b83e63e57a3ef4d9becc912d4f37775cc08ed039a45` et les valeurs essentielles sont enregistrées dans `research/reports/gate2b-step50-report.json`.

## PRIORITÉS STEP51 POUR REPRISE APRÈS INTERRUPTION

1. **OPÉRATION GITHUB ADMINISTRATIVE restante** — changer le défaut et supprimer les 2 refs via UI, sans perte d'historique grâce au commit `4f7a3a1`. Ne jamais déclarer suppression réalisée sans preuve depuis GitHub.
2. **REGRESSION HISTORIQUE AUTHENTIQUE** — reconstituer les véritables fichiers Step45/46/47 byte-identiques et lancer les deux tests Step48 désélectionnés puis les tests Step49/50 sans adapters.
3. **CERTIFICAT MATHÉMATIQUE GLOBAL** — dériver U1 exact ou rationnellement borné, puis prouver continuité/existence/signes des deux poussières pour la SOLUTION NON POLYNOMIALE RÉGULIÈRE jusqu'à .85 avec une EDO validée par intervalles, en conservant J>0,K/r²>0.
4. **DIRAC TEMPOREL** — calculer réellement `{C,Htot}` pour les SIX couples canoniques, rang, fixation des lapses, bords, chartes exceptionnelles. Ward exact et ODE radiale ne prouvent PAS l'absence BD. Vraie cosmologie on-shell et De Felice/Aoki après seulement.

**VERDICT : historique scientifique désormais préservé dans une seule ascendance active, MAIS TROIS REFS GITHUB ENCORE VISIBLES ; contrôle numérique Step50 PASS ; GLOBAL/Dirac Gate 2B OPEN ; JANUS-R NON VALIDÉ.**

---

# JANUS — REPRISE PRIORITAIRE : STEP49 TERMINÉ — 2026-10-22

**BRANCHE AUTORISÉE EXCLUSIVE :** `research/gate2b-nonhomothetic-transfer`. NE modifier NI `main` NI `research/v2-flrw`. NE PAS réactiver GitHub Actions/workflows.

**LIRE D'ABORD :** `research/STEP49_ANALYTIC_CENTER_AND_OUTWARD_SHOOTING_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step49-report.json`.
**CODE CENTRE ANALYTIQUE :** `numerics/hr_step49_analytic_center.py`, Git blob `d570948912885d45a625fa2db31c6a5435b6a654`.
**TESTS CENTRE ANALYTIQUE :** `tests/test_hr_step49_analytic_center.py`, blob `8f14de90a296f53f372dde4a29fc63149473644b`.
**CODE TIR FROBENIUS :** `numerics/hr_step49_regular_center_shoot.py`, blob `ef1316505f03ee030b29b91e0edfaa5e480132cc`.
**TESTS TIR :** `tests/test_hr_step49_regular_center_shoot.py`, blob `2db400a4b41541983dd49a5fab2d4d0777789aa4`.
**PRÉCÉDENT STEP48 :** `research/STEP48_ORIGINAL_POISSON_AND_CENTER_FROBENIUS_AUDIT.md`.

## NOUVEAU THÉORÈME CENTRE LOCAL, CONDITIONNEL AUX DONNÉES ANALYTIQUES

À partir du VRAI (C=K00-(K01)') du Hamiltonien sphérique ADM-HR positif et DEUX poussières canoniques (Step45), après élimination des deux primaires f (Step46), posons `s=r²`, `pLf(r)=r² U(s)`, `W=pLf'/r`. Une substitution PARITAIRE générale dans l'expression physique donne EXACTEMENT `C/r²` PAIR et analytique en r au centre dans la charte régulière avec autres fonctions canoniques analytiques paires en s, racines et dénominateurs non nuls.

La dérivée implicite CENTRALE exacte est `d(C/r²)/dW = -m² Mg² (a² beta1+2ab beta2+b² beta3)/(2 Mf² b)`, non nulle si `Astar>0`. Ainsi `W=G(s,U)` analytique locale, avec `G(0,U)=3U0-U`, où

```text
U0=Mf²*b*(Pg/(Mg²*a)-2*z1) ;
2*s*U_s=G(s,U)-2U ;
s*U_s=-(3/2)*(U-U0) + (s/2)*R(s,U) ; R analytique.
```

Une équation intégrale de Volterra contractive pour petit s assure l'UNIQUE solution ANALYTIQUE LOCALE régulière dans cette famille de DONNÉES INITIALES prescrites analytiques ; le mode `U-U0=C*s^(-3/2)`, donc `pLf=C/r`, est écarté. Ce résultat n'est PAS une preuve de l'existence globale sur `r∈[0,.85]` ni de la préservation temporelle par les lapses.

Une vérification RATIONNELLE EXACTE indépendante des formules de poussières au centre avec racine `H=sqrt(H²)` encadrée par `isqrt` donne `pg/r²|0=1107/1250=0.8856` et `pf/r²|0>0.1242` (approx `0.1242700002620524`), `J(y)>0.65`. Les sources restent strictement positives dans un CERTAIN voisinage du centre, par analyticity/continuité. Taille de ce voisinage NON bornée ici.

## INTÉGRATIONS VERS L'EXTÉRIEUR ET DONNÉES EFFECTIVEMENT TESTÉES

`U(s)=U0+U1*s+...`, `U1=(∂_s G)(0,U0)/5` exactement en formalisme; `U1≈0.0007897451669079507` ESTIMÉ numériquement par Richardson, PAS dérivé avec borne d'erreur rationnelle. Tir numérique `solve_ivp` à partir de rayon `eps>0`, données `pLf(eps)=U0 eps²` ou `U0 eps²+U1 eps⁴`, jusqu'à `.85`; référence `eps=.001`, `pLf(.85)=-.003386429356487895`, proche de Step47.

```text
eps      |endpoint order0 - reference|     |endpoint order1 - reference|
.05       2.9086971547e-10                 9.2725306600e-15
.025      9.0899401721e-12                 7.0689981646e-17
.0125     2.8406357128e-13                 1.7347234760e-18
.00625    8.8783147500e-15                 4.3368086899e-18
```

L'erreur de coupure d'ordre0 chute ≈32 par division du rayon par deux : signature numérique attendue `O(eps^5)`; ordre1 cohérent au départ avec amélioration `O(eps^7)`, puis plancher flottant. **CE NE SONT PAS DES BORNES CERTIFIÉES SUR L'EDO CONTINUE.**

129 rayons [.05,.85] : `min(pg/r²)≈.8856203219`, `min(pf/r²)≈.1118648330`, `max|C_algebraically_substituted|≈1.74e-14`. Ce sont des ÉCHANTILLONS POSITIFS, PAS un certificat continu le long du nouvel IVP.

## TESTS ET PROVENANCE RÉELS

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step49_regular_center_shoot.py tests/test_hr_step49_analytic_center.py
# EFFECTIVEMENT EXÉCUTÉ : 21 PASSED en 4.41 s, depuis /mnt/data/janus-step49.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step49_regular_center_shoot
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step49_analytic_center
```

Les QUATRE nouvelles sources/tests sont OCTET POUR OCTET IDENTIQUES aux blobs GitHub vérifiés. MAIS les dépendances HISTORIQUES Step45/46/47 du runtime local ont été reconstruites fidèlement par des adaptations mathématiques et NE SONT PAS les fichiers historiques GitHub strictement byte-identiques. Donc une régression authentique de toutes les dépendances est ENCORE BLOQUÉE ; les DEUX tests Step48 désélectionnés n'ont PAS été réexécutés. Ni suite entière du dépôt ni CI. Ne PAS dissimuler cette provenance.

JSON détaillés locaux générés : `/mnt/data/janus-step49/step49-local.json` SHA256 `45f59ca454ad1c9733d17049c72c175d94f54c663058ea47f79743ca8d9bc13a` ; `/mnt/data/janus-step49/step49-center-theorem.json` SHA256 `c197212b6c38e49a6f9d45694d3798dae5672f4c10d0acf0814981d6615c4be7`. Leurs résultats essentiels sont sauvegardés dans rapport GitHub; ces deux fichiers locaux JSON détaillés n'ont PAS été ajoutés au repo.

## PROCHAIN STEP50 — VERROUS OUVERTS

1. Recréer EN UN SEUL CHECKOUT les véritables Step45/46/47 bytes GitHub, lancer Step48 complet SANS DEUX tests désélectionnés + 21 tests Step49. Empreintes sources obligatoires.
2. Établir par ODE à intervalles, Chebyshev/résidus vérifiés ou bornes rigoureuses la CONTINUATION GLOBALE de la branche analytique régulière `U(s)` jusque `.85`, les erreurs numériques, la positivité CONTINUE des deux poussières et toutes marges de chartes J/K/coefficients de poussière. Prochaine extension utile: dériver `U1` SYMBOLIQUEMENT, pas Richardson.
3. Seulement sur données exactement contraintes, calculer la PRÉSERVATION TEMPORELLE `{C,Htotal}` pour les SIX couples canoniques, fixation des lapses et rang Dirac, bords et J/K exceptionnels. Ne pas déclarer absence BD avant cela.
4. Puis véritables cosmologies non homothétiques ON-SHELL, De Felice/Aoki même action, pli Candidate-C et observations. Critique du manuscrit JHR f-EH signe inversé = autre piste.

**STATUT : CENTRE ANALYTIQUE LOCAL CONDITIONNEL DÉMONTRÉ ; POUISSIÈRES POSITIVES STRICTES AU CENTRE CERTIFIÉES ; TIR NUMÉRIQUE VERS .85 TRÈS CONVERGENT ; CONTINUATION GLOBALE ET DIRAC TEMPOREL OUVERTS ; GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP48 TERMINÉ — 2026-10-22

**SEULE BRANCHE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main`, `research/v2-flrw` ; GitHub Actions/workflows désactivés par l'utilisateur.

**LIRE D'ABORD :** `research/STEP48_ORIGINAL_POISSON_AND_CENTER_FROBENIUS_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step48-report.json`.
**CALCULATEUR POISSON ORIGINAL SUR IVP :** `numerics/hr_step48_original_ivp_oracle.py` blob `dc5101d4b0d1d5b8d0834aacff4a3ad3715a28db`.
**CONDITION DU CENTRE :** `numerics/hr_step48_center_compatibility.py` blob `aa181529d33fcfa7d1e61a4525cade3e1b0ca4c7`.
**TESTS :** `tests/test_hr_step48_center_and_original_ivp.py` blob `e1f2946eabb4e47335940c7ce010cfd7dbe2b505`.
**ORACLE HISTORIQUE :** `numerics/hr_step37_original_nonibp_oracle.py` blob ORIGINAL EXACT GITHUB `005449ade6e3582e3b9a5c3374a881a77e73e3f6`.
**ÉQUATION ORIGINE :** `numerics/hr_step45_exact_physical_ward.py`, `numerics/hr_step46_exact_secondary_ode.py`, `numerics/hr_step47_interior_ivp.py`.

## AVANCÉE SCIENTIFIQUE RÉELLE : CONTRÔLE POISSON INDÉPENDANT

Sur l'IVP NUMÉRIQUE de Step47 (r=.05→.85, données courbes non comobiles, DEUX poussières positives aux points contrôlés), reconstruction des 12 champs canoniques sur grille, y compris les horloges poussière `theta_i(r)=k_i*a_i*(r²/2+c_i*r⁴/2+c_i²*r⁶/6)`. Le vrai calculateur historique ORIGINAL NON-IBP `hamiltonians(q,r)` a été reconstruit OCTET POUR OCTET depuis GitHub (SHA ci-dessus), et ses sorties réelles et complexes ont été comparées à une autre implémentation indépendante des mêmes densités — matrices NumPy IDENTIQUES.

Dérivées fonctionnelles du Poisson de TOUTES les 12 variables par complex-step nodal, six couples contractés. Deux choix de lapses compacts indépendants A et B, 4 grilles :

```text
n      crochet A             crochet B
161    -5.909466422135e-7    -9.466192093556e-7
321    -1.477085211689e-7    -2.366493849189e-7
641    -3.692537306677e-8    -5.916200890277e-8
1281   -9.231239094041e-9    -1.479048690706e-8
```

Richardson R4 sur les trois grilles les plus fines, en ASSUMANT développement en puissances paires de h (NON démontré) : **A -8.0411576792e-15**, **B -8.19811039928889e-15**. **C'EST UN CONTRÔLE NUMÉRIQUE INDÉPENDANT FAVORABLE** à la contrainte imposée via l'ODE analytique, pas une preuve du crochet continu exactement nul. Les crochets originaux de grilles finies restent NON NULS négatifs; primaires discrètes max ~1.24e-9 à n1281. Source dans rapport machine et module régénérable.

Full JSON local effectivement généré `/mnt/data/janus-step48/research/reports/step48-local-nonibp-full.json`, SHA256 `dfc18acda78163dff61021f51429a06d6d2db4854d19655fb5dd939ab472b9a1` ; **PAS ENCORE UPLOADÉ** comme fichier GitHub séparé ; les données essentielles et les codes de reproduction sont PUBLIÉS.

## NOUVEAU VERROU CENTRE — CONDITION EXACTE ET MODE SINGULIER

En développant le **C PHYSIQUE EXACT de Step45** sur donnée sphérique régulière `Lg=a+O(r²), Lf=b+O(r²), pLg=Pg*r²+O(r⁴), pLf=Uf*r²+O(r⁴), pSg=2Pg*r+O(r³), pSf=Vf*r+O(r³), z=z1*r+O(r³)`, on obtient la relation exacte, avec `A*=a² beta1+2ab beta2+b² beta3` :

```text
lim C(r)/r² = -(m² A*)/(2 Mf² a b) *
      [6 Mf² Mg² z1 a b - 3 Mf² Pg b + Mg² a (Uf+Vf)].
```

La primaire radiale f impose `Vf=2Uf` au centre régulier. Par conséquent, pour `A*>0`, condition NÉCESSAIRE exacte :
```text
Uf(0) = Mf²*b*( Pg/(Mg²*a) - 2*z1 )
```
= environ `-0.005252426896760733` pour le benchmark. L'ancien coefficient numérique figé donne `-0.005252426896763941`, écart ~`-3.20837e-15`. **Proximité ne signifie PAS égalité exacte.**

L'équation linéarisée au centre donne `pLf'+pLf/r=3*Uf(0)*r+O(r³)`, d'où solution formelle `pLf=Uf(0)r²+Csing/r`. Une solution régulière doit éliminer `Csing/r` : l'IVP arrière n'est donc pas une preuve de régularité au centre. Essai de sensibilité : modifier `pLf(.05)` de `+1e-12` entraîne amplification mesurée ≈1.2499973 (r=.04), 2.4999873 (.02), 4.9999710 (.01), 9.9999401 (.005), 24.9998492 (.002), vs loi prédite `.05/r`. Ce mode est un développement FORMEL/LINÉARISÉ, non un théorème de singularité de la solution non linéaire.

## PROVENANCE ET TESTS — NE PAS SURVENDRE

NOUVEAUX trois fichiers exécutés localement ET byte-identiques à GitHub (blob SHA ci-dessus). Fichier oracle historique original également byte-identique. Les AUTRES dépendances historiques Step45–47, dans ce runtime local, sont des reproductions mathématiques/compatibilité et PAS les fichiers originaux bit-identiques. Ainsi, sur 12 tests du nouveau module :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step48_center_and_original_ivp.py \
   -k 'not test_original_provider_source_pins_match_real_checkout and not test_interrupted_run_manifest_keeps_Dirac_red'
# ACTUELLEMENT 10 PASSED, 2 DESELECTED en 5.27 s.
```

Les 2 NON EXÉCUTÉS exigent les CINQ dépendances historiques authentiques dans UN checkout commun. Le module `numerics/hr_step48_original_ivp_oracle.py` vérifie les cinq Git blob SHAs **FAIL-CLOSED** en mode par défaut ; cette vérification a été contournée uniquement pour l'expérience locale, signalée `check_git=False` dans le JSON local, et NE DOIT PAS ÊTRE APPELÉE vérification complète GitHub. PAS de tests de tout dépôt ni de CI Actions.

## SUITE PRIORITAIRE STEP49

1. Obtenir dans UN environnement les CINQ vraies sources historiques SHA exactes, relancer `pytest -q tests/test_hr_step48_center_and_original_ivp.py` **sans filtre**, puis `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m numerics.hr_step48_original_ivp_oracle`. Enregistrer les résultats et tout échec. Ne pas débloquer CI.
2. Résoudre le problème **À DEUX BORDS** : paramétrer `pLf=r² U(r²)`, imposer `U(0)=Uf0` déduit exactement ci-dessus, annuler le mode (1/r), construire une solution régulière par séries/Frobenius ou tir analytique/numérique certifié. Vérifier poussières positives CONTINÛMENT le long de la vraie solution IVP, J>0,K/r²>0.
3. Calculer ensuite sur données exactement primaires+secondaires le VRAI Dirac temps `{C,Htotal}` avec six couples canoniques, rang, lapse fixing, secteurs exceptionnels J/K, bords; le contrôle Poisson spatial N,M ne remplace pas cela.
4. Puis seulement évolution non homothétique on-shell, De Felice/Aoki même action, pli Candidate-C et observations. Ne pas fusionner avec manuscrit JHR externe de signe f-EH inversé.

**VERDICT : STEP48 DEUX ORACLES POISSON CONCORDENT NUMÉRIQUEMENT SUR IVP; COMPATIBILITÉ AU CENTRE NÉCESSAIRE ANALYTIQUE DÉMONTRÉE ; CENTRE RÉGULIER GLOBAL NON DÉMONTRÉ ; PRÉSERVATION DIRAC / LAPSUS NON DÉRIVÉS ; GATE_2B=OPEN ; JANUS-R NON VALIDÉ.**

---

# JANUS — REPRISE PRIORITAIRE : STEP47 TERMINÉ — 2026-10-22

**BRANCHE AUTORISÉE UNIQUEMENT :** `research/gate2b-nonhomothetic-transfer` ; `main` et `research/v2-flrw` inchangées, Actions/workflows désactivés.

**LIRE EN PREMIER :** `research/STEP47_INTERIOR_SECONDARY_ODE_INTEGRATION_AUDIT.md`.
**RAPPORT :** `research/reports/gate2b-step47-report.json`.
**SOLVEUR INTÉRIEUR :** `numerics/hr_step47_interior_ivp.py` Git blob `c558a827939f2e1fffbfc0290f2b3cc88cb69ef9`.
**TESTS :** `tests/test_hr_step47_interior_ivp.py` Git blob `1e64b528bf87142f2d1059ac736b2d4ee7a79de5`.
**ÉQUATION EXACTE :** `numerics/hr_step46_exact_secondary_ode.py` + `numerics/hr_step45_exact_physical_ward.py`.

## RÉSULTAT SCIENTIFIQUE — PREMIÈRE INTÉGRATION NUMÉRIQUE DE L'EDO SECONDAIRE EXACTE

Les étapes45–46 ont démontré les identités physiques de Ward dans la réduction sphérique et dérivé EXACTEMENT `C=K00-(K01)'` sans différences finies, puis `pLf'=-C0/C1` par élimination des deux contraintes primaires f. Étape47 : INTÉGRATION numérique de cette EDO sur `r∈[.05,.85]` avec données g/métriques/poussières prescrites, poussières f recalculées de leurs primaires à chaque point, métriques courbes, phases de poussières non comobiles et déplacement relatif non nul.

- RK adaptatif `scipy.solve_ivp` : `rtol=1e-10,atol=1e-14,max_step=.02`, 338 RHS, `pLf(.05)=-1.3126131492021531e-05`, `pLf(.85)=-.0033864293564877215`.
- 33 points hors collocation : `min(pg/r²)=.8856203218885325`, `min(pf/r²)=.11186483299522221`, toutes DEUX poussières POSITIVES AUX POINTS TESTÉS.
- Contre-calcul primaire à partir des densités ADM sphériques ORIGINALES reconstruites : max `|Hg|≈1.11e-15`, `|Hf|≈1.39e-17`, `|Ddiag|≈1.37e-16`, `|Fz|≈1.37e-16`; résidu `|C|` de substitution analytique max `1.58e-14` (petit **PAR CONSTRUCTION**, donc pas un contrôle Poisson original indépendant).
- Trois tolérances donnent extrémités `-.0033864293564835235`, `-.0033864293564877215`, `-.0033864293564879007`; différences successives `4.20e-15`, `1.79e-16`. C'est une CONVERGENCE NUMÉRIQUE, PAS une erreur globale certifiée.
- À AUCUN MOMENT le r=0 centre n'est franchi, ni la positivité de la poussière continue du nouvel IVP démontrée. Les bornes Step40–42 du profil POLYNOMIAL figé ne sont PAS transférables sans preuve au nouveau profil non polynomial.

## EXACTE REPRODUCTION — TESTS EFFECTIVEMENT EXÉCUTÉS

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step45_exact_physical_ward.py tests/test_hr_step45_secondary_point_certificate.py tests/test_hr_step46_exact_secondary_ode.py tests/test_hr_step47_interior_ivp.py
# ACTUELLEMENT EXÉCUTÉ : 39 PASSED ~3.94 s, 12+12+8+7. Tous nouveaux fichiers exécutés byte-identical SHA GitHub.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step47_interior_ivp

# Si les 33 points complets sont nécessaires :
PYTHONPATH=. python -c "import json;from numerics.hr_step47_interior_ivp import integrate_interior;print(json.dumps(integrate_interior(),indent=2))"
```

Le JSON 33 points détaillé a été généré dans `/mnt/data/janus-step45/research/reports/gate2b-step47-interior-run.json` mais PAS uploadé en tant que tel sur Github. Le rapport condensé et code de régénération sont PUBLIÉS. CI/workflows désactivés. Suite complète GitHub d'avant Step45 NON réexécutée cette session.

## PROCHAIN STEP48 — VERROU RÉEL

1. Refaire le CROCHET POISSON INDEPENDANT **NON INTÉGRÉ PAR PARTIES** du modèle original sur le NOUVEL IVP nonpolynomial par interpolation/sampling, vérifier convergence 161/321/641/1281 à DEUX fonctions de lapses, sans substituer son algèbre C par construction.
2. **CERTIFIER** en continu par intervalles l'IVP radial (error enclosure et poussières positives) et analyser le point singulier/centre `r=0`. Chercher existence/unicité régulière ou obstruction. Contrôler J/K et conditions de bord.
3. Après une vraie donnée exactement contrainte vérifiée, dériver/calculer `{C,Htotal}` pour tous SIX couples canoniques, lapseratio et rang Dirac incluant branches exceptionnelles. Ne pas conclure BD à partir de Ward/ODE seuls.
4. Puis seulement vraie évolution cosmologique on-shell, critères De Felice/Aoki de même action, Candidate-C, observations.

**ÉTAT : Step45 WARD EXACT, Step46 ODE SECONDAIRE EXACTE, Step47 IVP INTÉRIEUR NUMÉRIQUE TRÈS BON (PAS CERTIFIÉ GLOBAL), GATE_2B=OPEN, JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP46 TERMINÉ — 2026-10-22

**BRANCHE ACTIVE UNIQUEMENT :** `research/gate2b-nonhomothetic-transfer`. Ne PAS toucher `main`, `research/v2-flrw` ; ne PAS réactiver Github Actions/workflows.

**LIRE EN PREMIER :** `research/STEP46_EXACT_AFFINE_SECONDARY_ODE_AUDIT.md`.
**RAPPORT :** `research/reports/gate2b-step46-report.json`.
**CODE :** `numerics/hr_step46_exact_secondary_ode.py`, Git blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
**TESTS :** `tests/test_hr_step46_exact_secondary_ode.py`, Git blob `f09e5205d5915d546cf83875ffcafe44232411e2`.
**SOURCE MATHÉMATIQUE REQUISE :** `numerics/hr_step45_exact_physical_ward.py` Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, avec audit `research/STEP45_EXACT_PHYSICAL_WARD_AND_ANALYTIC_SECONDARY_AUDIT.md`.

## RÉSULTAT DURABLE STEP46 : ODE EXACTE DE LA SECONDAIRE LOCALE

Sur les DEUX contraintes primaires f (Hamiltonienne et impulsion radiale) de l'action ADM sphérique Hassan–Rosen + deux poussières canoniques, choisir `P(r)=pLf(r)` et `V=P'(r)` ; éliminer les deux inconnues de poussière `pf,pSf`. Substituer dans la formule de `C=K00-(K01)'` dérivée exactement au Step45. Alors, **IDENTITÉ SYMBOLIQUE** :

```text
C(r;P,V) = C0(r;P) + C1(r;P)*V
C1 = -(m2*Mg2*At*sqrt(1-z²)/(2*Mf2*Sf)) * (Lf*beta_f)/(Sf_prime*dust_coef_f)
At = beta1*Sg² + 2 beta2*Sg Sf + beta3 Sf² = Sg² J(Sf/Sg)
beta_f = sqrt(1+(theta_f_prime/Lf)²)
dust_coef_f = beta_f + [P/(2 Mf2 Sf Sf_prime)]*theta_f_prime
pLf_prime = -C0/C1  => C=0 IDENTIQUEMENT.
```

Le coefficient C1 est STRICTEMENT NÉGATIF sur un intervalle intérieur `r>0` où les marges `At,Lf,Sf,Sf',beta_f,dust_coef_f>0` et `|z|<1` établies en étapes 40–42 persistent. Cela permet une formulation en problème de Cauchy LOCAL pour le moment radial f, sous prescription régulière des autres données. **AUCUNE SOLUTION GLOBALE SUR [0,.85] n'a encore été construite**. Une solution de l'EDO avec centre régulier et DEUX poussières positives est un VERROU OUVERT. La conservation temporelle et la fixation des lapses restent ENTIÈREMENT OUVERTES.

**Important :** cet outil n'est PAS un solveur de l'évolution cosmologique à deux métriques. Il ne donne pas encore une contrainte BD complète ni un comptage des degrés de liberté. Ne pas appeler cela « solution exacte JANUS-R ».

## TESTS RÉELLEMENT PASSÉS ET REPRISE

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step45_exact_physical_ward.py tests/test_hr_step45_secondary_point_certificate.py tests/test_hr_step46_exact_secondary_ode.py
# EFFECTIVEMENT EXÉCUTÉ : 32 PASSED en 2.04 s dans /mnt/data/janus-step45,
# comprenant 24 contrôles Step45 + 8 nouvelles identités Step46, SANS adaptations.
PYTHONPATH=. python -m numerics.hr_step46_exact_secondary_ode
```

Les SIX nouveaux fichiers source/test Step45–46 sont IDENTIQUES octet pour octet à leur version Github et exécutés en local. Tests ciblés sur équations hamiltoniennes symboliques / fractions exactes, **pas** suite entière, **pas** original Step33g→44 réexécuté intégralement cette session, **pas** CI.

## RAPPEL STEP45 CONFIRMÉ

- EXACT WARD: `K02=K12=K21=K22=0`, `K11=K20=2Mg2 Sg Sg' z/(Lg Lf)`, `W=K01-K10+(K20)'=z Hg/Lf`, donc `W=0` exactement sur `Hg=0`; shift `dHg/dz=Fz/Lg`, `dHf/dz=Fz/Lf` sur source originale. Hypothèses compact support, réduction sphérique et domaine régulier.
- `C(q,q',z,z')` calculé sans différence finie, sans aucune dérivée seconde des 12 champs ou de z.
- Pour le PROFIL POLYNOMIAL STEP41 FIGÉ et constantes décimales traitées comme fractions exactes, un encadrement rationnel exact prouve `6.5545288523431e-11 < C(r=.85) < 6.5545288523432e-11`. Ce PROFIL PARTICULIER n'est pas une solution exacte C=0 dans le modèle rationalisé ; cela ne réfute PAS l'existence d'autres solutions exactes. ATTENTION : source historique Step33g a des opérations flottantes ; ne pas confondre l'étalonnage rationnel avec toutes les instructions binary64.

## PROCHAIN VERROU STEP47

1. **INTÉGRER** l'EDO exacte `pLf'=-C0/C1` à partir d'un rayon intérieur r0>0, avec données de Step41 comme amorce, par une méthode contrôlée ; tester indépendamment `Hg,Hf,D_g+D_f,Fz,C` contre les Hamiltoniens originaux NON-IBP à des rayons hors ajustement.
2. Explorer prolongement sur `r∈(.0,.85]`, sphéricité régulière `pLf=r²*P_f(r²)`, conditions au centre, décroissance des marges de poussière `pg,pf>0`, non-dégénérescence `J, K/r²>0`, éventuelle obstruction ou preuve de continuation.
3. Une fois des données exactes ou certifiées : **PRÉSERVATION TEMPORELLE** `{C,Htotal}` avec tous SIX couples canoniques, fixation des lapses, matrice Dirac et branches exceptionnelles; ne jamais inférer ghost-free de Ward seul.
4. Après cela seulement : vraie évolution non homothétique on-shell, contrôles physiques De Felice/Aoki de même action, pli et observations. Manuscrit externe JHR avec mauvais signe f-EH = piste critique séparée.

**VERDICT : STEP45 IDENTITÉS WARD EXACTES ; STEP46 REFORMULATION EXACTE C=0 EN EDO LOCALE ; SOLUTION GLOBALE À DEUX POUSSIÈRES, DIRAC TEMPOREL ET LAPSES = OUVERTS ; GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP45 TERMINÉ — 2026-10-22

**BRANCHE ACTIVE UNIQUE :** `research/gate2b-nonhomothetic-transfer` ; ne pas modifier `main`, `research/v2-flrw`, ni réactiver GitHub Actions/workflows.

**LIRE EN PREMIER :** `research/STEP45_EXACT_PHYSICAL_WARD_AND_ANALYTIC_SECONDARY_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step45-report.json`.
**CODE SYMBOLE :** `numerics/hr_step45_exact_physical_ward.py` (Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`).
**CERTIFICAT RATIONNEL :** `numerics/hr_step45_secondary_point_certificate.py` (Git blob `6ab94dacb0c6429bdce8d71311161a6b76ecc0e6`).
**TESTS :** `tests/test_hr_step45_exact_physical_ward.py` (Git blob `64c32464df011e87c11e7ca7ff0d9d101bb167aa`) et `tests/test_hr_step45_secondary_point_certificate.py` (Git blob `d2c04e5961cfb31867ea40b8d003c8e35ced9eb8`).
**HISTORIQUE :** Le commit initial Step45 `e960f774` ajoutait `research/STEP45_CHECKPOINT.txt` (identités annoncées SANS code); la présente session a indépendamment calculé les identités sur les Hamiltoniens originaux et publié les sources exactes et les contrôles rationnels.

## RÉSULTAT SCIENTIFIQUE IMPORTANT — IDENTITÉS WARD EXACTES, PAS SEULEMENT NUMÉRIQUES

Sur la DENSITÉ SPHÉRIQUE ADM+Hassan–Rosen à deux secteurs Einstein-Hilbert positifs et deux poussières canoniques en mouvement, le noyau Poisson mixte à SIX couples canoniques et à NEUF jets de lapses vérifie SYMBOLIQUEMENT :
```text
K02 = K12 = K21 = K22 = 0                   [IDENTIQUES HORS CONTRAINTES]
K11 = K20 = 2*Mg2*Sg*Sg'*z/(Lg*Lf)          [IDENTIQUES HORS CONTRAINTES]
W = K01-K10+(K20)' = z*Hg/Lf               [IDENTITÉ HORS CONTRAINTES]
d(Hg)/dz = Fz/Lg, d(Hf)/dz = Fz/Lf          [STATIONNARITÉ ALGÉBRIQUE Fz=0]
```
Sur `Hg=0`, **W=0 EXACTEMENT**, avec hypothèses de compacité des fonctions de lapses et dénominateurs réguliers. La réduction formelle du crochet complet à `int N M C`, `C=K00-(K01)'`, est donc désormais **JUSTIFIÉE EXACTEMENT DANS CETTE RÉDUCTION SPHÉRIQUE**, plutôt que conjecturée via ≈1e-15. Ne jamais étendre sans preuve à tout secteur tensoriel 4D ou au Dirac temporel.

## NOUVEAU CALCUL ANALYTIQUE DE C SANS DIFFÉRENCES FINIES

Le nouveau module dérive TOUTES les gradients d'Euler `N,N',N''` et `M,M',M''` directement en SymPy, puis simplifie `C=K00-d(K01)/dr` EXACTEMENT. Toutes les dérivées secondes des 12 champs et `z''` s'annulent, laissant `C(q,q',z,z')` algébrique. Ce C est NON NUL HORS CONTRAINTES. Cela supprime le biais numérique Step37/39 dans la définition locale, mais **ne résout pas C=0**.

## CONTRE-CONTRÔLE RIGOUREUX DU PROFIL NUMÉRIQUE FIGÉ STEP41

Pour les 9 vrais coefficients de correction Step41 traités comme fractions binaires exactes `Fraction.from_float`, avec les constantes de calibration imprimées considérées comme **rationnels décimaux exacts**, la reconstruction des DEUX poussières et la valeur analytique de C sont calculées par arithmétique d'intervalles rationnels (racines encadrées par `isqrt` à 10^-70, aucune dérivée finie). À `r=17/20=0.85` :

```text
6.5545288523431e-11 < C_frozen(0.85) < 6.5545288523432e-11
```

Borne STRICTE: le profil collocation Step41 FIGÉ n'est donc pas exactement sur `C=0` dans cette interprétation rationnelle de l'étalonnage. Six rayons rationnels (.11,.21,.43,.71,.83,.85) ont tous une valeur strictement non nulle certifiée. **Cette conclusion ne réfute PAS la possibilité d'un autre profil solution exacte.** Les opérations intermédiaires de l'ancienne source originale Step33g sont parfois en binary64 et `sp.Float`; cette preuve rationnelle sur les entrées décimales ne doit PAS être vendue comme une borne machine-bit-identical de chaque opération du programme historique. L'ancienne valeur double à .85 est cohérente à ~1e-14 près.

## TESTS EFFECTIVEMENT PASSÉS ET REPRODUCTION

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step45_exact_physical_ward.py tests/test_hr_step45_secondary_point_certificate.py
# EXÉCUTÉ : 24 PASSED, 1.30s, /mnt/data/janus-step45
PYTHONPATH=. python -m numerics.hr_step45_exact_physical_ward
PYTHONPATH=. python -m numerics.hr_step45_secondary_point_certificate
```

Les QUATRE nouveaux fichiers source/test ont été exécutés en local, puis leurs blob SHA vérifiés identiques à GitHub. C'est une suite ciblée autonome à partir des densités originelles RECOPIÉES littéralement ; la suite COMPLÈTE du dépôt et les fournisseurs historiques Step33g→44 ne sont pas relancés en totalité cette session. Les anciens tests physiques Step44 (33 passes) demeurent archivés. Aucun CI ni GitHub Actions.

## ÉTAPE46 — PRIORITÉ SCIENTIFIQUE RÉELLE

1. Utiliser la formule **EXACTE** `C(q,q',z,z')` pour construire une véritable solution `C(r)=0` sur un INTERVALLE CONTINU courbe, non comobile, avec deux poussières positives, centre et bord réguliers. Voir si elle définit une EDO/équation algébrique pour le générateur libre `pLf`; démontrer existence/unicité ou obstruction, et ne pas confondre collocation polynomiale avec solution exacte.
2. Tester indépendamment la correspondance avec le véritable Hamiltonien sous élimination de z, et la sémantique exacte rationnelle vs opérations sources binary64.
3. Puis ET SEULEMENT PUIS calculer la préservation temporelle `{C,H_total}` avec tous les SIX couples canoniques, le rang Dirac et la fixation des lapses. Ne PAS conclure fantôme BD supprimé sans cela.
4. Enfin étude réellement on-shell non homothétique, De Felice/Aoki de même action, pli Candidate-C, données observables.

**STATUT : STEP45 WARD EXACT = DÉMONTRÉ SOUS HYPOTHÈSES SPHÉRIQUES ; C EXACT ANALYTIQUE = DISPONIBLE ; PROFIL STEP41 FIGÉ PAS EXACTEMENT CONTRAINT ; EXISTENCE C=0 SUR INTERVALLE + PRÉSERVATION DIRAC + LAPSES = OUVERTS ; GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART: STEP44 COMPLETE — 2026-10-21

**ONLY ACTIVE BRANCH:** `research/gate2b-nonhomothetic-transfer`. **DO NOT MODIFY** `main`, `research/v2-flrw`. **DO NOT REENABLE** GitHub workflows/Actions.

**READ FIRST:** `research/STEP44_ACTUAL_PHYSICAL_WARD_AND_ORIGINAL_NONIBP_AUDIT.md`.
**MACHINE SUMMARY:** `research/reports/gate2b-step44-report.json`.
**NEW SOURCE:** `scripts/verify_gate2b_step44.py` Git blob `2d088b7734abfb2487da43bd5330d465f114a1ae`.
**NEW TEST:** `tests/test_hr_step44_original_physical_ward.py` Git blob `bb06f2f56911b9f5f8932184b650a90e21b73bdd`.
**PREVIOUS:** `research/STEP43_EXACT_WARD_ADJOINT_AND_PHYSICAL_GATE_AUDIT.md`.

## DURABLE KEY BREAKTHROUGH: ACTUAL PHYSICAL SOURCE RUN, NOT JUST A MOCK!

This session DIRECTLY EXECUTED `scripts/verify_gate2b_step43.py --physical` and a SECOND, genuinely independent ORIGINAL UNINTEGRATED spherical ADM-HR+two-dust canonical Poisson oracle at 161/321/641/1281 radial grid points for both independent compact lapse smearings A,B. This resolves the previous Step43 **"physical runner unexecuted"** red. The corrected Step39 witness has degree4 even f-momentum, 6 iterations, radial derivative h=.001.

Exactly SEVEN original Step33g/37/39/43 provider modules were reconstructed together as FILES BYTES IDENTICAL TO GITHUB and locally `git hash-object` verified. The NEW Step44 source + test are also Git-blob-identical to the local files actually executed. Full original source blob hashes are pinned in `scripts/verify_gate2b_step44.py`, and verification FAILS CLOSED before physics calculations if any source changes. This was a coherent targeted source worktree at `/mnt/data/janus-step44`, NOT a complete repository checkout; local shell GitHub clone DNS still unavailable.

Run on a fresh branch checkout:

```bash
# Run complete physical 7-provider verification and save regenerable FULL raw output:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step44.py --full --output research/reports/gate2b-step44-physical-verification.json

# Confirm physical single test and original step43 regression jointly:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step43_ward_operator.py tests/test_hr_step43_physical_ward_gate.py tests/test_hr_step44_original_physical_ward.py
# ACTUALLY EXECUTED: 33 PASSED, in 13.17 seconds. Step44 alone 10 PASSED twice, in 11.97 and 12.42 s.
```

### ACTUAL PHYSICAL OBSERVATIONS

- Seven physical radii r=.11,.21,.31,.43,.61,.71,.83: `max |W=K01-K10+K20'| = 1.0512424264419451e-15`, `max |D=K20-K11|=4.336808689942018e-19`, `K02=K12=K21=K22=0` **NUMERICALLY** at these points. `max |C=K00-K01'|=5.0185595262819405e-11`. This is NOT an exact pointwise C=0.
- Genuine independent `original_nonibp_extended` computes all six Poisson pairs from original 12-node-variable UNINTEGRATED Hamiltonians and re-solves relative shift. Original brackets:

```text
grid N       161              321             641              1281
Pair A    -5.9094656e-7    -1.4770844e-7   -3.6925290e-8   -9.2311575e-9
Pair B    -9.4661907e-7    -2.3664925e-7   -5.9161875e-8   -1.4790348e-8
```

- ASSUMING even spatial-error powers, highest-grid 2-level Richardson R4 estimates **A +7.30563757648e-14**, **B +1.324021139624889e-13**, vs independently integrated full nine-jet Gaussian 96-point brackets **A +7.911118062876338e-14**, **B +1.3162936854562068e-13**. Discrepancies A -6.054804863963382e-15 and B +7.727454168682165e-16. **This is empirical extrapolation, NOT a rigorous mathematical limit or error bound.** Raw original finite grids are NEGATIVE and have discrete primary errors ~1e-9 even at N1281; small extrapolated values must not be mistaken for exact zeros.
- Physical full-jet minus C-only Gaussian 96-point integral ~-1.09e-16 (pair A), ~-1.47e-16 (pair B). This directly checks Step43 C/W/D reduction on genuine ORIGINAL physical Kij at finite numerical precision.
- Three additional physically primary-satisfying but NON-secondary-fitted families, with max sampled |C|=.4286, .5820, .5215, still have max sampled |W| <=1.4e-15 and |D|~1e-19, high jets zero at tested radii. Strong indication W/D near-cancellation is structural, NOT just due to fitting C. Still no symbolic proof.
- New `research/reports/gate2b-step44-report.json` COMMITTED contains all essential site/pair/grid quantitative values. The generated 14.5k full raw JSON `gate2b-step44-physical-verification.json` was **ACTUALLY generated locally**, SHA256 `7ae03597e0ba95e9775d434274aa75ecb8264ba72a58157849687e09d2b05ab9`, but **not uploaded as a standalone Github file**: regenerate with checked-in `--full` command. Do not claim uploaded!

## ACTUAL TESTS / SCIENTIFIC SCOPE

- 10/10 NEW real-provider regression tests PASSED with all seven provider source blobs EXACT. Combined with 16 Step43 exact SymPy tests and 7 physical-instrument fabricated-negative-control tests, **33/33 PASSED IN ONE pytest PROCESS**. This is not a complete project suite; user-disabled GitHub CI remains inactive.
- **STEP44 PHYSICAL WARD STATUS: NUMERICALLY WELL SUPPORTED**, NOT ANALYTICALLY PROVED. **FULL CURVED SECONDARY C(r)=0 ON CONTINUUM: OPEN**. **TIME PRESERVATION {C,H_total}: NOT COMPUTED**. **LAPSE FIXING AND FULL DIRAC RANK: NOT COMPUTED**. **GATE_2B OPEN; JANUS-R NOT VALIDATED**.
- Step40/41/42 exact rational restricted two-dust positivity and spherical centre parity remain as previous, conditional on the fixed canonical initial-data family; they DO NOT show nonhomothetic on-shell time evolution or the physical absence of Boulware–Deser ghosts.

## NEXT RED: STEP45 — NOT OPTIONAL

1. Derive **SYMBOLIC / EXACT physical** W=0, D=0 and high-smearing cancellations directly from original six-pair HR+two-dust spherical canonical action (or exhibit obstruction); investigate whether equality is on entire phase space or only on the primary/relative-shift surface, and specify boundary terms.
2. Derive `K01'(r)` WITHOUT a finite h floor or implement a rigorous interval/spectral derivative. Establish exactly constrained `C_local(r)=0` for all r over a nontrivial curved, noncomoving two-positive-dust radial family, or honestly falsify.
3. On exact primary+secondary data calculate full `{C_local,H_total}` preservation, six-pair Dirac rank and physical lapse fixing including J/K exceptional charts and regular spherical center.
4. ONLY THEN physical nonhomothetic on-shell evolution and same-action De Felice/Aoki stability and first fold. Keep external opposite-sign-f-EH JHR audit distinct.

**VERDICT: Step44 genuine original-source physical two-oracle/3x3-Ward NUMERICAL AUDIT achieved; exact continuum secondary and full Dirac dynamics still OPEN.**

---

# JANUS — AUTHORITATIVE RESTART — STEP43 COMPLETED — 2026-10-21

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`; preserve `main` and `research/v2-flrw`.
**READ FIRST:** `research/STEP43_EXACT_WARD_ADJOINT_AND_PHYSICAL_GATE_AUDIT.md`.
**JSON REPORT:** `research/reports/gate2b-step43-report.json`.
**NEW EXACT MATH SOURCE:** `numerics/hr_step43_ward_operator.py`.
**NEW NUMERICAL REAL-PROVIDER HOOK:** `numerics/hr_step43_physical_ward_gate.py`.
**NEW RUNNER:** `scripts/verify_gate2b_step43.py`.
**NEW TESTS:** `tests/test_hr_step43_ward_operator.py`, `tests/test_hr_step43_physical_ward_gate.py`.
**PREVIOUS:** `research/STEP42_CENTER_PARITY_AND_SHARP_POSITIVE_DUST_AUDIT.md`.

## CHECKED GITHUB BEFORE WORK

Before Step43, branch HEAD `9da1a11b192150b4b55b0eb233423cdcb3769af0` was verified LIVE through the connected GitHub API. `main` remained `aead63f4098f0d15a849e579105af034b6317b30` and `research/v2-flrw` `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`; don't edit them.

## ACTUAL EXECUTED TESTS AND PROVENANCE

In isolated `/mnt/data/janus-step43` (NOT a full Git clone):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step42_center_regular_interval.py tests/test_hr_step43_ward_operator.py tests/test_hr_step43_physical_ward_gate.py
# 40 passed in 3.53 seconds: historical Step42 17, Step43 formal 16, new physical-instrument MOCK controls 7

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --selftest
# PASSED, polynomial manufactured reference only, not physical JANUS.
```

NEW scripts and tests actually EXECUTED in the container and byte-for-byte matched to GitHub Git blobs (verified by GitHub fetch and container git hash):
- `numerics/hr_step43_ward_operator.py`: `fd91411ad6cec88d88f0889ccf99a5f070ccbb54`
- `tests/test_hr_step43_ward_operator.py`: `04825a5034421fc1e12dd51ba361d81cfbd5b753`
- `numerics/hr_step43_physical_ward_gate.py`: `386febaa9b805cf423efd6feb7a8027a2069301b`
- `tests/test_hr_step43_physical_ward_gate.py`: `c9eea74b6b14eef81d0816d960b10f9744e0b8b9`
- `scripts/verify_gate2b_step43.py`: `98ae82adaad17e8be9240ceed51ddfe2e141a476`

Original historical Step42 source and tests were byte-authentic GitHub blobs and re-ran successfully; local Step41 report used COMPLETE GitHub schema and exact nine published coefficients + SHA, but was manually reserialized and its blob SHA does NOT equal actual Step41 GitHub report blob. It is a semantically faithful numerical reference, NOT a byte-equal complete checkout. Real Step33g/37/39 providers were NOT executed this session. No GitHub Actions and no full-repo tests. Previous source-authenticated Step39 numerical 32+5 passes remain historical, not reexecuted.

## SCIENTIFIC RESULT — EXACT FORMAL WARD/ADJOINT, NOT HR PHYSICS YET

Full 3x3 smearing-jet functional bracket `B[N,M]=int sum_ij N^(i) Kij M^(j) dr`, i,j=0..2. Exact formal adjoint: `A_p=sum_ij (-1)^i binom(i,p-j) derivative^(i+j-p) Kij` for 0<=p<=4, with valid indices only, requiring appropriate compact support/boundary terms.

In restricted five-coefficient support `{K00,K01,K10,K11,K20}`, define
```text
C=K00-(K01)'            (prior Step37/39 numerical near-secondary)
W=K01-K10+(K20)'        (derivative Ward obstruction)
D=K20-K11               (second-jet obstruction)
```
Then EXACTLY for compact smears `B[N,M]=int N [C*M + (W*M)' + (D*M')'] dr`. Therefore `C=0` alone **does not imply** vanishing bracket. EXACT checks of `W=D=0` and high-jet exclusions `K02=K12=K21=K22=0` (or full adjoint cancellations `A_p-δ_p0 C=0`) are required before interpreting C as the sole secondary coefficient.

16 SymPy tests include EXACT rational polynomial smeared integrals and separate counterexamples where C=0 but W, D, or K22 gives nonzero original bracket; compact boundary controls protect against IBP errors. A manufactured Ward-closed example gives both original and C-only bracket EXACT rational `10753/21358810497024000`. These are **NOT JANUS-specific proofs**.

A separate new instrument computes `C,W,D`, checks the four excluded jets using **all nine** coefficients of the actual `hr_step37_curved_solver.kernel_fast` if available, and compares actual full mixed compact-smear bracket to `int N M C` for two independent Step39 lapse pairs. 7 INJECTED POLYNOMIAL test cases and `--selftest` pass. The real physical mode exists but **WAS NOT RUN**:

```bash
# NEXT FIRST NON-OPTIONAL ACTION ON BYTE-IDENTICAL ORIGINAL GITHUB WORKTREE:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --physical --output /tmp/gate2b-step43-physical.json
```

Do NOT call the synthetic `--selftest` a JANUS physical confirmation, or infer exact Ward from numerical five-point differences.

## STEP44 EXACT NEXT RED GATES

1. ASSEMBLE a coherent byte-authentic original Step33g/37/39 GitHub dependency worktree and RUN the above `--physical` mode. Print and commit actual seven-radii Kij/C/W/D/high jets and BOTH compact lapse-pair Gauss full-vs-C comparisons, scan h and quadrature. The normal shell cannot DNS-clone Github; do not fabricate a result.
2. Determine on the PHYSICAL original all-six-pair kernel whether high jets, `D=0`, `W=0` are exact identities or identify obstruction. Derive `(K01)'` analytically/certified, construct or refute exact continuous C=0 preserving both positive dust densities and center chart.
3. ONLY on exactly primary+secondary constrained data compute full canonical Dirac **time preservation**, rank, lapse fixing including exceptional K/J sectors and boundary.
4. Only after that genuine nonhomothetic on-shell evolution, same-action De Felice/Aoki controls, Candidate-C fold and observational validity. Keep independently audited sign-reversed-f-EH JHR manuscript separate.

**FINAL: STEP43 EXACT FORMAL WARD CRITERION PASSES AND FALSE-ZERO COUNTEREXAMPLES PROVED. PHYSICAL JANUS WARD/SECONDARY NOT VERIFIED. GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP42 COMPLETE — 2026-10-21

**BRANCH ACTIVE UNIQUE:** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main` ni `research/v2-flrw`.

**LIRE EN PREMIER:** `research/STEP42_CENTER_PARITY_AND_SHARP_POSITIVE_DUST_AUDIT.md`.
**RAPPORT:** `research/reports/gate2b-step42-report.json`.
**SOURCE:** `numerics/hr_step42_center_regular_interval.py` — Git blob `e6f2b5da131d142c0d443e7077cb826125450b05`.
**TESTS:** `tests/test_hr_step42_center_regular_interval.py` — Git blob `5b63eaeb5135dd524f7ec1c5bd744541c95be6d7`.

REPRO SUR UN VRAI CHECKOUT DE LA BRANCHE:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step42_center_regular_interval.py
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step42_center_regular_interval
```

## CE QUI A ETE REELLEMENT EXECUTE

- `17/17` nouveaux tests ciblés passés dans `/mnt/data/janus-step42` en ~2.08 s. Les NOUVEAUX fichiers source/test effectivement exécutés ont des Git blob SHAs strictement identiques aux fichiers déposés et reconsultés sur GitHub.
- Le test utilise un **MINI RAPPORT STEP41 LOCAL** contenant les NEUF vrais coefficients archivés et leur SHA256, pas le fichier original complet téléchargé. Le VRAI `research/reports/gate2b-step41-report.json` a été interrogé via le connecteur GitHub et les neuf coefficients, le SHA256, le chemin `status.GATE_2B` et le blob `16c8de6ee66725622c40ba2f327c8aafa99a5cb7` sont vérifiés. Pas de nouveau run avec les fournisseurs originaux Step33g/39/40 ou test de l'intégralité du dépôt. Git clone par shell bloqué par DNS, GitHub Actions toujours désactivés.
- Erreur de sérialisation corrigée par NORMALISATION EXACTEMENT CONFORME à Step41: le vrai rapport contient certains zéros JSON `0`, et le SHA `bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d` a été calculé en convertissant les coefficients en `float`, où leurs zéros deviennent `0.0`. Un contrôle naïf du JSON aurait échoué à tort.
- SUR TOUT LE CONTINUUM `0 <= r <= 0.85`, pour la configuration canonique Step41 CORRIGEE, bornes exactes via 256 intervalles rationnels `s=r²`: `p_g/r² > 0.8854`, `p_f/r² > 0.1114` (borne fixe largement plus serrée que l'ancienne boîte de corrections `>0.039`), `J(S_f/S_g)>0.659`, `K/r²>0.229`, avec coefficients poussière, dérivées `S'_i` et racine de déplacement strictement positives.
- NOUVEAU CONTROLE CENTRE: expansions algébriques `p_{L_i}=r² a_i(r²)`, `p_{S_i}=r b_i(r²)`, `p_i=r² d_i(r²)` avec `d_i>0`, `D_g=r³ e(r²)`, `K=r² k(r²)` avec `k>0`. Toutes les fonctions normalisées sont analytiques pour `s∈[0,0.85²]` car les dénominateurs et radicaux nécessaires sont contrôlés. Métriques spatiales conformes lisses en coordonnées cartésiennes, horloges poussière scalaires paires, vecteur déplacement radial linéaire; **PAS** encore une extension générale des densités tensorielles canoniques ni un espace-temps 4D évolué.
- Contrôle indépendant avec les ADM sphériques originaux non simplifiés et les deux poussières à 6 rayons non nuls, plus limites au centre et subdivision 64/128/256. C'est de l'évidence ciblée, pas la suite entière ni revue externe.

## PROCHAIN VRAI VERROU : STEP43

1. Reconstituer enfin la CHAINE COMPLETE DE DEPENDANCES EXACTEMENT IDENTIQUES AUX BLOBS GITHUB et relancer Step41+42 et les anciennes suites ciblées dans un checkout cohérent. Enregistrer SHA et résultats, ne pas substituer des reconstructions sans les étiqueter.
2. Dériver analytiquement (ou prouver par intervalles) `(K01)'(r)` du crochet Poisson mixte pour les SIX couples canoniques et donc `C_local(r)=K00-(K01)'` sans plancher de différences finies. Résoudre `C_local(r)=0` IDENTIQUEMENT sur un intervalle courbe non comobile à deux poussières strictement positives, ou réfuter honnêtement.
3. Seulement sur des données satisfaisant les contraintes secondaires EXACTES: calculer `{C_local,H_total}`, matrice de Dirac, lapses fixés, secteurs K/J exceptionnels et r=0 régulier.
4. Puis évoluer véritablement les deux métriques non homothétiques sur les équations du même lagrangien, recouper De Felice et Aoki et examiner le premier pli du Candidate-C. Signes f-EH inversés du JHR externe = piste CRITIQUE SEPAREE.

**ETAT FINAL:** Step42 centre et sources positifs PASS restreint, secondaire courbe exacte = OPEN; Dirac préservation/lapses = OPEN; `GATE_2B=OPEN`; `JANUS-R NOT VALIDATED`.

---

# JANUS — AUTHORITATIVE RESTART — STEP41 COMPLETE — 2026-10-21

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`. Do not modify `main` or `research/v2-flrw`.

**FIRST READ:** `research/STEP41_ACTUAL_PROFILE_CONTINUOUS_POSITIVE_TWODUST_AUDIT.md`.
**CODE:** `numerics/hr_step41_profile_bridge.py`.
**TESTS:** `tests/test_hr_step41_profile_bridge.py`.
**MACHINE REPORT:** `research/reports/gate2b-step41-report.json`.
**PREVIOUS THEOREM:** `research/STEP40_CURVATURE_BOX_AND_TWODUST_INTERVAL_AUDIT.md`.
**PREVIOUS PHYSICAL INITIAL DATA:** `research/STEP39_DUAL_SMEAR_AND_HIGHORDER_AUDIT.md`.

Targeted run:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step41_profile_bridge.py
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step41_profile_bridge
```

## DURABLE RESULT — CLOSED PREVIOUS STEP40→STEP39 BRIDGE

- On Step39 curved/noncomoving two-dust PRIMARY+numerically approximate-secondary profile `solve_five_point(scale=.1,degree=4,iterations=6,h=.001)`, the FULL computed f-momentum generator coefficients are:
```python
f_delta = (-2.1921905214999423e-05, 0.0, 0.0015479757723131573, 0.0,
           -2.0933708880890434e-05, 0.0, -1.757101536020765e-07, 0.0,
           -2.9380881416697167e-09)
```
- Canonical JSON coefficient SHA-256: `bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d`.
- **MAX |even f_delta|=0.0015479757723131573**, ALL odd = exactly 0, exact binary64 rational margin to the Step40 independent coefficient cap `1/200` is `397991296652400363/115292150460684697600` ≈0.0034520242276868426. This is strictly positive, hence the already PROVEN exact 256-cell Step40 interval certificate COVERS THE SPECIFIC Step39 corrected canonical initial data.
- Therefore for every r ∈[0,.85], **strict normalized continuum dust positivity**: `p_g/r²>0.885`, `p_f/r²>0.039`. For r>0 radial canonical p_i>0; at the spherical center p_i(0)=0 due to r². Fixed Step39 metric also satisfies Step40's exact uniform J(Sf/Sg)>.5039 and K/r²>.1596 (coordinate K(0)=0).
- Extra actual 73-point numerical check r=.03...85 (NOT itself a proof): max |C_local|=6.551957240641393e-11, max |C_local/r²|=9.068452928223382e-11, four primaries max 3.885780586188048e-16, sampled min pg/r²=.8856073159, pf/r²=.111864833.
- **11 new tests PASSED (~4.84 s)** on isolated reconstructed `/mnt/data/janus_step41/repo`. Both NEW source/test byte-matched GitHub blobs `26f4d5d24069dac469bf449da4c5997db6a15253`, `34fd411dad5bfa87ec30245cff949102a1328731`. CRITICAL: historical Step33g/39 source mathematical equations and Step40 exact interval arithmetic were independently reconstructed in this execution, NOT byte-identical to actual historical GitHub providers. A full authentic clean-provider Step41 rerun is still needed. Previous Step39/Step40 source-authenticated runs stand separately, not rerun today; no complete repo suite or GitHub Actions.
- Test boundary issue intentionally caught: Python binary64 `float(.005)` lies slightly ABOVE exact 1/200; strict Fraction membership rejects it, tests use `math.nextafter(.005,0.)` as passing just-inside control. Actual coefficient safety margin >0.00345, so not a borderline conclusion.

## NEW PRIORITY STEP42 (TRUE SCIENTIFIC RED)

1. Re-run new bridge **against byte-exact historical actual GitHub Step33g/37/39/40 providers in ONE worktree**, log hashes and actual tests.
2. Compute analytic / independently validated spectral `K01'(r)` and rigorously construct/verify `C_local(r)=0` as a **CONTINUUM** noncomoving curved condition (or establish an obstruction), preserving both positive dusts and genuine spherical regularity. Last best numerical local result ~1e-11 is NOT zero.
3. Compute full six-canonical-pair functional Dirac **TIME PRESERVATION of the secondary** and determine actual lapse fixing, Poisson rank, K/J exceptional branches. Generic Hassan–Rosen ghost-free lore alone is insufficient.
4. Only if above succeeds: genuinely nonhomothetic ON-SHELL evolution and both same-reduced-action De Felice finite-H mu→0 and Aoki nonlinear KS,cS² physical controls before Candidate-C first fold, then any observational tests.

**VERDICT: STEP41 specific corrected two-dust continuum positivity=PROVED CONDITIONAL ON FIXED INITIAL-DATA FAMILY; CURVED EXACT BD SECONDARY OPEN; FULL DIRAC OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART — STEP40 COMPLETED — 2026-10-20

**ACTIVE RESEARCH BRANCH:** `research/gate2b-nonhomothetic-transfer` ONLY; `main` and `research/v2-flrw` remain untouched.
**READ FIRST:** `research/STEP40_CURVATURE_BOX_AND_TWODUST_INTERVAL_AUDIT.md`.
**CURRENT REPORT:** `research/reports/gate2b-step40-report.json`.
**CODES:** `numerics/hr_step40_curvature_box.py`, `numerics/hr_step40_twodust_interval.py`.
**TESTS:** `tests/test_hr_step40_curvature_box.py`, `tests/test_hr_step40_twodust_interval.py`.

Reproduce from a branch checkout (only these four new Python files need numpy-free pure Python + pytest):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step40_curvature_box.py tests/test_hr_step40_twodust_interval.py
# GENUINELY EXECUTED: 35 passed in 1.80 s on isolated /mnt/data/janus-step40
PYTHONPATH=. python -m numerics.hr_step40_curvature_box
PYTHONPATH=. python -m numerics.hr_step40_twodust_interval
```

ALL FOUR locally EXECUTED bytes correspond exactly to uploaded GitHub Git blob hashes, as recorded in the Step40 audit+report. Do NOT claim whole-repo suite, enabled GitHub CI, or joint Step39+40 run. Previous Step39 genuinely authenticated test groups were 32+5 separately, not reexecuted today.

## SCIENTIFIC RESULT — CONTINUUM, EXACT RATIONAL, BUT RESTRICTED

1. For EVERY independent spherical conformal curvature `|c_g|,|c_f|<=.015` and ALL r∈[0,.85] at benchmark a=.4,y=.5787707228025044: `J(Sf/Sg)>=0.5039461792087735` and `K(r)/r²>=0.15968997603142235`; the displayed figures are decimal renderings of **exact strict Fraction certificates**. A second uniform background box with a∈[.395,.405], y∈[.5787,.5789] retains J>=.5034934 and K/r²>=.1516989. These bounds concern ONLY the specified conformal spatial metric ansatz; no Dirac degrees-of-freedom result.
2. Exact negative control: antialigned `c_g=+c,c_f=-c` at r=.85 attains algebraic J=0 for c≈.07854905913576 (certified by rational bisection between .07854 and .07856), showing that unrestricted curvature positivity is false.
3. For the ACTUAL uncorrected curved/noncomoving Step37 primary family with two DISTINCT dust phase gradients and nonzero relative shift, exact outward **rational INTERVAL** arithmetic, partitioning s=r²∈[0,289/400] into 256 rational subintervals, proves `p_g(r)/r²>0.885`, `p_f(r)/r²>0.114` for ALL 0<=r<=.85. The canonical radial densities p_i(0)=0 because of r² spherical weight; positivity is strict for r>0 and normalized density remains strictly positive at r=0.
4. Robust perturbation guarantee: for ANY independent coefficients `|delta_(2k)|<=.005`, k=0..4, with all odd corrections ZERO in `Q_f=(pLf)'/(2r(1+5c_f*r²))`, exact interval arithmetic certifies `p_g/r²>0.885`, `p_f/r²>0.039` over the ENTIRE interval. These inequalities are certified even if all five corrections vary adversarially and independently; they do NOT yet establish that the specific Step39 corrected profile has coefficients within this ball. Check first!
5. Independent original unsimplified two-sector Hamiltonian formula was reconstructed in the tests and compared at several radii for baseline and nonzero perturbations. Exact interval pass is NOT based on floating-point sampling.

## NEXT SCIENTIFIC ACTION — STEP41 (HARD RED)

**FIRST:** Reconstruct/check original byte-authenticated Step33g/37/39 providers, RUN `solve_five_point(scale=.1,degree=4,iterations=6,h=.001)` and PERSIST ALL FINAL `f_delta` coefficients (they were missing from Step39 JSON summary), verifying `delta_odd=0` and `max |delta_even|<=.005` exactly with conservative float-to-rational conversion. If within ball, the Step40 theorem extends continuous dust positivity to the actual Step39 high-order **approximate-secondary** profile; otherwise enlarge or replace certificate and report. Do not silently claim this link has been made.
**SECOND:** Derive or cross-verify actual analytic/spectral derivative of K01 and solve local C(r)=0 **as a continuous constraint** with primary, two dusts, shift/center regularity.
**THIRD:** Calculate FULL six-canonical-pair Dirac `{C_local,H_T}` and lapse fixing, including K/J degeneracy. Generic HR background folklore alone is insufficient.
**FOURTH:** Only then physically nonhomothetic on-shell + both same-action De Felice/Aoki controls, Candidate-C fold and observational tests, positive-EH JANUS-R separate from external sign-reversed JHR audit.

**VERDICT: STEP40 CONTINUOUS EXACT RESTRICTED CHART+DUST POSITIVITY GREEN; CURVED EXACT SECONDARY OPEN; DIRAC TIME PRESERVATION/LAPSE FIXING OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART — STEP39 COMPLETED — 2026-10-20

**BRANCH TO CONTINUE ON:** `research/gate2b-nonhomothetic-transfer` ONLY. DO NOT modify `main`, `research/v2-flrw`.
**FIRST READ:** `research/STEP39_DUAL_SMEAR_AND_HIGHORDER_AUDIT.md`.
**MACHINE REPORT:** `research/reports/gate2b-step39-report.json`.
**ORIGINAL ACTION CROSS ORACLE:** `numerics/hr_step39_cross_oracle.py`.
**FOURTH-ORDER RADIAL SECONDARY:** `numerics/hr_step39_highorder_secondary.py`.
**TESTS:** `tests/test_hr_step39_cross_oracle.py` and `tests/test_hr_step39_highorder_secondary.py`.
**PREVIOUS:** `research/CONTINUOUS_SPATIAL_JK_AND_POISSON_EXTRAPOLATION_STEP38_AUDIT.md`, `research/CURVED_APPROX_SECONDARY_STEP37_AUDIT.md`.

## LATEST ACTUALLY EXECUTED, EXACT GITHUB BYTES

For the first time, **ALL historical Step33g/37/38 providers and current Step39 source/tests were reproduced with EXACT matching Git blob hashes in ONE coherent /mnt/data/janus-step39 isolated worktree, WITHOUT adapters**. Eleven source/test SHA values and full commands appear in Step39 audit/report. Shell Git clone DNS unavailable, and NOT a complete checkout/full repository suite. GitHub workflows disabled.

Run as TWO SEPARATE pytest processes due all-in-one time/memory issues:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step37_curved_solver.py tests/test_hr_step38_continuum_gate.py tests/test_hr_step39_cross_oracle.py
# independently executed 32 PASSED

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step39_highorder_secondary.py
# independently executed 5 PASSED

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step39_cross_oracle
# independently executed; emits two-smearing IBP Poisson and five-point h scan
```

**IMPORTANT PROVENANCE:** 32+5 = 37 TARGETED PASSES in TWO workers. The combined single-worker attempt TIMED OUT after ~34 dots. A subprocess aggregator also timed out after first group despite second group separately succeeding. Do NOT claim one successful combined 37-test suite. No full GitHub repo test run or external validation.

## NEW SCIENTIFIC RESULT

1. Frozen Step37 h=.001 degree4 five-correction curved two-positive-dust profile: two independent compact lapse pairs A (support .2-.7) and B (.25-.73). Direct original non-IBP six-pair bracket at N up to **2561** vs analytic IBP full Kij lapse-jet Gaussian integral give conditional continuum estimates **A +5.3617022e-9**, **B +3.3387069e-9**. Both methods agree under grid extrapolation, so do NOT call Step37 frozen profile an exact zero-secondary solution. Discrete original primary residual has floating-point roundoff increase at N2561.
2. Re-solving with three-point radial derivative step h halved from .001 to .0000625 yields pair A full-jet bracket **+5.3611625e-9 -> +2.1019511e-11**; local max sampled |C| **9.3489e-8 -> 4.1507e-10**. Strong O(h²) derivative floor explains much of the old residual.
3. New **FIVE-POINT O(h^4)** derivative with six iterations, even-degree4 f momentum generator: at h=.001 max sampled |C_local| ≈**5.02e-11**, pair A full-jet integral ≈**7.91e-14**, pair B ≈**1.32e-13**. Result plateaus under h refinement; may be polynomial fit/roundoff/physical, **NO proof C_local(r)=0 for all r**.
4. Improved 5-point baseline coefficient at r=.43 is **0.471663864165** rather than 3-point h=.005 **0.471665550745** (prior approximate reference had O(h²) bias). Tests explicitly updated instead of forcing agreement with old low-order reference.
5. At sampled radii both independent dust canonical momenta remain positive, exact curved primaries roundoff ≈2.2e-16. Continuous J(Sf/Sg), K/r² positivity for the fixed metric was PROVED at Step38. Two-dust continuous-interval positivity, exact central regularity and arbitrary deformations are NOT certified.

## NEXT HARD RED: STEP40

- Seek exact analytic/spectral radial derivative of K01 (independently check the ORIGINAL EH+HR+two-dust bracket), then degree4→6+ or a convergent spectral solver and direct, interval-wide |C(r)|/r² error and both positive dust bounds. Report a negative obstruction if encountered, do not force exact zero.
- On genuinely simultaneous primary+EXACT secondary data compute field-theory FULL DIRAC TIME PRESERVATION `{C_local,H_T}` across all six canonical pairs and lapse fixing; test K/J exceptional branches and r=0 coordinate factors carefully.
- Only after proving or refuting this: physically nonhomothetic ON-SHELL dynamics, SAME physical action De Felice finite-H mu→0 and Aoki nonlinear K_S,c_S² stable/unstable oracles; then fold and observations.

**VERDICT: STEP39 NUMERIC TWO-ORACLE IMPROVED SECONDARY; GENERAL BD/DIRAC CONSTRAINT PRESERVATION OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.** Distinct external sign-reversed f-EH JHR manuscript track unchanged.

---

# JANUS — REPRISE PRIORITAIRE : STEP38 — 20 OCT 2026

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`. Do not touch `main` or `research/v2-flrw`.
**FIRST READ:** `research/CONTINUOUS_SPATIAL_JK_AND_POISSON_EXTRAPOLATION_STEP38_AUDIT.md`.
**SOURCE:** `numerics/hr_step38_continuum_gate.py` (`1e4874050d2a8e478cc2414580c737f69cee6309`).
**TESTS:** `tests/test_hr_step38_continuum_gate.py` (`cd9a7625c7a62beec0cc952b91d3b929ec1fce96`).
**NEW PERSISTED REPORT:** `research/reports/gate2b-step38-report.json`.
**REPRO COMMANDS:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_step38_continuum_gate.py` and `PYTHONPATH=. python numerics/hr_step38_continuum_gate.py` from repo root.

## ACTUALLY COMPLETED AT STEP38

- 11/11 new targeted tests PASS in isolated `/mnt/data/janus-step38` Python workspace (~0.08 seconds); **new source and test Git blobs exactly match the locally executed bytes and the current GitHub source**. The local workspace reused the four exact numerical PB data rows of the Step37 published JSON in a minimized fixture; NOT a full GitHub checkout or Step37 recomputation. The Step37 provider modules were NOT byte-exactly exercised this session, and CI remains disabled.
- **Continuous EXACT-RATIONAL interval proof, fixed Step37 metric ansatz only:** at a=.4,y=.5787707228025044, cg=.0015,cf=-.0012, and **every** radius 0<=r<=.85, J(Sf/Sg)>=0.6598708967925059, and K(r)/r²>=0.22774976204166372. For 0<r<=.85, K(r)>0; K(0)=0 from coordinate r². This is not a proof of central Dirac rank, arbitrary metric variation or continuous positivity of the dust densities.
- **Numerical correction to Step37 interpretation:** from exact four archived original non-IBP mixed-bracket records n=81,161,321,641, two-level Richardson (assumes even h² expansion) estimates **CONTINUUM B0≈+5.361704637064764e-9 after** five corrections and **B0≈+0.009387437474193680 uncorrected**. Two independent R4 windows differ 1.2721120e-13, but this is NOT a rigorous uncertainty bound, does NOT prove exact nonzero B0, and certainly does not prove B0=0. The n=641 negative bracket is affected by O(h²) discretization.
- Neither the exact curved local C(r)=0 **nor** its Dirac time preservation, two-dust lapse-fixing, the fully nonhomothetic Einstein-HR on-shell solution, De Felice/Aoki same-action physical oracles, fold regularity or observations are validated.

## NEXT NONNEGOTIABLE RED — STEP39

1. **REAL-PROVIDER CLEAN REPRODUCTION FIRST:** Assemble a coherent byte-identical GitHub worktree of original Step33g provider modules, modified Step37 builder, Step37 solver/tests and Step38 analyzer/tests; execute actual targeted suites and runner. Current shell DNS cannot directly clone GitHub; do not claim it has been done.
2. Recompute original non-IBP finite-grid Poisson bracket with stronger resolution (n>=1281 after efficiency changes) and at least two unrelated compact smearings; compare extrapolated B0 with integral of independent C_local(r) and derivative-stencil h scans. Reject any false apparent zero.
3. Establish continuous/controlled C_local=0 with certified two-dust positive densities and center/boundary regularity; independently handle J/K exceptional branches. Current Step37 finite points NOT SUFFICIENT.
4. Compute **full six-canonical-pair field-theory Dirac preservation** of secondary and lapse-fixing. If it fails, register the negative result.
5. Only then genuine nonhomothetic on-shell evolution, independent De Felice finite-H mu->0 and homothetic nonlinear Aoki kinetic/gradient oracles on SAME reduced action before first Candidate-C fold.

**VERDICT: STEP38 exact spatial J/K positivity conditional GREEN; Richardson PB limit DIAGNOSTIC only; GATE_2B OPEN; JANUS-R NOT VALIDATED.** The external negative f-EH-sign JHR manuscript audit remains a DIFFERENT project thread.

---

# JANUS — AUTHORITATIVE RESTART — 2026-10-20 — STEP37 (CURRENT)

ACTIVE BRANCH ONLY: research/gate2b-nonhomothetic-transfer. Preserve main and research/v2-flrw.

FIRST READ: research/CURVED_APPROX_SECONDARY_STEP37_AUDIT.md
CODE: numerics/hr_step37_curved_solver.py, numerics/hr_step37_original_nonibp_oracle.py, updated numerics/hr_curved_moving_dust_primary.py
TESTS: tests/test_hr_step37_curved_solver.py
RUNNER: scripts/verify_gate2b_step37.py
COMMITTED REPORT: research/reports/gate2b-step37-report.json

REPRODUCTION in a true, complete branch worktree:
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step37_curved_solver.py
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step37.py /tmp/gate2b-step37-repro.json

## LATEST VERIFIED

- Curved nonproportional and noncomoving two-dust spherical primary data, nonzero HR shift, two independent positive dust canonical momenta. Even-momentum parity near the center.
- Five iterative corrections applied to the ACTUAL CURVED local mixed Hamiltonian Poisson coefficient C_local=K00-(K01)' after radial smearing derivative cancellation. On NINE off-fit radii, max absolute local C decreases 0.801743553 -> 9.58445952e-8; all primary constraints at those sites have residual <=2.22e-16. Not a rigorous continuous exact solution.
- Independent ORIGINAL NON-IBP nodal six-canonical-pair bracket at 641 nodes decreases +.00938740055 -> -3.15636675e-8, with expected second-order grid residual decrease, not zero to machine precision.
- Real 12 NEW tests PASS (isolated reconstructed /mnt/data/janus-step37); NEW solver, oracle and test source Git blob SHAs match executed bytes. CRITICAL PROVENANCE: Step33g core modules were mathematical compatibility adapters in the fresh local workspace, NOT the literal GitHub original dependencies. Original provider clean regression PENDING. Earlier Step33/35/36 tests were not combined with the 10. GitHub Actions remain disabled.
- Implementation fix: polynomial momentum generator Q_f=(pLf)'/(2r) needs conversion (n+2)/2 to modify pLf/r²; omission caused a spurious residual plateau. Protected by flat controls.
- Parity regular at formal center by ansatz, but fully center-regular 4D evolution NOT SHOWN. Spherical K(r) coordinate factors vanish at r=0, and both positive dust values are NUMERICAL sample checks, not certified interval bounds.

## NEXT EXACT RED — STEP38

1. Run the Step37 test and regeneration runner with BYTE-EXACT real Step33g provider modules in a coherent complete Git checkout; fix any regressions.
2. Test radial fit-degree/h/support convergence and both dust positivity on an entire interval, ideally prove or find exact curved C_local=0. Nine-point near-zero is insufficient.
3. On simultaneous primary+secondary data calculate full Dirac time preservation brackets with ALL six canonical pairs, their rank, and solve the lapse-fixing condition. Handle J(Sf/Sg)=0 and K=0 separately from spherical coordinate r=0.
4. Only after that: genuinely nonhomothetic Einstein-HR two-dust on-shell evolution, same-action De Felice finite-H mu->0 and nonlinear Aoki K_S,c_S² controls, then test Candidate-C first fold a~0.0301646 and physics.

VERDICT: Step37 NUMERICAL APPROXIMATE secondary GREEN; GATE_2B OPEN; JANUS-R NOT VALIDATED. Distinct external wrong-sign-f-EH JHR critique is unchanged.

---

# JANUS — ACTIVE RESTART / 20 October 2026 — Step36 (CURRENT)

**WORK BRANCH:** `research/gate2b-nonhomothetic-transfer` ONLY. Do NOT touch `main` or `research/v2-flrw`.

**READ FIRST:** `research/CONTINUOUS_J_GATE_STEP36_AUDIT.md`
**SOURCE:** `numerics/candidate_c_continuous_j_certificate.py`
**TESTS:** `tests/test_candidate_c_continuous_j_certificate.py`
**REPORT:** `research/reports/gate2b-step36-report.json`

Run targeted reproduction:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_candidate_c_continuous_j_certificate.py
python numerics/candidate_c_continuous_j_certificate.py
```

## What actually ran, and what is new

- Step36 `19/19` targeted exact-rational certificate tests PASS in **isolated reconstructed** `/mnt/data/janus-step36`. Source/test committed Git blob SHA byte-identical to local executed source/test: `375e6c3197fb9d82f19b35c66331bab2675cd506` and `5b2634d0ac8a99915617ba27785b728f03a1ec00`.
- A **continuous conditional algebraic proof**, replacing Step35's 30-point scan: for every DUST-only Candidate-C a∈[0.025,1], there is exactly one calibrated quartic branch root y∈(0.556,2.3), with **J(y)>1/2** throughout. Other quartic roots outside this interval not excluded. Decimal parameters are taken as exact terminating rationals for the proof, not universally exact physics constants.
- Independent 85-step strict rational bisection: at earlier proposed fold a≈0.0301646, y≈1.971261154529 and J≈37.4491969831. **Thus J=0 is NOT a cause of that fold within this DUST-only calibrated background**. This is NOT a kinetic/gradient/constraint regularity or physical fold-crossing verdict.
- **NEW JOINT REPRODUCTION:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_regular_secondary_flat.py tests/test_candidate_c_continuous_j_certificate.py` -> **30 passed in 0.35 s**, one isolated reconstructed `/mnt/data/janus-step36` workspace. All FOUR Step35+36 Python source/test Git blobs match exactly. **Not** a full-repository suite or GitHub CI. The orphaned Step34 checkpoint remains unresolved.

## NEXT HARD RED (Step37) — do not confuse with previous algebraic proof

1. On the earlier exact curved/noncomoving TWO-dust primary family (`numerics/hr_curved_moving_dust_primary.py`) explicitly compute `C_local(r)=K00(r)-(K01)'(r)` from the actual mixed functional Poisson bracket, over a **radial interval**, not only r=.43.
2. Find an independent radial momentum/metric profile satisfying **BOTH** primary constraints, diagonal momentum and regular shift AND `C_local(r)=0` pointwise while BOTH dust densities stay strictly positive. A mere vanishing integrated smear bracket is insufficient. A useful linearized candidate for curvature source S is `delta X(r)=-int_0^r S(s) ds /(A r^3)`, A=m² Mg² a² J/2, ONLY after computing genuine source S and proving center regularity. No curved continuation is solved yet.
3. Then explicitly calculate the FULL Dirac preservation and local lapse-fixing bracket with all six canonical pairs, including curvature terms and `K=0,J=0` exceptional sectors. Distinguish the coordinate center r=0 (spherical r² factors) from physical degeneracy.
4. Finally genuinely nonhomothetic ON-SHELL two-dust Einstein-HR dynamics and **both** same-physical-action De Felice finite-H μ→0 and Aoki nonlinear K_S,c_S² stable/unstable oracles BEFORE first fold, then observational gates if justified.

**VERDICT: STEP36=PASS as restricted algebraic background certificate; GATE_2B=OPEN; JANUS-R NOT VALIDATED.** Opposite-EH-sign external JHR manuscript audit remains separate.

---

# JANUS — ACTIVE RESTART / 20 October 2026 — Step35

BRANCH: research/gate2b-nonhomothetic-transfer. Leave main and research/v2-flrw untouched.

**FIRST READ:** research/RESTRICTED_REGULAR_CENTER_SECONDARY_STEP35_AUDIT.md
**SOURCE:** numerics/hr_regular_secondary_flat.py
**TEST:** tests/test_hr_regular_secondary_flat.py
**REPORT:** research/reports/gate2b-step35-report.json
**REPRO:** OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_regular_secondary_flat.py

## Latest actually executed

11/11 targeted tests passed in isolated reconstructed /mnt/data/janus-step35 (Python with numpy and pytest), using source/test with Git blob SHAs d30281a11d854084270a4f536e24e2dc857d58fc and 6425b1c36c8d7e4401bfffe6dabf4f9b31f58cc6. Whole repository and other prior Step33/34 tests were NOT rerun. GitHub workflows disabled; full clone DNS unavailable.

## Scientific increment

On previously derived Step33f exact flat/comoving, nondegenerate-J local mixed Poisson bracket, C_flat = (m² Mg² a² J/2)*(r³ X)' with X=Pg/(Mg²a)-Pf/(Mf²b). Hence local C=0 implies r³ X=constant; CENTER REGULARITY forces X=0 everywhere. This NECESSITY (not just sufficiency) holds only in this restricted family.

An explicit radially varying positive TWO-dust primary+restricted-secondary witness at a=.4 has pg/r²>=.9, pf/r²>=.124128 on [0,1] for eps=.08; 5 eps cases including -.15 remain positive. Deliberately perturbing Pf separately retains the primaries but violates the secondary. Thirty dust-only Candidate-C points have J>.52; J=0 is an EXCLUDED degenerate relative-shift chart, not proven safe.

## WARNING: orphaned Step34 checkpoint

research/STEP34_CHECKPOINT.txt exists but referenced Step34 audit, test, runner and JSON do not appear in branch tree; only its source numerics/hr_original_discrete_pb.py exists. No new claim that historical Step34 tests can be rerun from this repository.

## HARD NEXT RED

Construct curved/noncomoving primary+LOCAL SECONDARY=0 on continuous radial interval using C_local=K00-(K01)' (not mere integral); preserve positivity of both dust densities, relative-shift K/J nondegeneracy, center regularity. THEN compute Dirac time preservation, full bracket rank and lapse fixing; THEN same-action nonhomothetic on-shell + De Felice/Aoki physical oracles before first fold. Distinct external JHR wrong-EH-sign audit stays separate.

VERDICT: STEP35 restricted rigidity tested; GATE_2B=OPEN; JANUS-R NOT VALIDATED. No physical ghost/gradient/fold/CMB viability conclusion.

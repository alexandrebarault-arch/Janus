# JANUS — CHECKPOINT b3c3d6 PARTIEL : JETS MIXTES ODE ET CHAMPS DE POUSSIÈRE (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD de reprise lu `6f697c915677e07ed16405729b152cde1b059e29`. Avancée scientifique locale : garde formelle exacte des jets mixtes `F(r,U,rG)` d'ordre radial 0 à 3. Prochaine étape INCHANGÉE : `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII`.

**THÉORÈME RESTREINT :** si `2sU_s=G(s,U)-2U` et `Uc` est le jet cubique exact en `s0=r0²>0`, les jets 0/1/2/3 de `F(r,U(r²),rG(r²,U(r²)))` sont reproduits par `Uc` pour F lisse. Remplacer `rG` par `d(r²Uc)/dr` modifie en général le troisième jet de F de `-16r0^6 U_ssss F_v`. Témoin rationnel JOUET : `U=3+2s+s³+s⁴`, `G=2u+2s(2+3s²+4s³)`, `r0=1/2`, défaut `D'''=-6`. Le candidat Step58 corrigé déjà publié utilise bien `pLfr=rG` pour les champs dépendants `pf,pSf` : conserver ce choix. Cela ne certifie A/B/E physiques ni le BVP.

**TESTS LOCAUX EXÉCUTÉS :** `cd /mnt/data/janus_b3c3d6_mixedjets && PYTHONPATH=. python -m unittest discover -s tests -v` : **5 PASS, 0 FAIL**, SymPy exact, témoins non indépendants ; `python -m compileall -q numerics tests` PASS. Aucun moteur original Step45/46/55/58 exécuté dans cette session ; sources et blobs lus via connecteur. DNS raw.githubusercontent.com du container échoue. Les quatre rayons et les six coefficients physiques restent NON REJOUÉS.

**LIVRABLES PUBLIÉS ET RELUS :**
- `numerics/hr_b3c3d6_mixed_ode_jet_guard.py` blob `fc14fa8b401699d37d2f2e530cb54925aad33898`.
- `tests/test_hr_b3c3d6_mixed_ode_jet_guard.py` blob `61ba4b0d35753cbfc1217878f642ffbb30810918`.
- `research/STEP68AD_B3C3D6_MIXED_ODE_JET_DEPENDENCY_AUDIT.md` blob `b9f4367413bb3115098f42a0dddf55749c3f58e1`.
Les blobs code/tests relus sont identiques aux octets testés localement.

**PRIORITÉS :** (1) rejeu authentique des cinq sources Step45/46/55/58 avec candidat cubique aux rayons 1/4, 1/2, 7/10, 17/20 ; comparer six coefficients affine/cubique et contrôles de coquille ; (2) factorisation/enclosures, raccord analytique/C∞ centre, budgets de jets, BVP positif deux vrais bords ; (3) Dirac six couples, charges/jauge, K=0/J=0, dynamique 4D, stabilité, observables. **Ne toucher ni main, ni research/v2-flrw, ni workflows. HISTORIQUE INTÉGRAL CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : BUDGET EXACT DES JETS DE LAPSES AU BORD (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD authentifié à cette reprise : `f91328dad757e383f69f899628cebb476e8be3eb`. HEAD après trois livrables scientifiques : `765a5a44e09e5d56caa954ba5e831e0fb066d578`. Étape effective `b3c3d6_PARTIAL_FULL_OPERATOR_ENDPOINT_JET_BUDGET`. Prochaine étape **inchangée** : `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII`.

**LEMME EXACT CONDITIONNEL (forme Step58 complète) :** à un bord `N(R)=M(R)=u>0`, si `T=(A_N+A_M)u+B_NN'+B_MM'+E_NN''+E_MM''`, `|T|<=tau`, `P=max(|N'|,|M'|)` et `Q=max(|N''|,|M''|)`, alors `|A_N+A_M|u<=tau+(|B_N|+|B_M|)P+(|E_N|+|E_M|)Q`. Avec budget commun `H>=P,Q`, `H>=max(0,|A_N+A_M|u-tau)/(sum|B|+sum|E|)` si le dénominateur est non nul ; si tous B/E sont exactement nuls et le défaut est supérieur à tau, terminal impossible. Saturation EXACTE sur le contre-exemple JOUET à `R=17/20,epsilon=10^-8` : `H=40000000000/289`. **Aucune borne de jets physique ni enclosures Step58 établies**. Les anciennes valeurs numériques ponctuelles suggèrent seulement, sous hypothèses NON certifiées, une échelle `H>2.79e46` au bord.

**EXÉCUTION LOCALE RÉELLE :** `PYTHONPATH=/mnt/data/janus_endpoint_guard python -m unittest discover -s /mnt/data/janus_endpoint_guard/tests -v` : **5 PASS, 0 FAIL**, arithmétique rationnelle exacte, tests non indépendants ; `python -m compileall -q` PASS. Sources originales Step45/46/55/58 **LUES** avec SHA GitHub, **NON EXÉCUTÉES** dans cette session ; candidat cubique aux quatre rayons NON REJOUÉ.

**FICHIERS PUBLIÉS ET RELUS :**
- `numerics/hr_b3c3d6_endpoint_jet_budget.py` — blob `c8684993db94ca0a186427d9d0921942f5b82cc3`, octets identiques aux tests locaux.
- `tests/test_hr_b3c3d6_endpoint_jet_budget.py` — blob `926ff2c0d6f4750ea92cf76d4a40baa493a7bf01`, octets identiques aux tests locaux.
- `research/STEP68AD_B3C3D6_FULL_OPERATOR_ENDPOINT_JET_BUDGET.md` — blob `6a587932c546d4a0539acbe73f181b90f578d502`.

**PRIORITÉS :** (1) rejeu SHA-authentifié Step45/46/55/58 avec jets cubiques à `r=1/4,1/2,7/10,17/20` et comparaison des six coefficients affine/cubique ; (2) factorisation exacte ou enclosures, régularité et borne des jets, raccord centre et vrai BVP positif aux deux bords ; (3) Dirac six couples, charges/jauge temporelle, K=0/J=0, 4D/stabilité/observables. `main`, `research/v2-flrw` et workflows interdits de modification. **HISTORIQUE INTÉGRAL CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : MODE PLAT C∞ EXCLU PAR ANALYTICITÉ CENTRALE (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD initial authentifié `32d2a2fe047efcaf2cb27d7efe378595d9fd7085`. Étape effective : `b3c3d6_PARTIAL_ANALYTIC_CENTER_SMALL_B_TOY_GUARD`. Prochaine étape inchangée : `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII`.

**THÉORÈME EXACT MAIS JOUET :** pour `r²(N-2)-εr⁴N'=0`, `ε>0`, `M=1`, toutes les solutions sur `r>0` sont `N=2+C exp(-1/(εr))`. Le terminal `N(R)=1` sélectionne une solution C∞ strictement positive et plate au centre, avec `N'(R)=-1/(εR²)`, mais **non analytique au centre**. Si N est analytique en r au centre, sa série formelle impose `N≡2` et exclut `N(R)=1`. La parité C∞ ne suffit pas. **Aucune analyticitė des lapses Step55/58 n'est établie.**

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_analytic_center && PYTHONPATH=. python -m unittest discover -s tests -v` : **5 PASS, 0 FAIL**, non indépendants ; `python -m compileall -q numerics tests` PASS. Aucun moteur original Step45/46/55/58 exécuté cette session ; candidat cubique Step58 aux quatre rayons NON rejoué.

**LIVRABLES GITHUB PUBLIÉS ET RELUS :** `numerics/hr_b3c3d6_analytic_center_small_B_guard.py` blob `9b16a93e258c7600d215f4c7eef23c69fbd76e74` ; `tests/test_hr_b3c3d6_analytic_center_small_B_guard.py` blob `5b63928c33ea5cbaa4a7e5e9891fe77b65c17fc2` ; `research/STEP68AD_B3C3D6_ANALYTIC_CENTER_SMALL_B_TOY_GUARD.md` blob `35b2f7770febc67965e3597322781f0f34d7bcfa`. Code/tests identiques aux octets locaux testés. Branches `main`, `research/v2-flrw` et workflows : ne pas modifier.

**ACTIONS PRIORITAIRES :** (1) rejeu original SHA-authentifié Step45/46/55/58 avec jets cubiques à `r=1/4,1/2,7/10,17/20`, comparaison six coefficients affine/cubique ; (2) factorisation exacte/enclosures et véritable analyticitė ou régularité centrale des lapses, puis BVP positif à deux vrais bords ; (3) Dirac six couples, charges/jauge temporelle, K=0/J=0, dynamique 4D, stabilité et observables. **HISTORIQUE INTÉGRAL CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : INVARIANCE EXACTE CUBIQUE→QUARTIQUE DES JETS STEP58 (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD lu au début : `8b7a0f1e0d2246eff8bcc14ea6c5d88f6dda74a6`. Dernier commit scientifique avant ce checkpoint : `c455646c053ce48c82d6469a869fd79a8b29c4fb`. Étape effective **b3c3d6_PARTIAL_CUBIC_QUARTIC_JET_ORDER_INVARIANCE**, prochaine étape **inchangée** : `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII`.

**AVANCÉE EXACTE MAIS FORMELLE :** sur `r0>0`, les prolongements cubique `Uc` et quartique `Uq=Uc+U4(r²-r0²)^4/24` donnent les mêmes jets radiaux 0,1,2,3 de toute composition lisse `F(r,U)`. Premier écart `ΔF''''=16 r0^4 U4 F_U(r0,U0)` ; pour `pLf=r²U`, `ΔpLf''''=16 r0^6 U4`. Lecture du moteur Step58 original blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` : ses coefficients retournés utilisent `q,q',q'',q'''` et `z,z',z'',z'''` (pas `q''''` effectivement atteint). **Conséquence CONDITIONNELLE : les six coefficients Step58 cubiques et quartiques doivent être identiques au point**, sans rien affirmer sur leurs valeurs physiques. Ce n'est PAS un rejeu de l'original ni une preuve de Dirac.

**TESTS EXÉCUTÉS :** `cd /mnt/data/janus_run11 && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 PASS, 0 FAIL** (non indépendants), cinq différences divisées SymPy exactes et deux calculs directs du saut de quatrième dérivée ; `python -m compileall -q numerics tests` PASS. Première tentative d'expansion symbolique rationnelle expirée, méthode finale par différences divisées PASS en 0,457 s. **Original Step45/46/55/58 NON exécuté**, candidat corrigé aux quatre rayons NON rejoué, six coefficients physiques NON calculés dans cette session. GitHub consulté via connecteur ; clone réseau DNS local impossible.

**NOUVEAUX FICHIERS GITHUB CRÉÉS ET RELUS, OCTETS IDENTIQUES AUX FICHIERS TESTÉS :**
- `numerics/hr_b3c3d6_cubic_quartic_step58_jet_invariance.py` blob `2e6df2e83cfb25d46b48d39a6e24176ac6db346c`.
- `tests/test_hr_b3c3d6_cubic_quartic_step58_jet_invariance.py` blob `0312ebdabeb2f0f12dc9d81f7bb13d8e9848690b`.
- `research/STEP68AD_B3C3D6_CUBIC_QUARTIC_STEP58_JET_ORDER_INVARIANCE.md` blob `eaf1fe08a4ba600e2307854c7bf0f8dd1ab65a5a`.

**PROCHAINES ACTIONS PRIORITAIRES :** (1) rejeu original SHA-authentifié Step45/46/55/58 avec candidat cubique à `r=1/4,1/2,7/10,17/20`, comparaison des six coefficients affine/cubique et résidus ; (2) factorisation/enclosures, raccord centre et BVP des lapses positifs aux DEUX bords ; (3) Dirac six couples, charges/jauge temporelle, K=0/J=0, dynamique 4D, stabilité et observables. **Ne modifier ni `main`, ni `research/v2-flrw`, ni les workflows désactivés.** Historique intégral ci-dessous.

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : CERTIFICAT EXACT D'ORDRE DU JET CUBIQUE (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD authentifié à cette reprise : `f06d8e8a61738760c60227c71a7e1a23778f67a9`. HEAD juste avant ce checkpoint : `9b08ff22069ab260b03f5cd69a6247cb6f6dc800`. Étape effective `b3c3d6_PARTIAL_CUBIC_HOLONOMICITY_ORDER_CERTIFICATE`; prochaine étape **inchangée** : `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII`.

**NOUVEAU RÉSULTAT EXACT, LOCAL ET LIMITÉ :** pour `2sU_s=G(s,U)-2U`, le prolongement cubique construit avec U_s/U_ss/U_sss de l'EDO annule les coefficients d'ordre 0,1,2 du résidu `H=2U_c+2sU_c'-G(s,U_c)`. Le coefficient cubique est `-s0 U_ssss/3`, avec `U_ssss=[G_sss+3G_ssU U_s+3G_sUU U_s²+G_UUU U_s³+3G_sU U_ss+3G_UU U_s U_ss+(G_U-8)U_sss]/(2s0)`. Pour `D(r)=d(r²U_c(r²))/dr-rG(r²,U_c(r²))`, `D=D'=D''=0` au rayon de contact, mais `D'''=-16r0^6 U_ssss` peut être non nul. Témoin analytique **JOUET** exact `r0=1/2, U_ssss=24/13, D'''=-6/13`. Cela établit la limite d'ordre du jet cubique, **aucun résultat numérique Step55/Step58 physique**.

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_preflight && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 PASS, 0 FAIL** non indépendants, 5 identités formelles exactes et un témoin analytique ; `python -m compileall -q numerics tests` PASS. Une erreur intermédiaire de substitution s0=r0² a été corrigée avant publication.

**FICHIERS PUBLIÉS ET RELUS SUR GITHUB :**
- `numerics/hr_b3c3d6_cubic_jet_order_certificate.py` blob `a149e0c81af460b9d8dcea40546331e167d079e5` (octets testés identiques).
- `tests/test_hr_b3c3d6_cubic_jet_order_certificate.py` blob `4b10f69301b4ff90e97adb5c186d8f296f1b19c0` (octets testés identiques).
- `research/STEP68AD_B3C3D6_CUBIC_HOLONOMICITY_ORDER_CERTIFICATE.md` blob `62e24c4365ebbaef79ced9e64546f809f1463622`.

**LIMITES ET ACTIONS PRIORITAIRES :** clone réseau GitHub impossible (DNS local), connecteur GitHub lecture/écriture opérationnel. Aucun moteur original Step45/46/55/58 exécuté dans cette session ; six coefficients corrigés aux quatre rayons, U_ss/U_sss/U_ssss physiques, factorisation/enclosures, raccord centre, lapses positifs/deux vrais bords et Dirac/4D/stabilité/observables **NON TESTÉS**. Prochaine action : rejeu original SHA-authentifié du candidat corrigé aux quatre rayons et comparaison affine/cubique ; puis seulement les certificats globaux. `main`, `research/v2-flrw`, workflows désactivés : ne pas modifier. **TOUT L'HISTORIQUE CI-DESSOUS EST CONSERVÉ.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : SENSIBILITÉ EXACTE DES JETS CUBIQUES (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD de reprise lu en direct : `610875ecc3715a6efeeb7f5c7ace2c9ea37f3e9f`. Étape effective : `b3c3d6_PARTIAL_ENDPOINT_JET_SENSITIVITY` ; prochaine étape **inchangée** : `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII`. Cette session a exécuté des preuves SymPy sur les sensibilités des jets, **PAS** le moteur Step58 original ni la solution numérique Step55.

**NOUVEAU RÉSULTAT EXACT RESTREINT :** les prolongements affine et cubique de U(s) ont les mêmes jets d'ordre 0/1 au point, mais les différences cubique-affine des jets radiaux sont `Delta pLf''=4r^4 U_ss`, `Delta pLf'''=36r^3 U_ss+8r^5 U_sss`, `Delta pLfr''=4r^3 G_U U_ss`, `Delta pLfr'''=24r² G_U U_ss+24r^4(G_sU+G_UU U_s)U_ss+8r^4 G_U U_sss`, avec `pLfr=rG(s,U)`. Pour `H=F(s,U)`, `Delta H''=4r² F_U U_ss`. L'opérateur Step58 original contient `Dt(X)` et `Dt(deltaZ)` ; aucune invariance de ses coefficients d'ordre inférieur ne découle des seuls jets 0/1 identiques. Ces formules **ne prouvent pas** des écarts physiques non nuls sur Step55.

**EXÉCUTION LOCALE :** `PYTHONPATH=. python -m unittest tests.test_hr_b3c3d6_endpoint_jet_sensitivity_audit -v` : **5 PASS, 0 FAIL**, non indépendants ; **9 résidus SymPy exacts nuls**, `compileall` PASS. Témoin rationnel jouet hors coquille : `Delta pLf''=1/14`, `Delta pLf'''=389/308`, `Delta pLfr''=15/14`, `Delta pLfr'''=21387/1540`. Sources Python publiées identiques aux octets testés, SHA Git vérifiés localement et via relecture connecteur.

**FICHIERS PUBLIÉS/RELUS :**
- `numerics/hr_b3c3d6_endpoint_jet_sensitivity_audit.py` blob `aa530d224e305bc8b23bd415be25f67a585d7328`.
- `tests/test_hr_b3c3d6_endpoint_jet_sensitivity_audit.py` blob `35b7d67e293687abdeda5dbadcaf3dc750856721`.
- `research/STEP68AD_B3C3D6_ENDPOINT_JET_SENSITIVITY_AUDIT.md` blob `62b4cb556534be45d7e3bd2625747159d86a53d2`.

**LIMITES ET ACTIONS PRIORITAIRES :** DNS réseau local vers GitHub bloqué ; connecteur GitHub lecture/écriture opérationnel. **Aucun** rejeu original Step45/46/55/58 dans cette session, aucune nouvelle valeur physique U_ss/U_sss, aucun résultat sur les six coefficients ni les lapses. Exécuter ensuite le candidat corrigé sur les cinq blobs originaux SHA-authentifiés aux quatre rayons ; comparer ancien affine/cubique, puis factorisation exacte et enclosures, raccord centre, BVP lapses positifs aux DEUX vrais bords, Dirac/charges/générateurs/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables. Branches `main`, `research/v2-flrw` et workflows intacts. **TOUT L'HISTORIQUE EST CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : CANDIDAT DE JETS ODE STEP55 CUBIQUES CORRIGÉS (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** HEAD au début de session `4831ad91b2120bc0ab5dbfbcd47d4d4b8e11ba60`. La prochaine étape effective reste `b3c3d6_CORRECTED_CUBIC_JETS_RERUN_ORIGINAL_STEP58_FOUR_RADII` ; le candidat est PUBLIÉ mais son intégration originale n'est PAS exécutée.

**RÉSULTAT EXACT RESTREINT :** pour `2sU_s=G(s,U)-2U`, dérivées `U_ss=[G_s+(G_U-4)U_s]/(2s)` et `U_sss=[G_ss+2G_sU U_s+G_UU U_s²+(G_U-6)U_ss]/(2s)`, vérifiées par 3 identités radiales SymPy indépendantes. Le nouvel outil calcule les jets d'ordre 1/2/3 et contrôle `pLf',pLf'',pLf'''` par deux voies. Témoin jouet `G=s²+U²,s=1/4,U=1/2` : `U_s=-11/8,U_ss=37/4`, défaut affine `pLf''=37/16`, `pLf'''=1369/64`. Ceci n'établit PAS de défaut non nul sur Step55 physique.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `cd /mnt/data/janus_ode_repair && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 PASS, 0 FAIL final**, non indépendants ; `python -m compileall -q numerics tests` PASS ; 3 identités exactes SymPy PASS. Deux erreurs initiales d'attente dans les tests jouets corrigées avant publication. **Step45/46/55/58 originaux et 3 tests d'intégration du candidat NON exécutés cette session** (DNS local indisponible). Le probe ancien et ses six coefficients numériques NE SONT PAS réévalués ni invalidés par ces tests. Aucune preuve uniforme, aucun BVP de lapses, aucun rang Dirac.

**NOUVEAUX LIVRABLES PUBLIÉS ET RELUS :**
- `numerics/hr_b3c3d6_ode_consistent_jet_map.py` blob `c66534cab7da29cf9c214f08c965def3b99b4e63` (octets localement testés).
- `tests/test_hr_b3c3d6_ode_consistent_jet_map.py` blob `6ed35dffb7f9c1f61d6ed0edc7106f990e912d32` (octets localement testés).
- `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` blob `9eb5167bec74fc427307a262faaa6a1f785785a8` (NON exécuté).
- `tests/test_hr_b3c3d6_corrected_step58_point_probe_candidate.py` blob `625304d17c903a7e8311c72030224a19d6f7e217` (3 tests NON exécutés).
- `research/STEP68AD_B3C3D6_CORRECTED_CUBIC_ODE_JET_REPAIR.md` blob `bbb5bc5240373867e1dc9c8fc3bc5eef87048ac4`.
- `research/reports/gate2b-b3c3d6-corrected-cubic-ode-jet-candidate.json` blob `9dbe7ef0a64fb28ec0a4eb3e9d0e1cbd3b95f043`.
- `README.md` préfixé, blob `e00a0fb04ea79004e692fceb9b97e755b66f9581`.

**PROCHAINES ACTIONS PRIORITAIRES :** 1) exécuter avec imports originaux SHA-authentifiés le nouveau candidat Step58 aux quatre rayons ; mesurer vrais `U_ss,U_sss`, défauts affines, les six coefficients et leur différence au probe ancien ; 2) factorisation exacte et enclosures sur `0<r<=17/20`, raccord centre ; 3) vrai BVP lapses strictement positifs et DEUX bords Step55 ; 4) pullback Dirac, charges/générateurs, quotient de jauge temporelle, six couples/rang/tertiaires, K=0/J=0, 4D/stabilité/observables. `main`, `research/v2-flrw` et workflows intacts. **HISTORIQUE COMPLET CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : AUDIT EXACT DE COHÉRENCE DES JETS STEP55/STEP58 (2026-10-29)

**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 PARTIELLE.** Une incohérence méthodologique du probe numérique Step58 original a été identifiée et démontrée **formellement**, sans conclure à une erreur des coefficients observés : le script source `numerics/hr_b3c3d6_full_original_step58_point_probe.py` (blob `643d90183367e74a28ed453d93f5489074b75b08`) prolonge localement `U(s)` par une fonction affine alors que l'EDO Step55 `2sU_s=G(s,U)-2U` impose en général des dérivées `U_ss,U_sss`. Les jets `pLf''` et `pLf'''` du prolongement manquent respectivement `4s² U_ss` et `36rs U_ss+8rs² U_sss`. Identités exactes `U_ss=[G_s+(G_U-4)U_s]/(2s)` et `U_sss=[G_ss+2G_sU U_s+G_UU U_s²+(G_U-6)U_ss]/(2s)`.

**TESTS RÉELLEMENT EXÉCUTÉS :** `PYTHONPATH=/mnt/data/janus_jet_audit python -m unittest discover -s /mnt/data/janus_jet_audit/tests -v` : **5 unittest PASS, 0 FAIL**, non indépendants ; exécution directe du certificat PASS. Témoin rationnel JOUET `G=s²+U², s=1/4,U=1/2` : `U_ss=37/4`, défauts `37/16` et `1369/64`. Témoin affine exact sans défaut PASS. **Aucun moteur Step45/55/58 original exécuté pendant cette session.** Ni `U_ss≠0` aux quatre points Step55 ni l'effet sur les six coefficients Step58 ne sont prouvés. Les résultats numériques antérieurs restent des indications NON certifiées, et non des résultats réfutés.

**NOUVEAUX LIVRABLES PUBLIÉS ET RELUS :** `numerics/hr_b3c3d6_step55_jet_holonomicity.py` blob `22fea2970d22027e2a8a8531f22bb87a4f7af2e5` ; `tests/test_hr_b3c3d6_step55_jet_holonomicity.py` blob `d607c1fcc4954982ffd30b47f088c461220ec351` ; `research/STEP68AD_B3C3D6_STEP55_ODE_HIGHER_JET_CONSISTENCY_AUDIT.md` blob `27a0539a2eebbcd0a538fe0188d6ff914c477e2b` ; `research/reports/gate2b-b3c3d6-step55-ode-higher-jet-consistency.json` blob `5474b12802dfdfda6c54c8f841698ca2326b9ac4`. HEAD vérifié avant checkpoint `60a2c9c086771528a0b03b3ede67edba0772b4e8`.

**PROCHAINE ÉTAPE PRIORITAIRE :** corriger le prolongement `U(s)` au moins jusqu'à l'ordre 3 à partir de l'EDO, imposer des gardes holonomiques indépendants sur `pLf',pLf'',pLf'''`, puis **REJOUER** l'original Step58 aux quatre rayons avec vrais jets. Ensuite seulement factorisation exacte des `B_N,B_M`, enclosures sur `0<r≤17/20`, lapses positifs/deux vrais bords, pullback Dirac, charges/générateurs/jauge temporelle, six couples/K=0/J=0/4D/stabilité/observables. Aucune modification des branches `main` et `research/v2-flrw` ni des workflows. **TOUT L'HISTORIQUE CI-DESSOUS EST CONSERVÉ.**

---

# JANUS — ADDENDUM DE COHÉRENCE DES JETS STEP55/STEP58 (2026-10-29)

Le script numérique Step58 a été corrigé pour évaluer `G(s,U)` au **même rayon décimal exact** que les jets `pLf'`, plutôt qu'au carré flottant de `radius` : ancien écart `pLf'` ~3,3e-19 à R=17/20. Une assertion `|pLf'_jet-r*G(s,U)|<1e-35` est ajoutée. **5 unittest PASS, 0 FAIL après correction**, y compris le rejeu original Step55 256 cellules et la sensibilité 70 décimales ; les six valeurs de coefficients publiées restent inchangées au format float. **NOUVEAU BLOB DU CODE TESTÉ : `643d90183367e74a28ed453d93f5489074b75b08`**, remplace `4e3c78bbdd09831416bf8699c8e24e99253f955d` dans le checkpoint immédiatement ci-dessous ; test blob `c74526a18cdae02ba56da19bd45e77fdd5f355b3` inchangé. Aucune preuve uniforme ajoutée. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : PREMIER REJEU NUMÉRIQUE COMPLET STEP58 ORIGINAL SUR STEP55 (2026-10-29)

**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 RESTE PARTIELLE.** Prochaine étape prioritaire : transformer le nouveau signal numérique en **certificat exact/intervalle** de B_N,B_M,E_N,E_M et des signes A_N,A_M sur la véritable solution Step55 pour tout 0<r<=17/20 ; vérifier les dérivées/zéros, le raccord central, les lapses strictement positifs et les DEUX vrais bords. Puis pullback Dirac, générateurs/charges, quotient de jauge temporelle, six couples/rang/tertiaires, K=0/J=0, 4D/stabilité/observables. Aucune validation physique globale.

**AVANCÉE RÉELLE :** moteurs originaux Step45/46/Step55-normalized/Step55-barrier/Step58 exécutés après reconstruction des octets SHA-authentifiés ; Step57 seulement shim minimal d'import, PAS moteur complet. Le vrai Step58 `physical_operator()` complet (six coefficients A_N,A_M,B_N,B_M,E_N,E_M) a été évalué sur la solution numérique de l'EDO Step55 aux quatre rayons r=1/4,1/2,7/10,17/20. L'original Step55 `certify_global_barrier(cells=256)` a aussi été REJOUÉ : PASS. Les primaires Fz,Hg,Hf et la secondaire C évaluées sur les jets construits ont des résidus <9e-45 (45 décimales). À R=17/20 : A_N≈2437.093996367644 ; A_M≈-4676.647234168184 ; B_N≈1.83e-44 ; B_M≈-1.00e-44 ; E_N≈1.40e-45 ; E_M≈5.61e-45. Aux trois autres points, les quatre coefficients de jets sont également compatibles avec zéro à ~10^-44. Ratios CONDITIONNELS -A_N/A_M ≈ 0.51877452, 0.51945939, 0.52031475, 0.52111991. Un contrôle hors coquille pSg' +0.01 donne B_N≈-0.08798, B_M≈-0.001918. À R, N=M implique numériquement A_N+A_M≈-2239.55324, mais **l'incompatibilité de cette condition de bord reste CONDITIONNELLE à une annulation exacte des jets**, NON démontrée.

**EXÉCUTÉ ET LIMITES :** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m unittest tests.test_hr_b3c3d6_full_original_step58_point_probe -v` : **5 unittest PASS, 0 FAIL**, non indépendants, ~13.078 s. Quatre rayons + contrôle négatif + sensibilité à 70 décimales (résidus <1e-60). EDO DOP853 double précision rtol=1e-12, atol=1e-14 ; mpmath 45/70 chiffres pour l'évaluation algébrique. **PAS** de preuve uniforme par intervalle des six coefficients, ni des zéros, dérivées, bords ou Dirac. Le test à 70 décimales n'améliore PAS l'erreur globale du solveur double. Aucun no-go JANUS.

**FICHIERS PUBLIÉS ET RELUS, BLOBS :**
- `numerics/hr_b3c3d6_full_original_step58_point_probe.py` : `4e3c78bbdd09831416bf8699c8e24e99253f955d` (octets identiques au script testé).
- `tests/test_hr_b3c3d6_full_original_step58_point_probe.py` : `c74526a18cdae02ba56da19bd45e77fdd5f355b3` (octets identiques au test exécuté).
- `research/reports/gate2b-b3c3d6-original-step58-numeric-summary.json` : `4f1ca600a29cd6d8d029d4435a984a2e2120772f` (identique au résumé local).
- `research/STEP68AD_B3C3D6_ORIGINAL_STEP58_FOUR_POINT_NUMERICAL_PROBE.md` : `890498d02e07b6ee2981e20aa1fb6f4dcd6af0aa`.
- `README.md` : `9cda72a733daf4823595f0b03e05b733e4a110bf`.

**SOURCES ORIGINALES GIT BLOBS :** Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55-normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55-barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. HEAD de reprise `5e024cf16d967a7517180fe65bacf09bf0cbebbe`. main initial `aead63f4098f0d15a849e579105af034b6317b30` ; research/v2-flrw initial `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow touché. **TOUT L'HISTORIQUE ANTÉRIEUR CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : COQUILLE PRIMAIRE STEP55 VÉRIFIÉE ALGÉBRIQUEMENT (2026-10-29)

**STATUT INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 PARTIELLE.** PROCHAINE ÉTAPE : exécuter le vrai probe original Step58 sur la solution radiale complète Step55 à R=17/20, avec jets pLf de l'EDO, les six coefficients A_N/A_M/B_N/B_M/E_N/E_M et leurs dérivées/zéros/cartes/raccord centre, lapses strictement positifs et DEUX bords physiques ; ensuite vrai pullback Dirac, charges/générateurs, quotient jauge temporelle, six couples/rang/tertiaires, K=0/J=0, 4D/stabilité/observables.

**AVANCÉE EXACTE MAIS RESTREINTE :** transcription indépendante des définitions Step45 et Step55 (blobs originaux authentifiés par lecture GitHub) : pLg'=r Gprime ; Dg=r*s*Dbar ; K=s*m2*Mg2*Lg*Lf*T ; Fz=0 ; identité de courbure -Lg-Sg'^2/Lg+2(Sg*Sg'/Lg)'=-s*Lg^3*Rg/2 ; la densité rho_g prescrite annule exactement Hg=Ag-Bg'=0 pour r>0. Combinée avec le certificat Step58 des plus hauts jets REJOUÉ PRÉCÉDEMMENT, E_M=0 sur Fz=0 et E_N=(z²-1)*Hg/(Lg*Lf), cette vérification établit E_N=E_M=0 sur la géométrie prescrite Step55 régulière. Au bord R=17/20, facteur (z²-1)/(Lg*Lf)=-9999884400000000000000000000000000000000/926432894764182404865494596893754186181 entre -11 et -10 ; ce n'est PAS un E_N non nul. La vérification ne dépend pas de la solution pLf, et ne prouve ni Hf, ni C=0, ni la préservation temporelle complète.

**TESTS RÉELLEMENT EXÉCUTÉS DANS CETTE SESSION :** `cd /mnt/data/janus_shell_audit && PYTHONPATH=. python -m unittest discover -s tests -v` : 4 unittest PASS non indépendants, 0 FAIL final ; `python step55_primary_shell_audit.py` : 9 résidus SymPy nuls, 2 contrôles négatifs, facteur extérieur rationnel exact. Un test négatif intermédiaire a échoué à cause d'une simplification de racines SymPy et a été corrigé avant la publication finale ; ne pas confondre ce problème de simplification avec une violation physique. **Les moteurs Python originaux Step45/55/58 n'ont PAS été exécutés dans cette session**, seules leurs formules transcrites ont été évaluées. Le rejeu original des hauts jets est celui du checkpoint antérieur, et ne doit pas être compté comme test nouveau.

**FICHIERS PUBLIÉS ET RELUS, BLOBS EXACTS :**
- `numerics/hr_b3c3d6_step55_primary_shell_audit.py` : fb12fd707314682faf430d214ab7d805532b1a8b.
- `tests/test_hr_b3c3d6_step55_primary_shell_audit.py` : a661afed0a7dbb1a6519597405c736363e67036a.
- `research/reports/gate2b-b3c3d6-step55-primary-shell.json` : c758db69390d93b8e5b63c2caa789d35bca80233.
- `research/STEP68AD_B3C3D6_STEP55_PRIMARY_SHELL_AUDIT.md` : fe25ff7a8aa0c1aa7f94015f19c390efc38bfe35.
- `README.md` préfixé sans perte, blob e54a0e9924124942eb44ef18b2b9118fa38bed4c.

**PROVENANCE :** HEAD initial branche autorisée 8a9f844136d9cee85788daac6bec86bd33afd525 ; sources originales Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e, Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe, Step58 802c23aebd41780d8c462f1aa1711707fe4ee88f. main initial aead63f4098f0d15a849e579105af034b6317b30 ; research/v2-flrw initial dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb. Aucun workflow modifié. **TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : REJEU ORIGINAL STEP45+STEP58 DES PLUS HAUTS JETS (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED. b3c3d6 reste PARTIELLE. PROCHAINE ÉTAPE :** vrai probe ORIGINAL Step58 sur le profil complet Step55 à R=17/20, coefficients A_N/A_M/B_N/B_M/E_N/E_M et dérivées, zéros, cartes et raccord centre, lapses positifs et les deux vrais bords ; ensuite Dirac/charges/générateurs/quotient jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables.

**AVANCÉE RÉELLEMENT EXÉCUTÉE :** octets originaux Step45 (Git blob 66aa43841dccfe4a5d586a49be9c10af3a67a10e, 5657 octets) et Step58 (Git blob 802c23aebd41780d8c462f1aa1711707fe4ee88f, 7314 octets) reconstruits et SHA Git vérifiés localement. Le module Step58 ORIGINAL a été exécuté avec SymPy (physical_operator + highest_lapse_certificate) via shim MINIMAL d'import Step57, PAS Step57 complet. Sur Fz=0, E_M=0 et E_N=(z²-1)Hg/(Lg Lf) ; donc E_N=E_M=0 sur Fz=Hg=0. Les coefficients d'ordres 0,1 ne sont PAS certifiés sur Step55. Le facteur géométrique Step55 TRANSCRIT à R=17/20 vaut exactement -9999884400000000000000000000000000000000/926432894764182404865494596893754186181, compris entre -11 et -10. Ceci est le FACTEUR de Hg, non une évaluation de E_N hors coquille.

**TESTS RÉELLEMENT EXÉCUTÉS :** `PYTHONPATH=. python -m numerics.hr_step58_temporal_operator` PASS (manifest original Step58, deux secteurs, ordres 0/1/2, certificat haut jet) ; `PYTHONPATH=. python -m numerics.hr_b3c3d6_authentic_step58_highjet_replay` PASS ; `PYTHONPATH=. python -m unittest discover -s tests -v` : 4 unittest PASS non indépendants, 0 FAIL. Test exécuté sur les octets identiques au code publié, SHA Git du code et du test contrôlés localement et via relecture connecteur. Le réseau Git local échoue par DNS ; connecteur GitHub lecture/écriture fonctionne.

**FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS SUR LA SEULE BRANCHE AUTORISÉE :**
- `numerics/hr_b3c3d6_authentic_step58_highjet_replay.py` blob f1f69b857eef98edbdcde60bbd12b1412ecc5998, commit 5a77e81fc9494993a97d3c75654000808e0008d7.
- `tests/test_hr_b3c3d6_authentic_step58_highjet_replay.py` blob 89abf9355b6e07d05ab206e194eedef5c2f2f7f8, commit a7dc77dfd2edab0109c15585b4822094619cc590.
- `research/reports/gate2b-b3c3d6-authentic-step58-highjet-replay.json` blob ea50fbbb9ee4535780f8d33a93f6d1861562f06b, commit 9014ae61258bd815314416a58713287ad290bdc3.
- `research/STEP68AD_B3C3D6_AUTHENTIC_STEP58_HIGHJET_REPLAY.md` blob a626483d8e7afa07417ecf37d1af8aecbdfdc2ce, commit 2d31b328c68ec2c26c60ae1e29a31b1a0cc91035.

**PROVENANCE :** HEAD de reprise 7f6ed649bd9bba5d2362f41b091a836e3851e32f ; HEAD après quatre livrables 2d31b328c68ec2c26c60ae1e29a31b1a0cc91035. Branches interdites au début main=aead63f4098f0d15a849e579105af034b6317b30 et research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb. AUCUN workflow touché. Le vrai probe Step58 R=17/20 sur Step55 COMPLET, les six coefficients et leurs dérivées, la preuve de lapses positifs et la tangence Dirac restent NON EXÉCUTÉS. Ce rejeu partiel ne doit PAS être annoncé comme résolution de b3c3d6.

**HISTORIQUE INTÉGRAL ANTÉRIEUR CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : COEFFICIENT ETA''*N STEP57 SUR STEP55 (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** b3c3d6 reste PARTIELLE. **PROCHAINE ÉTAPE PRIORITAIRE INCHANGÉE :** exécuter réellement le probe original Step58 sur Step55 à `R=17/20`, sources originales Step45/55/57/58/Step68o/b3c2 SHA-authentifiées ; certifier `A_N,A_M,B_N,B_M,E_N,E_M`, leurs dérivées, signes/zéros, cartes, raccord centre, vrais lapses strictement positifs et DEUX bords physiques. Ensuite pullback Dirac, charges/générateurs, quotient de jauge temporelle, six couples/rang/tertiaires, K=0/J=0, 4D/stabilité/observables.

**AVANCÉE SCIENTIFIQUE EXACTE, RESTREINTE :** le terme manquant `eta''*N` du symbole fonctionnel smeared Step57 a été réduit à `c_N=-(1-z²)/(Lg*Lf)*T_N0` sur `Fz=0,K>0`, avec `T_N0=kg+pg/sqrt(1+tg'^2/Lg²)-Mg2*Lg+Mg2*Sg'^2/Lg+m2*Mg2*Lg*(beta0*Sg²+2*beta1*Sg*Sf+beta2*Sf²)` et `kg=Lg*pLg²/(4*Mg2*Sg²)-pLg*pSg/(2*Mg2*Sg)`. Les termes explicites en z s'annulent dans T_N0 ; le facteur global `1-z²` reste. En transcrivant exactement la géométrie Step55 et en appliquant 256 cellules rationnelles sortantes de `s=r² in [0,289/400]` (grille `10^-28`), on certifie `6<c_N/r²<7`, `c_M/r²<-10`, `c_Nprime/r<-17/2` sur `0<r<=17/20`, avec `1/Lf` CORRECT dans `c_Nprime`. Les bornes et leurs fractions exactes figurent dans le JSON.

**POINT CRITIQUE DE LOGIQUE :** pour lapses pairs C² `N=N0+N2*r²+o(r²)`, `M=M0+M2_lapse*r²+o(r²)`, la seule annulation formelle du coefficient de `eta''` impose `cN2*N0+cM2*M0+2*cNp1*N2=0` au premier ordre non nul. Le terme `c_Nprime*N'` contribue au MÊME ordre `r²`. Si on ajoute conditionnellement la bande centrale b3c2 Step58 `1037/2000<M0/N0<2593/5000`, la courbure requise est `1/25<N2/N0<1/20`, sans contradiction au premier ordre. Ne JAMAIS imposer séparément cette annulation smeared comme une équation physique Dirac sans les intégrations par parties et le vrai opérateur local Step58. L'ancien écran de deux termes et son ratio `M0/N0<804/2249` sont INVALIDES ; le correctif antérieur `1/Lf` reste obligatoire. Le résultat actuel n'établit ni un no-go ni un lapse global.

**TESTS RÉELLEMENT EXÉCUTÉS LOCAL :** `cd /mnt/data/janus_eta2_n && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step57_full_eta2_N` : 3 résidus SymPy exacts nuls, 1795 gardes rationnelles (256 cellules, 3 au centre), 0 FAIL. `PYTHONPATH=. python -m unittest discover -s tests -v` : 5 unittest PASS, non indépendants, 0 FAIL. Sources Step45 blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step57 `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f` lues en direct via connecteur GitHub. **Moteurs originaux Step45/55/57/58 et probe Step58 R=17/20 NON exécutés** (DNS Git local indisponible). Preuve à partir d'une transcription algébrique et de données Step55 prescrites ; tests non indépendants.

**QUATRE FICHIERS SCIENTIFIQUES CRÉÉS SUR LA SEULE BRANCHE AUTORISÉE, PUBLIÉS ET RELUS (BLOBS IDENTIQUES AUX OCTETS LOCAUX POUR CODE/TEST/JSON) :**
- `numerics/hr_step68ad_b3c3d6_step57_full_eta2_N.py` blob `1ae6a933f9389afc57bb2ecc1c28bdf611b14eb9`, commit `7b633b175b8aeaed2d321c3eec90d4d6b3720139`.
- `tests/test_hr_step68ad_b3c3d6_step57_full_eta2_N.py` blob `e2ac46f34b736694a38898b81aa5008ea8cfafa6`, commit `90a7273d7f7c0b53acbbf37398cce1b11d5ebe03`.
- `research/reports/gate2b-step68ad-b3c3d6-step57-full-eta2-N.json` blob `3403cef30d7741fab11d83c195a73f0f379dcdc9`, commit `daf29a76b43aaff61225edcc7c0b886fecd2e02f`.
- `research/STEP68AD_B3C3D6_STEP57_FULL_ETA2_N_COEFFICIENT.md` blob `a117beda9ebd939958fce1bd1bda04952d2a91d4`, commit `aaa168cffb6821612bd39c117a3dda4c0f80b648`.
- `README.md` préfixé, blob `c912dbd7aa925a0ddb7f88aeecce78bc5ca1e9b9`, commit `e04cff86fe24b9b8063ca3d88b530f66cb0b8f9b`.

**PROVENANCE :** HEAD branche au démarrage `6b31fcc5c82e387f5d63070d0d70d44f0dfe2b7d`; HEAD après README `e04cff86fe24b9b8063ca3d88b530f66cb0b8f9b`. Branches interdites au démarrage `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` ; revérifier après mise à jour de l'index. Aucun workflow modifié. **HISTORIQUE INTÉGRAL PRÉEXISTANT CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : BORNE UNIFORME STEP57 CORRIGÉE (2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Étape b3c3d6 toujours PARTIELLE ; prochaine action prioritaire inchangée : **exécuter le probe original Step58 sur Step55 R=17/20**, avec Step45/55/57/58/Step68o/b3c2 SHA-authentifiés, certifier les six coefficients A_N,A_M,B_N,B_M,E_N,E_M, dérivées, zéros, cartes et raccord au centre, lapses strictement positifs et les deux véritables bords ; ensuite Dirac six couples/rang/tertiaires, charges/générateurs, quotient de jauge temporelle, K=0/J=0, dynamique 4D, stabilité et observables.

**AVANCÉE EXACTE MAIS STRICTEMENT RESTREINTE :** après correction de l'omission historique de `1/Lf` dans le coefficient `eta''*N'` original Step57, et relecture de `Sg=r*Lg` sur Step55, on démontre pour `0<r<=17/20` : `c_Nprime(r)<-(17/2)r`. Identité exacte : avec `s=r²`, `B=(2/5)*(5787707228025044/10^16)`, `ug=1+3s/2000`, `uf=1-3s/2500`, `-c_Nprime/r=2(1+15s/2000)(1-s/62500)/(B*ug*uf²)`. Les bornes rationnelles `B<7/30`, `ug<501/500`, `uf²<=1`, `1-s/62500>9999/10000` donnent `-c_Nprime/r>1666500/195223>17/2`. Limite centrale exacte `-12500000000000000/1446926807006261` contre `-2` dans les anciens scripts. La borne faible ancienne `c_Nprime<-(19999/10000)r` reste vraie, mais son ancienne formule et son certificat dérivé ne sont PAS valides. L'ancienne borne de ratio `M(0)/N(0)<804/2249` reste INVALIDÉE. Le terme `eta''*N` n'est pas évalué : ce n'est ni le symbole complet, ni Step58, ni Dirac, ni un no-go JANUS.

**EXÉCUTÉ LOCAL :** `cd /mnt/data/janus_20261029 && PYTHONPATH=. python -m numerics.hr_b3c3d6_step57_corrected_uniform_bound` : 5 résidus SymPy exacts nuls, 10 gardes rationnelles PASS, 0 FAIL ; `PYTHONPATH=. python -m unittest discover -s tests -v` : 5 unittest PASS, non indépendants, 0 FAIL. Une erreur de reconstruction intermédiaire `Sg/r=A*ug` a été détectée et corrigée en `Sg/r=Lg=A*ug²` avant publication scientifique finale. Les expressions originales Step57 (blob bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f) et Step55 (blob a6e7004120d0a166a3a8973c2fbe1487a8eb70fe) ont été lues en direct. **Moteurs originaux Step45/55/57/58 et vrai probe Step58 R=17/20 NON exécutés** : `git ls-remote` échoue par DNS local, malgré GitHub connector opérationnel.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS, SHA BLOBS ÉGAUX AUX OCTETS LOCAUX :**
- `numerics/hr_b3c3d6_step57_corrected_uniform_bound.py` : `cac0932de7c3ac35a3866963334e2daee6a85b0b`.
- `tests/test_hr_b3c3d6_step57_corrected_uniform_bound.py` : `3ed48cd774a154a40f8418f6f35661bc6ca86a64`.
- `research/STEP68AD_B3C3D6_STEP57_CORRECTED_UNIFORM_SIGN.md` : `deda3eb7d6839c6a89ac4ebe05621a68a9ac47ca`.
- `research/reports/gate2b-b3c3d6-step57-corrected-uniform-sign.json` : `7bffa9b29e0721035a7dda6098d7c4f96cd561e6`.
- `README.md` préfixé, blob `47d60eacc2314b66ed963219c214f6d7584d2000`.

**PROVENANCE :** HEAD GitHub de reprise `daa5b5c9d43f171c96ef26b408c4dce3cf332a7c` ; HEAD après README `3c91d13bf46cae5bdd336290cae5120c2c4a2d37`. Branches interdites vérifiées inchangées avant checkpoint : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. L'intégralité de l'historique est conservée ci-dessous.

---

# JANUS — CHECKPOINT CORRECTIF b3c3d6 PARTIEL : ERREUR FACTEUR 1/Lf STEP57 (2026-10-29)

**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 TOUJOURS PARTIELLE.** PRIORITÉ INCHANGÉE : vrai probe original Step58 sur Step55 R=17/20, avec Step45/55/57/58/Step68o/b3c2, A_N/A_M/B_N/B_M/E_N/E_M et dérivées/zéros/cartes/raccord centre, lapses positifs avec les deux vrais bords ; ensuite vrai Dirac/charges/générateurs/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables.

**ERRATUM SCIENTIFIQUE MAJEUR, PROUVÉ SUR LES EXPRESSIONS ORIGINALES :** le moteur original Step57 (blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`) donne le coefficient `eta''*N'` égal à `-2*Mg2*Sg*Sg'*(1-z²)/(Lg²*Lf)` sur Fz=0,K>0. Deux scripts dérivés b3c3d6 avaient OMIS `1/Lf`. Le coefficient `eta''*M` précédent était correct. Donc `lim c_Nprime/r=-2/Lf(0)≈-8.63899952608`, PAS `-2` ; l'ancien `q=c_M/c_Nprime` est trop grand d'un facteur `1/Lf` ; l'ancienne borne `q>1000r/201` est FAUSSE. Les anciennes valeurs centrales et l'ancien écran `M(0)/N(0)<804/2249` sont INVALIDÉS, bien que la borne de signe grossière `c_Nprime<-(19999/10000)r` reste vraie.

**PREUVE CORRIGÉE STRICTEMENT RESTREINTE :** `q_correct=Lf*q_ancien=m2*r*T(r²)*(1+cg*r²)/(2*(1+5cg*r²)*sqrt(1-r²/62500))`. Bernstein exact `53/500<T<109/1000`, `m2<24`, `sqrt(1-r²/62500)>99999/100000` donnent `int_0^(17/20) q<1/2`. Pour `M=1,N(R)=1` et annulation des DEUX termes `c_M*M+c_Nprime*N'=0`, `M(0)/N(0)>2/3>2593/5000` : incompatibilité avec le ratio central conditionnel b3c2, **DANS LE SENS OPPOSÉ** à la conclusion antérieure. Quadrature illustrative `M(0)/N(0)≈0.68938800746505`. Le coefficient `eta''*N` RESTE présent, non annulé : ce n'est PAS le symbole complet, PAS Step58, PAS Dirac, PAS un no-go JANUS. Source Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 contexte `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

**TESTS LOCAUX RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_erratum && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step57_lf_erratum` : 10 résidus exacts nuls, 15 assertions Python exactes (dont cinq coefficients Bernstein et leurs quatre différences), 0 échec final ; `PYTHONPATH=. python -m unittest discover -s tests -v` : 5 unittest PASS, non indépendants, 0 FAIL final. Un premier échec de simplification de racines et un échec de comparaison structurelle ont été corrigés avant publication. Moteurs originaux et probe Step58 R=17/20 NON exécutés (DNS local Git inaccessible) ; code original Step57 inspecté en direct via GitHub.

**LIVRABLES NOUVEAUX PUBLIÉS SUR LA SEULE BRANCHE AUTORISÉE, 4/4 BLOBS RELUS ET IDENTIQUES AUX OCTETS LOCAUX :**
- `numerics/hr_step68ad_b3c3d6_step57_lf_erratum.py` blob `6306a80963ca2091558cc15f41977b7489a897b8`, commit `a42f6448cee04b23f2f6cf23aee2d9e412ce423b`.
- `tests/test_hr_step68ad_b3c3d6_step57_lf_erratum.py` blob `27c177ac5d0202726c018f581a6fd41145f9928f`, commit `46a686b5241ed90b08d61a9d270efd9ea2673ae6`.
- `research/STEP68AD_B3C3D6_STEP57_NPRIME_LF_ERRATUM.md` blob `37b2bbd00007fc730c1a6de4eb005c193b2d68dd`, commit `7cfac810572cfafebb4998de29e6b1bbc7b72c33`.
- `research/reports/gate2b-step68ad-b3c3d6-step57-lf-erratum.json` blob `99ed5030c00c8e778daaaf385e8feea525439fff`, commit `300edd93c6d73f0746644453ba2381d28be3d064`.
- `README.md` préfixé avec avertissement, blob `90db49bfb8d1accf3573ddc3b4e2e7d3f97a4007`, commit `1bf2735174ca48cfba9b573c472a8106ca0f07cb`.

**PROVENANCE :** HEAD initial GitHub `744be4b5cb867807b75d80ed61d442fdf02b53ad`. Les fichiers historiques erronés sont conservés intacts pour audit, mais leur interprétation est explicitement remplacée par cet erratum. Aucun workflow GitHub modifié. Branches interdites au démarrage main=`aead63f4098f0d15a849e579105af034b6317b30`, research/v2-flrw=`dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` ; à revérifier en fin de session. Historique intégral conservé ci-dessous.

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : ÉCRAN DE COMPATIBILITÉ CENTRALE D'UNE ANNULATION PARTIELLE STEP57 (2026-10-29)

**ÉTAT SCIENTIFIQUE INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED. Étape b3c3d6 PARTIELLE.** Prochaine étape prioritaire INCHANGÉE : vrai probe original Step58 sur Step55 à R=17/20 (sources Step45/55/57/58/Step68o/b3c2 authentifiées), A_N,A_M,B_N,B_M,E_N,E_M, signes/zéros/dérivées et raccord central, lapses strictement positifs avec les deux vrais bords, puis pullback Dirac, charges/générateurs, jauge temporelle, six couples/rang/tertiaires, K=0/J=0, dynamique 4D/stabilité/observables.

**NOUVEAU RÉSULTAT EXACT MAIS TRÈS RESTREINT :** sur le profil géométrique prescrit Step55, K>0 pour 0<r<=17/20, les deux contributions du symbole smeared Step57 `eta''*M` et `eta''*N'` ont coefficients négatifs c_M<-10r² et |c_Nprime|<201r/100. Leur quotient q=c_M/c_Nprime >1000r/201. Dans la SOUS-FAMILLE M(r)=1, N(R)=M(R)=1, l'annulation des **deux seules contributions** c_M M+c_Nprime N'=0 impose N(r)=1+int_r^R q(t)dt, donc N(0)>2249/804 et M(0)/N(0)<804/2249<1037/2000. Cela contredit le ratio central b3c2 >1037/2000 **si l'on impose simultanément les hypothèses Step58 de ce ratio**. La construction N,M est positive, régulière, paire, mais NE satisfait PAS le ratio Step58. **CRUCIAL : le coefficient eta''*N original Step57 reste présent et non évalué ; il ne s'agit PAS de l'annulation du symbole complet, ni d'un no-go physique, ni d'un probe Step58.** Quadrature illustrative (non utilisée dans la preuve) : int q≈1.94788402529054, ratio≈0.33922637099.

**TESTS RÉELLEMENT EXÉCUTÉS EN LOCAL :** dans /mnt/data/janus_b3c3d6_bridge : `PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_two_term_cancellation` (6 résidus SymPy exacts nuls et 7 assertions de garde rationnelle PASS) ; `PYTHONPATH=. python -m unittest discover -s tests -v` (4 cas PASS, non indépendants, 0 FAIL) ; une quadrature mpmath informative. **Aucun moteur original Step45/55/57/58/Step68o/b3c2 ni probe Step58 R=17/20 exécuté.** Git local `git ls-remote` et curl échouent faute de réseau/DNS ; connecteur GitHub lecture/écriture fonctionne.

**LIVRABLES PUBLIÉS ET RELUS (4/4 SHA blob identiques aux octets locaux) :**
- `numerics/hr_step68ad_b3c3d6_two_term_cancellation.py` blob `461509a67b04eab4481e7411117b92ee1072ba38`, commit `bc6da1caee65b86d3b74dffa3ad08ce95207d58c`.
- `tests/test_hr_step68ad_b3c3d6_two_term_cancellation.py` blob `66951e464736c53a114d6d36d74d54c4993ef309`, commit `c23b10450330d4d3b5b76edbbc8ed0359a53a6d8`.
- `research/STEP68AD_B3C3D6_STEP57_TWO_TERM_CANCELLATION_CENTER_SCREEN.md` blob `96cbfdf10c657a2c6eed9068b384bba907c076fc`, commit `dbc90a1ab1460a176f28f1e5fbf1e9491ab2567f`.
- `research/reports/gate2b-step68ad-b3c3d6-two-term-cancellation.json` blob `2d225047cce91622bb8943661a945f26a03769d6`, commit `da5c27adb88f45dc9c6bb8cdb030d82722f301e2`.
- `README.md` blob `b3021e6e7b6f3b3d4ce324561445f2975330a2b6`, commit `b8cdc3c96775620325f832f928c524b1eae0d2a1`.

**PROVENANCE :** branche au démarrage `bed90a2f1493aee42737cd5856b8471ba41d8271`. Sources Step55 blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step57 `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Branches interdites au démarrage main=`aead63f4098f0d15a849e579105af034b6317b30`, research/v2-flrw=`dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` ; recontrôler après mise à jour de l'état. Aucun workflow modifié. Le présent checkpoint est préfixé ; tout l'historique précédent reste intact.

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : SIGNE UNIFORME DU SYMBOLE FONCTIONNEL STEP57 SUR STEP55 (2026-10-29)

**STATUT INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED. ÉTAPE EFFECTIVE b3c3d6 TOUJOURS PARTIELLE. PROCHAINE ÉTAPE b3c3d6 : exécuter le vrai probe original Step58 à R=17/20 sur Step55 avec les sources Step45/55/57/58/Step68o/b3c2, certifier A_N,A_M,B_N,B_M,E_N,E_M, dérivées/zéros/cartes/raccord centre, lapses positifs et les deux vrais bords ; ensuite pullback Dirac, générateurs/charges, quotient jauge temporelle, six couples/rang/tertiaires, K=0/J=0, dynamique 4D/stabilité/observables.**

**AVANCÉE EXACTE RESTREINTE (NON DIRAC) :** sur la coquille stationnaire Fz=0, K>0 de la géométrie Step55 prescrite et pour 0<r<=17/20, les coefficients originaux du **symbole fonctionnel smeared Step57** de eta''*M et eta''*N' sont c_M=-K*sqrt(1-z²)/(Lg*Lf²) et c_Nprime=-2*Mg2*Sg*Sg'*(1-z²)/Lg². En combinant la borne Bernstein précédente K/r²>9/40 avec les inégalités rationnelles Step55, **c_M < -10*r²** et **c_Nprime < -(19999/10000)*r** partout hors centre. Limites centrales : c_M/r²≈-10.90817664306727 (fraction exacte dans JSON), c_Nprime/r=-2. Les deux coefficients s'annulent au centre, donc aucun rang uniforme jusqu'à r=0. **Ce ne sont PAS les coefficients B_N,B_M de l'opérateur local Step58 : aucune conclusion sur lapses, tangence Dirac ou rang physique.** Résultat dérivé de formules originales inspectées, non un rejeu indépendant de Step57.

**TESTS RÉELLEMENT EXÉCUTÉS dans /mnt/data/janus_b3c3d6_20261029 :** PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step55_dirac_principal_sign : 14 assertions exactes PASS, 0 FAIL final. PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_step55_dirac_principal_sign.py' -v : 5 tests PASS non indépendants, dont garde négative de SHA. Une erreur initiale de transcription locale s=r² a été détectée et corrigée avant publication et tests finaux. **Moteurs originaux Step45/55/57/58/Step68o/b3c2 et vrai probe Step58 R=17/20 NON exécutés** ; git ls-remote échoue par DNS github.com, tandis que connecteur GitHub lit et écrit correctement.

**QUATRE LIVRABLES SCIENTIFIQUES CRÉÉS SUR LA SEULE BRANCHE AUTORISÉE, RELUS :**
- numerics/hr_step68ad_b3c3d6_step55_dirac_principal_sign.py — blob 43095132bd334a820e56b987ad196841433dcef0, commit c802c708c94704ee79d9d4cdc9f77492134c0a3f.
- tests/test_hr_step68ad_b3c3d6_step55_dirac_principal_sign.py — blob 21f3af2775efe21df1e65611722d1c1820b725fe, commit 791a68fa7d27519601ee3b5f59d9a1121868a58a.
- research/STEP68AD_B3C3D6_STEP55_STEP57_UNIFORM_PRINCIPAL_SYMBOL_SIGN.md — blob fc32d8c66f882bd16c6a2a3341e41f743390f339, commit 0beaf08f3ca688b06a0e70cecfd698a723044086.
- research/reports/gate2b-step68ad-b3c3d6-step55-step57-principal-sign.json — blob 09e1ac20c0aa97358fa3b9be661722958b30c344, commit 2f1aac45a25a15cd98bbb830092fbc9745faddf3.
- README.md index préfixé — blob 4223e5ccc2d666a6ab8d381a447a869207b28358, commit cac7ac3f865c4735df35d39fd7c4183ecdc290bc.
Les quatre SHA blobs publiés ont été relus via GitHub et comparés aux SHA des octets exécutés/produits localement : 4/4 MATCH. Sources originales inspectées en direct : Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe ; Step57 bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f ; Step58 802c23aebd41780d8c462f1aa1711707fe4ee88f. HEAD de branche au démarrage 95dd5d3f817329c049cf15504f53897e01a159aa ; avant ce checkpoint cac7ac3f865c4735df35d39fd7c4183ecdc290bc. Branches interdites au démarrage main=aead63f4098f0d15a849e579105af034b6317b30, research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb ; recontrôler après écriture d'état. Aucun workflow modifié.

**HISTORIQUE INTÉGRAL ANTÉRIEUR CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : CARTE K>0 STEP55 CERTIFIÉE PAR BERNSTEIN (2026-10-29)

**STATUT INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED. PROCHAINE ÉTAPE TOUJOURS b3c3d6 : exécuter le vrai probe original Step58 sur Step55 R=17/20 avec imports Step45/55/58/Step68o/b3c2 ; évaluer A_N/A_M/B_N/B_M/E_N/E_M, dérivées, zéros/cartes/raccord centre, puis compatibilité des lapses positifs et vrais bords ; ensuite Dirac/charges/générateurs/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables.**

**NOUVEAU CERTIFICAT EXACT, DE PORTÉE LIMITÉE :** En reprenant les constantes rationnelles du vrai profil géométrique Step55 (source GitHub blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) et la définition de `K` dans Step58 (blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`), le polynôme quartique `T(s)` possède cinq coefficients de Bernstein strictement positifs et quatre différences consécutives strictement négatives sur `s∈[0,289/400]`. Donc `53/500<T(s)<109/1000`, `K(r)/r²>9/40` sur `0<r<=17/20`, `z(r)=r/250` et `z(17/20)=17/5000<1`. Sur la coquille stationnaire `Fz=0`, `K~c r²`, `D~c' r³` avec `c,c'>0`. **Cela élimine K=0 sur l'anneau Step55 hors centre, mais pas la dégénérescence centrale ; ne dit RIEN sur les zéros de B_N/B_M, la résolution des lapses ni Dirac.** Le signe K>0 était déjà établi par Step54/55 ; valeur ajoutée : borne rationnelle explicite et certificat Bernstein indépendant.

**TESTS RÉELLEMENT EXÉCUTÉS DANS `/mnt/data/janus29` :** `PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step55_k_chart` : 14 assertions groupées exactes PASS (dont 5 signes Bernstein et 4 différences) ; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_step55_k_chart.py' -v` : 4 cas PASS non indépendants, 0 FAIL. Aucun moteur original Step45/55/58/Step68o/b3c2 ni le probe Step58 R=17/20 n'a été exécuté ; `git ls-remote` échoue toujours localement par DNS. Les quatre blobs publiés sont identiques aux octets locaux exécutés/produits, après relecture GitHub.

**LIVRABLES SUR LA SEULE BRANCHE AUTORISÉE :**
- `numerics/hr_step68ad_b3c3d6_step55_k_chart.py` blob `ff53c9ffd813a429dbf2e2c8b772f40dca8c893f`, commit `f2e2227899862f37acb49a4aa601e36918585dc2`.
- `tests/test_hr_step68ad_b3c3d6_step55_k_chart.py` blob `9d9c09fec2e1db6213d11e7d0224766a83639b5d`, commit `9a698dbe7b80f43c46dcaeda665e4b200c06148b`.
- `research/STEP68AD_B3C3D6_STEP55_K_CHART_EXACT_CERTIFICATE.md` blob `10b3e3b6c19cf67cd698c6880448f15cf749eab9`, commit `cf1e4f1149a82cb27b7dd53ed2f68f68f64e8dad`.
- `research/reports/gate2b-step68ad-b3c3d6-step55-k-chart.json` blob `16b6a014943fb56173b9afd2a611e1cb25ac66c6`, commit `dac18bf3280c607f78cb32a8bd9b4d7a6dc03282`.
- `README.md` nouveau blob `cf529a9f4babc28d0bed5b11eff60f4696edd2a5`, commit `73a2609947f400fc37a010887f407d2649471ea9`.

**PROVENANCE :** HEAD de la branche au démarrage `b47ec5325c6f3c50e8b49fea7b593e76cffae3a6`, HEAD avant ce checkpoint `73a2609947f400fc37a010887f407d2649471ea9`. Branches interdites au démarrage `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` ; recontrôler en fin de session. Aucun workflow modifié.

**HISTORIQUE INTÉGRAL PRÉEXISTANT CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : JETS POSITIFS AUX DEUX BORDS (2026-10-29)

**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED. PROCHAINE ÉTAPE TOUJOURS b3c3d6 : exécuter réellement le probe original Step58 sur Step55 R=17/20 avec Step45/55/58+b3c2/Step68o ; certifier B_N/B_M, dérivées, zéros/cartes/raccord centre, b,d, vrais lapses positifs et les deux bords physiques ; puis pullback Dirac, générateurs/charges, quotient jauge temporelle, six couples, K=0/J=0, 4D/stabilité/observables.**

**AVANCÉE EXACTE CONDITIONNELLE (NON PHYSIQUE) :** extension du théorème de faisabilité des quatre amplitudes aux **huit valeurs et dérivées de N,M aux deux bords** pour UNE équation scalaire `A_N N+A_M M+B_N N'+B_M M'=0`, `E_N=E_M=0` exactement, `B_N,B_M>0` C1 sur anneau compact et `A_N,A_M` continus. Avec `u=B_N N+B_M M`, `s_i=(B_i'-A_i)/B_i`, `T=log(u_R/u_0)`, `L=∫min(s_N,s_M)`, `U=∫max(s_N,s_M)`, la solution C1 positive aux **huit jets prescrits** existe ssi : (i) l'équation scalaire est satisfaite aux deux bords par les jets imposés ; (ii) `L<T<U` si les pentes diffèrent quelque part, sinon `T=∫s_N`. Preuve par `w=B_M M/u` strictement entre 0 et 1, avec **valeurs ET dérivées de w** prescrites aux deux extrémités, interpolation de Hermite en couches de bord, sélecteurs min/max et combinaison convexe. Aucune contrainte additionnelle de jets finis n'apparaît pour ce problème scalaire ; **ceci n'est ni Step55, ni Step58 complet, ni Dirac.**

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_derivative && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_endpoint_jet_reachability` : 10 résidus SymPy exacts nuls (dont définitionnels), 12 contrôles jouets/gardes exacts PASS. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_endpoint_jet_reachability.py' -v` : 4 tests PASS, non indépendants, 0 FAIL. Jouet analytique `B_N=B_M=1,A_N=0,A_M=-1,N=M=exp(r/2)` ; témoin d'incompatibilité des dérivées `N'(0)=M'(0)=0` malgré quatre amplitudes compatibles. Tests ne remplacent pas la preuve générale.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS, RELUS, SHAS :**
- `numerics/hr_step68ad_b3c3d6_endpoint_jet_reachability.py` blob `802fc250f854fc71c6ed7486db29fad9206abc9c`, identique aux octets exécutés ; commit `8c8065895988f3d7a5cd14dde6cc4f40b94d70e1`.
- `tests/test_hr_step68ad_b3c3d6_endpoint_jet_reachability.py` blob `19d2ef606d182db1139e1ecf8ee389f7faae298a`, identique aux octets exécutés ; commit `22da5d3229963c7e4a768df34f6550b96e91090c`.
- `research/STEP68AD_B3C3D6_ENDPOINT_JET_REACHABILITY.md` blob `ead41a5f16378944bd70f8e65f08c6f5f09f2d6b` ; commit `8ccb63910224ddfc66a551fcb633465e1658f653`.
- `research/reports/gate2b-step68ad-b3c3d6-endpoint-jet-reachability.json` blob `a893c7e5cfb242151e123579545e6f947135869b` ; commit `948936da7576a0db1c2c1098d66448c828298253`.
- `README.md` blob `4c34edb7bf12ff9a3e5dd7193a595eb62b40ab55` ; commit `d581eb0c77dd64deb6c5f6b020f53eb9512c0762`.

**PROVENANCE ET VERROUS :** HEAD GitHub au démarrage `5805344a22285df9ed79ab792899c557568ffa4f` (plus récent que le repère utilisateur `3172febd...`). Sources authentiques lues via connecteur : Step58 blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`, probe b3c3d5 `85469568e6df7c26920c1ebb87593dbf474deb04`. `git ls-remote` local : `Could not resolve host: github.com`. **Vrai probe original Step58 R=17/20 et moteurs complets Step55/Step68o/b3c2 NON exécutés** ; aucun signe physique B_N/B_M ni BVP Dirac certifié. Branches interdites au démarrage : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` (à recontrôler en fin de session). Aucun workflow modifié.

**HISTORIQUE INTÉGRAL PRÉEXISTANT CONSERVÉ CI-DESSOUS.**

---

# JANUS — CHECKPOINT b3c3d6 PARTIEL : AMPLITUDES POSITIVES AUX DEUX BORDS (2026-10-28)

**STATUT INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED. PROCHAINE ÉTAPE : b3c3d6, exécuter réellement le probe original Step58 sur Step55 R=17/20, Step45/55/58+b3c2/Step68o, certifier B_N/B_M, leurs dérivées, zéros/cartes/raccord centre, b,d, lapses positifs et les deux bords physiques ; puis Dirac, générateurs/charges, quotient jauge temporelle, six couples, K=0/J=0, 4D/stabilité/observables.**

**AVANCÉE EXACTE CONDITIONNELLE NON PHYSIQUE :** Le problème à quatre valeurs aux deux bords pour **une seule** équation du premier ordre `A_N N+A_M M+B_N N'+B_M M'=0`, avec `E_N=E_M=0`, `B_N,B_M>0`, est maintenant caractérisé exactement. En posant `u=B_N N+B_M M`, `s_i=(B_i'-A_i)/B_i`, `L=int min(s_N,s_M)`, `U=int max(s_N,s_M)`, `T=log(u_R/u_0)`, et si `s_N-s_M` n'est pas identiquement nul, il existe une paire de lapses strictement positifs C1 avec les **quatre valeurs terminales prescrites** si et seulement si `L<T<U` ; les égalités sont impossibles. Si `s_N=s_M` partout, `T=int s_N` est nécessaire et suffisant. Preuve constructive par le poids libre `w=B_M M/u in (0,1)`, `u'/u=(1-w)s_N+w s_M`, approximation des sélecteurs min/max, puis combinaison convexe pour atteindre toute amplitude intérieure. **Ceci améliore l'écran précédent de nécessité en condition suffisante stricte, mais n'est PAS une preuve Step55, Step58 complet ou Dirac.**

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_28 && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_sharp_amplitude_reachability` : 5 résidus symboliques exacts, 11 résidus jouets exacts, 2 contrôles de bornes PASS ; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_sharp_amplitude_reachability.py' -v` : 4 tests PASS non indépendants, 0 FAIL. Familles jouets B constants et B variables, toutes deux strictement positives ; aucune substitution au vrai profil Step55.

**LIVRABLES PUBLIÉS SUR LA SEULE BRANCHE AUTORISÉE, RELUS ET HASHÉS :**
- `numerics/hr_step68ad_b3c3d6_sharp_amplitude_reachability.py` blob `957f6f364eee5fc5f24eaca12de9373886ad098d` ; commit `20b9fbf4aa6897a72ca5c7c1d2ffbacea8849640` (octets exécutés = blob).
- `tests/test_hr_step68ad_b3c3d6_sharp_amplitude_reachability.py` blob `9cde2037e13c55f440af9e653d00bf7bdc053b93` ; commit `10a37695408ea00195eb730cc6c1d891d85e6abd` (octets exécutés = blob).
- `research/STEP68AD_B3C3D6_SHARP_POSITIVE_AMPLITUDE_REACHABILITY.md` blob `3efb2633df0e394ebace9f0a0b53db1e6bcc271b` ; commit `f62c5885c0d558b763ebe3d98e8db1d121b0f05a`.
- `research/reports/gate2b-step68ad-b3c3d6-sharp-positive-amplitude-reachability.json` blob `574eb38c01f8bb5117551532f7175f4bc293d0ae` ; commit `9ef3ac99538f169b60b78670a129e0b6a83fac99`.

**PROVENANCE ET LIMITES :** HEAD GitHub au démarrage `92591ab6b68e69a3007a03bdbb4384f57e0cc649`. Sources authentiques lues via connecteur : Step58 blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, probe Step58 publié dans b3c3d5 blob `85469568e6df7c26920c1ebb87593dbf474deb04`. DNS local `api.github.com`/`raw.githubusercontent.com` non résolu ; **vrai probe Step58 R=17/20 et Step55/Step68o/b3c2 NON exécutés**. Aucune information physique sur les signes de B_N/B_M ni les bords déduite du théorème. Branches interdites au démarrage `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. Recontrôler HEAD et branches après index.

**HISTORIQUE INTÉGRAL PRÉEXISTANT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, ATTEIGNABILITÉ CONSTRUCTIVE DU RATIO TERMINAL (2026-10-28)

**PROCHAINE ÉTAPE INCHANGÉE :** exécuter le vrai probe original Step58 sur le profil Step55 à `R=17/20`, en important les vrais Step45/55/58, b3c2 et Step68o ; certifier les coefficients `B_N,B_M` et leurs dérivées, zéros/cartes et raccord central, coefficients `b,d`, existence de lapses strictement positifs avec **toutes** les conditions aux deux bords ; ensuite vrai pullback Dirac, charges/générateurs, jauge temporelle, six couples/rang/tertiaires, K=0/J=0, dynamique 4D, stabilité et observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE MATHÉMATIQUE EXACTE, CONDITIONNELLE ET NON PHYSIQUE :** Pour l'unique équation `A_N N+A_M M+B_N N'+B_M M'=0` sur un anneau `[r0,R]`, `r0>0`, coefficients continus et `B_N,B_M>0` partout, toute donnée initiale `N0,M0>0` peut atteindre n'importe quel ratio final `M(R)/N(R)=kR>0`, si **aucune amplitude finale** n'est prescrite. Prendre une interpolation `k(r)>0` de `M0/N0` à `kR`, puis `N=N0 exp[-int (A_N+A_M k+B_M k')/(B_N+B_M k)]`, `M=kN`. Le dénominateur est strictement positif et les deux lapses le restent. Les coefficients analytiques et `k` analytique donnent des lapses analytiques. Le théorème ne couvre ni les signes opposés/zéros communs, ni le centre dégénéré, ni la présence de `E_N N''+E_M M''`, ni les autres contraintes. Il montre que l'écran de croissance précédent ne peut à lui seul rejeter **une condition de ratio seule** sur cette carte.

**TÉMOIN JOUET EXACT :** `r0=1/4, R=17/20, A_N=1, A_M=-1, B_N=2, B_M=3, N0=1, M0=10371/20000, kR=1`. Avec `k=k0+(9629/12000)(r-r0)`, `D=2+3k`, `D0=71113/20000`, `N=exp((r-r0)/3)*(D/D0)^(-48887/28887)`, `M=kN` : positifs analytiques, équation satisfaite exactement, `N(R)=M(R)≈0.685968777185562552`. **Pas le Step55 physique.**

**TESTS EFFECTIVEMENT EXÉCUTÉS (dans `/mnt/data/janus_session`) :** `PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_ratio_reachability` : 3 résidus algébriques génériques PASS et 5 contrôles exacts du témoin PASS ; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_ratio_reachability.py' -v` : 4 tests PASS, non indépendants, 0 FAIL. L'évaluation décimale n'intervient pas dans la preuve. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` : `Could not resolve host: github.com` ; le connecteur GitHub, lui, fonctionne en lecture/écriture. **Original Step55/Step68o/b3c2 et probe original Step58 à R=17/20 NON exécutés.**

**QUATRE LIVRABLES PUBLIÉS, RELUS ET HASHÉS (blobs identiques aux fichiers locaux exécutés/produits) :**
- `numerics/hr_step68ad_b3c3d6_ratio_reachability.py` blob `d5fad9c288ef166bb904a80c4fa68b7b7f452437`, commit `5bf1a53619120f2f9061c9b4f5c8b0898660b01a`.
- `tests/test_hr_step68ad_b3c3d6_ratio_reachability.py` blob `2a4d2d4c74a5bd75c8c8af2be9b28378e7ccc4ee`, commit `541b64ab94442f8d543d1432cbe6c00c6382da13`.
- `research/STEP68AD_B3C3D6_POSITIVE_RATIO_REACHABILITY_THEOREM.md` blob `a8b9e807ac970e1b8fe5d4906a4ae2df4582e9b1`, commit `89c75cd227a148b749e232dd90b1cdf26d066f27`.
- `research/reports/gate2b-step68ad-b3c3d6-ratio-reachability.json` blob `7efa594113164e2d4f5912beb93bc2f55f0b55c0`, commit `e2e21b8d27b0b5d78c301095810403f567226eab`.
- `README.md` blob `12f13a1c1967d709cd9aef14cd8908c5a2bed18b`, commit `bc3dadbb09a3e401733d062dde5903bb39a40d84`.

**PROVENANCE :** GitHub HEAD au démarrage `5a7d2354089c980ce4858e63b808d62ae357d7e8` (plus récent que le repère utilisateur `a53be6bb...`), HEAD avant checkpoint `bc3dadbb09a3e401733d062dde5903bb39a40d84`. Sources originales lues : Step58 blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step68o blob `c99caebc17f243784450ddff94fb061767e6d8e7`. Branches interdites lues inchangées : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. **Revalider les HEAD après mise à jour de l'index.**

**CHECKPOINT PRÉFIXÉ ; TOUT L'HISTORIQUE PRÉEXISTANT EST CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, CÔNE DE POSITIVITÉ ET CROISSANCE ANNULAIRE (2026-10-28)

**PROCHAINE ÉTAPE b3c3d6 INCHANGÉE : exécuter le probe original Step58 sur le vrai profil Step55 à R=17/20 avec Step45/55/58+b3c2 et Step68o ; certifier B_N/B_M, leurs dérivées, zéros communs, cartes/raccord central, coefficients b,d, lapses positifs et conditions réelles aux deux bords ; puis Dirac, charges/générateurs, quotient jauge temporelle, six couples, K=0/J=0, dynamique 4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE CONDITIONNELLE, NON PHYSIQUE :** Sur la coquille du premier ordre `A_N N+A_M M+B_N N'+B_M M'=0`, avec `B_N,B_M>0` et `N,M>0`, la carte sans division `u=B_N N+B_M M`, `v=-B_M N+B_N M` impose `-B_M/B_N<v/u<B_N/B_M`. L'identité exacte `u'=alpha*u+beta*v` donne un écran intégral nécessaire `u(r0)*exp(int ell)<=u(R)<=u(r0)*exp(int ups)` où `ell=alpha+min(-beta B_M/B_N,beta B_N/B_M)`, `ups=alpha+max(...)`. Une borne violée exclut des lapses positifs avec amplitudes aux deux bords prescrites ; une borne respectée ne prouve aucune existence. **Ne décide PAS une seule condition de ratio M(R)=N(R) sans amplitude ; ne traverse PAS les zéros B_N ou B_M ; ne prouve pas le raccord au centre Delta=0.** Témoin JOUET `B_N=B_M=1,A_N=-1,A_M=1`, `N(0)=M(0)=1` : `N(R)=M(R)=3` exclu, `N=M=1` admissible.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `cd /mnt/data/janus_work && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_positive_cone_growth` : 6 résidus SymPy algébriques exacts PASS, 6 résidus jouets exacts PASS ; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_positive_cone_growth.py' -v` : 4 unittest PASS non indépendants, 0 FAIL. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` : `Could not resolve host: github.com`. Le probe original Step58 R=17/20 et les moteurs complets Step45/55/58+b3c2/Step68o n'ont PAS été exécutés. Les sources originales ont été inspectées directement via GitHub : Step45 blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS SUR LA SEULE BRANCHE AUTORISÉE ET RELUS (BLOBS ÉGAUX AUX OCTETS TESTÉS) :**
- `numerics/hr_step68ad_b3c3d6_positive_cone_growth.py` blob `86a3299d870b65ce7f862c7d8067d9700e6705ca`, commit `428dda1a8c4f662a1d6a1c069078e339a9d59cd2`.
- `tests/test_hr_step68ad_b3c3d6_positive_cone_growth.py` blob `672d42648a59f91d71a92a88d220569736ca056e`, commit `ada3716d4fc6ecfcbdcf416c88a790d5a2dda1db`.
- `research/STEP68AD_B3C3D6_POSITIVE_CONE_GROWTH_SCREEN.md` blob `b648f63a2cf0fad31af3e5f94b8b0112cb4603a7`, commit `21f423b7c5b92ef19d2560e7dec7efb6b4238c23`.
- `research/reports/gate2b-step68ad-b3c3d6-positive-cone-growth.json` blob `2e526445d6cad782e029c8b8b6f4c58fa783bebb`, commit `df9e8dbcf126263ee8a7510bb323e6658491c636`.
- `README.md` blob `1564d8094ec39450e21134097acef0da20242834`, commit `ffbdd3afba025a3eb92a8beaa202dedd68086607`.

**PROVENANCE :** HEAD GitHub vérifié au démarrage `0ca8c624d37036370461bb3cc1c09c5ca7ae9ac1` (plus récent que le repère `a4e40c98...`). Branches interdites avant écriture : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucune GitHub Action ni branche interdite touchée. Vérifier à nouveau HEAD et branches après mise à jour de l'index.

**CHECKPOINT PRÉFIXÉ ; TOUT L'HISTORIQUE PRÉEXISTANT EST CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, CADRE RÉGULIER SANS DIVISION PAR B_M (2026-10-28)

**PROCHAINE ÉTAPE b3c3d6 INCHANGÉE : exécuter le vrai probe Step58 sur Step55 à R=17/20 avec Step45/55/58+b3c2 et Step68o ; certifier B_N/B_M et leurs dérivées, les zéros communs, cartes et raccord central, coefficients b,d, lapses strictement positifs et conditions réelles de bord. Puis Dirac, charges/générateurs, quotient jauge temporelle, six couples, K=0/J=0, 4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE MAIS CONDITIONNELLE, NON PHYSIQUE :** Pour A_N N+A_M M+B_N N'+B_M M'=0 sur un intervalle où B_i sont C1 et Delta=B_N²+B_M²>0, poser u=B_N N+B_M M et v=-B_M N+B_N M. En notant X=B_N'-A_N, Y=B_M'-A_M, alpha=(X B_N+Y B_M)/Delta, beta=(-X B_M+Y B_N)/Delta, on a exactement u'-alpha*u=beta*v ; N=(B_N u-B_M v)/Delta et M=(B_M u+B_N v)/Delta. Facteur intégrant I=exp(-int alpha) et terminal illustratif M(R)=N(R) disponibles dans la note. La carte reste régulière aux zéros de B_M quand B_N!=0 ; elle ne résout PAS Delta=0, notamment le centre b3c2 où B_i=O(r^4). Positivité et vraies conditions Step55 ne suivent PAS de cette identité.

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_atlas && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_nonsingular_lapse_frame` : 8 résidus SymPy exacts (2 définitionnels) PASS, 6 résidus rationnels jouets PASS, témoin ponctuel précédent repris (NON recalculé par Step58). `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_nonsingular_lapse_frame.py' -v` : 4 unittest PASS non indépendants, 0 FAIL. Exemple jouet positif N=M=1+r², B_N=1, B_M=r-1/2, traversant B_M=0 à r=1/2. Sur le témoin original publié : B_N=224/125, B_M=0, Delta=50176/15625>0 ; les dérivées B_N',B_M' et alpha,beta demeurent inconnues. **Step55/Step68o/b3c2 et probe original Step58 R=17/20 NON rejoués.** `git ls-remote` local : `Could not resolve host: github.com`.

**LIVRABLES PUBLIÉS SUR research/gate2b-nonhomothetic-transfer ET RELUS :**
- `numerics/hr_step68ad_b3c3d6_nonsingular_lapse_frame.py` blob `968996282fadaab84c139b119b42c342da6fed3d`, identique aux octets testés.
- `tests/test_hr_step68ad_b3c3d6_nonsingular_lapse_frame.py` blob `766b70dd13734d5aa4e57ab87a078c3b3506a8fa`, identique aux octets exécutés.
- `research/STEP68AD_B3C3D6_DIVISION_FREE_LAPSE_FRAME.md` blob `8111bb36e9d29ed13a3d7d8287b2aca4cd77367a`.
- `research/reports/gate2b-step68ad-b3c3d6-division-free-lapse-frame.json` blob `ef417eb03b9419897fcf45343cfcb6c9c208cdfa`.
- `README.md` blob `60d4e355e9ac52a40417441a3238a35b2a007975`.

**PROVENANCE ET SÉCURITÉ :** GitHub HEAD initial `34f51603d0f36cb46b00a78c3b25e806f856e6fb`, HEAD après publication des quatre livrables `ae30d9dce1b0d415c0b77a55631f23c737ec1336`, puis README `35f4d83d7c891676b32c68920fb8f0607c56ab31`. Sources originales consultées en direct : Step58 blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step68o blob `c99caebc17f243784450ddff94fb061767e6d8e7`, témoin original blob `0144e44cd65fd69390776c1bb2d2b6120ffd74b4`. Branches interdites initiales `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. **Vérifier le HEAD final et les deux branches après index.**

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE PRÉEXISTANT CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, TÉMOIN AUTHENTIQUE STEP58 B_M=0 (2026-10-28)

**ÉTAPE b3c3d6 TOUJOURS PARTIELLE. PROCHAINE ÉTAPE : exécuter le probe original Step58 sur le VRAI profil Step55 à R=17/20 avec Step45/55/58+b3c2 et Step68o ; certifier B_N/B_M, zéros, cartes et raccord centre, coefficients b,d et lapses positifs aux vrais bords ; ensuite pullback Dirac, charges/générateurs, jauge temporelle, six couples/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE SCIENTIFIQUE RÉELLE, MAIS PONCTUELLE NON-DIRAC :** Rejeu local des sources originales Step45 (Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`) et Step58 (Git blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`), authentifiées octet par octet ; import Step57 remplacé LOCALEMENT par un shim minimal de vérification SHA Step45, et NON par le vrai Step57. Un jet rationnel exact satisfait `Fz=Hg=Hf=C_exact=Fz'=Fz''=Fz'''=0` avec `K=1,z=3/5,pg=3/4,pf=311/100,Lg=Lf=Sg=Sf=1` et `sqrt(1-z²)=4/5`. Sur cet opérateur original, `A_N=1293/250, B_N=224/125, E_N=0 ; A_M=-79093/12500, B_M=0, E_M=0`. Ainsi `B_M != 0` NE découle PAS des contraintes ponctuelles, de la positivité du secteur K,z,poussières ni des trois jets de shift. **Ce n'est PAS un zéro prouvé sur Step55 : les dérivées de Hg,Hf,C, le profil spatial global, la tangence Dirac et les vrais bords restent non imposés.**

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `cd /mnt/data/janus_original_replay && python -m numerics.hr_step58_temporal_operator` PASS (~4,01 s), certificat original des seconds jets ; `exact_certificate_summary()` Step45 PASS (9 résidus Ward exacts) ; `python -m numerics.hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness` PASS (7 résidus exacts, 6 coefficients exacts, signes positifs) (~9,44 s) ; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness.py' -v` 4 PASS non indépendants (~8,56 s), 0 FAIL. Git direct : DNS `Could not resolve host: github.com`. **Step55/Step68o/b3c2 et probe original Step58 à R=17/20 NON exécutés.**

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS SUR LA SEULE BRANCHE RECHERCHE :**
- `numerics/hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness.py` blob `0144e44cd65fd69390776c1bb2d2b6120ffd74b4` (égal au fichier local testé), commit `ef938feba974273750f44b91b5cd24448284da80`.
- `tests/test_hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness.py` blob `b3a2aba30b6f9e02cc056a2bde9a718668eaf27c` (égal au fichier local exécuté), commit `4d1ca324f26c3df171a16268ce4f41b468df848d`.
- `research/STEP68AD_B3C3D6_AUTHENTIC_STEP58_SHIFT_JET_CHART_WITNESS.md` blob `84a22100c83f0d568c765b15c7b2ada7b9b26c84`, commit `1074574ae4dc2a52aa4e7f88116dca22ce8514c8`.
- `research/reports/gate2b-step68ad-b3c3d6-authentic-Step58-shift-jet-chart-witness.json` blob `96e12a77ba3a8e8b977e87783f97824a6deb67ec`, commit `2ee0e2ab735c06e8712d1c3890f86ae61154b840`.
- `README.md` blob `e9aba61ad3084cc856349bc7c79b91c29d6e23c6`, commit `de5bfab205ca05cb764ece4ad007d875e6de00c2`.

**ÉTAT GITHUB :** HEAD initial authentifié `51def2c42b3b983c00553c0c219cb8aeacb6376a`. Branches interdites au départ `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow ni branche interdite modifié. Vérifier HEAD final et branches après index. **VERROUS :** full original Step55/Step68o/b3c2 et rayon R ; couverture B_M/zéros et raccord central ; vrais lapses positifs/bords ; Dirac six couples et quotient temporel ; 4D/stabilité/observables.

**CHECKPOINT PRÉFIXÉ ; TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, COURBURE CENTRALE DU RATIO DES LAPSES (2026-10-28)

**ÉTAPE b3c3d6 TOUJOURS PARTIELLE. PROCHAINE ACTION : exécuter réellement le probe original Step58 à R=17/20 et les imports Step45/55/58+b3c2 ; certifier B_N/B_M, b,d et les cartes de raccordement au centre ; résoudre le vrai problème global des lapses positifs et les conditions Step55 ; puis pullback Dirac, charges/générateurs, quotient jauge temporelle, six couples/rang/tertiaires/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU LEMME EXACT, STRICTEMENT CONDITIONNEL, NON DIRAC :** Pour A_N=a r²+b r⁴+o(r⁴), A_M=c r²+d r⁴+o(r⁴), B_i=O(r⁴), lapses pairs C² N=N0+N2 r²+o(r²), M=M0+M2 r²+o(r²), N0>0, c≠0, sur la coquille où E_N=E_M=0 EXACTEMENT dans un voisinage, rho=M/N satisfait rho0=-a/c et **rho''(0)=-2(b+d rho0)/c**, indépendamment de N2. Si E_N=e r⁴+o(r⁴), E_M=f r⁴+o(r⁴) sans annulation exacte et c+2f≠0, rho2=-[(b+d rho0)+2(e+f rho0)N2/N0]/(c+2f) : la courbure peut dépendre de N2. Cas c+2f=0 non résolu par division. Deux familles d'opérateurs JOUETS positifs, u=0 et u=1 chacune, vérifient exactement cette distinction. **Coefficients physiques b,d et l'identité E=0 sur Step55 non certifiés : aucune courbure physique Step58 n'est affirmée.**

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_run11 && PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_center_ratio_curvature` : 11 résidus symboliques SymPy exacts PASS et 2 familles jouets positives (u=0,1) ; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_center_ratio_curvature.py' -v` : 4 unittest PASS non indépendants ; 0 FAIL final. Import des tests corrigé vers le chemin canonique du dépôt avant publication finale. `git ls-remote` : `Could not resolve host: github.com`. Moteurs originaux Step45/55/58, b3c2 et probe Step58 R=17/20 NON exécutés.

**LIVRABLES PUBLIÉS SUR research/gate2b-nonhomothetic-transfer ET RELUS, BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_b3c3d6_center_ratio_curvature.py` : blob `3ecd9f7a166834e851e6b34e23130642e7479bf1` ; commit `b79cd6d9e8c3c8ebb612785ba080f064d8ff264c`.
- `tests/test_hr_step68ad_b3c3d6_center_ratio_curvature.py` : blob `bdcf750390d33bf1bd4422d420abe3e4e39dc50d` ; commit correctif `f529a42ea6b92da907166f517d27e85e9aed0a5e`.
- `research/STEP68AD_B3C3D6_FORMAL_CENTER_LAPSE_RATIO_CURVATURE.md` : blob `e8f02659827a4931654864f8d8204e99c612f0aa` ; commit correctif `e9bb304b41b8013f576ebc695b9b57da1287d219`.
- `research/reports/gate2b-step68ad-b3c3d6-formal-center-ratio-curvature.json` : blob `82f40c37a6baa56b119e4c301067a66295c8e1f1` ; commit `4e85ef97690270a7b1cf18f131cb924fafb251c9`.
- `README.md` index mis à jour : blob `4fb6feee7b94b84dcf01af7a31e4e4dc34739120`, commit `505bf54900e9c1ce2e6ee7a75ffeffe9319105bb`.

**PROVENANCE ET LIMITES :** original `numerics/hr_step58_temporal_operator.py` lu sur GitHub, blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; `numerics/hr_step68o_temporal_interval_annulus.py` lu, blob `c99caebc17f243784450ddff94fb061767e6d8e7`. Aucune substitution des jouets aux coefficients authentiques. Branche initiale comparée à `c03c80e9289fc81fb77549a0991b834fac9a749f` : 1 commit d'index plus récent ; branches interdites initialement inchangées `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Vérifier HEAD final et ces branches après index.

**CHECKPOINT PRÉFIXÉ, HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, ÉCRAN INTÉGRAL NÉCESSAIRE DES LAPSES SUR ANNEAU (2026-10-28)

**b3c3d6 RESTE PARTIELLE — PROCHAINE ÉTAPE : EXÉCUTER LE PROBE ORIGINAL STEP58 À R=17/20 ET REJOUER STEP45/55/58+b3c2 ; CERTIFIER B_N/B_M SUR DES ANNEAUX, RACCORDER AU CENTRE DÉGÉNÉRÉ ET ÉTABLIR LES VRAIES CONDITIONS DE BORD DES LAPSES POSITIFS. PUIS PULLBACK DIRAC, GÉNÉRATEURS/CHARGES, QUOTIENT JAUGE TEMPORELLE, SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE, CONDITIONNELLE ET NON PHYSIQUE :** Sur `[epsilon,R]`, `epsilon>0`, `B_M != 0`, l'identité antérieure `W=M+qN`, `W'+pW=hN` fournit une nouvelle *exclusion par encadrement intégral* : si `0<nlo<=N<=nhi`, le membre droit de la condition terminale `(1+q(R))N(R)=exp(-P(R))W(epsilon)+int K hN` est entre `L=exp(-P(R))W(epsilon)+int K(hplus*nlo+hminus*nhi)` et `U=exp(-P(R))W(epsilon)+int K(hplus*nhi+hminus*nlo)`, `K=exp(P(s)-P(R))>0`. Un terminal hors de `[L,U]` est impossible ; un terminal dedans ne prouve RIEN sur l'existence physique. Témoins rationnels JOUETS sur `[1/4,17/20]` : `p=0,q=-1,W0=-1/2,1/2<=N<=2` ; `h=-1` exclut `M(R)=N(R)` car `[L,U]=[-17/10,-4/5]` et `T=0`. Avec `h=1`, `[L,U]=[-1/5,7/10]` et une solution positive explicite existe : `N=5/6,M=1/3+(5/6)(r-1/4)`. Contrôle d'un `h` changeant de signe exact. **Ce ne sont PAS les coefficients Step58 et `M(R)=N(R)` est illustratif, pas la vraie condition d'horloge Step55.**

**TESTS EXÉCUTÉS :** `PYTHONPATH=/mnt/data/janus_b3c3d6 python -m numerics.hr_step68ad_b3c3d6_annular_interval_screen` : 10 assertions exactes PASS ; `PYTHONPATH=/mnt/data/janus_b3c3d6 python -m unittest discover -s /mnt/data/janus_b3c3d6/tests -p 'test_hr_step68ad_b3c3d6_annular_interval_screen.py' -v` : 4 unittest PASS, non indépendants ; 0 FAIL final. Un premier témoin avait une pente `M'=1` incorrecte ; corrigé en `M'=5/6`, tous les tests rejoués. `git ls-remote` : `Could not resolve host: github.com`. **Probe original Step58 R=17/20, imports Step45/55/58+b3c2 NON exécutés.**

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS SUR LA SEULE BRANCHE RECHERCHE (BLOBS IDENTIQUES AUX OCTETS TESTÉS) :**
- `numerics/hr_step68ad_b3c3d6_annular_interval_screen.py` blob `ec8cc8b744b61305d20af77c84461c2a037c42d7`, commit `d3b33de10f2cf689ad6381089e9b9cdb82b1478e`.
- `tests/test_hr_step68ad_b3c3d6_annular_interval_screen.py` blob `add6a6bc7f41052dbe861f0549389ba273f2648e`, commit `4142c9cabf15686751c908fd90401784b88a8cbe`.
- `research/STEP68AD_B3C3D6_ANNULAR_POSITIVE_LAPSE_INTERVAL_SCREEN.md` blob `edb54bc560de0f38d004435e400d884ca9ffd183`, commit `1795a236ac85faa3fc153ed0bd3cd70bda03af1a`.
- `research/reports/gate2b-step68ad-b3c3d6-annular-positive-lapse-screen.json` blob `a9864033e2fc6f6fe9a5855d2080766bad5fed68`, commit `78c1515c13e2c68d5756ed1316e0a82de5aea7a6`.
- `README.md` mis à jour, blob `3a566c9ad1c2f5a3ac2227a986527a5e5fb737b1`, commit `8f38292a383fdabd7ec83817ecf7fed47617b374`.

**GITHUB :** HEAD initial authentifié `534d0453d1cb7adb3f491f26c82f8399b06c9d6b` ; avant ce checkpoint `8f38292a383fdabd7ec83817ecf7fed47617b374`. Branches interdites relues : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. Vérifier HEAD final après index.

**VERROUS :** (1) exécution des sources originales impossible via clone local DNS ; (2) évaluer `B_M` et ses zéros, `B_N/B_M` sur anneaux originaux avec certificats ; (3) raccord central `B_M(0)=0` et vrais bords/positivité ; (4) charges/générateurs, quotient jauge temporelle, Dirac six couples, K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, JETS CENTRAUX r⁴ (2026-10-28)

**b3c3d6 RESTE PARTIELLE — PROCHAINE ÉTAPE INCHANGÉE : EXÉCUTER LE PROBE ORIGINAL STEP58 À R=17/20 ET LES IMPORTS STEP45/55/58+b3c2 ; CERTIFIER B_N/B_M ET LES CARTES CENTRALES ; RÉSOUDRE LES VRAIS LAPSES POSITIFS ET LES DEUX BORDS ; PUIS PULLBACK DIRAC, CHARGES/GÉNÉRATEURS, QUOTIENT JAUGE TEMPORELLE, SIX COUPLES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVELLE IDENTITÉ EXACTE MAIS FORMELLE, NON PHYSIQUE :** Si `A_N=a r²+b r⁴+o(r⁴)`, `A_M=c r²+d r⁴+o(r⁴)`, `B_N,B_M=O(r⁴)`, `E_N=e r⁴+o(r⁴)`, `E_M=f r⁴+o(r⁴)`, et `N=N0+N2 r²+o(r²)`, `M=M0+M2 r²+o(r²)` sont pairs C², l'opérateur complet `A_N N+A_M M+B_N N'+B_M M'+E_N N''+E_M M''` impose `aN0+cM0=0` à l'ordre r² et `(a+2e)N2+(c+2f)M2+bN0+dM0=0` à l'ordre r⁴. Les termes `B_i L_i'` commencent à O(r⁵), MAIS `E_i L_i''` contribuent à r⁴ : `E=O(r⁴)` ne signifie pas `E=0`. Sur la coquille primaire exacte Step58, si `E=0` est réimposé, prendre `e=f=0`. Les coefficients physiques `b,d,e,f` ne sont PAS calculés. Trois opérateurs JOUETS avec mêmes `a=2,c=-4,N0=1,M0=1/2` et lapses analytiques positifs donnent `M2=0,3/4,3/2` : le seul ratio central ne détermine pas la courbure des lapses.

**TESTS RÉELLEMENT EXÉCUTÉS :** `python -m numerics.hr_step68ad_b3c3d6_center_subleading_jet` : 8 résidus SymPy nuls (certains élémentaires/non indépendants), 3 modèles exacts positifs ; `python -m unittest -v tests.test_hr_step68ad_b3c3d6_center_subleading_jet` : 4 tests PASS, non indépendants, 0 FAIL. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git refs/heads/research/gate2b-nonhomothetic-transfer` : échec DNS `Could not resolve host: github.com`. **Probe original Step58 R=17/20, Step45/55/58+b3c2 NON exécutés.**

**LIVRABLES SCIENTIFIQUES PUBLIÉS SUR LA SEULE BRANCHE RECHERCHE, RELUS OCTET POUR OCTET :**
- `numerics/hr_step68ad_b3c3d6_center_subleading_jet.py` blob `340d05c76db1f9ae25fdbc1fc7167e65b4a6867a`, commit `49517aee7e6ddfb4eafe09339cd58bda1d9c8ffc` ; blob égal aux octets Python locaux testés.
- `tests/test_hr_step68ad_b3c3d6_center_subleading_jet.py` blob `70a3376e9f9a173d75a0f214274a0d8094c0625d`, commit `b55331826573f48c41a3824296743e24aef7882c` ; blob égal aux octets du test local.
- `research/STEP68AD_B3C3D6_FORMAL_CENTER_SUBLEADING_LAPSE_JETS.md` blob `799d6881f74886346b62133ce55db686efbd0127`, commit `ecbed137bd817ad8376617eb5b6fde9fb8f30c02`.
- `research/reports/gate2b-step68ad-b3c3d6-formal-center-subleading-jets.json` blob `e19106f2718cae5e965bde73609f3a7fcd34a3cd`, commit `09ee941091d52d82578c5320b4f292250fedb64b`.

**GITHUB :** HEAD initial authentifié `8d0f60aa72d290b7d0f81b9947d77c58065a94b1`. Branches interdites lues avant écriture : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucune action GitHub Actions ni modification des branches interdites. Vérifier HEAD final après index.

**LIMITES / PRIORITÉS :** (1) DNS Git local bloque les imports originaux, mais connecteur GitHub lecture/écriture fonctionnel ; (2) b3c2 authentifié seulement par lecture de sources et audit antérieur, pas rejoué ; (3) vérifier Step58 sur la vraie coquille `F_z=H_g=0`, évaluer `b,d` et annulation exacte des `E` ; (4) exécuter probe externe pour `B_N,B_M`, cartes et raccord central ; (5) BVP lapses positifs et vrais bords Step55 ; (6) Dirac, charges/générateurs, quotient jauge temporelle, six couples, K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, IDENTITÉ GLOBALE CONDITIONNELLE DES LAPSES (2026-10-28)

**b3c3d6 RESTE PARTIELLE — PROCHAINE ÉTAPE INCHANGÉE : EXÉCUTER LE PROBE ORIGINAL STEP58 À R=17/20, CERTIFIER B_N/B_M SUR LES CARTES ADMISSIBLES ET LE PROBLÈME GLOBAL DES LAPSES AUX DEUX BORDS ; PUIS VRAI PULLBACK DIRAC, GÉNÉRATEURS/CHARGES, QUOTIENT JAUGE TEMPORELLE, SIX COUPLES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE MAIS CONDITIONNELLE :** Pour `A_N N+A_M M+B_N N'+B_M M'=0`, sur un intervalle où `B_M≠0`, poser `q=B_N/B_M`, `p=A_M/B_M`, `a=A_N/B_M`, `h=q'+pq-a`, `W=M+qN`. Alors `W'+pW=hN` exactement, et la condition illustrative `M(R)=N(R)` équivaut, pour `N` et `M(0)` prescrits, à `(1+q(R))N(R)=exp(-P(R))(M(0)+q(0)N(0))+∫_0^R exp(-(P(R)-P(s)))h(s)N(s)ds`, `P'=p`. Ce test intégral détecte l'obstruction globale des opérateurs jouets b3c3d6 : `L_bad` a `q=-1,p=h=0` et échoue, `L_good` a `q=-1,p=-κr,h=2κr` et admet le polynôme pair positif déjà certifié. **Ce n'est PAS un résultat physique Step58** : b3c2 indique `B_N,B_M=O(r⁴)` au centre, donc `B_M(0)=0` et la formule ne peut être appliquée à `[0,R]` sans analyse de raccordement ou carte `[ε,R]`. De plus `M(R)=N(R)` n'est pas la vraie condition Step55 des horloges, dépendant du shift.

**TESTS RÉELLEMENT EXÉCUTÉS :** `python -m numerics.hr_step68ad_b3c3d6_integrating_factor_bvp` : **13 résidus exacts SymPy nuls, 4 signes exacts PASS** ; `python -m unittest -v tests.test_hr_step68ad_b3c3d6_integrating_factor_bvp` : **4 unittest PASS, non indépendants**, 0 FAIL final. Premier essai : conversion implicite Python `0/-1=0.0` identifiée puis corrigée par `sympify` ; les tests ont ensuite été rejoués et réussis. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git ...` : **échec DNS `Could not resolve host: github.com`**. **Moteurs originaux Step45/55/58, b3c2 et probe original Step58 R=17/20 NON exécutés.** Sources originales Step58/Step68o/Step55/b3c2 lues via GitHub, blobs respectifs `802c23aebd41780d8c462f1aa1711707fe4ee88f`, `c99caebc17f243784450ddff94fb061767e6d8e7`, `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, `9a77f749a040aaec37e7c3f01368013154fdb562`.

**LIVRABLES SCIENTIFIQUES PUBLIÉS SUR LA SEULE BRANCHE RECHERCHE ET RELUS :**
- `numerics/hr_step68ad_b3c3d6_integrating_factor_bvp.py` : blob `04643b1ed377840a37303a5c7c5a673241d28ab8` (identique au fichier Python local testé).
- `tests/test_hr_step68ad_b3c3d6_integrating_factor_bvp.py` : blob `6857cf47a6e7c3817292a4b8a64a1084d1d0e5b2` (identique au test local exécuté).
- `research/STEP68AD_B3C3D6_CONDITIONAL_INTEGRATING_FACTOR_BVP.md` : blob `fe9b106e57642761991315eaa68f6dee94b7acae`.
- `research/reports/gate2b-step68ad-b3c3d6-conditional-integrating-factor-bvp.json` : blob `9f01c472354e1feb9fddb55c3df7f678c94eeea1`.
- `README.md` : blob `a9fddc38f652731a502566764121916a2a07ea18`.

**GITHUB :** HEAD de reprise authentifié `7e3e0844daa4eff3c27b52a9e0a0f6f116f1a4bb` ; commits des quatre livrables `f587ec5e27d65667866c0884230f75ece1c5a122`, `c73a8a33f59aa19019d15d1157a2011698ef6ef1`, `df695695126706961b8853bafabfbc0b6f682e02`, `fa0cf7bce3d11b23ad738c72c241e8bc92bf8455` ; README `c000c80350319f6b4f5cd549987fcddb66e0b799`. HEAD avant ce checkpoint `c000c80350319f6b4f5cd549987fcddb66e0b799`. Branches interdites au départ : `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié.

**VERROUS :** (1) DNS clone Git et rejeu original Step58/Step68o, Step45/55/58+b3c2 ; (2) certifier `B_M` non nul ou construire des cartes et raccords, évaluer `B_N/B_M` à `R=17/20` ; (3) résoudre la compatibilité globale des lapses positifs avec **les vraies** conditions d'horloge et les deux bords ; (4) Dirac six couples, charges/générateurs, quotient temporel, K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d6 PARTIEL, CONTRE-EXEMPLE AU PASSAGE RANG PONCTUEL → BVP GLOBAL (2026-10-28)

**b3c3d6 NON TERMINÉE — PROCHAINE ACTION : EXÉCUTER LE PROBE ORIGINAL STEP58 À R=17/20 SUR CLONE COMPLET, PUIS COMPATIBILITÉ GLOBALE DES LAPSES ET DEUX BORDS ; PULLBACK DIRAC, CHARGES/JAUGE TEMPORELLE, SIX COUPLES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT NOUVEAU, STRICTEMENT MATHÉMATIQUE :** deux opérateurs jouets linéaires scalaires ont le même symbole principal `(B_N,B_M)=(1,-1)`, donc la même projection ponctuelle de rang 2 sur `(N,M)` partout, mais leurs problèmes aux limites sont respectivement impossible et possible. Avec `R=17/20`, `rho=10371/20000` dans l'intervalle central b3c2, `N(0)=1,M(0)=rho,N'(0)=M'(0)=0,N(R)=M(R)`, l'opérateur `L_bad=N'-M'` est impossible par conservation de `N-M=1-rho>0`. L'opérateur `L_good=N'-M'+kappa*r*(N+M)` avec `kappa=7703200/8777219` admet la solution paire analytique strictement positive `N=(S+D*(1-(r/R)^2))/2,M=(S-D*(1-(r/R)^2))/2`, `S=1+rho,D=1-rho`. **Ceci ne teste PAS l'opérateur physique Step58 ni les vraies conditions d'horloge Step55.** Cela interdit de déduire un verdict global du seul rang ponctuel, même si les B sont connus exactement sur tout l'intervalle.

**EXÉCUTÉ :** `python -m numerics.hr_step68ad_b3c3d6_bvp_counterexample` : 10 résidus SymPy exactement nuls, 6 contrôles exacts de signes, 2 identités supplémentaires de positivité PASS ; `python -m unittest -v tests.test_hr_step68ad_b3c3d6_bvp_counterexample` : 4 tests PASS, non indépendants, 0 FAIL. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git refs/heads/research/gate2b-nonhomothetic-transfer` : échec DNS `Could not resolve host: github.com`. **Probe original Step58, moteurs originaux Step45/55/58 et unittest b3c2 NON exécutés.** Les fichiers Step58, Step68o et b3c3d5 ont été lus via le connecteur et leurs blobs vérifiés, sans les exécuter.

**QUATRE LIVRABLES SCIENTIFIQUES CRÉÉS SUR LA SEULE BRANCHE RECHERCHE ET RELUS (SHA Git blobs = octets locaux) :**
- `numerics/hr_step68ad_b3c3d6_bvp_counterexample.py` — `54cad42ea5804a7f72b460fd5810cd2e64aded5a`.
- `tests/test_hr_step68ad_b3c3d6_bvp_counterexample.py` — `f905c9ee823f08d2031def13925bac959910ecb7`.
- `research/STEP68AD_B3C3D6_POINTWISE_RANK_NOT_GLOBAL_BVP.md` — `09261bac0e704ae4714cbac51a03fa10af360fbb`.
- `research/reports/gate2b-step68ad-b3c3d6-bvp-counterexample.json` — `f7083967792e7c1027ff2a1953d8cc0ae2ce8b70`.
- `README.md` — `53aff81a882b94250e642b1629e1cab91736f89e`.

**GITHUB :** HEAD de reprise initial `da8dbfd5b7b431f8d04c08dc98e0df67cfbbbfea` ; commits scientifiques `71ba23009d6c1f4c0f93d25e0c0dc93d742fab1a`, `3da58e9418f42599c659e25438a7c2c6382b282e`, `ed6d145e43e6bb96aab46b7908caef9da6afe4c1`, `d85eebbe08d7a3193a27ba9f6fc8a91b85e30f37`, README `f9c817f0caac0ff1a582c17f69e73f04d846c3c2`. Les branches interdites `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` sont inchangées à la lecture avant checkpoint ; revérifier après l'index. Aucun workflow modifié.

**VERROUS / ACTIONS PRIORITAIRES :** (1) réparer l'accès clone Git et exécuter `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank --probe-original` avec authentification SHA ; certifier les enclosures des coefficients `A_N,A_M,B_N,B_M,E_N,E_M` au bord externe, sans convertir une enclosure contenant zéro en signe ; (2) étudier l'équation différentielle complète des lapses et la régularité centrale / conditions d'horloge réelles aux deux bords ; (3) rejouer Step45/55/58+b3c2 ; (4) véritable pullback Dirac, charges/générateurs et quotient temporel, six couples, rang/tertiaires, K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d5 PROJECTION DES JETS TEMPORELS ET DÉRIVE CENTRALE (2026-10-28)

**ÉTAPE b3c3d5 TERMINÉE (THÉORÈME ALGÉBRIQUE PONCTUEL EXACT, COROLLAIRE CENTRAL CONDITIONNEL, NON DIRAC) — PROCHAINE ÉTAPE b3c3d6 : EXÉCUTER LE PROBE ORIGINAL STEP58 À R=17/20, TESTER B_N/B_M ET LA TANGENCE GLOBALE DES LAPSES AVEC LES DEUX BORDS, REJOUER STEP45/55/58+b3c2, PUIS PULLBACK DIRAC/CHARGES/QUOTIENT TEMPOREL/SIX COUPLES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT PONCTUEL :** Après réduction des jets de lapses d'ordre 2 sur la coquille Step58 `Fz=0,Hg=0,K>0` (résultat original Step58, non rejoué ici), la condition temporelle à un point est `A_N N+A_M M+B_N N'+B_M M'=0`. Si `(B_N,B_M)≠(0,0)`, les valeurs de bord `(N,M)` restent libres au niveau des jets ponctuels : projection de rang 2 ; si les deux `B` sont nuls mais un `A` non nul, rang 1, tangente `(A_M,-A_N)`, et courbure de la forme b3c3d4 nulle sur cette tangente ssi `c_N A_M-c_M A_N=0`. **AUCUNE** implication de tangence globale Dirac, charges physiques, différentiabilité du générateur ni admissibilité aux deux bords. Les coefficients `B_N,B_M` authentiques à R=17/20 ne sont pas encore évalués.

**COROLLAIRE CENTRAL CONDITIONNEL :** Le rapport exact b3c2 `1037/2000<M(0)/N(0)<2593/5000`, avec `N(0)>0`, impose `2407/5000<∂t(tg−tf)(0)/N(0)<963/2000`. Si la vitesse relative est `C¹` et annulée à `R=17/20`, le théorème des accroissements finis impose `∃ξ∈(0,17/20): ∂r∂t(tg−tf)(ξ)/N(0)<−2407/4250`. **Ce n'est ni une singularité ni un no-go JANUS**, et le certificat b3c2 n'a pas été rejoué sur les imports originaux cette session.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank` : 12 résidus SymPy nuls + 6 contrôles de classification exacts PASS ; `python -m unittest -v tests.test_hr_step68ad_b3c3d5_temporal_boundary_jet_rank` : 4 unittest PASS non indépendants ; 0 FAIL final. Premier essai : test Python utilisant `is False` sur `sympy.BooleanFalse` corrigé par `bool()` avant publication. `git ls-remote` : échec DNS `Could not resolve host: github.com`. Le probe `--probe-original` n'a **PAS** été exécuté, ni Step45/55/58+b3c2 en clone complet. Les sources Step45/55/58/Step68o et le certificat b3c2 ont été lus via GitHub.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS, BLOBS ÉGAUX AUX OCTETS LOCAUX :**
- `numerics/hr_step68ad_b3c3d5_temporal_boundary_jet_rank.py` : `85469568e6df7c26920c1ebb87593dbf474deb04`.
- `tests/test_hr_step68ad_b3c3d5_temporal_boundary_jet_rank.py` : `419c6785aa1409edcd252694136b6a66ac4669ad`.
- `research/STEP68AD_B3C3D5_TEMPORAL_JET_PROJECTION_AND_CLOCK_DRIFT.md` : `a7f429fc82c2f7609a961f10d5e175dbd79efaf6`.
- `research/reports/gate2b-step68ad-b3c3d5-temporal-jet-rank.json` : `ef8fe6c789ed7a5bd519620574966b5e3c3ff2ec`.
- README mis à jour : `d8859c8c8190feecf9e8827b33703af774a44bc3`.

**GITHUB :** HEAD de reprise lu `2fea0149cf722e0d56ac77f977890588204841f8`. Quatre appels réels `create_file` et un `update_file` README exclusivement sur `research/gate2b-nonhomothetic-transfer`, commits `a8dd36628bb76bc885df9275262c0e0a0310f7a6`, `3d567284f6fd13c3546919a2073405c24b6e43e9`, `86b59f30b8736414ac1f7d0317827f8b65ef830b`, `21a704bc30437add7f9dd4e435ab7c696d9d08cf`, `b7037c7eb0539be6bf1ceb21d4b89f8ff3745c98`. Les branches interdites observées au départ : main `aead63f4098f0d15a849e579105af034b6317b30`, research/v2-flrw `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Vérification finale des HEAD à faire après l'index. Aucun workflow modifié.

**VERROUS PRIORITAIRES :** (1) exécuter l'évaluateur original Step58 des coefficients `A,B,E` au bord externe et contrôler la réduction par les primaires ; (2) résoudre l'équation différentielle des lapses avec conditions au centre et au bord externe, pas seulement un jet ponctuel ; (3) rejouer b3c2 et les moteurs originaux ; (4) générateurs améliorés/charges et quotient de jauge temporelle ; (5) Dirac six couples/rang/tertiaires, cartes K=0/J=0, dynamique 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d4 COURBURE DES LAPSES APRÈS SHIFT D'HORLOGE RELATIVE (2026-10-28)

**ÉTAPE b3c3d4 TERMINÉE (THÉORÈME EXACT RESTREINT, NON DIRAC) — PROCHAINE ÉTAPE b3c3d5 : IMPOSER LE VRAI OPÉRATEUR TEMPOREL STEP58 SUR STEP55 R=17/20, REJOUER LES IMPORTS ORIGINAUX STEP45/55/58 ET b3c2, CONTRÔLER LES DEUX BORDS ET LES VARIATIONS DIRAC, PUIS GÉNÉRATEURS/CHARGES/QUOTIENT TEMPOREL, SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT RESTREINT :** Sur la famille spatiale Step55 à R=17/20, avec a=∂lambda pLg=92730563/128000000>0, b=∂lambda pLf>0 (enclosure antérieure), q=Lg/Lf>0, T=tg'>0, U=−tf'>0, sg=sqrt(1+(T/Lg)^2)>0, sf=sqrt(1+(U/Lf)^2)>0, H=Lg*a+Lf*b>0, le pullback non-IBP Theta=[−z*a*(N+q*M)−H*V]d(lambda). Le shift qui préserve instantanément tg−tf est Vrel=[M*sf−N*sg−z*(N/Lg+M/Lf)*T]/(T+U). Sur la tranche étendue (lambda,N,M) à lapses **indépendants**, Theta=(cN*N+cM*M)d(lambda), avec cN=−z*a+H*(sg+z*T/Lg)/(T+U) et cM=−z*q*a−H*(sf−z*T/Lf)/(T+U). **cM−q*cN=−H*(sf+q*sg)/(T+U)<0**, exactement et indépendamment de z. Les deux composantes dN∧d(lambda) et dM∧d(lambda) ne peuvent donc s'annuler ensemble. **Ce n'est PAS** une courbure physique sur le sous-espace Step58/Dirac : les lapses sont des multiplicateurs et leurs variations admissibles sont inconnues.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** python -m numerics.hr_step68ad_b3c3d4_relative_clock_lapse_curvature : 13 résidus symboliques exacts nuls + 6 contrôles rationnels (dont 2 identités géométriques de racines et contrôle négatif) PASS ; python -m unittest -v tests.test_hr_step68ad_b3c3d4_relative_clock_lapse_curvature : 4 cas PASS, non indépendants ; 0 FAIL. Témoin rationnel NON Step55 : cN=3417/5500, cM=−7059/11000, cM−q*cN=−2323/2200. git ls-remote : ECHEC DNS Could not resolve host: github.com ; les moteurs originaux Step45/55/58 et b3c2 ne sont PAS rejoués. Sources Step45 et Step55 relues par connecteur, SHA authentifiés.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS, SHA BLOBS IDENTIQUES AUX OCTETS LOCAUX :**
- numerics/hr_step68ad_b3c3d4_relative_clock_lapse_curvature.py : 02ea2c65ff040ce96f42fd8ecf79eeea9bebee56.
- tests/test_hr_step68ad_b3c3d4_relative_clock_lapse_curvature.py : b2a352f578bdb30565484c734b9da7efc7ee1b0f.
- research/STEP68AD_B3C3D4_RELATIVE_CLOCK_OUTER_LAPSE_CURVATURE.md : 19684bc7ec0994a1348bff5c3ddf24f84a1c55b3.
- research/reports/gate2b-step68ad-b3c3d4-relative-clock-lapse-curvature.json : 71ba0d3fee5c53248522c2b5bd80383da934d195.

**GITHUB :** HEAD initial lu 40d81654c9eecc489448c137977bfa37ab891e4c. Quatre create_file réels exclusivement sur research/gate2b-nonhomothetic-transfer, derniers commits des livrables 4d1cbe535ee6e5a504e72b063bd55f143584cae0, 59462d30f0f07020a593217deece8f21f8a74ac9, d2effd99c49f5ab643d44c8dae9611c8c88f70e4 et 6a5c0fcd9e0de05c0d03e9adcd2f12535013836b. main initial aead63f4098f0d15a849e579105af034b6317b30 ; research/v2-flrw initial dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb. Aucun workflow modifié.

**VERROUS ET PRIORITÉS :** (1) obtenir la restriction temporelle originale Step58 sur N,M et sa tangence avec la variation lambda ; (2) réexécuter Step45/55/58+b3c2 dans clone complet ; (3) calculer la forme de bord complète sur la vraie surface de Dirac et bords conservés, les charges/générateurs et le quotient temporel ; (4) six couples, rang/tertiaires, cartes K=0/J=0, 4D, stabilité, observables. Aucune preuve générale pour JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d3 ANNULATION CUBIQUE DU BORD CENTRAL RÉGULIER (2026-10-28)

**ÉTAPE b3c3d3 TERMINÉE (LEMME CINÉMATIQUE EXACT RESTREINT, NON DIRAC) — PROCHAINE ÉTAPE b3c3d4 : REJEU ORIGINAL STEP45/55/58+b3c2, VARIATIONS TANGENTES AUX PRIMAIRES, C(r)=0, PRÉSERVATION TEMPORELLE STEP58 ET BORD EXTERNE STEP55 R=17/20 ; GÉNÉRATEURS AMÉLIORÉS, CHARGES, QUOTIENT JAUGE TEMPORELLE, PUIS DIRAC SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU RÉSULTAT EXACT MAIS RESTREINT :** Dans la classe analytique régulière au centre, avec `Lg,Lf,N,M` pairs, `Sg=r(L0+O(r²))`, `Sf=r(F0+O(r²))`, `pLg,pLf,pg,pf=O(r²)`, `pSg,pSf=O(r)`, `tg',tf',z,V=O(r)`, les dix termes de la forme originale de bord non-IBP sont impairs. Les seuls quatre coefficients potentiellement linéaires, `+2 Mg2 N0 r δSg'`, `-2 Mg2 N0 r δLg`, `+2 Mf2 M0 r δSf'`, `-2 Mf2 M0 r δLf`, s'annulent sous la tangence aux relations géométriques `δSg'(0)=δLg(0)`, `δSf'(0)=δLf(0)`. **Le pullback est Theta_center=O(r³), et dTheta_center=O(r³) sur les familles lisses uniformes**, même en faisant varier les lapses pairs. Ordre optimal : variation `δL2=1` donne `lim Theta/r³=-2 Mg2 N0`. Variation non régulière : `lim Theta/r=2 Mg2 N0(δH0−δL0)`. Cela élimine le terme mixte linéaire libre de lapse de b3c3d2 **sur cette classe centrale**, sans conclure sur le bord externe, la charge physique ou la tangence Dirac. Le shift régulier est **supposé**, pas obtenu des contraintes ; le critère central antérieur b3b2a demeure.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `python -m numerics.hr_step68ad_b3c3d3_center_boundary_parity` : **25 assertions exactes SymPy PASS** (10 parités, 10 coefficients linéaires, annulation, témoin cubique, contre-exemple non régulier, 2 contrôles lapse). `python -m unittest -v tests.test_hr_step68ad_b3c3d3_center_boundary_parity` : **4 cas PASS**, non indépendants. Premier unittest échoué sur compteur attendu 24 au lieu de 25, corrigé puis quatre cas PASS ; **0 FAIL final**. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git refs/heads/research/gate2b-nonhomothetic-transfer` : échec DNS `Could not resolve host: github.com`. Les sources Step37/45 et b3c3d2 ont été relues via GitHub, mais **imports originaux Step45/55/58 et test b3c2 NON rejoués**.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS, RELUS, BLOBS IDENTIQUES AUX OCTETS LOCAUX TESTÉS/PRODUITS :**
- `numerics/hr_step68ad_b3c3d3_center_boundary_parity.py` : `f63f05c6173c473a957fd4e87bbb37e141432a41`.
- `tests/test_hr_step68ad_b3c3d3_center_boundary_parity.py` : `06d481d5da02b8436acfcf351a615b7b0bd43db5`.
- `research/reports/gate2b-step68ad-b3c3d3-regular-center-boundary-parity.json` : `b9acd1a907c056d12a4d34cf6134c7908b32047f`.
- `research/STEP68AD_B3C3D3_REGULAR_CENTER_NONIBP_BOUNDARY_PARITY.md` : `e3ee970e68edb60f09c5beb24a3052ad8852a801`.
- README actualisé : blob `6c7d4a610810bda3a89f457a37c951865f9871ee`.

**GITHUB :** HEAD initial vérifié `aff5a788fb2c64f27b6f952d73e1808be6369e11` ; quatre `create_file` réels et un `update_file` README sur la **seule** branche `research/gate2b-nonhomothetic-transfer`. Dernier commit scientifique/README avant checkpoint : `104d768f66964cf3956f50c8f41e616b47a6b76b`. HEAD `main` observé `aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw` `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` ; à recontrôler après index. Aucun workflow GitHub Actions modifié.

**LIMITES ET ACTIONS PRIORITAIRES :** (1) Rejouer les moteurs originaux et b3c2 dans un environnement complet ; (2) calculer le pullback de la forme de bord extérieure Step55 sur de vraies variations tangentes aux primaires, secondaire fonctionnelle C(r)=0 et préservation Step58 ; (3) générateurs améliorés/charges, quotient temporel ; (4) Dirac six couples, rang/tertiaires, K=0/J=0, 4D/stabilité/observables. La disparition du bord central n'est **pas** une preuve de différentiabilité globale ni de stabilité JANUS. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d2 FORME NON-IBP COMPLÈTE SUR TRANCHE DIRICHLET (2026-10-28)

**ÉTAPE b3c3d2 TERMINÉE (THÉORÈME CINÉMATIQUE EXACT RESTREINT, NON DIRAC) — PROCHAINE ÉTAPE b3c3d3 : REJEU ORIGINAL STEP45/55/58 ET b3c2, VARIATIONS TANGENTES AUX PRIMAIRES, C(r)=0, PRÉSERVATION TEMPORELLE ET BORDS SUR STEP55 ; GÉNÉRATEURS AMÉLIORÉS, CHARGES, QUOTIENT JAUGE TEMPORELLE, DIRAC SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT RESTREINT :** Sur K>0 et à une extrémité régulière, les six coordonnées canoniques (Lg,Sg,tg,Lf,Sf,tf) et les multiplicateurs N,M,V étant fixés, la forme de bord originale non-IBP **complète restreinte à cette tranche** vaut `Theta_D=dC−Z dP`, avec `P=pLg*(N+M Lg/Lf)`, `Z=D/sqrt(D²+K²)`, `D=pSg*Sg'−Lg*pLg'+pg*tg'`, `C=2 Mg2 N Sg Sg'/Lg+2 Mf2 M Sf Sf'/Lf−V Lg pLg−V Lf pLf`. La dérivation directe des dix coefficients de bord, à partir des densités originales, vérifie `dTheta_D=dP∧dZ` ; donc la fermeture sur une sous-variété lisse de cette tranche équivaut au rang <=1 de (P,Z). Sur `Z=F(P)`, primitive locale `C−∫F(P)dP`. La forme complète restreinte et le secteur IBP de b3c3d1 diffèrent exactement de `d(C−PZ)`. Sur les deux jets libres (pLg,pLg'), courbure négative `−Lg*(N+M Lg/Lf)*K²/(D²+K²)^(3/2)`, témoin rationnel **NON Step55** `−32/375`. **L'extension à lapses variables est fausse en général :** `dTheta(dN,dSg')=2 Mg2 Sg/Lg` (témoin 2), terme non inclus dans dP∧dZ. Les lapses ne sont pas des paires canoniques ; aucune obstruction physique générale n'en découle.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `python -m numerics.hr_step68ad_b3c3d2_full_dirichlet_boundary` : **29 résidus symboliques SymPy exactement nuls + 2 témoins rationnels PASS**. `python -m unittest -v tests.test_hr_step68ad_b3c3d2_full_dirichlet_boundary` : **4 cas PASS**, rejouant les mêmes calculs (non indépendants), **0 FAIL final**. Premier unittest : simple erreur de compteur attendu 28 au lieu de 29, corrigée avant publication, puis quatre tests réussis. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` : **ECHEC DNS** `Could not resolve host: github.com`. Sources originales Step37/45/55/58 consultées via connecteur et SHA authentifiés ; **imports Python originaux Step45/55/58 et test b3c2 NON réexécutés**.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS, SHA GIT BLOB ÉGAUX AUX OCTETS TESTÉS / PRODUITS :**
- `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py` : `6898c88760cc0766e949f9bade4908b9bc176c58`.
- `tests/test_hr_step68ad_b3c3d2_full_dirichlet_boundary.py` : `724f06569fa2de8368e94b28eebea06f56dc81ea`.
- `research/reports/gate2b-step68ad-b3c3d2-full-nonibp-dirichlet.json` : `d24f28d9854bd159e798bc3eac9139e943e48c55`.
- `research/STEP68AD_B3C3D2_FULL_NONIBP_DIRICHLET_RANK.md` : `dd0eea2ed83a162acae8ebf251872c541b4884be`.

**GITHUB :** HEAD à l'ouverture `72123a1d08b8f0ccb26d3a51473e0e9d6103feec` ; HEAD après publication des quatre fichiers et README `9d6b69e7e6ea8926f038a71b45702ad52e312f6a` ; README blob `43c3d8e2249317b876b346cfe4629c00f298885f`. Les fichiers ont été créés réellement sur la seule branche `research/gate2b-nonhomothetic-transfer` et relus avec leurs blobs. Aucun workflow modifié. Contrôler à la fin les HEAD de main et research/v2-flrw.

**LIMITES ET PRIORITÉS :** Les conditions Dirichlet étudiées ne sont **pas** certifiées tangentes aux primaires, secondaire fonctionnelle C(r)=0, opérateur temporel Step58, régularité centrale ou bords conservés. Aucun générateur amélioré/charge ni rang physique n'est établi. (1) Rejouer Step45/55/58+b3c2 en clone si DNS disponible ; (2) construire les variations Dirac admissibles et tester les graphes Z=F(P) sur Step55 ; (3) charges, jauge temporelle, rang/tertiaires Dirac, cartes K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3d1 CRITÈRE DE RANG DU SECTEUR DE BORD (2026-10-28)

**ÉTAPE b3c3d1 TERMINÉE (THÉORÈME CINÉMATIQUE RESTREINT) — PROCHAINE ÉTAPE b3c3d2 : REJEU ORIGINAL STEP45/55/58 ET b3c2, FORME DE BORD NON-IBP COMPLÈTE, VARIATIONS ADMISSIBLES TANGENTES AUX CONTRAINTES, GÉNÉRATEURS AMÉLIORÉS/CHARGES/JAUGE TEMPORELLE, PUIS DIRAC SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**THÉORÈME EXACT LIMITÉ :** À partir des densités Step45 authentifiées, le secteur de la forme de bord associé au terme z' est `alpha_shift=P dZ` avec `P=pLg*(N+M*Lg/Lf)`, `Z=D/sqrt(D²+K²)` sur K>0, `D=pSg*Sg'−Lg*pLg'+pg*tg'`. Il vérifie `d alpha_shift=dP wedge dZ`. Sur une sous-variété lisse de données de bord, le pullback est fermé **ssi** le rang différentiel de (P,Z) est <=1. Les graphes `Z=c0+c1*P+c2*P²` avec |Z|<1 possèdent la primitive explicite `B=c1*P²/2+2*c2*P³/3`; fixer Z ou P fonctionne également **pour ce secteur uniquement**. La tranche libre (pLg,pLg') conserve la courbure négative de b3c3c, témoin rationnel NON Step55 `-32/375`. Ces graphes sont réalisables au niveau des jets par `D=K*Z/sqrt(1-Z²)`, mais **aucune admissibilité physique ni tangence Dirac n'est démontrée**. Le secteur n'est pas la forme non-IBP complète : aucune conclusion sur le pullback physique de dTheta, les charges ou un no-go JANUS.

**TESTS EXÉCUTÉS DANS CETTE SESSION :** `python -m numerics.hr_step68ad_b3c3d_boundary_sector_rank` : 16 assertions exactes SymPy PASS ; `python -m unittest -q tests.test_hr_step68ad_b3c3d_boundary_sector_rank` : 4 tests PASS (rejeu non indépendant), 0 FAIL. `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` : ECHEC `Could not resolve host: github.com`. Les sources Step45/55/58 ont été relues via le connecteur GitHub et leurs blobs authentifiés, mais **les imports Python originaux et le unittest b3c2 n'ont PAS été rejoués**.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS SUR LA SEULE BRANCHE AUTORISÉE :**
- `numerics/hr_step68ad_b3c3d_boundary_sector_rank.py` — blob `ac359aed8e3fadf465c328b2e5a7d7d559665eb5`, identique aux octets exécutés.
- `tests/test_hr_step68ad_b3c3d_boundary_sector_rank.py` — blob `de0aa6e3529f4e26e80f9fba44f8dc4f26d90c0a`, identique aux octets exécutés.
- `research/reports/gate2b-step68ad-b3c3d1-boundary-sector-rank.json` — blob `2c256bada46fb692d755c11c80342419553632ef`.
- `research/STEP68AD_B3C3D1_BOUNDARY_SECTOR_RANK_CLASSIFICATION.md` — blob `c982e5f70d190412086ad24943e65bb9b2687205`.

**GITHUB :** HEAD vérifié à l'ouverture `1a50255f7c458c2ffad4e85482ae2ba6501cdc8f`. Quatre create_file authentiques, relus, et README mis à jour (blob `58df9b2639abb796b7117bf3108f9e59d1318ac1`). Journal préfixé sans suppression du suffixe historique. Après mise à jour de l'index, revérifier le HEAD, et confirmer main et research/v2-flrw inchangées. Aucune GitHub Action modifiée.

**VERROUS ET ACTIONS PRIORITAIRES :** (1) Rejouer b3c2 sur les modules Python Step45/55/58 originaux en clone complet, dès accès réseau ; (2) calculer la forme de bord non-IBP intégrale, pas seulement son secteur shift ; (3) imposer primaires, secondaire C(r)=0, préservation temporelle, régularité centrale et conditions aux bords aux variations avant d'examiner le rang physique ; (4) charges/générateurs améliorés, quotient jauge temporelle, Dirac six couples, cartes K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3c COURBURE RESTREINTE DES JETS DE BORD (2026-10-28)

**ÉTAPE b3c3c TERMINÉE (THÉORÈME CINÉMATIQUE RESTREINT, NON DIRAC) — PROCHAINE ÉTAPE b3c3d : REJEU ORIGINAL b3c2 STEP45/55/58, CLASSIFICATION DES VARIATIONS DE BORD ADMISSIBLES ET GÉNÉRATEURS AMÉLIORÉS, CHARGES/JAUGE TEMPORELLE, PUIS DIRAC SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT LIMITÉ :** Sur la carte K>0 de Step45, après élimination algébrique z*=D/sqrt(D²+K²), la forme de bord issue des densités post-IBP, restreinte à deux variations LIBRES indépendantes de jets d'extrémité (pLg,pLg') avec les autres champs et lapses fixes, a la courbure dα=−Lg*(N+M*Lg/Lf)*K²/(D²+K²)^(3/2) d(pLg)∧d(pLg'). Le coefficient est strictement négatif pour Lg,Lf,N,M,K>0 et D fini. Témoin rationnel NON Step55 : Lg=2/5, Lf=3/5, N=M=1, D=3, K=4 : −32/375. Une variation exacte d'un contreterme ne peut annuler cette courbure sur cette tranche libre. **CE N'EST PAS** une obstruction physique générale : les deux variations n'ont pas été certifiées tangentes aux contraintes fonctionnelles, ni compatibles avec les conditions aux bords ; la réduction à une dimension peut supprimer la courbure. Pas de charge ni générateur amélioré ni pullback physique dTheta.

**TESTS RÉELLEMENT EXÉCUTÉS :** `python -m numerics.hr_step68ad_b3c3c_boundary_jet_curvature` : 15 assertions exactes SymPy PASS ; `python -m unittest -v tests.test_hr_step68ad_b3c3c_boundary_jet_curvature` : 4 tests PASS, non indépendants ; 0 FAIL final. Les scripts publiés ont été exécutés en structure de paquets numerics/tests. Une erreur initiale de substitution du témoin rationnel a été corrigée avant publication ; une erreur de chemin d'import du unittest a été corrigée puis rejouée dans la structure du dépôt. Le GitHub source Step45 a été relu, blob authentifié `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. **Les imports originaux Step45/55/58 et b3c2 n'ont PAS été exécutés en clone complet** (DNS Git indisponible localement).

**QUATRE LIVRABLES PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_b3c3c_boundary_jet_curvature.py` — blob `173516e616ef950927356b110a71006863db5301`, octets testés identiques.
- `tests/test_hr_step68ad_b3c3c_boundary_jet_curvature.py` — blob `1663bc360cd7c6da5f3e8947c1ecb6644578ab9a`, octets testés identiques après correction de l'import.
- `research/reports/gate2b-step68ad-b3c3c-restricted-boundary-jet-curvature.json` — blob `15f569d0da59eb33b49c6deec32966c2caa14bd0`.
- `research/STEP68AD_B3C3C_BOUNDARY_JET_CURVATURE_RESTRICTED.md` — blob `80f9f7df2d4c039deb8444c6ea7ec47dc32a3274`.

**GITHUB :** HEAD authentifié à l'ouverture `0a37234daa8b71ac910b39445aef63b9ca3d2453`. Quatre create_file, un update_file correctif du test et README mis à jour, tous exclusivement sur `research/gate2b-nonhomothetic-transfer`. Relire les SHA après journal et index ; ne pas modifier main, research/v2-flrw, ni workflows désactivés.

**PRIORITÉS :** (1) Rejouer b3c2 avec les vrais imports Step45/55/58 dans un environnement complet ; (2) imposer primaires, secondaire C(r)=0, préservation temporelle et conditions aux bords aux variations (pLg,pLg') avant toute conclusion physique ; (3) calculer la forme de bord complète non-IBP et les charges/générateurs améliorés ; (4) jauge temporelle, rang/tertiaires Dirac, chartes K=0/J=0, 4D, stabilité et observables. Aucune validation ni no-go JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3b IDENTITÉ DE LIE EXACTE DE C_red (2026-10-28)

**ÉTAPE b3c3b TERMINÉE (COVARIANCE LOCALE CINÉMATIQUE EXACTE) — PROCHAINE ÉTAPE b3c3c : REJEU b3c2 AVEC IMPORTS ORIGINAUX STEP45/55/58, VÉRIFICATION INDÉPENDANTE DE C_red, GÉNÉRATEURS AMÉLIORÉS ET CHARGES AUX BORDS, JAUGE TEMPORELLE, PUIS DIRAC SIX COUPLES, K=0/J=0, 4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVELLE PREUVE :** À partir de la transcription Step45 b3c3a dont les octets correspondent au blob Git authentifié, les coefficients exacts du crochet à six couples vérifient K00 poids 1, K01 poids 0, et C_exact=K00−∂rK01 poids 1, par annulation exacte des coefficients de V',V'',V''' (9 identités). Les 12 dérivées de C_exact par rapport aux seconds jets canoniques sont nulles ; ∂C_exact/∂z'=−(K sqrt(1−z²)+Dg z)/(Lg Lf). Sur K>0, z*=Dg/sqrt(Dg²+K²) est scalaire et son vrai gradient radial a poids 1 (3 identités exactes). Par composition, **δ_V C_red=(V C_red)' exactement sur les jets lisses de la carte K>0**, sans supposer C_red=0. Sur C_red(r)=0, la contribution radiale est nulle dans le volume. Ceci lève l'hypothèse cinématique de covariance de b3c3a ; cela ne construit ni générateur différentiable au bord ni charge de bord.

**TESTS EXÉCUTÉS :** 34 assertions symboliques exactes SymPy PASS, 1 unittest de rejeu PASS, 0 échec final. Un premier unittest avait échoué uniquement sur le compteur attendu 35 au lieu de 34, corrigé avant publication ; le code scientifique n'a pas échoué. Le unittest n'est pas indépendant. Le fichier parent b3c3a original publié a été recopié localement avec Git blob identique `e7f068a7c4063a27af2456515b58f8732b3b3343`. Sources physiques originales Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f` et Step57 `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f` authentifiées sur GitHub. Les moteurs Python Step45/55/58 originaux et le unittest b3c2 n'ont PAS été exécutés en clone complet.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_b3c3b_cred_lie_identity.py` — blob `010e5e10c071d4cfb270c32fb1d73ad94e77896f`, identique aux octets exécutés.
- `tests/test_hr_step68ad_b3c3b_cred_lie_identity.py` — blob `f641e9176ebdafc49742a8786165a1f11db9953f`, identique aux octets exécutés.
- `research/reports/gate2b-step68ad-b3c3b-cred-exact-lie.json` — blob `b92eec5b1e97134de1d960461483cdf511e2c66b`.
- `research/STEP68AD_B3C3B_EXACT_REDUCED_SECONDARY_RADIAL_LIE_IDENTITY.md` — blob `c8e8414d73ae27f282267208ccaf1bc3ca10f1cc`.

**GITHUB :** HEAD authentifié à l'ouverture `4aa7e86fde62d4207f115fec0844394985b07403`. Quatre create_file effectifs, relus et comparés ; README mis à jour au blob `93342fda6ab0f8cbc72f0de8d700c3940f5a615f`, commit `d9c0bff9f33db13e941dfc690931153b6df76788`. La branche `research/gate2b-nonhomothetic-transfer` est la seule cible ; `main` et `research/v2-flrw` doivent rester inchangées ; GitHub Actions désactivées non touchées.

**LIMITES ET PRIORITÉS :** (1) rejeu indépendant b3c2 sur les imports originaux et comparaison des quatre coefficients exacts ; (2) vérification indépendante de la formule complète C_red et des conditions de bord avec un générateur amélioré ; (3) charges, jauge temporelle, lapses et rang Dirac à six couples ; (4) chartes K=0/J=0, dynamique 4D, stabilité et observables. Aucun no-go général ni validation JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : b3c3a AUDIT COVARIANCE DU SHIFT DIAGONAL (2026-10-28)

**ÉTAPE b3c3a PARTIELLE TERMINÉE — 16 IDENTITÉS EXACTES SYMPY PASS, 1 UNITTEST DE REJEU PASS, 7 SIGNES RATIONNELS BIGINT PASS, 0 FAIL. PROCHAINE ÉTAPE : b3c3b — REJOUER b3c2 DANS UN CLONE COMPLET AVEC LES MODULES STEP45/55/58 ORIGINAUX, VÉRIFIER L'IDENTITÉ DE LIE DE LA SECONDAIRE RÉDUITE, GÉNÉRATEURS AMÉLIORÉS/CHARGES/JAUGE, PUIS DIRAC SIX COUPLES, K=0/J=0, 4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT :** La transcription algébrique des densités originales Step45 a été soumise aux prolongations infinitésimales du difféomorphisme radial diagonal. Pour Ag,Bg,Af,Bf,Dg,K,Fz,C_zprime, les deux identités exactes de covariance sont vérifiées (poids respectifs 1,0,1,0,2,2,2,0), soit 16 égalités symboliques PASS. Dg et K sont de poids 2, le shift relatif réduit z*(Dg,K) est scalaire sur K>0. Sous l'hypothèse d'un générateur radial différentiable et d'une secondaire C_red covariante de poids 1, son terme de shift diagonal en volume est (V C_red)' et disparaît sur C_red(r)=0. L'identité complète sur C_red n'a PAS été directement vérifiée : ce dernier point reste conditionnel, en particulier aux bords. Le rapport central b3c2 implique conditionnellement 2407/5000 < dot(tg-tf)(0)/N(0) < 963/2000.

**TESTS EXÉCUTÉS :** 16 identités SymPy exactes PASS, 1 unittest PASS (rejeu des mêmes identités), 7 contrôles rationnels BigInt V8 indépendants sur le certificat b3c2 PASS, 0 FAIL. Les moteurs originaux Step45/55/58 et le unittest b3c2 n'ont pas été rejoués en clone complet : accès réseau Git indisponible dans le conteneur. Sources SHA authentifiées : Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; Step58 802c23aebd41780d8c462f1aa1711707fe4ee88f ; Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe ; Step57 bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f.

**FICHIERS PUBLIÉS/RELUS :**
- numerics/hr_step68ad_b3c3a_diagonal_shift_covariance.py — e7f068a7c4063a27af2456515b58f8732b3b3343 (identique aux octets exécutés).
- tests/test_hr_step68ad_b3c3a_diagonal_shift_covariance.py — c82a474173f931f18881344489fd30e426d1a6de (identique aux octets exécutés).
- research/reports/gate2b-step68ad-b3c3a-diagonal-shift-covariance.json — 4934626b47262fa2bb7f94007258571eddb61008.
- research/STEP68AD_B3C3A_DIAGONAL_SHIFT_COVARIANCE_PARTIAL_AUDIT.md — 0643a5e4adb6a88c497f06783c814032a995441a.

**GITHUB :** HEAD initial 9b995e203955be609812232922176571f3050751, HEAD après quatre livrables 8e09450e3df3dd085861615c671f7ccc4c92b50a ; vérifier le HEAD final après journal/index/README. Branche autorisée research/gate2b-nonhomothetic-transfer seulement ; ne modifier ni main, ni research/v2-flrw, ni workflows. Aucun résultat de rang physique Dirac, charge temporelle, stabilité 4D ou validation JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR INTÉGRALEMENT CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2b3c2, COEFFICIENTS CENTRAUX EXACTS STEP58 (2026-10-28)

**ÉTAPE b3c2 TERMINÉE — RÉSULTAT LOCAL EXACT SUR STEP55, INCOMPATIBILITÉ CONDITIONNELLE D'UNE HORLOGE RELATIVE STATIONNAIRE, PAS DE NO-GO JANUS. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b3c3 — REJOUER DANS CLONE COMPLET LES SOURCES PYTHON ORIGINALES ET LE TEST PUBLIÉ ; AUDITER LES TERMES DE JAUGE/SHIFT ET LA PRÉSERVATION FONCTIONNELLE, PUIS GÉNÉRATEURS TEMPORELS AMÉLIORÉS, CHARGES, QUOTIENT DIRAC, SIX COUPLES/RANG/TERTIAIRES/K=0/J=0/4D/STABILITÉ/OBSERVABLES. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT MATHÉMATIQUE :** Sur le centre analytique authentique Step55, l'opérateur original Step58 donne `A_N(r)=a_N r²+O(r⁴)`, `A_M(r)=a_M r²+O(r⁴)`. Les coefficients de `N',M',N'',M''` n'ont aucun terme d'ordre <=3 dans la série formelle exacte ; pour lapses sphériques lisses, ils n'affectent pas l'ordre r². Les coefficients `a_N,a_M` sont des éléments explicites de `Q(sqrt(H2))` donnés exactement dans le JSON. Inégalités rationnelles strictes : `3507<a_N<3508`, `-6765<a_M<-6764`, `1037/2000<-a_N/a_M<2593/5000` (affichage ~0.518543059543765887). Sous préservation temporelle Step58 et `N(0)>0`, le rapport central requis est `M(0)/N(0)=-a_N/a_M`, incompatible avec `M(0)=N(0)` exigé pour une différence d'horloges stationnaire au centre. Ceci exclut **cette combinaison de conditions**, pas le modèle JANUS. Les coefficients libres u1..u7 ont été gardés symboliques ; les 28 dérivées du coefficient dominant par rapport à ces jets sont exactement nulles ; contrôle de valuation pour la queue analytique.

**TESTS RÉELLEMENT EXÉCUTÉS :** 190 comparaisons symboliques/algébriques exactes sur une reconstruction locale source-fidèle Step45/58, 0 FAIL ; 6 comparaisons de signes exactes BigInt V8 sur les fractions publiées, 0 FAIL ; sonde numérique haute précision à huit rayons exploratoire. Sources Step45 SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step58 SHA `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 SHA `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` authentifiées directement sur GitHub. **Moteurs Python originaux et unittest publié NON réexécutés dans un clone complet** ; ne pas compter des tests historiques.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS/RELUS :**
- `numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` — blob `9a77f749a040aaec37e7c3f01368013154fdb562`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` — blob `d0174425b2f43d6a7572e05cbd44bcb303cd78a3`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2b3c2-center-operator.json` — blob `4daa3b6ae9e6447eb380e512419ae4e7eaf2fedf`.
- `research/STEP68AD_C2D2E5B3B2C2B2D2D2B3C2_EXACT_STEP58_CENTRAL_OPERATOR_RATIO.md` — blob `40f5decd8fb3ac082808376496ae8b4054cf391e`.

**GITHUB :** HEAD initial authentifié `bbaba5aaec55d266ffc02467615ea2df9737642e`. Quatre create_file effectifs sur la seule branche `research/gate2b-nonhomothetic-transfer`, fichiers relus et SHA authentifiés ; README actualisé. HEAD avant ce checkpoint `cc05a7341267a1562fa6a2a7f2de4cbe0716e41e`. Vérifier HEAD final après index ; ne jamais modifier `main`, `research/v2-flrw` ni GitHub Actions.

**LIMITES ET ACTIONS PRIORITAIRES :** (1) Rejouer le nouveau script et unittest dans un clone complet avec les modules originaux et vérifier les 4 fractions exactes ; (2) vérifier séparément la réduction du shift diagonal et les bords des générateurs temporels, les charges et la jauge ; (3) résoudre ou réfuter l'existence de lapses globaux pour des données de bord physiquement admissibles ; (4) compléter l'oracle fonctionnel Dirac non-IBP six couples, rang, tertiaires, chartes K=0/J=0, 4D, stabilité, observables. Aucun verdict JANUS-R ne peut être changé à ce stade.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2b3c1, COURBURE NÉCESSAIRE DES LAPSES ENTRE CENTRE ET ANNEAU (2026-10-28)

**ÉTAPE b3c1 TERMINÉE : THÉORÈME CONDITIONNEL DE COUCHE CENTRALE, PAS DE LIMITE CENTRALE STEP58 CERTIFIÉE. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b3c2 — développer les coefficients originaux Step58 A_N,A_M et les jets N',M' au centre sur Step55, vérifier la réduction fonctionnelle, déterminer la limite réelle M/N et borner sa dérivée seconde avant toute conclusion de régularité ; ensuite générateurs temporels améliorés/charges, quotient jauge, Dirac non-IBP six couples/rang/tertiaires/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU RÉSULTAT EXACT CONDITIONNEL :** La première feuille authentique du certificat original Step58 (SHA `0c688d6648e16064b1eb4e8ad9c55e7b44a95947`) certifie au point r=1/64 `rho=M/N=-A_N/A_M<17/25`, sous l'hypothèse toujours ouverte que les jets de lapses disparaissent sur la coquille complète. Sur Step55, avec N(0)>0 et une différence d'horloges stationnaire jusqu'au centre, un shift Vrel fini impose rho(0)=1 ; la parité des lapses lisses impose rho'(0)=0. Si rho est C² jusqu'à r=1/64 et satisfait aussi la relation réduite Step58 à cette borne, il existe `eta,xi∈(0,1/64)` avec `rho'(eta)<-512/25` et `rho''(xi)<-65536/25`. Ceci n'est PAS une singularité ni un no-go : aucune borne physique sur rho'' n'est disponible. Les coefficients centraux exacts sont `d0=3321926807006261/3906250000000000000` et `ccrit=226687120771331833/18086585087578262500000` ; si `rho=1+rho2*r²+O(r⁴)`, alors `Vrel/N=r*(rho2-ccrit)/d0+O(r³)`.

**TESTS EXÉCUTÉS :** 921 assertions exactes BigInt V8 PASS, 0 FAIL ; quatre falsifications rejetées ; trois identités asymptotiques vérifiées séparément par SymPy, 0 FAIL. Le programme a été relu depuis GitHub et réexécuté sur le certificat authentifié. Test Node CLI publié mais NON exécuté ; moteurs Python originaux Step58/Step55 NON réexécutés. Aucune preuve de la limite Step58 à r=0, de la réduction complète des jets de lapses, de l'existence globale de lapses, de la différentiabilité améliorée, du quotient de jauge temporelle ou du rang Dirac.

**LIVRABLES SCIENTIFIQUES PUBLIÉS/RELUS :**
- `scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c1_center_boundary_layer.cjs` — blob `7735e10a798a038cd56a0f6de189bcff92d7c118`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b3c1_center_boundary_layer.cjs` — blob `cbe7d24553a8b47a4a399549cd95157c32ead52b`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2b3c1-center-boundary-layer.json` — blob `29f09b76877160157637cafce5719804f1b0c6cc`.
- `research/STEP68AD_C2D2E5B3B2C2B2D2D2B3C1_CENTER_TO_ANNULUS_LAPSE_CURVATURE_NECESSITY.md` — blob `82ba0e4303897f3cbecc6128eb8d5b5146c7cf08`.
- Sources originales SHA authentifiées : Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, certificat `0c688d6648e16064b1eb4e8ad9c55e7b44a95947`.

**GITHUB :** HEAD initial authentifié `5637ae49dd42e1b85be81f12fc36307a40d7b4a9`. Quatre fichiers scientifiques créés et relus uniquement sur `research/gate2b-nonhomothetic-transfer`. HEAD de pré-checkpoint `92af7be656f85fe16b9fb6245ff62e51b743144d`. Vérifier HEAD final après index. Branches main et research/v2-flrw protégées, aucun workflow GitHub Actions touché.

**ACTIONS PRIORITAIRES :** (1) Étudier l'opérateur Step58 original sur la parité centrale et calculer le quotient des coefficients d'ordre dominant ; (2) vérifier les coefficients N',M' sur la coquille de Dirac, non les supprimer par hypothèse ; (3) tenter une borne indépendante sur rho'' et vérifier la régularité de Vrel ; (4) reprendre générateurs temporels améliorés/charges, quotient de jauge, matrice Dirac et problèmes 4D/stabilité/observables.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2b3b, STEP58 ET HORLOGE RELATIVE (2026-10-28)

**ÉTAPE b3b TERMINÉE : NOUVEAU THÉORÈME CONDITIONNEL DE SOUS-ANNEAU, PAS DE NO-GO PHYSIQUE. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b3c — certifier la limite centrale r→0 du rapport temporel Step58 M/N=-A_N/A_M sur la branche Step55, confronter la condition nécessaire M(0)=N(0) pour préserver t_g−t_f avec shift régulier, puis construire générateurs temporels améliorés et charges, quotient de jauge, oracle Dirac non-IBP six couples/rang/tertiaires/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT PROUVÉ CONDITIONNEL :** Le certificat authentique Step58 `0c688d6648e16064b1eb4e8ad9c55e7b44a95947` a été audité sur 225 feuilles rationnelles couvrant exactement `r∈[1/64,1/32]` ; sous l'hypothèse que les termes de dérivées de lapses s'annulent effectivement sur la coquille complète, `M/N=-A_N/A_M<3/4` est certifié sur **154 feuilles**, en deux bandes `[1/64,225/14336]` (2 feuilles) et `[37/1792,1/32]` (152 feuilles). **71 feuilles sont INCOMPLETE pour cette borne**, sans contre-exemple physique. Avec Step55 et la condition instantanée `dot(tg−tf)=0`, `Vrel/N<−39880/7` et `|Lf Vrel|/M>31904/21` sur ces seules bandes. Pour le shift f diagonal V, `f_tt>0` : le vecteur de coordonnées ∂t est spatial en cette jauge, **pas** une perte de signature ni une incohérence physique. Au centre régulier, `dot(tg−tf)(0)=N(0)−M(0)`, donc stationnarité relative impose `M(0)=N(0)`; la limite du rapport Step58 au centre n'est PAS certifiée.

**TESTS RÉELLEMENT EXÉCUTÉS :** 1 147 assertions rationnelles exactes BigInt V8 PASS, 0 FAIL ; 4 entrées falsifiées rejetées ; rejeu depuis le programme publié et comparaison du certificat publié aux données recalculées. Le fichier de test Node est publié mais **pas exécuté sous Node CLI** ; les moteurs physiques Python originaux Step58/55 NON réexécutés dans cette session. SHA sources originaux relus : Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, b3a `edf4dd6c8ab3fea9579195c130b096dee7b7353a`.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- `scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3b_step58_relative_clock.cjs` — blob `11b81157ec2acb0f76f087b97da736f2b6fa71d1`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b3b_step58_relative_clock.cjs` — blob `74f9120912d0783cedffdf64217be2b3893fe6b0`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2b3b-step58-relative-clock.json` — blob `15ffd1369d36d66d5da2ab45655b694c65e37d45`.
- `research/STEP68AD_C2D2E5B3B2C2B2D2D2B3B_STEP58_RELATIVE_CLOCK_SUBANNULUS.md` — blob `b85d01b3cc74458ccc914111e9a7cbbd04906f08`.
- `README.md` — blob `7022508dd68df210ee2906d8316e846c77845f44`.

**GITHUB :** HEAD initial authentifié `23671226db65ffec977c1b6b2e7158a96270cf08`; 4 nouveaux fichiers et README publiés exclusivement sur `research/gate2b-nonhomothetic-transfer`. Les blobs du programme et du certificat ont été relus ; le programme exécuté sur octets GitHub produit le certificat attendu. HEAD final à relire après l'index. Branches `main` et `research/v2-flrw` vérifiées inchangées avant synchronisation ; aucun workflow GitHub Actions touché.

**VERROUS / ACTIONS PRIORITAIRES :** (1) Vérifier `M/N` au centre `r=0` avec opérateur Step58 authentique et réduction des jets de lapses, sans extrapoler depuis les bandes. (2) Tester `Vrel` avec la parité/régularité du shift et la différentiabilité du Hamiltonien amélioré. (3) Construire les charges et le quotient temporel Dirac, puis les directions physiques non-jauge et `dTheta`. (4) Poursuivre rang complet, tertiaires, chartes K=0/J=0, dynamique 4D, stabilité et observables ; ne jamais proclamer JANUS-R validé.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2b3a, PRÉSERVATION TEMPORELLE DES HORLOGES (2026-10-28)

**ÉTAPE b3a TERMINÉE : THÉORÈME EXACT CONDITIONNEL SUR LES SIGNES STEP55, PAS DE GÉNÉRATEUR TEMPOREL AMÉLIORÉ NI QUOTIENT DIRAC. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b3b — confronter Vrel à l'opérateur original Step58 de préservation des lapses et à la régularité, construire les générateurs temporels améliorés, charges et conditions de bord différentiables ; puis deux directions physiques non-jauge, dTheta, Dirac six couples/rang/tertiaires/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT PROUVÉ :** À partir du Hamiltonien non-IBP original, dot(tg)=N*sqrt(1+(tg'/Lg)^2)+(z*(N/Lg+M/Lf)+V)*tg' et dot(tf)=M*sqrt(1+(tf'/Lf)^2)+V*tf'. Sur Step55 R=17/20, tg'>0, tf'<0, z>0 et N,M>0 : aucun V fini ne permet dot(tg)=dot(tf)=0 au bord extérieur. Au centre régulier tg'=tf'=0, des Dirichlet individuels CONSTANTS DANS LE TEMPS imposent N(0)=M(0)=0, incompatibles avec des lapses strictement positifs. Fixer seulement la différence tg-tf permet un unique Vrel=(M*sf-N*sg-z*Q*tg')/(tg'-tf') et une vitesse commune strictement positive. Il s'agit d'une condition de compatibilité INSTANTANÉE, pas d'une solution globale Dirac.

**CHARGES :** Le calcul de volume donne dot(pg)=d_r Jg, dot(pf)=d_r Jf et formellement dot(Qi)=Ji(R)-Ji(0), Qi=int pi dr. Ceci NE démontre PAS la conservation des charges, ni la différentiabilité du générateur. Un témoin rationnel NON Step55 distingue Vrel=-2/5 et Vflux=-11/65 : au premier, Jg+Jf=-15/13. Préserver la différence des horloges ne supprime donc pas automatiquement le flux diagonal nu.

**TESTS :** 37 assertions BigInt exactes V8 PASS, 0 FAIL ; réexécutées depuis les octets publiés GitHub ; 6 gardes de wrapper PASS, NON indépendants, via shim V8 et non Node CLI ; certificat JSON régénéré identique. Sources originales Step37/45/55 et forme d2a relues avec SHA Git authentifiés ; moteurs Python originaux NON réexécutés.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3a_clock_time_evolution.cjs — blob edf4dd6c8ab3fea9579195c130b096dee7b7353a.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b3a_clock_time_evolution.cjs — blob ab314845598539a289f16d26b7df5fbc31bb5143.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2b3a-clock-time-evolution.json — blob e9905838241f8d6e50c35753221bbfeb361066b4.
- research/STEP68AD_C2D2E5B3B2C2B2D2D2B3A_CLOCK_TIME_EVOLUTION_BOUNDARY_PRESERVATION.md — blob f0756adb6b98574700591ae8cb8a1b10bbc60eb9.

**GITHUB :** HEAD initial relu fafe66a498518deeb93241e783449b49886385d5 ; quatre create_file réels sur research/gate2b-nonhomothetic-transfer, fichiers relus et comparés aux octets testés. HEAD final à relire après index. main et research/v2-flrw protégées ; ne toucher aucun workflow GitHub Actions.

**LIMITES :** Pas de quotient temporel Dirac, de charges physiques certifiées, de contreterme global admissible, de lapses préservant simultanément la secondaire et les bords, de rang/tertiaires six couples, de chartes K=0/J=0, de dynamique 4D, stabilité ou observables.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2b2, FLUX DE BORD DES HORLOGES ET CONDITIONS ADMISSIBLES (2026-10-28)

**ÉTAPE d2d2b2 TERMINÉE : THÉORÈME EXACT RESTRICTION STEP55/BARE NON-IBP, PAS DE QUOTIENT DE JAUGE TEMPORELLE. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b3 — générateurs temporels améliorés, charges d'horloges, conditions au centre et à R préservées dans le temps, quotient par la jauge temporelle ; ensuite directions canoniques physiques, pullback dTheta, bords/contretermes, oracle Dirac original six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT RESTREINT :** Sur la frontière Step55 R=17/20, avec pg,pf>0, N,M>0, Lg,Lf>0, z=17/5000>0, tg'>0 et tf'<0, les coefficients de bord du Hamiltonien original nu sont Jg/pg=N*A+M*B+V et Jf/pf=M*D+V, où A=tg'/(Lg²sqrt(1+(tg'/Lg)²))+z/Lg>0, B=z/Lf>0 et D=tf'/(Lf²sqrt(1+(tf'/Lf)²))<0. Pour Jg=0 il faut V<0 ; pour Jf=0 il faut V>0. Aucun V réel ne rend simultanément les deux flux nuls à lapses positifs, SANS contreterme ni restriction des variations. La matrice des coefficients (N,M) a déterminant pg*pf*A*D<0, donc rang 2 pour des lapses indépendants. La forme sur le plan des horloges à autres variables fixées est exacte et admet une primitive ; cela ne produit PAS un contreterme sur l'espace canonique/multiplicateur étendu, dont la courbure mixte est non nulle. Les conditions Dirichlet au centre peuvent éliminer les translations constantes même si le bord extérieur est libre ; fixer seulement tg-tf laisse une translation diagonale. Aucune classification de jauge TEMPORELLE ni préservation temporelle des conditions n'est obtenue.

**TESTS EXÉCUTÉS :** 57 assertions rationnelles exactes BigInt V8 PASS, 0 FAIL, réexécutées depuis le code relu sur GitHub ; 10 gardes de test supplémentaires PASS via shim CommonJS V8 (NON indépendants, pas une exécution Node CLI). Certificat JSON régénéré identique octet pour octet à GitHub. Aucun moteur physique original Python réexécuté ; sources Step37/45/55/58 et formes de bord SHA authentifiées.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b2_clock_boundary_flux.cjs — blob 006ad7eca13d70c872b3972c9eb137b94d12a7c1.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b2_clock_boundary_flux.cjs — blob 9f488f3c8850fdc69a81b6c98d94d83b5f806c18.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2b2-clock-boundary-flux.json — blob 8c0c6aa44d60ac8afd9514f0f34157fe7ee2a072.
- research/STEP68AD_C2D2E5B3B2C2B2D2D2B2_CLOCK_BOUNDARY_FLUX_AND_TEMPORAL_GAUGE_LIMITS.md — blob 0b7fd3858863a13c33b37a5aa8f27a6417bfc724.

**GITHUB :** HEAD initial authentifié 08dfd449a1c8c6d72a9d1da5fe1076703804d99d. Écritures sur research/gate2b-nonhomothetic-transfer UNIQUEMENT. Vérifier HEAD final après mise à jour de l'index ; protéger main, research/v2-flrw, workflows désactivés.

**VERROUS :** Le résultat ne prouve pas qu'une condition de bord donnée est compatible avec le problème de Dirac ni que les translations sont des charges physiques plutôt qu'une jauge temporelle. Aucun rang de Dirac complet, contreterme global admissible, équation de lapses temporelle, K=0/J=0, dynamique 4D, stabilité ou observable validé.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2b1, TRANSLATIONS CANONIQUES DES HORLOGES DE POUSSIÈRE (2026-10-28)

**ÉTAPE d2d2b1 TERMINÉE : SYMÉTRIE EXACTE DE VOLUME, RANG 2 DES TRACES D'HORLOGES MODULO JAUGE RADIALE, MAIS PAS DEUX DIRECTIONS PHYSIQUES DIRAC. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b2 — classifier les charges de translation face à la jauge TEMPORELLE, aux conditions t_i(0)/t_i(R), aux générateurs améliorés et à la préservation temporelle ; ensuite rechercher deux directions non-jauge admissibles, pullback dTheta, bords/contretermes, oracle original non-IBP six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT :** Les translations constantes indépendantes Xg: δtg=1, Xf: δtf=1 (toutes autres variations canoniques nulles) sont canoniques. Les densités originales Hg,Hf,Ddiag,Fz, le shift réduit z*, les densités IBP Step45 et tous leurs descendants de Poisson dans le VOLUME ne dépendent pas des valeurs tg,tf ; les deux translations les préservent exactement. Sur la géométrie Step55, Sg',Sf'>0 : ces directions ont rang 2 dans les traces (δtg(R),δtf(R)) modulo les SEULS difféomorphismes radiaux. Les coefficients de la forme de bord originale sont Θ[Xg]=pg[N tg'/(Lg² sqrt(1+(tg'/Lg)²))+z(N/Lg+M/Lf)+V] et Θ[Xf]=pf[M tf'/(Lf² sqrt(1+(tf'/Lf)²))+V]. dΘ(Xg,Xf)=0 EXACT, plan ISOTROPE et non noyau de toute la 2-forme. Sur Step55 à R=17/20, N=M=1,V=0, pg,pf>0, Θ[Xg]>0 et Θ[Xf]<0. La variation totale du Hamiltonien sous translation constante peut rester nulle grâce à la compensation volume/bord. Ne PAS assimiler ce rang 2 radial à un rang physique : la jauge temporelle, les conditions d'horloge au centre/au bord et les lapses complets ne sont pas traités.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** 48 assertions symboliques exactes SymPy PASS, 0 FAIL dans le programme local ; 1 unittest de rejeu PASS (les mêmes 48 assertions, NON indépendant). Les fichiers de code publiés ont les SHA Git identiques aux octets exécutés ; le certificat JSON est identique aux octets générés. Moteurs Python originaux Step45/55/58 NON réexécutés. Sources originales relues/SHA authentifiés : Step37 005449ade6e3582e3b9a5c3374a881a77e73e3f6 ; Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; Step58 802c23aebd41780d8c462f1aa1711707fe4ee88f ; Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe ; kernel original 45ccd73177cc1588efaf1d53e3dd0179d41ec30b ; forme de bord d2a 94bd7e089ebb0978569361c03a4f3ab950b950df.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b1_clock_translation.py — blob 1d973e04f296df9144f6ddef40681dd18342e28e.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b1_clock_translation.py — blob 945b0327c631c131d7e31bda865283283448fc88.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2b1-clock-translation.json — blob 50586bd81a9cdf35e966e6a13504bdf28906345f.
- research/STEP68AD_C2D2E5B3B2C2B2D2D2B1_DUST_CLOCK_TRANSLATIONS_AND_BOUNDARY_ISOTROPY.md — blob b419859f173794471a4eed253d27a6ae1ce0960e.

**GITHUB :** HEAD initial authentifié 103770128d44146a886da1fab713c1ee2f988a42 ; quatre nouveaux livrables + README + journal + index à synchroniser sur research/gate2b-nonhomothetic-transfer UNIQUEMENT. Ne toucher ni main, ni research/v2-flrw, ni workflows désactivés. HEAD final à relire après index.

**VERROUS :** (1) Déterminer si les deux translations sont globales physiques, jauge temporelle, ou exclues par les bords. (2) Déterminer le rang de traces après quotient complet et préservation temporelle ; (3) calculer la courbure sur de véritables directions canoniques admissibles ; (4) Dirac original non-IBP six couples, lapses, rang, tertiaires, K=0/J=0, 4D/stabilité/observables. Aucune validation cosmologique.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d2a, NOYAU DE JAUGE DES TANGENTES CANONIQUES (2026-10-27)

**ÉTAPE d2d2a TERMINÉE : LEMME STRUCTUREL EXACT, PAS UNE SOLUTION DIRAC. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2d2b — chercher des variations CANONIQUES NON-JAUGE à traces de bord indépendantes modulo difféomorphismes, satisfaisant primaires, secondaire C(r)=0 et préservation temporelle ; puis pullback de dTheta, bords/contretermes/lapses, oracle Dirac six couples/rang/tertiaires/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT :** Deux générateurs radiaux `eta1=x^4(1-x)^4`, `eta2=x*eta1`, x=r/R, sont indépendants et plats au bord jusqu'à l'ordre 3. Ils induisent les variations canoniques `delta X=eta X'+w eta' X` sur les SIX couples, et annulent toutes les variations des 12 champs et leurs jets jusqu'à l'ordre 2 aux deux frontières. Les identités exactes `delta Dg=eta Dg'+2 eta' Dg`, idem Df et K HR, confirment la covariance des densités et du shift z* scalaire sur K>0. Le tiré-en-arrière de Theta original non-IBP et de dTheta sur ces deux directions est NUL : le seul critère « deux directions indépendantes » ne suffit donc pas ; il faut des directions à traces de bord NON-JAUGE indépendantes. Les polynômes sont plats aux bords, PAS strictement à support compact ; une coupure C∞ intérieure fournit des variantes compactes. La tangence aux contraintes fonctionnelles/à leur préservation temporelle est CONDITIONNELLE à l'existence d'une solution complète et à la covariance des multiplicateurs, NON vérifiée ici sur Step55.

**TESTS EXÉCUTÉS :** 211 assertions BigInt EXACTES PASS dans V8 avant publication, 0 FAIL ; 211 PASS en rejeu sur octets GitHub et 4 gardes de wrapper vérifiés (non indépendants). Source originale Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e, Ward 89e7f6eab35d28317f2f7a4330601736525487e5, Step58 802c23aebd41780d8c462f1aa1711707fe4ee88f et audit d2d1 1ba6d012133a92b69a8c91498d065b22649afbe0 relus sur GitHub. Aucun moteur Python physique original réexécuté ; témoins polynomiaux NON physiques.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS :**
- `scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2a_gauge_tangent_kernel.cjs` — blob `1d047b8653af8b0dd8cee3735c29c1bc502983e3`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2a_gauge_tangent_kernel.cjs` — blob `4783099f702e7805c03ec7529854e846ec0aca70`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d2a-gauge-tangent-kernel.json` — blob `363a34d59bf3046baec0168efb8b59eaa98b04bf`.
- `research/STEP68AD_C2D2E5B3B2C2B2D2D2A_GAUGE_TANGENT_BOUNDARY_KERNEL.md` — blob `21d2dfacead128479844d88804926b716a7841ab`.

**GITHUB :** HEAD initial `f617d71e9182a74f706da7b44f69c935c24a3caf`. Écritures exclusivement sur `research/gate2b-nonhomothetic-transfer` ; protéger `main`, `research/v2-flrw` et les workflows désactivés. HEAD final à relire après index.

**LIMITES ET ACTIONS PRIORITAIRES :** (1) Pas de rang Dirac, de contreterme physique, de lapse déterminé, de seconde direction NON-JAUGE Step55. (2) Construire le quotient des traces de bord par jauge, vérifier sa dimension sur le vrai linéarisé des contraintes. (3) Contrôler préservation temporelle et bords, puis oracle original six couples. (4) Ne pas confondre covariance cinématique et existence d'une solution temporelle complète.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2d1, COURBURE MIXTE DES MULTIPLICATEURS SUR LA FAMILLE SPATIALE STEP55 (2026-10-27)

**ÉTAPE d2d1 TERMINÉE, RÉSULTAT EXACT/ENCADRÉ MAIS NON DIRAC. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b2d2d2 — trouver au moins deux variations CANONIQUES indépendantes tangentes à la secondaire fonctionnelle C(r)=0, primaires, régularité et préservation temporelle ; évaluer le pullback de dTheta, bords/lapses/contretermes puis Dirac original six couples/rang/tertiaires/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT :** sur la famille spatiale authentique Step55/68o, à R=17/20, géométrie et shift HR fixes, a=∂lambda pLg=92730563/128000000>0, 196809/40000000< b=∂lambda pLf <199121/40000000. La forme de bord non-IBP se tire en arrière comme Theta=F d(lambda), F=-z a(N+q M)-V(Lg a+Lf b), z=17/5000, q=Lg/Lf>0. À multiplicateurs fixes, dTheta=0 sur la famille canonique 1D par dimension : aucune obstruction ambiante ne peut en être déduite. Sur l'espace étendu (lambda,N,M,V), dTheta=(-za)dN∧d(lambda)+(-zqa)dM∧d(lambda)-(Lg a+Lf b)dV∧d(lambda), trois coefficients strictement négatifs, les deux premiers EXACTS et le troisième ENCLOS rationnellement. Les multiplicateurs ne sont PAS des paires canoniques. Aucune seconde direction canonique tangentielle complète, ni condition de bord physique, ni fermeture Dirac n'est établie.

**TESTS :** V8 35 assertions BigInt rationnelles PASS, 0 FAIL ; wrapper 4 invariants PASS rejouant le même programme (non indépendant). Sources Step37/45/46/55 SHA authentifiées et certificat b2c f relu ; moteurs Python originaux NON réexécutés. Programme et certificat relus après publication et comparés octet pour octet.

**FICHIERS SCIENTIFIQUES PUBLIÉS ET SHA BLOBS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b2d2d1_step55_multiplier_curvature.cjs — 2d646edb9c571ef75ef0e3d3448ad53a0b59b42a
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d1_step55_multiplier_curvature.cjs — 103c20deb16c3b6903eecae047ebcc154e8fde03
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d1-step55-multiplier-curvature.json — 5bdfe6a7297a4d0e1296d3f4abe250d3e0c8ca24
- research/STEP68AD_C2D2E5B3B2C2B2D2D1_STEP55_SPATIAL_SHELL_MULTIPLIER_CURVATURE.md — 1ba6d012133a92b69a8c91498d065b22649afbe0
- README.md — f70eeb0e1cd0caf7329bce12fa55076e4bb5a9a3.

**GITHUB :** HEAD initial 6a69648cb7596ac2ad0ab043593275ffd8a16fa6. Écritures exclusivement sur research/gate2b-nonhomothetic-transfer ; main et research/v2-flrw, workflows désactivés intouchés. Relire HEAD final après index.

**LIMITES ET PRIORITÉS :** (1) Ne pas confondre l'espace spatial 1D, l'espace étendu des multiplicateurs et la vraie surface Dirac. (2) Construire variations canoniques fonctionnelles indépendantes à C(r)=0 avec contraintes temporelles ; tester i*dTheta. (3) Définir polarisation de bord, lapses/shift, contretermes et préservation. (4) Oracle non-IBP six couples, rang/tertiaires, K=0/J=0, 4D, stabilité, observables. Aucune validation JANUS.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2c, TÉMOIN DE COURBURE SUR CONTRAINTES PRIMAIRES PONCTUELLES (2026-10-27)

**ÉTAPE d2c PARTIELLE TERMINÉE ; PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b2d2d — imposer la secondaire FONCTIONNELLE C(r)=0, les jets radiaux et les contraintes de préservation temporelle, calculer les véritables variations tangentes Dirac et le pullback de dTheta ; ensuite conditions de bord/lapses/contretermes, oracle original non-IBP six couples, rang, tertiaires, K=0/J=0, dynamique 4D, stabilité et observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT ET LIMITÉ :** pour une interaction témoin beta1=1/50, autres beta=0 (NON paramètres Step55), et des données de bord régulières Lg=2,Lf=3,Sg=5,Sf=7,Sg'=Sf'=1,Sg''=Sf''=-2,pSg=4,pLf=3,pSf=0,tg'=tf'=0,N=M=1,V=0, poser x=pLg, y=pLg', Dg=4-2y, K=3, z*=Dg/sqrt(9+Dg²), pLf'=Dg/3 et résoudre les deux poussières par pg=-Hg0(x,y), pf=-Hf0(x,y). Alors Hg=Hf=Dg+Df=Fz=0 EXACTEMENT sur une sous-variété bidimensionnelle des contraintes PRIMAIRES PONCTUELLES. Au témoin x=2,y=0 : pg=173/25>0, pf=5995/588>0, z*=4/5, pLf'=4/3. La forme de bord originale réduite se tire en arrière en i*Theta=-(5/3) z*(y) dx ; sa courbure est d(i*Theta)=30/(9+(4-2y)^2)^(3/2) dy∧dx, strictement positive, égale à 6/25 au témoin. Aucun contreterme scalaire ne peut annuler cette forme sur un ouvert de CE SOUS-ESPACE primaire. Cela ne prouve RIEN sur la secondaire fonctionnelle, la surface Dirac complète, les paramètres physiques Step55, les bords admissibles ou la dynamique.

**TESTS EXÉCUTÉS :** `python numerics/hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py` : 19 assertions SymPy exactes PASS, 0 FAIL. `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py' -v` : 1 unittest PASS rejouant les mêmes 19 assertions, non indépendant. Le certificat JSON est généré par le programme, identique octet pour octet à la publication. Sources originales Step37/ADM/IBP lues/SHA authentifiées, moteurs physiques originaux NON réexécutés dans cette étape.

**FICHIERS SCIENTIFIQUES PUBLIÉS, RELUS ET SHA COMPARÉS AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py` — blob `a71df68f58ea49e142e962bb9a5663de290e05b5`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py` — blob `55f736654f8a7087a664ae86b32a8c87b983ca98`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2c-primary-tangent-curvature.json` — blob `d9cd003e79d9cd6e11d96b99941e795d11c9bad5`.
- `research/STEP68AD_C2D2E5B3B2C2B2D2C_PRIMARY_CONSTRAINT_TANGENT_CURVATURE_WITNESS.md` — blob `b9098cc4c48c5cc380cba0e60af1d6bcf1b6bb64`.
- `README.md` — blob `95b1b5777539192b0fadab86cad1f1e3af3e50cd`.

**GITHUB :** HEAD initial lu en direct `28b08c060751b76e45a57c02d3caddd9f936cb57`. Écritures exclusivement sur `research/gate2b-nonhomothetic-transfer`. Les refs protégées initiales `main=aead63f4098f0d15a849e579105af034b6317b30` et `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` ne doivent pas bouger ; workflows désactivés intouchés. Relire HEAD final après mise à jour de l'index.

**LIMITES ET ACTIONS PRIORITAIRES :** (1) Revenir aux vrais paramètres Step55 et à la secondaire `C(r)=0` sur tout le domaine ; identifier des directions tangentes fonctionnelles non triviales, pas uniquement des contraintes primaires ponctuelles. (2) Calculer `i^*dTheta` sur cette vraie surface et la préservation temporelle des conditions de bord, avec lapses/shift et contretermes. (3) Seulement ensuite construire l'oracle Poisson/Dirac original non-IBP à six couples, rang/tertiaires et chartes K=0/J=0 ; 4D/stabilité/observables restent ouverts. Ne pas assimiler ce témoin positif de poussière à une solution physique JANUS.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2b, COURBURE EXACTE DE LA FORME DE BORD RÉDUITE (2026-10-27)

**ÉTAPE d2b TERMINÉE SUR L'ESPACE AMBIANT DES JETS, PAS SUR LA SURFACE DES CONTRAINTES. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b2d2c — pullback de la 2-forme de bord aux variations tangentes aux contraintes physiques, conditions de bord et contretermes admissibles ; puis gradients fonctionnels améliorés, oracle Dirac non-IBP six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT :** Sur la charte HR régulière K=m² Mg² Lg Lf At>0, avec D=pSg Sg'−Lg pLg'+pg tg', z*=D/sqrt(K²+D²), A=N+M Lg/Lf, la forme de bord originale sous Dirichlet des six coordonnées et N,M,V fixes vaut Theta_D=(2Mg² N Sg/Lg)dSg'+(2Mf² M Sf/Lf)dSf'−(A z*+V Lg)dpLg−V Lf dpLf. Son extérieur différentiel est non nul : dTheta_D(∂pLg',∂pLg)=A Lg K²/(K²+D²)^(3/2)>0, indépendamment de Sg'. Également dTheta_D(∂pSg,∂pLg)=−A Sg' K²/(K²+D²)^(3/2). Par d²C=0, AUCUN contreterme scalaire local C ne peut annuler Theta_D sur un ouvert de jets ambiants avec δpLg et δpLg' indépendants, sous ces hypothèses. Témoin rationnel HORS COQUILLE K=3,D=4,Lg=2,Lf=3,N=M=1,z*=4/5 : courbures 6/25 et −3/25. Ceci n'exclut pas des conditions physiques restreintes ou des variations tangentes aux contraintes.

**CONSTRUCTIONS RESTREINTES :** à coordonnées et N,M,V fixés, si δpLg=0, C1=−2Mg² N Sg Sg'/Lg−2Mf² M Sf Sf'/Lf+V Lf pLf annule Theta sur les directions restantes ; si δz*=0, C2=C1+(A z*+V Lg)pLg convient sur cette sous-variété. Si δz* est libre, dC2 contient A pLg dz*, non annulé (témoin A pLg ∂pSg z*=6/25). Ces polarisations ne sont PAS déclarées physiquement admissibles. Lapses variables non traités.

**TESTS RÉELLEMENT EXÉCUTÉS :** `python numerics/hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py` : 21 assertions SymPy exactes PASS, 0 FAIL. `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py' -v` : 1 cas PASS rejouant les mêmes 21 assertions, non indépendant. Sources Step37/ADM/IBP lues sur GitHub, SHA authentifiés, moteurs Python originaux NON réexécutés. Code et test locaux exécutés et octet-identiques aux blobs GitHub relus.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- numerics/hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py — blob 5bf025f11798772ee03d55f8e58b5c3febfcf419.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py — blob c15f9a71240cdf6db113c0c054b242c08bf4d713.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2b-boundary-curvature.json — blob 46feb5e0647f46c7ae06d44ed9d89b1f72a73440.
- research/STEP68AD_C2D2E5B3B2C2B2D2B_REDUCED_SHIFT_BOUNDARY_CURVATURE_NO_GO.md — blob 5f9262416ecb380c662e2f7a25597e6a4540bd61.
- README.md — blob f12303a68e76c87f01534b48cf9266569fb22eaf.

**ÉTAT GITHUB :** HEAD initial authentifié cf39bb6c7cdae806dcb5e1a2637e10f298e2578b ; écritures uniquement sur research/gate2b-nonhomothetic-transfer. Vérifier HEAD final après publication de l'index ; main et research/v2-flrw interdits ; workflows désactivés intouchés.

**LIMITES / ACTIONS PRIORITAIRES :** (1) Calculer le tiré-en-arrière de Theta_D et dTheta_D sur les variations tangentes à la surface complète des contraintes ; ne pas inférer une obstruction physique de la courbure ambiante. (2) Examiner les conditions de bord sur les lapses et le shift diagonal et la préservation temporelle des conditions choisies. (3) Construire l'oracle original non-IBP six couples et calculer la matrice de Dirac, son rang, les tertiaires et les chartes K=0/J=0. (4) Seulement ensuite tester 4D, stabilité et observables. Aucune validation JANUS.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d2a, FORME DE BORD TOTALE NON-IBP SIX COUPLES (2026-10-27)

**ÉTAPE EXACTE MAIS LIMITÉE À LA FORME DE BORD AMBIANTE TERMINÉE : 68ad-C2d2e5b3b2c2b2d2a. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2b — conditions physiques aux frontières et contretermes, variations tangentes aux contraintes, puis oracle Dirac non-IBP six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT :** à partir des densités originales Step37/ADM avec le shift diagonal V et les deux poussières indépendantes, les dix coefficients de la forme de bord du Hamiltonien radial nu ont été dérivés par le calcul variationnel du second ordre. En particulier, Θ[δSg']=2 Mg² N Sg/Lg, Θ[δSf']=2 Mf² M Sf/Lf, Θ[δpLg]=-z(N+M Lg/Lf)-V Lg, Θ[δpLf]=-V Lf, Θ[δSg]=-2 Mg² N' Sg/Lg+(zQ+V)pSg, Θ[δSf]=-2 Mf² M' Sf/Lf+V pSf, Q=N/Lg+M/Lf. Les coefficients restants (δLg,δLf,δtg,δtf) figurent dans l'audit et le certificat. Onze identités symboliques exactes vérifient Θ_original−Θ_IBP=δB, y compris la variation δz du shift : δB_z=−pLg(N+M Lg/Lf)δz, compensée par le terme de bord +pLg(N+M Lg/Lf)δz de la densité IBP. Pour la densité originale, F_z=Q(Dg−K z/sqrt(1−z²))=0 au shift réduit, donc δz* ne produit pas de contribution indépendante à sa variation. À lapses positifs et géométrie régulière, Dirichlet sur les six coordonnées seules laisse des variations ambiantes δSg',δSf' de flux strictement non nul : le Hamiltonien radial NU n'est pas différentiable sur cet espace sans restriction/contreterme. Ce résultat ne porte PAS sur l'espace tangent aux contraintes complètes et ne sélectionne aucune condition de bord physique.

**TESTS RÉELLEMENT EXÉCUTÉS :** 27 assertions exactes SymPy/rationnelles PASS, 0 FAIL (10 coefficients, 1 factorisation shift, 1 δB_z, 3 témoins rationnels, 11 comparaisons originale−IBP, 1 dérivée vraie HR), et 1 cas unittest PASS, 0 FAIL qui réexécute les mêmes 27 assertions. Commandes : `python numerics/hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py` ; `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py' -v`. Sources physiques originales Step37/ADM/IBP lues et SHA authentifiées, mais moteurs Python originaux NON réexécutés dans cette étape. Les deux fichiers Python publiés correspondent octet pour octet aux fichiers exécutés (SHA Git vérifiés).

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- numerics/hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py — blob 94bd7e089ebb0978569361c03a4f3ab950b950df.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py — blob 75c7ec89400ecd1abca6d2c709999648381d5f47.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2a-full-nonibp-boundary.json — blob 39aed544c8f7d5e25330de000ec464fd8a0b9bdc.
- research/STEP68AD_C2D2E5B3B2C2B2D2A_FULL_NONIBP_SIX_PAIR_BOUNDARY_ONE_FORM.md — blob 7f006902c31cfefdc8d94e011359a1b6c0f71101.
- README.md — blob ef79618c57a560b16d75296f4bb8d0ea3242cf3c.

**ÉTAT GITHUB :** HEAD vérifié au démarrage 1e45dcdb01fc57bc4b8bbdfd8bfc39002252e9a6. Toutes les écritures sont limitées à research/gate2b-nonhomothetic-transfer ; main, research/v2-flrw et workflows désactivés intouchés. Relire HEAD final après index. Historique antérieur conservé intégralement ci-dessous.

**LIMITES :** aucune condition physique de bord ni contreterme sélectionné ; aucune différentiabilité démontrée pour un Hamiltonien amélioré, ni pour les variations tangentes à la surface de contraintes. Aucun rang Dirac, aucune tertiaire, aucun lapse global, aucune charte K=0/J=0, ni dynamique 4D, stabilité ou observable prouvés. Prochaine étape d2b : choisir un espace de variations admissibles et une action améliorée, tester les contraintes de bord et l'algèbre non-IBP complète à six couples. Ne pas fabriquer de rang Dirac à partir de ces dix coefficients.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2d1, COMPENSATION DU FLUX DE BORD PAR LES LAPSES (2026-10-27)

**ÉTAPE EXACTE MAIS RESTREINTE TERMINÉE : 68ad-C2d2e5b3b2c2b2d1. PROCHAINE ÉTAPE : 68ad-C2d2e5b3b2c2b2d2 — traiter les variations de bord de la fonctionnelle totale originale non-IBP, y compris shift réduit et six couples, puis Dirac/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT PROUVÉ :** sur la famille Step55/68o et à géométrie/shift fixés, la différence originale−IBP au bord extérieur vaut B=[Ag−z a(Pg+lambda)]N+[Af−z q a(Pg+lambda)]M, avec a=∂lambda pLg(R)>0, q=Lg/Lf>0, Ag=2Mg² R Sgr, Af=2Mf² R Sfr. Les dérivées croisées ∂lambda∂N B=−za<0 et ∂lambda∂M B=−zaq<0 sont exactes. Sur le tiré-en-arrière connexe (lambda,N,M), d(B+C)=0 pour toutes les variations indépendantes ssi C=−B+constante ; aucun contreterme indépendant des lapses ne peut accomplir cela ; pour exclure les contretermes sans pLg il faut aussi interdire toute dépendance explicite en lambda à géométrie/shift fixés. Cependant, à M=1, N(lambda)=[Cg(0)+zqa lambda]/[Cg(0)−za lambda] conserve EXACTEMENT B(lambda,N(lambda),1)=B(0,1,1). Pour le vrai Pg Step55, 5<H2<6 implique −4/5<Pg<−16/25 ; sur |lambda|≤1/5000, une preuve rationnelle uniforme donne 999/1000<N(lambda)<1001/1000 et N'>0. Ceci est un contre-exemple à une extrapolation de l'obstruction à lapses FIXES, pas une condition physique de lapse ni une preuve de différentiabilité du Hamiltonien total.

**TESTS RÉELLEMENT EXÉCUTÉS :** 114 assertions rationnelles BigInt V8 PASS, 0 FAIL ; réexécution depuis octets GitHub relus 114 PASS, 0 FAIL (mêmes cas, pas 228 tests indépendants). Certificat JSON régénéré octet-identique. Modules originaux Step37/ADM/Step55 lus et SHA authentifiés ; moteurs Python originaux NON réexécutés dans cette étape. Aucune preuve nouvelle de poussière, Dirac ou 4D.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS/RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b2d1_boundary_lapse_compensation.cjs — blob ec967f4d5b184d4cd97fca8f5b7fa8d10dc58559.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2d1_boundary_lapse_compensation.cjs — blob 9065f20befabc1e06f0a3e0e4e94874f6d34d61e.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d1-boundary-lapse-compensation.json — blob 5525b24958be7dd0b7fcf310a55ac5b0adf0a352.
- research/STEP68AD_C2D2E5B3B2C2B2D1_BOUNDARY_LAPSE_COMPENSATION_AND_COUNTERTERM_CLASSIFICATION.md — blob 9f6d7357d72238e83c453c942f906b889484c886.
- README.md — blob fe9f3ea6e68ceda76902542e1eab2f38b4ebd481.

**ÉTAT GITHUB :** HEAD au démarrage 4e74225dc2910031c4f81071b77dfb1c310469a4, seules écritures sur research/gate2b-nonhomothetic-transfer ; main, research/v2-flrw et workflows intouchés. HEAD final à relire après index. L'historique du journal ci-dessous est conservé INTÉGRALEMENT (451126 caractères JavaScript antérieurs).

**LIMITES ET PRIORITÉS :** le flux B n'est que la différence original−IBP ; l'annuler ne suffit PAS à rendre l'un ou l'autre Hamiltonien fonctionnellement différentiable sur l'espace canonique complet. Les variations indépendantes des lapses sont des multiplicateurs, pas des paires canoniques. Priorité : audit de tous les termes de bord de l'action totale et du shift z* éliminé, espace admissible des champs et contretermes, puis oracle original non-IBP six couples, rang et contraintes tertiaires. Ne jamais déclarer JANUS validé sans fermeture temporelle et conditions aux bords, K=0/J=0, 4D, stabilité, observables.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2c, SENSIBILITÉS EXTÉRIEURES DES QUATRE TRACES f (2026-10-27)

**ÉTAPE SPATIALE CERTIFIÉE TERMINÉE : 68ad-C2d2e5b3b2c2b2c. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b2d — sélectionner/tester des conditions physiques aux limites, les variations indépendantes des lapses et les contretermes admissibles ; puis construire l'oracle Poisson/Dirac original non-IBP à six couples, rang, tertiaires, K=0/J=0, 4D, stabilité, observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT RIGOUREUX MAIS SPATIAL :** à R=17/20, pour toute la famille Step55/68o |lambda|<=1/5000 sous Step49 et les tubes authentiques b2/b2b, propagation par fractions rationnelles exactes du jacobien primaire f Step46 : 0.0135<∂lambda V<0.0139, 0.0049<∂lambda pLf<0.0050, 0.0115<∂lambda pLf'<0.0118, -0.020<∂lambda pf<-0.011, 0.0115<∂lambda pSf<0.0118. En outre -2<H<-0.6, -0.84<chi<-0.71, 1<D<1.01. Le certificat donne des fractions plus serrées, arrondies rigoureusement vers l'extérieur au pas 10^-12. Formules : ∂lambda V=G_U*v+G_Pg ; ∂lambda pLf=R²*v ; ∂lambda pLf'=R*∂lambda V ; ∂lambda pf=H*∂lambda pLf+chi*∂lambda pLf' ; ∂lambda pSf=(Lf/Sfr)*∂lambda pLf'-(R*kf*Lf/Sfr)*∂lambda pf. Les quatre traces f sont strictement monotones sur le tube ; en fixer UNE à sa valeur lambda=0 force lambda=0 DANS CETTE FAMILLE UNIQUEMENT. Aucune obstruction générale JANUS démontrée.

**MÉTHODE/TESTS :** 38 assertions exactes BigInt PASS, 0 FAIL, exécutées dans V8 sur les sources construites, puis réexécutées depuis les octets GitHub publiés ; certificat JSON régénéré identique. Les huit blobs sources/certificats précédents ont été relus et comparés aux SHA épinglés. Moteurs Python originaux Step45/46/55 NON réexécutés dans CETTE étape (ils ont été exécutés dans b2/b2b). Arithmétique rationnelle exacte, aucun échantillonnage de lambda. Commande reproductible dans le dépôt : `node tests/test_hr_step68ad_c2d2e5b3b2c2b2c_f_outer_sensitivities.cjs`.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS/RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b2c_f_outer_sensitivities.cjs — blob 315d6226f5feeb346d60ab0ac2e16ca0b9de9b41.
- tests/test_hr_step68ad_c2d2e5b3b2c2b2c_f_outer_sensitivities.cjs — blob 2787d5a79755b500d323e11e4844aa73eae3b030.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b2c-f-outer-sensitivities.json — blob b53eb93c48fba7099ae2d3275ec4eb5e0464a7a4.
- research/STEP68AD_C2D2E5B3B2C2B2C_CERTIFIED_F_OUTER_TRACE_SENSITIVITIES.md — blob 9ef72a5fe7f23785465356260ca30efcb0a80322.

**ÉTAT GITHUB :** HEAD authentifié au démarrage ee39bea4925b23b0606e7dcbb38d487bab453a4e. Écritures uniquement sur research/gate2b-nonhomothetic-transfer ; main et research/v2-flrw interdits ; GitHub Actions intouchées. Relire le HEAD final après l'index. Ancien journal de 447747 caractères conservé intégralement après ce préfixe.

**LIMITES/PRIORITÉS :** les conditions aux limites physiques, contretermes dépendant des lapses, différentiabilité fonctionnelle, rang Dirac six couples, tertiaires, lapses globaux, chartes K=0/J=0, évolution 4D, stabilité et observables ne sont PAS démontrés. Le rang 2 du jacobien formel n'est pas le rang Dirac. Prochaine étape : bords/contretermes et oracle fonctionnel original non-IBP ; ne pas créer de micro-étapes de simple reformulation.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3c2b2b, DÉRIVÉES PHYSIQUES G ET BARRIÈRE VARIATIONNELLE (2026-10-27)

**ÉTAPE RIGOUREUSE SPATIALE TERMINÉE : 68ad-C2d2e5b3b2c2b3c2b2b. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3c2b2c — encloser delta V=G_U*v+G_Pg et les quatre dérivées des traces canoniques f à R, puis sélectionner les conditions aux bords/contretermes et construire l'oracle fonctionnel Dirac non-IBP six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT NOUVEAU PHYSIQUE ET LIMITÉ :** les quatre fichiers originaux Step45/46/55 ont été reconstitués depuis GitHub et authentifiés octet-identiques par SHA Git (66aa43841dccfe4a5d586a49be9c10af3a67a10e, bac025c28dbe1561c0c36c56dbfda46dc326f804, a54a6acf2f7ad2f64c500faecfa1406ecbf7b862, a6e7004120d0a166a3a8973c2fbe1487a8eb70fe). Le G normalisé original a été effectivement compilé et évalué en nombres duaux d'intervalles rationnels 10^-28, en différenciant Pg dans Gmom, Gprime, Rhog et Psg0. Sur 256 cellules jointives, s∈[0,289/400], |lambda|≤1/5000, U dans le tube b2 : -1.001099494671<G_U<-0.993939366018 et 0.020435412499<G_Pg<0.020578225856 (fractions exactes dans JSON). Les résidus entrants de la barrière de v sont min(A*0.00681+B)=1024922611588406880813/62500000000000000000000000>0 et max(A*0.00689+B)=-841114594602624479574991/10000000000000000000000000000<0, avec A=G_U-2, B=G_Pg. Sous le théorème analytique Step49 et le tube spatial authentique b2, **0.00681<v(s,lambda)<0.00689 pour tout s et lambda du domaine**, donc aussi v(R²,lambda) ; v(R) n'est pas évalué à une valeur exacte. Aucune dérivée des traces f ni condition aux limites physique certifiée.

**TESTS EXÉCUTÉS :** 17 tests Python unittest PASS, 0 FAIL dans une arborescence locale contenant les quatre sources physiques originales SHA-identiques. Commandes : `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py' -v` et `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational`. Contre-vérification indépendante SymPy des dérivées à s=1/3, primal G identique, 256 et 512 cellules PASS ; barrière plus étroite [0.00682,0.00688] non certifiée, échec attendu testé (pas un contre-exemple physique). Le certificat JSON a été généré localement et publié octet-identique.

**FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS :**
- numerics/hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py — blob 285e547658dec8534247faf67fbd26dba15400bf.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py — blob f29015a1a2d14edcacfced0643040798cb626d36.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2b2b-authentic-variational-barrier.json — blob c8100b22ec0f169af2151f4308eea0bc6ba26c80.
- research/STEP68AD_C2D2E5B3B2C2B3C2B2B_AUTHENTIC_PHYSICAL_G_VARIATIONAL_BARRIER.md — blob 52937e5388438c0434c92020db667d1c4900cc11.
- README.md — blob 0334cd9ad38cb698dee6a5918955659eb656d877.

**ÉTAT GITHUB :** HEAD initial vérifié 7097b3d305c7cf9c257861c7f82fb4133fdf80c6 ; seules créations/modifications sur research/gate2b-nonhomothetic-transfer. Les branches main, research/v2-flrw et workflows désactivés ne doivent pas être modifiés. Vérifier le HEAD final après mise à jour de l'index.

**LIMITES ET PRIORITÉS :** preuve de sensibilité radiale dans la famille spatiale sphérique et sous Step49/b2, PAS de condition aux limites externe, ni contreterme, ni matrice complète Dirac, ni tertiaires, ni lapses globaux, ni 4D, stabilité ou observables. Prochain calcul : combiner G_U, G_Pg et v pour delta V, puis Jacobien Step46 des quatre traces f et étude des bords ; ensuite véritable oracle non-IBP six couples.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3c2b2a, LEMME VARIATIONNEL CENTRAL RÉGULIER (2026-10-27)

**ÉTAPE CONDITIONNELLE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b3c2b2a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3c2b2b — dériver et EXÉCUTER les vrais G_U/G_Pg du moteur original Step45/46/55, encloser leurs coefficients sur le tube, certifier v(R), dérivées des quatre traces f, bords et contretermes, puis oracle Dirac non-IBP six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT MAIS CONDITIONNEL :** l'identité centrale authentifiée lors de b2, G(0,U,P)=3*Mf2*b*(P/a-2*z1)-U, impose G_U(0)=-1, G_Pg(0)=3*v0 et v0=Mf2*b/a=274023815147385251710689588080861/40000000000000000000000000000000000. Pour A(s)=G_U-2=-3+Σ a_k s^k, B(s)=G_Pg=3v0+Σ b_k s^k, la sensibilité analytique v=Σv_n s^n satisfait exactement (2n+3)v_n=b_n+Σ(k=1..n)a_k v_(n-k). En particulier v1=(a1*v0+b1)/5 ; le mode s^(-3/2) est exclu. Sous les hypothèses supplémentaires |G_U+1|≤alpha*s, |G_Pg-3v0|≤beta*s, une majoration conditionnelle est |v(s)-v0|≤(alpha*|v0|+beta)*s*exp(alpha*s/2)/5 ; pour alpha*S/2<1, majorant rationnel ≤(alpha*|v0|+beta)*S/[5*(1-alpha*S/2)]. Les constantes alpha=1/10 et beta=1/100 sont EXCLUSIVEMENT SYNTHÉTIQUES et ne sont pas démontrées pour le G physique.

**TESTS RÉELLEMENT EXÉCUTÉS :** 47 assertions rationnelles BigInt V8 PASS, 0 FAIL, puis les mêmes 47 réexécutées depuis les octets GitHub relus ; le certificat JSON est régénéré octet-identique. Ce sont 47 cas distincts, pas 94 tests indépendants. Les quatre fichiers scientifiques ont été créés et relus octet-identiques. Sources physiques originales Step45/46/55 consultées avec SHA Git : 66aa43841dccfe4a5d586a49be9c10af3a67a10e, bac025c28dbe1561c0c36c56dbfda46dc326f804, a54a6acf2f7ad2f64c500faecfa1406ecbf7b862, a6e7004120d0a166a3a8973c2fbe1487a8eb70fe. Moteurs Python originaux NON réexécutés ; aucun G_U/G_Pg physique sur s>0, v(R) ou oracle Dirac calculé.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b3c2b2a_variational_regularization.cjs — blob 66a1c4846518d036a167fce7595949bf382df144.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3c2b2a_variational_regularization.cjs — blob c5432c15c01ea8da0ea1637f4e1dd97aa7ffe17b.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2b2a-regular-variation.json — blob 478be1ec26e99525a7d99f93698b40a40a32c2ae.
- research/STEP68AD_C2D2E5B3B2C2B3C2B2A_CONDITIONAL_REGULAR_VARIATIONAL_LEMMA.md — blob 1f0429d4269a54e2693946e64244faac8bcd1289.

**ÉTAT GITHUB :** HEAD authentifié au démarrage cdbdbe554bab461e10196629b58291c48d386b29 ; seules créations sur research/gate2b-nonhomothetic-transfer. Les branches main et research/v2-flrw restent interdites de modification ; aucune action workflow autorisée. Vérifier HEAD final après journal/index. Nettoyage Library non retenté dans cette session (anciens 401 Unauthorized).

**LIMITES :** ce lemme facilite une certification future mais n'établit aucune borne physique alpha/beta, aucune valeur v(R), aucune condition de bord admissible, aucune fermeture temporelle de Dirac, aucune stabilité ni observable cosmologique. Éviter de présenter le cas synthétique comme un calcul de sensibilité JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3c2b1, SENSIBILITÉ EXACTE DE LA POUSSIÈRE g (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b3c2b1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3c2b2 — véritable G_U/G_Pg de Step45/46/55, équation variationnelle et v(R), dérivées des traces f, bords/contretermes puis oracle Dirac original non-IBP six couples, rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE ET LIMITÉE :** en transcrivant indépendamment la reconstruction originale g de Step55 (blob a6e7004120d0a166a3a8973c2fbe1487a8eb70fe), rho_g(s,P)=-(a2 P²+a1 P+a0)/(b0+dP), P=Pg+lambda, on a dérivé exactement les dérivées première et seconde de cette fraction rationnelle. Sur s∈[0,289/400] et |lambda|<=1/5000, 256 cellules jointives et arithmétique entière dirigée 10^-28 prouvent uniformément -2.88<partial_lambda rho_g<-2.85, 3.74<partial_lambda² rho_g<3.77, 0.88<rho_g<0.90 et denom_g>0.999. L'enclosure à 512 cellules confirme les signes. Les fractions exactes figurent dans le certificat. La densité g décroît strictement et est convexe en lambda sur ce tube, à géométrie/shift fixes. Cela ne donne PAS G_U, G_Pg, v(R) ni la sensibilité des traces f.

**TESTS RÉELLEMENT EXÉCUTÉS :** 1551 assertions BigInt V8 PASS, 0 FAIL, réexécutées à partir des octets GitHub publiés. Cela comprend 256 cellules x 6 inégalités (1536) et 15 contrôles globaux, centraux, 512 cellules et garde-fous. Les 512 cellules sont un contrôle des signes, pas 3072 tests indépendants supplémentaires. Source originale Step55 SHA authentifiée et relue ; moteurs physiques Python Step45/46/55 NON réexécutés cette session. Aucun oracle Dirac exécuté.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS, RELUS ET TESTÉS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b3c2b1_gdust_sensitivity.cjs — blob 3336afdf3c2a6ecbb0446b682516ca17bdc5390a.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3c2b1_gdust_sensitivity.cjs — blob 83c04c69f736714073522a5efebe746a61f50b2b.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2b1-gdust-sensitivity.json — blob 68d9e728c561ab52ab9c676da63d3c1b3310f052.
- research/STEP68AD_C2D2E5B3B2C2B3C2B1_UNIFORM_G_DUST_PARAMETER_SENSITIVITY.md — blob 002c120fc713054b7c76f5e736c1e3e168907c52.

**ÉTAT GITHUB :** HEAD vérifié au début 847995c5c40f0fc91bdc783777ff4b28bfeb7d56. Quatre créations scientifiques sur research/gate2b-nonhomothetic-transfer ; README, journal et index actualisés ensuite. main et research/v2-flrw interdits de modification ; aucun workflow touché. Vérifier le HEAD final et les deux branches après écriture. Nettoyage Library non retenté (401 Unauthorized antérieur).

**LIMITES/PRIORITÉS :** (1) différencier le G original du secteur f et certifier G_U/G_Pg ; (2) résoudre rigoureusement v(s) jusqu'à R et calculer les quatre dérivées de traces f ; (3) définir les bords physiques et contretermes, y compris lapses ; (4) Dirac six couples, rang, tertiaires, K=0/J=0 ; (5) 4D, stabilité, observables. Aucun résultat physique global JANUS revendiqué.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3c2a, JACOBIEN EXACT DES TRACES f AU BORD (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b3c2a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3c2b — exécuter les véritables dérivées G_U et G_Pg du moteur Step45/46/55 sur le tube paramétrique, certifier l'équation variationnelle et v(R), calculer la sensibilité réelle des traces f et les conditions de bord/contretermes, puis oracle Dirac original non-IBP six couples, rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE, PORTÉE LIMITÉE :** à géométrie, shift et reconstruction g fixés, la primaire f originale Step46 fournit rho=-A/D, avec D=beta_f+kf*s*U/(2Mf2*Sfr), A=U²/(4Mf2Lf)-U*(V-sDbar/Lf)/(2Mf2Sfr)-Mf2Lf³Rf/2+s*z1*Dbar/Lf+Wfbar. Au bord R=17/20, définir H=-(A_U+rho D_U)/D et chi=R*U/(2Mf2*Sfr*D). Les identités exactes sont delta pf=H delta pLf+chi delta pLf' et delta pSf=(Lf/Sfr)delta pLf'-(R*kf*Lf/Sfr)delta pf. Le jacobien formel (delta U,delta V) vers les quatre traces a rang 2 puisque ses deux premières lignes sont diag(R²,R) ; ce n'est PAS le rang de Dirac. Le certificat b2 authentique antérieur et une borne rationnelle de sqrt prouvent uniformément -21/25<chi<-71/100 pour |lambda|<=1/5000. Ce chi n'est PAS le J temporel.

**TESTS RÉELLEMENT EXÉCUTÉS :** 24 assertions exactes BigInt PASS, 0 FAIL dans Node.js local et 24 réexécutées dans V8 sur les octets publiés (24 cas distincts, pas 48 tests indépendants). Dix égalités par nombres duaux rationnels sur cinq directions synthétiques, contrôles de signes, fractions physiques, garde-fous GATE/JANUS. Le certificat JSON a été régénéré octet-identique depuis le programme publié. Source originale Step46 relue avec blob Git bac025c28dbe1561c0c36c56dbfda46dc326f804 ; certificat b2 relu blob 012e70e49b41cc3180da423c3962d279e3909a26. Les moteurs Python physiques originaux n'ont PAS été réexécutés dans cette étape ; G_U/G_Pg authentiques et v(R) ne sont PAS calculés.

**LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs — blob 7615cdb1624748dac56ab1d969c401b258f8cdaa.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs — blob fdbc28c258cd38d96da602db5992dca10a85bf45.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2a-f-boundary-jacobian.json — blob e7966302ed157695df64fc887883a558d24e87ef.
- research/STEP68AD_C2D2E5B3B2C2B3C2A_EXACT_F_BOUNDARY_TRACE_JACOBIAN.md — blob d40b07eb87bbcb09b8c6b00a03a63152dd5472a4.
- README.md — blob d40f7b1e87807190312bd61561f61d035576d70c.

**ÉTAT GITHUB :** HEAD de reprise 770bb8e36b1519290748d48bd39c87c926125362 ; publications exclusivement sur research/gate2b-nonhomothetic-transfer. main et research/v2-flrw doivent être relus en fin de session ; aucun workflow modifié. Nettoyage Library non retenté, échecs 401 Unauthorized antérieurs.

**LIMITES ET PRIORITÉS :** (1) différencier le véritable G(s,U,Pg) original et encadrer G_U/G_Pg ; (2) certifier la sensibilité v(R) puis substituer delta U=v(R), delta V=G_U v+G_Pg dans les identités de bord ; (3) définir espace fonctionnel physique, lapses et contretermes ; (4) oracle original non-IBP six couples, rang/tertiaires/K=0/J=0 ; (5) 4D/stabilité/observables. Ne pas transformer un rang de jacobien de traces en rang Dirac.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3c1, SENSIBILITÉ CENTRALE EXACTE f (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b3c1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3c2 — vraie équation variationnelle G_U/G_Pg, v(R), dérivées des traces f, espace de bords et contretermes, puis oracle Dirac non-IBP six couples, rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE EXACTE, UNIQUEMENT AU CENTRE :** sur les identités originales Step46/49/55, U₀(λ)=Mf²b[(Pg+λ)/a−2z₁], V₀=2U₀. En utilisant la primaire f et la géométrie Step55, ρf,0(λ)=3U₀(λ)²/(4Mf²b)+Mf²b³Rf,0/2−Wfbar,0. Donc ∂λU₀=Mf²b/a=274023815147385251710689588080861/40000000000000000000000000000000000>0, ∂λV₀=2∂λU₀>0 et ∂λρf,0=3U₀(λ)/(2a)<0. Certification par fractions exactes et carré de Pg : −0,764<Pg<−0,763 ; sur |λ|≤1/5000, −0,020<∂λρf,0<−0,019 et ρf,0>0,12. Valeurs indicatives λ=0 : U₀≈−0,005252426897, ∂λρf,0≈−0,019696600863, ρf,0≈0,124270000262. La dépendance quadratique est exacte, pas une approximation par différences finies. Cela ne certifie AUCUNE dérivée à R.

**TESTS EXÉCUTÉS :** 20 assertions adversariales BigInt Node local PASS, 0 FAIL, et réexécution des mêmes 20 assertions dans V8 depuis les octets relus de GitHub. Le générateur comporte des contrôles rationnels internes supplémentaires non comptés comme tests indépendants. Rapport JSON généré, publié, relu octet-identique. Les sources originales Step46/55 ont été relues et SHA-authentifiées, mais leurs moteurs Python n'ont PAS été réexécutés dans cette session. Le tube spatial f/g global reste le certificat b2 antérieur. Une erreur initiale de chemin de test local a été corrigée avant la campagne finale.

**QUATRE LIVRABLES PUBLIÉS/RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b3c1_center_f_sensitivity.cjs — blob 77d141fb3d091d54b83fa622ec6dd98931e8d050.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3c1_center_f_sensitivity.cjs — blob db03a9e9997505967d88e7387b4c8599ca833996.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c1-center-f-sensitivity.json — blob dc46e73ad6b283c489efe67a179680ad68bffbfc.
- research/STEP68AD_C2D2E5B3B2C2B3C1_EXACT_CENTRAL_F_DUST_PARAMETER_SENSITIVITY.md — blob a8fc7e0d0adab1dfb4059d24eb774c5d0dd0ee87.
- README.md — blob eec6a8a3f25c450dbcb490de445965119dfb39eb.

**ÉTAT GITHUB :** HEAD à la reprise 4dd37794d54142e1e9d0553eaabae2c351380abf ; publication exclusivement sur research/gate2b-nonhomothetic-transfer, aucun changement voulu à main, research/v2-flrw ou workflows. HEAD final à vérifier après index. Les fichiers et leurs contenus ont été relus après écriture. Nettoyage Library non retenté cette session (401 Unauthorized antérieur).

**LIMITES ET PRIORITÉS :** (1) calculer et encadrer G_U, G_Pg sur le tube authentique puis v(R) ; (2) dériver les quatre traces f à R et déterminer bords/lapses/contretermes physiquement admissibles ; (3) oracle original non-IBP six couples, rang/tertiaires, K=0/J=0 ; (4) 4D/stabilité/observables. Ne pas confondre sensibilité centrale et globale ; ne pas valider JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3b, TRACES f AU BORD ET LAPSÉS VARIABLES (2026-10-27)

**ÉTAPE EXACTE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b3b. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3c — dériver et certifier la sensibilité v=∂lambda U du véritable G jusqu'à R, carte différentielle des traces f, déterminer les conditions aux bords physiques/contretermes, puis oracle Poisson/Dirac original non-IBP six couples/rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE SCIENTIFIQUE EXACTE, PORTÉE LIMITÉE :** propagation rationnelle rigoureuse du certificat authentique Step45/46/55 b2 (blob 012e70e49b41cc3180da423c3962d279e3909a26) à la reconstruction canonique f originale Step46 au bord R=17/20, pour tous |lambda|<=1/5000. Les enclosures de U=pLf/r², V=pLf'/r et rho_f=pf/r² et l'encadrement sqrt(1-z1²R²)∈(99999/100000,1) donnent exactement pLf(R)<0, pLf'(R)<0, pSf(R)<0, pf(R)>0. En particulier -0.013076<pSf(R)<-0.007534 et -0.003869<pLf(R)<-0.003313 (décimales élargies ; fractions exactes dans certificat). Ce sont des intervalles de valeurs, **PAS des dérivées en lambda**. Moteurs physiques originaux **NON RÉEXÉCUTÉS dans cette session** ; les sources Step45/46/55 ont été relues et authentifiées par leurs SHA Git, et le certificat b2 a été relu.

**VARIATIONS DES LAPSÉS ET NON-SÉPARABILITÉ :** B(R)=Ag*N+Af*M-z*pLg*(N+q*M), q=Lg/Lf, Ag=2Mg² R Sgr, Af=2Mf² R Sfr. À géométrie/shift fixes, delta B=(Ag-z*pLg)delta N+(Af-z*q*pLg)delta M-z*a*(N+q*M)delta lambda, a=partial_lambda pLg(R)>0. Les dérivées croisées partial_lambda partial_N B=-z*a<0 et partial_lambda partial_M B=-z*a*q<0 sont exactes ; aucun contreterme dépendant seulement de lambda, indépendant des lapses, ne peut annuler partial_lambda B pour tous N,M indépendants. **Cela ne prouve ni la non-différentiabilité générale de H_original, ni l'inadmissibilité de contretermes dépendant des lapses.** Les lapses sont des multiplicateurs et leur variation doit être traitée dans un espace fonctionnel correctement défini.

**TESTS EXÉCUTÉS :** 25 assertions BigInt rationnelles dans V8 PASS, 0 FAIL, sur le code produit puis de nouveau sur les octets effectivement relus de GitHub. Certificat JSON régénéré octet-identique. Les assertions couvrent l'encadrement de la racine, les quatre signes canoniques f, T/Dbar, bornes grossières et dérivées croisées des lapses. Aucune exécution Node, aucun moteur original réexécuté, aucun oracle Dirac fonctionnel exécuté.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b3b_f_traces_lapses.cjs — blob dae748bedd926327c2cdee9d474b97393f06f3dc.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3b_f_traces_lapses.cjs — blob 53ce8c8ea6f36a9f35b037595bf5abb9f4b83db8.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3b-f-traces-lapses.json — blob 4595292ee18c7f71cf773338177321a2b617592d.
- research/STEP68AD_C2D2E5B3B2C2B3B_EXACT_F_OUTER_TRACE_AND_LAPSE_MIXED_VARIATIONS.md — blob 814e91a9597f925d077c3ac996093c3f86a73266.
- README.md actualisé — blob a3278b607e6da8afda3f1b855503bef36805fd3f.

**ÉTAT GITHUB :** branche research/gate2b-nonhomothetic-transfer uniquement ; dernier commit vérifié avant journal 9cd527e824b53fe1e5f91edf3740fe56d0a74642. main=aead63f4098f0d15a849e579105af034b6317b30, research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb vérifiés inchangés au début. GitHub Actions non modifiées. Nettoyage Library non retenté dans cette session (échecs 401 Unauthorized antérieurs ; aucune suppression revendiquée).

**LIMITES ET PRIORITÉS :** (1) calculer les dérivées véritables des traces f via équation variationnelle et bords ; (2) sélectionner l'espace fonctionnel physique et les contretermes/lapses admissibles ; (3) oracle non-IBP original six couples, rang/tertiaires, K=0/J=0 ; (4) 4D/stabilité/observables. Aucune validation JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b3a, VARIATION NON-IBP AU BORD (2026-10-27)

**ÉTAPE EXACTE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b3a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3b — conditions aux bords physiques, contretermes, carte des traces f sur le tube, puis oracle Poisson/Dirac non-IBP six couples, rang/tertiaires/lapses/K=0/J=0/4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT EXACT CONDITIONNEL :** famille spatiale authentique Step55/68o certifiée précédemment pour |lambda|<=1/5000. Pendant Pg→Pg+lambda, géométrie, potentiels de poussière et shift z=r*z1 sont fixés ; N,M également fixés pendant la variation. À R=17/20 : ∂lambda pLg=92730563/128000000 ; ∂lambda pLg'=2734739/1600000 ; ∂lambda U0=274023815147385251710689588080861/40000000000000000000000000000000000 ; z(R)=17/5000 ; Lg/Lf(R)=2505421686285156250000000000/1444418923561876775155324829. L'identité original−IBP donne B=2Mg² N Sg Sg'/Lg+2Mf² M Sf Sf'/Lf−z pLg(N+M Lg/Lf). Pour lapses bornés B(0)=0, et ∂lambda[B]_0^R=−z(R)∂lambda pLg(R)[N(R)+M(R)Lg(R)/Lf(R)] ; pour N=M=1 : exactement −6226606039693438177138189375297828359/924428111079601136099407890560000000000<0. Robin alpha*pLg+beta*pLg'=const annule cette direction SSI alpha*a+beta*d=0 ; si alpha=1, beta=−5454739/12869360. Dirichlet sur les seules coordonnées n'annule pas ce flux pour lapses positifs non compacts. Il faut sélectionner les conditions physiques/contretermes. Les variations de N,M et du secteur f ne sont pas calculées.

**TESTS RÉELLEMENT EXÉCUTÉS :** code et wrapper JavaScript rationnels réexécutés depuis les contenus GitHub publiés : 25 assertions BigInt exactes PASS, 0 FAIL. Rapport JSON régénéré et comparé octet pour octet. Traces, signes N/M, N=M=0, centre, quatre différences finies exactes, produit original−IBP sur trois rayons, Robin exceptionnel et non-validation contrôlés. Aucune exécution Node ni des moteurs Python physiques originaux cette session ; sources Step45/46/55 et Step37 relues et SHA authentifiés. Le tube spatial original Step55 reste un résultat antérieur.

**QUATRE LIVRABLES PUBLIÉS ET RELUS :**
- scripts/hr_step68ad_c2d2e5b3b2c2b3a_nonibp_boundary.cjs — blob 485cbfcd9ccb255c12b1da1ff4615fdaa66df066.
- tests/test_hr_step68ad_c2d2e5b3b2c2b3a_nonibp_boundary.cjs — blob 1681226f7f4c29ec7f59c5ad1a0db07df4902a4b.
- research/reports/gate2b-step68ad-C2d2e5b3b2c2b3a-nonibp-boundary.json — blob b60a7fd132b8f8803c6eea5649b87c840b5502c0.
- research/STEP68AD_C2D2E5B3B2C2B3A_EXACT_PG_BOUNDARY_FLUX_AND_ROBIN_CLASSIFICATION.md — blob 865f1ed1d1c9a8f0c2a7bd62101dee29f387c38b.

**ÉTAT GITHUB :** HEAD de reprise 312e19cdb6571467516d6e9c4a1bf3d069263224 ; HEAD après les quatre livrables et avant les états b3ac027539d6cddd0424747018e71939c63e9441. main=aead63f4098f0d15a849e579105af034b6317b30 ; research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb ; aucun workflow modifié. Nettoyage Library non retenté cette session ; précédents échecs 401 Unauthorized, aucune suppression revendiquée.

**LIMITES / ACTIONS PRIORITAIRES :** (1) déterminer bords physiques, contretermes, variations des lapses ; (2) calculer la sensibilité des traces f à R sur le vrai tube paramétrique ; (3) oracle fonctionnel original Poisson/Dirac non-IBP six couples, rang/tertiaires, K=0/J=0 ; (4) 4D, stabilité, observables ; (5) nettoyer Library si autorisations rétablies. Aucune preuve de bords globaux, rang Dirac ou validation JANUS.

**CHECKPOINT PRÉFIXÉ — HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b2, VRAI G PARAMÉTRÉ ET DEUX POUSSIÈRES POSITIVES (2026-10-27)

**ÉTAPE SPATIALE CERTIFIÉE : 68ad-C2d2e5b3b2c2b2. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b3 — conditions aux limites physiques, carte des traces du tube paramétrique, puis opérateur fonctionnel Poisson/Dirac non-IBP à six couples, rang/tertiaires/lapses, K=0/J=0, 4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**AVANCÉE PHYSIQUE SPATIALE RÉELLEMENT EXÉCUTÉE :** les QUATRE sources originales Step45/46/55 ont été recopiées, SHA-authentifiées et réellement exécutées, notamment le véritable G(s,U,Pg) compilé depuis C=K00-(K01)' et le véritable moteur d'intervalles Step55. Sur tout s=r²∈[0,289/400], simultanément pour tout |lambda|<=1/5000, avec 256 cellules radiales et une enclosure unique du paramètre, les barrières originales restent strictement entrantes (Fplus<-0.0000359260, Fminus>0.0000355740). En reconstruisant la poussière f depuis la primaire Step46 originale : rho_f>0.1094480192, rho_g>0.8844952279, denom_f>=1, beta_g>0.9991759495, T>0.1060297323 et -0.005354<U<-0.004585. Les fractions EXACTES sont dans le certificat. La formule originale de rho_f et l'identité centrale G(0,U,Pg)=3Mf²*b*(Pg/a-2z1)-U ont des résidus SymPy EXACTEMENT nuls. U1/U2 de la base restent seulement des fonctions de comparaison, PAS les vrais jets perturbés. La continuation de la famille spatiale s'appuie sur le théorème analytique local Step49, non sur un tir numérique ponctuel.

**TESTS EXÉCUTÉS :** `cd /mnt/data/janus_run && PYTHONPATH=. python -m unittest discover -s tests -v` : **13 unittest PASS, 0 FAIL**, dont 2 identités SymPy exactes incluses. `PYTHONPATH=. python numerics/hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py` régénère le JSON ; revalidation à 512 cellules PASS ; à 128 cellules l'enclosure est insuffisante (échec de certification attendu et testé), pas un contre-exemple. Les quatre sources originales ont été exécutées dans une arborescence locale vérifiée par blob SHA : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalisation `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 barrière `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

**LIVRABLES PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py` — blob `180307509ad7992880b99319dbeb6f8662752127`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube.py` — blob `ec8e3145b65f902a95648872bfc3e5b554c25046`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2-authentic-Pg-fdust-tube.json` — blob `012e70e49b41cc3180da423c3962d279e3909a26`.
- `research/STEP68AD_C2D2E5B3B2C2B2_AUTHENTIC_G_PARAMETER_TWO_DUST_TUBE.md` — blob `2e388ef7eacf59df7bea0e443486bee72fb38fa3`.

**LIMITES STRICTES :** il s'agit d'une famille de données SPATIALES sphériques contraintes sur la géométrie prescrite, PAS d'une famille de solutions du problème aux limites physiques final. Les traces externes changent avec Pg. Les contraintes temporelles, rang de Dirac, tertiaires, lapses admissibles, chartes K=0/J=0, dynamique 4D, stabilité et observables restent NON PROUVÉS. Ne pas extrapoler les anciens indicateurs J/K Step54 à un rang Dirac paramétrique.

**GITHUB :** HEAD initial réellement lu `9559ffba454c126ccbc15531860a157c733c4e28`; commit audit `97c9e138efc174cf566b28f71f43ae9cf9372b0f`; commit README `dcc115ae68e667d0ec924bf4a606537905c4eeef`. Branches interdites vérifiées initialement : main=`aead63f4098f0d15a849e579105af034b6317b30`, research/v2-flrw=`dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. **NETTOYAGE LIBRARY :** deux suppressions `libfile_45aa141b5df881918aff37fe431c9c0b` et `libfile_17f52736778c819195709abedd20af01` réellement retentées, deux échecs exacts `401 Unauthorized /uninjest_file`, aucune suppression déclarée.

**ACTIONS PRIORITAIRES :** (1) déterminer conditions aux bords physiquement admissibles, calculer traces de la famille Pg et leur variation sur le tube certifié ; (2) construire véritable crochet Poisson/Dirac non-IBP à six couples sur le profil et variations admises, bords et rang/tertiaires ; (3) K=0/J=0, lapses et dynamique 4D/stabilité/observables ; (4) nettoyage Library seulement lorsque l'autorisation est réparée.

**CHECKPOINT PRÉFIXÉ — TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ OCTET POUR OCTET CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2b1, COEFFICIENT AFFINE Step46 f SUR UN CONTINUUM (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2b1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b2 — exécuter le véritable G(s,U,Pg) Step45/46/55 avec Pg variable, certifier U et poussière f et bords, puis oracle Poisson/Dirac non-IBP six couples, rang/tertiaires, K=0/J=0, 4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU RÉSULTAT EXACT CONDITIONNEL (PAS UNE SOLUTION f CERTIFIÉE) :** sur la géométrie Step55, pour tout s=r²∈[0,289/400] et tout U avec |U|<=1, le polynôme T(s)=beta1*Lg²+2beta2*Lg*Lf+beta3*Lf² a cinq coefficients Bernstein rationnels exacts tous dans (1/10,11/100). La formule originale Step46 donne le dénominateur poussière f beta_f+fac*tfr=sqrt(1+kf²*s)+kf*s*U/(2*Mf2*Sfr)>3/4 et le coefficient affine secondaire normalisé C_V/r<-372 pour 0<r<=17/20. Minima rationnels indicatifs T>0.106037774505..., dénominateur>0.787967230705..., -C_V/r>372.501551686... . **C_V n'est PAS J=∂B_N/∂pSf temporel** ; C_V=O(r) au centre. L'hypothèse |U|<=1 N'EST PAS certifiée pour le vrai U(s,lambda) ; aucune densité de poussière f positive ni continuation paramétrique n'est prouvée.

**EXÉCUTION RÉELLE :** `cd /mnt/data/janus68ad_c2d2e5b3b2c2b1 && PYTHONPATH=. python -m unittest discover -s tests -v` : **13 tests Python PASS, 0 FAIL** (dont 2 identités SymPy incluses, non additionnées). `python numerics/hr_step68ad_c2d2e5b3b2c2b1_f_chart_coefficient.py` : JSON rationnel régénéré. Source originale Step45 blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` relues et SHA authentifiés ; **moteurs originaux et G paramétré NON RÉEXÉCUTÉS**.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS OCTET-IDENTIQUES AUX TESTS :**
- `numerics/hr_step68ad_c2d2e5b3b2c2b1_f_chart_coefficient.py` — blob `d16150475c4d3ac38162c8be06c07d8734efa4c2`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b1_f_chart_coefficient.py` — blob `c608333536783b0c67a1c842b0ba94253939331d`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b1-f-chart-coefficient.json` — blob `24d9f2cefa001b1fabd3634b87556cbab6c90b42`.
- `research/STEP68AD_C2D2E5B3B2C2B1_EXACT_F_CHART_COEFFICIENT_CONDITIONAL.md` — blob `cf2fe91387f667a0792633bf43d39b784cf39865`.

**HEAD DE REPRISE INITIAL RELU :** `c73949877acf4b30d67073f1b8d6a0d8d6641092`. **HEAD AVANT JOURNAL :** `7b1fdefb966223855858769fb94775016f2272b6`. Branches main et research/v2-flrw non modifiées, aucun workflow Actions touché. **NETTOYAGE LIBRARY :** deux suppressions par library_file_id retentées, 2 échecs `401 Unauthorized /uninjest_file` ; aucune suppression déclarée.

**ACTIONS PRIORITAIRES :** (1) exécuter le G physique original avec Pg variable, certifier une borne uniforme de U et rho_f sur un intervalle non nul de lambda ; (2) conditions aux limites externes admissibles ; (3) oracle fonctionnel original non-IBP à six couples, rang Dirac/tertiaires et lapses ; (4) K=0/J=0, 4D/stabilité/observables ; (5) nettoyage Library seulement si autorisations rétablies.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c2a, TUBE UNIFORME DE POUSSIÈRE g SOUS PARAMÈTRE P_g (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c2a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2b — exécuter le véritable moteur physique G(s,U,Pg) Step45/46/55 avec Pg variable, certifier la continuation du secteur f et la sensibilité, puis examiner les conditions aux limites, les crochets Dirac non-IBP six couples, rang/tertiaires, K=0/J=0, 4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU RÉSULTAT EXACT, STRICTEMENT LIMITÉ AU SECTEUR g :** à partir d'une transcription indépendante de la reconstruction g Step55, le programme en arithmétique rationnelle exacte avec encadrements dirigés des racines prouve sur les 256 cellules jointives `0<=s=r²<=289/400` et simultanément `|lambda|<=1/1000` que `22/25<rho_g<9/10`, `beta_g>999/1000`, `Lg>=2/5`, `Sg'>=2/5`, `sqrt(1-z²)>0`, `Pg+lambda<0`. Minima d'enclosure brute : rho_g≈0.8806795666522835, beta_g≈0.9991750787755442 ; majorant rho_g≈0.8963937829249305. Les seuils renforcés ont été comparés EXACTEMENT comme fractions. **Cette marge |lambda|<=1/1000 N'EST PAS une marge de solution physique complète, car la poussière f, le vrai G, la continuation U et les bords restent non certifiés.**

**TESTS EXÉCUTÉS :** `PYTHONPATH=/mnt/data python -m unittest -v test_hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube` : **13 unittest PASS, 0 FAIL** ; `python /mnt/data/hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube.py` : certificat 256 cellules généré ; audits 64/128/512 cellules exécutés ; 3 inégalités rationnelles renforcées PASS. Les sources originales Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalization `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` et barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ont été relues via GitHub. **MOTEURS ORIGINAUX NON RÉEXÉCUTÉS ; aucun vrai G ni matrice de Dirac exécutés.**

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube.py` — blob `0def484f17d991bca4b482091d4e45711ec8d1b6`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube.py` — blob `bff1e9a18a48311ba8cb90502f73ce6b822deb53`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2a-gdust-parameter-tube.json` — blob `9b775de06f6a391c6817fa2bdb184e09d887ea76`.
- `research/STEP68AD_C2D2E5B3B2C2A_UNIFORM_G_DUST_PARAMETER_TUBE.md` — blob `675b7826c8fe37d9a8032984f0df51b2edf3dcc5`.

**HEAD DE REPRISE INITIAL RELU :** `8fdf9c53aa7ba0c0d0f90a19b36e7dd2ee3803ab`. **BRANCHES INTERDITES RELUES INCHANGÉES :** main `aead63f4098f0d15a849e579105af034b6317b30`, research/v2-flrw `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`. Aucun workflow modifié. **NETTOYAGE LIBRARY :** deux suppressions retentées (`libfile_45aa141b5df881918aff37fe431c9c0b`, `libfile_17f52736778c819195709abedd20af01`), deux échecs `401 Unauthorized /uninjest_file`, aucune suppression déclarée.

**ACTIONS PRIORITAIRES :** (1) exécuter réellement les modules physiques originaux et leur G paramétré ; (2) obtenir une borne non nulle de lambda qui contrôle aussi U, la poussière f, les dénominateurs et les bords ; (3) calculer l'opérateur fonctionnel Poisson/Dirac non-IBP six couples, rang/tertiaires et lapses ; (4) K=0/J=0, 4D, stabilité et observables ; (5) retenter nettoyage Library seulement si autorisations changent.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2c1, TRACES EXTÉRIEURES EXACTES DE LA FAMILLE P_g (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2c1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c2 — exécuter l'authentique moteur G(s,U,Pg) Step45/46/55 avec Pg variable, calculer sa sensibilité et certifier une marge lambda et les bords réellement prescrits, puis oracle Dirac non-IBP six couples, rang/tertiaires, K=0/J=0, 4D/stabilité/observables. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU RÉSULTAT EXACT CONDITIONNEL AUX BORDS :** la famille paramétrique Step55 a pLg(r)=r² Pg (1+5cg r²/2), cg=0.0015. À R=17/20, ∂lambda pLg(R)=92730563/128000000=0.7244575234375>0 et ∂lambda pLg'(R)=2734739/1600000=1.709211875>0. Step49 donne ∂lambda U0=274023815147385251710689588080861/40000000000000000000000000000000000>0. Par conséquent, **SI** pLg(R), pLg'(R) ou U0 est fixé par les conditions aux limites, cette famille à un seul paramètre ne permet que lambda=0. Ce n'est PAS une obstruction JANUS générale : les conditions physiques ne sont pas encore établies, et d'autres directions ou des bords mixtes peuvent convenir. Identité Dg=r³ Dbar vérifiée pour les reconstructions g Step55, sans exécution de l'EDO f.

**TESTS RÉELLEMENT EXÉCUTÉS :** 11 tests Python unittest PASS, 0 FAIL depuis une arborescence numerics/ et tests/ ; commande `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c1_boundary_trace.py' -v`. Le certificat JSON a été régénéré et son blob Git correspond aux octets produits. Sources Step45/46/49/55 relues et SHA authentifiés ; moteurs historiques NON RÉEXÉCUTÉS. Aucune marge lambda0, aucun oracle complet de Dirac, aucune condition de bord globale prouvée.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS OCTET-IDENTIQUES :**
- `numerics/hr_step68ad_c2d2e5b3b2c1_boundary_trace.py` — blob `ef031e1016f53fb0615d588dc63814b1a5c29030`.
- `tests/test_hr_step68ad_c2d2e5b3b2c1_boundary_trace.py` — blob `eae8ea08049177749ef3aefc695c9ce765ac5071`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c1-boundary-trace.json` — blob `6909e2b896470f49825ee458e4bf39a60e60184d`.
- `research/STEP68AD_C2D2E5B3B2C1_EXACT_PARAMETER_BOUNDARY_TRACE.md` — blob `fa39bdf695aed12cd173623185f35f3b3cb0d80e`.

**HEAD INITIAL AUTHENTIFIÉ :** d32ec6b518cd403b1ad1373416d3cae3c37ca2b4. **BRANCHES INTERDITES :** main=aead63f4098f0d15a849e579105af034b6317b30 ; research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb, inchangées à la vérification. Aucun workflow modifié. **ACTIONS PRIORITAIRES :** (1) vraie exécution G physique paramétré et bornes lambda ; (2) spécifier les bords admissibles, tester la tangence avec ces bords ; (3) six couples Poisson/Dirac, rang, tertiaires, lapses et chartes singulières ; (4) 4D/stabilité/observables ; (5) nettoyage Library si autorisation rétablie.

**CHECKPOINT PRÉFIXÉ ; TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2b2b, TANGENTE RADIALE PARAMÉTRIQUE CONDITIONNELLE (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2b2b. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2c — exécuter l'authentique G(s,U,Pg) Step45/46/55 avec paramètre Pg variable, calculer sa sensibilité et certifier une marge de continuation lambda, puis imposer les conditions aux bords et construire le véritable oracle Dirac non-IBP six couples, rang/tertiaires, K=0/J=0. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVEAU THÉORÈME CONDITIONNEL, PAS UNE CERTIFICATION PHYSIQUE GLOBALE :** Step49 donne G(0,U;Pg)=3U0(Pg)−U et U0(Pg)=Mf2*b*(Pg/(Mg2*a)−2*z1). En faisant varier Pg dans TOUTES les reconstructions g Step55, en conservant géométrie/shift, puis en résolvant l'EDO originale 2sU_s=G(s,U;Pg)−2U et en reconstruisant les variables f par Step46, les cinq contraintes spatiales sont préservées sur l'intervalle **si** les identités originales et la continuation analytique sur la charte régulière compacte sont applicables. La tangente non triviale v=∂Pg U satisfait 2s v_s=(G_U−2)v+G_Pg sur tout 0<s≤289/400, v(0)=Mf2*b/(Mg2*a)=274023815147385251710689588080861/40000000000000000000000000000000000>0. La formule intégrale de Volterra exclut le mode singulier s^(-3/2). Le shift réduit reste régulier sur cette famille restreinte car la reconstruction g garde Dg=r³Dbar. **Ni l'admissibilité de la variation aux bords externes, ni un rang Dirac, ni les lapses globaux ne sont établis.** La variation de Pg change les données du benchmark.

**SOURCES ORIGINALES AUTHENTIFIÉES PAR LECTURE GITHUB, NON RÉEXÉCUTÉES :** Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; Step46 bac025c28dbe1561c0c36c56dbfda46dc326f804 ; Step49 d570948912885d45a625fa2db31c6a5435b6a654 ; Step55 normalization a54a6acf2f7ad2f64c500faecfa1406ecbf7b862 ; Step55 barrier a6e7004120d0a166a3a8973c2fbe1487a8eb70fe ; Step68o c99caebc17f243784450ddff94fb061767e6d8e7.

**TESTS EXÉCUTÉS ET REJOUÉS SUR LES FICHIERS PUBLIÉS :** 36 assertions rationnelles BigInt dans V8 + 10 assertions wrapper V8 + 21 contrôles SymPy indépendants scratch (9 jets de l'EDO synthétique, 9 jets linéarisés, 3 identités de centre/reconstruction), **67 vérifications PASS, 0 FAIL**. Le modèle de séries est synthétique et respecte la forme Step49, PAS le G physique ; le témoin Dg=9/10 est un contrôle algébrique synthétique. Pas d'exécution Node native ni des moteurs physiques Python historiques.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS OCTET-IDENTIQUES :**
- scripts/hr_step68ad_c2d2e5b3b2b2b_parameter_tangent.cjs — blob 2630dc6b2c7cc741f28a47dfa4a9b5d3bb0f1b80.
- tests/test_hr_step68ad_c2d2e5b3b2b2b_parameter_tangent.cjs — blob a12abddda71a42eec44b2303ec82d390bb0241e8.
- research/reports/gate2b-step68ad-C2d2e5b3b2b2b-parameter-tangent.json — blob f2912e4023720d62ea3af74abf58dd1fffb9eb7f.
- research/STEP68AD_C2D2E5B3B2B2B_CONDITIONAL_FULL_RADIAL_PARAMETER_TANGENT.md — blob e989a0fa7c486259d70ae76475f1249355f4343d.

**HEAD INITIAL RELU :** 36b61286cf123edf32748fec1b0ad3b13ecac101. **ACTIONS PRIORITAIRES :** (1) rejouer l'authentique G physique paramétré et dérivée G_Pg ; (2) obtenir une borne quantitative de lambda et contrôler les bords externes ; (3) opérateur fonctionnel non-IBP à six couples, rang complet/tertiaires et conditions de lapse ; (4) K=0/J=0, 4D, stabilité, observables ; (5) retenter le nettoyage Library si 401 se résout. Aucun workflow ni branche protégée modifié.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2b2a, CONTRE-EXEMPLE EXACT DE JET RADIAL SUPÉRIEUR (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2b2a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2b2b — dériver la famille tangentielle à la secondaire sur tout r via la variation de l'EDO Step55, puis oracle fonctionnel non-IBP six couples, bords, rang Dirac/tertiaires et J=0. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**NOUVELLE PREUVE CONDITIONNELLE EXACTE :** sur la solution analytique Step55/68o, avec s=r² et pLf=r²U(s), la secondaire primaire-réduite Step46 s'écrit C/r²=A(s,U)[W−G(s,U)] avec W=2U+2sU_s, A(0)=−m2 Mg2 At/(2 b Mf2)≠0. L'identité Step49 G(0,U)=3U0−U donne G_U(0)=−1. Pour la perturbation pLf→pLf+epsilon*r^6, f poussière et pSf reconstruits algébriquement, Hg, Hf, Fz et Ddiag restent nuls (sous les hypothèses originales), et les premiers jets centraux demeurent inchangés ; mais **delta C=7A(0)epsilon*r^6+O(epsilon*r^8)+O(epsilon²*r^10)**. Sur les paramètres rationnels physiques Step55, 7A(0) est strictement négatif (≈−3225.510376708569). Il s'agit d'un **contre-exemple hors coquille secondaire** à la suffisance des jets centraux, PAS d'une réfutation de JANUS, PAS d'une preuve de rang Dirac et PAS d'une réfutation de la famille Pg de l'étape précédente.

**SOURCES PHYSIQUES ORIGINALES RELUES SUR GITHUB, SHA AUTHENTIFIÉS, NON RÉEXÉCUTÉES :** Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step49 `d570948912885d45a625fa2db31c6a5435b6a654`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

**EXÉCUTION RÉELLE :** 12 assertions BigInt V8 du programme publié PASS ; 9 assertions adversariales V8 du wrapper publié PASS ; 15 tests unittest Python PASS, avec 9 sous-identités SymPy exactes dans un script scratch non publié. **Ne pas additionner les sous-identités aux tests unittest.** Aucun échec final. Les moteurs physiques originaux et le script Node dans un clone complet n'ont pas été exécutés.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS, RELUS BYTE-IDENTIQUES :**
- `scripts/hr_step68ad_c2d2e5b3b2b2a_secondary_highjet.cjs` — blob `572e458622c853a09d4e6d859af424442c8833cd`.
- `tests/test_hr_step68ad_c2d2e5b3b2b2a_secondary_highjet.cjs` — blob `96fc16ff68e7f7f60ccf472b31dc46a81fd108ae`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2b2a-secondary-highjet.json` — blob `5c6eefc2d4747f768d383213c3f21169f4f94a89`.
- `research/STEP68AD_C2D2E5B3B2B2A_EXACT_HIGHER_RADIAL_SECONDARY_JET_COUNTEREXAMPLE.md` — blob `691c09a7a2e658411396d5166a77a6605b5dac9d`.

**LIMITES ET PRIORITÉS :** (1) démontrer/tester la vraie équation tangentielle linéarisée sur tout le domaine radial, y compris les bords, et classifier les variations admissibles ; (2) calculer l'opérateur original Poisson/Dirac non-IBP sur six couples, rang et tertiaires ; (3) traiter K=0/J=0 et lapses globaux ; (4) 4D, stabilité et observables. Le contre-exemple ne fournit pas une famille tangentielle à C=0.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2b1, CONTRAINTES CENTRALES TRONQUÉES (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2b1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2b2 — linéariser les contraintes physiques comme fonctions sur la solution Step55/68o, puis véritable oracle Poisson/Dirac non-IBP six couples, bords, rang, tertiaires et J=0. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**SOURCES ORIGINALES RELUES SUR GITHUB, SHA AUTHENTIFIÉS, NON RÉEXÉCUTÉES :** Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step49 `d570948912885d45a625fa2db31c6a5435b6a654`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. La formule de C/r² est reprise du théorème historique Step49 après élimination de la primaire poussière f, **pas** nouvellement dérivée de l'intégralité du crochet original.

**NOUVEAU RÉSULTAT EXACT CONDITIONNEL AUX JETS CENTRAUX :** avec `Lg=a(1+cg r²)², Sg=r Lg, Lf=b(1+cf r²)², Sf=r Lf`, moments `pLg=r²(Pg+Pg1 r²)`, `pLf=r²(U+U1 r²)`, `pSg=r(2Pg+Psg1 r²)`, `pSf=r(2U+Psf1 r²)`, poussières `pg=r² rhog,pf=r² rhof`, gradients `tg'=r kg Lg,tf'=r kf Lf`, shift `z=r z1+O(r³)`, les deux primaires originales ont pour coefficients d'ordre r² `Hg2=-3Pg²/(4mg a)+rhog+24mg a cg+m2 mg Vg`, `Hf2=-3U²/(4mf b)+rhof+24mf b cf+m2 mg Vf`. Leurs annulations fixent les deux densités de poussière. Step49 impose `U=mf b(Pg/(mg a)-2 z1)` à partir de C2=0. `Dg3=a(Psg1+8cg Pg-4Pg1+kg rhog)`, `Df3=b(Psf1+8cf U-4U1+kf rhof)` ; choisir `Psg1=k0 z1/a-8cg Pg+4Pg1-kg rhog`, `Psf1=-k0 z1/b-8cf U+4U1-kf rhof` avec `k0=m2 mg a b(b1 a²+2b2 ab+b3 b²)>0` impose `Fz3=Dg3-k0 z1=0` et `Ddiag3=Dg3+Df3=0`. Une famille `Pg→Pg+epsilon` avec ajustement algébrique non linéaire des autres jets préserve **exactement ces contraintes TRONQUÉES** ; cela ne prouve PAS la tangence aux contraintes fonctionnelles globales.

**EXÉCUTION RÉELLE :** programme publié exécuté dans V8 : **25 assertions rationnelles BigInt PASS** ; wrapper adversarial exécuté dans V8 : **12 assertions PASS** ; contrôle SymPy indépendant en session : **15 identités exactes PASS** (courbures, primaires, moments radiaux, substitutions, famille finie et tangence), script SymPy scratch **non publié**. Total **52 vérifications PASS, 0 FAIL**, ne pas les présenter comme 52 tests unitaires Python. Moteurs physiques originaux NON réexécutés ; aucun oracle Dirac complet exécuté.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS, RELUS ET OCTET-IDENTIQUES :**
- `scripts/hr_step68ad_c2d2e5b3b2b1_center_constraint_jets.cjs` — blob `de5e67cc1082335718575a72a5d2794bdca7afc6`.
- `tests/test_hr_step68ad_c2d2e5b3b2b1_center_constraint_jets.cjs` — blob `90328310e4887cf63ab0c8ec6fd9da4639a20ed9`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2b1-center-constraints.json` — blob `418e647c8ae5aeaa1e7204af1ec052fa0bb16542`.
- `research/STEP68AD_C2D2E5B3B2B1_EXACT_CENTRAL_CONSTRAINT_JET_COMPATIBILITY.md` — blob `5b2f4df4901610138492502f974a79b1d051eae9`.
- README actualisé — blob `77cae587c72033479bf008bd7044e3ad3bd862cb`.

**NETTOYAGE LIBRARY :** suppressions réellement retentées sur `libfile_c03fc70b65508191b4df733834c5b614` et `libfile_45aa141b5df881918aff37fe431c9c0b` ; **2 échecs exacts `401 Unauthorized /uninjest_file`**, fichiers non supprimés.

**LIMITES ET ACTIONS PRIORITAIRES :** (1) dériver les contraintes linéarisées **pour tout r** sur la véritable solution Step55/68o, avec variations de poussière et shift régulier ; (2) calculer le crochet original non-IBP à six couples et termes de bord, rang complet/tertiaires ; (3) examiner K=0/J=0, lapses/bords ; (4) 4D/stabilité/observables. **Aucun rang Dirac, lapse global, liberté du fantôme ni validation cosmologique démontré.** Branche autorisée uniquement ; main/v2-flrw/Actions intouchés.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b2a, CHARTE CENTRALE DE PARITÉ DU SHIFT RÉDUIT (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b2a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2b — imposer les contraintes linéarisées Hg/Hf/C sur les variations centrales, puis calculer le véritable oracle fonctionnel non-IBP à six couples sur la solution Step55/68o, avec bords, rang Dirac, tertiaires et J=0. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**SOURCES ORIGINALES AUTHENTIFIÉES SUR GITHUB, NON RÉEXÉCUTÉES :** Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`.

**NOUVEAU THÉORÈME EXACT CONDITIONNEL À LA CLASSE DE PARITÉ :** avec `s=r²`, `Lg=L(s),Sg=rH(s),pSg=rP(s),pLg=r²G(s),pg=r²rho(s),tg'=rTd(s)`, et `Lf=Lf(s),Sf=rF(s)`, les expressions originales donnent `D=r C(s)`, `C=P(H+2sH_s)-2L(G+sG_s)+s rho Td`, `K=r² k(s)`. Si `k(0)>0` et fonctions analytiques, `z*=D/sqrt(K²+D²)=O(r)` si et seulement si `c0=P0H0−2L0G0=0`. Sur `c0=0`, `C=s d`, `z*=r d/sqrt(k²+s d²)`. Tangence nécessaire `H0δP0+P0δH0−2G0δL0−2L0δG0=0` ; pour `H0=L0,P0=2G0,δH0=δL0` : `δP0=2δG0`. **Ce n'est PAS la tangence aux contraintes de Dirac.**

**CONTRE-EXEMPLE ALGÉBRIQUE NON LINÉAIRE HORS COQUILLE :** `Pε=2+ε+ε²`, `Gε=1+ε/2`, `H=L=1` : `c0(ε)=ε²`, donc `c0(0)=c0'(0)=0` mais `zε(r)->+1` pour `ε≠0` fixé. La famille `Pε=2+ε,Gε=1+ε/2` a la même tangente non nulle et conserve exactement `c0=0`. La condition linéarisée seule ne garantit donc pas la charte pour des perturbations finies.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** programme publié V8 **18 assertions PASS**, wrapper adversarial V8 **14 assertions PASS**, contrôle indépendant SymPy **8 identités PASS** après correction d'un brouillon échoué (confusion temporaire entre `s` et `r²` dans le terme de poussière). **40 vérifications finales PASS, 0 FAIL** ; ne pas les appeler 40 tests Python. Le programme Node natif dans un clone et les moteurs physiques originaux **NON réexécutés**.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS :**
- `scripts/hr_step68ad_c2d2e5b3b2a_center_parity_chart.cjs` — blob `63b84e9fad6051c45961247ac00f5abd23e6a1e8`.
- `tests/test_hr_step68ad_c2d2e5b3b2a_center_parity_chart.cjs` — blob `062e028ac9e88977add283f57775dbab861e07f6`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2a-center-parity.json` — blob `a53cf171a7d5b76a7161e59b34e8c3e646cfd5af`.
- `research/STEP68AD_C2D2E5B3B2A_EXACT_CENTRAL_PARITY_SHIFT_CHART.md` — blob `1a39a677eb82ed0a4576bf0e26482bd46d1b61e0`.

**HEAD À LA REPRISE :** `dfa1d2636dbeea3570ada1f09f9bb346d3b810e8`. HEAD APRÈS QUATRE PUBLICATIONS SCIENTIFIQUES : `8414d468045185862a52d343f33061acb3516614`. HEAD FINAL À RELIRE APRÈS MISE À JOUR DU JOURNAL ET DE L'INDEX. Branches `main` et `research/v2-flrw` intouchées ; aucun workflow modifié.

**LIMITES :** aucune preuve de `δHg=δHf=δC=0`, ni matrice fonctionnelle complète de Poisson/Dirac, rang, tertiaires, lapses/bords, charte `J=0`, 4D, stabilité ou observables. **ACTIONS PRIORITAIRES :** (1) dériver/tester les contraintes linéarisées dans cette charte centrale ; (2) calculer les crochets non-IBP avec les six couples et variations transverses admissibles ; (3) bords/rang/tertiaires/J=0 ; (4) 4D/stabilité/observables ; (5) nettoyage Library des copies temporaires si l'autorisation revient.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE PRÉCÉDENT CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3b1, VARIATIONS TRANSVERSES DU SHIFT RÉDUIT AU CENTRE (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3b1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b2 — construire l'oracle fonctionnel original à six couples sur la vraie solution Step55/68o, après définition explicite de l'espace tangent des variations canoniques régulières, avec bords, rang Dirac, tertiaires, charte J=0. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**SOURCES PHYSIQUES ORIGINALES RELUES SUR GITHUB, SHA AUTHENTIFIÉS, NON RÉEXÉCUTÉES :** `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; `numerics/hr_step68o_temporal_interval_annulus.py` blob `c99caebc17f243784450ddff94fb061767e6d8e7`.

**NOUVEAU RÉSULTAT ALGÉBRIQUE EXACT (PAS UN RANG DIRAC) :** à K>0, `F_red=sqrt(K²+D²)`, `z*=D/F_red`. Hessienne de F_red sur (K,D) : `[[D²,-KD],[-KD,K²]]/(K²+D²)^(3/2)`, rang ponctuel 1 et trace 1/F_red ; ne PAS confondre avec la matrice de Dirac. Sur le chemin Step68o `K=r²k>0,D=r³ka/w,w=sqrt(1-r²a²),a=Z1`, les variations `δK=r²κ,δD=r³d` donnent exactement `δz=r*w²/k*(w*d-a*κ)` et `δ²F_red=r⁴*w/k*(w*d-a*κ)²`. Sous bornes régulières, ces réponses sont O(r) et O(r⁴).

**NOUVEAU CONTRE-EXEMPLE HORS COQUILLE À UNE LINÉARISATION UNIFORME NON RESTREINTE :** la perturbation lisse formelle `pLg_ε=pLg+εr²` (autres variables fixes) impose `∂εD=-2r Lg`, donc `∂εz|0=-2 Lg*w³/(r*k)`, divergent comme 1/r. Pour ε fixé non nul, `z_ε(r)→-sign(ε)` à r→0+, contre `z_0(r)→0`. Cela démontre une obstruction à l'emploi naïf de l'oracle réduit sur toutes les variations lisses off-shell dans la norme sup, **PAS une instabilité physique ni une impossibilité de la formulation non réduite**. Cette perturbation n'est pas certifiée tangentielle aux contraintes ou admissible aux bords.

**TESTS RÉELLEMENT EXÉCUTÉS :** script publié exécuté dans V8, **18 assertions rationnelles BigInt PASS, 0 FAIL** ; wrapper de tests publié rejoué dans V8 avec shim Node (9 assertions de rapport supplémentaires PASS). Rapport JSON reconstitué octet-identique à la publication. Pas d'exécution Node autonome dans un clone, pas d'exécution des moteurs physiques originaux. Témoin exact : r=3/4,a=w=4/5,k=2,κ=3,d=5,Lg=2/5, K=9/8,D=27/32,z=3/5, δz=48/125, δ²F=81/250, ∂εz=-512/1875, δ²F(pLg-r²)=512/3125.

**QUATRE LIVRABLES SCIENTIFIQUES PUBLIÉS ET RELUS :**
- `scripts/hr_step68ad_c2d2e5b3b1_shift_tangent.cjs` — blob `3e47422a3b3f5c4f61cc32bae1588929b5de2ace`.
- `tests/test_hr_step68ad_c2d2e5b3b1_shift_tangent.cjs` — blob `498949c2ba7343fe699726446f95fe2e586fef03`.
- `research/reports/gate2b-step68ad-C2d2e5b3b1-shift-tangent.json` — blob `05af81e309abac84eda716f1e3081bd486ca0c1d`.
- `research/STEP68AD_C2D2E5B3B1_SHIFT_REDUCTION_TRANSVERSE_CENTER_DOMAIN.md` — blob `efab645b92c9bec1ab2a26946d9718431167f100`.

**HEAD INITIAL LU DIRECTEMENT :** `40ab9560ae62f2e6e4b6bd4132767d32027f318c`. **APRÈS QUATRE ÉCRITURES SCIENTIFIQUES :** `66a1f48f50f27581f40658ff5f155ef0090c1403`. HEAD final à relire après journal, README et index. Aucun changement autorisé sur `main`, `research/v2-flrw` ou workflows désactivés.

**VERROUS :** espace tangent régulier et coquille linéarisée, vrai oracle fonctionnel Poisson/Dirac à six couples sur Step55/68o, rang complet/tertiaires, lapses/bords, J=0, dynamique 4D, stabilité et observables NON DÉMONTRÉS. **ACTIONS PRIORITAIRES :** (1) classifier les perturbations centrales de D,K issues des six couples et tester leur compatibilité avec les contraintes linéarisées ; (2) calculer les crochets fonctionnels non-IBP sur le profil exact avec bords ; (3) matrice de Dirac/tertiaires/J=0 ; (4) 4D/stabilité/observables ; (5) retenter le nettoyage des copies temporaires Library si le service récupère.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE PRÉCÉDENT CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b3a, CHARTE K=0 : SINGULARITÉ AMBIANTE ET CHEMIN PHYSIQUE (2026-10-27)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b3a. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3b — véritable oracle fonctionnel de Poisson/Dirac sur le profil authentique Step55/68o, variations transverses, bords, contraintes tertiaires, rang et charte J=0.** **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**SOURCES PHYSIQUES RELUES/AUTHENTIFIÉES MAIS NON RÉEXÉCUTÉES :** `numerics/hr_step55_global_barrier.py` Git blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; `numerics/hr_step68o_temporal_interval_annulus.py` blob `c99caebc17f243784450ddff94fb061767e6d8e7`. Formules reconstruites dans un script autonome à fractions rationnelles exactes + SymPy ; aucune exécution de l'EDO Step55, aucun rang Dirac calculé.

**RÉSULTAT EXACT NOUVEAU :** pour `F(z)=D*z+K*sqrt(1-z²)`, `F_z=D-K*z/sqrt(1-z²)`, la carte `z*=sign(K)*D/sqrt(K²+D²)` existe uniquement pour `K≠0` (racine intérieure). `K=0,D≠0` n'admet aucune racine intérieure ; `K=D=0` laisse tout `|z|<1` stationnaire avec `∂F_z/∂z=0`. Sur `K=epsilon,D=0`, `z*=0`, alors que sur `K=3epsilon,D=4epsilon`, `z*=4/5` et `∂z*/∂D=9/(125epsilon)` diverge. **Pas d'extension continue dans l'espace ambiant (K,D)** ; ce n'est PAS une obstruction physique définitive ni une preuve du rang Dirac.

**NOUVELLE GARDE RATIONNELLE CONTINUE :** sur la géométrie prescrite Step55 `0≤r≤17/20`, `K=r²*k(r)`, borne **exacte** `k(r)≥klo>0`, avec `float(klo)≈0.221156881156` (fraction intégrale dans le certificat). Par `ylo≤Lf/Lg≤Y`, `T/Lg²≥1+2*beta2*Y+beta3*ylo²>0`. Donc `K>0` pour `0<r≤17/20`, mais `K(0)=0`. Sur le chemin algébrique Step68o `D=r³*k*Z1/sqrt(1-r²Z1²)`, `Z1=0.004`, `z=r*Z1` et `|z|≤17/5000`, avec limite radiale unique `z(0)=0` ; **régularité le long de CE chemin seulement**, pas dans toutes les directions de l'espace des phases.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `cd /mnt/data/janus_e5b3 && python -m unittest -v test_hr_step68ad_c2d2e5b3_k0_chart.py` → **15 PASS, 0 FAIL** à la seconde exécution, après correction du premier essai échoué (SymPy avait besoin de l'hypothèse explicite `K>0` pour simplifier la racine). `python hr_step68ad_c2d2e5b3_k0_chart.py > report.json` → 16 sous-identités symboliques exactes PASS, 4 contrôles ponctuels rationnels PASS. Ne PAS additionner ces 16 sous-identités aux 15 tests.

**QUATRE FICHIERS SCIENTIFIQUES PUBLIÉS ET RELUS AUX SHA BLOBS TESTÉS :**
- `numerics/hr_step68ad_c2d2e5b3_k0_chart.py` — `4dc80d951cb0b400445c4df864b7d49345faddfc`.
- `tests/test_hr_step68ad_c2d2e5b3_k0_chart.py` — `e9d09f2656a4b2f44a7d82c064515d687a768321`.
- `research/reports/gate2b-step68ad-C2d2e5b3a-K0-chart.json` — `ce2f1bb0094433fe3fac86480fd97e102768179e`.
- `research/STEP68AD_C2D2E5B3A_K_ZERO_CHART_AMBIENT_VS_PHYSICAL_PATH.md` — `0b4592ebae296d9e614fba4ed05cee39932e2a4c`.

**HEAD À LA REPRISE :** `c592a6cfc14b52ebd9fc1b13ff9db56ba4e25487`. **APRÈS QUATRE PUBLICATIONS SCIENTIFIQUES :** `f54642b942e9f933b38cb6b1fe4edb8d22d2c241`. Lire HEAD final après README/journal/index. `main`, `research/v2-flrw`, workflows désactivés intouchables.

**VERROUS SCIENTIFIQUES :** vraie coquille physique et variations fonctionnelles transverses, matrice Poisson/Dirac complète, rang, tertiaires, bords/lapses, J=0, dynamique 4D, stabilité et observables NON DÉMONTRÉS. La garde K>0 ne concerne que la géométrie Step55 prescrite. **NETTOYAGE LIBRARY :** bundle éphémère `/JANUS-e5b3a-EPHEMERAL-publish-bundle-20261027.json` et deux dossiers temporaires précédents : suppression réellement retentée, trois échecs `401 Unauthorized`.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b2, ORACLE NUMÉRIQUE NON-IBP/IBP À SIX COUPLES (2026-10-26)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b2. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b3 — véritable profil physique Step55/68o dans l'oracle à six couples, bords, matrice complète de Poisson/Dirac, contraintes tertiaires, chartes K=0/J=0.** **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**SOURCES GITHUB AUTHENTIFIÉES (LUES, NON IMPORTÉES/EXÉCUTÉES) :** non-IBP Step37 `numerics/hr_step37_original_nonibp_oracle.py` blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`, IBP `numerics/hr_spherical_mixed_hamiltonian_bracket.py` blob `6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`, ADM `numerics/hr_spherical_adm_primary.py` blob `c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`. Formules reconstruites dans un programme Python autonome ; ne PAS prétendre avoir réexécuté les modules sources originaux.

**CALCUL RÉEL HORS COQUILLE :** 12 champs canoniques polynomiaux indépendants, deux poussières, 6 contributions de crochet Poisson ; 4 maillages n=41,81,161,321 sur r∈[0.1,0.9], smearings compacts, K>0. Crochets non-IBP = [0.04406642354880436,0.04382138009906760,0.04375925289385715,0.04374366606848031] ; IBP = [0.03544757475454052,0.04160021783705362,0.04319972683180122,0.04360351853125577]. Différences = [0.00861884879426384,0.00222116226201398,0.00055952606205594,0.00014014753722454], décroissance ≈ facteur 4 à chaque raffinement, compatible avec O(h²), PAS preuve continuum. Résidu F_z≤2.8e-17. Geler z* UNIQUEMENT dans les variations bulk change le crochet de <7e-15, contrôle de la règle de l'enveloppe, PAS du bord.

**BORDS :** N=M=1 non compacts, sauts des primitives B_g≈2.05424226, B_f≈0.63793473 ; erreurs action-originale moins IBP moins sauts diminuent quadratiquement (résidus maximaux 2.50e-5,6.21e-6,1.54e-6,3.85e-7). Les termes de bord ne sont PAS annulés sans conditions aux limites. K≤0 rejeté explicitement par ce moteur de benchmark, charte J=0 non traitée.

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_e5b2 && python -m unittest -v test_hr_step68ad_c2d2e5b2_six_pair_crosscheck.py` → **12 PASS, 0 FAIL** ; `python oracle.py > report_raw.json` → 4 maillages calculés. Les 6 contributions ne sont pas 6 tests indépendants ; les modules physiques historiques ne sont pas rejoués.

**FICHIERS PUBLIÉS ET RELUS OCTET-IDENTIQUES :**
- `numerics/hr_step68ad_c2d2e5b2_six_pair_crosscheck.py` — Git blob `83ab284cf38aaad3ab509be0ccbbb0df275fd72e`.
- `tests/test_hr_step68ad_c2d2e5b2_six_pair_crosscheck.py` — `2f18ac63f96b498f900b41dc78154f1009badac0`.
- `research/reports/gate2b-step68ad-C2d2e5b2-six-pair-nonIBP-IBP-crosscheck.json` — `def1df65dc4ec5480ad7aa5b0eca7947f7d5a811`.
- `research/STEP68AD_C2D2E5B2_SIX_PAIR_NONIBP_IBP_NUMERICAL_CROSSCHECK.md` — `f22fba82c022dfedeb74c258fa5074d0dfc811b5`.

**HEAD À LA REPRISE :** `f4ee5f02aa044d24bdc88ef25a42bbe7e8e4e146`; **HEAD APRÈS 4 PUBLICATIONS SCIENTIFIQUES :** `af25cd80ba7ddbee422471a29ee74be1cf390704`. Vérifier le HEAD final après index. `main` et `research/v2-flrw` protégées ; aucun workflow modifié.

**VERROUS :** rang complet de Dirac, lapses globaux/bords, contraintes tertiaires, vraie coquille physique, K=0/J=0, 4D, stabilité et observables NON DÉMONTRÉS. Un crochet hors coquille non nul ne prouve ni ne réfute la suppression du mode BD. Prochaine étape : **68ad-C2d2e5b3**, comparer sur Step55/68o, puis rang et bords. Nettoyage des copies temporaires Library à retenter.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5b1, VARIATION DU SHIFT RÉDUIT AU BORD (2026-10-26)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5b1. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e5b2 — calculer le véritable opérateur de Poisson/Dirac fonctionnel non-IBP à six couples, shift éliminé avec sa variation, termes de bord, rang et chartes K=0/J=0.** Le HEAD de branche et `research/AUTOMATION_STATE.json` prévalent sur tout repère daté.
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Branche d'écriture exclusive `research/gate2b-nonhomothetic-transfer`, `main`, `research/v2-flrw` et workflows désactivés intouchés.

**AVANCÉE EXACTE ET LIMITÉE :** sur K>0, `z*=D/sqrt(K²+D²)`, `D=pSg*Sg'-Lg*pLg'+pg*tg'`. Le terme de bord de C2d2e5a `B_shift=-(N+M Lg/Lf) pLg z*` possède la variation `∂B_shift/∂pLg'=(N+M Lg/Lf)pLg Lg K²/(K²+D²)^(3/2)`, généralement non nulle ; la variation à shift fixé ne la capture pas. Témoin rationnel hors coquille K=3,D=4,Lg=2,Lf=3,N=M=1,pLg=7 : z*=4/5, Fz=0, ∂z*/∂pLg'=-18/125, ∂B_shift/∂pLg'=42/25. Pour K<0, le signe de la racine doit être inversé : K=-3,D=4 donne z*=-4/5 et Fz=0, tandis que +4/5 donne Fz=8. À K=0,D≠0 pas de racine intérieure ; à K=D=0 racine non unique. Ces témoins ne sont PAS des solutions Step68o ni une preuve de rang Dirac.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `cd /mnt/data/janus_e5b && python -m unittest -v test_hr_step68ad_c2d2e5b_shift_boundary.py` : 9 tests PASS, 0 FAIL, incluant quatre sous-identités exactes SymPy ; `python hr_step68ad_c2d2e5b_shift_boundary.py` PASS. Trois sources originales GitHub relues et leurs SHA authentifiés ; modules physiques originaux non réexécutés. **AUCUN oracle Poisson complet ni matrice Dirac calculé.**

**FICHIERS PUBLIÉS, RELUS ET SHA BLOBS :**
- `numerics/hr_step68ad_c2d2e5b_shift_boundary.py` — `1996748565b7f587eaf46be3b740167e9bd1adbc` (identique aux octets testés).
- `tests/test_hr_step68ad_c2d2e5b_shift_boundary.py` — `d771a62f9a0806ed39f3eeeea54233258e2f5978` (identique aux octets testés).
- `research/reports/gate2b-step68ad-C2d2e5b1-shift-boundary-chain.json` — `68afbfb6264d693636a76850d669220ff509d147`.
- `research/STEP68AD_C2D2E5B1_REDUCED_SHIFT_BOUNDARY_VARIATION_AND_K_CHARTS.md` — `25e9192af017864bbed993263afbcc003ddd3acb`.

**ACTIONS PRIORITAIRES :** (1) dérivées fonctionnelles originales non-IBP avec variation complète de z* et bords ; (2) comparer aux six contributions canoniques IBP et tester tertiaires/rang ; (3) conditions aux bords/lapses et chartes K=0/J=0 ; (4) dynamique 4D, stabilité et observables ; (5) retenter le nettoyage Library 401 Unauthorized. Aucun changement de conclusion scientifique globale.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE PRÉCÉDENT CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e5a, IDENTITÉ DE BORD ORIGINALE NON-IBP (2026-10-26)

**ÉTAPE PARTIELLE TERMINÉE : 68ad-C2d2e5a — dérivation exacte du terme de bord original/IBP à shift fixé et audit des variations aux bords. PROCHAINE : 68ad-C2d2e5b — construire le véritable oracle fonctionnel de Poisson/Dirac à six couples sur coquille, shift éliminé, avec bords, rang, tertiaires et chartes K=0/J=0.**
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Seule branche d'écriture `research/gate2b-nonhomothetic-transfer`; `main`, `research/v2-flrw`, workflows désactivés inchangés.

**SOURCES PHYSIQUES ORIGINALES RELUES SUR GITHUB :** `numerics/hr_step37_original_nonibp_oracle.py` blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`; `numerics/hr_spherical_mixed_hamiltonian_bracket.py` blob `6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`; `numerics/hr_spherical_adm_primary.py` blob `c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`. Ces moteurs originaux n'ont PAS été réexécutés en Python ; reconstruction analytique et audit rationnel indépendants.

**NOUVEAU THÉORÈME EXACT, FIXED-z :** pour les termes de courbure EH non intégrés et le terme `pLg'` des Hamiltoniens originaux, `L_original-L_IBP=∂r B` avec `B=2Mg² N Sg Sg'/Lg+2Mf² M Sf Sf'/Lf-z pLg(N+M Lg/Lf)`. Les autres termes communs s'annulent dans la différence. Si `N=M=0` aux bords, `[B]=0`. Sans cette hypothèse, suppression du bord INJUSTIFIÉE. Contre-exemple exact HORS coquille : `Lg=1,Lf=2,Sg=r,Sf=2r,pLg=-r²,z=r/4,N=M=1,Mg²=Mf²=1`, `B(1/2)=195/64`, `B(1)=51/8`, `[B]=213/64`. Les coefficients de `δSg'`, `δSf'`, `δpLg` au bord sont respectivement `2Mg² N Sg/Lg`, `2Mf² M Sf/Lf`, `-z(N+M Lg/Lf)`. Flux des deux poussières dérivés séparément dans l'audit. Ceci ne démontre PAS d'obstruction physique définitive : fixer les variations ou ajouter des contretermes peut rétablir la différentiabilité, et la variation du shift éliminé `z_*` reste à traiter.

**TESTS RÉELLEMENT EXÉCUTÉS :** **28 assertions rationnelles BigInt PASS, 0 FAIL** dans V8 sur deux familles de champs, 7+4 rayons rationnels, lapses compacts/non compacts, contre-exemples négatifs, flux, six couples déclarés et chartes non régulières rejetées ; **3 identités symboliques SymPy indépendantes PASS** dans Python (courbures g/f et impulsion). Les assertions ne constituent PAS un oracle de Poisson six couples complet ; aucune matrice de Dirac ni contrainte tertiaire physique n'a été calculée.

**QUATRE LIVRABLES PUBLIÉS ET RELUS OCTET POUR OCTET :**
- `scripts/hr_step68ad_c2d2e5a_original_boundary.cjs` — Git blob `78fe086dd06004fdcf30c2f022f759595671275a`.
- `tests/test_hr_step68ad_c2d2e5a_original_boundary.cjs` — Git blob `49657554d7246aa0607161afd795c1714f7b3454`.
- `research/reports/gate2b-step68ad-C2d2e5a-exact-boundary.json` — Git blob `c0167d2c370ee131769e1d148640d4fe3b60ba66`.
- `research/STEP68AD_C2D2E5A_ORIGINAL_NONIBP_BOUNDARY_DIFFERENTIABILITY_AUDIT.md` — Git blob `4d1f229cba28ee83a2bb2c47c34969239fba3601`.
README synchronisé. HEAD au démarrage `c2d625d35df086f4295255f99cc6eead7df0d363`; les commits ci-dessus sont publiés sur la branche autorisée uniquement ; relire le HEAD final après mise à jour de l'index.

**NETTOYAGE :** huit suppressions Library par `library_file_id` exact ont été réellement retentées : huit échecs `401 Unauthorized` de `/uninjest_file`. Aucune suppression prétendue.

**LIMITES ET ACTIONS PRIORITAIRES :** (1) construire et confronter le crochet de Poisson non-IBP original à six couples avec variations du shift réduit et termes de bord ; (2) spécifier conditions aux bords et contretermes, tester lapses globaux et tertiaires ; (3) rang Dirac complet et chartes K=0/J=0 ; (4) dynamique 4D, stabilité, observables ; (5) retenter nettoyage Library. Le rang 1 de la seule ligne temporelle Step58 sur 1 810 cellules reste conditionnel, inchangé.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e4, AUDIT DU RANG LOCAL DES LAPSES (2026-10-26)

**ÉTAPE TERMINÉE : 68ad-C2d2e4 — raccordement rationnel conditionnel de quatre certificats originaux Step58. PROCHAINE : 68ad-C2d2e5 — calcul indépendant non-IBP du crochet fonctionnel de Dirac à six couples, contraintes et conditions aux bords, chartes K=0/J=0.**
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Seule branche d'écriture `research/gate2b-nonhomothetic-transfer`. `main`, `research/v2-flrw`, workflows désactivés intouchés.

**RÉSULTAT EXACT CONDITIONNEL :** quatre rapports originaux GitHub, authentifiés par SHA blobs (`0c688d6648e16064b1eb4e8ad9c55e7b44a95947`, `e890998a2f925f881ab85b60a9027e5828e35ed5`, `82f5d046cd0ca0c342adabe8b8f13cfc3f99308d`, `978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6`), contrôlés par calcul rationnel BigInt : 225+1006+314+265=**1 810 cellules fermées**, couverture sans lacune `r∈[1/64,17/20]`, `A_N>0`, `A_M<0`. Les inégalités uniformes `1/50000 < M/N=-A_N/A_M < 14`, `A_N/r²>7/20`, `A_M/r²<-546` sont valables **uniquement sous les hypothèses des quatre certificats** et de la coquille lisse. Les extrêmes sont dans Step68p : le raccordement intérieur ne les améliore pas. La SEULE ligne `[A_N,A_M]` est de rang local 1, mais le rang COMPLET de Dirac demeure **NON PROUVÉ**. Contre-exemple abstrait : deux complétions antisymétriques 6×6 avec même première ligne non nulle peuvent avoir rang 2 ou 4 ; elles ne sont pas les matrices physiques JANUS.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** **11 tests adversariaux synthétiques PASS, 0 FAIL** dans le même module JavaScript V8 publié (un cas valide, dix données corrompues rejetées) ; **1 exécution complète** sur les 1 810 cellules archivées, toutes vérifiées. Ce sont 11 tests, PAS 1 810 tests. Le CLI Node publié vérifie les SHA Git à partir des octets d'un clone local, mais **n'a PAS été exécuté dans un clone complet** pendant cette session ; les opérateurs physiques originaux n'ont pas été réexécutés, aucun oracle Poisson indépendant n'a été réalisé.

**QUATRE FICHIERS PUBLIÉS ET RELUS IDENTIQUES :**
- `scripts/hr_step68ad_c2d2e4_connected_row_rank.cjs` — SHA blob `a719cfed2292489b3c0e24cb6b422b9e42a823dd`.
- `tests/test_hr_step68ad_c2d2e4_connected_row_rank.cjs` — SHA blob `e5df52e75bfd38655afbcf6085e26198a835e46e`.
- `research/reports/gate2b-step68ad-C2d2e4-connected-row-rank.json` — SHA blob `a9721a0077d6ae0d89514b09b8476edf56451118`.
- `research/STEP68AD_C2D2E4_CONNECTED_LAPSE_ROW_RANK_AND_DIRAC_LIMITS.md` — SHA blob `778b33be781ed3cc7083b6e05f6debc1d5b84fc9`.

**HEAD AU DÉMARRAGE :** `2f7906e9c3f5093c49cb4ae8c8dd6ed68b6265b2`. **HEAD APRÈS QUATRE PUBLICATIONS :** `53f7844440b91044a9c4ddfbf3f9f9d16af7b807`. Les branches protégées restent aux références historiques `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` (à revérifier en fin de session).

**LIMITES PRIORITAIRES :** rang de la matrice/opérateur complet de Dirac, conditions aux bords des lapses, éventuelles contraintes tertiaires, jauge, chartes singulières `K=0/J=0`, oracle indépendant NON-IBP, évolution 4D, stabilité et observables NON DÉMONTRÉS. Le calcul d'un noyau de la ligne locale ne résout aucune de ces questions. Prochaine action : **68ad-C2d2e5**, commencer par reconstruire l'opérateur fonctionnel de Poisson indépendant avec les six couples et les termes de bord, puis chercher activement un contre-exemple ou une obstruction au rang admissible.

**INCIDENT DE NETTOYAGE :** huit suppressions Library réellement retentées par ID exact ; **8 échecs 401 Unauthorized** de `/uninjest_file`. Copies éphémères non supprimées, GitHub inchangé.

**CHECKPOINT PRÉFIXÉ ; TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ EXACTEMENT CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e3, DEUX SIGNES STEP58 CONTINUS CERTIFIÉS CONDITIONNELLEMENT (2026-10-26)

**ÉTAPE TERMINÉE : 68ad-C2d2e3 — CERTIFICATION CONDITIONNELLE SUR LE CONTINUUM des coefficients d'ordre zéro de l'opérateur ORIGINAL Step58, A_N>0 et A_M<0 sur r∈[1/64,1/32]. PROCHAINE : 68ad-C2d2e4 — audit contradictoire du rang Dirac complet et des lapses avec conditions aux bords, chartes singulières, puis 4D/stabilité/observables.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Seule branche d'écriture `research/gate2b-nonhomothetic-transfer`. Ne jamais toucher `main`, `research/v2-flrw` ni les workflows désactivés.

**AVANCÉE PHYSIQUE RIGOUREUSE SOUS HYPOTHÈSES :** 22/22 fichiers originaux, dépendances et trois rapports Step68v/68ac/B2 transférés par GitHub et authentifiés par SHA Git des octets locaux. Le véritable `physical_operator()['operator'][N/M][0]` Step58 a été évalué avec le vrai profil Step68o, sur la coquille régulière `Sg=r Lg,Sf=r Lf,K>0` et avec la factorisation CSE déjà démontrée exactement. L'opérateur dépend des jets radiaux d'ordre 3 : pour une preuve MVT continue, l'ordre 4 est indispensable. Nouveau prolongement des jets via l'EDO Step55 originale `2s U_s=G(s,U)-2U` : `U_ssss/24 = [t³]((G(s+t,U(s+t))-2U(s+t))/(2(s+t)))/4`, et `[r⁴]U(r²)=U_ss/2+2r²U_sss+(2/3)r⁴U_ssss`. Les 48 jets Step68o originaux d'ordres 0–3 sont inchangés et comparés exactement sur trois rayons (144 égalités).

**CERTIFICAT CONTINU :** 7 cellules originales ×32 sous-cellules rationnelles ; une sous-cellule grossière a été déclarée INCOMPLETE pour A_N et scindée en deux. Résultat **225/225 sous-cellules fermées couvrantes**, A_N.lower>0 et A_M.upper<0. Plus petite borne inférieure de A_N : `738081248225184126420269/312500000000000000000000000` (≈0,00236186). Plus grande borne supérieure de A_M : `-1514435823797833476506571291/1250000000000000000000000000` (≈−1,21155). Toutes les bornes sont rationnelles sur la grille entière extérieure 10^28, dérivées par AD d'intervalles + théorème des accroissements finis. Ce ne sont ni des tests ponctuels ni une preuve de rang Dirac.

**TESTS EFFECTIVEMENT EXÉCUTÉS :** `cd /mnt/data/janus_stage_c2d2e3 && PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e3_step58_mvt --repo . --out research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json` → 7/7 cellules, 225 feuilles, 1 bisection, PASS. `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e3_step58_mvt.py` → **18 PASS, 0 FAIL**. Inclus : vrais Step58 ponctuels, 144 comparaisons exactes de jets Step68o, SHA originaux, deux identités symboliques d'ordre 4, cas grossier INCOMPLETE, bisection positive et refus de rapports/sources altérés. Ne PAS compter les campagnes historiques comme rejouées.

**QUATRE FICHIERS PUBLIÉS ET RELUS AVEC SHA BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2e3_step58_mvt.py` — `8574eb05a64b251b007cc9f16d586bf1965467f0`.
- `tests/test_hr_step68ad_c2d2e3_step58_mvt.py` — `272500b23a94c6f812a21769bc2c94485fae19a9`.
- `research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json` — `0c688d6648e16064b1eb4e8ad9c55e7b44a95947`.
- `research/STEP68AD_C2D2E3_ORIGINAL_STEP58_CONTINUUM_SIGN_CERTIFICATE.md` — `520799e1a190d0f125a30b46eb0dc92cabba3644`.

**HEAD AU DÉMARRAGE :** `998ca92d2ef6797080a1deb9b8e5cd56e200cb03`. **HEAD APRÈS PUBLICATION DES QUATRE FICHIERS :** `3bae1997f7399d7f3eed49365f71fdd88a286150`. `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`, aucun changement.

**INTERPRÉTATION LIMITÉE :** Si les termes N',M',N'',M'' s'annulent sur la coquille contrainte lisse comme l'indiquent les identités historiques Step58/68h/68j et l'étape C2d2e2, l'équation locale `A_N N+A_M M=0` impose `N/M=-A_M/A_N>0`. Ce n'est PAS une démonstration de lapses globaux admissibles, de rang Dirac, de fermeture de l'algèbre des contraintes, de bords, de dynamique 4D, de stabilité ou d'observables. La preuve ne couvre pas les chartes K=0/J=0.

**ACTIONS PRIORITAIRES :** (1) audit contradictoire des contraintes Dirac complètes et du rang de l'opérateur, des lapses avec bords et de la cohérence des prolongations sur le profil exact ; (2) singularités K=0/J=0 ; (3) extension 4D, stabilité, observables ; (4) nettoyer les documents Google temporaires et copies Library éphémères si possible.

**CHECKPOINT PRÉFIXÉ. L'INTÉGRALITÉ DU JOURNAL PRÉCÉDENT EST CONSERVÉE OCTET POUR OCTET CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2e2, COMPOSITION CONDITIONNELLE DE LA COQUILLE SPATIALE (2026-10-26)

**ÉTAPE TERMINÉE : 68ad-C2d2e2 — preuve symbolique indépendante de composition des contraintes spatiales Step45/46/55/68o avec les identités historiques Step58/68h/68j. PROCHAINE : 68ad-C2d2e3 — enclosures corrélées des deux coefficients originaux Step58 A_N/A_M sur les sept cellules, puis Dirac/lapses/bords.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Branche unique `research/gate2b-nonhomothetic-transfer` ; `main`, `research/v2-flrw` et workflows désactivés intouchés.

**RÉSULTATS EXACTS CONDITIONNELS :** reconstruction symbolique indépendante de l'identité de réduction des primaires originales `H_a=A_a-dB_a/dr=kinetic+dust-M_a² L_a S_a² R_a/2+W_a+zD_g/L_a`. Les densités de poussière prescrites Step55 imposent exactement `H_g/r²=H_f/r²=0` pour r>0 ; `Psg` impose `D_g=r³ Dbar` et `F_z=0` sur la branche k>0. L'identité affine **HISTORIQUE** Step46 `C=C0+C1 pLf'`, `C1!=0`, avec l'EDO **HISTORIQUE** Step55 `2sU_s=G(s,U)-2U`, `G=V_rhs/r`, donne exactement `C=0` sur la vraie solution, et non sur des boîtes indépendantes arbitraires. Si les fonctions sont suffisamment régulières sur un intervalle ouvert, `Hg'=C'=Fz'=0` par dérivation. Composition avec les identités **DÉJÀ PROUVÉES** Step58/68h/68j : les coefficients de `N'',M'',N',M'` s'annulent sur cette coquille. Un contre-exemple avec `Hg=C=0` mais `Hg'!=0` prouve que les prolongations ne sont pas facultatives. Les valeurs `tg=tf=0` des jets Step68o sont des origines LOCALES, pas deux fonctions globalement nulles ; deux primitives polynomiales explicites rétablissent des champs de poussière globaux avec jets 1–3 exacts.

**TESTS RÉELLEMENT EXÉCUTÉS :** `cd /mnt/data/janus_stage && PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e2_spatial_shell_closure.py` → **14 PASS, 0 FAIL (0,87 s)**. Manifeste produit par `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e2_spatial_shell_closure`. Les 36 tests historiques ne sont PAS comptés comme réexécutés. Les sources physiques originales ont été RELUES en direct sur GitHub et leurs SHA enregistrés, mais les modules originaux Step45/46/55/68o/58/60 n'ont PAS été importés et exécutés ensemble ici : la preuve est une reconstruction/composition indépendante sous hypothèses, pas une exécution intégrale de ces moteurs.

**QUATRE FICHIERS PUBLIÉS ET RELUS, SHA BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2e2_spatial_shell_closure.py` — `63deac8423b9352cd3ed0c37c66247648e3d876b`.
- `tests/test_hr_step68ad_c2d2e2_spatial_shell_closure.py` — `f551d7ab14323424da478befd95617413e969274`.
- `research/reports/gate2b-step68ad-C2d2e2-conditional-spatial-shell.json` — `30d69cbe0796cba9851cdd48d21d15c6f8b33349`.
- `research/STEP68AD_C2D2E2_CONDITIONAL_SPATIAL_SHELL_AND_LAPSE_JET_COMPOSITION.md` — `f7ffd1c69ff4eec1d1882a1e94b1a9f6d252359f`.

**HEAD AVANT CHECKPOINT :** `abec7124030e1bf1be872c9c0984b928472cd814`. **HEAD DE DÉMARRAGE :** `47c3c384c08c217cf00ec2a58fbaf3a6f15bf023`. `main=aead63f4098f0d15a849e579105af034b6317b30`, `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`, aucune écriture dans ces branches.

**LIMITES :** aucun signe Step58 continu nouveau ; coefficient Step60 A_M<0 reste certifié CONDITIONNELLEMENT depuis C2d2d ; Step68j B_N(lower)=0 modulo Hg=C=0 reste un théorème ANTÉRIEUR ; aucun rang Dirac complet, lapse avec conditions aux bords, carte K=0/J=0, stabilité 4D ou observables. Les sources historiques n'ont pas été réexécutées localement dans cette session.

**ACTIONS PRIORITAIRES :** (1) construire et tester les enclosures corrélées originales Step58 `A_N,A_M` sur les sept cellules et rechercher des contre-exemples ; (2) confronter les signes/rations aux contraintes Dirac, lapses, bords et chartes singulières ; (3) examiner 4D, stabilité et observables ; (4) supprimer les copies temporaires Library lorsque le service de suppression cessera de renvoyer 401 Unauthorized.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ INTÉGRALEMENT CI-DESSOUS SANS AUCUNE MODIFICATION.**

---

# JANUS — RECTIFICATION SCIENTIFIQUE PRIORITAIRE : Step68j PROUVE DÉJÀ B_N=0 MODULO CONTRAINTES (2026-10-26)

**BRANCHE UNIQUE :** `research/gate2b-nonhomothetic-transfer`. **ÉTAPE VALIDÉE : 68ad-C2d2e (transversality conditionnelle J<0, corrigée par relecture Step68j). PROCHAINE : 68ad-C2d2e2 — vérification explicite des contraintes Step68o, puis Step58 continu.**
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**ERRATUM OBLIGATOIRE AU CHECKPOINT PRÉCÉDENT :** le résultat exact de l'étape historique Step68j, retrouvé dans `README.md`, `research/STEP68J_EXACT_FULL_CDOT_BN_SECONDARY_IDENTITY_AUDIT.md` et `numerics/hr_step68j_BN_exact_secondary_identity.py` (SHA `a500cdb1a09c853d46848719e26be9bbec55fb64`), était déjà établi : sur la charte régulière `F_z=0`, `B_N(original)=-alpha Hg'+beta Hg+(z/Lg)C`, `alpha=(1-z²)/(Lg Lf)`. Par conséquent le représentant Step60 `B_N(lower)=B_N(original)+alpha Hg' = beta Hg+(z/Lg)C`, et il **s'annule EXACTEMENT si Hg=C=0** ; le coefficient original s'annule aussi lorsque `Hg'=0`. Il était incorrect de présenter cette identité comme non prouvée en général sur la surface contrainte. La nouvelle pente `J=∂B_N(lower)/∂pSf<0` décrit la transversality HORS de cette surface, et n'invalide nullement Step68j. L'applicabilité à la totalité du profil physique et aux prolongations requises doit être explicitement vérifiée ; ni le rang Dirac ni les lapses ne sont résolus.

**NOUVELLE CERTIFICATION CONDITIONNELLE :** `∂² B_N(lower)/∂pSf²=0` EXACTEMENT sur la coquille `F_z=0` ; `J=∂B_N(lower)/∂pSf` est indépendant de `pSf` et `J<0` sur `r∈[1/64,1/32]` par 224/224 enclosures de Taylor/MVT rationnelles à arrondi extérieur. Plus grande borne supérieure `-345763471741167637281851/312500000000000000000000000` (≈−0,0011064431). La nouvelle certification est une sensibilité canonique partielle, PAS une nouvelle preuve de B_N=0. La tentative de simplification globale a expiré après 130 s ; le théorème Step68j existant a évité une redémonstration inutile.

**TESTS EXÉCUTÉS APRÈS CORRECTION FINALE :** `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e_bn_psf_transversality.py tests/test_hr_step68ad_c2d2d_correlated_mean_value.py tests/test_hr_step60_full_constraint_prolongation.py` → **36 PASS, 0 FAIL** (15 nouveaux, 21 régressions). En plus, le groupe Step68j de **13/25 dérivées symboliques** a été exécuté directement à terminaison normale et le point rationnel original `R_BN-z C/Lg=0,C=-53/40≠0` a été rejoué. Les 12 autres dérivées du théorème historique n'ont PAS été entièrement réexécutées ici (tentative supplémentaire >240 s) ; leur certificat original SHA-pinné `25a47c7eeed9dec111ecd3f5da891a02d84184d9` est authentifié. **28/28** fichiers sources/dépendances/tests/rapports historiques transférés et Git-SHA authentifiés.

**QUATRE FICHIERS PUBLIÉS, CORRIGÉS ET RELUS (SHA blobs des octets finaux testés) :**
- `numerics/hr_step68ad_c2d2e_bn_psf_transversality.py` — `69045785b00302f272aff266ce3d89e7fe0ba7ac`.
- `tests/test_hr_step68ad_c2d2e_bn_psf_transversality.py` — `a2f715c3bd8925ecfae4cc0c92e80587db36c1c2`.
- `research/reports/gate2b-step68ad-C2d2e-Step60-BN-pSf-transversality.json` — `0edd2a168efea3064abf9b948fb5c6de61293496`.
- `research/STEP68AD_C2D2E_STEP60_BN_PSF_TRANSVERSALITY.md` — `f5921c5a602a0aa2ae47dbf735cd2129c680baea`.

**HEAD INITIAL :** `155be7f5f486388ca4a75a4c5032aacea99bdb9f`. **HEAD APRÈS RECTIFICATION DES 4 FICHIERS :** `40a2de933c7d8ed4441eb39d3368c5affdc540ed`. `main=aead63f4098f0d15a849e579105af034b6317b30` et `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` inchangées. Documents Google éphémères supprimés ; deux bundles temporaires Library à nettoyer (service `401 Unauthorized`).

**ACTIONS PRIORITAIRES :** (1) vérifier sur le profil Step68o original `Hg=C=Hgprime=Fzprime=0` avec hypothèses et prolongations correctes, et le lien avec Step68j ; (2) enclosures corrélées continues des deux coefficients originaux Step58 ; (3) rang Dirac complet, lapses, conditions aux limites, dynamique 4D, stabilité et observables. Ne pas créer de pseudo-preuve de `B_N=0` déjà démontré, ne pas confondre une annulation modulo contraintes avec la fermeture globale.

**CHECKPOINT RECTIFICATIF PRÉFIXÉ ; TOUT L'HISTORIQUE ANTÉRIEUR, Y COMPRIS LE CHECKPOINT RECTIFIÉ, RESTE STRICTEMENT IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : Step60 B_N AFFINE EN pSf ET PENTE J<0 CERTIFIÉE SUR LE CONTINUUM (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. `main`, `research/v2-flrw` et les workflows désactivés sont intouchables.
**ÉTAPE TERMINÉE : 68ad-C2d2e — transversality conditionnelle de B_N en pSf. PROCHAINE ÉTAPE EFFECTIVE : 68ad-C2d2e2 — dériver exactement la racine pSf*=-B0/J et la comparer au pSf de la coquille Step68o, puis Step58 corrélé.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**PREUVE ALGÉBRIQUE EXACTE :** dans le véritable représentant inférieur Step60 `third_free_BN_on_Fz`, `d²B_N/d(pSf)²=0`, `J=dB_N/d(pSf)` indépendant de `pSf` ; donc `B_N=B0+J*pSf` pour les autres jets fixés sur la coquille de stationnarité (B0 ici = ordonnée à l'origine, non le paramètre beta0). **CERTIFICAT CONTINU CONDITIONNEL :** par différentiation automatique d'intervalles et théorème des accroissements finis sur 7×32 sous-cellules rationnelles de `r∈[1/64,1/32]`, 224/224 bornes supérieures de J sont strictement négatives ; maximum exact `-345763471741167637281851/312500000000000000000000000` (≈−0,00110644). Minimum inférieur exact `-45183603720227163110391799/10000000000000000000000000000`. Une perturbation indépendante `ΔpSf=1/10000` dans le véritable Step60 donne une variation négative cohérente avec J. **AUCUNE identité B_N=0 sur la solution radiale n'est prouvée ; aucun signe B_N continu n'est certifié.**

**DIAGNOSTIC CRITIQUE :** aux points r=1/64,1/48,1/32, l'intervalle B_N se contracte autour de zéro lorsque la précision expérimentale passe de 28 à 50 puis 80 décimales (largeurs ~10^-15,10^-37,10^-67). Ce n'est PAS une preuve exacte ; une tentative de simplification globale `sympy.cancel` a été arrêtée après 130 s. Les essais sur des cellules trop larges ont été correctement rejetés (INCOMPLETE, pas singularité physique). Ne pas confondre la pente partielle J avec un signe de B_N, un lapse ou le rang de Dirac.

**TESTS EXÉCUTÉS APRÈS CORRECTION FINALE :** `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e_bn_psf_transversality.py tests/test_hr_step68ad_c2d2d_correlated_mean_value.py tests/test_hr_step60_full_constraint_prolongation.py` → **34 PASS, 0 FAIL** (13 nouveaux, 21 régressions). `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e_bn_psf_transversality --repo . --out research/reports/gate2b-step68ad-C2d2e-Step60-BN-pSf-transversality.json` → 224/224 témoins rationnels négatifs. 24/24 blobs de sources, dépendances, rapports et tests historiques ont été authentifiés lors de la reconstruction locale depuis GitHub ; originaux physiques inchangés.

**QUATRE FICHIERS PUBLIÉS ET RELUS, BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2e_bn_psf_transversality.py` — `0c97d7dd3580f85e0268657a139a563208181e03`.
- `tests/test_hr_step68ad_c2d2e_bn_psf_transversality.py` — `4b2e888d0268f1875545cde6210c9f937e98dfbe`.
- `research/reports/gate2b-step68ad-C2d2e-Step60-BN-pSf-transversality.json` — `77dfc389993cef38f05671378efb6935b44404f3`.
- `research/STEP68AD_C2D2E_STEP60_BN_PSF_TRANSVERSALITY.md` — `c0252f29a6bd4cdfe70e32526592696cfd5028c5`.

**HEAD INITIAL RELU :** `155be7f5f486388ca4a75a4c5032aacea99bdb9f`. **HEAD APRÈS QUATRE FICHIERS :** `cfc78835b5ec8b17468a95daa4a985e622324bc6`. Les branches `main=aead63f4098f0d15a849e579105af034b6317b30` et `research/v2-flrw=dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` sont inchangées.

**LIMITES ET PRIORITÉS :** (1) prouver ou réfuter `B_N=0` sur la coquille Step68o par factorisation exacte de `B_N` et comparaison de `pSf*=-B0/J` avec le profil physique ; (2) certifier ou réfuter les signes continus Step58 `A_N/A_M` ; (3) seulement ensuite rang Dirac, lapses et bords, dynamique 4D, stabilité, observables. Step60 `A_M<0` antérieur reste certifié conditionnellement. Un fichier temporaire Library `/JANUS-C2d2e-EPHEMERAL-publish-bundle-20261026.json` reste à supprimer : tentative authentique de suppression échouée `401 Unauthorized`, comme les deux dossiers temporaires historiques ; les documents Google de transfert ont été supprimés.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE ANTÉRIEUR CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : Step60 A_M CERTIFIÉ STRICTEMENT NÉGATIF SUR LES 7 CELLULES CONTINUES (2026-10-26)

**BRANCHE D'ÉCRITURE UNIQUE :** `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main`, `research/v2-flrw` ni les workflows désactivés.
**ÉTAPE EFFECTIVE ACHEVÉE : 68ad-C2d2d — certification corrélée par théorème des accroissements finis du représentant inférieur A_M de Step60. PROCHAINE ÉTAPE : 68ad-C2d2e — traiter B_N Step60 et A_N/A_M Step58 sur le continuum, puis Dirac/lapses/bords.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT SCIENTIFIQUE EXACT ET CONDITIONNEL :** après authentification de 20 sources/rapports locaux (20/20 Git blobs identiques à GitHub), le véritable représentant inférieur `third_free_AM_on_Fz` de Step60 a été évalué avec les jets canoniques Step68o et les bornes spatiales SHA-pinnées Step68v/68ac/B2. Différentiation automatique radiale par intervalles à arrondi extérieur 10^-28, avec dérivées jusqu'à U_sss et factorisation d'interaction exactement vérifiée sur coquille. Sur chaque sous-cellule fermée [a,b], `A_M([a,b]) ⊆ A_M(m)+[-(b-a)/2,(b-a)/2] A_M'([a,b])`. Les 7 cellules originales ont été subdivisées en 32 sous-cellules rationnelles chacune : **224/224 bornes supérieures strictement négatives**, sans trou de couverture, `max A_M upper = -12463417589607208432272964557/10000000000000000000000000000` (environ -1,24634). C'est une certification CONTINUE conditionnelle du signe de ce représentant, pas une preuve de lapse admissible ni de rang Dirac.

**TESTS RÉELLEMENT EXÉCUTÉS :** `PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2d_correlated_mean_value.py` → **9 PASS, 0 FAIL (17,91 s après version finale)**. Vérifications des dérivées duales, domaines interdits, contre-exemple aux signes ponctuels, SHA sources, 224 sous-cellules, strictes fractions négatives, inclusion du véritable Step60 au milieu d'une sous-cellule et reproduction indépendante de la première borne. Les 224 évaluations physiques ont été exécutées en quatre lots bornés, sans les compter comme 224 tests pytest. Les 88 tests de régression de l'étape précédente ne sont PAS recomptés ni prétendus rejoués.

**FICHIERS NOUVEAUX PUBLIÉS ET RELUS, SHA BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2d_correlated_mean_value.py` — `534a7b57294ccbcfcdaa0708c63db415d644fc5f`.
- `tests/test_hr_step68ad_c2d2d_correlated_mean_value.py` — `9a44c876a6e319b759a126ae7cf83a579e6850d6`.
- `research/reports/gate2b-step68ad-C2d2d-Step60-AM-mean-value-compact.json` — `d4c81ec912ec6cdfce19585f79d06a2e6761ea12`.
- `research/STEP68AD_C2D2D_CORRELATED_MEAN_VALUE_STEP60_AM_CONTINUUM.md` — `37fad77c7db391ecb73fd15a3d872f5fe0195c24`.

**HEAD INITIAL DE CETTE SESSION :** `d4e95966f1e1f67243240ab38b08f63fec7ee8db`. **LIMITES :** Step60 `B_N` toujours INCOMPLETE ; Step58 `A_N,A_M` sur les sept cellules toujours INCOMPLETE ; contraintes Dirac, lapses et conditions aux bords, rang, dynamique 4D, stabilité, observables NON DÉMONTRÉS. Ne pas confondre signe de coefficient et signe de lapse. Aucune validation cosmologique.

**ACTIONS PRIORITAIRES :** (1) chercher annulation exacte de `B_N` sur coquille ou certificat corrélé ; (2) construire des bornes corrélées pour les coefficients Step58, avec dérivées suffisantes ou réduction symbolique de l'ordre ; (3) confronter au rang et aux conditions aux bords ; (4) réexaminer les hypothèses physiques, stabilité et observables. Nettoyage des anciennes copies temporaires Library à retenter seulement si le service autorise la suppression.

**CHECKPOINT PRÉFIXÉ ; TOUT L'HISTORIQUE ANTÉRIEUR EST CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : Step60 QUOTIENT INFÉRIEUR ORIGINAL EXÉCUTÉ SUR 7 CELLULES ; SIGNES CONTINUS INCOMPLETE (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main`, `research/v2-flrw`, ni les workflows désactivés.
**DERNIÈRE ÉTAPE EFFECTIVE : 68ad-C2d2c — EXÉCUTION PHYSIQUE CONDITIONNELLE DU QUOTIENT INFÉRIEUR ORIGINAL Step60 ; PROCHAINE ÉTAPE : 68ad-C2d2c-continuum-correlated-Step58-Step60.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**RÉSULTAT VÉRIFIÉ :** 24 fichiers sources/tests/rapports matérialisés depuis GitHub et vérifiés par recalcul des 24/24 Git blob SHA ; originaux Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7` inchangés. Le quotient original Step60 a été compilé à partir de `full_constraint_prolongation()['third_free_BN_on_Fz']` et `['third_free_AM_on_Fz']` (annulation exacte préalable des q''' originalement démontrée). Les CSE d'interaction originaux indices 103 (BN) et 107 (AM) ont été développés et comparés symboliquement au même T ; seule l'évaluation de T a été factorisée sur la coquille Sg=r Lg, Sf=r Lf, Lg>0, K>0.

**EXÉCUTION EFFECTIVE :** 7/7 cellules radiales [1/64,1/32] calculées avec les vrais jets Step68o et les rapports spatiaux SHA-pinnés ; 14/14 enclosures rationnelles Step60 BN/AM contiennent zéro ; **0/14 signes CONTINUS Step60 certifiés**. Huit frontières radiales évaluées : 8/8 enclosures de AM strictement négatives ; 8/8 enclosures BN contiennent zéro (proches de zéro mais identité NON démontrée) ; 8/8 AM Step60 intersectent AM Step58 original. Les 14 enclosures Step58 précédentes restent INCOMPLETE. **Ne jamais interpréter des signes ponctuels comme une preuve continue, ni des enclosures contenant zéro comme un contre-exemple physique.**

**TESTS RÉELLEMENT EXÉCUTÉS :** `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2c_step60_lower_quotient_replay --repo . --out research/reports/gate2b-step68ad-C2d2c-original-Step60-lower-quotient.json` → 7 cellules, 8 frontières, 0 signe continu ; `PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2c_step60_lower_quotient_replay.py tests/test_hr_step68ad_c2d2b_executed_temporal_probe.py tests/test_hr_step68ad_c2d2b_guard.py tests/test_hr_step68ad_c2d2a_temporal_replay.py tests/test_hr_step58_temporal_operator.py tests/test_hr_step60_full_constraint_prolongation.py` → **88 PASS, 0 FAIL (9 nouveaux, 79 non-régression)**.

**FICHIERS PUBLIÉS ET RELUS, GIT BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2c_step60_lower_quotient_replay.py` — `96196aa02050a274d055831ef0e9091141aeed2e`.
- `tests/test_hr_step68ad_c2d2c_step60_lower_quotient_replay.py` — `54d872c2b74169f4d8976341d1c05fea76c18aaa`.
- `research/reports/gate2b-step68ad-C2d2c-original-Step60-lower-quotient.json` — `e1b1eadabe99ffa49ea070caaaffb35981a4b5d2`.
- `research/STEP68AD_C2D2C_AUTHENTIC_STEP60_LOWER_JET_SEVEN_CELL_REPLAY.md` — `c7eb3be98ea269900f4729a76ed8712765e12e24`.

**HEAD À LA REPRISE :** `1aeb49a1502ea6a69ec9a51cd04fd36f9a7409fc`. **PROCHAINES ACTIONS PRIORITAIRES :** (1) construire et prouver un encadrement radial CORRÉLÉ des coefficients Step58 et Step60 sur sept cellules (Taylor avec majorant de reste, factorisation globale ou arithmétique affine rigoureuse) ; (2) certifier les signes continus ou garder INCOMPLETE ; (3) seulement ensuite étudier rang de Dirac, lapses et conditions aux bords, dynamique 4D, stabilité et observables. **AUCUNE validation JANUS.**

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE INTÉGRAL ANTÉRIEUR CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : Step58 PHYSIQUE EXÉCUTÉ SUR 7 CELLULES, SIGNES CONTINUS INCOMPLETE ; Step60 SYMBOLIQUE REJOUÉ (2026-10-26)

**BRANCHE UNIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main`, `research/v2-flrw`, ni les workflows désactivés.
**ÉTAPE EFFECTIVE TERMINÉE : 68ad-C2d2b, EXÉCUTION PHYSIQUE AUTHENTIQUE Step58 ; PROCHAINE ÉTAPE : 68ad-C2d2c, CERTIFICATION CORRÉLÉE DES SIGNES ET QUOTIENT INFÉRIEUR Step60.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**BLOCAGE MATÉRIEL RÉSOLU :** 22 fichiers (19 sources/tests Python + 3 rapports physiques) transférés depuis le connecteur GitHub dans un environnement Python unique ; 22/22 SHA Git blobs authentifiés sur les octets locaux. Les originaux Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7` restent intacts. Le transfert a utilisé un document Google temporaire, à supprimer après sauvegarde.

**EXÉCUTION RÉELLE :** `python -m numerics.hr_step68ad_c2d2a_temporal_replay --repo . --out ...` : échoue effectivement sur première cellule par `ZeroDivisionError: crossing zero` (dénominateur CSE d'interaction `beta1*Sg²+2beta2*Sg*Sf+beta3*Sf²` ; dépendance d'intervalles perdue, NON une singularité physique prouvée). Nouvelle factorisation exacte sur coquille `Sg=r Lg,Sf=r Lf` : `T=Sg²*(beta1+2beta2*(Lf/Lg)+beta3*(Lf/Lg)²)`. Identité des CSE `x79` (N) et `x75` (M) démontrée par SymPy sur les sources originales. **Step58 original exécuté sur les 7 cellules avec cette réécriture algébrique équivalente : 14/14 enclosures contiennent zéro, 0/14 signes continus certifiés.** 8 frontières radiales évaluées ponctuellement : 8/8 `A_N>0` et 8/8 `A_M<0` ; ces 16 signes ponctuels NE CERTIFIENT PAS LE CONTINUUM. Raffinement de la première cellule en 32,64,128,256 sous-cellules : tous les coefficients encore INCOMPLETE.

**STEP60 :** `python -m numerics.hr_step60_full_constraint_prolongation` réellement exécuté sur les originaux SHA-authentifiés (EXIT=0, ~11.49 s) ; annulation symbolique des coefficients q''' du quotient original confirmée (BN:1, AM:3, tous zéro). **Step60 quotient inférieur sur les 7 cellules NON ÉVALUÉ** ; le manifeste original indique `full_lower_jet_constraint_quotient=NOT COMPLETED`.

**TESTS EXÉCUTÉS :** `PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2b_executed_temporal_probe.py tests/test_hr_step68ad_c2d2b_guard.py tests/test_hr_step68ad_c2d2a_temporal_replay.py tests/test_hr_step58_temporal_operator.py tests/test_hr_step60_full_constraint_prolongation.py` : **79 PASS, 0 FAIL (21.60 s pytest)** ; 9 tests nouveaux, 70 préexistants. Aucun test physique de rang de Dirac ni lapse admissible.

**FICHIERS PUBLIÉS ET RELUS, BLOBS IDENTIQUES AUX OCTETS TESTÉS :**
- `numerics/hr_step68ad_c2d2b_executed_temporal_probe.py` — `c81c08502bdd50f6c13fbe09d1fcecf853036ffd`.
- `tests/test_hr_step68ad_c2d2b_executed_temporal_probe.py` — `1b2ac08636874501a800d0ce61608bec8274cf08`.
- `research/reports/gate2b-step68ad-C2d2b-executed-physical-temporal.json` — `a369c2e65205d228a734817df3d3a02cf0e41c3d`.
- `research/STEP68AD_C2D2B_AUTHENTIC_STEP58_EXECUTION_AND_INTERVAL_DEPENDENCY.md` — `188df51cc5d81ba690eb10806a4f99a36a215d9c`.

**HEAD À LA REPRISE :** `caf2bb50db5a17860fefe713d2996557eef33dd9`. **PROCHAINES ACTIONS :** (1) construire une enclosure corrélée/Taylor du Step58 original, avec test d'inclusion des enclosures ponctuelles et couverture de chaque cellule ; (2) certifier signes continus ou conserver INCOMPLETE/produire contre-exemple ; (3) évaluer quotient inférieur Step60 sur la coquille exacte ; (4) ensuite seulement Dirac/lapses/bords/4D/stabilité/observables. **NE PAS CONFONDRE signes ponctuels, annulations algébriques et cohérence physique globale.**

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE INTÉGRAL ANTÉRIEUR CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : COQUILLE STATIONNAIRE Step55/68o VÉRIFIÉE ALGÉBRIQUEMENT ; Step58/60 PHYSIQUES TOUJOURS PENDING (2026-10-26)

**BRANCHE D'ÉCRITURE UNIQUE :** `research/gate2b-nonhomothetic-transfer`. Interdiction de modifier `main`, `research/v2-flrw` et les workflows GitHub désactivés.
**DERNIÈRE ÉTAPE PHYSIQUE : 68ad-C2d2a (adaptateur uniquement). DERNIER LEMME CONDITIONNEL TESTÉ : 68ad-C2d2b-exact-Step68o-shift-shell. NEXT EFFECTIF : 68ad-C2d2b — EXÉCUTER LE VRAI Step58 SUR SEPT CELLULES, PUIS Step60.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## NOUVELLE IDENTITÉ STRUCTURELLE DU PROFIL PHYSIQUE PRESCRIT

Lecture directe GitHub : Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Reconstitution symbolique indépendante des **formules** originales, sans exécuter le Step58 complet : pour `s=r²`, `Dg=pSg*Sg'-Lg*pLg'+pg*tg'=r³ Dbar`, `K=r² k`, `Dbar=k*z1/sqrt(1-z1²r²)`. Les termes en densité de poussière et en moment gravitationnel se compensent exactement dans `Dg`. Ainsi `(Dg²+K²)(1-z1²r²)=r⁴k²`. Pour `r>0,k>0,1-z1²r²>0`, le shift stationnaire est **exactement `z=r*z1`**, donc `z'=z1,z''=z'''=0`. Les quatre jets du shift fixés par Step68o sont compatibles avec cette coquille. Si `k<0`, la branche de la racine positive inverse le signe : l'hypothèse est indispensable.

**TESTS EXÉCUTÉS :** `cd /mnt/data/janus_shift_shell && PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2b_exact_step68o_shift_shell.py` → **10 PASS, 0 FAIL (21,26 s)**. Manifeste `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2b_exact_step68o_shift_shell` → PASS (15,12 s). Ces tests portent sur des identités symboliques conditionnelles, pas sur les 14 coefficients temporels.

**FICHIERS PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_c2d2b_exact_step68o_shift_shell.py` — blob `3a996c87fd832d927066e0a68f17279df50ac84c`, identique aux octets testés.
- `tests/test_hr_step68ad_c2d2b_exact_step68o_shift_shell.py` — blob `7746ca04e8c46c34f17a8bf35c4f90cdd71b251b`, identique aux octets testés.
- `research/STEP68AD_C2D2B_EXACT_STEP68O_SHIFT_SHELL_AUDIT.md` — blob `a7a0fef0cd05519fa1830314489bc43c20a79498`.
- `research/reports/gate2b-step68ad-C2d2b-exact-Step68o-shift-shell.json` — blob `5e7abde6bbd0265874fca2cecad47ed2689ddfdf`.

**HEAD INITIAL RELU :** `a0e0b6a1215ed305d33eb583754eed3223ef58f8`. **BLOCAGE MATÉRIEL INCHANGÉ :** le conteneur Python ne possède pas le checkout original et les trois rapports ensemble ; DNS GitHub direct indisponible. Le connecteur GitHub lit et écrit correctement. **Step58 physique sept cellules NON EXÉCUTÉ ; Step60 quotient NON EXÉCUTÉ ; 0/14 nouveaux signes temporels certifiés.** Le lemme ne prouve ni le rang de Dirac, ni les lapses admissibles, ni les bords, ni la stabilité ni les observables.

**ACTIONS PRIORITAIRES :** (1) matérialiser sources authentifiées Step45/55/57/58/60/68n/68o/C2b + trois rapports dans un même Python ; (2) rejouer intégration C2d2a et garde C2d2b ; (3) évaluer le vrai Step58 sur les sept cellules et inspecter les 14 enclosures ; (4) évaluer Step60 avec les jets exacts du shift ; (5) si une enclosure traverse zéro, rester INCOMPLETE ; (6) seulement ensuite traiter Dirac/lapses/bords/4D. Ne pas remplacer l'exécution physique par une nouvelle succession de lemmes préparatoires.

**CHECKPOINT PRÉFIXÉ ; L'HISTORIQUE INTÉGRAL ANTÉRIEUR (341784 caractères) EST CONSERVÉ STRICTEMENT À L'IDENTIQUE CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : LEMME CONDITIONNEL DE SECOND JET SHIFT Step60 ; EXÉCUTION PHYSIQUE TOUJOURS PENDING (2026-10-26)

**SEULE BRANCHE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main`, ni `research/v2-flrw`, ni GitHub Actions/workflows désactivés.
**DERNIÈRE ÉTAPE PHYSIQUE : 68ad-C2d2a (ADAPTATEUR UNIQUEMENT). DERNIER LEMME ALGÉBRIQUE TESTÉ : 68ad-C2d2b-conditional-shift-second-jet. NEXT EFFECTIF : 68ad-C2d2b — EXÉCUTER LE VRAI Step58 SUR SEPT CELLULES, PUIS Step60.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## NOUVEAU RÉSULTAT EXACT — SECOND JET STATIONNAIRE DU SHIFT RÉGULARISÉ

Sources physiques Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509` et Step68o `c99caebc17f243784450ddff94fb061767e6d8e7` lues directement sur GitHub. Sur Fz=0, K>0 : `z=D/sqrt(D²+K²)`, `W=K*D'-D*K'`, `z'=K*W/(D²+K²)^(3/2)` et `z''=[K'W+K(KD''-DK'')]/(D²+K²)^(3/2)-3KW(DD'+KK')/(D²+K²)^(5/2)`. L'expression originale Step60 pour z'' donne exactement la même dérivée après substitution cohérente `z=D/R`, `z'=KW/R³`.

Si de plus `D=r³d(r²)`, `K=r²k(r²)`, `k>0`, d,k C³, alors `z=rA(r²)` avec `A=d/sqrt(k²+s d²)`, `z''=r(6A_s+4sA_ss)`, `z'''=6A_s+24sA_ss+8s²A_sss`. Au centre `z''(0)=0`, `z'''(0)=6(d1/k0-d0*k1/k0²-d0³/(2k0³))`. Il s'agit d'un **lemme algébrique conditionnel**, pas d'un résultat temporel sur les sept cellules.

**EXÉCUTIONS LOCALES :** `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2b_shift_second_jet` : 10 identités symboliques exactes ; `PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2b_shift_second_jet.py` : **10 PASS, 0 FAIL (1,42 s)**, six profils rationnels indépendants et deux contre-exemples de domaine/branche. Ces profils tests ne sont PAS des solutions physiques.

**FICHIERS PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_c2d2b_shift_second_jet.py` — blob `b10085e6c8cbfc562f3b2cc1a120eb6448535a57`, identique aux octets locaux testés.
- `tests/test_hr_step68ad_c2d2b_shift_second_jet.py` — blob `c3fb478715587c02bad49f95093e9d4b06a0cae1`, identique aux octets locaux testés.
- `research/STEP68AD_C2D2B_EXACT_SHIFT_SECOND_JET_CENTER_LEMMA.md` — blob `a364d1d8c4660903951e96db68e0750d5c376be4`.
- `research/reports/gate2b-step68ad-C2d2b-conditional-shift-second-jet.json` — blob `33e39f996abb54b8c943ac4a07645ece863eafba`.

**HEAD RELU À LA REPRISE :** `b3dd7c08e84933e1d43f9de0530553d4c695a907`. **BLOCAGE INCHANGÉ :** le conteneur Python ne possède pas les sources originales authentifiées et les trois rapports dans un même checkout ; DNS GitHub direct échoue. **Aucun vrai Step58/60 exécuté ; 0/14 nouveaux signes temporels physiques.** Le lemme ne prouve ni la réalisation de D=r³d(s) sur tout profil, ni les lapses admissibles, le rang de Dirac, les conditions aux bords, la stabilité ou les observables.

**ACTIONS PRIORITAIRES :** (1) réunir le checkout byte-authentique des dépendances et rapports ; (2) rejouer les tests d'intégration C2d2a/C2d2b ; (3) exécuter le véritable Step58 sur sept cellules et vérifier les 14 intervalles exacts ; (4) exécuter le quotient original Step60 en imposant les jets du shift stationnaire, notamment z' et z'' ; (5) si un intervalle traverse zéro, rester INCOMPLETE ; (6) seulement ensuite reprendre Dirac/lapses/bords/4D. **NE PAS CONFONDRE LEMME ET EXÉCUTION PHYSIQUE.**

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE INTÉGRAL ANTÉRIEUR CONSERVÉ CI-DESSOUS SANS MODIFICATION (338312 caractères).**

---

# JANUS — REPRISE PRIORITAIRE : 68ad-C2d2b CERTIFICAT DE SIGNES RENFORCÉ ; PHYSIQUE TOUJOURS PENDING (2026-10-26)

**SEULE BRANCHE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main`, ni `research/v2-flrw`, ni GitHub Actions/workflows désactivés.
**DERNIÈRE ÉTAPE PHYSIQUE : 68ad-C2d2a (ADAPTATEUR SEULEMENT). DERNIER CORRECTIF TESTÉ : 68ad-C2d2b-sign-enclosure-integrity. NEXT EFFECTIF : 68ad-C2d2b — EXÉCUTER LE VRAI Step58 SUR SEPT CELLULES, PUIS Step60.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## NOUVEAU CONTRE-EXEMPLE EXÉCUTÉ — 14 FAUX SIGNES CERTIFIÉS PAR ANCIEN RÉSUMÉ

L'ancien `summarize_temporal_signs` vérifiait les étiquettes `POSITIVE_CERTIFIED`/`NEGATIVE_CERTIFIED`, **sans jamais lire les intervalles**. Un contrôle négatif Python reproduisant fidèlement l'ancien algorithme retourne `True,True` pour sept cellules dont les 14 `enclosure=[-1,1]` traversent zéro. C'est un défaut RÉEL de validation du rapport, PAS une réfutation des opérateurs physiques originaux.

Le nouveau garde recalcule indépendamment les 14 signes depuis les fractions exactes des bornes, rejette les divergences étiquette/bornes, et vérifie que les sept cellules forment sans trou/recouvrement la couverture `[1/64,1/32]`. `N/M` dans le rapport signifient **coefficients A_N/A_M d'ordre zéro**, PAS valeurs des lapses N/M ; le résultat fournit `all_expected_A_N_positive_A_M_negative` (alias historique conservé).

**TESTS RÉELLEMENT EXÉCUTÉS : 23 PASS, 0 FAIL**, `cd /mnt/data/janus_c2d2b_integrity && PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2b_guard.py` (0,07 s). **1 contrôle négatif supplémentaire** de l'ancien résumé exécuté séparément. Ce sont des tests du GARDE, PAS de la physique.

**FICHIERS MODIFIÉS ET RELUS APRÈS ÉCRITURE, BLOBS IDENTIQUES AUX OCTETS LOCAUX TESTÉS :**
- `numerics/hr_step68ad_c2d2b_guard.py` — `7ea03654054632d1ca8ecbe9dbf8df0d66cf582c`.
- `tests/test_hr_step68ad_c2d2b_guard.py` — `cf8532bfc15ef2ebc0c2ec71a46985d8f6f866f1`.

**NOUVEAUX LIVRABLES RELUS :**
- `research/STEP68AD_C2D2B_SIGN_ENCLOSURE_INTEGRITY_AUDIT.md` — `d154d54d767224edb24016a6c8109c05c357aa8a`.
- `research/reports/gate2b-step68ad-C2d2b-sign-enclosure-integrity.json` — `8007c76e369ef07198f8797db47b15bf1a2b86ac`.

**LIMITES :** le vrai Step58 sur sept cellules et Step60 quotient n'ont PAS été exécutés ; 0/14 nouveaux signes temporels physiques. Tests d'intégration de l'adaptateur modifié non exécutés. Le conteneur Python ne dispose pas du checkout complet et ne peut résoudre GitHub ; le connecteur GitHub fonctionne en lecture/écriture, mais ne matérialise pas les sources dans le conteneur. Les anciens rapports de preuve restent CONDITIONNELS ; aucun rang de Dirac, lapses admissibles, bords, BD ou 4D validé.

**ACTIONS PRIORITAIRES :** (1) obtenir un checkout byte-authentique exécutable avec les 6 sources pinées, dépendances et 3 rapports ; (2) rejouer les 23 tests et l'intégration C2d2a ; (3) exécuter effectivement Step58 sur les sept cellules, vérifier 14 intervalles par le nouveau garde ; (4) exécuter le quotient original Step60 sur contraintes/shift prolongé ; (5) si zéro appartient à un intervalle, rester INCOMPLETE, affiner plutôt que certifier ; (6) traiter ensuite rang Dirac/lapses/bords/dynamique 4D.

**CHECKPOINT PRÉFIXÉ : les 334908 caractères de l'historique précédent sont conservés strictement à l'identique ci-dessous.**

---

# JANUS — REPRISE PRIORITAIRE : C2d2b GARDE RENFORCÉE, EXÉCUTION PHYSIQUE TOUJOURS PENDING (2026-10-26)

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer` ; ne jamais modifier `main`, `research/v2-flrw`, GitHub Actions/workflows désactivés.
**DERNIÈRE ÉTAPE PHYSIQUE VALIDÉE : 68ad-C2d2a (adaptateur seulement). DERNIER CORRECTIF TESTÉ : 68ad-C2d2b-interface-hardening. NEXT EFFECTIF : 68ad-C2d2b — EXÉCUTER LE VRAI Step58 ET ENSUITE Step60.**
**STATUT : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE D'ABORD :** `research/STEP68AD_C2D2B_INTERFACE_GUARD_AUDIT.md`, `numerics/hr_step68ad_c2d2b_guard.py`, `numerics/hr_step68ad_c2d2a_temporal_replay.py`, `research/AUTOMATION_STATE.json`. Tout l'historique est conservé ci-dessous.

## CORRECTIF CONCRET — BINDING DES BOÎTES ET ORIENTATION DES SIGNES

L'ancien `evaluate_original_step58` vérifiait le domaine radial demandé par Step68o, mais pas l'égalité entre le vrai `s=I.hull(rlo,rhi)**2` et l'intervalle `s` des bornes U/U_s/U_ss/U_sss injectées. Une boîte périmée pouvait donc être utilisée directement. Le nouveau garde vérifie cette égalité en fractions rationnelles EXACTES, la présence du marqueur outward, le domaine `s≤1/1024`, et les quatre paires ordonnées, avant toute évaluation.

La sortie distingue désormais la certification de non-nullité de N/M et la concordance avec le motif historique N>0, M<0 ; une orientation inverse n'est pas automatiquement qualifiée de confirmation physique.

**12 TESTS NOUVEAUX LOCAUX : 12 PASS, 0 FAIL**, `cd /mnt/data/janus_c2d2b_guard && PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2b_guard.py` (0,04 s). Tests de GARDE, pas de physique. Le test complet de l'adaptateur modifié n'a PAS été relancé en clone ; les 20 tests historiques C2d2a ne sont PAS comptés comme exécutés aujourd'hui. Sept intersections rationnelles des boîtes physiques ont été vérifiées indépendamment, 7/7 non vides, mais cela n'exécute pas Step58.

**SIX SOURCES ORIGINALES Step55/58/60/68n/68o/C2b RE-LUES ET REHASHÉES SHA Git : 6/6 MATCH**. Le module de garde et son fichier de tests publiés sont byte-identiques aux octets locaux testés.

**FICHIERS NOUVEAUX :**
- `numerics/hr_step68ad_c2d2b_guard.py` — blob `a0657a023fc59073bd1ab9f9a4255cf5248e0b9b`.
- `tests/test_hr_step68ad_c2d2b_guard.py` — blob `78a00ecccbffbfbd5d262c1cac9d6437d12f3c3f`.
- `research/STEP68AD_C2D2B_INTERFACE_GUARD_AUDIT.md` — blob `33a35f037f2d0c0bbb1f0c174d6f0dc62de08bae`.
- `research/reports/gate2b-step68ad-C2d2b-interface-guard.json` — blob `bef872259eba1f9086ec44940b2101b22c63b486`.

**FICHIERS MODIFIÉS :**
- `numerics/hr_step68ad_c2d2a_temporal_replay.py` — blob `e5a6c34ba95548527bc26d946f1e210d77355ee6`.
- `tests/test_hr_step68ad_c2d2a_temporal_replay.py` — blob `1efb3dc7515c5af00cd487bc98aa49ad6edcf8d9`.

**BLOCAGE EXACT :** le connecteur GitHub peut lire/écrire, mais le conteneur de calcul ne peut pas résoudre/joindre GitHub pour cloner et ne possède pas de checkout complet. **Aucun vrai coefficient Step58/60 calculé aujourd'hui ; 0/14 signes temporels nouveaux ; Step60 quotient NON exécuté.** Ne pas confondre garde testée et preuve physique.

**NEXT 68ad-C2d2b TOUJOURS OUVERT :** matérialiser les fichiers authentiques complets et trois rapports dans un même environnement Python ; exécuter les 20 tests de l'adaptateur plus les 12 nouveaux ; exécuter le vrai `numerics.hr_step68ad_c2d2a_temporal_replay.run()` sur 7 cellules, inspecter les 14 intervalles N/M (et les orientations), puis le vrai quotient Step60 avec contraintes et shift prolongé. Ne jamais certifier un intervalle contenant zéro. Rang Dirac, lapses positifs/bords, BD et dynamique 4D restent OPEN.

**CHECKPOINT PRÉFIXÉ ; LES 331101 CARACTÈRES DE L'HISTORIQUE ANTÉRIEUR SONT CONSERVÉS OCTET POUR OCTET CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-C2d2a TERMINÉE (2026-10-26)

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. NE PAS MODIFIER `main`, `research/v2-flrw` ni les GitHub Actions/workflows désactivés.
**DERNIÈRE ÉTAPE RÉELLEMENT TESTÉE : 68ad-C2d2a (garde d'arrondi extérieur + adaptateur original Step58). NEXT : 68ad-C2d2b (EXÉCUTION PHYSIQUE EFFECTIVE).**
**STATUT INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68AD_C2D2A_OUTWARD_DOMAIN_GUARD_AND_TEMPORAL_REPLAY.md`, `numerics/hr_step68ad_c2d2a_temporal_replay.py`, `tests/test_hr_step68ad_c2d2a_temporal_replay.py`, `research/AUTOMATION_STATE.json`. Historique antérieur conservé intégralement CI-DESSOUS.

## NOUVEAU RÉSULTAT MÉTHODOLOGIQUE — DÉFAUT RÉEL DE COUVERTURE PAR ARRONDI

Le Step68o original évalue `si=I.hull(rlo,rhi)**2`, qui est plus large que `[rlo²,rhi²]` pour plusieurs frontières internes rationnelles. Les boîtes C2b construites sur les seules frontières exactes ne suffisent donc pas telles quelles pour garantir une inclusion sur le vrai domaine machine. **Contre-exemple exécuté :** pour `r∈[1/56,9/448]`, la fonction test `U(s)=s` dépasse sa borne idéale à l'extrémité arrondie supérieure. Ce constat concerne la preuve d'intervalle, PAS une invalidation physique du modèle.

Un nouvel adaptateur reconstruit la boîte `U,U_s,U_ss,U_sss` sur les bornes EXACTES de l'intervalle entier `si`, par fractions rationnelles et certificats historiques. Il injecte le jet `[U,U_s,U_ss/2,U_sss/6]` uniquement pendant l'appel au vrai Step68o, avec restauration automatique de la fonction d'origine et rejet des sources non conformes aux SHA Git attendus. Les sorties futures ne pourront certifier un signe que si l'intervalle exclut strictement zéro.

**20 TESTS LOCAUX RÉELLEMENT EXÉCUTÉS : 20 PASS, 0 FAIL**, `PYTHONPATH=/mnt/data/janus_c2d2a python -m pytest -q /mnt/data/janus_c2d2a/tests/test_hr_step68ad_c2d2a_temporal_replay.py` (0,07 s). Les tests utilisent des DOUBLES pour I/Jet/Step68o : **le vrai Step58/60 et les sept signes temporels n'ont PAS été exécutés dans cette session**. Le conteneur ne dispose pas du clone GitHub complet (DNS GitHub inaccessible) ; la provenance positive des six dépendances sera vérifiée par le nouveau code lors de sa première exécution dans un clone.

**TROIS FICHIERS PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_c2d2a_temporal_replay.py` — blob `6b68c33ceac7f1f1a890e0d61a938a9ddb23ea95`, identique aux octets locaux testés.
- `tests/test_hr_step68ad_c2d2a_temporal_replay.py` — blob `3dea95d2233ea23b5cbee2583a38ca5a9be16dba`, identique aux octets locaux testés.
- `research/STEP68AD_C2D2A_OUTWARD_DOMAIN_GUARD_AND_TEMPORAL_REPLAY.md` — blob `589b473285143af59890545d898dba6140336ca4`.

**NEXT 68ad-C2d2b :** dans un clone complet, exécuter réellement `PYTHONPATH=. python -m numerics.hr_step68ad_c2d2a_temporal_replay --repo . --out research/reports/gate2b-step68ad-C2d2b-original-temporal-seven-cells.json` et les tests d'intégration, examiner les 7 intervalles N/M du vrai Step58 ; ne jamais inventer les signes si les boîtes traversent zéro. Exécuter ensuite le quotient Step60 avec le vrai shift et les contraintes ; approfondir Dirac/lapses/bords/BD/4D seulement sur preuves. **NE PAS CONFONDRE HARNESS TESTÉ ET ÉVALUATION PHYSIQUE EXÉCUTÉE.**

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE INTÉGRAL CONSERVÉ CI-DESSOUS.**

---

# JANUS — REPRISE PRIORITAIRE : STEP68ad-C2d1 TERMINÉE (2026-10-26)

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main`, ni `research/v2-flrw`, ni les workflows/Actions GitHub désactivés.
**DERNIÈRE ÉTAPE VÉRIFIÉE : 68ad-C2d1 (annulation exacte de la variation du shift et régularité conditionnelle au centre). NEXT : 68ad-C2d2.**
**STATUT SCIENTIFIQUE INCHANGÉ : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**LIRE EN PREMIER :** `research/STEP68AD_C2D1_EXACT_SHIFT_RESPONSE_CENTER_CANCELLATION.md`, `numerics/hr_step68ad_c2d1_shift_variation_center.py`, `research/reports/gate2b-step68ad-C2d1-shift-variation-center.json`, `research/AUTOMATION_STATE.json`. Le checkpoint 68ad-C2c et TOUT l'historique antérieur sont conservés intégralement CI-DESSOUS.

## RÉSULTAT ORIGINAL VÉRIFIÉ — RÉPONSE DU SHIFT AU CENTRE

**TROIS SOURCES PHYSIQUES ORIGINALES AUTHENTIFIÉES PAR SHA-1 GIT RECALCULÉ SUR LE CONTENU COMPLET LU VIA LE CONNECTEUR :** Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`. La reconstruction algébrique indépendante reproduit les densités originales post-IBP et les variations canoniques utiles de D,K ; le code original Step58 Cdot et Step60 quotient n'ont PAS été exécutés.

**HUIT IDENTITÉS EXACTES HORS CONTRAINTES :** les coefficients des dérivées secondes et troisièmes des lapses N,M dans `deltaD` et `deltaK` s'annulent identiquement (2 secteurs × 2 grandeurs × 2 ordres). Cela concerne seulement le SOUS-OPÉRATEUR de réponse du shift, pas les dérivées de lapse du Cdot complet.

**LEMME DE CENTRE CONDITIONNEL :** avec `Lg(0)=A>0, Lf(0)=B>0, pLg=r²(G+O(r²)), pSg=r(P+O(r²)), z=rZ`, les limites symboliques exactes donnent
```
lim (deltaD_N0/r) = Z(P-2G)
lim (deltaD_M0/r) = 3AZ(P-2G)/B
Fz=0 impose P=2G (car D=A(P-2G)r+O(r³), Kz=O(r³)).
```
Les coefficients de profils d'ordre supérieur sont laissés symboliques. Sur Fz=0 : `deltaD_N0,deltaD_M0=O(r³)`, `deltaD_N1,deltaD_M1=O(r²)`, `deltaK_N0,deltaK_M0=O(r²)`, `deltaK_N1,deltaK_M1=O(r³)`. Pour des lapses réguliers PAIRS `N',M'=O(r)` et `K/r²>0` (C2c), le shift non figé vérifie `deltaZ=Z_D deltaD+Z_K deltaK=O(r)`, malgré `Z_D=O(r^-2)` isolément. Cela NE démontre ni l'existence de lapses positifs, ni la préservation de C, ni l'absence du fantôme BD.

**22 TESTS LOCAUX RÉELLEMENT EXÉCUTÉS : 22 PASS, 0 FAIL**, `cd /mnt/data/janus_c2d1 && PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d1_shift_variation_center.py` (11,21 s). Les tests exécutent la reconstruction SymPy exacte, PAS les coefficients temporels complets Step58/60. Les sept signes temporels restent PENDING.

**QUATRE FICHIERS PUBLIÉS ET RELUS :**
- `numerics/hr_step68ad_c2d1_shift_variation_center.py` — blob `2e499b7ea3d1fe0a87df7a485c3bb9367a00a0e3`, identique aux octets locaux exécutés.
- `tests/test_hr_step68ad_c2d1_shift_variation_center.py` — blob `6913aaeba68925d8405d9dacb830c7a57cc1f5e9`, identique aux octets locaux exécutés.
- `research/reports/gate2b-step68ad-C2d1-shift-variation-center.json` — blob `e8647d7dbc808b9ee18e5042094ea985b563a21d`, identique au certificat local.
- `research/STEP68AD_C2D1_EXACT_SHIFT_RESPONSE_CENTER_CANCELLATION.md` — blob `ccffef117d8c48bfa908eaea85db33f9478cbfaa`.

**NEXT 68ad-C2d2 :** reconstituer les dépendances originales dans un environnement d'exécution, convertir les 7 boîtes C2b en jets `old.I` sortants, exécuter réellement les A_N/A_M de Step58 et les quotients Step60 sans figer le shift ; si une borne contient zéro, conserver INCOMPLETE. Exploiter la factorisation en r des variations avant division par K. Rang Dirac, lapses/bords, J/K, NON-IBP, BD, dynamique 4D et observables toujours ouverts.

**CHECKPOINT PRÉFIXÉ ; HISTORIQUE COMPLET CONSERVÉ CI-DESSOUS.**

---

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

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

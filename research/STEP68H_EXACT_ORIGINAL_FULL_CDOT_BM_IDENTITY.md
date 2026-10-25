# JANUS — Étape 68h : le coefficient de M' du VRAI crochet temporel est exactement proportionnel à Fz'

**25 octobre 2026. Branche de recherche exclusive :** `research/gate2b-nonhomothetic-transfer`. **GATE 2B OPEN — JANUS-R NOT_VALIDATED.**

## 1. Résultat nouveau, plus fort que la réduction Step68g

Dans le vrai crochet temporel \(\dot C_{\rm red}\) original Step58 à **six couples canoniques** et deux poussières mobiles, notons
\[
B_M=[\dot C_{\rm red}]_{M'} .
\]
Dans la charte du déplacement relatif \(|z|<1\), \(K>0\), métriques régulières et branche racine positive, le calcul exact prouve **sans imposer \(H_g,H_f,C\)** :
\[
\boxed{
F_z=0\ \Longrightarrow\
B_M=\lambda F_z',
\qquad \lambda=\frac{3z(z^2-1)}{L_gL_f^2}.
}
\]
Par conséquent :
\[
\boxed{F_z=0,\quad F_z'=0\ \Longrightarrow\ B_M=0.}
\]

Il s'agit du coefficient des premières dérivées du **lapse M** dans le **crochet secondaire complet**, pas seulement dans la variation du shift. Le résultat est **indépendant de la branche spéciale Step55** : aucune valeur numérique de ses constantes n'a été substituée pour obtenir l'identité.

## 2. Chaîne de preuve symbolique EXÉCUTÉE

Les sources historiques originales de Step45, Step57 et Step58 sont vérifiées **octet pour octet** avant le calcul :

- `66aa43841dccfe4a5d586a49be9c10af3a67a10e` — Step45, Hamiltonien et Ward à six couples ;
- `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f` — Step57, pullback du shift ;
- `802c23aebd41780d8c462f1aa1711707fe4ee88f` — Step58, opérateur temporel complet.

Step68g avait déjà démontré que le représentant
\[
R_{B_M}=B_M-\lambda F_z'
\]
ne dépend **d'aucun des douze jets \(q_i''\)** sur la stationnarité `Fz=0`, et que le représentant pouvait être construit sans geler ces jets.

**NOUVEAU :** dans `numerics/hr_step68h_BM_global_identity.py`, ce représentant réduit dépend syntaxiquement de **24 autres symboles indépendants**. Pour **CHACUN des 24**, le programme calcule la dérivée symbolique exacte, met le résultat sur un dénominateur commun et vérifie que son **numérateur développé est strictement le polynôme ZÉRO**. Cette étape est une vérification d'identité algébrique (pas d'échantillonnage).

Comme les dérivées sont toutes nulles, le représentant est constant sur chaque composante régulière analytique de la charte. Une valeur de référence **exactement rationnelle et non singulière** (notamment `z=3/5`, `sqrt(1-z²)=4/5`, `zr=1/10`, `tgr=0`, `beta2=-1/2`, autres variables à 1) donne exactement `R_BM=0`. La forme rationnelle/radicale et les identités de numérateur permettent la conclusion sur la branche physique régulière positive considérée, où les racines et dénominateurs sont définis.

**Contrôle indépendant plus fort :** en résolvant **directement** `Fz=0` pour `pLg'`, puis `Fz'=0` pour `pLg''`, un point canonique rationnel construit sans imposer les autres contraintes donne exactement
\[
F_z=F_z'=B_M=0,
\]
tout en ayant **les autres contraintes strictement non nulles** :
\[
H_g=357/80,\qquad H_f=33/10+11\sqrt2/10,\qquad C=-247/200.
\]
Cette contre-vérification exclut que l'annulation de \(B_M\) ait été fabriquée en imposant clandestinement \(H_g,H_f,C\).

Le test du **mauvais signe** `B_M+lambda*Fz'` conserve un coefficient non nul devant `pLg''`.

## 3. Reproductibilité et sauvegarde

Nouveau code byte-identique au GitHub et à l'exécution locale :
- `numerics/hr_step68h_BM_global_identity.py` — Git blob `991eeb0e1b557a65964ca0157c0577ce7524dcfc`.
- `tests/test_hr_step68h_BM_global_identity.py` — Git blob `4cdd3fce5b385e77894cac4e29e58386dbf1995b`.

Rapports bruts GitHub, **identiques aux octets créés localement** :
- `research/reports/gate2b-step68h-original-BM-identity.json`.
- `research/reports/gate2b-step68h-24-derivative-certificate.json`.

Commande réellement exécutée :

```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q \
 tests/test_hr_step68e_exact_shift_full_lapse_response.py \
 tests/test_hr_step68f_joint_profile.py \
 tests/test_hr_step68g_full_Cdot_Mprime_quotient.py \
 tests/test_hr_step68h_BM_global_identity.py
# RÉEL : 49 passed in 31.86s
```

Une première exécution dans l'ordre INVERSE des tests a atteint le délai d'exécution après avoir affiché les tests passants, et **n'est pas comptée comme succès** ; l'ordre reproduit ci-dessus est complet et confirmé. Les 8 tests spécifiques Step68h réussissent seuls en 18,94s.

## 4. Conséquence pour le verrou et tâches qui restent

Le coefficient \(\boxed{B_M=0}\) est **DÉSORMAIS DÉMONTRÉ EXACTEMENT** sur `Fz=Fz'=0` dans la charte régulière, au lieu de n'être qu'observé numériquement. Cela fait passer la partie `M'` de \(\dot C\) du statut « à réduire » au statut « éliminée analytiquement ».

Cela **NE DÉTERMINE PAS** les trois autres coefficients d'ordre inférieur :
\[
A_N,\quad B_N,\quad A_M,
\]
ni leur dépendance aux contraintes complètes `Hg,Hf,Ddiag,C,Hg',C'`, ni le rang du Dirac, le rapport des lapses global exact, les conditions aux bords, les chartes singulières `K=0,J=0`, l'absence du fantôme BD ou les prédictions 4D.

**Priorité scientifique Step68i :** réduire le vrai coefficient temporel \(B_N\) avec **les contraintes complètes et leurs prolongations** (le troisième jet est déjà supprimé par `Hg'` dans l'original Step60), puis prouver par intervalles sur la **trajectoire globale exacte Step55** les signes \(A_N>0\), \(A_M<0\) et la régularité de \(M/N=-A_N/A_M\), en conservant la liberté de jauge et les conditions aux bords. Construire enfin un oracle Poisson indépendant non-IBP sur six couples.

**VERDICT : B_M=0 démontré dans la charte stationnaire prolongée ; GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

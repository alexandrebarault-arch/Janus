# JANUS-005 — Seuil de signe de la variation extérieure de pf (2026-11-11)

**HEAD source :** `f56afe49936f6e37adb18e75cf72400905c5cabd`. **Portée :** conséquence algébrique conditionnelle, non calcul physique Step55/58.

Le code original `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs` (blob `7615cdb1624748dac56ab1d969c401b258f8cdaa`) fournit, à géométrie fixée, `dpf=H*dP+chi*dQ` et le certificat de borne simple `-21/25 < chi < -71/100` au rayon `R=17/20`, sous les hypothèses de sa fonction `physicalChiBounds`. Les bornes Step49/55 reprises dans `research/JANUS005_CONDITIONAL_OUTER_F_MOMENTUM_TRACE_TANGENT_BOUNDS_20261111.md` donnent `0.004920225<dP<0.004978025` et `0.0115071614336092885<dQ<0.011738073957404807`. Toutes ces bornes sont **conditionnelles** et leur validité simultanée pour une famille physique doit être démontrée; aucune n'a été recalculée sur l'ODE originale ici.

Comme `dP>0`, le seuil de changement de signe est exactement `T=-chi*dQ/dP`, avec `dpf=dP*(H-T)`. L'arithmétique rationnelle exacte donne les bornes strictes
```
96118642563089351/58565000000000000 < T < 4833324570696097/2411875000000000
```
soit environ `1.641... < T < 2.004...`. Par conséquent, sous les hypothèses simultanées, si `H <= 96118642563089351/58565000000000000`, alors `dpf<0`; si `H >= 4833324570696097/2411875000000000`, alors `dpf>0`. **Aucun de ces deux critères n'est actuellement établi pour le H physique.** L'intervalle intermédiaire ne détermine pas le signe.

**Contre-contrôle :** pour `H=2`, l'enclosure brute `2*dP+chi*dQ` traverse zéro : borne inférieure `-488303105500947/25000000000000000000`, borne supérieure `357193076427481033/200000000000000000000`. Cette indétermination d'intervalles ne prouve pas que le véritable `dpf` change de signe, car les variables sont corrélées. Elle interdit seulement d'affirmer un signe à partir des bornes indépendantes disponibles.

**Commande exécutée :** Python standard `fractions.Fraction` pour les produits/quotients rationnels et le test `H=0,2`; sortie ci-dessus, aucune erreur. Aucun test moteur Step55/58 rejoué, 0 cellule physique évaluée, 0 certifiée.

**NEXT_ACTION_EXACT :** évaluer/encloser `H` depuis la formule authentique `jacobian(p)` avec les paramètres physiques et leurs corrélations, en vérifiant le signe du dénominateur `den` et la provenance des données au HEAD fixé; puis calculer `dpf` et `dpSf` par arithmétique d'intervalles contrôlée. Vérifier les véritables conditions au bord avant d'inférer une obstruction. JANUS-001 reste bloqué sur la reconstruction des sources historiques pour le pilote.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**

# JANUS — d2d2b3b : contrainte conditionnelle Step58 / horloges relatives sur un sous-anneau certifié

28 octobre 2026. **Résultat exact sous hypothèses Step55/Step58 ; ni solution temporelle complète ni obstruction physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Source originale et hypothèses

L'opérateur `numerics/hr_step58_temporal_operator.py` (Git blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`) est une variation six couples et shift HR non gelé. Sa réduction aux coefficients d'ordre zéro `A_N,A_M` sur la coquille Step55 n'est valide pour l'équation `A_N N+A_M M=0` **que si** les coefficients de dérivées de lapses s'annulent effectivement sous les contraintes complètes. Le certificat authentique `0c688d6648e16064b1eb4e8ad9c55e7b44a95947` donne 225 feuilles jointives sur `r∈[1/64,1/32]`, `A_N>0,A_M<0`, et non un théorème sur les lapses globaux.

Sur chaque feuille, le quotient nécessaire `rho=M/N=-A_N/A_M` est encadré rationnellement par `N_low/(-M_low) < rho < N_high/(-M_high)`. Les 225 feuilles ont été contrôlées par entiers exacts. **154/225** certifient `rho<3/4`, en deux bandes fermées jointives chacune : `[1/64,225/14336]` (2 feuilles) et `[37/1792,1/32]` (152 feuilles). **71 feuilles restent INCOMPLETE pour cette borne de ratio** : cela ne prouve pas que `rho≥3/4` sur celles-ci.

## Nouvelle implication quantitative, sur ces deux bandes uniquement

Step55 fixe exactement `t'_g=(3/2500)r L_g>0`, `t'_f=-(1/625)r L_f<0`, `z=r/250>0`, avec `L_g=(2/5)(1+(3/2000)r²)²` et `L_f=(2/5)(5787707228025044/10^16)(1-(3/2500)r²)²`. Pour `r∈[1/64,1/32]`, l'arithmétique rationnelle donne `0<L_g<1/2`, `1/5<L_f<1/2`, `s_g≥1`, `s_f<1001/1000` et `0<t'_g-t'_f<7/160000`.

En imposant la condition de bord instantanée `dot(t_g-t_f)=0`, l'expression originale b3a donne, avec `rho=M/N` et `Q=N/L_g+M/L_f` :

`Vrel/N=[rho*s_f-s_g-z*(1/L_g+rho/L_f)*t'_g]/(t'_g-t'_f)`.

Dès que `0<rho<3/4`, le numérateur est strictement inférieur à `(3/4)(1001/1000)-1=-997/4000`. D'où, **sur les 154 feuilles seulement** :

\[
\boxed{V_{rel}/N<-39880/7<-5697,\qquad |L_f V_{rel}|/M>31904/21>1519.}
\]

Pour la métrique ADM f avec shift radial diagonal `V`, ceci entraîne `f_{tt}=-M²+L_f² V_{rel}²>0` : le vecteur de coordonnées `∂_t` n'est pas temporel pour f dans ce choix de jauge. **Ce n'est PAS une perte de signature lorentzienne, une instabilité ou une obstruction physique : un vecteur de coordonnées peut être spatial avec des tranches ADM régulières.**

## Centre et vrai verrou

Au centre régulier, `t'_g=t'_f=0`, donc `dot(t_g-t_f)(0)=N(0)-M(0)` pour `V` fini. La préservation d'une différence d'horloges constante au centre impose `M(0)=N(0)`. Si `N(0)>0`, une extension continue du rapport temporel `rho=M/N` doit tendre vers 1. **Aucun certificat Step58 du rapport au centre `r=0` n'est disponible ; les bandes extérieures ne réfutent pas cette limite.**

## Reproductibilité et limites

Sources GitHub lues : certificat temporel `0c688d6648e16064b1eb4e8ad9c55e7b44a95947`, opérateur original Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, géométrie Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, équations des horloges b3a `edf4dd6c8ab3fea9579195c130b096dee7b7353a`. Le script Node recalcule les blobs SHA-1 Git à partir des fichiers d'un clone complet ; ici l'audit a été exécuté avec BigInt V8 sur les octets JSON relus du connecteur et les SHA fournis par GitHub. **1147 assertions exactes PASS, 0 FAIL** ; quatre contrôles négatifs V8 ont rejeté les certificats altérés. Les modules physiques Python originaux et le CLI Node ne sont **pas** réexécutés dans cette session.

Aucune preuve de compatibilité globale `Vrel` / Step58 / bords, aucun générateur temporel amélioré différentiable, aucune réduction de jauge temporelle, aucun rang de Dirac complet, aucun résultat K=0/J=0, 4D, stabilité ou observables.

**Prochaine étape : d2d2b3c** — certifier le quotient temporel Step58 près de `r=0`, vérifier s'il tend vers 1, puis tester la régularité du shift `Vrel` et les charges du générateur temporel amélioré. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

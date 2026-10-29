# JANUS b3c3d6 — coquille primaire Step55 (résultat exact restreint, 2026-10-29)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Vérification algébrique indépendante par transcription des formules Step45 et Step55, **pas** le probe original Step58 complet.

## Résultat

Sur la géométrie prescrite Step55, avec $s=r^2$, $S_g=rL_g$, $S_f=rL_f$, $z=r z_1$, $p_{Lg}=sG_{\rm mom}$, $p_{Sg}=rP_{Sg}$, $p_g=s\rho_g$ et $t'_g=r k_gL_g$ :

- $p'_{Lg}=rG_{\rm prime}$, $D_g=r s D_{\rm bar}$, $K=s m^2 M_g^2 L_g L_f T$, et $D_{\rm bar}=m^2 M_g^2 L_g L_f T z_1/\sqrt{1-z^2}$, d'où **$F_z=D_g-Kz/\sqrt{1-z^2}=0$**.
- L'identité géométrique $-L_g-(S'_g)^2/L_g+2(S_gS'_g/L_g)'=-s L_g^3 R_g/2$ et la définition Step55 de $\rho_g$ impliquent **$H_g=A_g-(B_g)'=0$**, pour $r>0$, sans résoudre l'EDO de $p_{Lf}$.
- En combinant avec le certificat précédent issu du rejeu ORIGINAL Step58, $E_M|_{F_z=0}=0$ et $E_N|_{F_z=0}=(z^2-1)H_g/(L_gL_f)$, on obtient **$E_N=E_M=0$** sur cette coquille prescrite et régulière. Le raccord central est une question distincte.

À $R=17/20$, le facteur $(z^2-1)/(L_gL_f)$ est exactement $-9999884400000000000000000000000000000000/926432894764182404865494596893754186181$, compris entre $-11$ et $-10$. **Ce facteur n'est pas une valeur non nulle de $E_N$.**

## Reproductibilité

Code : `numerics/hr_b3c3d6_step55_primary_shell_audit.py`. Tests : `tests/test_hr_b3c3d6_step55_primary_shell_audit.py`. Rapport : `research/reports/gate2b-b3c3d6-step55-primary-shell.json`. **9 résidus exacts nuls, 2 contrôles négatifs, 4 unittest non indépendants PASS, 0 FAIL final.** Sources consultées sur GitHub : Step45 blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

**Limites :** transcription et tests non indépendants, pas de rejeu original Step58 ni Step55 dans cette session. L'audit ne certifie pas $H_f=0$, $C(r)=0$, $A_N,A_M,B_N,B_M$ sur la solution radiale exacte, les dérivées/zéros, lapses globaux positifs, les deux bords, la tangence/rang Dirac, charges/jauge, dynamique 4D, stabilité ou observables. $F_z=H_g=0$ n'est pas la coquille Dirac complète.

**Prochaine action b3c3d6 :** vrai probe original Step58 sur Step55 avec jets $p_{Lf}$ de l'EDO, les six coefficients et leurs dérivées, puis lapses positifs/deux bords et Dirac.

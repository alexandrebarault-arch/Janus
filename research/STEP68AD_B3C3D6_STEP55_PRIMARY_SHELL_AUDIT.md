# JANUS b3c3d6 — identité exacte de la coquille primaire Step55 (partielle, 2026-10-29)

**Statut : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Ceci est une vérification algébrique indépendante par transcription des formules originales Step45 et Step55, et NON le probe original Step58 complet.

## Résultat

Sur la géométrie prescrite Step55, avec (s=r^2), (S_g=rL_g), (S_f=rL_f), (z=r z_1), (p_{Lg}=sG_{m mom}), (p_{Sg}=rP_{Sg}), (p_g=s\rho_g), (t'_g=r k_gL_g), les définitions originales donnent exactement

- (p'_{Lg}=rG_{m prime}), (D_g=r s D_{\rm bar}), (K=s m^2 M_g^2 L_g L_f T), (D_{\rm bar}=m^2 M_g^2 L_g L_f T z_1/\sqrt{1-z^2}) ; donc **(F_z=D_g-Kz/\sqrt{1-z^2}=0)**.
- La combinaison de courbure (-L_g-(S'_g)^2/L_g+2(S_gS'_g/L_g)'=-s L_g^3 R_g/2). La définition Step55 de (\rho_g) annule alors **(H_g=A_g-(B_g)'=0)** identiquement, pour (r>0), sans résoudre l'EDO de (p_{Lf}).
- En combinant avec le certificat des hauts jets obtenu lors du rejeu original Step58 précédent, (E_M|_{F_z=0}=0) et (E_N|_{F_z=0}=(z^2-1)H_g/(L_gL_f)), on conclut **(E_N=E_M=0)** sur cette coquille prescrite, là où les dénominateurs sont réguliers. Au centre, le prolongement doit être traité séparément.

À (R=17/20), le seul facteur ((z^2-1)/(L_gL_f)) vaut exactement (-9999884400000000000000000000000000000000/926432894764182404865494596893754186181\in(-11,-10)). Ce facteur n'est PAS une valeur non nulle de (E_N).

## Reproductibilité et limites

Code : `numerics/hr_b3c3d6_step55_primary_shell_audit.py`. Tests : `tests/test_hr_b3c3d6_step55_primary_shell_audit.py`. Rapport : `research/reports/gate2b-b3c3d6-step55-primary-shell.json`. **9 résidus exacts nuls, 2 contrôles négatifs et 4 unittest non indépendants PASS**, zéro échec final. Les formules originales consultées sont identifiées par leurs Git blobs Step45 `66aa43841...`, Step55 `a6e70041...`, Step58 `802c23ae...` ; le code original Step58 n'a PAS été exécuté dans cette session.

**Non prouvé :** (H_f=0), (C(r)=0) par ce seul audit, les coefficients (A_N,A_M,B_N,B_M) sur l'EDO radiale exacte, leurs dérivées et zéros, les deux bords physiques, lapses strictement positifs, rang Dirac, charges/jauge, 4D/stabilité/observables. La coquille (F_z=H_g=0) ne doit jamais être assimilée à la coquille Dirac complète.

**Prochaine action b3c3d6 :** exécuter les six coefficients du véritable Step58 original sur Step55, y compris les jets (p_{Lf}) fournis par l'EDO, puis les conditions aux deux bords et la tangence Dirac.

# JANUS — 68ad-C2d2e5a : obstruction de différentiabilité aux bords (audit exact non-IBP)

Date : 26 octobre 2026. Branche : \`research/gate2b-nonhomothetic-transfer\`.
**GATE_2B OPEN — JANUS_R NOT_VALIDATED.** Étape partielle de C2d2e5 ; aucun rang complet de Dirac calculé.

## Sources physiques originales authentifiées

- \`numerics/hr_step37_original_nonibp_oracle.py\` : Git blob \`005449ade6e3582e3b9a5c3374a881a77e73e3f6\` (courbure sphérique non intégrée, terme \`-z pLg'\`).
- \`numerics/hr_spherical_mixed_hamiltonian_bracket.py\` : \`6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81\` (densités IBP et exigence de fonctions test nulles aux deux bords).
- \`numerics/hr_spherical_adm_primary.py\` : \`c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41\` (action ADM originale, deux poussières).
Les trois fichiers ont été relus en direct via le connecteur GitHub ; leurs empreintes blobs proviennent de ce même connecteur. Leurs moteurs Python ne sont PAS réexécutés ici.

## Identité fonctionnelle exacte et portée

Posons \(N=N_g\), \(M=N_f\), \(P=p_{L_g}\), \(W_a=S_a'/L_a\) et \(z\) un shift fixé, régulier. Pour les termes de courbure EH et le terme gravitationnel \(p_{L_g}'\) des deux densités hamiltoniennes originales (tous les autres termes identiques s'annulent dans la différence original–IBP), l'identité de dérivation donne, sans supposer les contraintes :

\[
 {\cal L}_{\rm original}-{\cal L}_{\rm IBP}=\partial_r {\cal B},
\quad
 {\cal B}=
 2M_g^2 N {S_gS_g'\over L_g}
 +2M_f^2 M {S_fS_f'\over L_f}
 -zP\left(N+M{L_g\over L_f}\right).
\]

La vérification analytique est immédiate avec
\(-M_a^2 L_a S_a^2 R_a/2=-M_a^2 L_a+M_a^2 S_a'^2/L_a+2M_a^2 S_a(S_a'/L_a)'\)
et \(-uP'=(u'P)-(uP)'\) où \(u=z(N+ML_g/L_f)\).

Pour des lapses compacts, \({\cal B}\) s'annule aux bords. Pour des lapses non nuls, on NE peut PAS reprendre la formule IBP en oubliant \([{\cal B}]_a^b\). Le contre-exemple rationnel hors coquille \(L_g=1,L_f=2,S_g=r,S_f=2r,P=-r^2,z=r/4,N=M=1,M_g^2=M_f^2=1\) sur \([1/2,1]\) donne exactement
\({\cal B}(1/2)=195/64\), \({\cal B}(1)=51/8\), \([{\cal B}]_{1/2}^{1}=213/64\ne0\).
**Ceci est un contre-exemple à la suppression universelle du bord, PAS un contre-exemple à JANUS sur coquille.**

## Variation directe au bord de l'action originale

À shift fixé, les coefficients de \(\delta S_g'\), \(\delta S_f'\) et \(\delta p_{L_g}\) dans la variation au bord sont respectivement
\(2M_g^2 NS_g/L_g\), \(2M_f^2 MS_f/L_f\), \(-z(N+ML_g/L_f)\).
Pour les poussières canoniques indépendantes, les coefficients de \(\delta\theta_g\), \(\delta\theta_f\) sont
\[
p_g\left[{N\theta_g'\over L_g^2\sqrt{1+\theta_g'^2/L_g^2}}
 +z\left({N\over L_g}+{M\over L_f}\right)\right],
\qquad
 {Mp_f\theta_f'\over L_f^2\sqrt{1+\theta_f'^2/L_f^2}}.
\]
Les termes en \(\delta S_a\), \(\delta L_a\) et les contributions supplémentaires liées à la variation de \(z_*\) doivent aussi être traités avant une conclusion sur la forme symplectique de bord complète. Pour \(N>0,M>0,S_a>0,L_a>0,M_a^2>0\), les coefficients \(\delta S_a'\) sont strictement positifs à un bord externe régulier. Il faut donc fixer les variations appropriées ou construire les contretermes adéquats pour avoir une fonctionnelle différentiable.

**Important :** ces flux sont calculés à shift fixé avant réduction par \(F_z=0\). Ils ne prouvent pas une obstruction physique irréparable : des conditions de Dirichlet, des contretermes ou une réduction cohérente peuvent les supprimer. Les résultats de rang local Step58 et les enclosures restent inchangés.

## Tests, provenance et limites

Le vérificateur \`scripts/hr_step68ad_c2d2e5a_original_boundary.cjs\` et son test \`tests/test_hr_step68ad_c2d2e5a_original_boundary.cjs\` utilisent des fractions \`BigInt\` exactes, évaluent les courbures originales non-IBP, les densités IBP et leurs dérivées de bord sur des champs polynomiaux indépendants, y compris les six couples déclarés. **27 assertions PASS, 0 FAIL** dans V8 ; aucune exécution de Node dans un clone, aucun moteur Python original rejoué. Les variations génériques des poussières avec gradients non nuls ne sont pas numériquement certifiées dans ce test rationnel, mais leurs expressions découlent de la dérivation directe des racines de poussière originales. Les identités fonctionnelles sont exactes pour les termes isolés ; les évaluations rationnelles sont des contrôles indépendants, non des preuves de fermeture de Dirac.

**Étape suivante : 68ad-C2d2e5b.** Définir et authentifier les conditions aux bords du profil Step55/68o, construire l'oracle de Poisson non-IBP complet à six couples en incluant la variation de \(z_*\) et les contretermes, puis tester le rang et les contraintes tertiaires sur coquille. Analyser séparément \(K=0,J=0\). 4D, stabilité et observables restent ouverts.

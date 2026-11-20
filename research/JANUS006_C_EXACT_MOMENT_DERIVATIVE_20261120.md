# JANUS-006 — dérivée explicite du mineur 4×4 (2026-11-20)

## Provenance et méthode
HEAD de départ `b2899794282708587f8f94175d81712e98df830d`; source consultée via connecteur GitHub : `numerics/hr_step45_exact_physical_ward.py`, blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Reconstruction locale manuelle des expressions algébriques `Ag,Bg,Af_full,Bf`, du calcul Euler et de `C_exact=K00-d_r K01`, puis calcul avec SymPy 1.14.0. **Le fichier local est une transcription, non un transfert octet-pour-octet authentifié : son SHA Git n'est pas présenté comme identique.** La conclusion est donc un résultat symbolique reproductible sous concordance de ces expressions avec la source GitHub, et non un certificat du runner original.

Commande locale : `cd /mnt/data/janus && PYTHONPATH=. python -m numerics.hr_step45_exact_physical_ward`. Résultat :

```text
m2*(2*Lf*Sf*Sg*beta3 + 2*Lf*Sg**2*beta2 - Lg*Sf**2*beta3*sqrt(1 - z**2) + Lg*Sg**2*beta1*sqrt(1 - z**2))/(2*Sg**2)
```

Ainsi, sur Sg≠0, |z|<1,

\[\partial_{p_{Lg}}C_{exact}=\frac{m^2}{2S_g^2}\left[2L_f S_g(S_f\beta_3+S_g\beta_2)+L_g\sqrt{1-z^2}(S_g^2\beta_1-S_f^2\beta_3)\right].\]

Contrôle indépendant : dériver `K00` et `K01` séparément par rapport à `pLg`, commuter avec la dérivée radiale totale, puis soustraire la dérivée de `C_exact` : résidu SymPy exactement 0. La dérivée est indépendante de `pLg` (seconde dérivée exactement 0). Contrôles de strates : pour beta1=beta2=beta3=0, dérivée nulle ; pour beta1=1, beta2=beta3=0 et Lg=Lf=Sg=Sf=1,z=0, dérivée =m2/2. **Ce sont des affectations algébriques, pas des solutions physiques aux contraintes.**

En combinant avec le jalon antérieur :

\[\det J_{(H_g,H_f,F_z,C_{exact})/(S_g'',S_f'',p'_{Lg},p_{Lg})}=-\frac{4M_g^2M_f^2S_gS_f}{L_f}\partial_{p_{Lg}}C_{exact}.\]

Le mineur est non nul sur les sous-domaines réguliers où le crochet ci-dessus est non nul, mais s'annule sur son hypersurface zéro. **Rang 4 générique de ce mineur dans l'espace ambiant, non rang Dirac sur contraintes, non admissibilité holonome et non validation de JANUS.** La condition de surface des contraintes n'a pas été vérifiée pour les affectations tests ; il faut examiner si cette hypersurface rencontre `Hg=Hf=Fz=C_exact=0`, les deux vrais bords et les conditions de lapses.

Tests moteur b3c3d9 SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

NEXT_ACTION_EXACT : (1) transférer et authentifier octet-pour-octet le Step45 original et rejouer `python -c "from numerics.hr_step45_exact_physical_ward import exact_physical_ward; import sympy as s; p=exact_physical_ward(); print(s.factor(s.diff(p['C_exact'],p['q'][1])))"`; (2) résoudre/échantillonner contradictoirement le système complet sur la strate où le crochet s'annule, sans confondre rang d'un mineur et rang complet ; (3) reconstruire les imports historiques JANUS-001, neuf tests puis pilote physique.

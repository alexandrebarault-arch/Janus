# b3c3d6 — défaut de transport holonome des jets cubiques (30 octobre 2026)

**Statut : correction d'un candidat numérique, PAS de preuve physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Défaut réel du candidat

Dans `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py`, `fields_at(t)` utilisait `pLfr=t*G(t²,U_c(t²))` tout en construisant `pLf=t² U_c(t²)` à partir du polynôme cubique de Taylor de la solution Step55. Ces deux fonctions sont égales sur la vraie solution ODE, mais **pas** sur l'extension cubique hors du point de base. L'égalité de leurs jets n'est assurée que jusqu'à l'ordre radial 2, pas 3. Le candidat passe les deux expressions à la construction de `pf` et `pSf`, puis différencie ces champs trois fois pour Step58.

Pour `2s U_s=G(s,U)-2U`, `s=r²`, `s_*=r_*²>0`, `U_c` le Taylor cubique exact au point et `U` de classe C⁴ :
`D(r)=rG(r²,U_c(r²)) - d[r²U_c(r²)]/dr` satisfait `D(r_*)=D'(r_*)=D''(r_*)=0` et **`D'''(r_*)=+16 r_*^6 U_{ssss}(s_*)`**. Le signe est celui de `rG - pLf'`, inverse du défaut défini précédemment comme `pLf'-rG`.

Avec `fac=pLf/(2 Mf² (r Lf) Sfr)`, `beta=sqrt(1+tfr²/Lf²)`, `denom=beta+fac*tfr`, les dépendances exactes du candidat sont `∂pf/∂pLfr=fac*Lf/denom` et `∂pSf/∂pLfr=Lf*beta/(Sfr*denom)`. Par conséquent, si les autres champs sont fixés, le défaut de troisième jet induit est respectivement `16 r_*^6 U_{ssss} fac*Lf/denom` et `16 r_*^6 U_{ssss} Lf*beta/(Sfr*denom)`. Ces expressions sont **conditionnelles** à la régularité et à `denom*Sfr != 0` ; elles ne prouvent pas que les six coefficients physiques Step58 changent.

## Correction

`fields_at(t)` calcule désormais `U_{c,s}=U_s+U_{ss}(s-s_*)+U_{sss}(s-s_*)²/2`, puis `pLfr=t*(2U_c+2s U_{c,s})`. C'est l'unique dérivée holonome du même polynôme utilisé pour `pLf`, à tous les points. Le calcul original `G(s_*,U_*)` reste utilisé pour les jets ODE au point.

## Contrôle reproductible réellement exécuté

`python -m unittest discover -s /mnt/data/janus_holonomic/tests -v` : **6 tests SymPy PASS, 0 FAIL**, et `python -m compileall -q /mnt/data/janus_holonomic/tests` PASS. Jouet exact `U=s⁴`, `G=2U+8s⁴`, `r_*=1/2` : `D'''=6` ; défauts propagés vers `pf'''` et `pSf'''` contrôlés avec coefficients rationnels variables ; témoin négatif hors point. Tests non indépendants, sans import des cinq originaux ni exécution du candidat complet. Les valeurs Step58 A/B/E précédentes ne sont pas certifiées.

## Suite obligatoire

Matérialiser cinq sources originales SHA-authentifiées, exécuter candidat corrigé et référence affine aux rayons `1/4,1/2,7/10,17/20`, comparer les six coefficients et la convergence ODE, vérifier factorisation/enclosures et lapses positifs avec deux vrais bords, puis Dirac/4D/stabilité/observables. Aucun no-go ou go JANUS déduit.

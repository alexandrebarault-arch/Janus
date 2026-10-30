# b3c3d6 — erratum : le probe affine historique conserve déjà le premier jet ODE (30/10/2026)

**Résultat exact conditionnel au contrat des sources inspectées ; PAS de rejeu numérique physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources originales inspectées via GitHub

Step45 blob 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; Step58 blob 802c23aebd41780d8c462f1aa1711707fe4ee88f ; probe affine historique numerics/hr_b3c3d6_full_original_step58_point_probe.py blob 643d90183367e74a28ed453d93f5489074b75b08 ; candidat cubique numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py blob 43a140cacfca81aaf41073facea3da4e47e64f5e. L'audit structurel précédent numerics/hr_b3c3d6_original_step58_minimum_jet.py blob 8d81fc1bc7823774e6304e25a52653d32e36c4ee a vérifié sur l'opérateur ORIGINAL que seuls les jets 0/1 des champs dépendant de U (pLf,pSf,pf) entrent dans les six coefficients ; seul A_M contient pSf'.

## Théorème exact de comparaison des prolongements réellement programmés

Poser s=r², s0=r0²>0, 2s U_s=G(s,U)-2U, u1=U_s(s0), u2=[G_s+(G_U-4)u1]/(2s0). Le probe appelé « affine » utilise Ua(s)=u0+u1(s-s0) pour pLf=s Ua, MAIS pLfr_mixed=r G(s,Ua) dans les champs pf,pSf, plutôt que la dérivée holonome de pLf hors point. Le quadratique Uq=Ua+u2(s-s0)²/2 et le cubique ont la dérivée holonome pLfr=d(r²U)/dr.

Au rayon r0, les valeurs et les premières dérivées radiales de pLf et de pLfr_mixed coïncident EXACTEMENT avec celles du quadratique/cubique. En revanche, la dérivée seconde holonome de pLf_affine diffère de celle du quadratique de -4r0⁴u2. Un affine rendu strictement holonome aurait pLfr'_affine - pLfr'_quadratique = -4r0⁴u2. L'extension historique, non holonome hors point, a déjà incorporé la courbure ODE dans le jet de pLfr=rG.

Les expressions originales de pf et pSf sont algébriques et lisses en (r,pLf,pLfr) dans la carte positive. Leur valeur et leur première dérivée radiale coïncident donc pour les deux extensions. Tous les autres champs sont prescrits indépendamment de U. **Conséquence structurelle : les six coefficients ponctuels du vrai Step58 sont identiques entre le probe affine historique mixte et les prolongements quadratique/cubique holonomes**, si l'on fixe la même solution, le même rayon et les mêmes conventions numériques. Ce n'est pas une identité globale des champs hors point.

**Rectification explicite :** la sensibilité exacte non nulle de A_M à U_ss trouvée auparavant reste correcte pour une comparaison de prolongements TOUS holonomes ; elle ne prédit PAS un écart A_M entre l'ancien probe affine mixte et le nouveau cubique. Une divergence numérique entre eux serait un signal d'incohérence de calcul/abscisse/jet/substitution à auditer.

## Tests et limites

10 unittest SymPy rationnels locaux PASS, 0 FAIL ; compileall PASS. Contrôles : quatre identités de jets, défaut non holonome non nul sur témoin rationnel, propagation dans deux cartes rationnelles non linéaires type pf/pSf. Tests non indépendants ; aucun original Step45/46/55/58, solveur DOP853 ou coefficient physique exécuté dans cette session. Les blobs cités ont été LUS via le connecteur ; pas de certification d'enclosure ou de BVP.

**Prochaine étape :** cinq originaux SHA-authentifiés, deux probes aux quatre rayons 1/4, 1/2, 7/10, 17/20 avec transport binary64 contrôlé, vérifier l'égalité attendue des six coefficients, et ajouter comme contrôle négatif un affine réellement holonome pour isoler A_M. Ensuite résidu DOP853 continu, enclosures physiques A/B/E, BVP positif deux vrais bords, Dirac six couples, dynamique 4D, stabilité, observables. Aucun JANUS validé.

# JANUS — b3c3d7 : critère continu conditionnel sur l'anneau et contre-exemple analytique (02/11/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Résultat mathématique exact conditionnel et contre-modèle non physique. Aucun nouveau certificat continu des vrais coefficients physiques Step58.

## Provenance

HEAD de main lu à l'entrée : f016fbcb0958ee06129c2235c12fee1067eb4c02. Les quatre boîtes originales sont reprises du rapport Git blob c502b9779056e8a493c43d330696515a661128c4 ; la lecture GitHub des sources Step45 et Step58 confirme les blobs 66aa43841dccfe4a5d586a49be9c10af3a67a10e et 802c23aebd41780d8c462f1aa1711707fe4ee88f. L'archive spatiale Step55 est e74057dcf741bcdb655c7d9be48c6a9650d7ff3f. Ces sources et les quatre boîtes ont été authentifiées ou lues, mais les moteurs physiques originaux et la barrière 256 cellules n'ont PAS été réexécutés.

## Théorème exact, avec hypothèses supplémentaires NON CERTIFIÉES physiquement

Sur r entre 1/4 et 17/20, poser s=r², a(s)=A_N(sqrt(s))/s et q(s)=-A_M(sqrt(s))/s. Supposer a,q de classe C1 et des bornes globales sur tout s entre 1/16 et 289/400 : |a'(s)| <= L_N et |q'(s)| <= L_M. Les quatre boîtes physiques archivées impliquent des marges strictes a(s_i)>l_i>0 et q(s_i)>h_i>0.

Sur chaque intervalle [s_i,s_(i+1)], le théorème des accroissements finis donne a(s)>l_i-L_N(s-s_i) et a(s)>l_(i+1)-L_N(s_(i+1)-s). Le maximum est supérieur ou égal à la moyenne, d'où une borne uniforme stricte (l_i+l_(i+1)-L_N*delta_s)/2. Même démonstration pour q.

Les seuils suffisants exacts, minimisés sur les trois intervalles, sont :

- L_N < 4123900/147, soit environ 28053,7415 ;
- L_M < 378550/7, soit environ 54078,5714.

**Si ces hypothèses étaient certifiées pour les coefficients physiques**, alors A_N>0, A_M<0, et rho=-A_N/A_M>0 continûment sur cet anneau. Ce sont des seuils critiques infimaux au vu des seules bornes aux deux extrémités et d'une hypothèse Lipschitz ; une fonction en V peut atteindre zéro en limite au seuil. Ce n'est PAS une preuve que les dérivées physiques satisfont les seuils.

Exemple purement conditionnel : si L_N<=1000 et L_M<=1000 sur tout l'anneau, les cônes rationnels donnent
181641335/392415471 < rho(s) < 5897045/10163981
pour tout s dans [1/16,289/400]. Ces bornes ne sont PAS des enclosures physiques démontrées.

## Contre-exemple pair analytique, NON PHYSIQUE

Le modèle synthétique positif déjà publié a a_good(s)=3500-175s et m_good(s)=-6750+375s, A_N=s*a_good et A_M=s*m_good. Il admet N=1, M=-a_good/m_good>0 sur [0,17/20]. Poser P(s)=produit des quatre (s-s_i), avec s_i=1/16,1/4,49/100,289/400. Définir
m_bad(s)=m_good(s)+C*s²*P(s), C=-2130706432000000/10929009.

On vérifie EXACTEMENT m_bad(s_i)=m_good(s_i) aux quatre rayons, ainsi que m_bad(0)=-6750 et m_bad'(0)=375. Le rapport central régulier reste 14/27, et son premier jet en s est inchangé. Pourtant m_bad(9/64)=0 à r=3/8 et a_good(9/64)>0 : l'équation A_N*N+A_M*M=0 impose alors N=0. Aucun couple strictement positif ne peut résoudre cette seule équation pour le modèle bad. Les deux modèles partagent donc exactement les huit valeurs ponctuelles et les deux premiers coefficients centraux mais ont des comportements continus incompatibles. Cela démontre la non-identifiabilité à partir des seules données publiées, **PAS un zéro réel de A_M sur la branche physique**.

Le théorème des accroissements finis impose sup|m_bad'| >= 86100 entre s=1/16 et 9/64, au-delà du seuil 378550/7. Les contrôles sont entièrement rationnels.

## Reproduction, limites et suite

Fichiers : numerics/hr_b3c3d7_annular_lipschitz_sign_gate.py ; tests/test_hr_b3c3d7_annular_lipschitz_sign_gate.py ; research/reports/gate2b-b3c3d7-annular-lipschitz-sign-gate.json. Tests locaux réellement exécutés sur ces octets : 11 PASS, 0 FAIL, 0 SKIP, avec contrôle de mutation du blob source ; module Python exécuté PASS ; compileall PASS. Les deux blobs code/test sont respectivement e281e230ce3a0e14a7865c62edbba89386aab282 et 748b2fdffd7b3f123303b5ae7268de207a508db6.

Prochaine étape : obtenir sur le vrai Step55/58 les bornes globales de d(A_N/r²)/ds et d(-A_M/r²)/ds avec jets holonomes et tubes corrélés, en subdivisant les cellules si nécessaire. Puis traiter le centre 0<=r<=1/4, les zéros possibles de A_M, les deux vrais bords temporels, le système Dirac/charges/jauge, la dynamique 4D, la stabilité et les observables. Aucune conclusion générale JANUS.

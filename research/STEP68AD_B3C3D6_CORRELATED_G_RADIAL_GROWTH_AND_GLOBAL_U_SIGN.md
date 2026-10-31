# JANUS b3c3d6 — audit rationnel corrélé Step55 (31 octobre 2026)

GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

À partir de la barrière physique Step55 déjà certifiée, |U-Ustar|<=1/10000 sur 0<=s<=289/400, et des constantes originales, le calcul par fractions donne -67/12500 < U(s) < -229/50000 sur cet intervalle. Donc pLf(r)=r²U(r²)<0 pour 0<r<=17/20, sans singularité de division par U sur cet anneau ouvert (mais U(0) fini et pLf(0)=0).

Aux seuls rayons r=1/4,1/2,7/10,17/20, les boîtes physiques Step55 déjà publiées et authentifiées (blob e74057dcf741bcdb655c7d9be48c6a9650d7ff3f) donnent par règle de chaîne totale d_s G(s,U(s))=G_s+G_U(G-2U)/(2s)>1/2000. Par conséquent d_r G=2r d_s G>0 et pLf_rr-pLf_r/r=2s d_s G>0 en ces quatre points. À r=1/4, U_s n'a pas de signe certifié, mais le total d_s G reste positif ; la soustraction naïve des boîtes indépendantes pLf_rr et G ne certifie pas ce signe. Aucun prolongement de d_r G>0 entre ces points n'est revendiqué.

Ce transfert dépend des enclosures physiques antérieures, sans nouveau rejeu des moteurs Step45/46/55/58 ni DOP853. Les six coefficients A/B/E Step58, leur factorisation, les lapses positifs aux deux vrais bords, Dirac, 4D, stabilité et observables restent NON CERTIFIÉS. La prochaine étape reste le calcul des six enclosures originales Step58 aux quatre rayons, puis le BVP global.

Contrôle local exécuté : 7 unittest PASS, compileall PASS ; sources originales non rejouées. SHA des octets du nouveau candidat local : e0391b8b5611de21016e51ca7dcabb6f1fdae041 ; tests : 8bd2a493f5b2f397dc674abd9bfda3979476fa4b. Les fichiers candidats ne sont pas encore publiés sur GitHub.


## Certificat exécutable et provenance (audit final)

Le code a été **ajouté au module déjà authentifié** `numerics/hr_b3c3d6_step58_plf_input_certificate.py`, fonction `certify_correlated_growth()`, afin de préserver les fonctions précédentes et d'éviter toute modification des sources physiques originales. **Git blob du fichier complet testé** : `7655039bcfb9878262f8d63051f53f17836619a7`. Les cinq nouveaux tests ont été ajoutés à `tests/test_hr_b3c3d6_step58_plf_input_certificate.py` : **Git blob complet testé** `32f5b11cbab16fd31b0a02de2fa89e9efca38d2f`. Les anciens tests restent présents : **7 unittest PASS au total, 0 FAIL, 0 SKIP**, `python -m compileall -q numerics tests` PASS.

**Commande :** `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_plf_input_certificate.py' -v`. Le module utilise l'archive physique Step55 (SHA `e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`) et le vérificateur antérieur (SHA `801ca6c384d1b12f8443e5b8624f416f6954c618`), tous deux égaux aux octets locaux effectivement testés. La borne globale provient du **tube global Step55 certifié précédemment**, et non des quatre seules boîtes ponctuelles.

**Boîtes rationnelles de d_s G :** le code renvoie les fractions exactes pour chaque rayon. Valeurs décimales d'affichage seulement : r=1/4 [0,0006497615 ; 0,005652949], r=1/2 [0,002426296 ; 0,003830755], r=7/10 [0,002690099 ; 0,003508820], r=17/20 [0,002759431 ; 0,003383107]. La borne stricte commune certifiée est `d_s G > 1/2000`. À r=1/4, `U_s` traverse zéro, et la soustraction de boîtes indépendantes `pLf_rr-G` traverse zéro : **la corrélation de l'identité ODE est essentielle**.

**Attention :** `G_s` est la dérivée partielle composée de la géométrie prescrite (pas la dérivée de G à géométrie gelée). Aucun signe continu de `d_r G` entre les quatre points n'est démontré. La stricte négativité de U est **globale** sur l'intervalle indiqué uniquement sous la barrière physique Step55 déjà certifiée. Aucune nouvelle certification des six coefficients Step58 ni du BVP de lapses n'est revendiquée.

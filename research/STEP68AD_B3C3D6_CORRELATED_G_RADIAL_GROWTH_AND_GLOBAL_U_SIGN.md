# JANUS b3c3d6 — audit rationnel corrélé Step55 (31 octobre 2026)

GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

À partir de la barrière physique Step55 déjà certifiée, |U-Ustar|<=1/10000 sur 0<=s<=289/400, et des constantes originales, le calcul par fractions donne -67/12500 < U(s) < -229/50000 sur cet intervalle. Donc pLf(r)=r²U(r²)<0 pour 0<r<=17/20, sans singularité de division par U sur cet anneau ouvert (mais U(0) fini et pLf(0)=0).

Aux seuls rayons r=1/4,1/2,7/10,17/20, les boîtes physiques Step55 déjà publiées et authentifiées (blob e74057dcf741bcdb655c7d9be48c6a9650d7ff3f) donnent par règle de chaîne totale d_s G(s,U(s))=G_s+G_U(G-2U)/(2s)>1/2000. Par conséquent d_r G=2r d_s G>0 et pLf_rr-pLf_r/r=2s d_s G>0 en ces quatre points. À r=1/4, U_s n'a pas de signe certifié, mais le total d_s G reste positif ; la soustraction naïve des boîtes indépendantes pLf_rr et G ne certifie pas ce signe. Aucun prolongement de d_r G>0 entre ces points n'est revendiqué.

Ce transfert dépend des enclosures physiques antérieures, sans nouveau rejeu des moteurs Step45/46/55/58 ni DOP853. Les six coefficients A/B/E Step58, leur factorisation, les lapses positifs aux deux vrais bords, Dirac, 4D, stabilité et observables restent NON CERTIFIÉS. La prochaine étape reste le calcul des six enclosures originales Step58 aux quatre rayons, puis le BVP global.

Contrôle local exécuté : 7 unittest PASS, compileall PASS ; sources originales non rejouées. SHA des octets du nouveau candidat local : e0391b8b5611de21016e51ca7dcabb6f1fdae041 ; tests : 8bd2a493f5b2f397dc674abd9bfda3979476fa4b. Les fichiers candidats ne sont pas encore publiés sur GitHub.

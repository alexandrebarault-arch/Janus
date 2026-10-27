# JANUS — 68ad-C2d2e5b3b2c2b2d2d2a : noyau de jauge des variations tangentes de bord

27 octobre 2026. **Résultat structurel exact, NON une résolution du problème de Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Question et résultat

Le critère proposé « construire deux directions canoniques indépendantes tangentes aux contraintes » est **insuffisant** pour tester une obstruction de bord : deux directions de jauge peuvent satisfaire ce critère tout en ayant toutes leurs traces de bord nulles. Pour le prouver, introduire x=r/R dans [0,1] et deux champs de déplacement radial `eta_1=x^4(1-x)^4`, `eta_2=x*eta_1`. Ils sont linéairement indépendants (leur rapport vaut x là où eta_1 est non nul) et leurs jets jusqu'à l'ordre trois s'annulent aux deux extrémités. Ces polynômes sont **plats au bord jusqu'à l'ordre trois, mais ne sont pas à support compact dans l'intervalle ouvert** ; les multiplier par une coupure C∞ supportée strictement à l'intérieur donne de véritables générateurs à support compact, sans changer l'argument local.

Sur les six couples `(Lg,pLg),(Sg,pSg),(tg,pg),(Lf,pLf),(Sf,pSf),(tf,pf)`, les poids radiaux des coordonnées sont `(1,0,0,1,0,0)` dans cet ordre, et ceux des moments sont complémentaires. La transformation canonique infinitésimale est `delta_eta X=eta X'+w_X eta' X`. Elle est engendrée par la contrainte diagonale `D[eta]=int eta*(pSg*Sg'-Lg*pLg'+pg*tg'+pSf*Sf'-Lf*pLf'+pf*tf') dr` (à termes de bord nuls). Les identités polynomiales exactes donnent `delta Dg=eta Dg'+2 eta' Dg`, idem pour `Df`, et `delta K=eta K'+2 eta' K`, avec `K=m² Mg² Lg Lf*(beta1 Sg²+2 beta2 Sg Sf+beta3 Sf²)`. Sur K>0, `z*=Dg/sqrt(K²+Dg²)` est donc un scalaire radial.

Pour chacun des 12 champs canoniques, `delta X`, `delta X'` et `delta X''` s'annulent aux deux frontières. La forme de bord originale non-IBP d2a, qui ne dépend que de ces traces (et de leurs coefficients de fond), s'annule sur les deux directions. Sa courbure tirée en arrière sur leur plan est également nulle. **Cela ne fournit aucune information sur la courbure de bord dans les directions physiques non-jauge.**

## Portée et précautions

La covariance de la théorie implique qu'une transformation diagonale à support intérieur transporte les solutions des contraintes primaires et de la secondaire fonctionnelle vers d'autres solutions, sous les hypothèses de régularité et de différentiabilité des générateurs. La préservation temporelle est également transportée **si** les lapses et shifts sont transformés conformément à leur nature géométrique et si une solution complète existe. Nous n'avons ni construit une telle solution temporelle Step55 ni évalué la véritable matrice de Dirac ; la tangence complète est donc **conditionnelle**, pas certifiée physiquement. La preuve de covariance de la secondaire n'est pas réexécutée symboliquement ici : les tests vérifient exactement les lois canoniques, Dg/Df/K et le noyau de bord, non les opérateurs Step58/60.

Ce résultat impose une correction méthodologique : rechercher au moins **deux directions canoniques à traces de bord indépendantes modulo les diffeomorphismes diagonaux**, tangentes aux contraintes fonctionnelles et temporelles, plutôt que simplement deux directions indépendantes sur l'espace des champs. À défaut, le pullback nul de dTheta est une tautologie de jauge.

## Sources et reproductibilité

SHA des sources originales relues via le connecteur GitHub : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Ward radial `89e7f6eab35d28317f2f7a4330601736525487e5`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, rapport Step55/d2d1 `1ba6d012133a92b69a8c91498d065b22649afbe0`. Moteurs originaux non réexécutés. Le programme `scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2a_gauge_tangent_kernel.cjs` effectue **211 assertions exactes BigInt**, 0 échec, sur des profils polynomiaux **témoins algébriques non physiques**. Le wrapper Node contient quatre gardes de rejeu, sans validation indépendante. Le certificat JSON consigne explicitement les limites.

## Suite prioritaire

Construire une deuxième direction canonique **non-jauge** avec traces de bord indépendantes sur la famille Step55, en résolvant la linéarisation complète des primaires et de C(r)=0, puis la préservation temporelle et les conditions de bord. Tester le rang du morphisme des traces modulo jauge avant d'évaluer dTheta. Ensuite oracle original non-IBP six couples, rang Dirac, tertiaires, lapses, K=0/J=0, dynamique 4D, stabilité et observables. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

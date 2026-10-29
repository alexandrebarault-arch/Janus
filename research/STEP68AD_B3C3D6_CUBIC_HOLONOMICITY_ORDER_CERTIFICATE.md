# b3c3d6 — Certificat exact d'ordre du jet cubique Step55 (29/10/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED. Résultat formel local, pas un rejeu original Step58.**

Le checkpoint précédent a identifié le défaut du prolongement affine de U(s), avec s=r², et publié un candidat cubique. Cette vérification indépendante précise **jusqu'à quel ordre le prolongement cubique est réellement holonomique**. Les sources de référence Step58 et du candidat ont été relues sur GitHub (blobs `802c23aebd41780d8c462f1aa1711707fe4ee88f` et `9eb5167bec74fc427307a262faaa6a1f785785a8`). Les cinq moteurs originaux n'ont pas été exécutés pendant cette session.

Pour l'EDO Step55 `2s U_s=G(s,U)-2U`, à `s0=r0²>0`, le jet cubique `U_c(s)=U0+U1 h+U2 h²/2+U3 h³/6`, `h=s-s0`, où U1,U2,U3 sont dérivés exactement de l'EDO, vérifie :

- `H(s)=2U_c+2s U_c' -G(s,U_c)` : coefficients de h^0,h^1,h^2 **exactement nuls**.
- Le coefficient de h³ est `[h³]H=-s0 U4/3`, où le jet quatrième de la **vraie solution**, seulement formel ici, vaut
  `U4=[G_sss+3G_ssU U1+3G_sUU U1²+G_UUU U1³+3G_sU U2+3G_UU U1 U2+(G_U-8)U3]/(2s0)`.
- Si `D(r)=d(r²U_c(r²))/dr-rG(r²,U_c(r²))`, alors `D(r0)=D'(r0)=D''(r0)=0` mais **`D'''(r0)=-16r0^6 U4`**. La coïncidence des jets jusqu'au troisième ordre de `pLf` ne doit donc jamais être étendue automatiquement à son quatrième jet.

**Témoin analytique non physique, véritable solution d'une EDO du même type** : `U(s)=1/3+(2/5)s-(1/7)s²+(3/11)s³+(1/13)s⁴`, `G(s,U)=2U+2s[(2/5)-(2/7)s+(9/11)s²+(4/13)s³]`. À `r0=1/2`, `U4=24/13` et `D'''=-6/13≠0`, alors que D,D',D'' s'annulent. Ce témoin prouve la possibilité d'un défaut au quatrième jet, **pas** son existence sur le profil physique Step55.

**Tests réellement exécutés localement** : `cd /mnt/data/janus_preflight && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 unittest PASS, 0 FAIL** (non indépendants), 5 identités algébriques exactes, un témoin analytique exact ; `python -m compileall -q numerics tests` PASS. Une erreur intermédiaire de normalisation `s0=r0²` a été corrigée avant publication ; seuls les octets finaux ont été publiés et leurs blobs vérifiés.

**Livrables SHA-authentifiés publiés** :
- `numerics/hr_b3c3d6_cubic_jet_order_certificate.py` : `a149e0c81af460b9d8dcea40546331e167d079e5`.
- `tests/test_hr_b3c3d6_cubic_jet_order_certificate.py` : `4b10f69301b4ff90e97adb5c186d8f296f1b19c0`.

**Limites et priorité inchangée** : le candidat cubique Step58, ses six coefficients aux quatre rayons, les valeurs physiques de U_ss/U_sss/U_ssss, la factorisation/enclosure uniforme, le raccord centre, les lapses positifs aux deux vrais bords, Dirac/charges/4D/stabilité/observables **ne sont pas vérifiés ici**. La preuve d'ordre local n'est ni un rang Dirac ni une validation JANUS. Le rejeu SHA-authentifié Step45/46/55/58 demeure la prochaine étape prioritaire ; DNS local GitHub indisponible, connecteur GitHub lecture/écriture opérationnel.

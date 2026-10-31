# JANUS b3c3d6 — tranche locale exacte à deux paramètres (31 octobre 2026)

**Verdict : résultat algébrique ponctuel élargi, non physique ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Origine et authentification

Le code `numerics/hr_b3c3d6_step58_two_parameter_primary_shell.py` importe et exécute les opérateurs originaux Step45 et Step58, dont les SHA Git des octets effectivement exécutés sont respectivement `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Un shim minimal fournit uniquement l'import Step57, sans prétendre rejouer Step57 complet. Les fichiers originaux ont été reconstruits localement et leurs blobs vérifiés avant l'exécution.

## Calcul exact, portée limitée

Fixer `Lg=Lf=Sg=Sf=Mg2=Mf2=m2=1`, `beta0=-5,beta1=1,beta2=beta3=0,beta4=-2`, `z=3/5`, `pg=7/4>0,pf=1>0` et les autres champs/jets exactement comme le certificat exécutable. Deux paramètres libres indépendants : `a=z_r` et `b=Sf_r`. Les quatre jets ajustés en résolvant successivement `Fz,Hg,Fz_r,Hg_r` sont

`pLg_r=1/4, Sg_rr=0, pLg_rr=-(125a+96)/64, Sg_rrr=-(75a+128b-360)/128`.

La substitution dans les véritables expressions Step45/58 donne **identiquement en a,b** :

`Fz=Fz_r=Hg=Hg_r=0`, `K=1>0`, `B_M=E_N=E_M=0`,

`C=-(25a+24b+12)/20`, `B_N=-3(25a+24b+12)/100=(3/5)C`.

Sur la droite `b=-(25a+12)/24`, on a aussi `C=B_N=0` ; à `(a,b)=(0,1)`, `C=-9/5` et `B_N=-27/25`. Ainsi les primaires et leurs premiers jets ne forcent pas à eux seuls `C=0`. Les deux dérivées exactes `∂a C=-5/4`, `∂b C=-6/5` montrent que la tranche a bien deux paramètres actifs.

**Ce résultat n'est pas la factorisation universelle** de `B_N-zC/Lg` sur l'idéal des contraintes : la famille a une codimension élevée. Ce n'est pas le profil physique Step55 ; les contraintes de jets de shift d'ordre supérieur, les six coefficients physiques et les lapses globaux ne sont pas certifiés. Les sondages rationnels exploratoires ne remplacent pas une preuve de factorisation.

## Reproductibilité

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_two_parameter_primary_shell.py' -v` : **9 PASS, 0 FAIL, 0 SKIP** au rejeu final ; un premier essai avait quatre FAIL d'égalité structurelle SymPy (forme factorisée contre forme développée), corrigés en comparant `cancel(différence)==0`. `python -m compileall -q numerics tests` : PASS. CLI `PYTHONPATH=. python -m numerics.hr_b3c3d6_step58_two_parameter_primary_shell` : PASS.

Blobs Git des octets réellement testés : source `93ae66920b69d8da0f439d54b9d04a1f3338cac8`, tests `a1631a005931ca5291e8362d92c928f9b000d6be`, JSON `7e951cfe36348c5282e8033ff9c6bd9f79590e02`. Ils ont été relus depuis GitHub après écriture et correspondent aux octets locaux.

## Verrous prioritaires

Prouver ou réfuter **universellement** le résidu inférieur de `B_N-zC/Lg-beta Hg_r` sur `Fz=Fz_r=Hg=Hg_r=0`, sans confondre tranches algébriques et coquille physique complète ; imposer `C=0` sur le vrai Step55, certifier les six enclosures Step58 aux quatre rayons `1/4,1/2,7/10,17/20`, résoudre ou exclure le BVP de deux lapses strictement positifs, puis effectuer Dirac/4D/stabilité/observables. **Aucune de ces étapes n'est close ici.**

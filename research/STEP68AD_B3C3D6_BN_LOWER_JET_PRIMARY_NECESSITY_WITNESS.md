# JANUS b3c3d6 — contre-exemple exact au raccourci « jets supérieurs annulés ⇒ résidu B_N nul » (31 octobre 2026)

**Statut : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Rejeu effectif des originaux Step45 et Step58, octets Git SHA-authentifiés (`66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `802c23aebd41780d8c462f1aa1711707fe4ee88f`) avec shim Step57 minimal, **sans** exécuter le Step57 complet.

## Famille algébrique exacte, non physique

Sur la carte `K=1, z=3/5, Lg=Lf=Sg=Sf=1, pg=7/4>0, pf=1>0`, avec `z_r=-36/25`, poser `t=Sg_rr`, `pLg_rr=t+21/16`, `Sg_rrr=85/32-2t`. Les autres jets et paramètres sont explicitement dans le module de preuve. Substitution dans le **vrai opérateur original** donne, identiquement pour tout t réel :

- `Fz=Fz_r=Hg_r=Hf=C=B_M=E_M=0`, et `K=1`.
- `Hg=2t`, `B_N=-416t/125`, `E_N=-32t/25`.
- Pour `beta=-(1-z²)/(Lg Lf)`, `B_N-z*C/Lg-beta*Hg_r = -208*Hg/125` **sur cette seule famille**.

Au témoin `t=1`, **le résidu inférieur est strictement non nul** (`-416/125`) alors que `Fz,Fz_r,Hg_r,Hf,C` et les deux coefficients `B_M,E_M` s'annulent. La contrainte primaire **`Hg=0` n'est pas satisfaite** (`Hg=2`) ; le témoin ne réfute donc PAS la conjecture de factorisation sur la coquille physique complète. À `t=0`, `Hg=B_N=E_N=0` et la famille rejoint un point de coquille, sans preuve d'universalité. Le contrôle `E_N=-(1-z²)Hg/(Lg Lf)` est cohérent avec le certificat Step58 antérieur.

**Apport scientifique précis :** le résidu de jets inférieurs n'est pas identiquement nul sur la seule surface `Fz=Fz_r=Hg_r=0`, même si `C=Hf=0`. Une future factorisation universelle doit traiter **explicitement Hg**, ou produire un contre-exemple satisfaisant aussi `Hg=0`. Aucun passage à `B_N=z*C/Lg` sur la coquille physique n'est autorisé par ce témoin.

## Reproductibilité et limites

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_BN_lower_jet_witness.py' -v` : **8 PASS, 0 FAIL, 0 SKIP**, réellement exécutés ; `python -m compileall -q numerics tests` : **PASS** ; `PYTHONPATH=. python -m numerics.hr_b3c3d6_step58_BN_lower_jet_witness` : **PASS**. Vérifications SymPy dépendantes du même opérateur, non indépendantes physiquement. Source et tests locaux testés : blobs Git `e49d8c61d24528ff88198d486d8b07996b7108a2`, `1110a9ebb368bb9470093b5a9a57d08e557d75fb` ; rapport CLI `df15cf758f7307fcd41d77eea69b08270f78dfc1`. Ces SHA doivent être vérifiés **après publication**.

Aucun Step46/55 physique ni DOP853 exécuté ici ; aucune des six enclosures physiques Step58 aux quatre rayons, aucun BVP positif aux deux bords, aucun rang Dirac/4D/stabilité/observables certifié.

**Prochaine étape :** réduire le résidu inférieur sur **`Fz=Fz_r=Hg=Hg_r=0`** (et `Hf,C` si requis) par certificat d'idéal explicite ou contre-exemple exact sur la coquille complète ; ensuite six enclosures Step58 sur la vraie Step55 aux rayons `1/4,1/2,7/10,17/20`, BVP deux bords, Dirac/4D/stabilité/observables.

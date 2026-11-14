# JANUS-005 — KG et portée du certificat Step55 (14 novembre 2026)

HEAD de lecture : f5c112c80f3733b2624a09dd8e1b98fd90d3b25a.

Audit statique des fichiers authentiques numerics/hr_step45_exact_physical_ward.py, numerics/hr_step55_normalized_secondary.py, numerics/hr_step55_global_barrier.py et du rapport JANUS005_KG_FIRST_RADIAL_JET_COMPENSATION_20261114.md.

Dans hr_step55_global_barrier.py, KG=I.c(F('.0012')) est fixé ; certify_global_barrier n'accepte pas KG en argument. La géométrie utilise betag=(1+KG**2*s).sqrt()+s*fac*KG*Lg, Rhog=-(...)/betag, Psg=(s*Dbar+Lg*Gprime-Rhog*s*KG*Lg)/Sgr et tg0=KG*Lg. La normalisation Step55 injecte Rhog, Psg0 et tg0 dans la contrainte secondaire. La certification existante à KG fixé ne s'étend donc PAS à la tangente dKG/dA≈0.1020305911 sans nouveau calcul.

Step45 fixe les lapses extérieurement lors de la première variation et utilise des smearings compacts. Les sources inspectées ne prouvent ni que KG est une jauge, ni que KG est physiquement fixé, ni que sa variation respecte Dirac et les deux vrais bords. KG intervient dans les données cinématiques de poussière ; ne pas l'assimiler à un lapse.

Contrôle contradictoire : l'annulation locale de rho_g'(0) par KG n'implique pas conservation du profil radial complet, de la barrière, ou de la solution 4D. Le rapport précédent reste une identité algébrique conditionnelle, pas un certificat physique.

Tests moteur SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0.

NEXT_ACTION_EXACT : reconstruire les 18 modules authentiques et sources historiques JANUS-001, vérifier git hash-object, exécuter neuf tests puis pilote ; en parallèle paramétrer KG dans une copie de calcul de Step55 et re-certifier la barrière et les contraintes, puis vérifier Dirac et deux vrais bords. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

# b3c3d6 — cadre régulier des lapses sans division par B_M

**Résultat exact, algébrique, conditionnel et non Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

Considérer A_N N + A_M M + B_N N' + B_M M'=0 sur un intervalle avec A_i,B_i continus, B_i de classe C1 et Delta=B_N²+B_M²>0. Poser u=B_N N+B_M M et v=-B_M N+B_N M. La matrice de passage a pour déterminant Delta, et l'inverse est N=(B_N u-B_M v)/Delta, M=(B_M u+B_N v)/Delta.

Avec X=B_N'-A_N, Y=B_M'-A_M, alpha=(X B_N+Y B_M)/Delta et beta=(-X B_M+Y B_N)/Delta, l'équation originale est exactement équivalente à u'-alpha*u=beta*v. Son facteur intégrant I(r)=exp(-integral(r0,r) alpha) donne I(R)u(R)-u(r0)=integral(r0,R) I(s)beta(s)v(s) ds. Pour v prescrit et u résolvant cette ODE, la reconstruction est équivalente, mais la positivité exige en plus B_N u-B_M v>0 et B_M u+B_N v>0.

La condition illustrative M(R)=N(R) se réécrit (B_M-B_N)u+(B_N+B_M)v=0 au bord. Elle n'est PAS assimilée aux vraies conditions d'horloge Step55. Le cadre reste régulier si B_M=0 mais B_N!=0, ou inversement. Si les deux B s'annulent, Delta=0 et il faut revenir à l'équation non divisée, qui impose alors A_N N+A_M M=0. Si les deux A ont même signe strict, aucune solution N,M>0 n'existe au point. Au centre du problème b3c2, B_i=O(r^4) et Delta=O(r^8) : aucune extension à r=0 n'est établie.

**Certificats exécutés :** 8 résidus SymPy exacts (dont deux définitionnels), 6 résidus exacts sur un jouet analytique positif avec B_N=1, B_M=r-1/2, N=M=1+r², A_M=0 et A_N=-2r(r+1/2)/(1+r²). Il traverse B_M=0 à r=1/2 et satisfait M(17/20)=N(17/20). Quatre unittest PASS non indépendants ; 0 FAIL. Les valeurs du témoin ponctuel original publiées précédemment B_N=224/125, B_M=0, A_N=1293/250, A_M=-79093/12500 donnent Delta=50176/15625>0, A_N/B_N=1293/448, A_M/B_N=-11299/3200. Elles sont reprises d'un certificat antérieur : les moteurs Step45/Step58 ne sont PAS rejoués ici. B_N' et B_M' demeurent inconnus, donc alpha et beta ne sont pas évalués sur ce témoin.

**Sources lues en direct par connecteur GitHub :** Step58 blob 802c23aebd41780d8c462f1aa1711707fe4ee88f ; Step68o blob c99caebc17f243784450ddff94fb061767e6d8e7 ; témoin original b3c3d6 blob 0144e44cd65fd69390776c1bb2d2b6120ffd74b4. Le clone local échoue avec « Could not resolve host: github.com ». Probe Step58 sur le vrai Step55 à R=17/20, Step55/Step68o/b3c2 non exécutés.

**Prochaine étape inchangée :** exécuter le probe original Step58 sur Step55, certifier B_N/B_M et leurs dérivées sur le profil, identifier zéros communs et raccords centraux, calculer b,d, résoudre le vrai problème global des lapses positifs et les bords ; puis Dirac six couples, charges/générateurs, quotient de jauge temporelle, K=0/J=0, dynamique 4D, stabilité, observables. Aucune validation physique JANUS n'est déduite.

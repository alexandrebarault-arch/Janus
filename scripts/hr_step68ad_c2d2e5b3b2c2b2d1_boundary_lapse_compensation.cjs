'use strict';
/* Exact finite-dimensional boundary pullback from the original non-IBP minus IBP
   identity. Lapses are independent boundary multipliers; co-variation is NOT
   a physical lapse boundary condition or a full six-pair Dirac calculation. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
function q(s){s=String(s);if(s.includes('/')){const x=s.split('/');return Q(x[0],x[1]);}if(s.includes('.')){let neg=s[0]==='-';if(neg)s=s.slice(1);const x=s.split('.');return Q((neg?-1n:1n)*BigInt(x[0]+x[1]),10n**BigInt(x[1].length));}return Q(s);}
function add(a,b){return Q(a.n*b.d+b.n*a.d,a.d*b.d);}
function neg(a){return Q(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return Q(a.n*b.n,a.d*b.d);}
function div(a,b){return Q(a.n*b.d,a.d*b.n);}
function cmp(a,b){const x=a.n*b.d-b.n*a.d;return x<0n?-1:x>0n?1:0;}
function eq(a,b){return cmp(a,b)===0;}
function show(a){return String(a.n)+(a.d===1n?'':'/'+String(a.d));}
const Z=q('0'),O=q('1'),T=q('2'),R=q('17/20'),S=mul(R,R),LAMBDA=q('1/5000');
const A=q('.4'),Y=q('.5787707228025044'),B=mul(A,Y);
const CG=q('.0015'),CF=q('-.0012'),Z1=q('.004');
const MG2=O,MF2=mul(q('.10879548725'),q('.10879548725')),M2=q('23.3348939346');
const B2=q('-4.2383993109'),B3=q('13.6801214252');
function sq(x){return mul(x,x);}
const H2=add(div(q('.9'),mul(q('3'),mul(sq(A),A))),
 div(mul(M2,add(add(mul(q('3'),Y),mul(q('3'),mul(B2,sq(Y)))),mul(B3,mul(sq(Y),Y)))),q('3')));
const pgBounds=[q('-4/5'),q('-16/25')]; // Step55 Pg=-2*A^2*sqrt(H2), and 5<H2<6 imply this interval.
const ug=add(O,mul(CG,S)),uf=add(O,mul(CF,S));
const Lg=mul(A,sq(ug)),Lf=mul(B,sq(uf)),ratio=div(Lg,Lf);
const Sgr=mul(A,mul(ug,add(O,mul(q('5'),mul(CG,S)))));
const Sfr=mul(B,mul(uf,add(O,mul(q('5'),mul(CF,S)))));
const z=mul(R,Z1),a=mul(S,add(O,mul(q('5/2'),mul(CG,S))));
const Ag=mul(T,mul(MG2,mul(R,Sgr))),Af=mul(T,mul(MF2,mul(R,Sfr)));
const za=mul(z,a);
function p(P,lam=Z){return mul(a,add(P,lam));}
function Cg(P,lam=Z){return sub(Ag,mul(z,p(P,lam)));}
function Cf(P,lam=Z){return sub(Af,mul(mul(z,ratio),p(P,lam)));}
function boundary(P,lam,N=O,M=O){return add(mul(Cg(P,lam),N),mul(Cf(P,lam),M));}
function compensatingN(P,lam,M=O){
 // Keep B(lam,N(lam),M)=B(0,1,M); no assertion about temporal constraints.
 return div(add(Cg(P,Z),mul(mul(za,ratio),mul(lam,M))),Cg(P,lam));
}
function compensationSlope(P,lam,M=O){
 return div(mul(za,mul(add(O,mul(ratio,M)),Cg(P,Z))),sq(Cg(P,lam)));
}
function dBdl(N=O,M=O){return neg(mul(za,add(N,mul(ratio,M))));}
function counterterm(P,lam,N=O,M=O){return neg(boundary(P,lam,N,M));}
function certificate(){
 return {
 step:'68ad-C2d2e5b3b2c2b2d1',
 scope:'EXACT boundary pullback classification on Step55/68o spatial family; not a physical BC or a Dirac proof',
 source_blobs:{
  'numerics/hr_step37_original_nonibp_oracle.py':'005449ade6e3582e3b9a5c3374a881a77e73e3f6',
  'numerics/hr_spherical_adm_primary.py':'c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41',
  'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
 },
 R:show(R),lambda_abs_max:show(LAMBDA),H2:show(H2),
 physical_Pg_rational_enclosure:pgBounds.map(show),
 z:show(z),a_dlambda_pLg:show(a),q_Lg_over_Lf:show(ratio),
 Ag:show(Ag),Af:show(Af),za:show(za),
 boundary_formula:'B=(Ag-z*a*(Pg+lambda))*N+(Af-z*q*a*(Pg+lambda))*M',
 boundary_fixed_lapses_slope_N1_M1:show(dBdl()),
 mixed_derivatives:{lambda_N:show(neg(za)),lambda_M:show(neg(mul(za,ratio)))},
 exact_lapse_compensation_M1:'N(lambda)=[Cg(Pg,0)+z*q*a*lambda]/[Cg(Pg,0)-z*a*lambda]',
 compensation_slope:'Nprime=z*a*(1+q)*Cg(Pg,0)/[Cg(Pg,0)-z*a*lambda]^2 >0',
 certified_uniform_conditions:['5<H2<6','-4/5<Pg<-16/25','Pg+lambda<0','Cg>Ag>2/3','Cf>Af>0','0<z<1/250','0<a<3/4','1<q<2','999/1000<N(lambda)<1001/1000'],
 counterterm_classification:'On the connected (lambda,N,M) pullback, d(B+C)=0 in all three independent directions iff C=-B+constant. No lapse-independent C(lambda), and no momentum-independent C(N,M; fixed geometry/shift and NO explicit lambda dependence), can do this.',
 physical_limits:'Cancels only original-minus-IBP boundary difference on this restricted pullback. Does not certify functional differentiability of either Hamiltonian, six-pair Poisson/Dirac, lapse admissibility, temporal propagation, K=0/J=0, 4D or observables.',
 GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'
 };
}
module.exports={Q,q,add,neg,sub,mul,div,cmp,eq,show,Z,O,R,S,LAMBDA,H2,pgBounds,z,a,ratio,Ag,Af,za,p,Cg,Cf,boundary,compensatingN,compensationSlope,dBdl,counterterm,certificate};
if(require.main===module)process.stdout.write(JSON.stringify(certificate(),null,2)+'\n');

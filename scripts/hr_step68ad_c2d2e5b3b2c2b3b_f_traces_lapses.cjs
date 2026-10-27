'use strict';
/* Step68ad b3b: rigorous rational outer f-trace enclosures inherited from
   authenticated Step45/46/55 Pg-tube certificate b2; no new ODE execution.
   Root enclosure is proven on the entire radial interval.
   Also classify lapse-dependent original-minus-IBP boundary variation. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return {n:n/g,d:d/g};}
function q(x){let s=String(x);if(s.includes('/')){let p=s.split('/');return Q(p[0],p[1]);}if(s.includes('.')){let neg=s[0]==='-';if(neg)s=s.slice(1);let p=s.split('.');return Q((neg?-1n:1n)*BigInt(p[0]+p[1]),10n**BigInt(p[1].length));}return Q(s);}
function add(a,b){return Q(a.n*b.d+b.n*a.d,a.d*b.d);}
function neg(a){return Q(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return Q(a.n*b.n,a.d*b.d);}
function div(a,b){return Q(a.n*b.d,a.d*b.n);}
function cmp(a,b){let v=a.n*b.d-b.n*a.d;return v<0n?-1:v>0n?1:0;}
function show(a){return String(a.n)+(a.d===1n?'':'/'+String(a.d));}
const Z=q('0'),ONE=q('1'),TWO=q('2');
function I(lo,hi=lo){if(cmp(lo,hi)>0)throw Error('invalid interval');return {lo,hi};}
function ci(x){return x&&x.lo!==undefined?x:I(x);}
function ia(a,b){a=ci(a);b=ci(b);return I(add(a.lo,b.lo),add(a.hi,b.hi));}
function ineg(a){a=ci(a);return I(neg(a.hi),neg(a.lo));}
function isub(a,b){return ia(a,ineg(b));}
function im(a,b){a=ci(a);b=ci(b);let x=[mul(a.lo,b.lo),mul(a.lo,b.hi),mul(a.hi,b.lo),mul(a.hi,b.hi)];x.sort(cmp);return I(x[0],x[3]);}
function idiv(a,b){a=ci(a);b=ci(b);if(cmp(b.lo,Z)<=0&&cmp(b.hi,Z)>=0)throw Error('zero interval');return im(a,I(div(ONE,b.hi),div(ONE,b.lo)));}
function sq(a){a=ci(a);if(cmp(a.lo,Z)<=0&&cmp(a.hi,Z)>=0)return I(Z,cmp(mul(a.lo,a.lo),mul(a.hi,a.hi))>0?mul(a.lo,a.lo):mul(a.hi,a.hi));let x=mul(a.lo,a.lo),y=mul(a.hi,a.hi);return I(cmp(x,y)<0?x:y,cmp(x,y)>0?x:y);}
function exact(i){return [show(i.lo),show(i.hi)];}
const R=q('17/20'),S=mul(R,R),A=q('0.4'),B=mul(A,q('0.5787707228025044'));
const CG=q('0.0015'),CF=q('-0.0012'),KF=q('-0.0016'),Z1=q('0.004'),M2=q('23.3348939346'),MF=mul(q('0.10879548725'),q('0.10879548725'));
const U=I(q('-10707594192153122134265173/2000000000000000000000000000'),q('-1146420876631433922729177/250000000000000000000000000'));
const V=I(q('-31475070089799984705831899/2500000000000000000000000000'),q('-61130791189474633664185037/10000000000000000000000000000'));
const RHOF=I(q('13681002401623193480723629/125000000000000000000000000'),q('1269204970466940095332675403/10000000000000000000000000000'));
const BASE_CERT_BLOB='012e70e49b41cc3180da423c3962d279e3909a26';
function calculate(){
 let ug=add(ONE,mul(CG,S)),uf=add(ONE,mul(CF,S));
 let Lg=mul(A,mul(ug,ug)),Lf=mul(B,mul(uf,uf));
 let Sfr=mul(B,mul(uf,add(ONE,mul(q('5'),mul(CF,S)))));
 let T=add(add(mul(Lg,Lg),mul(mul(TWO,q('-4.2383993109')),mul(Lg,Lf))),mul(q('13.6801214252'),mul(Lf,Lf)));
 let rootLow=q('99999/100000'),rootSquare=sub(ONE,mul(mul(Z1,Z1),S));
 if(cmp(mul(rootLow,rootLow),rootSquare)>=0||cmp(rootSquare,ONE)>=0)throw Error('root bracket not proven');
 let root=I(rootLow,ONE);
 let Dbar=idiv(I(mul(mul(mul(mul(M2,Lg),Lf),T),Z1)),root);
 let pLf=im(I(S),U),pLfPrime=im(I(R),V),pf=im(I(S),RHOF);
 let pSf=idiv(isub(ia(ineg(im(I(mul(mul(R,R),R)),Dbar)),im(I(Lf),pLfPrime)),im(pf,I(mul(mul(R,KF),Lf)))),I(Sfr));
 if(cmp(pLf.hi,Z)>=0||cmp(pLfPrime.hi,Z)>=0||cmp(pSf.hi,Z)>=0||cmp(pf.lo,Z)<=0)throw Error('trace sign not certified');
 let a=mul(S,add(ONE,mul(q('5/2'),mul(CG,S)))),z=mul(R,Z1),ratio=div(Lg,Lf);
 let mixedN=neg(mul(z,a)),mixedM=mul(mixedN,ratio);
 if(cmp(mixedN,Z)>=0||cmp(mixedM,Z)>=0)throw Error('lapse mixed derivatives not negative');
 return {step:'68ad-C2d2e5b3b2c2b3b',scope:'EXACT_OUTER_F_TRACE_ENCLOSURE_AND_LAPSE_MIXED_VARIATION_ONLY',
  source:'Previously certified authentic Step45/46/55 parameter-tube enclosure; no original engine reexecution in this step',
  original_tube_certificate_blob:BASE_CERT_BLOB,
  lambda_domain:['-1/5000','1/5000'],r_outer:show(R),root_bracket:[show(rootLow),'1'],
  root_square_exact:show(rootSquare),T_outer:show(T),Dbar_outer:exact(Dbar),
  pLf_outer:exact(pLf),pLf_prime_outer:exact(pLfPrime),pf_outer:exact(pf),pSf_outer:exact(pSf),
  pLf_sign:'STRICT_NEGATIVE',pLf_prime_sign:'STRICT_NEGATIVE',pSf_sign:'STRICT_NEGATIVE',pf_sign:'STRICT_POSITIVE',
  mixed_lambda_lapse_N:show(mixedN),mixed_lambda_lapse_M:show(mixedM),
  boundary_variation:'delta B=(Ag-z*pLg)*delta N+(Af-z*q*pLg)*delta M-z*a*(N+q*M)*delta lambda; Ag=2Mg2*R*Sgr; Af=2Mf2*R*Sfr; q=Lg/Lf',
  no_go:'No lapse-independent counterterm C(lambda) can cancel delta_lambda B for all independently variable N,M, since mixed_lambda_lapse_N and M are nonzero',
  caution:'These are broad enclosure bounds, not sensitivity derivatives of f traces; no physical boundary condition or full functional Dirac matrix established',
  tests_runtime:'V8 BigInt rational',GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'};
}
module.exports={q,Q,add,sub,mul,div,cmp,show,I,ia,im,idiv,calculate,R,S,U,V,RHOF,Z,ONE,BASE_CERT_BLOB};
if(require.main===module)process.stdout.write(JSON.stringify(calculate(),null,2)+'\n');

'use strict';
// Exact regular variational lemma, conditional on analytic authentic G.
// Does NOT calculate G_U/G_Pg on the physical radial tube.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const Z=Q(0),O=Q(1);
function add(a,b){return Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function neg(a){return [-a[0],a[1]];}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return Q(a[0]*b[0],a[1]*b[1]);}
function div(a,b){if(!b[0])throw Error('division by zero');return Q(a[0]*b[1],a[1]*b[0]);}
function eq(a,b){return a[0]*b[1]===b[0]*a[1];}
function lt(a,b){return a[0]*b[1]<b[0]*a[1];}
function abs(a){return a[0]<0n?neg(a):a;}
function fmt(a){return a[1]===1n?String(a[0]):String(a[0])+'/'+String(a[1]);}
const mf=Q(10879548725n,100000000000n);
const y=Q(5787707228025044n,10000000000000000n);
const v0=mul(mul(mf,mf),y);
const smax=Q(289,400);
const GU0=Q(-1), GP0=mul(Q(3),v0);
// A=G_U-2=-3+sum a_k s^k; B=G_P=3*v0+sum b_k s^k.
// Analytic bounded solution: (2n+3)v_n=b_n+sum_{k=1}^n a_k*v_{n-k}.
function series(a,b,n){
 if(!Number.isInteger(n)||n<0||n>100)throw Error('invalid degree');
 const v=[v0];
 for(let j=1;j<=n;j++){
  let sum=b[j]||Z;
  for(let k=1;k<=j;k++)sum=add(sum,mul(a[k]||Z,v[j-k]));
  v.push(div(sum,Q(2*j+3)));
 }
 return v;
}
function residual(a,b,v){
 const out=[add(mul(Q(-3),v[0]),mul(Q(3),v0))];
 for(let n=1;n<v.length;n++){
  let rhs=add(mul(Q(-3),v[n]),b[n]||Z);
  for(let k=1;k<=n;k++)rhs=add(rhs,mul(a[k]||Z,v[n-k]));
  out.push(sub(mul(Q(2*n),v[n]),rhs));
 }
 return out;
}
// If |G_U+1|<=alpha*s and |G_P-3*v0|<=beta*s on [0,S],
// then |v(s)-v0| <= (alpha*|v0|+beta)*s*exp(alpha*s/2)/5.
// exp(x)<=1/(1-x) for 0<=x<1 gives a fully rational sufficient bound.
function enclosure(alpha,beta,S=smax){
 if(lt(alpha,Z)||lt(beta,Z)||lt(S,Z))throw Error('negative bound');
 const x=div(mul(alpha,S),Q(2));
 if(!lt(x,O))throw Error('rational exponential majorant unavailable');
 const q=add(mul(alpha,abs(v0)),beta);
 const bound=div(mul(q,S),mul(Q(5),sub(O,x)));
 return {bound,positive:lt(bound,v0),x};
}
function certificate(){
 const ex=enclosure(Q(1,10),Q(1,100));
 const a=[Z,Q(1,10)],b=[Z,Q(1,100)];
 const v=series(a,b,4);
 return {
  step:'68ad-C2d2e5b3b2c2b3c2b2a',
  classification:'EXACT_CONDITIONAL_REGULAR_VARIATIONAL_LEMMA_NOT_PHYSICAL_G_DERIVATIVE',
  source_identity:'Step55 G(0,U,P)=3*Mf2*b*(P/a-2*z1)-U (previously authenticated)',
  s_domain:['0',fmt(smax)],
  center:{v0:fmt(v0),GU0:fmt(GU0),GP0:fmt(GP0),A0:'-3',B0:fmt(GP0)},
  recurrence:'(2n+3)*v_n = b_n + sum_{k=1}^n a_k*v_{n-k}, n>=1; A=-3+sum a_k s^k, B=3v0+sum b_k s^k',
  first_jet:'v1=(a1*v0+b1)/5',
  synthetic_example:{a1:'1/10',b1:'1/100',v1:fmt(v[1]),v2:fmt(v[2]),v3:fmt(v[3]),v4:fmt(v[4])},
  conditional_rational_majorant:{alpha:'1/10',beta:'1/100',alpha_S_over_2:fmt(ex.x),max_abs_v_minus_v0:fmt(ex.bound),positivity_if_hypotheses_certified:ex.positive},
  hypotheses_not_checked:['authentic G_U/G_Pg bounds alpha,beta','physical v(R)','f trace derivatives','boundary admissibility','six-pair temporal Dirac rank'],
  GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'
 };
}
module.exports={Q,Z,O,add,sub,mul,div,eq,lt,abs,fmt,mf,y,v0,smax,GU0,GP0,series,residual,enclosure,certificate};
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(certificate(),null,2));

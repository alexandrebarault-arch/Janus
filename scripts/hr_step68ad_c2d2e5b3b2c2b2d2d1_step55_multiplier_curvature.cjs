'use strict';
/* JANUS d2d1: authentic Step55 spatial shell, NOT full Dirac tangent.
   The non-IBP boundary one-form is pulled back to the one-parameter
   spatial Pg family, with independent boundary multipliers N,M,V.
   Exact rational arithmetic; f-sector derivative is an enclosure. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
function q(x){x=String(x);if(x.includes('/')){const p=x.split('/');return Q(p[0],p[1]);}if(x.includes('.')){let neg=x[0]==='-';if(neg)x=x.slice(1);const p=x.split('.');return Q((neg?-1n:1n)*BigInt(p[0]+p[1]),10n**BigInt(p[1].length));}return Q(x);}
function add(a,b){return Q(a.n*b.d+b.n*a.d,a.d*b.d);}
function neg(a){return Q(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return Q(a.n*b.n,a.d*b.d);}
function div(a,b){return Q(a.n*b.d,a.d*b.n);}
function eq(a,b){return a.n===b.n&&a.d===b.d;}
function lt(a,b){return a.n*b.d<b.n*a.d;}
function show(a){return a.n.toString()+(a.d===1n?'':'/'+a.d.toString());}
function run(){
 let passed=0;function check(cond,label){if(!cond)throw Error('assertion '+(passed+1)+' '+label);passed++;}
 const R=q('17/20'),s=mul(R,R),cg=q('0.0015'),cf=q('-0.0012'),A=q('0.4'),B=mul(A,q('0.5787707228025044'));
 const Lg=mul(A,mul(add(q(1),mul(cg,s)),add(q(1),mul(cg,s))));
 const Lf=mul(B,mul(add(q(1),mul(cf,s)),add(q(1),mul(cf,s))));
 const ratio=div(Lg,Lf),z=mul(R,q('0.004'));
 const a=mul(s,add(q(1),mul(q('5/2'),mul(cg,s))));
 const bLo=q('196809/40000000'),bHi=q('199121/40000000');
 const cN=neg(mul(z,a)),cM=mul(cN,ratio);
 const cVlo=neg(add(mul(Lg,a),mul(Lf,bHi)));
 const cVhi=neg(add(mul(Lg,a),mul(Lf,bLo)));
 check(eq(s,q('289/400')),'radius squared');
 check(eq(z,q('17/5000')),'shift at outer boundary');
 check(eq(a,q('92730563/128000000')),'exact g momentum derivative');
 check(eq(ratio,q('2505421686285156250000000000/1444418923561876775155324829')),'original g/f geometry ratio');
 check(lt(q(0),Lg),'positive Lg');
 check(lt(q(0),Lf),'positive Lf');
 check(lt(q(0),ratio),'positive ratio');
 check(lt(q(0),a),'positive g derivative');
 check(lt(q(0),bLo),'positive f derivative lower bound');
 check(lt(bLo,bHi),'strict f derivative enclosure');
 check(eq(cN,neg(mul(z,a))),'mixed N coefficient');
 check(eq(cM,mul(cN,ratio)),'mixed M coefficient');
 check(lt(cN,q(0)),'negative N curvature');
 check(lt(cM,q(0)),'negative M curvature');
 check(lt(cVlo,cVhi),'V curvature ordered enclosure');
 check(lt(cVhi,q(0)),'negative V curvature');
 check(eq(sub(cVhi,cVlo),mul(Lf,sub(bHi,bLo))),'V enclosure width');
 check(eq(div(cM,cN),ratio),'N/M curvature ratio');
 // Representative b is ONLY an algebraic test point inside a proven interval.
 const bMid=div(add(bLo,bHi),q(2));
 check(lt(bLo,bMid),'representative inside lower bound');
 check(lt(bMid,bHi),'representative inside upper bound');
 const cV=neg(add(mul(Lg,a),mul(Lf,bMid)));
 check(lt(cVlo,cV),'representative V curvature lower bound');
 check(lt(cV,cVhi),'representative V curvature upper bound');
 const F=(N,M,V)=>add(add(mul(cN,N),mul(cM,M)),mul(cV,V));
 const n=q('7/6'),m=q('11/9'),v=q('-2/7'),dn=q('1/17'),dm=q('-3/13'),dv=q('5/19');
 check(eq(sub(F(add(n,dn),m,v),F(n,m,v)),mul(cN,dn)),'exact independent N finite difference');
 check(eq(sub(F(n,add(m,dm),v),F(n,m,v)),mul(cM,dm)),'exact independent M finite difference');
 check(eq(sub(F(n,m,add(v,dv)),F(n,m,v)),mul(cV,dv)),'exact independent V finite difference');
 check(eq(sub(F(add(n,dn),add(m,dm),add(v,dv)),F(n,m,v)),add(add(mul(cN,dn),mul(cM,dm)),mul(cV,dv))),'combined finite difference');
 check(eq(sub(F(add(n,dn),add(m,dm),v),F(add(n,dn),m,v)),mul(cM,dm)),'N/M cross consistency');
 check(eq(sub(F(add(n,dn),m,add(v,dv)),F(n,m,add(v,dv))),mul(cN,dn)),'N/V cross consistency');
 check(eq(sub(F(n,add(m,dm),add(v,dv)),F(n,m,add(v,dv))),mul(cM,dm)),'M/V cross consistency');
 check(eq(F(q(0),q(0),q(0)),q(0)),'zero multiplier');
 check(eq(F(q(1),q(0),q(0)),cN),'unit N');
 check(eq(F(q(0),q(1),q(0)),cM),'unit M');
 check(eq(F(q(0),q(0),q(1)),cV),'unit V');
 check(lt(cN,q('-0.002')),'N curvature stronger than -0.002');
 check(lt(q('-0.003'),cN),'N curvature weaker than -0.003');
 return {
  step:'68ad-C2d2e5b3b2c2b2d2d1',assertions_passed:passed,assertions_failed:0,
  scope:'Authentic Step55/68o one-parameter spatial C(r)=0 family conditional on Step49 and b2/b2b; boundary multipliers independent; NOT full Dirac tangent.',
  R:'17/20',lambda:['-1/5000','1/5000'],
  exact:{Lg:show(Lg),Lf:show(Lf),q:show(ratio),z:show(z),a_dpLg_dlambda:show(a),dTheta_dN_wedge_dlambda:show(cN),dTheta_dM_wedge_dlambda:show(cM)},
  enclosures:{dpLf_dlambda:[show(bLo),show(bHi)],dTheta_dV_wedge_dlambda:[show(cVlo),show(cVhi)]},
  one_dimensional_fixed_multiplier_pullback:'dTheta=0 on the lambda-only spatial family for fixed N,M,V, by dimension; no ambient obstruction can be inferred from this 1D pullback.',
  extended_multiplier_pullback:'Theta=F(lambda,N,M,V) d(lambda); dTheta=cN dN^d(lambda)+cM dM^d(lambda)+cV dV^d(lambda), with cV enclosed; no dN/dM/dV components of Theta at fixed boundary fields.',
  status:{GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'},
  original_source_blobs:{
   step37:'005449ade6e3582e3b9a5c3374a881a77e73e3f6',
   step45:'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
   step46:'bac025c28dbe1561c0c36c56dbfda46dc326f804',
   step55:'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
   prior_f_derivative_certificate:'b53eb93c48fba7099ae2d3275ec4eb5e0464a7a4'
  },
  limits:['No second independent canonical tangent to the full secondary functional constraint surface constructed','N,M,V are Lagrange multipliers, not canonical pairs','No physical lapse/boundary polarization selected','No tertiary preservation or full six-pair Dirac matrix','No original Python engine rerun in this step']
 };
}
module.exports={run};
if(require.main===module)process.stdout.write(JSON.stringify(run(),null,2)+'\n');

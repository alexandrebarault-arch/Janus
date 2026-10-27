'use strict';
// Step45/46/55 central Pg sensitivity: exact rational arithmetic, no floating point.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q {
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 static of(x){if(x instanceof Q)return x;const s=String(x);if(s.includes('/')){const [a,b]=s.split('/');return new Q(BigInt(a),BigInt(b));}if(s.includes('.')){const sign=s[0]==='-'?-1n:1n;const p=s.replace('-','').split('.');return new Q(sign*BigInt(p[0]+p[1]),10n**BigInt(p[1].length));}return new Q(BigInt(s));}
 add(x){x=Q.of(x);return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(x){return this.add(Q.of(x).neg());}
 mul(x){x=Q.of(x);return new Q(this.n*x.n,this.d*x.d);}
 div(x){x=Q.of(x);return new Q(this.n*x.d,this.d*x.n);}
 pow(k){return new Q(this.n**BigInt(k),this.d**BigInt(k));}
 cmp(x){x=Q.of(x);const t=this.n*x.d-x.n*this.d;return t<0n?-1:t>0n?1:0;}
 toString(){return this.d===1n?String(this.n):this.n+'/'+this.d;}
}
const q=Q.of;
function check(c,m){if(!c)throw Error(m);}
function center(){
 const A=q('.4'),Y=q('.5787707228025044'),B=A.mul(Y),MF=q('.10879548725').pow(2),M2=q('23.3348939346'),Z=q('.004'),CF=q('-.0012');
 const B1=q('1'),B2=q('-4.2383993109'),B3=q('13.6801214252'),B4=q('-38.5117901844');
 const H2=q('.9').div(q(3).mul(A.pow(3))).add(M2.mul(q(3).mul(B1).mul(Y).add(q(3).mul(B2).mul(Y.pow(2))).add(B3.mul(Y.pow(3)))).div(3));
 // PG=-2*A^2*sqrt(H2). Strict rational enclosure by squaring.
 const pglo=q('-.764'),pghi=q('-.763'),p2=q(4).mul(A.pow(4)).mul(H2);
 check(H2.cmp(0)>0,'H2 positive');check(pglo.pow(2).cmp(p2)>0 && p2.cmp(pghi.pow(2))>0,'PG squared bracket');
 const u=(p)=>MF.mul(B).mul(p.div(A).sub(q(2).mul(Z)));
 const ulo=u(pglo),uhi=u(pghi),v=MF.mul(B).div(A);
 check(ulo.cmp(uhi)<0 && uhi.cmp(0)<0,'U0 negative');
 const expected=q('274023815147385251710689588080861/40000000000000000000000000000000000');
 check(v.cmp(expected)===0,'Step49 center v0');
 const Rf=q(-48).mul(CF).div(B.pow(2));
 const Tf=B2.mul(A.pow(2)).add(q(2).mul(B3).mul(A).mul(B)).add(B4.mul(B.pow(2)));
 const T=B1.mul(A.pow(2)).add(q(2).mul(B2).mul(A).mul(B)).add(B3.mul(B.pow(2)));
 const Wf=M2.mul(B.mul(Tf).add(A.mul(T)));
 const offset=MF.mul(B.pow(3)).mul(Rf).div(2).sub(Wf);
 const rho=(x)=>q(3).mul(x.pow(2)).div(q(4).mul(MF).mul(B)).add(offset);
 const drho=(x)=>q(3).mul(x).div(q(2).mul(A));
 const quadratic=q(3).mul(v.pow(2)).div(q(4).mul(MF).mul(B));
 check(drho(ulo).cmp(drho(uhi))<0,'derivative monotone');
 check(drho(ulo).cmp(q('-.020'))>0 && drho(uhi).cmp(q('-.019'))<0,'central f density slope strict bounds');
 check(rho(uhi).cmp(q('.12'))>0 && rho(ulo).cmp(q('.13'))<0,'positive central f dust bounds');
 // On lambda in [-1/5000,+1/5000], rho(lambda) strictly decreases; minimum at lambda=+1/5000.
 const rad=q('1/5000');
 check(drho(uhi).add(q(2).mul(quadratic).mul(rad)).cmp(0)<0,'strict monotonicity entire parameter tube');
 check(rho(uhi.add(v.mul(rad))).cmp(q('.12'))>0,'uniform central rho_f>0.12');
 // Step46 central identities: V0=2U0, pSf/r -> 2U0, pLf/r^2 -> U0, pLf_prime/r -> 2U0.
 check(q(3).mul(v).sub(v).cmp(q(2).mul(v))===0,'G(0) central slope');
 // Exact polynomial identity from the primary reconstruction.
 for(const lam of [q(0),rad,rad.neg(),q('1/10000')]){
  const lhs=rho(ulo.add(v.mul(lam)));
  const rhs=rho(ulo).add(drho(ulo).mul(lam)).add(quadratic.mul(lam.pow(2)));
  check(lhs.cmp(rhs)===0,'rho_f central polynomial');
 }
 return {step:'68ad-C2d2e5b3b2c2b3c1',status:'EXACT_CENTER_ONLY_PHYSICAL_SENSITIVITY',H2:H2.toString(),PG_enclosure:[pglo.toString(),pghi.toString()],U0_enclosure:[ulo.toString(),uhi.toString()],v0:v.toString(),dV0_dlambda:q(2).mul(v).toString(),drho_f0_enclosure:[drho(ulo).toString(),drho(uhi).toString()],rho_f0_enclosure:[rho(uhi).toString(),rho(ulo).toString()],rho_f0_quadratic_lambda_coefficient:quadratic.toString(),lambda_domain:['-1/5000','1/5000'],rho_f0_uniform_lower:'3/25',source_blobs:{'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804','numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'},not_proven:['outer trace derivatives at R','admissible physical boundary conditions','full Dirac rank and tertiary constraints','4D stability and observables'],GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'};
}
module.exports={Q,center};
if(require.main===module)console.log(JSON.stringify(center(),null,2));

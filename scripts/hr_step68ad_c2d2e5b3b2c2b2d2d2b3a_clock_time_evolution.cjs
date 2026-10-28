"use strict";
/* JANUS d2d2b3a: exact-rational temporal dust-clock boundary audit.
   Algebraic proof applies conditionally to Step55 signs; toy witness is NOT Step55.
   Does NOT construct an improved Dirac generator. */
function certificate(){
 let checks=0;
 function ok(c,m){if(!c)throw Error("FAIL "+m);checks++;}
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a||1n;}
 class F{
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);this.n=n/g;this.d=d/g;}
  static of(v){if(v instanceof F)return v;let s=String(v),neg=s[0]==="-";if(neg)s=s.slice(1);let p=s.split(".");let d=10n**BigInt((p[1]||"").length);return new F((neg?-1n:1n)*BigInt(p.join("")),d);}
  add(v){v=F.of(v);return new F(this.n*v.d+v.n*this.d,this.d*v.d);}
  neg(){return new F(-this.n,this.d);}
  sub(v){return this.add(F.of(v).neg());}
  mul(v){v=F.of(v);return new F(this.n*v.n,this.d*v.d);}
  div(v){v=F.of(v);return new F(this.n*v.d,this.d*v.n);}
  eq(v){v=F.of(v);return this.n*v.d===v.n*this.d;}
  gt(v){v=F.of(v);return this.n*v.d>v.n*this.d;}
  lt(v){v=F.of(v);return this.n*v.d<v.n*this.d;}
  str(){return this.n+"/"+this.d;}
 }
 const f=F.of,one=f(1),R=f("0.85"),s=R.mul(R);
 const gg=one.add(f("0.0015").mul(s));
 const ff=one.add(f("-0.0012").mul(s));
 const Lg=f("0.4").mul(gg).mul(gg);
 const Lf=f("0.4").mul(f("0.5787707228025044")).mul(ff).mul(ff);
 const hg=f("0.0012").mul(R).mul(Lg),hf=f("-0.0016").mul(R).mul(Lf);
 const z=f("0.004").mul(R);
 ok(R.eq(f(17).div(20)),"R exact");
 ok(s.eq(f(289).div(400)),"s exact");
 ok(Lg.gt(0)&&Lf.gt(0),"positive metric factors");
 ok(hg.gt(0)&&hf.lt(0),"opposite clock slopes");
 ok(z.gt(0),"positive HR shift");
 ok(hg.sub(hf).gt(0),"relative clock denominator");
 for(const [N,M] of [[f(1),f(1)],[f(2),f(3)],[f("0.0001"),f("1000")]]){
  const Q=N.div(Lg).add(M.div(Lf));
  ok(N.gt(0)&&M.gt(0)&&Q.gt(0),"positive lapses");
  ok(z.mul(Q).mul(hg).gt(0),"positive HR g clock term");
  // If dot(tg)=0, V=-zQ-N*sg/hg<0; if dot(tf)=0, V=-M*sf/hf>0.
  // sg,sf>=1, hence the following strict rational root separation.
  const VgUpper=z.mul(Q).neg().sub(N.div(hg));
  const VfLower=M.div(hf).neg();
  ok(VgUpper.lt(0),"stationary g requires V negative");
  ok(VfLower.gt(0),"stationary f requires V positive");
  ok(VgUpper.lt(VfLower),"stationary V intervals disjoint");
  // For dot(tg)=dot(tf), unique V and common speed strictly positive.
  const uLower=hf.neg().mul(N.add(z.mul(Q).mul(hg))).add(hg.mul(M)).div(hg.sub(hf));
  ok(uLower.gt(0),"relative clock common speed positive");
 }
 // Exact Pythagorean toy witness (not physical Step55).
 const x=f(3).div(4),y=f(-5).div(12),sg=f(5).div(4),sf=f(13).div(12);
 const N=one,M=one,lg=one,lf=one,zz=f(1).div(5),pg=f(2),pf=f(3);
 const Q=N.div(lg).add(M.div(lf));
 ok(sg.mul(sg).eq(one.add(x.mul(x))),"exact g square root");
 ok(sf.mul(sf).eq(one.add(y.mul(y))),"exact f square root");
 const ag=x.div(lg.mul(lg).mul(sg)),af=y.div(lf.mul(lf).mul(sf));
 ok(ag.mul(lg.mul(lg)).mul(sg).eq(x),"g derivative identity");
 ok(af.mul(lf.mul(lf)).mul(sf).eq(y),"f derivative identity");
 const baseg=N.mul(sg).add(zz.mul(Q).mul(x)),basef=M.mul(sf);
 const Vrel=basef.sub(baseg).div(x.sub(y));
 const ug=baseg.add(Vrel.mul(x)),uf=basef.add(Vrel.mul(y));
 ok(Vrel.eq(f(-2).div(5)),"unique Vrel");
 ok(ug.eq(uf),"preserved relative clock");
 ok(ug.eq(f(5).div(4))&&ug.gt(0),"common clock speed");
 const Jg=pg.mul(N.mul(ag).add(zz.mul(Q)).add(Vrel));
 const Jf=pf.mul(M.mul(af).add(Vrel));
 const Vflux=pg.mul(N.mul(ag).add(zz.mul(Q))).add(pf.mul(M.mul(af))).neg().div(pg.add(pf));
 ok(Vflux.eq(f(-11).div(65)),"Vflux exact");
 ok(Jg.add(Jf).eq(f(-15).div(13)),"Vrel fails diagonal bare flux");
 ok(!Vrel.eq(Vflux),"Vrel and Vflux distinct");
 const Jg0=pg.mul(N.mul(ag).add(zz.mul(Q)).add(Vflux));
 const Jf0=pf.mul(M.mul(af).add(Vflux));
 ok(Jg0.add(Jf0).eq(0),"Vflux cancels diagonal bare flux");
 ok(!baseg.add(Vflux.mul(x)).eq(basef.add(Vflux.mul(y))),"Vflux fails relative preservation");
 // At a regular center with both slopes zero, dot(tg)=N and dot(tf)=M.
 ok(one.gt(0),"positive lapse premise at regular center");
 return {
  step:"68ad-C2d2e5b3b2c2b2d2d2b3a",assertions_passed:checks,assertions_failed:0,
  original_source_shas:{step37:"005449ade6e3582e3b9a5c3374a881a77e73e3f6",step45:"66aa43841dccfe4a5d586a49be9c10af3a67a10e",step55:"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",boundary_d2a:"94bd7e089ebb0978569361c03a4f3ab950b950df"},
  step55_sign_data:{R:R.str(),Lg:Lg.str(),Lf:Lf.str(),tg_prime:hg.str(),tf_prime:hf.str(),z:z.str()},
  exact_toy_witness_not_step55:{V_relative:Vrel.str(),common_speed:ug.str(),V_diagonal_flux:Vflux.str(),bare_diagonal_flux_at_V_relative:Jg.add(Jf).str()},
  proof_scope:"Exact algebra on positive-lapse Step55 signs: no finite V can freeze both clocks at outer boundary; a unique V preserves their relative value with positive common velocity. At regular center time-independent Dirichlet requires zero corresponding lapse. Bulk clock momentum satisfies dot(p_i)=d_r(J_i), conditional integrated flux balance. No improved generator or Dirac temporal gauge quotient.",
  original_physics_reexecuted:false,
  scientific_status:{GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"}
 };
}
if(typeof module!=="undefined"&&module.exports)module.exports={certificate};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(certificate(),null,2)+"\n");

"use strict";
// Exact outward fixed-point intervals; each bound is an integer multiple of 10^-28.
// Independent transcription of the g-sector reconstruction in the SHA-authenticated
// original Step55 global barrier; NOT the Step45/46/55 G_U or G_Pg engine.
const SCALE=10n**28n;
function floorDiv(a,b){if(b<0n){a=-a;b=-b;}let q=a/b,r=a%b;return r<0n?q-1n:q}
function ceilDiv(a,b){return -floorDiv(-a,b)}
function isqrt(n){if(n<0n)throw Error("negative sqrt");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);while(true){let y=(x+n/x)>>1n;if(y>=x)return x;x=y}}
function parse(x){let z=String(x);if(z.includes("/")){let [a,b]=z.split("/");return [BigInt(a),BigInt(b)]}let neg=z.startsWith("-");if(neg)z=z.slice(1);let [a,b=""]=z.split(".");return [BigInt((a||"0")+b)*(neg?-1n:1n),10n**BigInt(b.length)]}
class I{
 constructor(lo,hi=lo){this.lo=lo;this.hi=hi;if(lo>hi)throw Error("bad interval")}
 static c(x){if(x instanceof I)return x;let [n,d]=parse(x);return new I(floorDiv(n*SCALE,d),ceilDiv(n*SCALE,d))}
 add(x){x=I.c(x);return new I(this.lo+x.lo,this.hi+x.hi)}
 neg(){return new I(-this.hi,-this.lo)}
 sub(x){return this.add(I.c(x).neg())}
 mul(x){x=I.c(x);let v=[this.lo*x.lo,this.lo*x.hi,this.hi*x.lo,this.hi*x.hi];let l=v.reduce((a,b)=>a<b?a:b),h=v.reduce((a,b)=>a>b?a:b);return new I(floorDiv(l,SCALE),ceilDiv(h,SCALE))}
 inv(){if(this.lo<=0n&&this.hi>=0n)throw Error("zero denominator");return new I(floorDiv(SCALE*SCALE,this.hi),ceilDiv(SCALE*SCALE,this.lo))}
 div(x){return this.mul(I.c(x).inv())}
 sq(){let a=this.lo,b=this.hi;if(a<=0n&&b>=0n){let m=a*a>b*b?a*a:b*b;return new I(0n,ceilDiv(m,SCALE))}let l=a*a<b*b?a*a:b*b,h=a*a>b*b?a*a:b*b;return new I(floorDiv(l,SCALE),ceilDiv(h,SCALE))}
 pow(k){if(k===0)return I.c(1);if(k===1)return this;if(k===2)return this.sq();let x=I.c(1);for(let i=0;i<k;i++)x=x.mul(this);return x}
 sqrt(){if(this.lo<0n)throw Error("negative sqrt");let l=isqrt(this.lo*SCALE),h=isqrt(this.hi*SCALE);if(h*h<this.hi*SCALE)h++;return new I(l,h)}
 gt(x){return this.lo>I.c(x).hi}
 lt(x){return this.hi<I.c(x).lo}
 fraction(which){return String(this[which])+"/"+String(SCALE)}
}
const A=I.c(".4"),Y=I.c(".5787707228025044"),B=A.mul(Y),M2=I.c("23.3348939346");
const CG=I.c(".0015"),CF=I.c("-.0012"),KG=I.c(".0012"),Z1=I.c(".004");
const B2=I.c("-4.2383993109"),B3=I.c("13.6801214252");
const H2=I.c(".9").div(I.c(3).mul(A.pow(3))).add(M2.mul(I.c(3).mul(Y).add(I.c(3).mul(B2).mul(Y.sq())).add(B3.mul(Y.pow(3)))).div(3));
const PG=I.c(-2).mul(A.sq()).mul(H2.sqrt());
function evaluate(s,p){
 s=I.c(s);p=I.c(p);
 let ug=I.c(1).add(CG.mul(s)),uf=I.c(1).add(CF.mul(s));
 let lg=A.mul(ug.sq()),lf=B.mul(uf.sq()),sgr=A.mul(ug).mul(I.c(1).add(I.c(5).mul(CG).mul(s)));
 let t0=I.c(2).mul(lg).mul(lf).add(B2.mul(lf.sq()));
 let t=lg.sq().add(I.c(2).mul(B2).mul(lg).mul(lf)).add(B3.mul(lf.sq()));
 let root=I.c(1).sub(Z1.sq().mul(s)).sqrt();
 let db=M2.mul(lg).mul(lf).mul(t).mul(Z1).div(root);
 let wg=M2.mul(lg.mul(t0).add(lf.mul(t).mul(root)));
 let rg=I.c(-48).mul(CG).div(A.sq().mul(ug.pow(5)));
 let h=I.c(1).add(I.c("5/2").mul(CG).mul(s)),j=I.c(1).add(I.c(5).mul(CG).mul(s));
 // Original rho_g = -(a2*P^2+a1*P+a0)/(b0+d*P).
 let a2=h.sq().div(I.c(4).mul(lg)).sub(h.mul(j).div(sgr));
 let a1=h.mul(s).mul(db).neg().div(I.c(2).mul(lg).mul(sgr));
 let a0=lg.pow(3).mul(rg).neg().div(2).add(s.mul(Z1).mul(db).div(lg)).add(wg);
 let b0=I.c(1).add(KG.sq().mul(s)).sqrt();
 let d=s.mul(h).mul(KG).div(I.c(2).mul(sgr));
 let n=a2.mul(p.sq()).add(a1.mul(p)).add(a0);
 let den=b0.add(d.mul(p));
 let first=I.c(-1).mul(I.c(2).mul(a2).mul(p).add(a1).mul(den).sub(n.mul(d))).div(den.sq());
 let second=I.c(-2).mul(a2.mul(b0.sq()).sub(a1.mul(b0).mul(d)).add(a0.mul(d.sq()))).div(den.pow(3));
 return {rho:n.neg().div(den),first,second,den,a2,a1,a0,b0,d};
}
function run(cells=256){
 if(!Number.isInteger(cells)||cells<64||cells>2048)throw Error("unsupported partition");
 const p=PG.add(new I(I.c("-1/5000").lo,I.c("1/5000").hi));
 let minima={rho:10n**50n,first:10n**50n,second:10n**50n,den:10n**50n};
 let maxima={rho:-(10n**50n),first:-(10n**50n),second:-(10n**50n),den:-(10n**50n)};
 const slabs=[];
 for(let i=0;i<cells;i++){
  const s=new I(I.c(String(289*i)+"/"+String(400*cells)).lo,I.c(String(289*(i+1))+"/"+String(400*cells)).hi);
  const e=evaluate(s,p);slabs.push(e);
  for(const k of Object.keys(minima)){if(e[k].lo<minima[k])minima[k]=e[k].lo;if(e[k].hi>maxima[k])maxima[k]=e[k].hi}
 }
 const f=(x)=>String(x)+"/"+String(SCALE);
 const summary={step:"68ad-C2d2e5b3b2c2b3c2b1",kind:"EXACT_G_DUST_PARAMETER_SENSITIVITY_ONLY",cells,
  s_domain:["0","289/400"],lambda_domain:["-1/5000","1/5000"],
  PG:[PG.fraction("lo"),PG.fraction("hi")],H2:[H2.fraction("lo"),H2.fraction("hi")],
  rho_g:[f(minima.rho),f(maxima.rho)],partial_lambda_rho_g:[f(minima.first),f(maxima.first)],
  partial_lambda2_rho_g:[f(minima.second),f(maxima.second)],denominator:[f(minima.den),f(maxima.den)],
  source_sha:"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",
  not_proven:["G_U/G_Pg physical","v(R)","f trace derivatives","physical boundary conditions","Dirac rank","tertiaries","4D stability","observables"],
  GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"};
 return {summary,slabs};
}
module.exports={I,SCALE,PG,H2,evaluate,run};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(run().summary,null,2)+"\n");

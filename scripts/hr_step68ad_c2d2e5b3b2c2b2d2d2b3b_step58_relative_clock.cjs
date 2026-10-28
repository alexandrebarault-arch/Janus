"use strict";
/* JANUS d2d2b3b: conditional Step58/Step55 relative-clock boundary diagnostic.
   This is NOT a full lapse existence or Dirac closure proof. */
const EXPECTED={
 temporal:"0c688d6648e16064b1eb4e8ad9c55e7b44a95947",
 step58:"802c23aebd41780d8c462f1aa1711707fe4ee88f",
 step55:"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",
 b3a:"edf4dd6c8ab3fea9579195c130b096dee7b7353a"
};
function F(x){if(Array.isArray(x))return x;let s=String(x).split("/");return [BigInt(s[0]),BigInt(s[1]||"1")];}
function lt(a,b){a=F(a);b=F(b);return a[0]*b[1]<b[0]*a[1];}
function add(a,b){a=F(a);b=F(b);return [a[0]*b[1]+b[0]*a[1],a[1]*b[1]];}
function mul(a,b){a=F(a);b=F(b);return [a[0]*b[0],a[1]*b[1]];}
function div(a,b){a=F(a);b=F(b);if(b[0]===0n)throw Error("zero");return [a[0]*b[1],a[1]*b[0]];}
function neg(a){a=F(a);return [-a[0],a[1]];}
function eq(a,b){return !lt(a,b)&&!lt(b,a);}
function audit(report,shas){
 let checks=0;function ok(v,label){checks++;if(!v)throw Error("FAIL "+label);}
 ok(shas.temporal===EXPECTED.temporal,"temporal SHA");
 ok(shas.step58===EXPECTED.step58,"Step58 SHA");
 ok(shas.step55===EXPECTED.step55,"Step55 SHA");
 ok(shas.b3a===EXPECTED.b3a,"b3a SHA");
 ok(report.kind==="CONDITIONAL_CONTINUUM_STEP58_ORIGINAL_ZEROTH_LAPSE_COEFFICIENTS","kind");
 ok(report.GATE_2B==="OPEN"&&report.JANUS_R==="NOT_VALIDATED","status");
 ok(report.cells.length===7&&report.total_leaves===225,"cell count");
 ok(eq(report.covered_r[0],"1/64")&&eq(report.covered_r[1],"1/32"),"coverage");
 let leaves=report.cells.flatMap(c=>c.leaves);
 ok(leaves.length===225,"leaf count");
 let prev="1/64",qualified=[],unresolved=0;
 for(let i=0;i<leaves.length;i++){
  const x=leaves[i],nl=F(x.N[0]),nh=F(x.N[1]),ml=F(x.M[0]),mh=F(x.M[1]);
  ok(eq(x.r[0],prev),"contiguous "+i);
  ok(lt(x.r[0],x.r[1]),"positive cell "+i);
  ok(lt("0",nl)&&lt(nh,neg("0"))===false,"N positive "+i);
  ok(lt(nl,nh),"N ordered "+i);
  ok(lt(mh,"0")&&lt(ml,mh),"M negative "+i);
  const upper=div(nh,neg(mh));
  if(lt(upper,"3/4"))qualified.push(i);else unresolved++;
  prev=x.r[1];
 }
 ok(eq(prev,"1/32"),"last endpoint");
 let spans=[];for(let i=0;i<qualified.length;){
  let j=i;while(j+1<qualified.length&&qualified[j+1]===qualified[j]+1)j++;
  spans.push({leaves:j-i+1,start:leaves[qualified[i]].r[0],end:leaves[qualified[j]].r[1]});i=j+1;
 }
 ok(qualified.length===154&&unresolved===71,"qualified 154, unresolved 71");
 ok(spans.length===2,"two spans");
 ok(spans[0].leaves===2&&eq(spans[0].start,"1/64")&&eq(spans[0].end,"225/14336"),"first span");
 ok(spans[1].leaves===152&&eq(spans[1].start,"37/1792")&&eq(spans[1].end,"1/32"),"second span");
 // Exact Step55 geometry on 1/64 <= r <= 1/32:
 // Lg=(2/5)(1+(3/2000)r²)^2, Lf=(2/5)q(1-(3/2500)r²)^2.
 const rmax=F("1/32"),smax=mul(rmax,rmax),q=F("5787707228025044/10000000000000000");
 const gg=add("1",mul("3/2000",smax)),ff=add("1",neg(mul("3/2500",smax)));
 const LgMax=mul("2/5",mul(gg,gg)),LfMin=mul(mul("2/5",q),mul(ff,ff));
 ok(lt(LgMax,"1/2"),"Lg<1/2");
 ok(lt(q,"1")&&lt("0",ff),"Lf<2/5<1/2");
 ok(lt("1/5",LfMin),"Lf>1/5");
 // sf=sqrt(1+(r/625)^2)<1001/1000, sg>=1.
 const sf2=add("1",mul(div(rmax,"625"),div(rmax,"625")));
 ok(lt(sf2,mul("1001/1000","1001/1000")),"sf<1001/1000");
 ok(eq(add(mul("3/4","1001/1000"),neg("1")),"-997/4000"),"numerator margin");
 ok(eq(mul("1/32",add(mul("3/2500","1/2"),mul("1/625","1/2"))),"7/160000"),"denominator upper");
 ok(eq(div("997/4000","7/160000"),"39880/7"),"Vrel/N bound");
 ok(eq(div(mul("39880/7","1/5"),"3/4"),"31904/21"),"f shift ratio bound");
 return {step:"68ad-C2d2e5b3b2c2b2d2d2b3b",assertions_passed:checks,assertions_failed:0,
  source_git_blobs:EXPECTED,original_step58_python_reexecuted:false,archive_leaves_checked:225,
  Step58_lapse_relation:"M/N=-A_N/A_M (conditional on lower lapse jets vanishing on full constrained shell)",
  certified_ratio_lt_3_over_4_leaves:154,ratio_not_certified_lt_3_over_4_leaves:71,
  certified_closed_spans:spans,
  implication_on_spans:"N,M>0 and Step55: Vrel/N < -39880/7; |Lf*Vrel|/M > 31904/21; hence f_tt=-M^2+Lf^2 Vrel^2>0 if ADM f shift is V",
  center_necessary_condition:"If tg'=tf'=0 and V finite, dot(tg-tf)(0)=N(0)-M(0); stationary relative clock at center requires M(0)=N(0). No Step58 ratio limit at r=0 certified.",
  caution:"f_tt>0 is coordinate-time vector spacelike, NOT loss of Lorentzian signature or physical inconsistency; 71 leaves not certified for rho<3/4, and the entire interval (0,1/64) is not covered.",
  scientific_status:{GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"}};
}
if(typeof module!=="undefined")module.exports={audit,EXPECTED};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),crypto=require("crypto"),path=require("path"),root=path.resolve(__dirname,"..");
 const files={temporal:"research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json",step58:"numerics/hr_step58_temporal_operator.py",step55:"numerics/hr_step55_global_barrier.py",b3a:"scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3a_clock_time_evolution.cjs"};
 let shas={};for(let [k,v] of Object.entries(files)){let bytes=fs.readFileSync(path.join(root,v));shas[k]=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\\0")).update(bytes).digest("hex");}
 let data=JSON.parse(fs.readFileSync(path.join(root,files.temporal),"utf8"));
 process.stdout.write(JSON.stringify(audit(data,shas),null,2)+"\\n");
}

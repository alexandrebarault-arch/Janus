"use strict";
// Adversarial exact rational regression for b3b2a. No physical Dirac rank claim.
function run(c){
 const {Q,Z,O,T,add,sub,mul,div,sq,eq,gt,build,original}=c;
 const checks=[];const ok=(name,condition)=>{if(!condition)throw Error("FAIL "+name);checks.push(name);};
 const make=(i)=>({L:[Q(2+i,5),Q(1+i,100)],H:[Q(2+i,5),Q(1,30)],P:[Q(-6-3*i,5),Q(1,20)],G:[Q(-3-3*i/2,5),Q(1,70)],rho:[Q(2,3)],Td:[Q(1,7)],Lf:[Q(1+i,4)],F:[Q(1+i,4)],m2:Q(5),mg:O,b1:O,b2:Q(-1,2),b3:Q(3)});
 // Use integral i=0,2,4 to avoid fractional BigInt input.
 for(const i of [0,2,4]){
   const q=make(i),r=Q(3+i,10),v=original(q,r),b=build(q);
   ok("D_factor_"+i,eq(v.D,v.factor));
   ok("K_positive_"+i,gt(v.K,Z));
   ok("c0_zero_"+i,eq(b.c0,Z));
 }
 let q=make(0),r=Q(1,1000);
 let bad={...q,G:[add(q.G[0],Q(1,10))]};
 let v=original(bad,r);
 ok("broken_chart_detected",!eq(v.b.c0,Z));
 ok("bad_chart_shift_near_unit",gt(div(sq(v.D),add(sq(v.D),sq(v.K))),Q(99,100)));
 let good={...q,P:[add(q.P[0],Q(1,5))],G:[add(q.G[0],Q(1,10))]};
 ok("matching_momenta_restores_c0",eq(build(good).c0,Z));
 ok("dust_irrelevant_to_c0",eq(build({...q,rho:[Q(900)],Td:[Q(12)]}).c0,Z));
 ok("zero_denominator_rejected",(()=>{try{Q(1,0);return false;}catch{return true;}})());
 return {wrapper_passed:checks.length,wrapper_failed:0,checks};
}
module.exports={run};
if(typeof require!=="undefined"&&require.main===module){
 const c=require("../scripts/hr_step68ad_c2d2e5b3b2a_center_parity_chart.cjs");
 console.log(JSON.stringify(run(c),null,2));
}

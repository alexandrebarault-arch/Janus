"use strict";
// Adversarial regression tests for the exact centre-leading-jet construction.
const c=require("../scripts/hr_step68ad_c2d2e5b3b2b1_center_constraint_jets.cjs");
const {Q,add,sub,eq,construct,residuals,example,runTests}=c;
function run(){
 const checks=[];const ok=(n,v)=>{if(!v)throw Error("FAIL "+n);checks.push(n);};
 const x=construct(example()),e=Q(1,1234);
 ok("core_replay",runTests().failed===0);
 ok("all_central_zero",Object.entries(residuals(x)).every(([k,v])=>k==="Dg3"||k==="Df3"||eq(v,Q(0))));
 ok("different_Pg_preserves_shell",eq(residuals(construct({...example(),Pg:add(x.Pg,e)})).C2,Q(0)));
 ok("different_z1_preserves_shell",eq(residuals(construct({...example(),z1:add(x.z1,e)})).Fz3,Q(0)));
 ok("different_Pg1_preserves_shell",eq(residuals(construct({...example(),Pg1:add(x.Pg1,e)})).Fz3,Q(0)));
 ok("different_U1_preserves_shell",eq(residuals(construct({...example(),U1:add(x.U1,e)})).Ddiag3,Q(0)));
 ok("change_cg_rebalances_Hg",eq(residuals(construct({...example(),cg:add(x.cg,e)})).Hg2,Q(0)));
 ok("change_cf_rebalances_Hf",eq(residuals(construct({...example(),cf:add(x.cf,e)})).Hf2,Q(0)));
 ok("broken_Psg0_detected",!eq(residuals({...x,Psg0:sub(x.Psg0,e)}).Dg1,Q(0)));
 ok("broken_Psf0_detected",!eq(residuals({...x,Psf0:sub(x.Psf0,e)}).Df1,Q(0)));
 ok("broken_Psg1_detected",!eq(residuals({...x,Psg1:sub(x.Psg1,e)}).Fz3,Q(0)));
 ok("broken_Psf1_detected",!eq(residuals({...x,Psf1:sub(x.Psf1,e)}).Ddiag3,Q(0)));
 return {passed:checks.length,failed:0,checks};
}
module.exports={run};
if(require.main===module)console.log(JSON.stringify(run(),null,2));

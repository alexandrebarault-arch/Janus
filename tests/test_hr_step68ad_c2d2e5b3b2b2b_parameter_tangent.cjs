"use strict";
const core=require("../scripts/hr_step68ad_c2d2e5b3b2b2b_parameter_tangent.cjs");
function runTests(){
 let names=[];const check=(v,name)=>{if(!v)throw Error("FAILED "+name);names.push(name);};
 const q=core.q,c=core.c,base=q("-2/5"),h=q("1/101");
 const report=core.run();
 check(report.failed===0,"core_zero_fail");
 check(report.passed>=30,"core_checks_executed");
 check(c.gt(0),"nonzero_physical_center_parameter_slope");
 check(core.center(base.add(h)).sub(core.center(base)).eq(c.mul(h)),"exact_finite_Pg_center_shift");
 const v=core.tangent();
 check(v[0].eq(c),"indicial_regular_tangent");
 check(v[1].eq(q("3/11").mul(c).add(q("5/13")).div(5)),"first_linearized_jet");
 const u=core.series(base),up=core.series(base.add(h));
 check(up[8].sub(u[8]).eq(h.mul(v[8])),"eighth_jet_exact_linearized");
 let g1=core.radial(q("9/25"),base),g2=core.radial(q("9/25"),base.add(h));
 check(g1.Dg.eq(g2.Dg),"radial_shift_source_unchanged");
 check(g1.Dg.eq("9/10"),"synthetic_Dg_exact");
 check(report.status.JANUS_R==="NOT_VALIDATED","no_physical_validation");
 return {passed:names.length,failed:0,checks:names};
}
if(typeof module!=="undefined")module.exports={runTests};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(runTests(),null,2));

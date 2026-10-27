"use strict";
// Independent command: node tests/test_hr_step68ad_c2d2e5b3b1_shift_tangent.cjs
const assert=require("node:assert/strict");
const a=require("../scripts/hr_step68ad_c2d2e5b3b1_shift_tangent.cjs");
const report=a.runTests();
assert.equal(report.checks_failed,0);
assert.equal(report.checks_passed,18);
assert.equal(report.exact_sample.transverse_dz,"48/125");
assert.equal(report.exact_sample.transverse_Hessian_Q,"81/250");
assert.equal(report.exact_sample.pLg_r2_dz_depsilon,"-512/1875");
assert.equal(report.exact_sample.pLg_r2_Hessian_Q,"512/3125");
assert.equal(report.exact_sample.off_shell_ratio_at_r_1_over_100000,"-400");
assert.equal(report.GATE_2B,"OPEN");
assert.equal(report.JANUS_R,"NOT_VALIDATED");
console.log("18 exact rational assertions PASS; 8 independent report checks PASS");

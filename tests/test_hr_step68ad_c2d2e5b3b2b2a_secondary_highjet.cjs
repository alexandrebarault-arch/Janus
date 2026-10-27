"use strict";
// Adversarial checks independent of the core's internal assertion list.
const m=require("../scripts/hr_step68ad_c2d2e5b3b2b2a_secondary_highjet.cjs");
let n=0;function ok(x,msg){if(!x)throw Error("FAIL "+msg);n++;}
const x=m.physical(),t=m.tests();
ok(t.passed===12,"core assertion count");ok(t.failed===0,"core no failures");
ok(m.eq(m.mul(m.q(7),x.cw),x.lead),"factor seven");
ok(!m.eq(m.mul(m.q(6),x.cw),x.lead),"negative control factor six");
ok(!m.eq(m.mul(m.q(8),x.cw),x.lead),"negative control factor eight");
ok(x.at[0]>0n&&x.cw[0]<0n,"physical chart signs");
ok(t.interpretation.includes("C(r) nonzero"),"no false tangency");
ok(t.limits.includes("not a physical Dirac tangent"),"scope");
ok(t.GATE_2B==="OPEN"&&t.JANUS_R==="NOT_VALIDATED","gate");
console.log(JSON.stringify({step:t.step,wrapper_passed:n,wrapper_failed:0}));

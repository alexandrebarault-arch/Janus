"use strict";
const m=require("../scripts/hr_step68ad_c2d2e5b3b2c2b3c2b1_gdust_sensitivity.cjs");
const I=m.I;let count=0;
function ok(cond,msg){if(!cond)throw Error("FAIL "+msg);count++}
function nearContains(i,x){return i.lo<=I.c(x).lo&&i.hi>=I.c(x).hi}
ok(m.PG.gt("-0.764"),"Pg lower");ok(m.PG.lt("-0.763"),"Pg upper");
ok(m.H2.gt("5.69"),"H2 positive");ok(m.H2.lt("5.70"),"H2 upper");
const c=m.run(256);ok(c.slabs.length===256,"256 slabs");
for(let k=0;k<256;k++){
 const e=c.slabs[k];
 ok(e.den.gt(".999"),"den "+k);
 ok(e.rho.gt(".88"),"rho positive "+k);
 ok(e.first.gt("-2.88"),"first lower "+k);
 ok(e.first.lt("-2.85"),"first upper "+k);
 ok(e.second.gt("3.74"),"convex lower "+k);
 ok(e.second.lt("3.77"),"convex upper "+k);
}
const e0=m.evaluate(I.c(0),m.PG);
ok(e0.a1.lo===0n&&e0.a1.hi===0n,"linear coefficient center zero");
ok(e0.d.lo===0n&&e0.d.hi===0n,"den derivative center zero");
ok(e0.a2.lt("-1.874"),"center quadratic coefficient");
ok(e0.a2.gt("-1.876"),"center quadratic coefficient lower");
ok(e0.first.gt("-2.87")&&e0.first.lt("-2.86"),"center slope");
ok(e0.second.gt("3.749")&&e0.second.lt("3.751"),"center convexity");
const d=m.run(512);ok(d.slabs.length===512,"512 slab crosscheck");
ok(d.slabs.every(x=>x.first.lt("-2.85")&&x.second.gt("3.74")),"512 signs");
ok(c.summary.GATE_2B==="OPEN"&&c.summary.JANUS_R==="NOT_VALIDATED","status");
ok(c.summary.not_proven.includes("G_U/G_Pg physical"),"scope");
module.exports={count,summary:c.summary};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify({passed:count,failed:0,step:c.summary.step}));

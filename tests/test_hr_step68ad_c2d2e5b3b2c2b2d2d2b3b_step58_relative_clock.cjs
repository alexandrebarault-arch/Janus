"use strict";
const assert=require("assert"),fs=require("fs"),path=require("path"),crypto=require("crypto");
const {audit,EXPECTED}=require("../scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3b_step58_relative_clock.cjs");
const root=path.resolve(__dirname,"..");
const files={temporal:"research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json",step58:"numerics/hr_step58_temporal_operator.py",step55:"numerics/hr_step55_global_barrier.py",b3a:"scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3a_clock_time_evolution.cjs"};
const shas={};for(const [k,v] of Object.entries(files)){let bytes=fs.readFileSync(path.join(root,v));shas[k]=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");}
const data=JSON.parse(fs.readFileSync(path.join(root,files.temporal),"utf8"));
const cert=audit(data,shas);let tests=0;function ok(v){assert(v);tests++;}
ok(cert.archive_leaves_checked===225);ok(cert.certified_ratio_lt_3_over_4_leaves===154);
ok(cert.ratio_not_certified_lt_3_over_4_leaves===71);
ok(cert.certified_closed_spans.length===2);
ok(cert.scientific_status.GATE_2B==="OPEN");
ok(cert.scientific_status.JANUS_R==="NOT_VALIDATED");
ok(cert.source_git_blobs.temporal===EXPECTED.temporal);
function reject(mut){const x=structuredClone(data);mut(x);assert.throws(()=>audit(x,shas));tests++;}
reject(x=>x.cells[0].leaves[0].M[1]="1/2");
reject(x=>x.cells[0].leaves[0].N[0]="-1/2");
reject(x=>x.cells[0].leaves[0].r[0]="0");
reject(x=>x.cells[0].leaves[0].N[1]="100");
assert.throws(()=>audit(data,{...shas,step58:"tampered"}));tests++;
console.log(JSON.stringify({test_assertions_passed:tests,failed:0,main_certificate_assertions:cert.assertions_passed}));

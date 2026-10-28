"use strict";
/* Adversarial replay: four negative cases; not independent of the primary proof. */
const {audit,EXPECTED}=require("../scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c1_center_boundary_layer.cjs");
const fs=require("fs"),path=require("path"),crypto=require("crypto");
const root=path.resolve(__dirname,"..");
const files={temporal:"research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json",step58:"numerics/hr_step58_temporal_operator.py",step55:"numerics/hr_step55_global_barrier.py"};
const shas={};for(let [k,p] of Object.entries(files)){const b=fs.readFileSync(path.join(root,p));shas[k]=crypto.createHash("sha1").update(Buffer.from("blob "+b.length+"\0")).update(b).digest("hex");}
const cert=JSON.parse(fs.readFileSync(path.join(root,files.temporal),"utf8"));
const valid=audit(cert,shas);if(valid.assertions_failed!==0)throw Error("unexpected audit failure");
let rejected=0;function reject(x,y){try{audit(x,y)}catch(e){rejected++;return;}throw Error("forgery not rejected");}
const clone=x=>JSON.parse(JSON.stringify(x));
let x=clone(cert);x.cells[0].leaves[0].N[1]="999";reject(x,shas);
x=clone(cert);x.cells[0].leaves.shift();reject(x,shas);
x=clone(cert);x.cells[0].leaves[0].r[0]="0";reject(x,shas);
reject(cert,{...shas,step58:"0000000000000000000000000000000000000000"});
if(rejected!==4)throw Error("negative guards failed");
process.stdout.write(JSON.stringify({assertions:valid.assertions_passed,negative_rejected:rejected,status:"PASS"})+"\n");

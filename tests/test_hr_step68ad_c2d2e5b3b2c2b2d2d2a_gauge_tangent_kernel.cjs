"use strict";
// Replay of the exact polynomial certificate; NOT an independent physical engine.
const assert=require("node:assert/strict");
const {run}=require("../scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2a_gauge_tangent_kernel.cjs");
const c=run();
assert.equal(c.passed,211);assert.equal(c.failed,0);
assert.equal(c.gate,"GATE_2B OPEN");assert.equal(c.janus,"JANUS_R NOT_VALIDATED");
console.log("PASS 211 exact BigInt assertions; 4 wrapper guards; 0 FAIL (replay only)");

"use strict";
/* Reproducible Node regression; replays 57 rational assertions in the source. */
const assert=require("node:assert/strict");
const {certificate}=require("../scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b2_clock_boundary_flux.cjs");
const c=certificate();
assert.equal(c.assertions_passed,57);
assert.equal(c.assertions_failed,0);
assert.equal(c.exact_rational_enclosures.r,"17/20");
assert.equal(c.exact_rational_enclosures.z,"17/5000");
assert.equal(c.boundary_cases.length,7);
assert.equal(c.boundary_cases.find(x=>x.name==="fix both at center").remaining,0);
assert.equal(c.boundary_cases.find(x=>x.name==="fix tg-tf at either boundary").remaining,1);
assert.equal(c.scientific_status.GATE_2B,"OPEN");
assert.equal(c.scientific_status.JANUS_R,"NOT_VALIDATED");
assert.equal(c.original_physics_reexecuted,false);
console.log("PASS: 57 rational source assertions replayed; 10 regression guards (not independent).");

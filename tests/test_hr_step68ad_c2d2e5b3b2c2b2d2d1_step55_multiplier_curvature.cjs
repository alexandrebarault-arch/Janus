'use strict';
const assert=require('assert');
const {run}=require('../scripts/hr_step68ad_c2d2e5b3b2c2b2d2d1_step55_multiplier_curvature.cjs');
const certificate=run();
assert.strictEqual(certificate.assertions_passed,35);
assert.strictEqual(certificate.assertions_failed,0);
assert.strictEqual(certificate.status.GATE_2B,'OPEN');
assert.strictEqual(certificate.status.JANUS_R,'NOT_VALIDATED');
console.log('JANUS d2d1: 35 exact BigInt assertions PASS, 0 FAIL; wrapper replay PASS');

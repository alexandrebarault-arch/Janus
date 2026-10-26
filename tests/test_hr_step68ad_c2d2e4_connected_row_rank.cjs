'use strict';
// Synthetic adversarial tests (11 cases) are embedded in the production module.
// Execute with Node: node tests/test_hr_step68ad_c2d2e4_connected_row_rank.cjs
const {selfTest}=require('../scripts/hr_step68ad_c2d2e4_connected_row_rank.cjs');
const count=selfTest();
if(count!==11)throw Error('unexpected test count '+count);
console.log(count+' tests passed');

'use strict';
const x=require('../scripts/hr_step68ad_c2d2e5b3b2c2b3c2b2a_variational_regularization.cjs');
function run(){
 let n=0;
 const check=(p,msg)=>{n++;if(!p)throw Error('FAIL '+n+': '+msg);};
 const equal=(a,b,msg)=>check(x.eq(a,b),msg);
 const q=x.Q;
 equal(x.v0,q(274023815147385251710689588080861n,40000000000000000000000000000000000n),'physical central v0');
 check(x.lt(q(0),x.v0),'positive central sensitivity');
 equal(x.GU0,q(-1),'center G_U');
 equal(x.GP0,x.mul(q(3),x.v0),'center G_P');
 equal(x.add(x.mul(q(-3),x.v0),x.GP0),q(0),'regular center cancellation');
 const a=[q(0),q(1,10)],b=[q(0),q(1,100)];
 const v=x.series(a,b,10);
 equal(v[1],x.div(x.add(x.mul(a[1],x.v0),b[1]),q(5)),'first jet denominator five');
 equal(v[2],x.div(x.mul(a[1],v[1]),q(7)),'second jet denominator seven');
 for(let j=2;j<=10;j++)equal(v[j],x.div(x.mul(a[1],v[j-1]),q(2*j+3)),'recurrence '+j);
 for(const [i,r] of x.residual(a,b,v).entries())equal(r,q(0),'polynomial residual degree '+i);
 const noA=x.series([q(0)],[q(0),q(1)],5);
 equal(noA[1],q(1,5),'exact forcing saturation');
 for(let j=2;j<=5;j++)equal(noA[j],q(0),'no higher terms '+j);
 const e0=x.enclosure(q(0),q(0));
 equal(e0.bound,q(0),'zero forcing zero deviation');
 check(e0.positive,'zero forcing positive');
 const e1=x.enclosure(q(0),q(1));
 equal(e1.bound,x.div(x.smax,q(5)),'sharp alpha zero majorant');
 check(!e1.positive,'large beta cannot certify sign');
 const e2=x.enclosure(q(1,10),q(1,100));
 check(e2.positive,'small synthetic alpha beta sufficient');
 check(x.lt(q(0),e2.bound),'majorant nonzero');
 check(x.lt(e2.x,q(1)),'majorant denominator positive');
 check(x.lt(e2.bound,x.v0),'strict v positivity if hypotheses');
 check(x.certificate().GATE_2B==='OPEN','gate open');
 check(x.certificate().JANUS_R==='NOT_VALIDATED','not validated');
 check(x.certificate().classification.includes('CONDITIONAL'),'conditional label');
 check(x.certificate().hypotheses_not_checked.length===5,'all blockers');
 for(const [aa,bb] of [[q(-1),q(0)],[q(0),q(-1)],[q(3),q(0)]]){
  let rejected=false;try{x.enclosure(aa,bb)}catch(_){rejected=true;}
  check(rejected,'reject invalid interval hypothesis');
 }
 return {passed:n,failed:0,step:x.certificate().step};
}
module.exports={run};
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(run()));

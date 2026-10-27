'use strict';
const assert=require('assert');
const x=require('../scripts/hr_step68ad_c2d2e5b3b2c2b3a_nonibp_boundary.cjs');
let passed=0;
function ok(v,msg){assert.ok(v,msg);passed++;}
const q=x.q,eq=x.eq,mul=x.mul,add=x.add,sub=x.sub;
const t=x.trace(),R=x.R;
ok(eq(t.a,q('92730563/128000000')),'outer pLg');
ok(eq(t.d,q('2734739/1600000')),'outer pLg prime');
ok(eq(t.u0,q('274023815147385251710689588080861/40000000000000000000000000000000000')),'U0 sensitivity');
ok(eq(t.z,q('17/5000')),'nonzero physical shift');
ok(eq(t.ratio,q('2505421686285156250000000000/1444418923561876775155324829')),'outer Lg/Lf');
ok(eq(x.boundarySlope(),q('-6226606039693438177138189375297828359/924428111079601136099407890560000000000')),'N=M=1 exact boundary slope');
ok(eq(x.boundarySlope(R,q('1/2'),q('1/2')),mul(q('1/2'),x.boundarySlope())),'positive lapse bound');
ok(x.boundarySlope().n<0n,'strict negative for positive lapses');
ok(x.boundarySlope(R,q('1'),q('0')).n<0n,'g lapse positive');
ok(x.boundarySlope(R,q('0'),q('1')).n<0n,'f lapse positive');
ok(eq(x.boundarySlope(R,q('0'),q('0')),q('0')),'compact lapse endpoint');
ok(eq(x.boundary(q('0'),q('-1')),q('0')),'center bounded lapse B=0');
ok(eq(add(t.a,mul(t.robin_beta_for_alpha_one,t.d)),q('0')),'unique Robin slope');
ok(eq(t.robin_beta_for_alpha_one,q('-5454739/12869360')),'exact Robin fraction');
for(const lam of ['1/5000','-1/5000','1/100000','0']){
 const p0=q('-1'),delta=q(lam);
 ok(eq(sub(x.boundary(R,add(p0,delta)),x.boundary(R,p0)),mul(delta,x.boundarySlope())),'finite difference '+lam);
}
for(const r of ['1/5','17/20','3/4']){
 const a=x.momentumTermIdentity(q(r),q('-1'),q('1'),q('1/2'));
 ok(eq(sub(a.original,a.ibp),a.totalDerivative),'original minus IBP product derivative '+r);
}
ok(x.profile(R).Lg.n>0n && x.profile(R).Lf.n>0n,'positive metric factors');
ok(x.profile(R).z.n>0n,'nonzero shift at outer boundary');
ok(x.SOURCE_SHA['numerics/hr_step45_exact_physical_ward.py']==='66aa43841dccfe4a5d586a49be9c10af3a67a10e','original SHA reference');
ok(x.certificate().GATE_2B==='OPEN' && x.certificate().JANUS_R==='NOT_VALIDATED','no physical validation');
if(require.main===module)console.log('PASS '+passed+' exact BigInt assertions, 0 FAIL');
module.exports={passed};

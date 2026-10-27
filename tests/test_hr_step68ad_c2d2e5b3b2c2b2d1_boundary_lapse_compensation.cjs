'use strict';
const c=require('../scripts/hr_step68ad_c2d2e5b3b2c2b2d1_boundary_lapse_compensation.cjs');
const {q,add,neg,sub,mul,div,cmp,eq,Z,O,LAMBDA,H2,pgBounds,z,a,ratio,Ag,Af,za,Cg,Cf,boundary,compensatingN,compensationSlope,dBdl,counterterm,certificate}=c;
let n=0;function ok(v,msg){n++;if(!v)throw Error('FAIL '+n+': '+msg);}
const lt=(x,y)=>cmp(x,y)<0,gt=(x,y)=>cmp(x,y)>0;
ok(gt(H2,q('5')),'H2>5');ok(lt(H2,q('6')),'H2<6');
ok(gt(a,Z),'a>0');ok(lt(a,q('3/4')),'a<3/4');
ok(gt(z,Z),'z>0');ok(lt(z,q('1/250')),'z<1/250');
ok(gt(ratio,O),'q>1');ok(lt(ratio,q('2')),'q<2');
ok(gt(Ag,q('2/3')),'Ag>2/3');ok(gt(Af,Z),'Af>0');
ok(gt(za,Z),'za>0');ok(lt(mul(za,add(O,ratio)),q('9/1000')),'za(1+q)<9/1000');
const lam=[neg(LAMBDA),Z,LAMBDA];
for(const P of [...pgBounds,q('-3/4')]){
 for(const l of lam){
  ok(lt(add(P,l),Z),'Pg+lambda<0');
  ok(gt(Cg(P,l),Ag),'Cg>Ag');
  ok(gt(Cf(P,l),Af),'Cf>Af');
  const N=compensatingN(P,l);
  ok(gt(N,q('999/1000')),'compensated N lower');
  ok(lt(N,q('1001/1000')),'compensated N upper');
  ok(eq(boundary(P,l,N,O),boundary(P,Z,O,O)),'exact constant B');
  ok(eq(add(mul(Cg(P,l),compensationSlope(P,l)),dBdl(N,O)),Z),'chain rule exact zero');
  ok(eq(add(boundary(P,l,O,O),counterterm(P,l,O,O)),Z),'counterterm identity');
 }
}
for(const P of [q('-3/4'),q('-2/3')]){
 for(const l of lam){
  ok(eq(sub(boundary(P,l,q('2'),O),boundary(P,l,O,O)),Cg(P,l)),'d_N B exact');
  ok(eq(sub(boundary(P,l,O,q('2')),boundary(P,l,O,O)),Cf(P,l)),'d_M B exact');
  ok(eq(sub(Cg(P,l),Cg(P,Z)),neg(mul(za,l))),'mixed derivative N');
  ok(eq(sub(Cf(P,l),Cf(P,Z)),neg(mul(mul(za,ratio),l))),'mixed derivative M');
 }
}
ok(!eq(dBdl(O,O),dBdl(q('2'),O)),'no lapse-independent lambda-only counterterm for independent N');
ok(!eq(neg(za),Z),'momentum-lapse mixed derivative nonzero');
ok(!eq(neg(mul(za,ratio)),Z),'second mixed derivative nonzero');
ok(gt(compensationSlope(q('-3/4'),Z),Z),'positive lapse slope');
ok(eq(compensatingN(q('-3/4'),Z),O),'N(0)=1');
ok(certificate().GATE_2B==='OPEN'&&certificate().JANUS_R==='NOT_VALIDATED','no false validation');
module.exports={run:()=>n};
if(require.main===module)process.stdout.write('PASS '+n+' exact rational assertions; FAIL 0\n');

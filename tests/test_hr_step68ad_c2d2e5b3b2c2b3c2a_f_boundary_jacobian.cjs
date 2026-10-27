'use strict';
const {Q,jacobian,dualCheck,physicalChiBounds,certificate}=require('../scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs');
const q=Q.of;let n=0;
function check(cond,message){if(!cond)throw Error(message);n++;}
const p={R:'17/20',mf:'0.011836458045964912',Lf:'0.23110702776990028',Sfr:'0.230304853112166',kf:'-0.0016',U:'-0.005',V:'-0.010',beta:'1.000001',Dbar:'0.003',Wfbar:'0.09',Rf:'0.3',z1:'0.004'};
const c=jacobian(p);
check(c.den.cmp(1)>0,'positive f denominator');
check(c.chi.cmp(0)<0,'chi negative on test point');
for(const [du,dv] of [['1','0'],['0','1'],['1/3','-2/7'],['-1/17','3/11'],['0','0']]){
 const z=dualCheck(p,du,dv);
 check(z.pf.cmp(z.expectedPf)===0,'exact pf dual derivative');
 check(z.pSf.cmp(z.expectedPSf)===0,'exact pSf dual derivative');
}
const b=physicalChiBounds();
check(q(b.U_lower).cmp(q(b.U_upper))<0,'U ordered');
check(q(b.D_lower).cmp(1)>0,'D lower');
check(q(b.D_upper).cmp(q(b.D_lower))>0,'D ordered');
check(q(b.chi_lower).cmp(q('-21/25'))>0,'chi lower strict');
check(q(b.chi_upper).cmp(q('-71/100'))<0,'chi upper strict');
check(q(b.chi_lower).cmp(q(b.chi_upper))<0,'chi bounds ordered');
const r=certificate();
check(r.rank_of_formal_trace_map===2,'rank two from nonzero R');
check(r.v_R==='NOT_COMPUTED','no fabricated sensitivity');
check(r.GATE_2B==='OPEN'&&r.JANUS_R==='NOT_VALIDATED','science gates');
check(q('0.0002').cmp(q('1/5000'))===0,'parameter radius');
check(q('-0.84').cmp(q('-21/25'))===0,'lower decimal exact');
check(q('-0.71').cmp(q('-71/100'))===0,'upper decimal exact');
console.log('PASS '+n+' exact assertions; FAIL 0');

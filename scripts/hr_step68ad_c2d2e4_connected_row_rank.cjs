'use strict';
// JANUS 68ad-C2d2e4: independent exact-rational audit of FOUR published interval certificates.
// Usage: node scripts/hr_step68ad_c2d2e4_connected_row_rank.cjs <repo-root>
// No physical Hamiltonian re-execution; full Dirac rank remains UNPROVED.
const EXPECTED={inner:['1/64','1/32',225],s:['1/32','1/16',1006],q:['1/16','1/8',314],p:['1/8','17/20',265]};
const FILES={
 inner:['research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json','0c688d6648e16064b1eb4e8ad9c55e7b44a95947'],
 s:['research/reports/gate2b-step68s-inner-1over32-to-1over16-cover.json','e890998a2f925f881ab85b60a9027e5828e35ed5'],
 q:['research/reports/gate2b-step68q-inner-1over16-to-1over8-cover.json','82f5d046cd0ca0c342adabe8b8f13cfc3f99308d'],
 p:['research/reports/gate2b-step68p-adaptive-outer-cover.json','978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6']
};
function rat(x){const v=String(x).split('/');if(v.length>2)throw Error('bad rational');let n=BigInt(v[0]),d=BigInt(v[1]||'1');if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}return [n,d];}
function cmp(a,b){const v=a[0]*b[1]-b[0]*a[1];return v<0n?-1:v>0n?1:0;}
function div(a,b){if(!b[0])throw Error('zero divisor');let n=a[0]*b[1],d=a[1]*b[0];return d<0n?[-n,-d]:[n,d];}
function neg(a){return [-a[0],a[1]];}
function sq(a){return [a[0]*a[0],a[1]*a[1]];}
function show(a){return a[0].toString()+'/'+a[1].toString();}
function check(ok,msg){if(!ok)throw Error(msg);}
function audit(src){
 let all=[],counts={};
 for(const k of ['inner','s','q','p']){
  const d=src[k];check(d&&typeof d==='object','missing '+k);
  check(d.GATE_2B==='OPEN'&&d.JANUS_R==='NOT_VALIDATED','invalid scientific status '+k);
  if(k==='inner')check(d.N_positive_continuum===true&&d.M_negative_continuum===true,'uncertified inner');
  else{check(d.status==='CERTIFIED','uncertified '+k);check(Array.isArray(d.failures)&&d.failures.length===0,'failures '+k);check(Array.isArray(d.queue)&&d.queue.length===0,'queue '+k);}
  const cells=k==='inner'?d.cells.flatMap(c=>c.leaves):d.certified;
  check(cells.length===EXPECTED[k][2],'count '+k);counts[k]=cells.length;
  let prev=rat(EXPECTED[k][0]);
  for(let i=0;i<cells.length;i++){
   const c=cells[i],rr=c.r||[c.lo,c.hi],r0=rat(rr[0]),r1=rat(rr[1]);
   const [nl,nu]=c.N.map(rat),[ml,mu]=c.M.map(rat);
   check(cmp(r0,prev)===0,'gap/overlap '+k+':'+i);
   check(cmp(r0,r1)<0,'invalid radial cell '+k+':'+i);
   check(cmp(nl,nu)<=0&&cmp(ml,mu)<=0,'inverted box '+k+':'+i);
   check(cmp(nl,rat('0'))>0&&cmp(mu,rat('0'))<0,'sign failure '+k+':'+i);
   all.push({k,i,r0,r1,nl,nu,ml,mu});prev=r1;
  }
  check(cmp(prev,rat(EXPECTED[k][1]))===0,'wrong end '+k);
 }
 let low=null,high=null,lowAt=null,highAt=null,normN=null,normM=null;
 for(const c of all){
  const a=div(c.nl,neg(c.ml)),b=div(c.nu,neg(c.mu));
  const nn=div(c.nl,sq(c.r1)),mm=div(c.mu,sq(c.r1));
  if(low===null||cmp(a,low)<0){low=a;lowAt={band:c.k,index:c.i,r:[show(c.r0),show(c.r1)]};}
  if(high===null||cmp(b,high)>0){high=b;highAt={band:c.k,index:c.i,r:[show(c.r0),show(c.r1)]};}
  if(normN===null||cmp(nn,normN)<0)normN=nn;
  if(normM===null||cmp(mm,normM)>0)normM=mm;
 }
 check(cmp(low,rat('1/50000'))>0&&cmp(high,rat('14'))<0,'lapse ratio uniform bound failed');
 check(cmp(normN,rat('7/20'))>0&&cmp(normM,rat('-546'))<0,'normalized row uniform bound failed');
 return {status:'CONDITIONAL_LOCAL_ROW_RANK_ONLY',GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED',
  coverage:['1/64','17/20'],counts,total:all.length,
  M_over_N_lower:show(low),M_over_N_upper:show(high),lower_at:lowAt,upper_at:highAt,
  min_AN_over_r2_lower:show(normN),max_AM_over_r2_upper:show(normM),
  simple_bounds:{M_over_N:['1/50000','14'],AN_over_r2_lower:'7/20',AM_over_r2_upper:'-546'},
  full_Dirac_rank:'NOT_PROVED',boundary_compatible_lapses:'NOT_PROVED',
  singular_charts:'NOT_PROVED',oracle_independent_non_IBP:'NOT_PROVED',
  interpretation:'Conditional audit of four SHA-pinned original Step58 reports; no independent Poisson/Hamiltonian oracle.'};
}
function selfTest(){
 let n=0;const assert=(v,msg)=>{if(!v)throw Error('test '+n+': '+msg);};
 const make=()=>{let s={};for(const k of Object.keys(EXPECTED)){let [start,end,count]=EXPECTED[k],a=rat(start),b=rat(end);
  const d=a[1]*b[1]*BigInt(count),base=a[0]*b[1]*BigInt(count),delta=b[0]*a[1]-a[0]*b[1];
  const cell=i=>({r:[show([base+delta*BigInt(i),d]),show([base+delta*BigInt(i+1),d])],N:['1','2'],M:['-1000','-900']});
  const arr=Array.from({length:count},(_,i)=>cell(i));
  s[k]=k==='inner'?{GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED',N_positive_continuum:true,M_negative_continuum:true,cells:[{leaves:arr}]}:
   {GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED',status:'CERTIFIED',failures:[],queue:[],certified:arr.map(x=>({lo:x.r[0],hi:x.r[1],N:x.N,M:x.M}))};
 }return s;};
 const pass=()=>{n++;assert(audit(make()).total===1810,'synthetic valid cover');};pass();
 const bad=(change)=>{n++;let s=make();change(s);let rejected=false;try{audit(s)}catch(e){rejected=true;}assert(rejected,'invalid data accepted');};
 bad(s=>{s.inner.cells[0].leaves[0].N[0]='-1';});
 bad(s=>{s.inner.cells[0].leaves[0].M[1]='0';});
 bad(s=>{s.inner.cells[0].leaves[1].r[0]='1/10';});
 bad(s=>{s.s.certified.pop();});
 bad(s=>{s.q.queue=['unresolved'];});
 bad(s=>{s.p.status='INCOMPLETE';});
 bad(s=>{s.inner.N_positive_continuum=false;});
 bad(s=>{s.p.certified[0].N=['2','1'];});
 bad(s=>{s.s.certified[0].N[0]='1/0';});
 bad(s=>{s.inner.GATE_2B='CLOSED';});
 return n;
}
module.exports={audit,selfTest,rat,cmp,div,show,FILES};
if(typeof require==='function'&&require.main===module){
 const fs=require('fs'),path=require('path'),crypto=require('crypto'),root=process.argv[2]||'.',data={};
 for(const [k,[p,sha]] of Object.entries(FILES)){const bytes=fs.readFileSync(path.join(root,p));
  const got=crypto.createHash('sha1').update(Buffer.concat([Buffer.from('blob '+bytes.length+'\0'),bytes])).digest('hex');
  check(got===sha,'Git SHA mismatch '+p);data[k]=JSON.parse(bytes.toString('utf8'));}
 const result=audit(data);console.log(JSON.stringify({self_tests:selfTest(),...result},null,2));
}

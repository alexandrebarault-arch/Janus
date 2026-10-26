'use strict';
const a=require('../scripts/hr_step68ad_c2d2e5a_original_boundary.cjs');
function run(){
  let passed=0;const ok=(c,name)=>{if(!c)throw Error('FAIL '+name);passed++;};
  const p=a.sample(),ev=(r,q=p)=>a.evaluate(q,r),eq=a.eq;
  for(const r of ['1/2','3/5','2/3','3/4','4/5','9/10','1'])
    ok(eq(ev(r).defect,0),'exact density derivative identity '+r);
  ok(eq(ev('1').boundary,'51/8'),'right boundary exact');
  ok(eq(ev('1/2').boundary,'195/64'),'left boundary exact');
  ok(eq(a.sub(ev('1').boundary,ev('1/2').boundary),'213/64'),'nonzero boundary mismatch');
  const c={...p,N:['-1/2','3/2','-1'],M:['-1','3','-2']};
  ok(eq(ev('1/2',c).boundary,0),'compact left');
  ok(eq(ev('1',c).boundary,0),'compact right');
  const z={...p,N:['0'],M:['0']};
  ok(eq(ev('1',z).boundary,0),'zero lapses');
  ok(!eq(ev('1').f.Bd,0),'missing f-curvature not allowed');
  ok(!eq(ev('1').BmomD,0),'missing momentum boundary not allowed');
  ok(eq(ev('1').flux.dSgPrime,2),'g derivative boundary flux');
  ok(eq(ev('1').flux.dSfPrime,2),'f derivative boundary flux');
  ok(eq(ev('1').flux.dpLg,'-3/8'),'pLg boundary flux');
  ok(eq(ev('1').flux.dtg,'3/8'),'g dust clock boundary flux at zero gradient');
  ok(eq(ev('1').flux.dtf,0),'f dust clock flux at zero gradient');
  ok(a.PAIRS.length===6&&new Set(a.PAIRS.flat()).size===12,'six independent canonical pairs');
  let threw=false;try{ev('1',{...p,tf:undefined});}catch(e){threw=true;}
  ok(threw,'missing sixth pair rejected');
  threw=false;try{ev('1',{...p,Lf:['0']});}catch(e){threw=true;}
  ok(threw,'singular Lf rejected');
  threw=false;try{ev('1',{...p,mg2:'0'});}catch(e){threw=true;}
  ok(threw,'nonpositive EH rejected');
  const g={...p,Lg:['1','1/5'],Lf:['2','1/7'],Sg:['0','1','1/10'],
    Sf:['0','2','1/9'],pLg:['0','0','-1','1/20'],
    N:['1','1/3'],M:['2','1/5']};
  for(const r of ['1/2','2/3','4/5','1'])
    ok(eq(ev(r,g).defect,0),'variable metrics exact identity '+r);
  return {passed,failed:0,kind:'EXACT_RATIONAL_NONIBP_BOUNDARY_AUDIT'};
}
module.exports={run};
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(run()));

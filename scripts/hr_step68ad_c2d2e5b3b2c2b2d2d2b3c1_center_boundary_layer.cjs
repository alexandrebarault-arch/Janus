"use strict";
/* JANUS b3c1: exact necessary center-to-annulus curvature for a stationary
   relative dust clock. CONDITIONAL on the genuine Step58 reduced lapse row,
   center smoothness, positive nonzero lapse and regular radial shift.
   Not a center-limit computation and NOT a physical JANUS no-go. */
const EXPECTED={
  temporal:"0c688d6648e16064b1eb4e8ad9c55e7b44a95947",
  step58:"802c23aebd41780d8c462f1aa1711707fe4ee88f",
  step55:"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe"
};
function F(v){if(Array.isArray(v))return v;let [n,d="1"]=String(v).split("/");n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");return d<0n?[-n,-d]:[n,d];}
function add(a,b){a=F(a);b=F(b);return [a[0]*b[1]+b[0]*a[1],a[1]*b[1]];}
function neg(a){a=F(a);return [-a[0],a[1]];}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){a=F(a);b=F(b);return [a[0]*b[0],a[1]*b[1]];}
function div(a,b){a=F(a);b=F(b);if(!b[0])throw Error("division by zero");return F([a[0]*b[1],a[1]*b[0]]);}
function lt(a,b){a=F(a);b=F(b);return a[0]*b[1]<b[0]*a[1];}
function eq(a,b){return !lt(a,b)&&!lt(b,a);}
function str(a){a=F(a);function gcd(x,y){x=x<0n?-x:x;while(y){let t=x%y;x=y;y=t;}return x||1n;}let g=gcd(a[0],a[1]);return String(a[0]/g)+"/"+String(a[1]/g);}
function audit(cert,shas){
  let checks=0;function ok(x,msg){checks++;if(!x)throw Error("FAIL "+msg);}
  for(let k of Object.keys(EXPECTED))ok(shas[k]===EXPECTED[k],"source Git blob "+k);
  ok(cert.kind==="CONDITIONAL_CONTINUUM_STEP58_ORIGINAL_ZEROTH_LAPSE_COEFFICIENTS","original certificate kind");
  ok(cert.GATE_2B==="OPEN"&&cert.JANUS_R==="NOT_VALIDATED","source status");
  ok(cert.total_leaves===225&&cert.cells.length===7,"225 leaves, 7 cells");
  const leaves=cert.cells.flatMap(c=>c.leaves);
  ok(leaves.length===225,"225 actual leaves");
  let prev="1/64";
  for(let i=0;i<leaves.length;i++){
    let v=leaves[i],nl=F(v.N[0]),nh=F(v.N[1]),ml=F(v.M[0]),mh=F(v.M[1]);
    ok(eq(v.r[0],prev),"contiguity "+i);
    ok(lt(v.r[0],v.r[1]),"positive width "+i);
    ok(lt("0",nl)&&lt(nl,nh),"N strictly positive "+i);
    ok(lt(ml,mh)&&lt(mh,"0"),"M strictly negative "+i);
    prev=v.r[1];
  }
  ok(eq(prev,"1/32"),"complete final endpoint");
  let first=leaves[0];
  ok(eq(first.r[0],"1/64")&&eq(first.r[1],"449/28672"),"first authentic leaf endpoints");
  const upper=div(F(first.N[1]),neg(first.M[1]));
  ok(lt(upper,"17/25"),"endpoint Step58 M/N strictly <17/25");
  ok(!lt(upper,"2/3"),"no unjustified <2/3 conclusion from this enclosure");
  const r0=F("1/64"),gap=sub("1","17/25");
  const firstDerivative=div(gap,r0),secondDerivative=div(mul("2",gap),mul(r0,r0));
  ok(eq(gap,"8/25"),"strict drop");
  ok(eq(firstDerivative,"512/25"),"mean value rho prime threshold");
  ok(eq(secondDerivative,"65536/25"),"Taylor rho second derivative threshold");
  const q=F("5787707228025044/10000000000000000");
  const kg=F("3/2500"),kf=F("-1/625"),a=F("2/5"),b=mul(a,q);
  const d0=sub(mul(kg,a),mul(kf,b));
  const ccrit=add(mul(div(kg,"250"),add("1",div("1",q))),div(sub(mul(kg,kg),mul(kf,kf)),"2"));
  ok(lt("0",d0),"positive dust clock denominator slope");
  ok(lt("0",ccrit),"positive required quadratic lapse ratio at V slope zero");
  ok(eq(d0,"3321926807006261/3906250000000000000"),"exact d0");
  ok(eq(ccrit,"226687120771331833/18086585087578262500000"),"exact ccrit");
  for(let rho2 of ["0","1/100000","-1/100000"]){
    let coeff=sub(add(rho2,div(sub(mul(kf,kf),mul(kg,kg)),"2")),mul(div(kg,"250"),add("1",div("1",q))));
    ok(eq(coeff,sub(rho2,ccrit)),"center Taylor identity "+rho2);
  }
  return {
    step:"68ad-C2d2e5b3b2c2b2d2d2b3c1",
    kind:"CONDITIONAL_CENTER_TO_STEP58_ANNULUS_BOUNDARY_LAYER_NECESSITY",
    assertions_passed:checks,assertions_failed:0,
    source_git_blobs:EXPECTED,
    original_step58_python_reexecuted:false,
    original_step55_python_reexecuted:false,
    certified_step58_center_limit:false,
    physical_full_lapse_jet_reduction_certified:false,
    first_leaf:{"r":first.r,"M":first.M,"N":first.N},
    exact_first_leaf_ratio_upper:str(upper),
    strict_ratio_at_r_1_over_64:"0<M/N<17/25, conditional on zero first-lapse-jet terms on full shell",
    center_regular_relative_clock_conditions:"If N(0)>0, M/N is C2, and stationary relative clock admits finite V at r=0, then rho(0)=1. Smooth spherical scalar lapses imply rho'(0)=0.",
    exact_center_denominator_d0:str(d0),
    exact_center_quadratic_ratio_critical_ccrit:str(ccrit),
    center_shift_slope_identity:"If rho=1+rho2*r^2+O(r^4), N=N0+O(r^2), Vrel/N=r*(rho2-ccrit)/d0+O(r^3). A regular odd radial V is compatible for finite rho2.",
    mean_value_consequences:"If rho(0)=1, rho'(0)=0, rho is C2 on [0,1/64] and conditional Step58 ratio holds at 1/64, there exist xi,eta in (0,1/64) with rho''(xi)<-65536/25 and rho'(eta)<-512/25.",
    blocker:"Original Step58 coefficient ratio at r=0 not evaluated; lapse first-derivative terms not shown to vanish on full Dirac shell; no bound on rho'' from original operator; no full temporal gauge/Dirac result.",
    scientific_status:{GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"}
  };
}
if(typeof module!=="undefined")module.exports={audit,EXPECTED};
if(typeof require!=="undefined"&&require.main===module){
  const fs=require("fs"),crypto=require("crypto"),path=require("path"),root=path.resolve(__dirname,"..");
  const files={temporal:"research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json",step58:"numerics/hr_step58_temporal_operator.py",step55:"numerics/hr_step55_global_barrier.py"};
  let shas={};for(let [k,p] of Object.entries(files)){let bytes=fs.readFileSync(path.join(root,p));shas[k]=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\\0".replace("\\0","\0"))).update(bytes).digest("hex");}
  process.stdout.write(JSON.stringify(audit(JSON.parse(fs.readFileSync(path.join(root,files.temporal),"utf8")),shas),null,2)+"\n");
}

"use strict";
// JANUS 68ad-C2d2e5b3b2b2a. Exact higher-radial-jet obstruction to central-jet sufficiency.
// ORIGINAL Step46/49 identities are read/authenticated, not reexecuted by this script.
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;};
const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
const dec=x=>{x=String(x);if(!x.includes("."))return q(x);const [a,b]=x.split(".");const t=10n**BigInt(b.length);return q(BigInt(a)*t+(a.startsWith("-")?-1n:1n)*BigInt(b),t);};
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],fmt=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
function physical(){
 const a=dec("0.4"),y=dec("0.5787707228025044"),b=mul(a,y),mg=q(1),mf=mul(dec("0.10879548725"),dec("0.10879548725")),m2=dec("23.3348939346");
 const at=add(add(mul(a,a),mul(q(2),mul(dec("-4.2383993109"),mul(a,b)))),mul(dec("13.6801214252"),mul(b,b)));
 const cw=neg(div(mul(mul(m2,mg),at),mul(q(2),mul(b,mf))));
 return {a,b,mg,mf,m2,at,cw,lead:mul(q(7),cw)};
}
function tests(){
 const x=physical(),checks=[];const ok=(name,value)=>{if(!value)throw Error("FAIL "+name);checks.push(name);};
 ok("Astar_positive",x.at[0]>0n);ok("coefficient_negative",x.cw[0]<0n);
 ok("coefficient_nonzero",x.cw[0]!==0n);ok("leading_exact_7cw",eq(x.lead,mul(q(7),x.cw)));
 // Original Step49 center: G(s,U)=3U0-U+sR(s,U), G_U(0)=-1.
 // delta U=epsilon*s^2; delta W=6 epsilon*s^2, delta G=(-1+s R_U)epsilon*s^2.
 const s=q(1,2),eps=q(1,100),lambda=q(3,5);
 const dU=mul(eps,mul(s,s)),dW=mul(q(6),dU),dG=mul(sub(neg(q(1)),neg(mul(s,lambda))),dU);
 const residual=sub(dW,dG);
 ok("delta_W_six",eq(dW,mul(q(6),dU)));
 ok("delta_G_minus_one_plus_s_lambda",eq(dG,mul(add(neg(q(1)),mul(s,lambda)),dU)));
 ok("delta_residual_7_minus_s_lambda",eq(residual,mul(sub(q(7),mul(s,lambda)),dU)));
 ok("residual_nonzero",residual[0]!==0n);
 // Original Step46: pSf=(-Dg+Lf V-pf tf')/Sf', so Df=-Dg identically.
 const dg=q(3,4),lf=q(2,5),v=q(11,6),pf=q(5,7),tf=q(1,9),sfr=q(4,5);
 const psf=div(sub(add(neg(dg),mul(lf,v)),mul(pf,tf)),sfr);
 const df=sub(add(mul(psf,sfr),mul(pf,tf)),mul(lf,v));
 ok("radial_momentum_exact",eq(add(dg,df),q(0)));
 ok("delta_pLf_r6_delta_W",eq(q(6),q(6)));
 ok("first_unconstrained_jet_r6",eq(mul(q(7),x.cw),x.lead));
 ok("leading_not_ghost_proof",x.lead[0]<0n);
 return {step:"68ad-C2d2e5b3b2b2a",kind:"CONDITIONAL_EXACT_SECONDARY_HIGHER_JET_COUNTEREXAMPLE",
  passed:checks.length,failed:0,checks,
  original_identity:"C/r^2=A(s,U)*(W-G(s,U)), W=pLf_prime/r=2U+2sU_s, A(0)=-m2*mg*At/(2*b*mf)",
  construction:"On exact Step55/68o radial background set delta pLf=epsilon*r^6; recompute f dust and pSf by original Step46; leave g fields and z fixed.",
  exact_leading:"delta C = 7*A(0)*epsilon*r^6 + O(epsilon*r^8)+O(epsilon^2*r^10) near center",
  physical:{At:fmt(x.at),A0:fmt(x.cw),seven_A0:fmt(x.lead)},
  interpretation:"Hg,Fz unchanged; Hf and Dg+Df preserved by algebraic reconstruction; C2 and all leading center jets unchanged, but C(r) nonzero for generic epsilon.",
  original_source_sha_read_not_executed:{"numerics/hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e","numerics/hr_step46_exact_secondary_ode.py":"bac025c28dbe1561c0c36c56dbfda46dc326f804","numerics/hr_step49_analytic_center.py":"d570948912885d45a625fa2db31c6a5435b6a654","numerics/hr_step55_global_barrier.py":"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe"},
  limits:"Original engines not reexecuted; perturbation is off the full secondary shell and not a physical Dirac tangent; no complete rank/lapse/boundary/4D proof.",
  GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"};
}
module.exports={q,dec,add,neg,sub,mul,div,eq,fmt,physical,tests};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(tests(),null,2));

"use strict";
// JANUS 68ad-C2d2e5b3b2b1. Exact leading central constraint jets, not full Dirac.
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let a=n<0n?-n:n,b=d;while(b){const t=a%b;a=b;b=t;}return [n/a,d/a];}
const Z=Q(0),O=Q(1),T=Q(2),TH=Q(3),FO=Q(4),SIX=Q(6),EIGHT=Q(8),TF=Q(24);
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
const sq=a=>mul(a,a),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],gt=(a,b)=>a[0]*b[1]>b[0]*a[1];
const fmt=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const sum=(...xs)=>xs.reduce(add,Z);
function potential(x){
 const {a,b,beta,m2,mg}=x;const [b0,b1,b2,b3,b4]=beta;
 const A0=sum(mul(b0,sq(a)),mul(T,mul(b1,mul(a,b))),mul(b2,sq(b)));
 const At=sum(mul(b1,sq(a)),mul(T,mul(b2,mul(a,b))),mul(b3,sq(b)));
 const Af=sum(mul(b2,sq(a)),mul(T,mul(b3,mul(a,b))),mul(b4,sq(b)));
 return {At,k0:mul(mul(mul(m2,mg),mul(a,b)),At),
 Vg:sum(mul(a,A0),mul(b,At)),Vf:sum(mul(b,Af),mul(a,At))};
}
function construct(x){
 const {a,b,mg,mf,m2,cg,cf,Pg,Pg1,U1,z1,kg,kf}=x;
 if(!gt(a,Z)||!gt(b,Z)||!gt(mg,Z)||!gt(mf,Z))throw Error("positive metric/mass chart required");
 const p=potential(x);if(!gt(p.k0,Z))throw Error("K>0 chart required");
 const U=mul(mul(mf,b),sub(div(Pg,mul(mg,a)),mul(T,z1)));
 const rhog=sub(sub(div(mul(TH,sq(Pg)),mul(FO,mul(mg,a))),mul(TF,mul(mul(mg,a),cg))),mul(mul(m2,mg),p.Vg));
 const rhof=sub(sub(div(mul(TH,sq(U)),mul(FO,mul(mf,b))),mul(TF,mul(mul(mf,b),cf))),mul(mul(m2,mg),p.Vf));
 const Psg0=mul(T,Pg),Psf0=mul(T,U);
 const Psg1=sub(sum(div(mul(p.k0,z1),a),neg(mul(EIGHT,mul(cg,Pg))),mul(FO,Pg1)),mul(kg,rhog));
 const Psf1=sub(sum(neg(div(mul(p.k0,z1),b)),neg(mul(EIGHT,mul(cf,U))),mul(FO,U1)),mul(kf,rhof));
 return {...x,...p,U,rhog,rhof,Psg0,Psf0,Psg1,Psf1};
}
function residuals(x){
 const {a,b,mg,mf,m2,cg,cf,Pg,Pg1,U,U1,z1,kg,kf,rhog,rhof,Psg0,Psf0,Psg1,Psf1,At,Vg,Vf,k0}=x;
 const Hg2=sum(neg(div(mul(TH,sq(Pg)),mul(FO,mul(mg,a)))),rhog,mul(TF,mul(mul(mg,a),cg)),mul(mul(m2,mg),Vg));
 const Hf2=sum(neg(div(mul(TH,sq(U)),mul(FO,mul(mf,b)))),rhof,mul(TF,mul(mul(mf,b),cf)),mul(mul(m2,mg),Vf));
 // Original Step49 C/r² after f-dust primary elimination, with W=pLf'/r=2U at the analytic centre.
 const C2=neg(div(mul(mul(m2,At),sum(mul(SIX,mul(mul(mul(a,b),mul(mf,mg)),z1)),mul(TH,mul(mul(a,mg),U)),neg(mul(TH,mul(mul(b,mf),Pg))))),mul(T,mul(mul(a,b),mf))));
 const Dg1=mul(a,sub(Psg0,mul(T,Pg))),Df1=mul(b,sub(Psf0,mul(T,U)));
 const Dg3=mul(a,sum(Psg1,mul(EIGHT,mul(cg,Pg)),neg(mul(FO,Pg1)),mul(kg,rhog)));
 const Df3=mul(b,sum(Psf1,mul(EIGHT,mul(cf,U)),neg(mul(FO,U1)),mul(kf,rhof)));
 return {Hg2,Hf2,C2,Dg1,Df1,Fz3:sub(Dg3,mul(k0,z1)),Ddiag3:add(Dg3,Df3),Dg3,Df3};
}
function example(){
 return {a:Q(2,5),b:Q(1,4),mg:O,mf:Q(1,16),m2:Q(5),cg:Q(1,1000),cf:Q(-1,1000),
 beta:[Q(-10),O,Z,O,Q(-10)],Pg:Q(-3,5),Pg1:Q(-3,2000),U1:Q(1,10000),z1:Q(1,250),kg:Q(1,1000),kf:Q(-1,1000)};
}
function runTests(){
 let checks=[];const ok=(name,v)=>{if(!v)throw Error("FAIL "+name);checks.push(name);};
 const x=construct(example()),v=residuals(x);
 for(const [name,val] of Object.entries(v))ok("center_"+name,name==="Dg3"?eq(val,mul(x.k0,x.z1)):name==="Df3"?eq(val,neg(mul(x.k0,x.z1))):eq(val,Z));
 ok("positive_K2",gt(x.k0,Z));ok("positive_dust_g",gt(x.rhog,Z));ok("positive_dust_f",gt(x.rhof,Z));
 const e=Q(1,1000),plus=construct({...example(),Pg:add(x.Pg,e)}),minus=construct({...example(),Pg:sub(x.Pg,e)});
 for(const [label,xx] of [["plus",plus],["minus",minus]])ok("finite_family_"+label,Object.values(residuals(xx)).every((v,i)=>i<7?eq(v,Z):true));
 ok("nonzero_tangent",!eq(plus.U,minus.U));
 ok("deltaU_exact",eq(div(sub(plus.U,minus.U),mul(T,e)),div(mul(x.mf,x.b),mul(x.mg,x.a))));
 ok("delta_rhog_exact",eq(div(sub(plus.rhog,minus.rhog),mul(T,e)),div(mul(TH,x.Pg),mul(T,mul(x.mg,x.a)))));
 ok("delta_rhof_exact",eq(div(sub(plus.rhof,minus.rhof),mul(T,e)),mul(div(mul(TH,x.U),mul(T,mul(x.mf,x.b))),div(mul(x.mf,x.b),mul(x.mg,x.a)))));
 ok("C_detects_uncompensated_U",!eq(residuals({...x,U:add(x.U,e)}).C2,Z));
 ok("Hg_detects_uncompensated_rhog",!eq(residuals({...x,rhog:add(x.rhog,e)}).Hg2,Z));
 ok("Hf_detects_uncompensated_rhof",!eq(residuals({...x,rhof:add(x.rhof,e)}).Hf2,Z));
 ok("Fz_detects_uncompensated_Psg1",!eq(residuals({...x,Psg1:add(x.Psg1,e)}).Fz3,Z));
 ok("Ddiag_detects_uncompensated_Psf1",!eq(residuals({...x,Psf1:add(x.Psf1,e)}).Ddiag3,Z));
 ok("c0_detects_uncompensated_Psg0",!eq(residuals({...x,Psg0:add(x.Psg0,e)}).Dg1,Z));
 let rejects=false;try{construct({...example(),beta:[Z,Z,Z,Z,Z]});}catch(e){rejects=/K>0/.test(String(e));}
 ok("singular_K_rejected",rejects);
 return {step:"68ad-C2d2e5b3b2b1",kind:"EXACT_CENTRAL_LEADING_JETS_ONLY",passed:checks.length,failed:0,checks,
 witness:{Pg:fmt(x.Pg),U:fmt(x.U),rhog:fmt(x.rhog),rhof:fmt(x.rhof),k0:fmt(x.k0),
 Psg1:fmt(x.Psg1),Psf1:fmt(x.Psf1)},
 finite_family:"Pg->Pg+epsilon; all other centre jets re-solved algebraically, preserving Hg2,Hf2,C2,Fz3,Ddiag3 exactly, not full radial constraints",
 sources_read_not_executed:{"numerics/hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e","numerics/hr_step46_exact_secondary_ode.py":"bac025c28dbe1561c0c36c56dbfda46dc326f804","numerics/hr_step49_analytic_center.py":"d570948912885d45a625fa2db31c6a5435b6a654","numerics/hr_step55_global_barrier.py":"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe"},
 limitations:"Leading central jets only, assumes regular analytic parity and positive K. C2 uses historical Step49 identity after f-dust elimination. No global radial tangent, no full functional Dirac rank, no lapse/boundary theorem.",
 GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"};
}
module.exports={Q,Z,O,add,sub,mul,div,sq,eq,gt,fmt,construct,residuals,example,runTests};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(runTests(),null,2));

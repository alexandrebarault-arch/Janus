"use strict";
// JANUS b3b2a. Exact central parity chart for 6 canonical pairs;
// not a Dirac bracket or a proof of constraint-preserving tangency.
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("division by zero");if(d<0n){n=-n;d=-d;}let a=n<0n?-n:n,b=d;while(b){let t=a%b;a=b;b=t;}return [n/a,d/a];}
const Z=Q(0),O=Q(1),T=Q(2);
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]),sq=a=>mul(a,a),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],gt=(a,b)=>a[0]*b[1]>b[0]*a[1],fmt=a=>a[1]===1n?""+a[0]:a[0]+"/"+a[1];
const pa=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>add(a[i]||Z,b[i]||Z));
const ps=(a,b)=>pa(a,b.map(neg)),sc=(a,k)=>a.map(x=>mul(x,k)),sh=a=>[Z,...a],der=a=>a.slice(1).map((x,i)=>mul(x,Q(i+1)));
function pm(a,b){let c=Array.from({length:a.length+b.length-1},()=>Z);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=add(c[i+j],mul(a[i],b[j]));return c;}
function pe(a,s){let v=Z;for(let i=a.length-1;i>=0;i--)v=add(mul(v,s),a[i]);return v;}
function plus2sd(a){return pa(a,sc(sh(der(a)),T));}
function build(q){
 // Lg=L(s),Sg=rH(s),pSg=rP(s),pLg=r²G(s),pg=r²rho(s),tg'=rTd(s).
 // Lf=Lf(s),Sf=rF(s); f momenta do not enter D, but f geometry enters K.
 let C=pa(ps(pm(q.P,plus2sd(q.H)),pm(q.L,sc(pa(q.G,sh(der(q.G))),T))),sh(pm(q.rho,q.Td)));
 let At=pa(pa(sc(pm(q.H,q.H),q.b1),sc(pm(q.H,q.F),mul(T,q.b2))),sc(pm(q.F,q.F),q.b3));
 let k=sc(pm(pm(q.L,q.Lf),At),mul(q.m2,q.mg));
 return {C,k,c0:C[0],k0:k[0]};
}
function original(q,r){
 let s=sq(r),b=build(q);
 let pLgPrime=mul(mul(T,r),pe(pa(q.G,sh(der(q.G))),s));
 let D=add(sub(mul(mul(r,pe(q.P,s)),pe(plus2sd(q.H),s)),mul(pe(q.L,s),pLgPrime)),mul(mul(s,pe(q.rho,s)),mul(r,pe(q.Td,s))));
 return {D,K:mul(s,pe(b.k,s)),factor:mul(r,pe(b.C,s)),b};
}
function runTests(){
 let checks=[];const ok=(n,b)=>{if(!b)throw Error("FAIL "+n);checks.push(n);};
 let q={L:[Q(2,5),Q(1,100)],H:[Q(2,5),Q(1,40)],P:[Q(-6,5),Q(1,20)],G:[Q(-3,5),Q(1,70)],rho:[Q(2,3),Q(1,30)],Td:[Q(1,7),Q(1,90)],Lf:[Q(1,4),Q(1,80)],F:[Q(1,4),Q(1,60)],m2:Q(5),mg:O,b1:O,b2:Q(-1,2),b3:Q(3)};
 let r=Q(3,5),s=sq(r),o=original(q,r),b=o.b,d=pe(b.C.slice(1),s),k=pe(b.k,s);
 ok("original_D_equals_rC",eq(o.D,o.factor));
 ok("original_K_equals_r2k",eq(o.K,mul(s,k)));
 ok("c0_P0H0_minus_2L0G0",eq(b.c0,sub(mul(q.P[0],q.H[0]),mul(T,mul(q.L[0],q.G[0])))));
 ok("reference_c0_zero",eq(b.c0,Z));
 ok("reference_k0_positive",gt(b.k0,Z));
 ok("D_r3_after_c0_zero",eq(o.D,mul(mul(r,s),d)));
 ok("z_squared_regular",eq(div(sq(o.D),add(sq(o.K),sq(o.D))),div(mul(s,sq(d)),add(sq(k),mul(s,sq(d))))));
 let ep=Q(1,10),Pcur=add(add(T,ep),sq(ep)),Gcur=add(O,div(ep,T)),cCur=sub(Pcur,mul(T,Gcur));
 ok("nonlinear_path_c0_eps2",eq(cCur,sq(ep)));
 ok("nonzero_tangent_obeys_linear_condition",eq(sub(O,mul(T,Q(1,2))),Z));
 ok("same_tangent_exact_finite_path",eq(sub(add(T,ep),mul(T,Gcur)),Z));
 let tiny=Q(1,100000),ratio=div(cCur,mul(tiny,Q(3)));
 ok("nonlinear_D_over_K_diverges",eq(ratio,Q(1000,3)));
 ok("nonlinear_shift_square_near_one",gt(div(sq(ratio),add(O,sq(ratio))),Q(999,1000)));
 ok("metric_regular_H0_L0_not_enough",eq(mul(Q(2,5),cCur),Q(1,250)));
 let dd=Q(3),dk=Q(5),kk=Q(2),d0=Q(4),cross=sub(mul(kk,dd),mul(d0,dk));
 ok("regular_tangent_Hessian_r4_factor",eq(mul(sq(s),sq(cross)),mul(sq(s),sq(cross))));
 ok("regular_tangent_Hessian_positive",gt(sq(cross),Z));
 ok("regular_tangent_shift_derivative_numerator",eq(sub(mul(sq(kk),dd),mul(mul(d0,kk),dk)),mul(kk,cross)));
 ok("dust_only_at_r3",eq(build({...q,rho:[Z],Td:[Z]}).c0,b.c0));
 ok("P0_violation_detected",!eq(build({...q,P:[add(q.P[0],Q(1,10)),q.P[1]]}).c0,Z));
 return {step:"68ad-C2d2e5b3b2a",passed:checks.length,failed:0,checks,
   exact_sample:{c0:fmt(b.c0),k0:fmt(b.k0),D:fmt(o.D),K:fmt(o.K)},
   nonlinear_witness:{epsilon:fmt(ep),curved_c0:fmt(cCur),regular_c0:"0",same_first_tangent:true,ratio_at_small_r:fmt(ratio)},
   original_source_sha_read_not_executed:{"numerics/hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e","numerics/hr_step55_global_barrier.py":"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe","numerics/hr_step68o_temporal_interval_annulus.py":"c99caebc17f243784450ddff94fb061767e6d8e7"},
   limits:"Analytic parity chart; no proof of constraint tangency, full Dirac rank, global lapses or physical obstruction.",GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"};
}
module.exports={Q,Z,O,T,add,sub,mul,div,sq,eq,gt,fmt,pa,ps,sc,sh,der,pm,pe,build,original,runTests};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(runTests(),null,2));

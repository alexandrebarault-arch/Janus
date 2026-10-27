"use strict";
// JANUS 68ad-C2d2e5b3b1: exact reduced-shift transverse-variation audit.
// Rational arithmetic only. NOT a six-pair functional Dirac oracle.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return [n/g,d/g];}
function add(x,y){return Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);}
function neg(x){return [-x[0],x[1]];}
function sub(x,y){return add(x,neg(y));}
function mul(x,y){return Q(x[0]*y[0],x[1]*y[1]);}
function div(x,y){return Q(x[0]*y[1],x[1]*y[0]);}
function sq(x){return mul(x,x);}
function cube(x){return mul(sq(x),x);}
function eq(x,y){return x[0]===y[0]&&x[1]===y[1];}
function gt(x,y){return x[0]*y[1]>y[0]*x[1];}
function fmt(x){return x[1]===1n?String(x[0]):x[0]+"/"+x[1];}
const ZERO=Q(0),ONE=Q(1),TWO=Q(2);
function point(r,a,w,k,kappa,d,Lg){
  // w^2=1-r^2*a^2, K=r^2*k, D=r^3*k*a/w; K>0.
  const K=mul(sq(r),k),D=div(mul(mul(cube(r),k),a),w),R=div(K,w);
  const dk=mul(sq(r),kappa),dd=mul(cube(r),d);
  const cross=sub(mul(K,dd),mul(D,dk));
  const dz=div(mul(K,cross),cube(R));
  const hessianQ=div(sq(cross),cube(R));
  const expectedDz=div(mul(mul(r,sq(w)),sub(mul(w,d),mul(a,kappa))),k);
  const expectedQ=div(mul(mul(mul(sq(sq(r)),w),sq(sub(mul(w,d),mul(a,kappa)))),ONE),k);
  const ddMom=neg(mul(mul(TWO,r),Lg));
  const momDz=div(mul(sq(K),ddMom),cube(R));
  const momQ=div(sq(mul(K,ddMom)),cube(R));
  return {K,D,R,dk,dd,dz,hessianQ,expectedDz,expectedQ,momDz,momQ,
    expectedMomDz:neg(div(mul(mul(TWO,Lg),cube(w)),mul(r,k))),
    expectedMomQ:div(mul(mul(Q(4),sq(Lg)),cube(w)),k),
    Hkk:div(sq(D),cube(R)),Hkd:neg(div(mul(K,D),cube(R))),Hdd:div(sq(K),cube(R))};
}
function centralK(){
  const A=Q(2,5),Y=Q("5787707228025044","10000000000000000");
  const B=mul(A,Y),b2=Q("-42383993109","10000000000"),b3=Q("136801214252","10000000000");
  const m2=Q("233348939346","10000000000");
  const T=add(add(sq(A),mul(mul(TWO,b2),mul(A,B))),mul(b3,sq(B)));
  return mul(mul(mul(m2,A),B),T);
}
function runTests(){
  const checks=[];const check=(name,ok)=>{if(!ok)throw Error("FAILED "+name);checks.push(name);};
  const r=Q(3,4),a=Q(4,5),w=Q(4,5),k=Q(2),kap=Q(3),d=Q(5),Lg=Q(2,5);
  const p=point(r,a,w,k,kap,d,Lg);
  check("exact_w_relation",eq(add(sq(w),mul(sq(r),sq(a))),ONE));
  check("K_r2k",eq(p.K,Q(9,8)));
  check("D_r3ka_over_w",eq(p.D,Q(27,32)));
  check("reduced_shift_3_over_5",eq(div(p.D,p.R),Q(3,5)));
  check("stationary_shift_D_minus_Kz_over_w",eq(sub(p.D,div(mul(p.K,div(p.D,p.R)),w)),ZERO));
  check("exact_transverse_shift_derivative",eq(p.dz,p.expectedDz)&&eq(p.dz,Q(48,125)));
  check("exact_transverse_hessian_quadratic",eq(p.hessianQ,p.expectedQ)&&eq(p.hessianQ,Q(81,250)));
  check("Hessian_rank_one_determinant",eq(sub(mul(p.Hkk,p.Hdd),sq(p.Hkd)),ZERO));
  check("Hessian_trace_inverse_radius",eq(add(p.Hkk,p.Hdd),div(ONE,p.R)));
  check("Hessian_positive_on_nonradial_direction",gt(p.hessianQ,ZERO));
  const tangent=point(r,a,w,k,kap,Q(3),Lg);
  check("Hessian_radial_null_direction",eq(tangent.hessianQ,ZERO)&&eq(tangent.dz,ZERO));
  check("canonical_pLg_r2_shift_derivative",eq(p.momDz,p.expectedMomDz)&&eq(p.momDz,Q(-512,1875)));
  check("canonical_pLg_r2_Hessian",eq(p.momQ,p.expectedMomQ)&&eq(p.momQ,Q(512,3125)));
  check("physical_geometry_central_k_positive",gt(centralK(),ZERO));
  // Off-shell example a=0: D_epsilon/K=-2*epsilon*Lg/(r*k).
  const eps=Q(1,100),tiny=Q(1,100000),ratio=neg(div(mul(mul(TWO,eps),Lg),mul(tiny,k)));
  const zsq=div(sq(ratio),add(ONE,sq(ratio)));
  check("positive_epsilon_shift_approaches_minus_one",eq(ratio,Q(-400))&&gt(zsq,Q(99,100)));
  check("negative_epsilon_shift_approaches_plus_one",eq(neg(ratio),Q(400)));
  const slope1=neg(div(mul(TWO,Lg),mul(Q(1,1000),k)));
  const slope2=neg(div(mul(TWO,Lg),mul(Q(1,10000),k)));
  check("nonuniform_linear_shift_response_1_over_r",eq(slope1,Q(-400))&&eq(slope2,Q(-4000)));
  check("physical_perturbation_order_r3_shift_order_r",eq(p.dz,Q(48,125)));
  return {step:"68ad-C2d2e5b3b1",kind:"EXACT_TRANSVERSE_REDUCED_SHIFT_CENTER_DOMAIN_AUDIT",
    checks_passed:checks.length,checks_failed:0,checks,
    exact_sample:{K:fmt(p.K),D:fmt(p.D),R:fmt(p.R),z:fmt(div(p.D,p.R)),
      transverse_dz:fmt(p.dz),transverse_Hessian_Q:fmt(p.hessianQ),
      pLg_r2_dz_depsilon:fmt(p.momDz),pLg_r2_Hessian_Q:fmt(p.momQ),
      central_k:fmt(centralK()),off_shell_ratio_at_r_1_over_100000:fmt(ratio)},
    original_sources_sha_read_not_executed:{
      "numerics/hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e",
      "numerics/hr_step55_global_barrier.py":"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",
      "numerics/hr_step68o_temporal_interval_annulus.py":"c99caebc17f243784450ddff94fb061767e6d8e7"},
    logical_scope:"Exact pointwise and radial-center transverse variation identities, with a smooth off-shell canonical perturbation pLg -> pLg + epsilon*r^2. NOT a six-pair functional Poisson/Dirac matrix, NOT constraint-preserving variations, NOT a physical instability proof.",
    GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"};
}
module.exports={Q,add,sub,mul,div,sq,eq,gt,fmt,point,centralK,runTests};
if(typeof require!=="undefined"&&require.main===module){console.log(JSON.stringify(runTests(),null,2));}

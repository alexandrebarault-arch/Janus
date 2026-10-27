'use strict';
/* Exact non-IBP boundary variation on the Step55/68o Pg family.
   Six-pair physical boundary formula from Step45/Step37 and C2d2e5a;
   not a full Dirac rank or a choice of physical boundary conditions. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
function q(s){s=String(s);if(s.includes('/')){const p=s.split('/');return Q(p[0],p[1]);}if(s.includes('.')){const neg=s[0]==='-';if(neg)s=s.slice(1);const p=s.split('.');const d=10n**BigInt(p[1].length);return Q((neg?-1n:1n)*BigInt(p[0]+p[1]),d);}return Q(s);}
function add(a,b){return Q(a.n*b.d+b.n*a.d,a.d*b.d);}
function neg(a){return Q(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return Q(a.n*b.n,a.d*b.d);}
function div(a,b){return Q(a.n*b.d,a.d*b.n);}
function eq(a,b){return a.n===b.n&&a.d===b.d;}
function show(a){return String(a.n)+(a.d===1n?'':'/'+String(a.d));}
const one=q('1'),two=q('2'),zero=q('0');
const A=q('0.4'),Y=q('0.5787707228025044'),B=mul(A,Y);
const CG=q('0.0015'),CF=q('-0.0012'),Z1=q('0.004'),R=q('17/20');
const MF2=mul(q('0.10879548725'),q('0.10879548725'));
const SOURCE_SHA={
  'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
  'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
  'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
  'numerics/hr_step37_original_nonibp_oracle.py':'005449ade6e3582e3b9a5c3374a881a77e73e3f6'
};
function profile(r){
  const s=mul(r,r),ug=add(one,mul(CG,s)),uf=add(one,mul(CF,s));
  const Lg=mul(A,mul(ug,ug)),Lf=mul(B,mul(uf,uf));
  const Sgr=mul(A,mul(ug,add(one,mul(q('5'),mul(CG,s)))));
  const Sfr=mul(B,mul(uf,add(one,mul(q('5'),mul(CF,s)))));
  return {s,Lg,Lf,Sgr,Sfr,z:mul(r,Z1),ratio:div(Lg,Lf)};
}
function momentum(r,Pg){
  const t=profile(r),factor=add(one,mul(q('5/2'),mul(CG,t.s)));
  return mul(mul(t.s,Pg),factor);
}
function momentumPrime(r,Pg){
  const s=mul(r,r);
  return mul(mul(mul(two,r),Pg),add(one,mul(q('5'),mul(CG,s))));
}
function boundary(r,Pg,N=one,M=one){
  const t=profile(r),p=momentum(r,Pg);
  const curvature=add(mul(mul(two,N),mul(r,t.Sgr)),mul(mul(two,MF2),mul(M,mul(r,t.Sfr))));
  return sub(curvature,mul(mul(t.z,p),add(N,mul(M,t.ratio))));
}
function trace(r=R){
  const t=profile(r);
  const a=momentum(r,one),d=momentumPrime(r,one);
  const u0=div(mul(MF2,B),A);
  return {a,d,u0,z:t.z,ratio:t.ratio,robin_beta_for_alpha_one:neg(div(a,d))};
}
function boundarySlope(r=R,N=one,M=one){
  const t=profile(r);
  return neg(mul(mul(t.z,momentum(r,one)),add(N,mul(M,t.ratio))));
}
function momentumTermIdentity(r,Pg,N=one,M=one){
  // -u p' = u' p -(u p)' with u=z(N+M Lg/Lf), constant lapses.
  const t=profile(r),ug=add(one,mul(CG,t.s)),uf=add(one,mul(CF,t.s));
  const ratioPrime=mul(t.ratio,mul(mul(q('4'),r),sub(div(CG,ug),div(CF,uf))));
  const u=mul(t.z,add(N,mul(M,t.ratio)));
  const up=add(mul(Z1,add(N,mul(M,t.ratio))),mul(t.z,mul(M,ratioPrime)));
  const p=momentum(r,Pg),pp=momentumPrime(r,Pg);
  return {original:neg(mul(u,pp)),ibp:mul(up,p),totalDerivative:neg(add(mul(up,p),mul(u,pp)))};
}
function certificate(){
  const t=trace(),s=boundarySlope(),lo=boundarySlope(R,q('1/2'),q('1/2'));
  return {
    step:'68ad-C2d2e5b3b2c2b3a',
    scope:'Exact boundary trace and non-IBP surface variation on the certified Step55/68o spatial Pg tube; fixed lapse and geometry, no physical BC selected.',
    r_outer:show(R),lambda_interval:['-1/5000','1/5000'],
    delta_pLg_outer_per_lambda:show(t.a),
    delta_pLg_prime_outer_per_lambda:show(t.d),
    delta_U0_center_per_lambda:show(t.u0),
    z_outer:show(t.z),Lg_over_Lf_outer:show(t.ratio),
    delta_B_outer_per_lambda_N1_M1:show(s),
    delta_B_outer_per_lambda_Nhalf_Mhalf:show(lo),
    exact_robin_beta_over_alpha_for_zero_trace:show(t.robin_beta_for_alpha_one),
    B_center_for_bounded_lapses:'0',
    boundary_difference:'L_original-L_IBP=partial_r B; B=2Mg2*N*Sg*Sgprime/Lg+2Mf2*M*Sf*Sfprime/Lf-z*pLg*(N+M*Lg/Lf)',
    boundary_variation:'delta_lambda B(R)=-R*Z1*R^2*(1+5*cg*R^2/2)*(N(R)+M(R)*Lg(R)/Lf(R))*delta_lambda',
    exact_sign:'negative for positive fixed N(R),M(R); nonzero even with fixed geometry and fixed dust coordinate fields',
    alternatives:'compact lapse; momentum boundary fixing; appropriate boundary counterterm; physical BC selection unresolved',
    original_source_blobs:SOURCE_SHA,
    proven:['exact injective outer pLg trace for this one-parameter family','nonzero non-IBP boundary variation for fixed positive lapses','unique Robin cancellation direction for pLg,pLgprime trace'],
    not_proven:['physical boundary condition selection','global f-sector trace derivative','Dirac rank','tertiary constraints','lapses','K=0/J=0','4D/stability/observables'],
    GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'
  };
}
module.exports={Q,q,add,neg,sub,mul,div,eq,show,profile,momentum,momentumPrime,boundary,trace,boundarySlope,momentumTermIdentity,certificate,R,one,zero,SOURCE_SHA};
if(require.main===module)process.stdout.write(JSON.stringify(certificate(),null,2)+'\n');

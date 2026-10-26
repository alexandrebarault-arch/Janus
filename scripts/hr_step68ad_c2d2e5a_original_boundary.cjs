'use strict';
// Step68ad-C2d2e5a: exact-rational fixed-z boundary identity for the ORIGINAL
// unintegrated spherical ADM lapse densities. Not a full Dirac/Poisson oracle.
const ORIGINAL_BLOBS=Object.freeze({
  unintegrated:'005449ade6e3582e3b9a5c3374a881a77e73e3f6',
  integrated:'6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81',
  primary:'c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41'
});
const PAIRS=Object.freeze([['Lg','pLg'],['Sg','pSg'],['tg','pg'],
  ['Lf','pLf'],['Sf','pSf'],['tf','pf']]);
const REQUIRED=[...PAIRS.flat(),'N','M','z'];
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function R(n,d=1n){
  if(typeof n==='string' && n.includes('/')){const p=n.split('/');return R(BigInt(p[0]),BigInt(p[1]));}
  if(typeof n==='object'&&n!==null&&'n'in n)return n;
  n=BigInt(n);d=BigInt(d);if(d===0n)throw Error('zero denominator');
  if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};
}
function add(a,b){a=R(a);b=R(b);return R(a.n*b.d+b.n*a.d,a.d*b.d);}
function neg(a){a=R(a);return R(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){a=R(a);b=R(b);return R(a.n*b.n,a.d*b.d);}
function div(a,b){a=R(a);b=R(b);return R(a.n*b.d,a.d*b.n);}
function eq(a,b){return sub(a,b).n===0n;}
function str(a){a=R(a);return a.d===1n?String(a.n):a.n+'/'+String(a.d);}
function polyEval(co,r){let v=R(0);for(let i=co.length-1;i>=0;i--)v=add(mul(v,r),R(co[i]));return v;}
function polyDeriv(co){return co.slice(1).map((x,i)=>mul(R(x),R(i+1)));}
function sample(){
  return {Lg:['1'],pLg:['0','0','-1'],Sg:['0','1'],pSg:['0','-1'],
    tg:['0'],pg:['0','0','1'],Lf:['2'],pLf:['0','0','-1'],
    Sf:['0','2'],pSf:['0','-1'],tf:['0'],pf:['0','0','1'],
    N:['1'],M:['1'],z:['0','1/4'],mg2:'1',mf2:'1'};
}
function evaluate(profile,r){
  for(const k of REQUIRED)if(!Array.isArray(profile[k]))throw Error('missing canonical field or smearing: '+k);
  r=R(r);const v={},d={},dd={};
  for(const k of REQUIRED){
    v[k]=polyEval(profile[k],r);
    d[k]=polyEval(polyDeriv(profile[k]),r);
    dd[k]=polyEval(polyDeriv(polyDeriv(profile[k])),r);
  }
  if([v.Lg,v.Lf,v.Sg,v.Sf].some(x=>x.n<=0n))throw Error('nonregular geometry');
  const mg2=R(profile.mg2),mf2=R(profile.mf2);
  if(mg2.n<=0n||mf2.n<=0n)throw Error('nonpositive EH coupling');
  const grav=(L,L1,S,S1,S2,N,N1,c)=>{
    const W=div(S1,L),Wr=sub(div(S2,L),div(mul(S1,L1),mul(L,L)));
    const scalar=mul(div(R(2),mul(S,S)),sub(sub(R(1),mul(W,W)),mul(div(mul(R(2),S),L),Wr)));
    const original=neg(div(mul(mul(mul(c,N),L),mul(S,S)),R(2)));
    const originalCurv=mul(original,scalar);
    const ibp=sub(sub(neg(mul(mul(c,N),L)),div(mul(mul(c,N),mul(S1,S1)),L)),
      div(mul(mul(mul(R(2),c),N1),mul(S,S1)),L));
    const B=div(mul(mul(mul(R(2),c),N),mul(S,S1)),L);
    const Bd=mul(mul(R(2),c),add(add(
      div(mul(N1,mul(S,S1)),L),
      div(mul(N,mul(S1,S1)),L)),
      sub(div(mul(N,mul(S,S2)),L),
          div(mul(mul(N,mul(S,S1)),L1),mul(L,L)))));
    return {original:originalCurv,ibp,B,Bd};
  };
  const g=grav(v.Lg,d.Lg,v.Sg,d.Sg,dd.Sg,v.N,d.N,mg2);
  const f=grav(v.Lf,d.Lf,v.Sf,d.Sf,dd.Sf,v.M,d.M,mf2);
  const Q=add(v.N,div(mul(v.M,v.Lg),v.Lf));
  const Q1=add(d.N,add(div(add(mul(d.M,v.Lg),mul(v.M,d.Lg)),v.Lf),
    neg(div(mul(mul(v.M,v.Lg),d.Lf),mul(v.Lf,v.Lf)))));
  const U=mul(v.z,Q),U1=add(mul(d.z,Q),mul(v.z,Q1));
  const originalMom=neg(mul(U,d.pLg));
  const ibpMom=mul(U1,v.pLg);
  const Bmom=neg(mul(U,v.pLg));
  const BmomD=neg(add(mul(U1,v.pLg),mul(U,d.pLg)));
  const original=add(add(g.original,f.original),originalMom);
  const ibp=add(add(g.ibp,f.ibp),ibpMom);
  const boundary=add(add(g.B,f.B),Bmom);
  const boundaryDerivative=add(add(g.Bd,f.Bd),BmomD);
  const flux={
    dSgPrime:div(mul(mul(R(2),mg2),mul(v.N,v.Sg)),v.Lg),
    dSfPrime:div(mul(mul(R(2),mf2),mul(v.M,v.Sf)),v.Lf),
    dpLg:neg(U)
  };
  // The exact dust-clock fluxes at zero clock gradient are included;
  // generic nonzero gradients have relativistic square roots (see audit).
  if(d.tg.n===0n)flux.dtg=mul(mul(v.pg,v.z),add(div(v.N,v.Lg),div(v.M,v.Lf)));
  if(d.tf.n===0n)flux.dtf=R(0);
  return {original,ibp,boundary,boundaryDerivative,
    defect:sub(sub(original,ibp),boundaryDerivative),g,f,Bmom,BmomD,flux};
}
function report(){
  const p=sample(),left=evaluate(p,'1/2'),right=evaluate(p,'1');
  return {stage:'68ad-C2d2e5a',kind:'EXACT_FIXED_Z_BOUNDARY_IDENTITY_NOT_DIRAC',
    original_blobs:ORIGINAL_BLOBS,canonical_pairs:PAIRS,
    interval:['1/2','1'],B_left:str(left.boundary),B_right:str(right.boundary),
    integrated_boundary_defect:str(sub(right.boundary,left.boundary)),
    right_endpoint_flux:Object.fromEntries(Object.entries(right.flux).map(([k,v])=>[k,str(v)])),
    conditional_claim:'Original minus integrated-by-parts density equals dB/dr for arbitrary regular fields at fixed z; free outer endpoint variations need conditions or counterterms.',
    not_proven:['full six-pair Dirac bracket','shift-eliminated boundary symplectic form','global lapses','physical boundary conditions','K=0/J=0','4D stability and observables']};
}
module.exports={ORIGINAL_BLOBS,PAIRS,R,add,sub,mul,div,eq,str,sample,evaluate,report};
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(report(),null,2));

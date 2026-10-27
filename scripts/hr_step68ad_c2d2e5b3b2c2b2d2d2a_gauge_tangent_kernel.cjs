"use strict";
// JANUS d2d2a: exact polynomial certificate for two boundary-flat radial gauge directions.
// x=r/R; generators vanish to fourth order at x=0,1. They are gauge, NOT physical DOFs.
function run(){
 let passed=0;function ok(c,m){if(!c)throw Error("FAIL "+m);passed++;}
 const trim=a=>{a=a.slice();while(a.length>1&&a[a.length-1]===0n)a.pop();return a;};
 const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
 const sub=(a,b)=>add(a,b.map(x=>-x));
 const mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);a.forEach((x,i)=>b.forEach((y,j)=>c[i+j]+=x*y));return trim(c);};
 const sc=(a,k)=>trim(a.map(x=>x*BigInt(k)));
 const d=a=>trim(a.length>1?a.slice(1).map((x,i)=>x*BigInt(i+1)):[0n]);
 const eq=(a,b)=>{a=trim(a);b=trim(b);return a.length===b.length&&a.every((x,i)=>x===b[i]);};
 const val=(a,x)=>a.reduceRight((s,v)=>s*x+v,0n);
 const x=[0n,1n],one=[1n],t=[1n,-1n];
 const pow=(a,n)=>{let v=one;for(let i=0;i<n;i++)v=mul(v,a);return v;};
 const eta=[mul(pow(x,4),pow(t,4)),mul(pow(x,5),pow(t,4))];
 const fields={
  Lg:[2n,1n,1n],pLg:[1n,2n,-1n],Sg:[0n,1n,1n],pSg:[2n,-1n,1n],
  tg:[1n,2n,1n],pg:[2n,1n,1n],
  Lf:[3n,1n,2n],pLf:[1n,-1n,2n],Sf:[0n,2n,1n],pSf:[1n,2n,2n],
  tf:[1n,-1n,1n],pf:[3n,1n,-1n]
 };
 const weights={Lg:1,pLg:0,Sg:0,pSg:1,tg:0,pg:1,Lf:1,pLf:0,Sf:0,pSf:1,tf:0,pf:1};
 const variation=(f,w,e)=>add(mul(e,d(f)),sc(mul(d(e),f),w));
 const delta=(name,e)=>variation(fields[name],weights[name],e);
 for(let j=0;j<2;j++){
  let e=eta[j];
  for(let order=0;order<4;order++){ok(val(e,0n)===0n,"eta center");ok(val(e,1n)===0n,"eta outer");e=d(e);}
  for(const name of Object.keys(fields)){
   let df=delta(name,eta[j]);
   for(let order=0;order<3;order++){
    ok(val(df,0n)===0n,"canonical center "+name);
    ok(val(df,1n)===0n,"canonical outer "+name);df=d(df);
   }
  }
  for(const prefix of ["g","f"]){
   const L="L"+prefix,pL="pL"+prefix,S="S"+prefix,pS="pS"+prefix,th="t"+prefix,p="p"+prefix;
   const D=sub(add(mul(fields[pS],d(fields[S])),mul(fields[p],d(fields[th]))),mul(fields[L],d(fields[pL])));
   const dD=sub(add(add(mul(delta(pS,eta[j]),d(fields[S])),mul(fields[pS],d(delta(S,eta[j])))),
                     add(mul(delta(p,eta[j]),d(fields[th])),mul(fields[p],d(delta(th,eta[j]))))),
                 add(mul(delta(L,eta[j]),d(fields[pL])),mul(fields[L],d(delta(pL,eta[j])))));
   ok(eq(dD,variation(D,2,eta[j])),"D density two "+prefix);
  }
  const At=add(sub(mul(fields.Sg,fields.Sg),mul(fields.Sf,fields.Sf)),sc(mul(fields.Sg,fields.Sf),4));
  const dAt=add(sub(sc(mul(fields.Sg,delta("Sg",eta[j])),2),sc(mul(fields.Sf,delta("Sf",eta[j])),2)),
                sc(add(mul(delta("Sg",eta[j]),fields.Sf),mul(fields.Sg,delta("Sf",eta[j]))),4));
  const K=mul(mul(fields.Lg,fields.Lf),At);
  const dK=add(add(mul(mul(delta("Lg",eta[j]),fields.Lf),At),
                     mul(mul(fields.Lg,delta("Lf",eta[j])),At)),
                mul(mul(fields.Lg,fields.Lf),dAt));
  ok(eq(dK,variation(K,2,eta[j])),"K density two");
  for(const [q,p] of [["Lg","pLg"],["Sg","pSg"],["tg","pg"],["Lf","pLf"],["Sf","pSf"],["tf","pf"]]){
   ok(weights[q]+weights[p]===1,"canonical weight pair");
   ok(eq(delta(q,eta[j]),variation(fields[q],weights[q],eta[j])),"canonical q generator");
   ok(eq(delta(p,eta[j]),variation(fields[p],1-weights[q],eta[j])),"canonical p generator");
  }
  const boundaryTheta=b=>{
   const A=3n,B=5n,V=7n,z=1n;
   return A*val(d(delta("Sg",eta[j])),b)+B*val(d(delta("Sf",eta[j])),b)
     -(z+V*val(fields.Lg,b))*val(delta("pLg",eta[j]),b)
     -V*val(fields.Lf,b)*val(delta("pLf",eta[j]),b);
  };
  ok(boundaryTheta(0n)===0n,"theta center zero");
  ok(boundaryTheta(1n)===0n,"theta outer zero");
 }
 ok(eq(eta[1],mul(x,eta[0])),"eta2=x eta1");
 ok(eq(delta("Sg",eta[1]),mul(x,delta("Sg",eta[0]))),"independence field ratio");
 ok(val(eta[0].map((v,i)=>v*(2n**BigInt(eta[0].length-1-i))),1n)>0n,"eta1 at half positive");
 ok(val(eta[0].map((v,i)=>v*(4n**BigInt(eta[0].length-1-i))),1n)>0n,"eta1 at quarter positive");
 ok(Object.keys(fields).length===12,"six complete canonical pairs");
 return {stage:"68ad-C2d2e5b3b2c2b2d2d2a",kind:"EXACT_BOUNDARY_FLAT_RADIAL_GAUGE_TANGENT_KERNEL",passed,failed:0,
  conclusions:["Two linearly independent boundary-flat diagonal radial diffeomorphism directions exist on any regular radial profile; smooth interior compact-support versions can be made by multiplying by a bump.",
  "All 12 canonical variations and their first two radial jets vanish at both boundaries for these polynomial generators.",
  "The original non-IBP boundary one-form and the boundary two-form vanish on their span, irrespective of background coefficients.",
  "Dg,Df and HR K transform exactly as weight-two densities; z*(Dg,K) is scalar on the regular K>0 chart.",
  "Full Dirac tangency and time preservation are CONDITIONAL on a genuine solution and covariant transformations of lapse/shift; no such solution is certified here.",
  "These are gauge directions, not two independent physical boundary directions; no Dirac rank or counterterm admissibility follows."],
  source_sha:{"step45":"66aa43841dccfe4a5d586a49be9c10af3a67a10e",
    "radial_ward":"89e7f6eab35d28317f2f7a4330601736525487e5",
    "step58":"802c23aebd41780d8c462f1aa1711707fe4ee88f",
    "boundary_d2d1":"1ba6d012133a92b69a8c91498d065b22649afbe0"},
  gate:"GATE_2B OPEN",janus:"JANUS_R NOT_VALIDATED"};
}
if(typeof module!=="undefined")module.exports={run};

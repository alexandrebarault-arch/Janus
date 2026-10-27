"use strict";
// JANUS 68ad-C2d2e5b3b2b2b: exact rational structural tangent checks.
// This is NOT an execution of the original Step45/46/49/55 Python engines.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a||1n;}
class Q{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);this.n=n/g;this.d=d/g;}
 static of(v){if(v instanceof Q)return v;let s=String(v);if(s.includes("/")){let a=s.split("/");return new Q(a[0],a[1]);}if(s.includes(".")){let neg=s.startsWith("-");let x=neg?s.slice(1):s;let p=x.split(".");return new Q((neg?"-":"")+(p[0]+p[1]),10n**BigInt(p[1].length));}return new Q(s);}
 add(v){v=Q.of(v);return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(v){return this.add(Q.of(v).neg());}
 mul(v){v=Q.of(v);return new Q(this.n*v.n,this.d*v.d);}
 div(v){v=Q.of(v);return new Q(this.n*v.d,this.d*v.n);}
 pow(n){let z=Q.of(1),v=this;for(let i=0;i<n;i++)z=z.mul(v);return z;}
 eq(v){v=Q.of(v);return this.n===v.n&&this.d===v.d;}
 gt(v){v=Q.of(v);return this.n*v.d>v.n*this.d;}
 str(){return this.d===1n?String(this.n):this.n+"/"+this.d;}
 num(){return Number(this.n)/Number(this.d);}
}
const q=Q.of;
const y=q("0.5787707228025044"),mf=q("0.10879548725").pow(2),a0=q("0.4"),b0=a0.mul(y),mg=q(1),z1=q("0.004");
const c=mf.mul(b0).div(mg.mul(a0)); // exact dU0/dPg from Step49
function center(P){return mf.mul(b0).mul(q(P).div(mg.mul(a0)).sub(z1.mul(2)));}
const alpha=q("2/7"),beta=q("3/11"),gamma=q("5/13");
function series(P,N=9){P=q(P);let u=[c.mul(P)];for(let n=1;n<N;n++){let numerator=beta.mul(u[n-1]);if(n===1)numerator=numerator.add(alpha).add(gamma.mul(P));u.push(numerator.div(2*n+3));}return u;}
function tangent(N=9){let v=[c];for(let n=1;n<N;n++){let numerator=beta.mul(v[n-1]);if(n===1)numerator=numerator.add(gamma);v.push(numerator.div(2*n+3));}return v;}
function radial(s,P){s=q(s);P=q(P);let cg=q("0.0015"),kg=q("0.0012"),Dbar=q("5/2");
 let ug=q(1).add(cg.mul(s)),Lg=a0.mul(ug.pow(2)),Sgr=a0.mul(ug).mul(q(1).add(q(5).mul(cg).mul(s)));
 let Gprime=q(2).mul(P).mul(q(1).add(q(5).mul(cg).mul(s))),rho=q(1).add(P.pow(2));
 let pSg=s.mul(Dbar).add(Lg.mul(Gprime)).sub(rho.mul(s).mul(kg).mul(Lg)).div(Sgr);
 let Dg=pSg.mul(Sgr).sub(Lg.mul(Gprime)).add(rho.mul(s).mul(kg).mul(Lg));
 return {Dg,Dbar,Lg,Sgr,pSg};
}
function run(){
 let checks=[];function ck(b,name){if(!b)throw Error("FAILED "+name);checks.push(name);}
 ck(c.eq("274023815147385251710689588080861/40000000000000000000000000000000000"),"exact_physical_center_derivative");
 ck(c.gt(0),"nonzero_center_tangent");
 const P=q("-2/5"),e=q("1/101"),u=series(P),up=series(P.add(e)),v=tangent();
 ck(center(P.add(e)).sub(center(P)).eq(c.mul(e)),"Step49_center_Pg_parameter_difference");
 ck(q(3).mul(c).eq(q(3).mul(mf).mul(b0).div(mg.mul(a0))),"G_Pg_center_3c");
 ck(v[0].eq(c),"regular_indicial_center");
 for(let n=0;n<9;n++)ck(up[n].sub(u[n]).div(e).eq(v[n]),"exact_tangent_series_"+n);
 for(let n=1;n<9;n++){
   let lhs=q(2*n+3).mul(u[n]);
   let rhs=beta.mul(u[n-1]).add(n===1?alpha.add(gamma.mul(P)):q(0));
   ck(lhs.eq(rhs),"full_radial_model_ode_coefficient_"+n);
 }
 for(let n=1;n<9;n++){
   let lhs=q(2*n+3).mul(v[n]);
   let rhs=beta.mul(v[n-1]).add(n===1?gamma:q(0));
   ck(lhs.eq(rhs),"linearized_model_ode_coefficient_"+n);
 }
 let r=q("3/5"),s=r.pow(2),p1=q("-1/2"),p2=p1.add(e),g1=radial(s,p1),g2=radial(s,p2);
 ck(g1.Dg.eq(s.mul(g1.Dbar)),"Step55_g_radial_reconstruction_P1");
 ck(g2.Dg.eq(s.mul(g2.Dbar)),"Step55_g_radial_reconstruction_P2");
 ck(g2.Dg.eq(g1.Dg),"Step55_Dg_independent_of_Pg");
 let K=s.mul(2),z=r,root=q("4/5");
 ck(r.mul(g1.Dg).eq(K.mul(z).div(root)),"Fz_exact_rational_synthetic_witness");
 let boundary=q(0),pow=q(1),S=q("289/400");
 for(let n=0;n<v.length;n++){boundary=boundary.add(v[n].mul(pow));pow=pow.mul(S);}
 ck(boundary.gt(0),"toy_outer_trace_nonzero_not_physical_boundary");
 let homogeneous=q(0);for(let n=1;n<9;n++)homogeneous=beta.mul(homogeneous).div(2*n+3);
 ck(homogeneous.eq(0),"fixed_background_regular_homogeneous_tangent_zero");
 return {step:"68ad-C2d2e5b3b2b2b",kind:"EXACT_STRUCTURAL_PARAMETER_TANGENT_CHECKS_NOT_ORIGINAL_PHYSICAL_ENGINE",passed:checks.length,failed:0,checks,physical_center_dU0_dPg:c.str(),toy_outer_tangent_partial_sum:boundary.str(),toy_outer_tangent_partial_sum_display:boundary.num(),radial_synthetic_Dg:g1.Dg.str(),status:{GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"},limits:"Toy analytic G tests the exact indicial/linearization structure, not the original Step55 G(s,U,Pg). The radial reconstruction check uses synthetic rational data; no original Python engine or complete Dirac matrix executed."};
}
if(typeof module!=="undefined")module.exports={Q,q,c,center,series,tangent,radial,run};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));

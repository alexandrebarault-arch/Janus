'use strict';
// Exact boundary differential of the ORIGINAL Step46 f-primary reconstruction.
// Fixed geometry, not the derivative of the solved Step55 U(s,lambda).
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q {
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 static of(x){if(x instanceof Q)return x;const t=String(x);if(t.includes('/')){const [a,b]=t.split('/');return new Q(a,b);}if(t.includes('.')){const neg=t[0]==='-';const u=neg?t.slice(1):t;const [a,b]=u.split('.');return new Q((neg?'-':'')+(a||'0')+b,10n**BigInt(b.length));}return new Q(t);}
 add(x){x=Q.of(x);return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(x){return this.add(Q.of(x).neg());}
 mul(x){x=Q.of(x);return new Q(this.n*x.n,this.d*x.d);}
 div(x){x=Q.of(x);return new Q(this.n*x.d,this.d*x.n);}
 cmp(x){x=Q.of(x);const a=this.n*x.d,b=x.n*this.d;return a<b?-1:a>b?1:0;}
 toString(){return this.d===1n?String(this.n):String(this.n)+'/'+String(this.d);}
}
const q=Q.of;
class AD {
 constructor(v,d=0){this.v=q(v);this.d=q(d);}
 static of(x){return x instanceof AD?x:new AD(x);}
 add(x){x=AD.of(x);return new AD(this.v.add(x.v),this.d.add(x.d));}
 neg(){return new AD(this.v.neg(),this.d.neg());}
 sub(x){return this.add(AD.of(x).neg());}
 mul(x){x=AD.of(x);return new AD(this.v.mul(x.v),this.d.mul(x.v).add(this.v.mul(x.d)));}
 div(x){x=AD.of(x);return new AD(this.v.div(x.v),this.d.mul(x.v).sub(this.v.mul(x.d)).div(x.v.mul(x.v)));}
}
function jacobian(p){
 const R=q(p.R),s=R.mul(R),mf=q(p.mf),Lf=q(p.Lf),Sfr=q(p.Sfr),kf=q(p.kf),U=q(p.U),V=q(p.V),beta=q(p.beta),db=q(p.Dbar),w=q(p.Wfbar),rf=q(p.Rf),z=q(p.z1);
 const den=beta.add(kf.mul(s).mul(U).div(q(2).mul(mf).mul(Sfr)));
 const numer=U.mul(U).div(q(4).mul(mf).mul(Lf)).sub(U.mul(V.sub(s.mul(db).div(Lf))).div(q(2).mul(mf).mul(Sfr))).sub(mf.mul(Lf).mul(Lf).mul(Lf).mul(rf).div(2)).add(s.mul(z).mul(db).div(Lf)).add(w);
 const rho=numer.neg().div(den);
 const dden=kf.mul(s).div(q(2).mul(mf).mul(Sfr));
 const dnum=U.div(q(2).mul(mf).mul(Lf)).sub(V.sub(s.mul(db).div(Lf)).div(q(2).mul(mf).mul(Sfr)));
 const H=dnum.add(rho.mul(dden)).neg().div(den);
 const chi=R.mul(U).div(q(2).mul(mf).mul(Sfr).mul(den));
 return {den,rho,H,chi,R,s,mf,Lf,Sfr,kf,U,V,beta,db,w,rf,z};
}
function dualCheck(p,du,dv){
 const c=jacobian(p),{R,s,mf,Lf,Sfr,kf,beta,db,w,rf,z,H,chi}=c;
 const u=new AD(c.U,du),v=new AD(c.V,dv);
 const den=AD.of(beta).add(u.mul(kf.mul(s).div(q(2).mul(mf).mul(Sfr))));
 const numer=u.mul(u).div(q(4).mul(mf).mul(Lf)).sub(u.mul(v.sub(s.mul(db).div(Lf))).div(q(2).mul(mf).mul(Sfr))).sub(mf.mul(Lf).mul(Lf).mul(Lf).mul(rf).div(2)).add(s.mul(z).mul(db).div(Lf)).add(w);
 const rho=numer.neg().div(den);
 const pf=rho.mul(s);
 const psf=v.mul(R.mul(Lf)).sub(R.mul(s).mul(db)).sub(rho.mul(R.mul(s).mul(kf).mul(Lf))).div(Sfr);
 const dplf=s.mul(q(du)),dplfp=R.mul(q(dv));
 const dpf=H.mul(dplf).add(chi.mul(dplfp));
 const dpsf=Lf.div(Sfr).mul(dplfp).sub(R.mul(kf).mul(Lf).div(Sfr).mul(dpf));
 return {pf:pf.d,pSf:psf.d,expectedPf:dpf,expectedPSf:dpsf};
}
function physicalChiBounds(){
 // Prior Step55 b2 exact uniform U enclosure; no new ODE execution.
 const R=q('17/20'),s=R.mul(R),a=q('2/5'),b=a.mul(q('0.5787707228025044'));
 const mf=q('0.10879548725').mul(q('0.10879548725'));
 const cf=q('-0.0012'),kf=q('-0.0016');
 const Sfr=b.mul(q(1).add(cf.mul(s))).mul(q(1).add(q(5).mul(cf).mul(s)));
 const ulo=q('-10707594192153122134265173/2000000000000000000000000000');
 const uhi=q('-1146420876631433922729177/250000000000000000000000000');
 // sqrt(1+x) in [1,1+x/2] for x>=0, and kf*U>0.
 const dlo=q(1).add(kf.mul(s).mul(uhi).div(q(2).mul(mf).mul(Sfr)));
 const dhi=q(1).add(kf.mul(kf).mul(s).div(2)).add(kf.mul(s).mul(ulo).div(q(2).mul(mf).mul(Sfr)));
 const clo=R.mul(ulo).div(q(2).mul(mf).mul(Sfr).mul(dlo));
 const chi=R.mul(uhi).div(q(2).mul(mf).mul(Sfr).mul(dhi));
 if(!(ulo.cmp(uhi)<0&&dlo.cmp(1)>0&&dhi.cmp(dlo)>0&&clo.cmp(q('-21/25'))>0&&chi.cmp(q('-71/100'))<0))throw Error('physical boundary chi certificate failed');
 return {U_lower:ulo.toString(),U_upper:uhi.toString(),D_lower:dlo.toString(),D_upper:dhi.toString(),chi_lower:clo.toString(),chi_upper:chi.toString(),simple_chi_interval:['-21/25','-71/100']};
}
function certificate(){return {step:'68ad-C2d2e5b3b2c2b3c2a',scope:'FIXED_GEOMETRY_STEP46_F_BOUNDARY_DIFFERENTIAL_NOT_SOLVED_VARIATIONAL_ODE',R:'17/20',lambda:['-1/5000','1/5000'],chi:physicalChiBounds(),identities:['delta_pf=H*delta_pLf+chi*delta_pLf_prime','delta_pSf=(Lf/Sfr)*delta_pLf_prime-(R*kf*Lf/Sfr)*delta_pf'],rank_of_formal_trace_map:2,rank_of_one_parameter_solution_tangent:'AT_MOST_1_NOT_COMPUTED',authentic_G_U_G_Pg:'NOT_EXECUTED',v_R:'NOT_COMPUTED',physical_boundary_conditions:'NOT_SELECTED',GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'};}
module.exports={Q,AD,jacobian,dualCheck,physicalChiBounds,certificate};
if(require.main===module)console.log(JSON.stringify(certificate(),null,2));

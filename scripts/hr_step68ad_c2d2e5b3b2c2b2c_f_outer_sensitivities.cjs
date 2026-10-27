'use strict';
// Rigorous, dependency-safe rational interval propagation of prior authentic
// Step45/46/55 certificates through the exact Step46 f-primary Jacobian.
// NO original physical Python reexecution in this standalone certificate.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
class Q {
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}let g=gcd(n,d);this.n=n/g;this.d=d/g;}
 static of(x){if(x instanceof Q)return x;let s=String(x);if(s.includes('/')){let [n,d]=s.split('/');return new Q(n,d);}if(s.includes('.')){let sign=s[0]==='-'?-1n:1n;if(sign<0)s=s.slice(1);let [a,b]=s.split('.');return new Q(sign*BigInt((a||'0')+b),10n**BigInt(b.length));}return new Q(s);}
 add(x){x=Q.of(x);return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(x){return this.add(Q.of(x).neg());}
 mul(x){x=Q.of(x);return new Q(this.n*x.n,this.d*x.d);}
 div(x){x=Q.of(x);return new Q(this.n*x.d,this.d*x.n);}
 cmp(x){x=Q.of(x);let z=this.n*x.d-x.n*this.d;return z<0n?-1:z>0n?1:0;}
 toString(){return this.d===1n?String(this.n):this.n+'/'+this.d;}
}
const q=Q.of;
class I {
 constructor(lo,hi=lo){this.lo=q(lo);this.hi=q(hi);if(this.lo.cmp(this.hi)>0)throw Error('inverted interval');}
 static of(x){return x instanceof I?x:new I(x);}
 add(x){x=I.of(x);return new I(this.lo.add(x.lo),this.hi.add(x.hi));}
 neg(){return new I(this.hi.neg(),this.lo.neg());}
 sub(x){return this.add(I.of(x).neg());}
 mul(x){x=I.of(x);let v=[this.lo.mul(x.lo),this.lo.mul(x.hi),this.hi.mul(x.lo),this.hi.mul(x.hi)].sort((a,b)=>a.cmp(b));return new I(v[0],v[3]);}
 div(x){x=I.of(x);if(x.lo.cmp(0)<=0&&x.hi.cmp(0)>=0)throw Error('interval division by zero');return this.mul(new I(q(1).div(x.hi),q(1).div(x.lo)));}
 inside(a,b){return this.lo.cmp(q(a))>0&&this.hi.cmp(q(b))<0;}
}
const i=I.of;
const provenance={
 'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
 'numerics/hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
 'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
 'research/reports/gate2b-step68ad-C2d2e5b3b2c2b2-authentic-Pg-fdust-tube.json':'012e70e49b41cc3180da423c3962d279e3909a26',
 'research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2b2b-authentic-variational-barrier.json':'c8100b22ec0f169af2151f4308eea0bc6ba26c80',
 'research/reports/gate2b-step68ad-C2d2e5b3b2c2b3b-f-traces-lapses.json':'4595292ee18c7f71cf773338177321a2b617592d',
 'research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2a-f-boundary-jacobian.json':'e7966302ed157695df64fc887883a558d24e87ef'
};
function compute(){
 const R=i('17/20'),s=R.mul(R),mf=i(q('0.10879548725').mul('0.10879548725'));
 const a=i('2/5'),b=a.mul('0.5787707228025044'),cf=i('-0.0012'),kf=i('-0.0016');
 const Lf=b.mul(i(1).add(cf.mul(s))).mul(i(1).add(cf.mul(s)));
 const Sfr=b.mul(i(1).add(cf.mul(s))).mul(i(1).add(cf.mul(5).mul(s)));
 // b2 global enclosures (safe at the outer boundary, though deliberately broad).
 const U=new I('-10707594192153122134265173/2000000000000000000000000000','-1146420876631433922729177/250000000000000000000000000');
 const V=new I('-31475070089799984705831899/2500000000000000000000000000','-61130791189474633664185037/10000000000000000000000000000');
 const rho=new I('13681002401623193480723629/125000000000000000000000000','1269204970466940095332675403/10000000000000000000000000000');
 // b3b original Step55 Dbar(R) enclosure.
 const Dbar=new I(
 '1119310171393987546506900679860822682658425608511020400584104222446054158868507637619389388275738047532747799414279/1220703125000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
 '124367796821554171834100075540091409184269512056780044509344913605117128763167515291043265363970894170305311046031/135632324218750000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000');
 // b2b original-G automatic differentiation and invariant variational barrier.
 const GU=new I('-10010994946700078347820701723/10000000000000000000000000000','-2484848415045686623953723383/2500000000000000000000000000');
 const GP=new I('8174164999902538951243999/400000000000000000000000000','102891129278229903179165297/5000000000000000000000000000');
 const v=new I('681/100000','689/100000');
 const dV=GU.mul(v).add(GP);
 // sqrt(1+x) in [1,1+x/2], x=kf^2*s >=0, exact rational bounds.
 const beta=new I(1,q(1).add(q('-0.0016').mul('-0.0016').mul('289/400').div(2)));
 const D=beta.add(kf.mul(s).mul(U).div(i(2).mul(mf).mul(Sfr)));
 const DU=kf.mul(s).div(i(2).mul(mf).mul(Sfr));
 const AU=U.div(i(2).mul(mf).mul(Lf))
   .sub(V.sub(s.mul(Dbar).div(Lf)).div(i(2).mul(mf).mul(Sfr)));
 const H=AU.add(rho.mul(DU)).neg().div(D);
 const chi=R.mul(U).div(i(2).mul(mf).mul(Sfr).mul(D));
 const dpLf=s.mul(v),dpLfPrime=R.mul(dV);
 const dpf=H.mul(dpLf).add(chi.mul(dpLfPrime));
 const dpSf=Lf.div(Sfr).mul(dpLfPrime)
   .sub(R.mul(kf).mul(Lf).div(Sfr).mul(dpf));
 return {R,s,Lf,Sfr,U,V,rho,Dbar,GU,GP,v,beta,D,H,chi,dV,dpLf,dpLfPrime,dpf,dpSf};
}
function floorDiv(n,d){if(d<=0n)throw Error('positive divisor required');return n>=0n?n/d:-((-n+d-1n)/d);}
function ceilDiv(n,d){return -floorDiv(-n,d);}
function outward(x){let scale=1000000000000n;return [
 new Q(floorDiv(x.lo.n*scale,x.lo.d),scale).toString(),
 new Q(ceilDiv(x.hi.n*scale,x.hi.d),scale).toString()
];}
function certificate(){
 const x=compute();
 for(let [k,lo,hi] of [
 ['dV','0.0135','0.0139'],['dpLf','0.0049','0.0050'],
 ['dpLfPrime','0.0115','0.0118'],['dpf','-0.020','-0.011'],
 ['dpSf','0.0115','0.0118'],['H','-2','-0.6'],['chi','-0.84','-0.71']
 ])if(!x[k].inside(lo,hi))throw Error('physical interval certificate failed '+k);
 if(!x.D.inside('1','1.01'))throw Error('f primary denominator');
 const keys=['GU','GP','v','U','V','rho','Dbar','D','H','chi','dV','dpLf','dpLfPrime','dpf','dpSf'];
 return {
  step:'68ad-C2d2e5b3b2c2b2c',scope:'SPATIAL_AUTHENTIC_TUBE_PROPAGATED_THROUGH_EXACT_STEP46_JACOBIAN',
  radius:'17/20',s:'289/400',lambda:['-1/5000','1/5000'],
  original_physical_sources_and_prior_certificate_blobs:provenance,
  bounds_rounded_outward_1e_minus_12:Object.fromEntries(keys.map(k=>[k,outward(x[k])])),
  strict_signs:{dV:'POSITIVE',dpLf:'POSITIVE',dpLfPrime:'POSITIVE',dpf:'NEGATIVE',dpSf:'POSITIVE'},
  conditional_fixed_single_trace:'Each individual f momentum trace fixed to its lambda=0 value forces lambda=0 within this certified one-parameter family, by the mean value theorem.',
  derivative_identities:[
   'dV=GU*v+GP','dpLf=s*v','dpLfPrime=R*dV',
   'dpf=H*dpLf+chi*dpLfPrime',
   'dpSf=(Lf/Sfr)*dpLfPrime-(R*kf*Lf/Sfr)*dpf'
  ],
  original_python_reexecuted_this_step:false,
  prior_original_python_execution_certified_by_b2_and_b2b:true,
  boundary_conditions_selected:false,full_dirac_oracle_executed:false,
  caveat:'Bounds use global physical interval enclosures and ignore correlations safely; only spherical spatial constrained family, conditional on Step49 and b2/b2b.',
  GATE_2B:'OPEN',JANUS_R:'NOT_VALIDATED'
 };
}
module.exports={Q,I,compute,outward,certificate,provenance};
if(require.main===module)console.log(JSON.stringify(certificate(),null,2));

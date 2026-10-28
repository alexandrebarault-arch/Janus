"use strict";
/* JANUS d2d2b2: exact-rational boundary-clock flux and boundary-condition audit.
   Based on SHA-authenticated original Step37/45/55 and d2a/d2d2b1.
   Not a temporal Dirac gauge classification or physical counterterm. */
function certificate(){
  let checks=0;
  function ok(x,msg){if(!x)throw Error("FAIL "+msg);checks++;}
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a||1n;}
  class F {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    static of(v){if(v instanceof F)return v;let s=String(v),neg=s[0]==="-";if(neg)s=s.slice(1);let p=s.split(".");let d=10n**BigInt(p[1]?.length||0);return new F((neg?-1n:1n)*BigInt(p.join("")),d);}
    add(b){b=F.of(b);return new F(this.n*b.d+b.n*this.d,this.d*b.d);}
    neg(){return new F(-this.n,this.d);}
    sub(b){return this.add(F.of(b).neg());}
    mul(b){b=F.of(b);return new F(this.n*b.n,this.d*b.d);}
    div(b){b=F.of(b);return new F(this.n*b.d,this.d*b.n);}
    pow(k){if(k===0)return F.of(1);let v=F.of(1);for(let i=0;i<k;i++)v=v.mul(this);return v;}
    cmp(b){b=F.of(b);let x=this.n*b.d-b.n*this.d;return x<0n?-1:x>0n?1:0;}
    eq(b){return this.cmp(b)===0;}
    gt(b){return this.cmp(b)>0;}
    lt(b){return this.cmp(b)<0;}
    toString(){return this.n+"/"+this.d;}
  }
  const f=F.of, zero=f(0), one=f(1), two=f(2);
  const r=f("0.85"),s=r.pow(2),a=f("0.4"),y=f("0.5787707228025044"),b=a.mul(y);
  const cg=f("0.0015"),cf=f("-0.0012"),kg=f("0.0012"),kf=f("-0.0016"),z=f("0.004").mul(r);
  const Lg=a.mul(one.add(cg.mul(s)).pow(2)), Lf=b.mul(one.add(cf.mul(s)).pow(2));
  const xg=kg.mul(r),xf=kf.mul(r),ug=xg.pow(2),uf=xf.pow(2);
  // Exact rational enclosure 1-u/2 <= 1/sqrt(1+u) <= 1 for 0<=u<=2.
  // Square the lower bound: (1-u/2)^2(1+u) = 1-u^2(3-u)/4 <= 1.
  for(const [label,u] of [["g",ug],["f",uf]]){
    ok(u.gt(0),label+" u positive");ok(u.lt(2),label+" u < 2");
    const lo=one.sub(u.div(two));
    ok(lo.gt(0),label+" lower inverse sqrt positive");
    ok(lo.pow(2).mul(one.add(u)).cmp(one)<=0,label+" exact square lower bound");
    ok(one.add(u).gt(1),label+" inverse sqrt upper bound");
    ok(one.sub(u.pow(2).mul(f(3).sub(u)).div(f(4))).eq(lo.pow(2).mul(one.add(u))),label+" polynomial identity");
  }
  const agBase=xg.div(Lg),afBase=xf.div(Lf);
  const agLo=agBase.mul(one.sub(ug.div(two))),agHi=agBase;
  const afLo=afBase,afHi=afBase.mul(one.sub(uf.div(two)));
  const ALo=agLo.add(z.div(Lg)),AHi=agHi.add(z.div(Lg));
  const B=z.div(Lf),DLo=afLo,DHi=afHi;
  ok(r.eq(new F(17n,20n)),"R exact");ok(s.eq(new F(289n,400n)),"s exact");
  ok(a.gt(0)&&b.gt(0),"metric scaling positive");
  ok(Lg.gt(0)&&Lf.gt(0),"lapses geometry positive");
  ok(kg.gt(0)&&kf.lt(0),"opposite dust slopes");
  ok(z.gt(0)&&z.lt(1),"shift regular");
  ok(agBase.gt(0)&&afBase.lt(0),"raw dust velocities opposite");
  ok(agLo.gt(0)&&agHi.gt(agLo),"g coefficient strictly positive");
  ok(afLo.lt(afHi)&&afHi.lt(0),"f coefficient strictly negative");
  ok(ALo.gt(0)&&AHi.gt(ALo),"g N coefficient strictly positive");
  ok(B.gt(0),"g M coefficient strictly positive");
  ok(DHi.lt(0),"f M coefficient strictly negative");
  // Jg/pg=N*A+M*B+V, Jf/pf=M*D+V, with A>0,B>0,D<0.
  // For N,M>0, Jg=0 requires V<0, Jf=0 requires V>0.
  for(const [N,M] of [[f(1),f(1)],[f(2),f(3)],[f("0.0001"),f("1000")]]){
    const VgHi=N.mul(AHi).add(M.mul(B)).neg();
    const VfLo=M.mul(DHi).neg();
    const gapLo=N.mul(ALo).add(M.mul(B.sub(DHi)));
    ok(VgHi.lt(0),"V required for Jg=0 is negative");
    ok(VfLo.gt(0),"V required for Jf=0 is positive");
    ok(gapLo.gt(0),"gap between incompatible V solutions positive");
    ok(VfLo.sub(VgHi).gt(0),"separated root intervals");
  }
  // For independent N,M even with V fixed, flux map has rank 2:
  // det [[pg*A,pg*B],[0,pf*D]]=pg*pf*A*D != 0 if pg,pf>0.
  ok(ALo.mul(DHi).lt(0),"N/M flux determinant negative");
  ok(AHi.mul(DLo).lt(0),"N/M determinant other endpoint negative");
  // V column=(pg,pf) is nonzero in both rows, N column=(pg*A,0).
  ok(ALo.gt(0),"N and V columns linearly independent");
  // Boundary data on constant-shift plane: each fixed clock kills its shift.
  const cases=[
    {name:"no fixed clock values",matrix:[],rank:0,remaining:2},
    {name:"fix tg at center",matrix:[[1,0]],rank:1,remaining:1},
    {name:"fix tf at outer",matrix:[[0,1]],rank:1,remaining:1},
    {name:"fix both at center",matrix:[[1,0],[0,1]],rank:2,remaining:0},
    {name:"fix tg-tf at either boundary",matrix:[[1,-1]],rank:1,remaining:1},
    {name:"fix tg-tf and tg+tf",matrix:[[1,-1],[1,1]],rank:2,remaining:0},
    {name:"fix tg at center and tf at outer",matrix:[[1,0],[0,1]],rank:2,remaining:0}
  ];
  function rank2(mat){if(!mat.length)return 0;if(mat.some(row=>row[0]!==0||row[1]!==0)){
    for(let i=0;i<mat.length;i++)for(let j=i+1;j<mat.length;j++)
      if(mat[i][0]*mat[j][1]-mat[i][1]*mat[j][0]!==0)return 2;
    return 1;}return 0;}
  for(const c of cases){ok(rank2(c.matrix)===c.rank,"boundary rank "+c.name);
    ok(2-c.rank===c.remaining,"surviving shifts "+c.name);}
  // Fixed positive dust momenta: no nonzero clock variation annihilates
  // the flux for ALL independently variable N,M,V (rank 2).
  ok(ALo.gt(0)&&DHi.lt(0),"full-multiplier flux annihilator trivial");
  // At fixed N,M,V, the clock-plane one-form is exact, but this does NOT
  // establish a counterterm for the full canonical/multiplier variation.
  const tg=f(2),tf=f(3),N=f(1),M=f(1),V=f(0);
  const JgLo=N.mul(ALo).add(M.mul(B)).add(V);
  const JfHi=M.mul(DHi).add(V);
  ok(JgLo.gt(0),"g clock flux positive at V=0");
  ok(JfHi.lt(0),"f clock flux negative at V=0");
  ok(JgLo.mul(tg).add(JfHi.mul(tf)).eq(tg.mul(JgLo).add(tf.mul(JfHi))),"clock-plane primitive algebra");
  const result={
    step:"68ad-C2d2e5b3b2c2b2d2d2b2",
    assertions_passed:checks,assertions_failed:0,
    input_source_blobs:{
      step37:"005449ade6e3582e3b9a5c3374a881a77e73e3f6",
      step45:"66aa43841dccfe4a5d586a49be9c10af3a67a10e",
      step55:"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",
      step58:"802c23aebd41780d8c462f1aa1711707fe4ee88f",
      original_boundary:"94bd7e089ebb0978569361c03a4f3ab950b950df",
      clock_translation:"1d973e04f296df9144f6ddef40681dd18342e28e"
    },
    exact_rational_enclosures:{
      A_g_N:[ALo.toString(),AHi.toString()],
      B_g_M:B.toString(),
      D_f_M:[DLo.toString(),DHi.toString()],
      r:r.toString(),z:z.toString()
    },
    proved:"At Step55 outer boundary with pg,pf,N,M positive, Jg=Jf=0 is impossible for any common diagonal V; independent lapse N,M clock-flux coefficient matrix has rank 2, so no nonzero fixed clock variation cancels flux for all lapse choices. Exact boundary-condition rank classification on constant-shift plane.",
    restrictions:"Original bare non-IBP Hamiltonian, no clock counterterm, Step55 outer dust slopes and z>0, positive lapses and dust momenta. Not a complete Dirac temporal gauge quotient.",
    not_proved:["physical temporal gauge classification","Hamiltonian improved differentiability","allowed counterterm under full variations","time preservation of clock boundary conditions","full Dirac rank/tertiaries/lapses","4D/stability/observables"],
    original_physics_reexecuted:false,
    scientific_status:{GATE_2B:"OPEN",JANUS_R:"NOT_VALIDATED"},
    boundary_cases:cases
  };
  return result;
}
if(typeof module!=="undefined"&&module.exports)module.exports={certificate};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(certificate(),null,2)+"\n");

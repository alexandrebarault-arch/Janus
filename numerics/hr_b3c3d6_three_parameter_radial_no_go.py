"""Exact restricted radial-closure no-go on a 3-parameter Step45/58 slice.

The polynomial certificate is independent of a numerical ODE. The optional
operator replay must be run against byte-authentic Step45/58 separately;
local independent reconstructions are NOT an original-engine replay.
"""
import sympy as S

a,b,c=S.symbols('a b c',real=True)
C=25*a+24*b+12
Hf=b*b-2*b*c-1
Frr=5625*a*a+4000*a*c+8600*a+1024*b+3712*c-1344
Hfr=75*a-192*b*b*c+256*b*c*c-256*b-176*c+160
Cr=375*a*a+640*a*b+920*a-384*b*c+192*b-128*c+160
P=204*b**3-72*b**2-141*b-56
T=144*b**3+224*b**2+b-20
U=4708409040*b*b+5217306528*b-2808576443
V=-6670246140*b*b+5338958712*b+2939061345
BEZOUT=98499053908

def certificate():
    aa=-(24*b+12)/25
    cc=(b*b-1)/(2*b)  # Hf=0 forces b != 0
    assert S.cancel(Frr.subs({a:aa,c:cc})-16*P/b)==0
    assert S.cancel(Cr.subs({a:aa,c:cc})+16*T/(5*b))==0
    assert S.expand(U*P+V*T)==BEZOUT
    assert S.resultant(P,T,b)==4727954587584
    assert list(S.groebner([C,Hf,Frr,Cr],a,b,c,order='grevlex'))==[S.S.One]
    return {'scope':'RESTRICTED_FROZEN_JETS_THREE_PARAMETER_SLICE_NOT_PHYSICAL_STEP55',
            'shell':'Fz=Fz_r=Hg=Hg_r=0',
            'secondary_conditions':'C=0,Hf=0',
            'radial_closure_test':'Fz_rr=0,C_r=0',
            'substitution':{'a':'-(24*b+12)/25','c':'(b**2-1)/(2*b)','b_nonzero':True},
            'P':str(P),'T':str(T),
            'resultant':str(S.resultant(P,T,b)),
            'bezout_constant':str(BEZOUT),
            'bezout_U':str(U),'bezout_V':str(V),
            'groebner_basis':['1'],
            'conclusion':'NO COMPLEX (a,b,c) solves all four conditions on this frozen-jet slice',
            'not_concluded':'No global Step55 no-go, no universal B_N factorization, no lapse BVP or Dirac result',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

def derive_from_operator(p,o):
    """Replay published original symbolic formulas or an explicitly labeled clone."""
    q=dict(zip(p['Q'],p['q'])); qp=dict(zip(p['Q'],p['dq']))
    params=p.get('parameters',tuple(p[k] for k in ('mg','mf','m2','b0','b1','b2','b3','b4','z','zr','zrr')))
    mg,mf,m2,b0,b1,b2,b3,b4,z,zr,zrr=params
    fields=(*o['q'],*o['qp'],*o['qpp'],*o['qppp'],*o['q4'],o['z'],o['zr'],o['zrr'],o['zrrr'],*params[:8])
    d={k:S.S.Zero for k in fields}
    for name in ('Lg','Lf','Sg','Sf'):d[q[name]]=S.S.One
    for k in (mg,mf,m2):d[k]=S.S.One
    d.update({b0:-5,b1:1,b4:-2,z:S.Rational(3,5),zr:a,qp['Sf']:b,qp['Lf']:c})
    for k in (qp['Sg'],q['pSg'],q['pLf'],q['pSf'],q['pf']):d[k]=S.S.One
    d[q['pg']]=S.Rational(7,4)
    x,w,v,u=qp['pLg'],o['qpp'][2],o['qpp'][1],o['qppp'][2]
    for k in (x,w,v,u):d.pop(k)
    def ev(expr):return S.cancel(expr.subs(d))
    F=o['Fz'];H=p['Hg'];Fr=o['Dt'](F);Hr=o['Dt'](H)
    for expr,k in ((F,x),(H,w),(Fr,v),(Hr,u)):
        ex=ev(expr)
        slope=S.diff(ex,k)
        assert slope!=0 and not slope.has(k)
        d[k]=S.factor(-ex.subs(k,0)/slope)
        assert S.cancel(ev(expr))==0
    opers=o.get('operator',o.get('outs'))
    targets={'C':-(25*a+24*b+12)/20,
             'Hf':Hf,
             'Fz_rr':-Frr/1024,
             'Hf_r':Hfr/64,
             'C_r':-Cr/320,
             'B_N':-3*(25*a+24*b+12)/100,
             'B_M':S.S.Zero,'E_N':S.S.Zero,'E_M':S.S.Zero}
    expressions={'C':o['C'],'Hf':p['Hf'],'Fz_rr':o['Dt'](Fr),
                 'Hf_r':o['Dt'](p['Hf']),'C_r':o['Dt'](o['C']),
                 'B_N':opers['N'][1],'B_M':opers['M'][1],
                 'E_N':opers['N'][2],'E_M':opers['M'][2]}
    for name,expr in expressions.items():
        assert S.cancel(ev(expr)-targets[name])==0,name
    return {'solved_jets':{str(k):str(d[k]) for k in (x,w,v,u)},
            'checked_polynomials':len(targets),
            'full_primary_and_first_derivatives':'EXACT_ZERO',
            'operator_source':'CALLER_SUPPLIED_CHECK_REQUIRED'}

if __name__=='__main__':
    import json
    print(json.dumps(certificate(),indent=2))

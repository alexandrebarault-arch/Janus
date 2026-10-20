"""Exact-rational continuous branch certificate for dust-only Candidate-C.

Certifies one regular positive quartic root y(a) for a in [0.025,1],
within y in (0.556,2.3), and the strict J(y)>1/2 lower bound.
Does NOT certify an on-shell NONHOMOTHETIC 4D solution or BD closure.
Decimal model parameters are interpreted as exact terminating rationals;
physical precision is no better than their given decimal calibration.
"""
from fractions import Fraction as F

BETAS = tuple(F(s) for s in ('0','1','-4.2383993109',
                              '13.6801214252','-38.5117901844'))
M2 = F('23.3348939346')
MG2 = F(1)
MF2 = F('0.10879548725')**2
CG = F('0.9')
Y0 = F('0.5568825591873054')
CF = 3*F('0.23958426762')*Y0**3
Y_LOW, Y_HIGH = F('0.556'), F('2.3')
A_LOW, A_HIGH = F('0.025'), F(1)


def evaluate(coeffs, y):
    y=F(y)
    z=F(0)
    for c in reversed(coeffs):
        z=z*y+c
    return z


def derivative(coeffs):
    return tuple(i*coeffs[i] for i in range(1,len(coeffs)))


def q_coefficients():
    """P(y,a)=M2*Q(y)+(MF2*CG*y-CF)/(3*a^3)=0."""
    b0,b1,b2,b3,b4=BETAS
    return (-b1/3,-b2, MF2*b1-b3,
            MF2*b2-b4/3, MF2*b3/3)


def j_value(y):
    _,b1,b2,b3,_=BETAS
    return b1+2*b2*y+b3*y*y


def t_of_y(y):
    """t = a^{-3} = 3*M2*Q(y)/(CF-MF2*CG*y)."""
    y=F(y)
    return 3*M2*evaluate(q_coefficients(),y)/(CF-MF2*CG*y)


def t_derivative_num(y):
    """t' numerator after extracting 3*M2 / (CF-MF2*CG*y)^2."""
    q=q_coefficients()
    return evaluate(derivative(q),y)*(CF-MF2*CG*y)+MF2*CG*evaluate(q,y)


def verified_bounds():
    """All proofs below are exact strict Fraction inequalities, not samples.

    Q'''(y)=6 q3+24 q4*y >0 on y>=Y_LOW because q3,q4>0.
    Q''(Y_LOW), Q'(Y_LOW), Q(Y_LOW)>0 hence each stays positive
    for y>=Y_LOW. D(y)=CF-MF2*CG*y>0 up to Y_HIGH.
    Thus t'(y)>0 and t(Y_LOW)<1<64000<t(Y_HIGH).
    J'(y)=2*(beta2+beta3*y)>0 for y>=Y_LOW, and
    J(Y_LOW)>1/2. By IVT, the calibrated quartic has exactly ONE
    positive branch root y in (Y_LOW,Y_HIGH) for every a in [0.025,1].
    Other roots OUTSIDE this interval are not excluded.
    """
    q=q_coefficients()
    d=derivative(q);dd=derivative(d)
    assert q[3]>0 and q[4]>0
    assert evaluate(q,Y_LOW)>0
    assert evaluate(d,Y_LOW)>0
    assert evaluate(dd,Y_LOW)>0
    assert CF-MF2*CG*Y_HIGH>0
    assert 0<t_of_y(Y_LOW)<1
    assert t_of_y(Y_HIGH)> A_LOW**(-3)
    assert t_derivative_num(Y_LOW)>0
    assert BETAS[2]+BETAS[3]*Y_LOW>0
    assert j_value(Y_LOW)>F(1,2)
    # y(1) is bracketed independently; the supplied Y0 agrees within
    # the precision of the input calibration, but is NOT taken as exact root.
    assert t_of_y(F('.55688'))<1<t_of_y(F('.55689'))
    return {'y_global_lower_strict': str(Y_LOW),
            'y_global_upper_strict': str(Y_HIGH),
            'J_global_lower_strict': '1/2',
            'J_at_lower':float(j_value(Y_LOW)),
            'J_at_y0':float(j_value(Y0)),
            't_lower':float(t_of_y(Y_LOW)),
            't_upper':float(t_of_y(Y_HIGH)),
            't_max':int(A_LOW**-3),
            'parameter_interpretation':'exact rational of supplied decimals'}


def unique_y_interval(a, iterations=85):
    """Exact dyadic nested bracket on certified branch (never np.roots)."""
    verified_bounds()
    a=F(a)
    if not A_LOW<=a<=A_HIGH:raise ValueError('a outside certified range')
    if not isinstance(iterations,int) or not 1<=iterations<=128:
        raise ValueError('invalid rational bisection iterations')
    t=a**-3
    lo,hi=Y_LOW,Y_HIGH
    for _ in range(iterations):
        mid=(lo+hi)/2
        if t_of_y(mid)<t:lo=mid
        else:hi=mid
    assert t_of_y(lo)<t<t_of_y(hi)
    return lo,hi


def witness(a):
    lo,hi=unique_y_interval(a)
    y=(lo+hi)/2
    return {'a':float(F(a)), 'y_bracket':[float(lo),float(hi)],
            'y_mid':float(y),'J_mid':float(j_value(y)),
            'relative_t_bracket':float((t_of_y(hi)-t_of_y(lo))/(F(a)**-3))}


def manifest():
    result=verified_bounds()
    result['controls']=[witness(a) for a in
                        ('1','0.4','0.09','0.0301646','0.03','0.025')]
    result['limitations']=['dust-only benchmark; no radiation',
        'certifies the chosen regular quartic root inside y=(.556,2.3), not all quartic roots',
        'J>0 does not prove a regular kinetic matrix or passage through first fold',
        'the full radial Dirac secondary and lapse fixing remain OPEN']
    return result

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))

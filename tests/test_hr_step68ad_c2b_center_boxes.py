from fractions import Fraction as F
from copy import deepcopy
import pytest
from numerics.hr_step68ad_c2b_center_boxes import Q,PINS,center_cell_box,certify_cells,validate_reports,git_blob,load_pinned

# Exact rational FIELDS copied from the SHA-pinned historical reports via
# authenticated GitHub fetch_file. This local test does NOT assert that the
# full original source tree or full report bytes are present in the container.
def reports():
    v={'step':'68v','center_s_range':['0','1/64'],
       'center_cubic_barrier_kappa':'1/10000000',
       'U_s_strict_positive_inner':True,
       'U_s_center_lower_rational':'3947151372926460534852373/5000000000000000000000000000',
       'U_s_center_upper_rational':'7897452509337401302640553/10000000000000000000000000000',
       'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    ac={'step':'68ac','center_exact_symbolic_GU':{'center_GU0_exact':'-1'},
        'center_U0_interval':['-10504853793521470008293157/2000000000000000000000000000','-26262134483803675020732891/5000000000000000000000000000'],
        'original_U1_interval':['1974362916800616227331277/2500000000000000000000000000','7897451667202464909325109/10000000000000000000000000000'],
        'original_U2_interval':['-100738534867438281757369/10000000000000000000000000000','-12592316858429785219671/1250000000000000000000000000'],
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    b={'step':'68ad-B2','s_domain':['0','1/1024'],'r_domain':['0','1/32'],
       'strict_negative_R2_U_ss_R3_U_sss':True,
       'original_report_sha':{'68v':PINS['68v'][1],'68ac':PINS['68ac'][1]},
       'U_ss_global':['-1414170375015186192017477/69938619264706447051250697260','-281308311835510868820846/14012170704330665327521777975'],
       'U_sss_global':['-3660344913192819744137/44969309632353223525625348630','-6226026282646364646283/90060853521653326637608889875'],
       'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    return {'68v':v,'68ac':ac,'B2':b}

def test_rational_interval_arithmetic_exact():
    a=Q(F(-1,3),F(2,3));b=Q(F(1,5),F(1,2))
    assert (a+b).pair()==['-2/15','7/6']
    assert (a*b).pair()==['-1/6','1/3']
    assert (a**2).pair()==['0','4/9']
    assert (Q(-3,-2)**2).pair()==['4','9']
    assert (Q(-3,-2)**3).pair()==['-27','-8']

def test_rational_reversed_fails():
    with pytest.raises(ValueError):Q(2,1)

def test_source_report_fields_are_coherent():
    a=validate_reports(reports())
    assert len(a)==6
    assert a[0].hi<0<a[3].lo
    assert a[4].hi<0 and a[5].hi<0

def test_exact_seven_cell_closed_partition():
    x=certify_cells(reports())
    assert x['cell_count']==7
    assert x['closed_radius_domain']==['1/64','1/32']
    for left,right in zip(x['cells'],x['cells'][1:]):
        assert left['r'][1]==right['r'][0]
    assert all(not row['s_denominator_division'] for row in x['cells'])

def test_seven_cells_strict_signs_and_sharp_cubic_tube():
    x=certify_cells(reports())
    for row in x['cells']:
        assert F(row['U'][1])<0<F(row['U_s'][0])
        assert F(row['U_ss'][1])<0 and F(row['U_sss'][1])<0
        assert F(row['cubic_barrier_error_abs'])<=F(1,10**7*1024**3)
    assert max(F(r['cubic_barrier_error_abs']) for r in x['cells'])<F(1,10**15)

def test_center_zero_included_without_division():
    x=center_cell_box(reports(),0,F(1,128))
    assert x['s'][0]=='0'
    u0=Q.from_pair(reports()['68ac']['center_U0_interval'])
    assert F(x['U'][0])<=u0.lo<=u0.hi<=F(x['U'][1])

def test_no_r_outside_b2():
    for a,b in [(-1,F(1,128)),(F(1,64),F(1,16)),(F(1,64),F(1,128))]:
        with pytest.raises(ValueError):center_cell_box(reports(),a,b)

def test_invalid_report_status_fails_closed():
    x=reports();x['B2']['JANUS_R']='VALIDATED'
    with pytest.raises(ValueError):validate_reports(x)

def test_invalid_source_hash_crosscheck_fails_closed():
    x=reports();x['B2']['original_report_sha']['68v']='0'*40
    with pytest.raises(ValueError):validate_reports(x)

def test_wrong_cubic_kappa_fails_closed():
    x=reports();x['68v']['center_cubic_barrier_kappa']='1/1000000'
    with pytest.raises(ValueError):validate_reports(x)

def test_missing_report_file_fails_closed(tmp_path):
    with pytest.raises(FileNotFoundError):load_pinned(tmp_path)

def test_corrupted_report_blob_fails_closed(tmp_path):
    for name,_ in PINS.values():
        (tmp_path/name).write_text('{}')
    with pytest.raises(ValueError,match='Pinned physical report drift'):load_pinned(tmp_path)

def test_jet_input_formula_is_exact_polynomial_chain_rule():
    import sympy as s
    r=s.symbols('r'); u0,u1,u2,u3=s.symbols('u0:4')
    U=u0+u1*r**2+u2*r**4+u3*r**6
    us=u1+2*u2*r**2+3*u3*r**4
    uss=2*u2+6*u3*r**2
    usss=6*u3
    assert s.expand(s.diff(U,r,3)-(12*r*uss+8*r**3*usss))==0
    assert s.expand(s.diff(U,r,2)-(2*us+4*r**2*uss))==0
    assert s.expand(s.diff(U,r)-2*r*us)==0

def test_invalid_edges_fails():
    with pytest.raises(ValueError):certify_cells(reports(),[F(1,32),F(1,64)])
    with pytest.raises(ValueError):certify_cells(reports(),[F(1,64),F(1,64)])
    with pytest.raises(ValueError):certify_cells(reports(),[F(1,64),F(1,16)])

def test_report_scope_does_not_claim_temporal_signs():
    x=certify_cells(reports())
    assert x['original_Step58_Step60_temporal_operator']=='NOT_EXECUTED'
    assert x['seven_temporal_cell_signs']=='PENDING'
    assert x['GATE_2B']=='OPEN' and x['JANUS_R']=='NOT_VALIDATED'

def test_algebraic_dust_profile_third_jet_needs_no_U4():
    # Original Step68o rho_f and pSf are algebraic in (s,U,G(s,U))
    # and analytic geometry. The generic chain-rule dependency stops at U'''.
    import sympy as sp
    s=sp.symbols('s')
    u0,u1,u2,u3,u4=sp.symbols('u0:5')
    U=u0+u1*s+u2*s**2+u3*s**3+u4*s**4
    G=(1+s)*(2*U+s*U**2)
    rho=(U**2+s*G+1)/(2+s*U)
    p=(G-s*rho)/(1+s)
    for expr in (rho,p):
        coeff=sp.expand(sp.series(expr,s,0,4).removeO()).coeff(s,3)
        assert not coeff.has(u4)
        assert sp.diff(expr,s,4).has(u4)

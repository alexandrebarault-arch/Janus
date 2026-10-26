"""Local harness tests. These do NOT execute original Step58/60."""
from fractions import Fraction as F
from types import SimpleNamespace
import pytest
from numerics.hr_step68ad_c2d2a_temporal_replay import (
    git_blob, outward_interval, validated_s_jet, inject_s_jet,
    classify_sign, evaluate_original_step58, verify_original_files, PINNED, box_for_rounded_s)

S=10**28
class I:
    def __init__(self,lo,hi=None):self.lo,self.hi=lo,lo if hi is None else hi
    @classmethod
    def hull(cls,a,b):return cls((a*S).__floor__(),(b*S).__ceil__())
    def __pow__(self,n):
        assert n==2 and self.lo>=0
        return I(self.lo*self.lo//S,-(-self.hi*self.hi//S))
    def __truediv__(self,n):return I(self.lo//n,-(-self.hi//n))

class Jet:
    def __init__(self,a):self.a=a

BOX={"r":["1/64","1/56"],"U":["-1/7","-1/8"],
     "U_s":["1/1000","2/1000"],"U_ss":["-1/30000","-1/40000"],
     "U_sss":["-1/10000000","-1/20000000"]}
RBOX=I.hull(F(1,64),F(1,56))**2
BOX["s"]=[str(F(RBOX.lo,S)),str(F(RBOX.hi,S))]
BOX["outward_s_lattice_guard"]=True

@pytest.mark.parametrize("x",["1/7","-1/7","-1/123456789123456789","1/3","0"])
def test_outward_conversion(x):
    z=outward_interval([x,x],I);v=F(x)
    assert F(z.lo,S)<=v<=F(z.hi,S)

def test_reversed_interval_fails_closed():
    with pytest.raises(ValueError):outward_interval(["1/2","1/3"],I)

def test_missing_pair_fails_closed():
    with pytest.raises(ValueError):outward_interval(["1/2"],I)

def test_jet_factorials():
    j=validated_s_jet(BOX,Jet,I)
    assert len(j.a)==4
    assert F(j.a[2].lo,S)<=F(BOX['U_ss'][0])/2
    assert F(j.a[3].hi,S)>=F(BOX['U_sss'][1])/6

def test_injection_exactly_once_and_restored():
    def old(si):raise AssertionError('singular original ODE called')
    m=SimpleNamespace(_ode_coeff=old)
    s=I.hull(F(1,64),F(1,56))**2
    with inject_s_jet(m,BOX,Jet,I,s) as called:
        assert len(m._ode_coeff(s).a)==4
    assert len(called)==1 and m._ode_coeff is old

def test_wrong_cell_rejected_and_restored():
    old=lambda si: None
    m=SimpleNamespace(_ode_coeff=old)
    s=I.hull(F(1,64),F(1,56))**2
    with pytest.raises(AssertionError,match='Unexpected radial'):
        with inject_s_jet(m,BOX,Jet,I,s):m._ode_coeff(I(2,3))
    assert m._ode_coeff is old

def test_original_evaluate_is_called_with_safe_jet():
    original=lambda si: (_ for _ in ()).throw(AssertionError('old ODE called'))
    def evaluate(lo,hi):
        s=I.hull(lo,hi)**2
        assert len(annulus._ode_coeff(s).a)==4
        return {'N':I(1,2),'M':I(-2,-1)}
    annulus=SimpleNamespace(_ode_coeff=original,evaluate_cell=evaluate)
    row=evaluate_original_step58(BOX,annulus,Jet,I)
    assert row['N']['sign']=='POSITIVE_CERTIFIED'
    assert row['M']['sign']=='NEGATIVE_CERTIFIED'
    assert annulus._ode_coeff is original

def test_incomplete_never_certified():
    assert classify_sign(I(-1,1))=='INCOMPLETE'
    assert classify_sign(I(0,1))=='INCOMPLETE'
    assert classify_sign(I(-1,0))=='INCOMPLETE'

def test_outside_domain_rejected():
    annulus=SimpleNamespace()
    with pytest.raises(ValueError):
        evaluate_original_step58({**BOX,'r':['0','1/64']},annulus,Jet,I)

def test_source_sha_known_vector():
    assert git_blob(b'hello\n')=='ce013625030ba8dba906f756967f9e9ca394464a'

def test_source_verifier_fails_closed_on_absent_files(tmp_path):
    with pytest.raises(FileNotFoundError):verify_original_files(tmp_path)

def test_source_verifier_fails_closed_on_tamper(tmp_path):
    for name in PINNED:(tmp_path/name).write_bytes(b'tampered')
    with pytest.raises(ValueError,match='Source drift'):verify_original_files(tmp_path)


def test_rounded_s_guard_uses_true_interval_not_ideal_endpoints():
    from dataclasses import dataclass
    @dataclass(frozen=True)
    class Q:
        lo:F
        hi:F
        def __add__(self,o):return Q(self.lo+o.lo,self.hi+o.hi)
        def __mul__(self,o):
            p=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
            return Q(min(p),max(p))
        def __pow__(self,n):
            assert n in (2,3) and self.lo>=0
            return Q(self.lo**n,self.hi**n)
        def pair(self):return [str(self.lo),str(self.hi)]
    def validation(_):
        return Q(F(-1),F(-1)),Q(F(1),F(1)),Q(F(-1),F(-1)),Q(F(1),F(1)),Q(F(-1),F(-1)),Q(F(-1),F(-1))
    rounded=I.hull(F(1,56),F(9,448))**2
    result=box_for_rounded_s({},rounded,BOX,Q,validation)
    assert F(result['s'][0])==F(rounded.lo,S)
    assert F(result['s'][1])==F(rounded.hi,S)
    assert F(result['s'][0])<=F(1,56)**2
    assert F(result['s'][1])>=F(9,448)**2
    assert result['outward_s_lattice_guard'] is True

def test_outward_s_domain_rejects_overrun():
    with pytest.raises(ValueError,match='escapes'):
        box_for_rounded_s({},I(0,S),BOX,None,None)


def test_all_seven_outward_cells_cover_without_leaving_domain():
    edges=[F(1,64)+F(i,7)*F(1,64) for i in range(8)]
    intervals=[I.hull(a,b)**2 for a,b in zip(edges,edges[1:])]
    assert intervals[0].lo==S//4096
    assert intervals[-1].hi==S//1024
    assert all(a.hi>=b.lo for a,b in zip(intervals,intervals[1:]))
    assert all(0<=x.lo<=x.hi<=S//1024 for x in intervals)


def test_naive_exact_rational_box_misses_outward_lattice_cell():
    lo,hi=F(1,56),F(9,448)
    si=I.hull(lo,hi)**2
    # U(s)=s is a legitimate smooth monotone example. A naive ideal-cell
    # box [lo²,hi²] does not contain U at the rounded upper endpoint.
    assert F(si.hi,S)>hi**2
    assert F(si.lo,S)<=lo**2

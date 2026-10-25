"""Synthetic exact-rational negative controls; full original archives checked separately."""
import json
from fractions import Fraction as F
import pytest
from scripts.hr_step68w_archived_lapse_ratio_audit import check_covers, git_blob


def fixtures(tmp_path):
    rows = []
    pins = []
    for tag, lo, hi in [('s','1/32','1/16'),('q','1/16','1/8'),('p','1/8','17/20')]:
        # N=r²*1; M=r²*(-1000); exact endpoint range, deliberately broad
        a,b=F(lo),F(hi)
        one={'lo':lo,'hi':hi,'N':[str(a*a),str(b*b)],
             'M':[str(-1000*b*b),str(-1000*a*a)]}
        name=tag+'.json'
        doc={'status':'CERTIFIED','queue':[],'failures':[],
             'coverage':[lo,hi],'processed':1,'certified':[one],
             'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
        raw=json.dumps(doc).encode()
        (tmp_path/name).write_bytes(raw)
        pins.append((tag,name,lo,hi,1,git_blob(raw)))
        rows.append(doc)
    return pins, rows


def test_git_blob_known_value():
    assert git_blob(b'hello\n') == 'ce013625030ba8dba906f756967f9e9ca394464a'


def test_exact_fraction_comparisons():
    assert F('1/50000') < F('299788821342512672157652732/12067825969226896389389147905439')
    assert F('12100110164989551454170392062459/870429215706122757278389599591') < 14


def test_synthetic_valid_cover_needs_narrow_enough_cells(tmp_path):
    # The synthetic wide bands imply lower bounds too poor to meet published
    # normalized thresholds; the verifier MUST reject rather than overclaim.
    p, _ = fixtures(tmp_path)
    with pytest.raises(ValueError,match='rational inequalities'):
        check_covers(tmp_path,p)


def test_modified_bytes_rejected(tmp_path):
    p,_=fixtures(tmp_path)
    (tmp_path/'p.json').write_bytes((tmp_path/'p.json').read_bytes()+b' ')
    with pytest.raises(ValueError,match='authenticity'):
        check_covers(tmp_path,p)


def test_unfinished_certification_rejected(tmp_path):
    p,_=fixtures(tmp_path)
    path=tmp_path/'q.json';j=json.loads(path.read_bytes());j['queue']=[['1/16','1/8',0]]
    raw=json.dumps(j).encode();path.write_bytes(raw)
    p=[(*x[:5],git_blob(raw)) if x[0]=='q' else x for x in p]
    with pytest.raises(ValueError,match='Unfinished'):
        check_covers(tmp_path,p)


def test_bad_negative_sign_rejected(tmp_path):
    p,_=fixtures(tmp_path)
    path=tmp_path/'s.json';j=json.loads(path.read_bytes());j['certified'][0]['M'][1]='1'
    raw=json.dumps(j).encode();path.write_bytes(raw)
    p=[(*x[:5],git_blob(raw)) if x[0]=='s' else x for x in p]
    with pytest.raises(ValueError,match='Invalid signed cell'):
        check_covers(tmp_path,p)


def test_missing_boundary_rejected(tmp_path):
    p,_=fixtures(tmp_path)
    path=tmp_path/'s.json';j=json.loads(path.read_bytes());j['certified'][0]['lo']='1/30'
    raw=json.dumps(j).encode();path.write_bytes(raw)
    p=[(*x[:5],git_blob(raw)) if x[0]=='s' else x for x in p]
    with pytest.raises(ValueError,match='Missing cover endpoints'):
        check_covers(tmp_path,p)

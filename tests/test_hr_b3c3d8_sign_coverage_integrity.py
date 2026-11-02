import copy
import json
import tempfile
import unittest
from pathlib import Path
from numerics.hr_b3c3d8_sign_coverage_integrity import (
    audit, git_blob, load_pinned, verify_continuum, verify_points, EXPECTED_SHA,
)


def fixture():
    # Only a synthetic test fixture: the real report has 225 leaves.
    cells=[]
    for i in range(7):
        from fractions import Fraction as F
        a=F(1,64)+(F(1,32)-F(1,64))*i/7
        b=F(1,64)+(F(1,32)-F(1,64))*(i+1)/7
        leaves=[]
        for j in range(32+(i==0)):
            n=32+(i==0)
            x=a+(b-a)*j/n
            y=a+(b-a)*(j+1)/n
            leaves.append({'r':[str(x),str(y)],'N':['1','2'],'M':['-2','-1']})
        cells.append({'r':[str(a),str(b)],'leaves':leaves})
    continuum={'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED','N_positive_continuum':True,
        'M_negative_continuum':True,'covered_r':['1/64','1/32'],
        'adaptive_bisections':1,'total_leaves':225,'cells':cells,
        'min_N_lower':'1','max_M_upper':'-1'}
    points={'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED','strict_bounds_integer':{
        r:{'A_N':[2,3],'A_M':[-6,-4],'sum':[-5,-1]}
        for r in ('1/4','1/2','7/10','17/20')}}
    return continuum, points


class IntegrityTests(unittest.TestCase):
    def test_fixture_exact_225_leaves(self):
        c,p=fixture()
        self.assertEqual(verify_continuum(c)['verified_leaves'],225)
    def test_four_isolated_points(self):
        c,p=fixture()
        self.assertEqual(verify_points(p)['point_count'],4)
    def test_no_false_annular_claim(self):
        c,p=fixture()
        r=audit(c,p)
        self.assertFalse(r['annular_continuum_certified'])
        self.assertEqual(len(r['uncertified_open_intervals_r']),5)
    def test_gap_detected(self):
        c,p=fixture()
        c['cells'][1]['leaves'][0]['r'][0]='1/8'
        with self.assertRaisesRegex(ValueError,'start mismatch|gap or overlap'):verify_continuum(c)
    def test_overlap_detected(self):
        c,p=fixture()
        c['cells'][0]['leaves'][1]['r'][0]=c['cells'][0]['leaves'][0]['r'][0]
        with self.assertRaisesRegex(ValueError,'gap or overlap'):verify_continuum(c)
    def test_zero_sign_detected(self):
        c,p=fixture()
        c['cells'][0]['leaves'][0]['N'][0]='0'
        with self.assertRaisesRegex(ValueError,'uncertified sign'):verify_continuum(c)
    def test_wrong_minimum_detected(self):
        c,p=fixture()
        c['min_N_lower']='2'
        with self.assertRaisesRegex(ValueError,'min N'):verify_continuum(c)
    def test_wrong_maximum_detected(self):
        c,p=fixture()
        c['max_M_upper']='0'
        with self.assertRaisesRegex(ValueError,'max M'):verify_continuum(c)
    def test_bad_point_sign_detected(self):
        c,p=fixture()
        p['strict_bounds_integer']['1/4']['A_M'][1]=1
        with self.assertRaisesRegex(ValueError,'point sign'):verify_points(p)
    def test_point_sum_inconsistency_detected(self):
        c,p=fixture()
        p['strict_bounds_integer']['1/4']['sum']=[-100,-90]
        with self.assertRaisesRegex(ValueError,'inconsistent sum'):verify_points(p)
    def test_point_set_missing_detected(self):
        c,p=fixture()
        del p['strict_bounds_integer']['1/2']
        with self.assertRaisesRegex(ValueError,'point set'):verify_points(p)
    def test_blob_sha_mismatch_detected(self):
        c,p=fixture()
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for path in EXPECTED_SHA:
                f=root/path;f.parent.mkdir(parents=True,exist_ok=True)
                f.write_text('{}',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'SHA mismatch'):load_pinned(root)
    def test_git_blob_known_vector(self):
        self.assertEqual(git_blob(b'hello\n'),'ce013625030ba8dba906f756967f9e9ca394464a')
    def test_declared_domain_tampering_detected(self):
        c,p=fixture()
        c['covered_r']=['0','17/20']
        with self.assertRaisesRegex(ValueError,'declared domain'):verify_continuum(c)


if __name__=='__main__':unittest.main()

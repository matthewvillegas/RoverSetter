import math, unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from roversetter_stability import StaticModel,RECALLED_TEST_MASS_KG, with_carriage
class TestStaticModel(unittest.TestCase):
    def setUp(self):self.m=StaticModel(40,.5,RECALLED_TEST_MASS_KG,1.29)
    def test_previous_v11_cases(self):
        for d,reaction,lam in ((.25,91.7,.397),(.50,31.4,.794),(.75,-29.0,1.191)):
            z=self.m.state(d)
            self.assertAlmostEqual(z['rear_unconstrained_N'],reaction,delta=.18)
            self.assertAlmostEqual(z['lambda'],lam,delta=.0015)
    def test_balances(self):
        for d in (.1,.25,.5,.75,1.0):
            z=self.m.state(d)
            self.assertAlmostEqual(z['front_unconstrained_N']+z['rear_unconstrained_N'],(40+RECALLED_TEST_MASS_KG)*9.81,places=8)
            self.assertAlmostEqual(z['rear_unconstrained_N']*1.29,z['net_restoring_Nm'],places=8)
    def test_slope(self):
        eps=.001
        actual=(self.m.state(.3+eps)['rear_unconstrained_N']-self.m.state(.3)['rear_unconstrained_N'])/eps
        self.assertAlmostEqual(actual,self.m.slope_rear_force_per_m(),places=8)
    def test_threshold(self):
        self.assertAlmostEqual(self.m.state(self.m.critical_overhang_m())['rear_unconstrained_N'],0,places=8)
    def test_negative_unphysical_contact(self):
        self.assertEqual(self.m.state(.75)['rear_status'],'infeasible_four_contact_static')
    def test_input_validation(self):
        with self.assertRaises(ValueError):StaticModel(0,.5,32,1.3)
        with self.assertRaises(ValueError):self.m.state(-.01)
    def test_carriage_movement_lowers_reaction(self):
        args=(35,.5,5,.25,RECALLED_TEST_MASS_KG,.25)
        a=with_carriage(*args,0,1.29)
        b=with_carriage(*args,.08,1.29)
        self.assertLess(b['rear_unconstrained_N'],a['rear_unconstrained_N'])
        self.assertAlmostEqual((b['rear_unconstrained_N']-a['rear_unconstrained_N'])/.08,b['rear_slope_N_per_m'],places=7)

if __name__=='__main__':unittest.main()

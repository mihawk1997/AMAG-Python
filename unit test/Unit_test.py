import unittest
import sys
sys.path.append('C:/Users/suraj/Desktop/AMAG python challenge/src')
import Cal

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(Cal.get_calc(4,4,'addition'),8)
    def test_subtract(self):
        self.assertEqual(Cal.get_calc(3,-1,'subtraction'),4)
    def test_multiplication(self):
        self.assertEqual(Cal.get_calc(0,-3,'multiplication'),0)
    def test_invalid_input(self):
        self.assertEqual(Cal.get_calc(3,2,'somethid'),'Invalid input')
    def test_case_sensitivity(self):
        self.assertEqual(Cal.get_calc(1,3,'ADDITION'),4)
    def test_division_by_zero(self):
        self.assertEqual(Cal.get_calc(3,0,'division'),'Division by 0 error')
    def test_division(self):
        self.assertEqual(Cal.get_calc(-2,-4,'division'),0.5)
    def test_exponentiation(self):
        self.assertEqual(Cal.get_calc(2,-3,'exponentiation'),0.125)
    def test_exponentiation_error(self):
        self.assertEqual(Cal.get_calc(-2,-3,'exponentiation'),'No significant solution')
    def test_all_opeations_universality(self):
        self.assertEqual(len(Cal.df.operation.unique()),5)  
    
        
     
# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)






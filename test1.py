import unittest
from task1 import calculate_output

class Test_calculate_output(unittest.TestCase):
    def test_sum_greater_than_100(self):
        self.assertEqual(calculate_output(80, 60), 140)
    
    def test_sum_equal_to_100(self):
        self.assertEqual(calculate_output(25, 75), 1875)
    
    def test_sum_less_than_100(self):
        self.assertEqual(calculate_output(30, 50), 20)
    
    def test_negative_input(self):
        self.assertEqual(calculate_output(15, -30), "Error")
        self.assertEqual(calculate_output(-15, 30), "Error")
        self.assertEqual(calculate_output(-15, -30), "Error")
    
    def test_zero_input(self):
        self.assertEqual(calculate_output(30, 0), "Error")
        self.assertEqual(calculate_output(0, 30), "Error")
        self.assertEqual(calculate_output(0, 0), "Error")

if __name__ == '__main__':
    unittest.main()
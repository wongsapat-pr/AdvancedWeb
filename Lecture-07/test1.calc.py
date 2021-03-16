import unittest
from unittest import result
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        # result = calc.add(10,5)
         result = calc.add(10,7)
         self.assertEqual(result,15)

if __name__ == '__main__':
    unittest.main()
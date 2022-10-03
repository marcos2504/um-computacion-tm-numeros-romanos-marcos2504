import unittest
from romano_decima import convert_roman_to_decimal
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        decimal = convert_roman_to_decimal('I')
        self.assertEqual( decimal, 1)
    def test_2 (self):
        decimal = convert_roman_to_decimal('II')
        self.assertEqual(decimal,2)
    def test_3(self):
        decimal = convert_roman_to_decimal('III')
        self.assertEqual(decimal,3)
    def test_4 (self):
        decimal = convert_roman_to_decimal('V')
        self.assertEqual(decimal,5)
    def test_5 (self):
        decimal = convert_roman_to_decimal('VII')
        self.assertEqual(decimal,7)
    def test_6 (self):
        decimal = convert_roman_to_decimal('X')
        self.assertEqual(decimal,10)
    def test_7 (self):
        decimal = convert_roman_to_decimal('XXV')
        self.assertEqual(decimal,25)
    def test_8 (self):
        decimal = convert_roman_to_decimal('L')
        self.assertEqual(decimal,50)
    def test_9 (self):
        decimal = convert_roman_to_decimal('LVI')
        self.assertEqual(decimal,56)
    def test_10 (self):
        decimal = convert_roman_to_decimal('C')
        self.assertEqual(decimal,100)
    '''def test_11 (self):
        decimal = convert_roman_to_decimal('IX')
        self.assertEqual(decimal,9)
    def test_12 (self):
        decimal = convert_roman_to_decimal('IV')
        self.assertEqual(decimal,4)
    def test_13 (self):
        decimal = convert_roman_to_decimal('XIV')
        self.assertEqual(decimal,14)
    def test_14 (self):
        decimal = convert_roman_to_decimal('XXIX')
        self.assertEqual(decimal,29)
    def test_15 (self):
        decimal = convert_roman_to_decimal('LXIV')
        self.assertEqual(decimal,64)'''
  
  
if __name__ == '__main__':
    unittest.main()
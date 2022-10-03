
import unittest


def convert_roman_to_decimal(roman_number):
    decimal= 0
    resultado_1 = 0
    resultado_2 = 0 
    resultado_3 =0  
    resultado_4 =0
    resultado_5= 0
    y=roman_number.count('V')
    z=roman_number.count('X')
    x= roman_number.count('I')
    d=roman_number.count('L')
    e=roman_number.count('C')
    
    if x >=1 :
        resultado_1 = x*1
    if y>=1 :
        resultado_2 = y*5
    if z>=1 :
        resultado_3 = z*10
    if d>=1 :
        resultado_4 = d*50
    if e>=1 :
        resultado_5= e*100 
    
    
    
    


  
    resultado = resultado_1+resultado_2+resultado_3+resultado_4+resultado_5

    return resultado 

    
    

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
    def test_11 (self):
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
        self.assertEqual(decimal,64)
  
  
if __name__ == '__main__':
    unittest.main()
import unittest


def convert_decimal_to_roman(decimal_number):
    roman = ''
    
    rest = decimal_number % 10
    mult_10 = decimal_number // 10
    result_1 = ''
    result_2 = ''
    result_3 = ''
    result_4 = ''
    result_5 = ''
    result_6 = ''
    result_7 = ''
    result_10 =''
    result_11 = ''
    result_12 = ''
    result_13 = ''
    result_14 = ''
    if 0<mult_10 <4:
        for digit in range(mult_10):
            result_1 += 'X'

    if mult_10 == 4 :
        for digit in range(1):
            result_12 = 'XL'

    if 5<=mult_10 <9:
        for digit in range(1):
            result_10 = 'L'
        for digit in range(mult_10-5):
            result_11 += 'X'
    if mult_10 == 9 :
        for digit in range(1):
            result_13 = 'XC'
    if mult_10 == 10:
        for digit in range(1):
            result_14= 'C'


    if rest < 4:
        for digit in range(rest):
            result_2 += 'I'
    if rest == 5:
        for digit in range(1):
            result_3 = 'V'
    if rest == 4 :
        for digit in range(1):
            result_6 += 'IV'
    if rest == 9 :
        for digit in range(1):
            result_5 += 'IX'
    if 5<=rest<9:
        for digit in range(1):
            result_3 = 'V'
        for digit in range(rest-5):
            result_7 += 'I'
       
            

        
    
  

    result = result_10+result_11+result_12+result_13+result_14+result_1 + result_2 +result_3+result_4+result_5+result_6+ result_7
    return result

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')

    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, 'X')

    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, 'III')
    
    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, 'XX')

    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual (roman_number, 'XXX')
    
    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual (roman_number, 'XXIII')
    
    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual (roman_number, 'XI')
    
    def test_12(self): 
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual (roman_number, 'XII')
    
    def test_13(self): 
        roman_number = convert_decimal_to_roman(13)
        self.assertEqual (roman_number, 'XIII')
    
    def test_25(self): 
        roman_number = convert_decimal_to_roman(25)
        self.assertEqual (roman_number, 'XXV')
    
    def test_19(self): 
        roman_number = convert_decimal_to_roman(19)
        self.assertEqual (roman_number, 'XIX')
    
    def test_14(self): 
        roman_number = convert_decimal_to_roman(14)
        self.assertEqual (roman_number, 'XIV')
        
    def test_16(self): 
        roman_number = convert_decimal_to_roman(16)
        self.assertEqual (roman_number, 'XVI')
    
    def test_17(self): 
        roman_number = convert_decimal_to_roman(17)
        self.assertEqual (roman_number, 'XVII') 
    
    def test_18(self):
        roman_number = convert_decimal_to_roman(18)
        self.assertEqual(roman_number, 'XVIII')

    def test_50(self):
        roman_number = convert_decimal_to_roman(50)
        self.assertEqual(roman_number, 'L')
    
    def test_60(self):
        roman_number = convert_decimal_to_roman(60)
        self.assertEqual(roman_number, 'LX')
        
    
    def test_40(self):
        roman_number = convert_decimal_to_roman(40)
        self.assertEqual(roman_number, 'XL')
    
    def test_70(self):
        roman_number = convert_decimal_to_roman(70)
        self.assertEqual(roman_number, 'LXX')
    
    def test_80(self):
        roman_number = convert_decimal_to_roman(80)
        self.assertEqual(roman_number, 'LXXX')
    
    def test_90(self):
        roman_number = convert_decimal_to_roman(90)
        self.assertEqual(roman_number, 'XC')

    def test_100(self):
        roman_number = convert_decimal_to_roman(100)
        self.assertEqual(roman_number, 'C')
    
    def test_62(self):
        roman_number = convert_decimal_to_roman(62)
        self.assertEqual(roman_number, 'LXII')

    def test_54(self):
        roman_number = convert_decimal_to_roman(54)
        self.assertEqual(roman_number, 'LIV')

    def test_47(self):
        roman_number = convert_decimal_to_roman(47)
        self.assertEqual(roman_number, 'XLVII')
    
    def test_88(self):
        roman_number = convert_decimal_to_roman(88)
        self.assertEqual(roman_number, 'LXXXVIII')
    
    def test_99(self):
        roman_number = convert_decimal_to_roman(99)
        self.assertEqual(roman_number, 'XCIX')
    
    

  
    
    
if __name__ == '__main__':
    unittest.main()
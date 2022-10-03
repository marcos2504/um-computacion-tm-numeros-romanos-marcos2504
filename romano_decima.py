


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

    
    
''' Principle : To reduce the number of multiplication needed by using 
repeated squared multiplication. 
Using binary number expression to define the needed squared multiplication
 '''

def Calcul_Exponentiation(num, exponent):
    res = 1
    while exponent > 0:
        if (exponent & 1):      # If the first significant bit is 1
            res = res * num
        num = num*num           
        exponent >>= 1          # Shift the bit to the right
    return res

# Version with modulo

def Calcul_Exponentiation(num, exponent, mod):
    res = 1
    num %= mod
    while exponent > 0:
        if (exponent & 1):
            res = res*num % mod
        num = num*num % mod
        exponent >>= 1
    return res
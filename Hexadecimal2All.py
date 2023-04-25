import unittest
from binario2All import binario2decimal, binario2octal

DiccionarioHexadecimal = {
    '0' : "0000",
    '1' : "0001",
    '2' : "0010",
    '3' : "0011",
    '4' : "0100",
    '5' : "0101",
    '6' : "0110",
    '7' : "0111",
    '8' : "1000",
    '9' : "1001",
    'A' : 1010,
    'B' : 1011,
    'C' : 1100,
    'D' : 1101,
    'E' : 1110,
    'F' : 1111
}



def hexadecimal2binario(hexa):
    hexadecimal = ""
    for digito in hexa:
      hexadecimal += str(DiccionarioHexadecimal[digito])
    return(hexadecimal)

def hexadecimal2decimal(hexa):
   binario = hexadecimal2binario(hexa)
   return(binario2decimal(binario))

def hexadecimal2octal(hexa):
   binario = hexadecimal2binario(hexa)
   return(binario2octal(binario))

if __name__ == '__main__':
    unittest.main()

import unittest
from binario2All import  binario2decimal, binario2hexadecimal
DiccionarioOctal = {
    '0' : "0000",
    '1' : "0001",
    '2' : "0010",
    '3' : "0011",
    '4' : "0100",
    '5' : "0101",
    '6' : "0110",
    '7' : "0111",
}


def octal2binario(octa):
    octal = ""
    for digito in octa:
      octal += str(DiccionarioOctal[digito])
    return(octal)

def octal2decimal(octa):
   binario = octal2binario(octa)
   return(binario2decimal(binario))

def octal2hexadecimal(octa):
   binario = octal2binario(octa)
   return(binario2hexadecimal(binario))

if __name__ == '__main__':
    unittest.main()

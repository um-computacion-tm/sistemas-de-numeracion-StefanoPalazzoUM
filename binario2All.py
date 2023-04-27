import unittest

def binario2decimal(numero):
    total = 0
    valorPosicional = 1
    numero = numero[:: -1] #invierte el numero para realizar el cálculo
    for bit in numero:
        total += (int(bit)*valorPosicional)
        valorPosicional = valorPosicional*2
    return (total)

def binario2octal(binario):
    total = ""                        # Acá se almacena el resultado final
    while (len(binario) % 3) != 0:    # Agregamos 0s para que se pueda separar en grupos de 3
        binario = "0" + binario 
    for i in range(0,len(binario),3): # Separamos en grupos de 3
       digito = int(binario[int(i)])*4 + int(binario[int(i)+1])*2 + int(binario[int(i+2)]) # Le damos peso a cada digito y los guardamos como un digito
       total += str(digito)
    return (int(total))

def binario2hexadecimal(binario):
    total = ""                        # Acá se almacena el resultado final
    while (len(binario) % 4) != 0:    # Agregamos 0s para que se pueda separar en grupos de 4
        binario = "0" + binario 
    for i in range(0,len(binario),4): # Separamos en grupos de 4
       digito = int(binario[int(i)])*8 + int(binario[int(i)+1])*4 + int(binario[int(i+2)])*2 + int(binario[int(i+3)]) # Le damos peso a cada digito y los guardamos como un digito
       if digito >= 10:
           AbcHex= "ABCDEF"
           digito = AbcHex[digito-10]
       total += str(digito)
    print (total)
    return (total)
    

if __name__ == '__main__':
    unittest.main()



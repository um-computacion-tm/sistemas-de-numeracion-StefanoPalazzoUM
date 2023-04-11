import unittest



def binario2decimal(numero):
    total = 0
    valorPosicional = 1
    numero = numero[:: -1]
    for bit in numero:
        total += (int(bit)*valorPosicional)
        valorPosicional = valorPosicional*2
    return (total)



if __name__ == '__main__':
    unittest.main()

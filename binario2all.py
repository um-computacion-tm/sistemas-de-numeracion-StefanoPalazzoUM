def binario2decimal(numero):
    total = 0
    valorPosicional = 1
    numero = numero[:: -1]
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
    return (total)
    


binario = input("Ingrese un binario: ")
binario2octal(binario)



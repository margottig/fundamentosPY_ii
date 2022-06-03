'''
Escribe una función llamada numerosPrimos. Esta función recibe como parámetro
# un número entero positivo. La función se encarga de crear un arreglo con los
# números primos desde el 1 hasta el número proporcionado. La función retorna
# el arreglo como resultado.
# 13 => [2, 3, 5, 7, 11]
'''

def esPrimo(numeroIterador):
    contador = 0
    for x in range (1, numeroIterador+1):
        if numeroIterador % x == 0:
            contador += 1
    if contador == 2:
        #print("VINO ACA")
        return True
    else:
        return False
   

def numeroPrimo(numero):
    arreglo = []
    for i in range(1,numero):
        #llamar a la funcion que indica si es primo esprimo(i)
        if esPrimo(i) == True:
            arreglo.append(i)
    return arreglo

        #if i % 2 != 0:
        #    arreglo.append(i)
    #return arreglo

print(numeroPrimo(13))





numeros = [1,2,3,4,5,6,7,8,9,10]

def filtrar_pares(lista_numeros: list[int]):
    numeros_pares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            
    return numeros_pares


print(filtrar_pares(numeros))
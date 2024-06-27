numeros = [1,2,3]


def sumar_lista(lista_numeros: list[int]):
    resultado_suma = 0
    
    for numero in lista_numeros:
        # resultado_suma = resultado_suma + numero
         resultado_suma += numero
         
    return resultado_suma

print(sumar_lista(numeros))

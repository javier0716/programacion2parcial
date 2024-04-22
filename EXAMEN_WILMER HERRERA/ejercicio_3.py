num = int(input("ingrese un numero: "))

contador = 1
while contador < 201:
    
    print(contador)
    if (contador % num == 0):
       print(f'{contador}  es divisible')  
    else:
        print(f'{contador} no es divisible')  
    contador += 1
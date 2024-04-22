salir = False

while not salir:

    print("------ Menu ------")
    print("1. Comprobar numero")
    print("0. salir")

    opt = input("Ingrese una opcion: ")
    
if(opt == '0'):
    salir = True
elif(opt == '1'):
    num = int(input("Ingrese un numero: "))

    if(num % 2 == 0):
         print('El numero es par')
    else:
        print('El numero no es par')
else:
        print('Opcion no valida')
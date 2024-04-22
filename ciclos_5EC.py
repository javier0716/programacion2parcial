

salir = False

while not salir:

    print("------ Menu ------")
    print("1. Sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("0. salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        numero1 =int(input("ingrese un numero: "))
        numero2 =int(input("ingrese otro numero: "))

        resultado= numero1 + numero2

        print("El resultado de la suma es " + str (resultado))

    elif(opt == '2'):
        numero1 =int(input("ingrese un numero: "))
        numero2 =int(input("ingrese otro numero: "))

        resultado= numero1 - numero2

        print("El resultado de la resta es " + str (resultado))

    elif(opt == '3'):
        numero1 =int(input("ingrese un numero: "))
        numero2 =int(input("ingrese otro numero: "))

        resultado= numero1 * numero2

        print("El resultado de la multiplicacion es " + str (resultado))

    elif(opt == '4'):
        numero1 =int(input("ingrese un numero: "))
        numero2 =int(input("ingrese otro numero: "))

        resultado= numero1 / numero2

        print("El resultado de la division es " + str (resultado))
        
    else:
        print("Opcion no valida!")
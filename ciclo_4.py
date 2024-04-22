

salir = False

while not salir:
    print("------ Menu ------")
    print("1. imprimir tabla")
    print("0. Salir")

    opt = input ("Ingrese una opcion:")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        tabla = int(input("Ingrse el numero de tabla que desea: "))
        

        print(f"***** Tabla del {tabla} *****")
        for i in range(1,11):
            print(f"{tabla} x {i} = {tabla*i}")
    else:
        print("Opcion no valida!")



salir = False
lista_compras = []

while not salir:
    print("------ Menu ------")
    print("1. imprimir lista de compras")
    print("2. Agregar elemento a la lista")
    print("0. Salir")

    opt = input ("Ingrese una opcion:")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        print("-------- Lista de compras --------")
        for i in range  (len(lista_compras)):
            print(f"{i + 1}. {lista_compras[i]}")
    elif(opt == '2'):
        nuevo_elemento = input ("Ingrese el nombre del producto: ")
        # print(nuevo_elemento)
        lista_compras . append(nuevo_elemento)

        print(f"El elemento '^{nuevo_elemento}' fue agregado a la lista.")
    else:
        print("Opcion no valida!")
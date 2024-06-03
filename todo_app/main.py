from menu import imprimir_menu
from datos import crear_tarea, obtener_todas_las_tareas


salir = False

while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")
    
    if resp =='0':
        salir = True
    elif resp =='1':
        pass
    elif resp =='2':
        pass
    elif resp =='3':
        pass
    elif resp =='4':
        crear_tarea('Tarea Matematicas')
        print(obtener_todas_las_tareas())
    elif resp =='5':
        pass
    else:
        print(f"La opcion '{resp}' no es valida:")
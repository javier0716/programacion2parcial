from menu import imprimir_menu
from datos import crear_tarea, obtener_todas_las_tareas, eliminar_tarea, obtener_tareas_pendientes, obtener_tareas_completadas, completar_tarea
# import json 

salir = False


#with open('test.json') as testfile:
#   texto = testfile.read
#    print(texto)
#    
#    data = json.loads(texto)
#    print(data)
#    print(data['usuarios'][0]['ud'])
    
    
# test_data = {
#         'texto': 'Hola Mundo',
#         'estado': True,
#         'valor': 3.1
#     }

# print(test_data)

# json_text = json.dumps(test_data)
# print(json_text)
    
# with open('YHLQMDLG.json', 'w') as YHLQMDLG_file:
#     YHLQMDLG_file.write(json_text)
#     YHLQMDLG_file.close()
#open sin cometario pasa automaticamente a lectura "r"
    
    
    
    
while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")
    
    if resp =='0':
        salir = True
    elif resp =='1':
        print('\n------ Todas las tareas ------')
        tareas = obtener_todas_las_tareas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1})  {tarea['titulo']}')
            
    elif resp =='2':
         print('\n------ Tareas pendientes ------')
         tareas = obtener_tareas_pendientes()
         for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1})  {tarea['titulo']}')
    elif resp =='3':
        print('\n------ Tareas completadas ------')
        tareas = obtener_tareas_completadas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1})  {tarea['titulo']}')
            
    elif resp =='4':
        titulo_tarea = input('Ingrese la nueva tarea: ')
        crear_tarea(titulo_tarea)
        print('\nTarea Agregada!\n\n')
    elif resp =='5':
        print('\n------ Eliminar una tarea ------')
        tareas = obtener_todas_las_tareas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1})  {tarea['titulo']}')
            
        del_opt = input("Ingrese el numero de la tarea que desea eliminar: ")
        
        del_index = int(del_opt) - 1
        
        del_tarea = tareas[del_index]
        
        eliminar_tarea(del_tarea)
        
        print('\nTarea Eliminada!\n\n')
    elif resp == '6':
           print('\n------ Completar una tarea ------')
           tareas = obtener_tareas_pendientes()
           for tarea in tareas:
                index = tareas.index(tarea)
                print(f'{index + 1})  {tarea['titulo']}')
            
           comp_opt = input("Ingrese el numero de la tarea que desea completar: ")
           
           comp_index = int(comp_opt) - 1
        
           comp_tarea = tareas[comp_index]
           
           completar_tarea(comp_tarea['id'])
           
           print('\nTarea completada!\n\n')
    else:
        print(f"La opcion '{resp}' no es valida:")
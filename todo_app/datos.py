from uuid import uuid4
from file_manager import obtener_datos, sincronizar_todos

datos_guardados = obtener_datos()

_tareas =  datos_guardados['todos']

def crear_tarea(titulo: str):
    nueva_tarea = {
        'id': str(uuid4()),
        'titulo': titulo,
        'completada': False
    }
    
    _tareas.append(nueva_tarea)
    
    sincronizar_todos(_tareas)
    #append es agregar en este contexto
    
    
def obtener_todas_las_tareas():
    return _tareas 

def obtener_tareas_completadas():
    tareas_completadas = []
    
    for tarea in _tareas:
        if tarea['completada']:
            tareas_completadas.append(tarea)
            
    return tareas_completadas

def obtener_tareas_pendientes():
    tareas_pendientes = []
    
    for tarea in _tareas:
        if not tarea['completada']:
            tareas_pendientes.append(tarea)
            
    return tareas_pendientes

def eliminar_tarea(tarea: dict):
    _tareas.remove(tarea)
    
    sincronizar_todos(_tareas)
    
    
def completar_tarea(tarea_id: str):
    for tarea in _tareas:
        if tarea['id'] == tarea_id:
            tarea['completada'] = True
            sincronizar_todos(_tareas)
            break
            
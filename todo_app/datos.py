from uuid import uuid4
from file_manager import obtener_datos

obtener_datos()

_tareas =  []

def crear_tarea(titulo: str):
    nueva_tarea = {
        'id': uuid4(),
        'titulo': titulo,
        'completada': False
    }
    
    _tareas.append(nueva_tarea)
    
def obtener_todas_las_tareas():
    return _tareas 
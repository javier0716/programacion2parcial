from pathlib import Path
import json 


ROOT_PATH = Path(__file__).resolve().parent

FILE_PATH = ROOT_PATH / 'datos.json'


DEFAULT_DATA ={
    'todos': []
}

def obtener_datos():
    with open(FILE_PATH) as datos_file:
       file_data = datos_file.read()
       datos_file.close
        
    if not file_data:
        return DEFAULT_DATA
    
    datos = json.loads(file_data)
    return datos

def sincronizar_todos(todos: list):
    datos = obtener_datos()
    datos['todos'] = todos
    
    with open(FILE_PATH, 'w') as datos_file:
        file_data = json.dumps(datos)
        datos_file.write(file_data)
        datos_file.close()
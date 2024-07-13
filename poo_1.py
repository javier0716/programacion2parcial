from uuid import uuid4


# init se llama constructor
# los nombres de clases siempre empiezan con MAYUSCULA
class Todo: 
    def __init__(self, nombre: str, completada : bool = False):
        self.__id__ = uuid4()
        self.nombre = nombre
        self.completada = completada
        self.hora = "16:18"
todo_1 = Todo("Test 1")
todo_2 = Todo("Test 2")


print(todo_1.__id__)

todo_1.id = "ABC123"

print(todo_1.__id__)
# Pseudocodigo
# Solicitar la edad del usuario y guardarla en una variable llamada “edad_usuario” si la variable “edad_usuario” es mayor a 18
# si la variable "edad_usuario" es mayor a 18:
#   Imprimir por consola el texto “Eres mayor de edad”     
# Caso contrario:
#    Imprimir por consola el texto “No eres mayor de edad”


# Codigo
edad_usuario = int(input("Ingrese su edad: "))

if(edad_usuario > 18):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
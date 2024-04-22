# Pseudocodigo
# Solicitar el total de la compra y guardarla en una variable llamada “total_compra”
# Si la variable “total_compra” es mayor a 2000 
# Crear una variable llamada “descuento” que contenga el resultado de la multiplicación de las variables “total_compra” y “0.08”
# Imprimir por consola el texto “<Se ha aplicado descuento >”
# Caso contrario:
# Imprimir por consola “No aplica descuento”

# Codigo
total_compra =float(input("Ingrese el total de la compra: "))

if(total_compra > 2000):
    descuento = total_compra * 0.08
    print("Aplica descuento " + str (descuento))
else:
    print("No aplica descuento")


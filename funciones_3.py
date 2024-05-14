

def crear_usuario(nombre:str, apellido:str, f_nac:str, estado:bool= True,):
    if nombre == "Josue":
        print("el nombre es Josue")
    nuevo_usuario= {
        'nombre': nombre,
        'apellido': apellido,
        'f_nac': f_nac,
        'estado': True,
        'estado': estado
    }
    
    return nuevo_usuario


usuario_1 = crear_usuario('Josue', 'Soriano', '23/05/2008')
usuario_2 = crear_usuario('Javier', 'Herrera', '30/09/2007', False)

print(usuario_1)
print(usuario_2)
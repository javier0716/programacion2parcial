

class Animal:
    def __init__(self, color_pelaje: str, pelaje:str, sexo: str, tamano: str, cuerpo: str, raza: str):
        self.color_pelaje = color_pelaje
        self.pelaje = pelaje
        self.sexo = sexo
        self.tamano = tamano
        self.cuerpo = cuerpo
        self.raza = raza

    def comer(self):
        pass


animal_1 = Animal("cafe oscuro", "largo", "macho", "mediano", "delgado", "pastor aleman")

print(animal_1.color_pelaje)


class Perro(Animal):
    def __init__(self, color_pelaje: str, pelaje: str, sexo: str, tamano: str, cuerpo: str, raza: str):
        super().__init__(color_pelaje, pelaje, sexo, tamano, cuerpo, raza)

    def ladrar(self):  
        print("Wao Wao")

    def comer(self):
        print("ñam ñam")

perro_1 = Perro("cafe oscuro", "largo", "macho", "mediano", "delgado", "pastor aleman")
perro_1.ladrar()
perro_1.comer()

class Gato(Animal):
    def __init__(self, color_pelaje: str, pelaje: str, sexo: str, tamano: str, cuerpo: str, raza: str):
        super().__init__(color_pelaje, pelaje, sexo, tamano, cuerpo, raza)
        self.comida = 0 
    def maullar(self):
        print("Miau Miau")

    #def comer(self):
     #   print("ñam ñam")

gato_1 = Gato("negro", "frondoso", "femenino", "pequeño", "flaco","siames")
#gato_1.maullar()


#animal_1 = Animal("", "", "", "", "","")
animal_1 = Perro("", "", "", "", "","")


print(animal_1.cuerpo)
gato_1.comer()


class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int, color: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.color = color
        
        
        
    def get_marca(self) -> str:
        return self.__marca
    
    def set_marca(self, marca: str):
        self.__marca = marca
    
    def get_modelo(self) -> str:
        return self.__modelo
    
    def set_modelo(self, modelo: str):
        self.__modelo = modelo
    
    def get_año(self) -> int:
        return self.__año
    
    def set_año(self, año: int):
        self.__año = año
        
        
    def detalles(self):
        print("marca")    
        
        
class Automovil(Vehiculo):
    def __init__(self,marca: str, modelo: str, año: int, color: str, numero_puertas: int, capacidad_maletero: float):
        super().__init__(marca, modelo, año, color)
       
        self.__numero_puertas = numero_puertas 
        self.__capacidad_maletero = capacidad_maletero
       
    def get_numero_puertas(self) -> int:
        return self.__numero_puertas
    
    def   set_numero_puertas(self, numero_puertas: int) :
            self.__numero_puertas = numero_puertas
       
    def get_capacidad_maletero(self) -> int:
        return self.__capacidad_maletero   
    
    def set_capacidad_maletero(self, capacidad_maletero: float):
        self.__capacidad_maletero = capacidad_maletero
        
        
        
        
        
        
        
class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, color: str, tipo: str, cilindraje: int):
        super().__init__(marca, modelo, año, color )
        
        self.__tipo = tipo
        self.__cilindraje = cilindraje
        
        
    def get_tipo(self) ->str :
        return self.__tipo
    def set_tipo( self, tipo: str):
        self.__tipo = tipo
        
    def get_cilindraje(self) -> int:
        return self.__cilindraje
    def set_cilindraje(self, cilindraje: int):
        self.__cilindraje = cilindraje
        
    
    
Automovil_1 = Automovil("ford", "escape", "2013", "gris", "4", "0")
print(Automovil_1.detalles())

        
        

from pygame import surface
import pygame



class Player:
    def __init__(self, screen:surface ,x:int ,y:int ,ancho:int = 25, alto:int = 150) -> None:
        self.__x = x
        self.__y = y 
        self.__ancho = ancho
        self.__alto = alto
        self.__velocidad = 0
        self.__screen = screen
        self.__puntos = 0

    def set_velocidad(self, velocidad: int):
        self.__velocidad = velocidad

    def draw(self) -> None:
        pygame.draw.rect(
            self.__screen,
            "white",
            (self.__x, self.__y, self.__ancho, self.__alto)
        )          

    def move(self, delta_time: float) -> None:
        self.__y += self.__velocidad * delta_time

        if self.__y < 0:
            self.__y = 0

        if self.__y > 450:
            self.__y = 450  

    def get_puntos(self) -> int:
        return self.__puntos
    
    def aumentar_punto(self) -> None:
        self.__puntos += 1
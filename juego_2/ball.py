from pygame import Surface
import pygame 


class Ball:
    def __init__(self, screen:Surface ,x:int ,y:int, size: int):
        self.__x = x
        self.__y = y
        self.__screen = screen
        self.__size = size

    def draw(self) -> None:
        pygame.draw.rect(
            self.__screen,
            "white",
            (self.__x, self.__y, self.__size, self.__size)
        )
        
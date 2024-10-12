from pygame import Surface
from config import Config
import random
import pygame 


class Ball:
    def __init__(self, screen:Surface ,x:int ,y:int, size: int):
        self.__x = x
        self.__y = y
        self.__velocidad_x = Config.BALL_MAX_SPEED * random.choice((1, -1))
        self.__velocidad_y = Config.BALL_MAX_SPEED * random.choice((1, -1))
        self.__screen = screen
        self.__size = size

    def draw(self) -> None:
        pygame.draw.rect(
            self.__screen,
            "white",
            (self.__x, self.__y, self.__size, self.__size)
        )

    def invertir_velocidad_y(self) -> None:
        self.__velocidad_y *= -1


    def move(self, delta_time: float) -> None:
        self.__x += self.__velocidad_x * delta_time
        self.__y += self.__velocidad_y * delta_time
        
        if (self.__y <= 0) or (self.__y >= Config.SCREEN_HEIGHT - self.__size):
            self.invertir_velocidad_y()
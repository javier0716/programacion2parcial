import pygame 


pygame.init()

screen = pygame.display.set_mode((800,600))

running = True 


while running: 
    
    screen.fill("black")
    
    pygame.display.flip()

pygame.quit()
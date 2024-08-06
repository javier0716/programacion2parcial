import pygame 
import random 

pygame.init()

screen = pygame.display.set_mode((800,600), flags=pygame.SCALED, vsync=1)

running = True 


coord_x = 390
coord_y = 290


speed_x = 225
speed_y = 225

bg_color = [0,0,0]

clock = pygame.time.Clock()


def siguiente_fondo():
    for index in range(len(bg_color)):
        bg_color[index] = random.randint(0, 255)


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    delta_time = clock.tick(60) / 1000
    
    coord_x += speed_x * delta_time
    
    if coord_x > 780:
        coord_x = 780
    
    elif coord_x < 0:
        coord_x = 0
    
    if coord_x >= 780 or coord_x <= 0:
        siguiente_fondo()
        speed_x *= -1
    
    coord_y += speed_y * delta_time
    
    
    
    if coord_y > 580:
        coord_y = 580
        
    elif coord_y < 0:
        coord_y = 0
    
    if coord_y>= 580 or coord_y<= 0:
        siguiente_fondo()
        speed_y *= -1

    screen.fill(bg_color)
    pygame.draw.rect(screen, "white", (coord_x, coord_y, 20, 20))
    pygame.display.flip()

pygame.quit()
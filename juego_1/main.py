import pygame 


pygame.init()

screen = pygame.display.set_mode((800,600))

running = True 


coord_x = 390
coord_y = 290

speed_x = 1
speed_y = 1
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
    coord_x += speed_x
    
    
    if coord_x >= 780 or coord_x <= 0:
       speed_x *= -1
    
    coord_y += speed_y
    
    if coord_y>= 580 or coord_y<= 0:
        speed_y *= -1

    screen.fill("black")
    pygame.draw.rect(screen, "white", (coord_x, coord_y, 20, 20))
    pygame.display.flip()

pygame.quit()
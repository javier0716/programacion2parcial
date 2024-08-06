import pygame 


pygame.init()

screen = pygame.display.set_mode((800,600), flags=pygame.SCALED, vsync=1)

running = True 

bg_color = [0,0,0]

clock = pygame.time.Clock()
player_1_coord_x = 40
player_1_coord_y = 225

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("w")
        
        elif event.type == pygame.KEYUP:
            print("KEYUP")
        

    delta_time = clock.tick(60) / 1000

    screen.fill(bg_color)
    
    pygame.draw.rect(screen,"white", (player_1_coord_x, player_1_coord_y, 25, 150))
    
    
    pygame.display.flip()

pygame.quit()
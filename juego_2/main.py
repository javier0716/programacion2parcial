import pygame 

pygame.init()

screen = pygame.display.set_mode((800,600), flags=pygame.SCALED, vsync=1)

running = True 

bg_color = [0,0,0]

clock = pygame.time.Clock()
PLAYER_MAX_SPEED = 400

ball_coord_x = 390
ball_coord_y = 290

ball_speed_x = 225
ball_speed_y = 225


player_1_coord_x = 40
player_1_coord_y = 225
player_1_speed = 0

player_2_coord_x = 740


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
             player_1_speed = PLAYER_MAX_SPEED * -1
            if event.key == pygame.K_s:
                player_1_speed = PLAYER_MAX_SPEED
                
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_1_speed = 0
            if event.key == pygame.K_s:
                player_1_speed = 0
                
        
        

    delta_time = clock.tick(60) / 1000
    
    player_1_coord_y += player_1_speed * delta_time
    
    
    if ball_coord_y > 580:
        ball_coord_y = 580
        
    elif ball_coord_y < 0:
        ball_coord_y = 0
        
    if player_1_coord_y < 0:
        player_1_coord_y = 0
        
    if player_1_coord_y > 450:
        player_1_coord_y = 450
        
    ball_coord_y += ball_speed_y * delta_time

    
    screen.fill(bg_color)
    
    pygame.draw.rect(screen,"white", (player_1_coord_x, player_1_coord_y, 25, 150))
    pygame.draw.rect(screen,"white",(ball_coord_x, ball_coord_y, 20, 20))
    
    
    pygame.display.flip()

pygame.quit()
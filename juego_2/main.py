import pygame 
from player import Player
from config import Config
pygame.init()

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)

running = True

pelota_coord_x = 390
pelota_coord_y = 290

pelota_speed_x = 200
pelota_speed_y = 200

bg_color = [0,0,0]

clock =pygame.time.Clock()

player_1 = Player (
    screen,
      Config.PLAYER_BORDERDISTANCE,
        (Config.SCREEN_WIDTH/2) - (Config.PLAYER_HEIGHT/2),
        Config.PLAYER_WIDTH,
        Config.PLAYER_HEIGHT
      )
player_2 = Player (
    screen,
      Config.SCREEN_WIDTH - Config.PLAYER_BORDERDISTANCE - Config.PLAYER_WIDTH,
        (Config.SCREEN_WIDTH/2) - (Config.PLAYER_HEIGHT/2),
        Config.PLAYER_WIDTH,
        Config.PLAYER_HEIGHT
        )


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1.set_velocidad(Config.PLAYER_MAX_SPEED * -1)
            if event.key == pygame.K_s:
                player_1.set_velocidad(Config.PLAYER_MAX_SPEED)
            if event.key == pygame.K_UP:
                player_2.set_velocidad(Config.PLAYER_MAX_SPEED * -1)
            if event.key == pygame.K_DOWN:
                    player_2.set_velocidad(Config.PLAYER_MAX_SPEED)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_1.set_velocidad(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_2.set_velocidad(0)

    delta_time = clock.tick(60) / 1000
    player_1.move(delta_time)
    player_2.move(delta_time)

    pelota_coord_y += pelota_speed_y * delta_time

    if pelota_coord_y > 580:
        pelota_coord_y = 580
    
    elif pelota_coord_y < 0:
        pelota_coord_y = 0

    if pelota_coord_y >= 580 or pelota_coord_y <= 0:
        pelota_speed_y *= -1

    pelota_coord_x += pelota_speed_x * delta_time

    screen.fill(bg_color)
    
    #pygame.draw.rect(screen, "white", (player_1_coord_x, player_1_coord_y, 25, 150))
    player_1.draw()
    player_2.draw()
    pygame.draw.rect(screen, "white",(pelota_coord_x, pelota_coord_y, 20, 20))
    pygame.display.flip()
    
    pygame.display.flip()

pygame.quit()
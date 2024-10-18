import pygame 
from player import Player
from config import Config

from ball import Ball
pygame.init()

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)

running = True

bg_color = [0,0,0]

clock =pygame.time.Clock()
player_1 = Player (
    screen,
    20,
        (Config.SCREEN_WIDTH/2) - (Config.PLAYER_HEIGHT/2),
        Config.PLAYER_WIDTH,
        Config.PLAYER_HEIGHT
)
player_2 = Player (
    screen,
      Config.SCREEN_WIDTH - 20  - Config.PLAYER_WIDTH,
        (Config.SCREEN_WIDTH/2) - (Config.PLAYER_HEIGHT/2),
        Config.PLAYER_WIDTH,
        Config.PLAYER_HEIGHT
)

ball = Ball  (
    screen,
     (Config.SCREEN_WIDTH/2) - 15,
     (Config.SCREEN_HEIGHT/2) - 15,
     30

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

    ball_l = ball.get_x()



    player_1_r = player_1.get_x() + player_1.get_ancho()

    if ((player_1_r >= ball_l )):
        ball.invertir_velocidad_x()





    if ball.get_x() >= Config.SCREEN_WIDTH:
        ball.reiniciar_pos()
        ball.invertir_velocidad_x()
        ball.set_random_y_direction()
        player_1.aumentar_punto()

    if ball.get_x() <= 0 - 30:
        ball.reiniciar_pos()
        ball.invertir_velocidad_x()
        ball.set_random_y_direction()
        player_2.aumentar_punto()


    # print(f"Player 1:{player_1.get_puntos} player_2: {player_2.get_puntos}")

    delta_time = clock.tick(120) / 1000
    player_1.move(delta_time)
    player_2.move(delta_time)
    ball.move(delta_time)
    
    screen.fill(bg_color)
    player_1.draw()
    player_2.draw()
    ball.draw()

    font = pygame.font.SysFont(None, 110)
    img_player1_points = font.render(str(player_1.get_puntos()), True, "white")
    img_player2_points = font.render(str(player_2.get_puntos()), True, "white")
    screen.blit(img_player1_points, ((Config.SCREEN_WIDTH/2) - 60 ,30))
    screen.blit(img_player2_points, ((Config.SCREEN_WIDTH/2) + 60 ,30))

    pygame.display.flip()
    
    pygame.display.flip()

pygame.quit()
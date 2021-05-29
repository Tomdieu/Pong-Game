import pygame
from game import Game
import sys
from pygame.locals import *

pygame.init()

scr = pygame.display.set_mode((1300, 750))
pygame.display.set_caption("Pong Game")
run = True

game = Game(scr)

pause = True
running = False

fps = 120
clock = pygame.time.Clock()

one = 0

while run:
    scr.fill(pygame.Color('dodger blue'))
    game.player.draw()
    game.border(scr)
    game.ball.draw()
    game.opponent.draw()
    game.Player_Ball_Collision()
    game.opponent.move_ai()

    if one == 0:
        game.paused(scr, 'Ready?')
    elif pause == True and running == False:
        game.paused(scr, "Paused")

    if pause == False and running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game.player.move_up()
        if keys[pygame.K_DOWN]:
            game.player.move_down()
        game.ball.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.ball.reset()
                game.player.score = 0
                game.opponent.score = 0
            if event.key == pygame.K_SPACE:
                if pause == True and running == False:
                    pause = False
                    running = True
                    one = 1
                else:
                    pause = True
                    running = False
                    one = 1

    clock.tick(fps)
    # print('Fps = ', clock.get_fps(), 'Time = ', clock.get_time())
    # print('width = ',scr.get_width(),'height = ',scr.get_height())
    pygame.display.update()

pygame.quit()

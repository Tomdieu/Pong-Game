import pygame
from player import Player
from opponent import Opponent
from ball import Ball
import sys

pygame.init()


class Game(pygame.sprite.Sprite):
    system = sys.platform

    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.player = Player(surface)
        self.ball = Ball(surface, self.player)
        self.opponent = Opponent(surface, self.ball)

        self.score_font = ''
        self.pl_name = ''
        if Game.system == 'linux':
            self.score_font = pygame.font.SysFont('Ubuntu Condensed', 20)
            self.pl_name = pygame.font.SysFont('Ubuntu Condensed', 20)

    def border(self, surface):
        pygame.draw.line(surface, pygame.Color('white'), (surface.get_width() // 2 - 15, 0),
                         (surface.get_width() // 2 - 15, surface.get_height()), 10)
        pygame.draw.rect(surface, pygame.Color('orange'), (0, 0, surface.get_width(), surface.get_height()), 10)

        txt = "Player  Score : "
        img = self.score_font.render(txt + str(self.player.score), True, pygame.Color('white'))
        surface.blit(img, (60, 35))

        img2 = self.pl_name.render("Computer  Score : " + str(self.opponent.score), True, pygame.Color('white'))
        surface.blit(img2, (1100, 35))
        surface.blit(self.pl_name.render("Designer : Ivan Tom", True, pygame.Color('grey')),
                     (1100, surface.get_height() - 50))

    def paused(self, surface, info):
        if sys.platform == 'linux':
            font = pygame.font.SysFont("Ubuntu Condense", 60)
            txt = font.render(info, True, pygame.Color('white'))
            txt_rect = txt.get_rect(center=(self.surface.get_width() // 2,
                                            self.surface.get_height() // 2))
            surface.blit(txt, txt_rect)

    def Player_Ball_Collision(self):
        if self.player.rect.colliderect(self.ball.rect):
            if abs(self.ball.rect.left - self.player.rect.left) < 10:
                self.ball.x_velocity *= -1

            elif abs(self.ball.rect.top - self.player.rect.bottom) < 10 and self.ball.y_velocity > 0:
                self.ball.y_velocity *= -1
            elif abs(self.ball.rect.top - self.player.rect.bottom) < 10 and self.ball.y_velocity < 0:
                self.ball.y_velocity *= -1

        if self.ball.rect.x + self.ball.rect.width >= self.surface.get_width() - 10:
            self.player.score += 1
            self.ball.reset()
            print('hey = ',self.ball.rect.w)

        if self.ball.rect.x <= 10:
            self.opponent.score += 1
            self.ball.reset()

        #print( f'ball left = {self.ball.rect.right}  Opponent paddle = {self.opponent.rect.left} wall = {self.surface.get_width() - 10}')

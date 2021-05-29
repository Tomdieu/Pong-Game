import pygame
from ball import Ball

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.rect = pygame.Rect(10, 10, 10, 90)
        self.velocity = 4
        self.score = 0
        self.color = pygame.Color('orange')

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def move_up(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.y -= self.velocity

    def move_down(self):
        if self.rect.bottom >= self.surface.get_height():
            self.rect.bottom = self.surface.get_height()
        else:
            self.rect.y += self.velocity

import pygame
import random

pygame.init()


class Ball(pygame.sprite.Sprite):
    def __init__(self, surface, player):
        super(Ball, self).__init__()
        self.x_velocity = 3 * random.choice((-1, 1))
        self.y_velocity = 3 * random.choice((-1, 1))
        self.surface = surface
        self.rect = pygame.Rect(10, 10, 30, 30)
        self.color = pygame.Color('black')
        self.rect.x = surface.get_width() // 2 - self.rect.width
        self.rect.y = surface.get_height() // 2 - self.rect.height

    def move(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        if self.rect.left < 10 or self.rect.x + self.rect.width >= self.surface.get_width() - 10:
            self.x_velocity *= -1
        if self.rect.bottom > self.surface.get_height() - 10 or self.rect.top < 10:
            self.y_velocity *= -1

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.rect)

    def reset(self):
        self.rect.x = self.surface.get_width() // 2 - self.rect.width
        self.rect.y = self.surface.get_height() // 2 - self.rect.height

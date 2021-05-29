import pygame

pygame.init()


class Opponent(pygame.sprite.Sprite):
    def __init__(self, surface, ball):
        self.velocity = 1
        self.surface = surface
        self.score = 0
        self.velocity = 4
        self.color = pygame.Color('red')
        self.rect = pygame.Rect(surface.get_width() - 10, 10, 10, 90)
        self.rect.x = surface.get_width() - 20
        self.rect.y = 10
        self.ball = ball

    def move_ai(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.surface.get_height():
            self.rect.bottom = self.surface.get_height()
        if self.ball.rect.top < self.rect.top:
            self.rect.y -= self.velocity
        if self.ball.rect.bottom > self.rect.bottom:
            self.rect.y += self.velocity

        if self.ball.rect.colliderect(self.rect):
            self.ball.x_velocity *= -1
            """
            if abs(self.ball.rect.left - self.rect.left) < 5:
                self.ball.x_velocity *= -1
            elif abs(self.ball.rect.top - self.rect.bottom) < 5 and self.ball.y_velocity > 0:
                self.ball.y_velocity *= -1
            elif abs(self.ball.rect.top - self.rect.bottom) < 5 and self.ball.y_velocity < 0:
                self.ball.y_velocity *= -1
            """

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
